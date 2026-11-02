# Stage 4 (part b): Holm adjustment across the 6 target tests and the pre-specified decision rule.
# usage: Rscript 04b_verdict.R
source("/home/mo2273/ace_manuscript/scripts/common.R")
P <- file.path(AN, "primary")
E <- rbindlist(lapply(c("brfss", "chis"), function(s) fread(file.path(P, sprintf("effects_%s.csv", s)))), fill = TRUE)
T <- E[lhs %in% TARGETS]
T[, p_holm := p.adjust(p, method = "holm")]
T[, `:=`(neg = est < 0, sig = p_holm < 0.05, big = est <= -0.24)]
T[, meets := neg & sig & big]
E <- merge(E, T[, .(survey, lhs, p_holm, meets)], by = c("survey", "lhs"), all.x = TRUE)
E[, item_label := LAB[lhs]]; E[lhs %in% c("HD", "AB"), item_label := c(HD = "Household dysfunction factor", AB = "Physical/emotional abuse factor")[lhs]]
fwrite(E, file.path(AN, "primary_results.csv"))

per <- T[, .(n_meet = sum(meets)), by = survey]
both_items <- T[, .(both = all(meets)), by = lhs]
supported <- all(T$meets)
partial_same <- sum(both_items$both) >= 2                       # same >= 2 items meet all criteria in both surveys
partial_count <- all(per$n_meet >= 2) && nrow(per) == 2        # >= 2 items per survey (items may differ)
one_survey_all <- any(per$n_meet == 3)
verdict <- if (supported) "SUPPORTED" else if (partial_same || one_survey_all) "PARTIALLY SUPPORTED" else "NOT SUPPORTED"
verdict_alt <- if (supported) "SUPPORTED" else if (partial_count || one_survey_all) "PARTIALLY SUPPORTED" else "NOT SUPPORTED"
out <- list(verdict = verdict, verdict_alt_reading = verdict_alt, all_six_criteria_met = supported,
            items_meeting_in_both = both_items[both == TRUE, lhs], per_survey_items_meeting = setNames(as.list(per$n_meet), per$survey),
            rule = "H1 supported if in both surveys all three direct effects < 0, Holm-adjusted p < .05 (6 tests) and b <= -0.24; partially supported if these hold for >= 2 items in both surveys or for all 3 items in one survey; otherwise not supported.",
            tests = T[, .(survey, item = lhs, b = est, se_rep, z, p, p_holm, ci_lo, ci_hi, OR_eq, OR_lo, OR_hi, pdiff_pp, pdiff_lo, pdiff_hi, neg, sig, big, meets)])
write_json(out, file.path(AN, "H1_verdict.json"), auto_unbox = TRUE, digits = 8, pretty = TRUE)

ln <- c("## Primary MIMIC: target direct effects (uniform DIF) and language -> factor effects", "",
        "| Survey | Parameter | b (probit) | Replicate SE | 95% CI | OR-equiv. exp(1.7b) (95% CI) | p | Holm p | Model-implied Δ prob., Spanish (pp, 95% CI) | Meets all criteria |",
        "|---|---|---:|---:|---|---|---:|---:|---|---|")
for (i in seq_len(nrow(E))) {
  r <- E[i]
  tgt <- r$lhs %in% TARGETS
  ln <- c(ln, sprintf("| %s | %s | %s | %s | %s, %s | %s | %s | %s | %s | %s |", r$survey, r$item_label, fmt(r$est, 3), fmt(r$se_rep, 3),
                      fmt(r$ci_lo, 3), fmt(r$ci_hi, 3),
                      if (tgt) sprintf("%s (%s, %s)", fmt(r$OR_eq), fmt(r$OR_lo), fmt(r$OR_hi)) else "",
                      fmtp(r$p), if (tgt) fmtp(r$p_holm) else "",
                      if (tgt) sprintf("%s (%s, %s)", fmt(r$pdiff_pp, 1), fmt(r$pdiff_lo, 1), fmt(r$pdiff_hi, 1)) else "",
                      if (tgt) ifelse(r$meets, "yes", "no") else ""))
}
ln <- c(ln, "", sprintf("**H1 verdict (pre-specified decision rule): %s.** Items meeting all criteria (b < 0, Holm p < .05, b ≤ −0.24) in both surveys: %s. Per survey: %s.",
                        verdict, if (sum(both_items$both)) paste(both_items[both == TRUE, LAB[lhs]], collapse = ", ") else "none",
                        paste(sprintf("%s %d/3", per$survey, per$n_meet), collapse = "; ")),
        if (verdict != verdict_alt) sprintf("Under the alternative reading of the partial rule (≥ 2 items per survey, not necessarily the same items) the verdict would be %s.", verdict_alt)
        else "The verdict is the same under both readings of the partial-support rule.")
writeLines(ln, file.path(AN, "primary_results.md"))
cat(paste(ln, collapse = "\n"), "\n")
status(sprintf("Stage 4 verdict: H1 %s (Holm across 6 tests); analysis/primary_results.csv, primary_results.md, H1_verdict.json", verdict))
