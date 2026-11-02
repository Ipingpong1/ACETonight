# STATUS (H1 confirmatory analysis)

- 2026-11-02 06:48 UTC: Stage 1 data prep done: BRFSS n=35418 (Sp 10945 / En 24473), CHIS n=29954 (Sp 5536 / En 24418); files in analysis/data/ (brfss_analytic, chis_analytic .rds/.csv); log 01_prep_log.txt
- 2026-11-02 06:54 UTC: Stage 2 Table 1 done: analysis/table1.csv, analysis/table1.md
- 2026-11-02 06:57 UTC: Stage 4 primary MIMIC CHIS: fitted + 80/80 replicates; outputs analysis/primary/effects_chis.csv, params_chis.csv, fit_indices_chis.json
- 2026-11-02 07:01 UTC: Stage 3 Table 2 done: analysis/table2.csv, analysis/table2.md
- 2026-11-02 07:03 UTC: Stage 5 S1 done (replicate SEs): analysis/secondary/effects_s1.csv
- 2026-11-02 07:04 UTC: Stage 4 primary MIMIC BRFSS: fitted + 100/100 replicates; outputs analysis/primary/effects_brfss.csv, params_brfss.csv, fit_indices_brfss.json
- 2026-11-02 07:04 UTC: Stage 5 S5 impact CHIS done: analysis/secondary/s5_impact_chis.csv
- 2026-11-02 07:05 UTC: Stage 4 verdict: H1 SUPPORTED (Holm across 6 tests); analysis/primary_results.csv, primary_results.md, H1_verdict.json
- 2026-11-02 07:05 UTC: Stage 5 S2 done (replicate SEs): analysis/secondary/effects_s2.csv
- 2026-11-02 07:05 UTC: Stage 5 S6 mode interaction done: analysis/secondary/s6_mode.csv
- 2026-11-02 07:06 UTC: Stage 5 S5 impact BRFSS done: analysis/secondary/s5_impact_brfss.csv
- 2026-11-02 07:06 UTC: Stage 5 S7 BRFSS 11-item MIMIC done: analysis/secondary/s7_effects.csv
- 2026-11-02 07:06 UTC: Stage 5 S3 MGCFA done: analysis/secondary/s3_fit.csv, s3_difftests.csv, s3_latent_means.csv, s3_score_tests.csv [SUPERSEDED: group.equal thresholds not applied; rerun 07:08 with explicit syntax]
- 2026-11-02 07:08 UTC: Stage 5 S3 MGCFA done: analysis/secondary/s3_fit.csv, s3_difftests.csv, s3_latent_means.csv, s3_score_tests.csv
- 2026-11-02 07:11 UTC: Stage 5 S4 anchor sensitivity done: analysis/secondary/s4_effects.csv, s4b_purification_history.csv, s4d_alignment_*.csv
- 2026-11-02 07:16 UTC: Stage 6 figures done: figures/fig1_item_prevalence_by_language, fig2_dif_estimates_all_items, fig3_robustness_target_dif, fig4_impact_gap (.png 300 dpi, .pdf, .csv of plotted numbers); palette grey #898781 + accent #2a78d6 validated (CVD dE 15.9, normal 17.8, contrast >= 3:1)
- 2026-11-02 07:17 UTC: Stage 7 RESULTS.md written: analysis/RESULTS.md (verdict, summary and caveats, fit, Tables 1-2, S1-S7, deviations, files); DEVIATIONS.md updated; plan SHA-256 re-verified unchanged
