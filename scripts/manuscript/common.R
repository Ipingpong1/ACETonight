# common.R -- shared helpers for the H1 confirmatory analysis (sourced by every stage script).
# Plan: /home/mo2273/ace_manuscript/prereg/H1_analysis_plan.md (frozen; SHA-256 in H1_analysis_plan.sha256.txt)
suppressPackageStartupMessages({
  library(data.table); library(lavaan); library(survey); library(jsonlite); library(parallel)
})
options(survey.lonely.psu = "adjust", width = 200)
ROOT <- "/home/mo2273/ace_manuscript"
AN <- file.path(ROOT, "analysis"); FIG <- file.path(ROOT, "figures"); DAT <- file.path(AN, "data")
dir.create(DAT, showWarnings = FALSE, recursive = TRUE)

ITEMS8 <- c("mh", "drink", "drugs", "jail", "divorce", "ipv", "phys", "verbal")
TARGETS <- c("mh", "drugs", "jail")
NONTARGET <- setdiff(ITEMS8, TARGETS)
HD <- c("mh", "drink", "drugs", "jail", "divorce")   # household dysfunction (Ford 2014)
AB <- c("ipv", "phys", "verbal")                     # physical/emotional abuse (Ford 2014: witnessed DV loads here)
SX <- c("touch", "tthem", "hvsex")                   # BRFSS-only sexual abuse
F2 <- list(HD = HD, AB = AB)
LAB <- c(mh = "Household mental illness", drink = "Household problem drinking", drugs = "Household drug use",
         jail = "Household incarceration", divorce = "Parental separation/divorce",
         ipv = "Witnessed parental violence", phys = "Physical abuse", verbal = "Verbal abuse",
         touch = "Sexual abuse: touched", tthem = "Sexual abuse: made to touch", hvsex = "Sexual abuse: forced sex",
         ace4 = "4+ ACEs (standard 8-category score)")
NCORES <- 10

status <- function(msg) {
  cat(sprintf("- %s UTC: %s\n", format(Sys.time(), "%Y-%m-%d %H:%M", tz = "UTC"), msg),
      file = file.path(AN, "STATUS.md"), append = TRUE)
}
logf <- function(file, ...) { s <- paste0(...); cat(s, "\n"); cat(s, "\n", file = file, append = TRUE) }

# numeric 0/1 dummies for a categorical column (reference = ref); returns the new column names
dummies <- function(d, var, prefix, ref) {
  lev <- setdiff(sort(unique(d[[var]])), ref)
  nm <- paste0(prefix, lev)
  for (i in seq_along(lev)) set(d, j = nm[i], value = as.numeric(d[[var]] == lev[i]))
  nm
}

# BRFSS: covariates per plan = age group, sex, education, income (missing as category), survey year, Census region
load_brfss <- function() {
  d <- copy(readRDS(file.path(DAT, "brfss_analytic.rds")))
  cov <- c(dummies(d, "agecat", "age", 1), dummies(d, "educ", "edu", 4), dummies(d, "sex", "fem", 1),
           dummies(d, "inc", "inc", 5), dummies(d, "year", "y", 2019), dummies(d, "region", "reg", 3))
  list(d = d, cov = cov, w = "w")
}
# CHIS: covariates per plan = age group, sex, education, poverty level, survey year
load_chis <- function() {
  d <- copy(readRDS(file.path(DAT, "chis_analytic.rds")))
  cov <- c(dummies(d, "agecat", "age", 18), dummies(d, "educ", "edu", 3), dummies(d, "sex", "fem", 1),
           dummies(d, "pov", "pov", 4), dummies(d, "year", "y", 2021))
  nat <- c("fb", dummies(d, "pctlf", "pctlf", 5))   # S1 additions: foreign-born + % life in US
  pct <- dummies(d, "pctlf", "pctlf", 5)
  list(d = d, cov = cov, nat = nat, pct = pct, w = "w")
}

# ---------- model syntax ----------
# factors: named list; covs: covariate columns for the factor regressions; direct: items with direct effects of `pred`
mimic_syntax <- function(factors, covs, direct = TARGETS, pred = "sp", extra = NULL) {
  s <- sprintf("%s =~ %s", names(factors), vapply(factors, paste, "", collapse = " + "))
  s <- c(s, sprintf("%s ~ %s", names(factors), paste(c(pred, covs), collapse = " + ")))
  for (it in direct) s <- c(s, sprintf("%s ~ %s", it, paste(sprintf("d%s_%s*%s", seq_along(pred), it, pred), collapse = " + ")))
  if (length(factors) > 1) {
    cb <- combn(names(factors), 2)
    s <- c(s, sprintf("%s ~~ %s", cb[1, ], cb[2, ]))
  }
  paste(c(s, extra), collapse = "\n")
}

fit_wlsmv <- function(model, data, w, ordered, se = "robust.sem", test = "scaled.shifted", start = "default", ...) {
  sem(model, data = data, ordered = ordered, estimator = "WLSMV", parameterization = "theta",
      sampling.weights = w, std.lv = TRUE, se = se, test = test, start = start, ...)
}

FITIDX <- c("chisq.scaled", "df.scaled", "pvalue.scaled", "cfi.scaled", "tli.scaled", "rmsea.scaled",
            "cfi.robust", "tli.robust", "rmsea.robust", "srmr")
fit_indices <- function(fit) {
  fm <- tryCatch(fitMeasures(fit, FITIDX), error = function(e) fitMeasures(fit, intersect(FITIDX, names(fitMeasures(fit)))))
  as.list(round(fm, 4))
}

# direct effects of `pred` on items + pred -> factor effects (point est, lavaan robust SE)
get_effects <- function(fit, pred = "sp") {
  pe <- as.data.table(parameterEstimates(fit))
  pe[op == "~" & rhs == pred, .(lhs, rhs, est, se, z, pvalue, ci.lower, ci.upper)]
}

# ---------- model-implied endorsement probabilities ----------
# P(y_j = 1 | x) = Phi((lambda_j * Gamma_F'x + sum_k b_jk*pred_k - tau_j) / sqrt(lambda_j^2 psi_F + theta_j)), theta param.
item_pars <- function(pe, item, factors) {
  F <- names(factors)[vapply(factors, function(v) item %in% v, TRUE)]
  list(F = F,
       lambda = pe[op == "=~" & lhs == F & rhs == item, est],
       tau = pe[op == "|" & lhs == item, est],
       theta = pe[op == "~~" & lhs == item & rhs == item, est],
       psi = pe[op == "~~" & lhs == F & rhs == F, est],
       direct = pe[op == "~" & lhs == item, .(rhs, est)])
}
eta_hat <- function(pe, F, data) {
  g <- pe[op == "~" & lhs == F]
  as.vector(as.matrix(data[, g$rhs, with = FALSE]) %*% g$est)
}
# average (weighted, among Spanish-interview respondents) model-implied probability with vs without the sp direct effect
implied_pdiff <- function(fit, data, wcol, factors, items = TARGETS, pred = "sp") {
  pe <- as.data.table(parameterEstimates(fit, se = FALSE))
  m <- data[[pred]] == 1; w <- data[[wcol]][m]
  rbindlist(lapply(items, function(it) {
    ip <- item_pars(pe, it, factors)
    eta <- eta_hat(pe, ip$F, data)[m]
    sdv <- sqrt(ip$lambda^2 * ip$psi + ip$theta)
    b <- ip$direct[rhs == pred, est]
    p1 <- pnorm((ip$lambda * eta + b - ip$tau) / sdv); p0 <- pnorm((ip$lambda * eta - ip$tau) / sdv)
    data.table(item = it, p_with = weighted.mean(p1, w), p_without = weighted.mean(p0, w),
               pdiff_pp = 100 * weighted.mean(p1 - p0, w))
  }))
}

# ---------- replicate refits ----------
# repw: matrix (n x R) of replicate analysis weights aligned with data rows; returns matrix R x p of coef()
rep_refit <- function(model, data, repw, ordered, start_fit, cores = NCORES) {
  res <- mclapply(seq_len(ncol(repw)), function(r) {
    dd <- copy(data); dd[, .rw := repw[, r]]; dd <- dd[.rw > 0]
    f <- tryCatch(suppressWarnings(fit_wlsmv(model, dd, ".rw", ordered, se = "none", test = "none", start = start_fit)),
                  error = function(e) NULL)
    if (is.null(f) || !isTRUE(lavInspect(f, "converged"))) return(NULL)
    coef(f)
  }, mc.cores = cores, mc.preschedule = FALSE)
  ok <- !vapply(res, is.null, TRUE)
  M <- do.call(rbind, res[ok]); rownames(M) <- which(ok)
  attr(M, "n_ok") <- sum(ok); attr(M, "n_rep") <- ncol(repw)
  M
}
# replicate variance: scale * sum(rscales * (theta_r - centre)^2), centre = full-sample estimate if mse
rep_se <- function(M, theta0, scale, rscales = 1, mse = TRUE) {
  ctr <- if (mse) theta0 else colMeans(M)
  D <- sweep(M, 2, ctr[colnames(M)])
  sqrt(scale * colSums(rscales * D^2))
}

# replicate weights: CHIS jackknife (rakedw1-80 / 5, type other, scale 1, rscales 1, mse) ; BRFSS Rao-Wu subbootstrap
chis_repw <- function(d) as.matrix(d[, paste0("w", 1:80), with = FALSE])
brfss_repw <- function(d, R = 100, seed = 20261102) {
  f <- file.path(DAT, sprintf("brfss_boot%d_weights.rds", R))
  if (file.exists(f)) return(readRDS(f))
  # integer IDs: survey's subbootweights calls unique()/factor() per stratum x replicate, which is O(#levels) when the
  # PSU id is a factor with ~35k levels (hours for R = 100); integer ids give the identical algorithm in seconds.
  # PSU ids are made unique within (collapsed) stratum, i.e. the same semantics as nest = TRUE.
  dd <- data.frame(w = d$w, sb = as.integer(factor(d$strat_boot)), pid = as.integer(factor(paste(d$strat_boot, d$psu))))
  set.seed(seed)
  des <- svydesign(ids = ~pid, strata = ~sb, weights = ~w, data = dd, nest = FALSE)
  rd <- as.svrepdesign(des, type = "subbootstrap", replicates = R, mse = TRUE)
  out <- list(W = weights(rd, type = "analysis"), scale = rd$scale, rscales = rd$rscales, mse = rd$mse)
  saveRDS(out, f)
  out
}

fmt <- function(x, k = 2) formatC(x, format = "f", digits = k)
fmtp <- function(p) ifelse(is.na(p), "", ifelse(p < 0.001, "<0.001", formatC(p, format = "f", digits = 3)))
