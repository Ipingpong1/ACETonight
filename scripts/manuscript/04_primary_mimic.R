# Stage 4 (part a): PRIMARY MIMIC per plan, one survey per call, with design-based replicate variance.
# usage: Rscript 04_primary_mimic.R brfss|chis CORES
#   model: HD =~ mh+drink+drugs+jail+divorce ; AB =~ ipv+phys+verbal ; HD, AB ~ sp + covariates ;
#          direct effects sp -> mh, drugs, jail ; anchors = all other items. WLSMV, theta, survey weights.
#   variance: CHIS 80 jackknife (rakedw1-80/5; scale 1, rscales 1, MSE); BRFSS 100 Rao-Wu subbootstrap replicates.
args <- commandArgs(trailingOnly = TRUE)
source("/home/mo2273/ace_manuscript/scripts/common.R")
SV <- args[1]; CORES <- as.integer(args[2])
OUT <- file.path(AN, "primary"); dir.create(OUT, showWarnings = FALSE)
LOG <- file.path(OUT, sprintf("log_%s.txt", SV)); if (file.exists(LOG)) file.remove(LOG)

if (SV == "brfss") {
  L <- load_brfss(); d <- L$d
  bw <- brfss_repw(d, R = 100)
  repw <- bw$W; scl <- bw$scale; rsc <- bw$rscales; vtype <- "Rao-Wu rescaled bootstrap (subbootstrap), 100 replicates, MSE"
} else {
  L <- load_chis(); d <- L$d
  repw <- chis_repw(d); scl <- 1; rsc <- 1; vtype <- "Jackknife, 80 replicates (rakedw1-80), scale 1, rscales 1, MSE"
}
model <- mimic_syntax(F2, L$cov)
writeLines(model, file.path(OUT, sprintf("model_%s.lav", SV)))
t0 <- Sys.time()
fit <- fit_wlsmv(model, d, "w", ITEMS8)
logf(LOG, SV, ": full-sample fit converged = ", lavInspect(fit, "converged"), " (", round(difftime(Sys.time(), t0, units = "secs")), " s)")
saveRDS(fit, file.path(OUT, sprintf("fit_%s.rds", SV)))
pe <- as.data.table(parameterEstimates(fit)); fwrite(pe, file.path(OUT, sprintf("params_%s.csv", SV)))
fi <- fit_indices(fit); write_json(fi, file.path(OUT, sprintf("fit_indices_%s.json", SV)), auto_unbox = TRUE, digits = 6)
logf(LOG, "fit indices: ", paste(names(fi), unlist(fi), sep = "=", collapse = "; "))

# ---- replicate refits ----
t0 <- Sys.time()
M <- rep_refit(model, d, repw, ITEMS8, fit, cores = CORES)
logf(LOG, "replicates: ", attr(M, "n_ok"), "/", attr(M, "n_rep"), " converged (", round(difftime(Sys.time(), t0, units = "mins"), 1), " min); ", vtype)
saveRDS(list(M = M, scale = scl, rscales = rsc, theta0 = coef(fit)), file.path(OUT, sprintf("repcoef_%s.rds", SV)))
th0 <- coef(fit)
se_all <- rep_se(M, th0, scl, rsc, mse = TRUE)

# ---- effects of interest: direct effects (targets) + language -> factor ----
pt <- as.data.table(parTable(fit))
key <- pt[op == "~" & rhs == "sp", .(lhs, rhs, free)]
key[, est := th0[free]]; key[, se_rep := se_all[free]]
key <- merge(key, pe[op == "~" & rhs == "sp", .(lhs, se_lavaan = se)], by = "lhs")
key[, `:=`(z = est / se_rep, p = 2 * pnorm(-abs(est / se_rep)), ci_lo = est - 1.96 * se_rep, ci_hi = est + 1.96 * se_rep)]
key[, type := fifelse(lhs %in% c("HD", "AB"), "language -> factor", "direct effect (uniform DIF)")]
key[type != "language -> factor", `:=`(OR_eq = exp(1.7 * est), OR_lo = exp(1.7 * ci_lo), OR_hi = exp(1.7 * ci_hi))]

# ---- model-implied probability differences (Spanish respondents, with vs without direct effect), with replicate SE ----
pdf0 <- implied_pdiff(fit, d, "w", F2)
pd_from_coef <- function(cvec, wvec) {
  p <- copy(pt); idx <- which(p$free > 0); p$est[idx] <- cvec[p$free[idx]]
  m <- d$sp == 1
  sapply(TARGETS, function(it) {
    ip <- item_pars(p, it, F2); eta <- eta_hat(p, ip$F, d)[m]
    sdv <- sqrt(ip$lambda^2 * ip$psi + ip$theta); b <- ip$direct[rhs == "sp", est]
    100 * weighted.mean(pnorm((ip$lambda * eta + b - ip$tau) / sdv) - pnorm((ip$lambda * eta - ip$tau) / sdv), wvec[m])
  })
}
# map replicate rows of M back to replicate columns (rep_refit drops non-converged; keep order of converged)
conv_idx <- as.integer(rownames(M)); if (anyNA(conv_idx) || length(conv_idx) != nrow(M)) conv_idx <- seq_len(nrow(M))
PD <- t(vapply(seq_len(nrow(M)), function(i) pd_from_coef(M[i, ], repw[, conv_idx[i]]), numeric(3)))
pd0 <- setNames(pdf0$pdiff_pp, pdf0$item)
pd_se <- sqrt(scl * colSums(rsc * sweep(PD, 2, pd0[colnames(PD)])^2))
pdf0[, `:=`(pdiff_se_rep = pd_se[item], pdiff_lo = pdiff_pp - 1.96 * pd_se[item], pdiff_hi = pdiff_pp + 1.96 * pd_se[item])]
key <- merge(key, pdf0, by.x = "lhs", by.y = "item", all.x = TRUE)
key[, survey := toupper(SV)]; key[, variance := vtype]; key[, n_rep_ok := attr(M, "n_ok")]
key[, `:=`(n = nrow(d), n_spanish = sum(d$sp))]
setcolorder(key, c("survey", "type", "lhs", "rhs"))
fwrite(key, file.path(OUT, sprintf("effects_%s.csv", SV)))
print(key[, .(lhs, est = round(est, 3), se_rep = round(se_rep, 3), se_lavaan = round(se_lavaan, 3), p = signif(p, 3),
              OR_eq = round(OR_eq, 2), pdiff_pp = round(pdiff_pp, 2))])
logf(LOG, "done ", SV)
status(sprintf("Stage 4 primary MIMIC %s: fitted + %d/%d replicates; outputs analysis/primary/effects_%s.csv, params_%s.csv, fit_indices_%s.json",
               toupper(SV), attr(M, "n_ok"), attr(M, "n_rep"), SV, SV, SV))
