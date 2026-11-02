# Stage 5: pre-specified secondary analyses S1-S4, S6, S7 (S5 impact is in 06_s5_impact.R).
# usage: Rscript 05_secondary.R TASK CORES     TASK in s1 | s2 | s3 | s4 | s6 | s7
#   S1  CHIS primary + nativity (born outside US) + % life in US (tests H1b)        [jackknife replicate SEs]
#   S2  CHIS foreign-born only, primary + % life in US                               [jackknife replicate SEs]
#   S3  MGCFA by interview language: configural / full scalar / partial scalar (both surveys)
#   S4  anchor sensitivity: (a) one factor; (b) purified anchors; (c) one-at-a-time; (d) alignment (both surveys; c also CHIS+nativity)
#   S6  CHIS Spanish x web interaction on the target direct effects
#   S7  BRFSS 11 items, three-factor MIMIC
# Secondary analyses use lavaan weight-robust SEs unless stated.
args <- commandArgs(trailingOnly = TRUE)
source("/home/mo2273/ace_manuscript/scripts/common.R")
TASK <- args[1]; CORES <- as.integer(args[2])
OUT <- file.path(AN, "secondary"); dir.create(OUT, showWarnings = FALSE)
LOG <- file.path(OUT, sprintf("log_%s%s.txt", TASK, if (length(args) > 2) paste0("_", args[3]) else "")); if (file.exists(LOG)) file.remove(LOG)

eff_table <- function(fit, label, survey, pred = "sp") {
  e <- get_effects(fit, pred)
  e[, `:=`(analysis = label, survey = survey, OR_eq = exp(1.7 * est), OR_lo = exp(1.7 * ci.lower), OR_hi = exp(1.7 * ci.upper),
           se_type = "lavaan weight-robust")]
  e
}
with_rep <- function(fit, model, d, repw, ordered, label, survey, scl = 1, rsc = 1) {
  M <- rep_refit(model, d, repw, ordered, fit, cores = CORES)
  th0 <- coef(fit); se <- rep_se(M, th0, scl, rsc, TRUE)
  pt <- as.data.table(parTable(fit))
  k <- pt[op == "~" & rhs == "sp", .(lhs, rhs, free)]
  k[, `:=`(est = th0[free], se = se[free])]
  k[, `:=`(z = est / se, pvalue = 2 * pnorm(-abs(est / se)), ci.lower = est - 1.96 * se, ci.upper = est + 1.96 * se)]
  k[, `:=`(analysis = label, survey = survey, OR_eq = exp(1.7 * est), OR_lo = exp(1.7 * ci.lower), OR_hi = exp(1.7 * ci.upper),
           se_type = sprintf("jackknife replicate (%d/%d converged)", attr(M, "n_ok"), attr(M, "n_rep")))]
  k[, free := NULL]
  list(eff = k, M = M)
}

# ------------------------------------------------------------------ S1 / S2 (CHIS)
if (TASK %in% c("s1", "s2")) {
  C <- load_chis()
  if (TASK == "s1") { d <- C$d; cov <- c(C$cov, C$nat); lab <- "S1 CHIS + nativity, % life in US" }
  else { d <- C$d[fb == 1]; cov <- c(C$cov, C$pct); lab <- "S2 CHIS foreign-born only + % life in US" }
  keep <- cov[vapply(cov, function(v) length(unique(d[[v]])) > 1, TRUE)]
  if (length(keep) < length(cov)) logf(LOG, "dropped constant covariates: ", paste(setdiff(cov, keep), collapse = ", "))
  model <- mimic_syntax(F2, keep)
  fit <- fit_wlsmv(model, d, "w", ITEMS8)
  logf(LOG, lab, ": n = ", nrow(d), " (Spanish ", sum(d$sp), "), converged = ", lavInspect(fit, "converged"))
  saveRDS(fit, file.path(OUT, sprintf("fit_%s.rds", TASK)))
  fwrite(as.data.table(parameterEstimates(fit)), file.path(OUT, sprintf("params_%s.csv", TASK)))
  rob <- eff_table(fit, lab, "CHIS")
  rr <- with_rep(fit, model, d, chis_repw(d), ITEMS8, lab, "CHIS")
  saveRDS(rr$M, file.path(OUT, sprintf("repcoef_%s.rds", TASK)))
  pdf0 <- implied_pdiff(fit, d, "w", F2)
  eff <- merge(rr$eff, rob[, .(lhs, se_lavaan = se)], by = "lhs")
  eff <- merge(eff, pdf0, by.x = "lhs", by.y = "item", all.x = TRUE)
  eff[, `:=`(n = nrow(d), n_spanish = sum(d$sp))]
  fwrite(eff, file.path(OUT, sprintf("effects_%s.csv", TASK)))
  write_json(fit_indices(fit), file.path(OUT, sprintf("fit_indices_%s.json", TASK)), auto_unbox = TRUE, digits = 6)
  print(eff[, .(lhs, est = round(est, 3), se = round(se, 3), se_lavaan = round(se_lavaan, 3), p = signif(pvalue, 3), OR_eq = round(OR_eq, 2))])
  if (TASK == "s1") {
    tg <- eff[lhs %in% TARGETS]
    h1b <- all(tg$est < 0 & tg$pvalue < 0.05)
    logf(LOG, "H1b (all three CHIS direct effects < 0 with p < .05 after nativity + % life in US): ", if (h1b) "SUPPORTED" else "NOT SUPPORTED")
    write_json(list(H1b_supported = h1b, per_item = tg[, .(lhs, est, se, pvalue)]), file.path(OUT, "h1b_verdict.json"), auto_unbox = TRUE, digits = 6)
  }
  status(sprintf("Stage 5 %s done (replicate SEs): analysis/secondary/effects_%s.csv", toupper(TASK), TASK))
}

# ------------------------------------------------------------------ S3 MGCFA by interview language
if (TASK == "s3") {
  res <- list(); lrt <- list(); sc <- list(); lm <- list()
  # Explicit labelled syntax (group.equal = "thresholds" was silently not applied in lavaan 0.7.2 here: scalar df = 44, latent
  # means stayed fixed). Binary items, theta: residual variances fixed at 1 in both groups. Configural: latent means 0 and
  # variances 1 in both groups. Scalar: loadings + thresholds equal; Spanish latent means/variances free.
  # Partial: as scalar but loading + threshold of the 3 target items free in the Spanish group. Expected df 38 / 50 / 44.
  mg_syntax <- function(type) {
    eqf <- function(j) type == "scalar" || (type == "partial" && !(j %in% TARGETS))
    s <- vapply(names(F2), function(Fn) sprintf("%s =~ %s", Fn, paste(vapply(F2[[Fn]], function(j)
      if (eqf(j)) sprintf("c(l_%s, l_%s)*%s", j, j, j) else sprintf("c(l_%s_E, l_%s_S)*%s", j, j, j), ""), collapse = " + ")), "")
    for (j in ITEMS8) {
      s <- c(s, if (eqf(j)) sprintf("%s | c(t_%s, t_%s)*t1", j, j, j) else sprintf("%s | c(t_%s_E, t_%s_S)*t1", j, j, j),
             sprintf("%s ~~ c(1, 1)*%s", j, j))
    }
    s <- c(s, if (type == "configural") c("HD ~~ c(1, 1)*HD", "AB ~~ c(1, 1)*AB", "HD ~ c(0, 0)*1", "AB ~ c(0, 0)*1")
              else c("HD ~~ c(1, NA)*HD", "AB ~~ c(1, NA)*AB", "HD ~ c(0, NA)*1", "AB ~ c(0, NA)*1"), "HD ~~ AB")
    paste(s, collapse = "\n")
  }
  for (SV in c("brfss", "chis")) {
    L <- if (SV == "brfss") load_brfss() else load_chis(); d <- L$d
    d[, lang := fifelse(sp == 1, "Spanish", "English")]
    g <- function(type) cfa(mg_syntax(type), data = d, ordered = ITEMS8, estimator = "WLSMV", parameterization = "theta",
                            sampling.weights = "w", std.lv = TRUE, group = "lang", group.label = c("English", "Spanish"))
    fc <- g("configural"); fs <- g("scalar"); fp <- g("partial")
    dfs <- vapply(list(fc, fs, fp), function(f) fitMeasures(f, "df"), 0)
    logf(LOG, SV, " S3 df configural/scalar/partial = ", paste(dfs, collapse = "/"), " (expected 38/50/44)")
    stopifnot(all(dfs == c(38, 50, 44)))
    saveRDS(list(configural = fc, scalar = fs, partial = fp), file.path(OUT, sprintf("fit_s3_%s.rds", SV)))
    for (nm in c("configural", "scalar", "partial")) {
      f <- list(configural = fc, scalar = fs, partial = fp)[[nm]]
      res[[length(res) + 1]] <- data.table(survey = toupper(SV), model = nm, converged = lavInspect(f, "converged"), t(unlist(fit_indices(f))))
    }
    cmp <- function(a, b, lab) {
      t <- tryCatch(as.data.frame(lavTestLRT(a, b)), error = function(e) NULL)
      if (is.null(t)) return(NULL)
      fa <- fitMeasures(a, c("cfi.scaled", "rmsea.scaled")); fb <- fitMeasures(b, c("cfi.scaled", "rmsea.scaled"))
      data.table(survey = toupper(SV), comparison = lab, chisq_diff = t[2, "Chisq diff"], df_diff = t[2, "Df diff"], p = t[2, "Pr(>Chisq)"],
                 method = attr(lavTestLRT(a, b), "heading")[1], dCFI = fb[1] - fa[1], dRMSEA = fb[2] - fa[2])
    }
    lrt[[length(lrt) + 1]] <- cmp(fc, fs, "configural vs full scalar")
    lrt[[length(lrt) + 1]] <- cmp(fc, fp, "configural vs partial scalar (targets free)")
    lrt[[length(lrt) + 1]] <- cmp(fp, fs, "partial scalar vs full scalar")
    for (nm in c("scalar", "partial")) {
      f <- list(scalar = fs, partial = fp)[[nm]]
      pe <- as.data.table(parameterEstimates(f))
      lm[[length(lm) + 1]] <- pe[op == "~1" & lhs %in% names(F2) & group == 2, .(survey = toupper(SV), model = nm, factor = lhs, est, se, pvalue, ci.lower, ci.upper)]
    }
    # score tests on the full scalar model: which equality constraints are most violated (no reference to H1)
    st <- lavTestScore(fs)$uni
    pt <- as.data.table(parTable(fs))
    pl <- pt[plabel != "", .(plabel, par = paste0(lhs, op, rhs))]
    st <- as.data.table(st)
    st[, par := pl$par[match(lhs, pl$plabel)]]
    st[, survey := toupper(SV)]
    sc[[length(sc) + 1]] <- st[order(-X2)]
    logf(LOG, SV, " S3 done")
  }
  fwrite(rbindlist(res, fill = TRUE), file.path(OUT, "s3_fit.csv"))
  fwrite(rbindlist(lrt), file.path(OUT, "s3_difftests.csv"))
  fwrite(rbindlist(lm), file.path(OUT, "s3_latent_means.csv"))
  fwrite(rbindlist(sc), file.path(OUT, "s3_score_tests.csv"))
  print(rbindlist(res, fill = TRUE)); print(rbindlist(lrt)); print(rbindlist(lm)); print(rbindlist(sc)[, head(.SD, 8), by = survey])
  status("Stage 5 S3 MGCFA done: analysis/secondary/s3_fit.csv, s3_difftests.csv, s3_latent_means.csv, s3_score_tests.csv")
}

# ------------------------------------------------------------------ S4 anchor sensitivity
if (TASK == "s4") {
  # one specification per call (run in parallel): args[3] in brfss | chis | chisnat ; then TASK s4combine merges the parts
  out <- list(); hist <- list()
  specs <- list(brfss = list(sv = "brfss", nat = FALSE, lab = "BRFSS"), chis = list(sv = "chis", nat = FALSE, lab = "CHIS"),
                chisnat = list(sv = "chis", nat = TRUE, lab = "CHIS + nativity"))
  SPEC <- args[3]; specs <- specs[SPEC]
  for (sp_ in specs) {
    L <- if (sp_$sv == "brfss") load_brfss() else load_chis(); d <- L$d
    cov <- if (sp_$nat) c(L$cov, L$nat) else L$cov
    # (c) each non-target item freed one at a time (targets also free, as in the primary model)
    fits_c <- mclapply(NONTARGET, function(k) fit_wlsmv(mimic_syntax(F2, cov, direct = c(TARGETS, k)), d, "w", ITEMS8), mc.cores = min(CORES, 5))
    names(fits_c) <- NONTARGET
    for (k in NONTARGET) {
      e <- eff_table(fits_c[[k]], "S4c one-at-a-time", sp_$lab)[lhs == k]
      out[[length(out) + 1]] <- e
    }
    logf(LOG, sp_$lab, " S4c done")
    if (sp_$nat) next     # (a), (b), (d) for the two primary specifications only
    # (a) one-factor model, all 5 non-target items as anchors
    fa <- fit_wlsmv(mimic_syntax(list(ACE = ITEMS8), cov), d, "w", ITEMS8)
    out[[length(out) + 1]] <- eff_table(fa, "S4a one factor", sp_$lab)
    write_json(fit_indices(fa), file.path(OUT, sprintf("fit_indices_s4a_%s.json", sp_$sv)), auto_unbox = TRUE, digits = 6)
    # (b) purified anchors: iteratively free the non-target item with the largest |b| among those with p < .01 and |b| >= 0.24
    #     (one item per iteration; at least one anchor kept per factor); iteration 1 = the S4c fits.
    freed <- character(0); it <- 1; cur <- fits_c
    repeat {
      cand <- rbindlist(lapply(names(cur), function(k) { e <- get_effects(cur[[k]])[lhs == k]; e[, item := k]; e }))
      cand[, flag := pvalue < 0.01 & abs(est) >= 0.24]
      # identification: an item may be freed only if its factor keeps >= 1 anchor
      cand[, ok_id := vapply(item, function(k) { Fk <- names(F2)[vapply(F2, function(v) k %in% v, TRUE)]
        length(setdiff(F2[[Fk]], c(TARGETS, freed, k))) >= 1 }, TRUE)]
      hist[[length(hist) + 1]] <- cand[, .(survey = sp_$lab, iteration = it, already_freed = paste(freed, collapse = "+"), item, est, se, pvalue, flag, ok_id)]
      sel <- cand[flag & ok_id][order(-abs(est))]
      if (!nrow(sel)) break
      freed <- c(freed, sel$item[1]); it <- it + 1
      rest <- setdiff(NONTARGET, freed)
      cur <- mclapply(rest, function(k) fit_wlsmv(mimic_syntax(F2, cov, direct = c(TARGETS, freed, k)), d, "w", ITEMS8), mc.cores = min(CORES, 5))
      names(cur) <- rest
      if (!length(rest)) break
    }
    fb_ <- fit_wlsmv(mimic_syntax(F2, cov, direct = c(TARGETS, freed)), d, "w", ITEMS8)
    eb <- eff_table(fb_, sprintf("S4b purified anchors (freed: %s)", if (length(freed)) paste(freed, collapse = "+") else "none"), sp_$lab)
    out[[length(out) + 1]] <- eb
    logf(LOG, sp_$lab, " S4a/S4b done; purification freed: ", paste(freed, collapse = ", "))
    # (d) alignment (anchor-free check): configural 2-group CFA (no covariates) -> sirt::invariance.alignment per factor
    if (requireNamespace("sirt", quietly = TRUE)) {
      d[, lang := fifelse(sp == 1, "Spanish", "English")]
      m2 <- paste(sprintf("%s =~ %s", names(F2), vapply(F2, paste, "", collapse = " + ")), collapse = "\n")
      fc <- cfa(paste0(m2, "\nHD ~~ AB"), data = d, ordered = ITEMS8, estimator = "WLSMV", parameterization = "theta", sampling.weights = "w",
                std.lv = TRUE, group = "lang", group.label = c("English", "Spanish"))
      pe <- as.data.table(parameterEstimates(fc))
      wgt <- matrix(c(sum(d$sp == 0), sum(d$sp == 1)), nrow = 2, ncol = 1)
      for (Fn in names(F2)) {
        its <- F2[[Fn]]
        lam <- t(sapply(1:2, function(gi) pe[op == "=~" & lhs == Fn & group == gi][match(its, rhs), est]))
        nu <- t(sapply(1:2, function(gi) -pe[op == "|" & group == gi][match(its, lhs), est]))
        dimnames(lam) <- dimnames(nu) <- list(c("English", "Spanish"), its)
        al <- tryCatch(sirt::invariance.alignment(lambda = lam, nu = nu, wgt = wgt[, rep(1, length(its)), drop = FALSE], optimizer = "optim"),
                       error = function(e) { logf(LOG, "alignment error: ", conditionMessage(e)); NULL })
        if (is.null(al)) next
        nu_al <- al$nu.aligned; lam_al <- al$lambda.aligned
        hist[[length(hist) + 1]] <- data.table(survey = sp_$lab, iteration = NA, already_freed = paste0("ALIGNMENT ", Fn), item = its,
                                               est = nu_al[2, ] - nu_al[1, ], se = NA_real_, pvalue = NA_real_, flag = NA, ok_id = NA)
        fwrite(data.table(survey = sp_$lab, factor = Fn, item = its, lambda_En = lam_al[1, ], lambda_Sp = lam_al[2, ],
                          nu_En = nu_al[1, ], nu_Sp = nu_al[2, ], nu_diff_Sp_minus_En = nu_al[2, ] - nu_al[1, ],
                          aligned_mean_Sp = al$pars$alpha0[2], aligned_sd_Sp = al$pars$psi0[2],
                          R2_lambda = al$es.invariance["R2", "loadings"], R2_nu = al$es.invariance["R2", "intercepts"]),
               file.path(OUT, sprintf("s4d_alignment_%s_%s.csv", sp_$sv, Fn)))
        logf(LOG, sp_$lab, " S4d alignment ", Fn, ": Spanish mean ", round(al$pars$alpha0[2], 3), "; nu diffs ",
             paste(its, round(nu_al[2, ] - nu_al[1, ], 3), collapse = "; "))
      }
    } else logf(LOG, "sirt not available: S4d alignment skipped")
  }
  saveRDS(list(out = out, hist = hist), file.path(OUT, sprintf("s4_part_%s.rds", SPEC)))
  logf(LOG, "part saved: ", SPEC)
}
if (TASK == "s4combine") {
  parts <- lapply(c("brfss", "chis", "chisnat"), function(k) readRDS(file.path(OUT, sprintf("s4_part_%s.rds", k))))
  E <- rbindlist(lapply(parts, function(p) rbindlist(p$out, fill = TRUE)), fill = TRUE); fwrite(E, file.path(OUT, "s4_effects.csv"))
  fwrite(rbindlist(lapply(parts, function(p) rbindlist(p$hist, fill = TRUE)), fill = TRUE), file.path(OUT, "s4b_purification_history.csv"))
  print(E[, .(analysis, survey, lhs, est = round(est, 3), se = round(se, 3), p = signif(pvalue, 3), OR = round(OR_eq, 2))])
  status("Stage 5 S4 anchor sensitivity done: analysis/secondary/s4_effects.csv, s4b_purification_history.csv, s4d_alignment_*.csv")
}

# ------------------------------------------------------------------ S6 mode (CHIS)
if (TASK == "s6") {
  C <- load_chis(); d <- C$d
  pred <- c("sp", "web", "spweb")
  extra <- sprintf("web_%s := d1_%s + d3_%s", TARGETS, TARGETS, TARGETS)
  model <- mimic_syntax(F2, C$cov, direct = TARGETS, pred = pred, extra = extra)
  fit <- fit_wlsmv(model, d, "w", ITEMS8)
  saveRDS(fit, file.path(OUT, "fit_s6.rds"))
  pe <- as.data.table(parameterEstimates(fit))
  e <- rbind(pe[op == "~" & lhs %in% TARGETS & rhs == "sp", .(item = lhs, term = "Spanish direct effect, phone", est, se, pvalue, ci.lower, ci.upper)],
             pe[op == ":=", .(item = sub("web_", "", lhs), term = "Spanish direct effect, web", est, se, pvalue, ci.lower, ci.upper)],
             pe[op == "~" & lhs %in% TARGETS & rhs == "spweb", .(item = lhs, term = "Spanish x web interaction", est, se, pvalue, ci.lower, ci.upper)],
             pe[op == "~" & lhs %in% TARGETS & rhs == "web", .(item = lhs, term = "Web direct effect (English)", est, se, pvalue, ci.lower, ci.upper)],
             pe[op == "~" & lhs %in% names(F2) & rhs %in% pred, .(item = lhs, term = paste0("factor ~ ", rhs), est, se, pvalue, ci.lower, ci.upper)])
  e[, `:=`(OR_eq = exp(1.7 * est), OR_lo = exp(1.7 * ci.lower), OR_hi = exp(1.7 * ci.upper), se_type = "lavaan weight-robust")]
  fwrite(e, file.path(OUT, "s6_mode.csv")); print(e)
  write_json(fit_indices(fit), file.path(OUT, "fit_indices_s6.json"), auto_unbox = TRUE, digits = 6)
  status("Stage 5 S6 mode interaction done: analysis/secondary/s6_mode.csv")
}

# ------------------------------------------------------------------ S7 BRFSS 11 items
if (TASK == "s7") {
  B <- load_brfss(); d <- B$d
  F3 <- list(HD = HD, AB = AB, SX = SX)
  model <- mimic_syntax(F3, B$cov)
  fit <- fit_wlsmv(model, d, "w", c(ITEMS8, SX))
  saveRDS(fit, file.path(OUT, "fit_s7.rds"))
  e <- eff_table(fit, "S7 BRFSS 11 items, 3 factors", "BRFSS")
  pdf0 <- implied_pdiff(fit, d, "w", F3)
  e <- merge(e, pdf0, by.x = "lhs", by.y = "item", all.x = TRUE)
  fwrite(e, file.path(OUT, "s7_effects.csv")); print(e)
  write_json(fit_indices(fit), file.path(OUT, "fit_indices_s7.json"), auto_unbox = TRUE, digits = 6)
  status("Stage 5 S7 BRFSS 11-item MIMIC done: analysis/secondary/s7_effects.csv")
}
