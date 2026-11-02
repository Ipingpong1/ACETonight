# Stage 5 / S5: impact. Model-implied, simulation-based Spanish-English gap in the mean 8-item ACE count and in
# >= 4 of the 8 harmonized items, with the primary MIMIC as estimated vs with the Spanish target direct effects set to 0.
# Replicate-based 95% CIs (same replicate coefficient sets as the primary analysis; replicate weights for averaging).
# usage: Rscript 06_s5_impact.R brfss|chis CORES
args <- commandArgs(trailingOnly = TRUE)
source("/home/mo2273/ace_manuscript/scripts/common.R")
SV <- args[1]; CORES <- as.integer(args[2]); MDRAW <- 50
OUT <- file.path(AN, "secondary"); dir.create(OUT, showWarnings = FALSE)
fit <- readRDS(file.path(AN, "primary", sprintf("fit_%s.rds", SV)))
R <- readRDS(file.path(AN, "primary", sprintf("repcoef_%s.rds", SV)))
if (SV == "brfss") { L <- load_brfss(); d <- L$d; repw <- brfss_repw(d, 100)$W } else { L <- load_chis(); d <- L$d; repw <- chis_repw(d) }
pt0 <- as.data.table(parTable(fit))
n <- nrow(d); sp <- d$sp

sim <- function(p, wvec) {
  ip <- lapply(setNames(ITEMS8, ITEMS8), item_pars, pe = p, factors = F2)
  mu <- list(HD = eta_hat(p, "HD", d), AB = eta_hat(p, "AB", d))
  Psi <- matrix(c(p[op == "~~" & lhs == "HD" & rhs == "HD", est], rep(p[op == "~~" & ((lhs == "HD" & rhs == "AB") | (lhs == "AB" & rhs == "HD")), est], 2),
                  p[op == "~~" & lhs == "AB" & rhs == "AB", est]), 2)
  Lc <- chol(Psi)
  cnt1 <- cnt0 <- ge1 <- ge0 <- numeric(n)
  for (m in seq_len(MDRAW)) {
    set.seed(5000 + m)                                   # common random numbers across scenarios and replicates
    z <- matrix(rnorm(2 * n), n, 2) %*% Lc
    eta <- list(HD = mu$HD + z[, 1], AB = mu$AB + z[, 2])
    c1 <- c0 <- numeric(n)
    for (it in ITEMS8) {
      q <- ip[[it]]; e <- rnorm(n, 0, sqrt(q$theta))
      lin <- q$lambda * eta[[q$F]] + e - q$tau
      b <- if (nrow(q$direct)) q$direct[rhs == "sp", est] else 0
      c1 <- c1 + (lin + b * sp > 0); c0 <- c0 + (lin > 0)          # with vs without the sp direct effect (targets only)
    }
    cnt1 <- cnt1 + c1; cnt0 <- cnt0 + c0; ge1 <- ge1 + (c1 >= 4); ge0 <- ge0 + (c0 >= 4)
  }
  cnt1 <- cnt1 / MDRAW; cnt0 <- cnt0 / MDRAW; ge1 <- 100 * ge1 / MDRAW; ge0 <- 100 * ge0 / MDRAW
  ws <- wvec[sp == 1]; we <- wvec[sp == 0]
  c(mean_Sp_model = weighted.mean(cnt1[sp == 1], ws), mean_Sp_noDIF = weighted.mean(cnt0[sp == 1], ws), mean_En_model = weighted.mean(cnt1[sp == 0], we),
    p4_Sp_model = weighted.mean(ge1[sp == 1], ws), p4_Sp_noDIF = weighted.mean(ge0[sp == 1], ws), p4_En_model = weighted.mean(ge1[sp == 0], we),
    mean_Sp_obs = weighted.mean(d$count8h[sp == 1], ws), mean_En_obs = weighted.mean(d$count8h[sp == 0], we),
    p4_Sp_obs = 100 * weighted.mean(d$ace4h[sp == 1], ws), p4_En_obs = 100 * weighted.mean(d$ace4h[sp == 0], we))
}
derive <- function(v) {
  c(v, gap_mean_obs = v[["mean_Sp_obs"]] - v[["mean_En_obs"]], gap_mean_model = v[["mean_Sp_model"]] - v[["mean_En_model"]],
    gap_mean_noDIF = v[["mean_Sp_noDIF"]] - v[["mean_En_model"]], change_gap_mean = v[["mean_Sp_noDIF"]] - v[["mean_Sp_model"]],
    pct_gap_mean_due_DIF = 100 * (v[["mean_Sp_noDIF"]] - v[["mean_Sp_model"]]) / -(v[["mean_Sp_model"]] - v[["mean_En_model"]]),
    gap_p4_obs = v[["p4_Sp_obs"]] - v[["p4_En_obs"]], gap_p4_model = v[["p4_Sp_model"]] - v[["p4_En_model"]],
    gap_p4_noDIF = v[["p4_Sp_noDIF"]] - v[["p4_En_model"]], change_gap_p4 = v[["p4_Sp_noDIF"]] - v[["p4_Sp_model"]],
    pct_gap_p4_due_DIF = 100 * (v[["p4_Sp_noDIF"]] - v[["p4_Sp_model"]]) / -(v[["p4_Sp_model"]] - v[["p4_En_model"]]))
}
est0 <- derive(sim(pt0, d$w))
pt_from <- function(cv) { p <- copy(pt0); idx <- which(p$free > 0); p$est[idx] <- cv[p$free[idx]]; p }
ridx <- as.integer(rownames(R$M))
REP <- do.call(rbind, mclapply(seq_len(nrow(R$M)), function(i) derive(sim(pt_from(R$M[i, ]), repw[, ridx[i]])), mc.cores = CORES))
se <- sqrt(R$scale * colSums(R$rscales * sweep(REP, 2, est0[colnames(REP)])^2))
res <- data.table(survey = toupper(SV), quantity = names(est0), estimate = unname(est0), se_rep = unname(se[names(est0)]))
res[, `:=`(ci_lo = estimate - 1.96 * se_rep, ci_hi = estimate + 1.96 * se_rep)]
res[, n_rep := nrow(R$M)]; res[, draws_per_person := MDRAW]
fwrite(res, file.path(OUT, sprintf("s5_impact_%s.csv", SV)))
print(res[, .(quantity, estimate = round(estimate, 3), se_rep = round(se_rep, 3))])
status(sprintf("Stage 5 S5 impact %s done: analysis/secondary/s5_impact_%s.csv", toupper(SV), SV))
