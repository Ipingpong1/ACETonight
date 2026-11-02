# Stage 3: Table 2 -- weighted prevalence (design-based 95% CI) of 8 items + 4+ ACEs by interview language;
# crude and adjusted prevalence ratios (survey-weighted Poisson working model, covariates per plan).
# usage: Rscript 03_table2.R CORES
args <- commandArgs(trailingOnly = TRUE)
source("/home/mo2273/ace_manuscript/scripts/common.R")
CORES <- as.integer(args[1])
b <- readRDS(file.path(DAT, "brfss_analytic.rds")); ch <- readRDS(file.path(DAT, "chis_analytic.rds"))
des_b <- svydesign(ids = ~psu, strata = ~strat, weights = ~w, data = b, nest = TRUE)   # lonely.psu = "adjust" (common.R)
des_c <- svrepdesign(data = ch, weights = ~w, repweights = as.matrix(ch[, paste0("w", 1:80), with = FALSE]),
                     type = "other", scale = 1, rscales = rep(1, 80), mse = TRUE, combined.weights = TRUE)
OUTC <- c(ITEMS8, "ace4")
adj_b <- "factor(agecat) + factor(educ) + factor(sex) + factor(inc) + factor(year) + factor(region)"
adj_c <- "factor(agecat) + factor(educ) + factor(sex) + factor(pov) + factor(year)"
nat_c <- paste(adj_c, "+ fb + factor(pctlf)")

prev <- function(des, y, g) {
  r <- svyciprop(as.formula(sprintf("~I(%s == 1)", y)), subset(des, sp == g), method = "logit", level = 0.95)
  ci <- attr(r, "ci"); c(100 * as.numeric(r), 100 * ci[1], 100 * ci[2])
}
pr <- function(des, y, rhs) {
  m <- svyglm(as.formula(sprintf("%s ~ sp %s", y, if (rhs == "") "" else paste("+", rhs))), design = des, family = quasipoisson())
  b0 <- coef(m)["sp"]; s <- sqrt(vcov(m)["sp", "sp"])
  c(PR = exp(b0), lo = exp(b0 - 1.96 * s), hi = exp(b0 + 1.96 * s), p = 2 * pnorm(-abs(b0 / s)))
}
run <- function(des, survey, specs) {
  rbindlist(mclapply(OUTC, function(y) {
    pe <- prev(des, y, 0); ps <- prev(des, y, 1)
    row <- data.table(survey = survey, item = y, label = LAB[[y]],
                      En_pct = pe[1], En_lo = pe[2], En_hi = pe[3], Sp_pct = ps[1], Sp_lo = ps[2], Sp_hi = ps[3])
    for (nm in names(specs)) {
      r <- pr(des, y, specs[[nm]])
      row[, paste0(nm, c("_PR", "_lo", "_hi", "_p")) := as.list(unname(r))]
    }
    row
  }, mc.cores = CORES))
}
t2b <- run(des_b, "BRFSS", list(crude = "", adj = adj_b))
t2c <- run(des_c, "CHIS", list(crude = "", adj = adj_c, adjnat = nat_c))
t2 <- rbind(t2b, t2c, fill = TRUE)
fwrite(t2, file.path(AN, "table2.csv"))

ci <- function(x, l, h, k = 1) sprintf("%s (%s, %s)", fmt(x, k), fmt(l, k), fmt(h, k))
mk <- function(t, nat = FALSE) {
  h <- "| Item | English % (95% CI) | Spanish % (95% CI) | Crude PR (95% CI) | Adjusted PR (95% CI) |"
  s <- "|---|---|---|---|---|"
  if (nat) { h <- paste0(h, " Adj. + nativity PR (95% CI)* |"); s <- paste0(s, "---|") }
  rows <- vapply(seq_len(nrow(t)), function(i) {
    r <- t[i]
    x <- sprintf("| %s | %s | %s | %s | %s |", r$label, ci(r$En_pct, r$En_lo, r$En_hi), ci(r$Sp_pct, r$Sp_lo, r$Sp_hi),
                 ci(r$crude_PR, r$crude_lo, r$crude_hi, 2), ci(r$adj_PR, r$adj_lo, r$adj_hi, 2))
    if (nat) x <- paste0(x, sprintf(" %s |", ci(r$adjnat_PR, r$adjnat_lo, r$adjnat_hi, 2)))
    x
  }, "")
  paste(c(h, s, rows), collapse = "\n")
}
txt <- paste0("## Table 2. Weighted prevalence of ACE items by interview language and Spanish-vs-English prevalence ratios\n\n",
              "**BRFSS 2019-2025** (Taylor linearization; strata = year x file x _STSTR, PSU = _PSU, nest = TRUE, lonely PSU = adjust)\n\n", mk(t2b),
              "\n\n**CHIS 2021-2025** (jackknife replicate weights RAKEDW1-80, scale 1, MSE)\n\n", mk(t2c, nat = TRUE),
              "\n\nPrevalence CIs: logit-transformed design-based intervals (svyciprop). PR = Spanish vs English prevalence ratio from a ",
              "survey-weighted Poisson working model (log link), Wald 95% CI. Adjusted: BRFSS age group, sex, education, income (missing as category), ",
              "survey year, Census region; CHIS age group, sex, education, poverty level, survey year. ",
              "4+ ACEs: standard 8-category score including sexual abuse (BRFSS: any of the 3 sexual items; CHIS: ACE8 = 4+). ",
              "*Not pre-specified for Table 2; added as context for H1b (adds born outside US and percent of life in US).\n")
writeLines(txt, file.path(AN, "table2.md"))
status("Stage 3 Table 2 done: analysis/table2.csv, analysis/table2.md")
cat(txt)
