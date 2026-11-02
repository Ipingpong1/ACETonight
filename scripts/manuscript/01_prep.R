# Stage 1: harmonized R-ready analytic files for BRFSS 2019-2025 and CHIS 2021-2025.
# usage: Rscript 01_prep.R BRFSS_CSV CHIS_CSV
args <- commandArgs(trailingOnly = TRUE)
source("/home/mo2273/ace_manuscript/scripts/common.R")
brfss_csv <- args[1]; chis_csv <- args[2]
LOG <- file.path(AN, "01_prep_log.txt"); if (file.exists(LOG)) file.remove(LOG)

# ------------------------------------------------------------------ BRFSS
b <- fread(brfss_csv)
setnames(b, c("_STSTR", "_PSU", "_AGEG5YR"), c("STSTR", "PSU", "AGEG5YR"))
stopifnot(all(b$lang %in% c("English", "Spanish")), all(b$hisp == "Hispanic"), !any(b$terr), all(b$ace_complete))
# same coding as /home/mo2273/ace_tonight_scripts/dif/build_dif_data.py (e_* indicators): yes/no items 1 = yes;
# ACEDIVRC 1 = yes, 2 = no, 8 = parents not married -> 0; frequency items once (2) or more than once (3) -> 1.
d <- b[, .(year, source, state, STSTR, PSU,
           sp = as.numeric(lang == "Spanish"), wt_file = wt, w = wt / 7,
           mh = e_ACEDEPRS, drink = e_ACEDRINK, drugs = e_ACEDRUGS, jail = e_ACEPRISN, divorce = e_ACEDIVRC,
           ipv = e_ACEPUNCH, phys = e_ACEHURT, verbal = e_ACESWEAR, touch = e_ACETOUCH, tthem = e_ACETTHEM, hvsex = e_ACEHVSEX,
           agecat = as.integer(AGEG5YR), educ = as.integer(EDUCA), sex = as.integer(sex), inc = as.integer(inc5))]
# recheck item coding against raw codes
chk <- b[, .(mh = all((ACEDEPRS == 1) == (e_ACEDEPRS == 1)), div = all((ACEDIVRC == 1) == (e_ACEDIVRC == 1)),
             ipv = all((ACEPUNCH %in% 2:3) == (e_ACEPUNCH == 1)), sw = all((ACESWEAR %in% 2:3) == (e_ACESWEAR == 1)))]
stopifnot(all(unlist(chk)))
# Census region from state FIPS (1 Northeast, 2 Midwest, 3 South, 4 West)
NE <- c(9, 23, 25, 33, 44, 50, 34, 36, 42); MW <- c(17, 18, 26, 39, 55, 19, 20, 27, 29, 31, 38, 46)
SO <- c(10, 11, 12, 13, 24, 37, 45, 51, 54, 1, 21, 28, 47, 5, 22, 40, 48); WE <- c(4, 8, 16, 30, 32, 35, 49, 56, 2, 6, 15, 41, 53)
d[, region := fifelse(state %in% NE, 1L, fifelse(state %in% MW, 2L, fifelse(state %in% SO, 3L, fifelse(state %in% WE, 4L, NA_integer_))))]
stopifnot(!anyNA(d$region))
d[, sexany := pmax(touch, tthem, hvsex)]
d[, ace8score := mh + pmax(drink, drugs) + jail + divorce + ipv + phys + verbal + sexany]   # standard BRFSS 8-category score
d[, ace4 := as.numeric(ace8score >= 4)]
d[, count8h := mh + drink + drugs + jail + divorce + ipv + phys + verbal]                  # 8 harmonized items (S5)
d[, ace4h := as.numeric(count8h >= 4)]
# design: strata = year x file x _STSTR ; PSU = _PSU (made unique by year/file/state; nest = TRUE)
d[, strat := paste(year, source, STSTR, sep = "_")]
d[, psu := paste(year, source, state, PSU, sep = "_")]
# collapsed strata for the Rao-Wu bootstrap only (survey's subbootstrap is undefined for 1-PSU strata):
# each singleton stratum is merged with the nearest (by _STSTR code) multi-PSU stratum in the same year x file x state;
# if none exists there, with the nearest multi-PSU stratum in the same year x file.
d[, grp := paste(year, source, state, sep = "_")]; d[, grp2 := paste(year, source, sep = "_")]
d[, strat_boot := strat]
for (iter in 1:5) {
  ns <- d[, .(npsu = uniqueN(psu), code = STSTR[1]), by = .(grp, grp2, strat_boot)]
  if (!any(ns$npsu == 1)) break
  map <- character(0)
  for (i in which(ns$npsu == 1)) {
    cand <- ns[grp == ns$grp[i] & npsu > 1]
    if (!nrow(cand)) cand <- ns[grp2 == ns$grp2[i] & npsu > 1]
    map[ns$strat_boot[i]] <- cand$strat_boot[which.min(abs(cand$code - ns$code[i]))]
  }
  d[strat_boot %in% names(map), strat_boot := map[strat_boot]]
}
nsb <- d[, .(npsu = uniqueN(psu)), by = strat_boot]
logf(LOG, "BRFSS n = ", nrow(d), " (Spanish ", sum(d$sp), ", English ", sum(1 - d$sp), "); strata (year x file x _STSTR) = ",
     uniqueN(d$strat), ", singleton strata = ", d[, uniqueN(psu), by = strat][V1 == 1, .N],
     "; bootstrap strata after collapsing singletons = ", nrow(nsb), " (min PSUs/stratum = ", min(nsb$npsu), ")")
logf(LOG, "BRFSS missing-code counts: age 14 (DK/Ref) = ", sum(d$agecat == 14), "; EDUCA 9 (Ref) = ", sum(d$educ == 9),
     "; income 9 (missing) = ", sum(d$inc == 9))
d[, c("grp", "grp2") := NULL]
saveRDS(d, file.path(DAT, "brfss_analytic.rds")); fwrite(d, file.path(DAT, "brfss_analytic.csv"))

# ------------------------------------------------------------------ CHIS
c0 <- fread(chis_csv)
c0 <- c0[ombsrr_p1 == 1 & intvlngc_p1 %in% c(1, 2)]
stopifnot(all(c0$aq1 %in% 1:2), all(c0$aq5 %in% 1:3), all(c0$aq6 %in% 1:3), all(c0$ace8 %in% 1:5))
ch <- c0[, .(year, sp = as.numeric(intvlngc_p1 == 2),
             mh = as.numeric(aq1 == 1), drink = as.numeric(aq2 == 1), drugs = as.numeric(aq3 == 1), jail = as.numeric(aq4 == 1),
             divorce = as.numeric(aq5 == 1),                     # 3 = parents not married -> 0
             ipv = as.numeric(aq6 >= 2), phys = as.numeric(aq7 >= 2), verbal = as.numeric(aq8 >= 2),
             ace4 = as.numeric(ace8 == 5),                       # CHIS 8-category score (includes sexual abuse), 5 = 4+
             agecat = as.integer(srage_p1), educ = as.integer(ahedc_p1), sex = as.integer(srsex), pov = as.integer(povll),
             fb = as.numeric(ah33new == 2), pctlf = as.integer(pctlf_p), web = as.numeric(intv_mode2 == 2),
             spk_eng = as.integer(spk_eng))]
ch[, w := c0$rakedw0 / 5]
for (r in 1:80) set(ch, j = paste0("w", r), value = c0[[paste0("rakedw", r)]] / 5)
ch[, count8h := mh + drink + drugs + jail + divorce + ipv + phys + verbal]
ch[, ace4h := as.numeric(count8h >= 4)]
ch[, spweb := sp * web]
logf(LOG, "CHIS n = ", nrow(ch), " (Spanish ", sum(ch$sp), ", English ", sum(1 - ch$sp), "); foreign-born Spanish ",
     ch[sp == 1, sum(fb)], ", foreign-born English ", ch[sp == 0, sum(fb)], "; Spanish phone/web ", ch[sp == 1, sum(1 - web)], "/",
     ch[sp == 1, sum(web)], "; English phone/web ", ch[sp == 0, sum(1 - web)], "/", ch[sp == 0, sum(web)])
logf(LOG, "CHIS min replicate weight = ", signif(min(as.matrix(ch[, paste0("w", 1:80), with = FALSE])), 4),
     "; any zero replicate weights: ", any(as.matrix(ch[, paste0("w", 1:80), with = FALSE]) <= 0))
saveRDS(ch, file.path(DAT, "chis_analytic.rds")); fwrite(ch, file.path(DAT, "chis_analytic.csv"))

# quick unweighted endorsement check vs exploratory numbers
logf(LOG, "BRFSS weighted % (Sp/En): ", paste(sapply(c(ITEMS8, "ace4"), function(v)
  sprintf("%s %.1f/%.1f", v, 100 * d[sp == 1, weighted.mean(get(v), w)], 100 * d[sp == 0, weighted.mean(get(v), w)])), collapse = "; "))
logf(LOG, "CHIS weighted % (Sp/En): ", paste(sapply(c(ITEMS8, "ace4"), function(v)
  sprintf("%s %.1f/%.1f", v, 100 * ch[sp == 1, weighted.mean(get(v), w)], 100 * ch[sp == 0, weighted.mean(get(v), w)])), collapse = "; "))
status(sprintf("Stage 1 data prep done: BRFSS n=%d (Sp %d / En %d), CHIS n=%d (Sp %d / En %d); files in analysis/data/ (brfss_analytic, chis_analytic .rds/.csv); log 01_prep_log.txt",
               nrow(d), sum(d$sp), sum(1 - d$sp), nrow(ch), sum(ch$sp), sum(1 - ch$sp)))
