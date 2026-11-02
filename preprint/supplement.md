# Supplement to: Does interview language change how Hispanic adults report childhood household adversity?

*Preprint version 0.1, 2 November 2026. All tables are generated from the files in `analysis/` and `exploratory/` of the repository; the source file is named under each table.*

**Contents**

- S1. Full sample characteristics
- S2. Item prevalence with design-based CIs and prevalence ratios
- S3. Model fit
- S4. Multigroup CFA by interview language (S3 in the plan)
- S5. Anchor sensitivity and alignment (S4 in the plan)
- S6. Impact, mode and 11-item models (S5–S7 in the plan); deviations from the frozen plan
- S7. Exploratory analyses (not pre-specified)
- S8. Literature search summary

## S1. Full sample characteristics

Source: `analysis/table1.md`. n = unweighted; % = weighted column percentage (BRFSS final weight ÷ 7; CHIS RAKEDW0 ÷ 5). Models use the native age groups (BRFSS _AGEG5YR 1–13 plus DK/refused; CHIS SRAGE_P1 14 groups); the groups below are collapsed for display.

**BRFSS 2019–2025** (English n = 24,473; Spanish n = 10,945)

| Characteristic | English n | English % | Spanish n | Spanish % |
|---|---:|---:|---:|---:|
| *Age* 18–24 | 4,175 | 21.7 | 747 | 8.5 |
| 25–34 | 5,186 | 22.9 | 2,126 | 19.0 |
| 35–44 | 4,536 | 18.9 | 2,687 | 23.6 |
| 45–54 | 3,731 | 13.9 | 2,154 | 18.3 |
| 55–64 | 3,202 | 12.3 | 1,565 | 15.0 |
| 65+ | 3,450 | 9.6 | 1,625 | 15.4 |
| Don't know/refused | 193 | 0.8 | 41 | 0.3 |
| *Sex* Male | 11,873 | 50.7 | 4,880 | 44.5 |
| Female | 12,600 | 49.3 | 6,065 | 55.5 |
| *Education* Never attended/kindergarten | 43 | 0.2 | 307 | 2.4 |
| Grades 1–8 | 571 | 3.4 | 3,665 | 36.3 |
| Grades 9–11 | 1,468 | 8.9 | 1,899 | 21.8 |
| Grade 12/GED | 7,425 | 29.9 | 2,856 | 23.4 |
| College 1–3 years | 7,218 | 33.1 | 948 | 8.6 |
| College 4+ years | 7,692 | 24.1 | 1,149 | 6.7 |
| Refused | 56 | 0.3 | 121 | 1.0 |
| *Household income* <$15,000 | 1,644 | 6.8 | 2,115 | 22.2 |
| $15,000–24,999 | 2,934 | 11.5 | 2,920 | 25.4 |
| $25,000–34,999 | 2,664 | 10.7 | 1,694 | 14.2 |
| $35,000–49,999 | 3,277 | 12.6 | 1,052 | 9.6 |
| $50,000+ | 10,463 | 44.2 | 625 | 6.2 |
| Missing/DK/refused | 3,491 | 14.2 | 2,539 | 22.4 |
| *Survey year* 2019 | 4,371 | 14.0 | 1,726 | 11.9 |
| 2020 | 7,607 | 36.2 | 2,995 | 40.6 |
| 2021 | 2,675 | 9.3 | 1,124 | 7.9 |
| 2022 | 2,581 | 10.9 | 1,214 | 9.7 |
| 2023 | 2,638 | 10.9 | 1,641 | 11.7 |
| 2024 | 2,634 | 11.3 | 883 | 9.1 |
| 2025 | 1,967 | 7.4 | 1,362 | 9.1 |
| *Census region* Northeast | 3,498 | 18.0 | 2,056 | 19.7 |
| Midwest | 5,038 | 12.0 | 2,368 | 6.8 |
| South | 8,638 | 42.8 | 4,441 | 43.1 |
| West | 7,299 | 27.2 | 2,080 | 30.5 |

**CHIS 2021–2025** (English n = 24,418; Spanish n = 5,536)

| Characteristic | English n | English % | Spanish n | Spanish % |
|---|---:|---:|---:|---:|
| *Age* 18–25 | 2,755 | 25.4 | 189 | 5.9 |
| 26–34 | 3,778 | 20.0 | 449 | 9.4 |
| 35–44 | 4,476 | 17.6 | 1,029 | 22.9 |
| 45–54 | 4,247 | 14.3 | 1,388 | 24.9 |
| 55–64 | 4,321 | 11.8 | 1,347 | 20.4 |
| 65+ | 4,841 | 10.9 | 1,134 | 16.5 |
| *Sex* Male | 9,789 | 49.7 | 2,190 | 47.1 |
| Female | 14,629 | 50.3 | 3,346 | 52.9 |
| *Education* No formal education or grades 1–8 | 660 | 7.0 | 1,428 | 39.9 |
| Grades 9–11 | 777 | 8.7 | 741 | 22.7 |
| Grade 12/high school diploma | 4,263 | 31.4 | 1,386 | 23.8 |
| Some college | 4,515 | 13.7 | 555 | 4.5 |
| Vocational school | 2,006 | 4.7 | 404 | 2.3 |
| AA/AS degree | 2,205 | 5.8 | 121 | 0.8 |
| BA/BS degree or some graduate school | 6,137 | 18.7 | 692 | 4.7 |
| MA/MS degree | 2,923 | 7.6 | 142 | 1.0 |
| PhD or equivalent | 932 | 2.4 | 67 | 0.4 |
| *Poverty level* 0–99% FPL | 3,659 | 18.5 | 1,848 | 35.0 |
| 100–199% FPL | 4,305 | 20.4 | 1,833 | 32.7 |
| 200–299% FPL | 3,509 | 15.4 | 845 | 15.2 |
| 300%+ FPL | 12,945 | 45.7 | 1,010 | 17.1 |
| *Survey year* 2021 | 4,921 | 20.2 | 1,105 | 20.3 |
| 2022 | 4,581 | 20.5 | 1,136 | 19.7 |
| 2023 | 4,934 | 20.8 | 1,064 | 19.3 |
| 2024 | 5,482 | 19.2 | 1,324 | 19.9 |
| 2025 | 4,500 | 19.3 | 907 | 20.8 |
| *Nativity* Born in US | 18,113 | 72.3 | 402 | 7.8 |
| Born outside US | 6,305 | 27.7 | 5,134 | 92.2 |
| *Percent of life in US* 0–20% | 230 | 1.2 | 606 | 10.3 |
| 21–40% | 494 | 2.2 | 964 | 15.4 |
| 41–60% | 1,094 | 5.8 | 1,959 | 36.6 |
| 61–80% | 2,040 | 10.1 | 1,457 | 27.4 |
| 81–100% (incl. all US-born) | 20,560 | 80.7 | 550 | 10.3 |
| *Interview mode* Phone (interviewer) | 3,104 | 13.3 | 1,844 | 34.1 |
| Web (self-administered) | 21,314 | 86.7 | 3,692 | 65.9 |
| *English proficiency* Speaks only English | 9,669 | 32.4 | 29 | 0.5 |
| Very well/well | 14,070 | 62.3 | 2,640 | 40.1 |
| Not well/not at all | 679 | 5.4 | 2,867 | 59.4 |

## S2. Item prevalence with design-based CIs and prevalence ratios

Source: `analysis/table2.md`. Prevalence CIs: logit-transformed design-based intervals. PR = Spanish vs English prevalence ratio from a survey-weighted Poisson working model, Wald 95% CI. Adjusted: BRFSS age group, sex, education, income (missing as category), survey year, Census region; CHIS age group, sex, education, poverty level, survey year.

**BRFSS 2019–2025** (Taylor linearization; strata = year × file × _STSTR, PSU = _PSU, lonely PSU = adjust)

| Item | English % (95% CI) | Spanish % (95% CI) | Crude PR (95% CI) | Adjusted PR (95% CI) |
|---|---|---|---|---|
| Household mental illness | 21.9 (20.8, 23.0) | 4.0 (3.3, 4.9) | 0.18 (0.15, 0.23) | 0.24 (0.19, 0.31) |
| Household problem drinking | 25.3 (24.2, 26.5) | 16.8 (15.3, 18.4) | 0.67 (0.60, 0.74) | 0.68 (0.60, 0.77) |
| Household drug use | 14.2 (13.3, 15.2) | 3.1 (2.6, 3.7) | 0.22 (0.18, 0.26) | 0.21 (0.17, 0.26) |
| Household incarceration | 14.0 (13.0, 15.0) | 2.6 (2.1, 3.3) | 0.19 (0.15, 0.24) | 0.20 (0.16, 0.26) |
| Parental separation/divorce | 39.0 (37.6, 40.3) | 24.7 (23.1, 26.4) | 0.63 (0.59, 0.68) | 0.66 (0.60, 0.72) |
| Witnessed parental violence | 23.1 (21.9, 24.3) | 17.1 (15.6, 18.6) | 0.74 (0.67, 0.82) | 0.67 (0.59, 0.76) |
| Physical abuse | 33.8 (32.5, 35.1) | 30.4 (28.5, 32.3) | 0.90 (0.83, 0.97) | 0.88 (0.80, 0.97) |
| Verbal abuse | 40.8 (39.4, 42.2) | 18.1 (16.5, 19.8) | 0.44 (0.40, 0.49) | 0.51 (0.45, 0.57) |
| 4+ ACEs (standard 8-category score) | 25.3 (24.1, 26.5) | 10.8 (9.5, 12.1) | 0.43 (0.37, 0.48) | 0.43 (0.37, 0.51) |

**CHIS 2021–2025** (jackknife replicate weights RAKEDW1–80, scale 1, MSE)

| Item | English % (95% CI) | Spanish % (95% CI) | Crude PR (95% CI) | Adjusted PR (95% CI) | Adj. + nativity PR (95% CI)* |
|---|---|---|---|---|---|
| Household mental illness | 23.8 (23.1, 24.5) | 5.6 (4.9, 6.5) | 0.24 (0.21, 0.27) | 0.35 (0.30, 0.40) | 0.45 (0.38, 0.53) |
| Household problem drinking | 30.1 (29.2, 31.0) | 18.4 (17.2, 19.5) | 0.61 (0.57, 0.65) | 0.60 (0.56, 0.65) | 0.67 (0.62, 0.73) |
| Household drug use | 14.5 (13.9, 15.1) | 4.6 (3.9, 5.3) | 0.31 (0.27, 0.37) | 0.32 (0.27, 0.37) | 0.49 (0.41, 0.58) |
| Household incarceration | 13.1 (12.6, 13.7) | 2.6 (2.1, 3.2) | 0.20 (0.16, 0.25) | 0.22 (0.17, 0.28) | 0.43 (0.33, 0.57) |
| Parental separation/divorce | 30.5 (29.6, 31.4) | 21.0 (19.9, 22.1) | 0.69 (0.65, 0.73) | 0.70 (0.65, 0.75) | 0.78 (0.71, 0.85) |
| Witnessed parental violence | 27.6 (26.9, 28.3) | 20.3 (19.1, 21.7) | 0.74 (0.69, 0.79) | 0.69 (0.63, 0.75) | 0.71 (0.65, 0.78) |
| Physical abuse | 28.5 (27.7, 29.4) | 29.4 (28.1, 30.7) | 1.03 (0.98, 1.08) | 1.00 (0.94, 1.05) | 0.98 (0.92, 1.05) |
| Verbal abuse | 45.8 (44.9, 46.8) | 27.3 (25.9, 28.7) | 0.60 (0.56, 0.63) | 0.67 (0.63, 0.70) | 0.72 (0.67, 0.77) |
| 4+ ACEs (standard 8-category score) | 26.1 (25.4, 26.8) | 13.6 (12.6, 14.8) | 0.52 (0.48, 0.57) | 0.56 (0.51, 0.62) | 0.65 (0.58, 0.73) |

*Not pre-specified for Table 2; added as context for H1b (adds born outside US and percent of life in US).

## S3. Model fit

Source: `analysis/RESULTS.md` §3. WLSMV, theta parameterization, survey weights; scaled (mean- and variance-adjusted) indices. CFI/TLI are computed against a baseline conditional on the covariates. Fit was reported but was not a decision criterion.

| Model | χ² (scaled) | df | CFI | TLI | RMSEA | SRMR |
|---|---:|---:|---:|---:|---:|---:|
| Primary MIMIC, BRFSS | 1124.0 | 226 | 0.946 | 0.993 | 0.0106 | 0.050 |
| Primary MIMIC, CHIS | 1594.6 | 196 | 0.942 | 0.992 | 0.0154 | 0.050 |
| S1 CHIS + nativity | 1521.1 | 226 | 0.947 | 0.993 | 0.0138 | 0.050 |
| S2 CHIS foreign-born | 516.7 | 220 | 0.968 | 0.996 | 0.0109 | 0.065 |
| S4a one factor, BRFSS | 1535.5 | 262 | 0.924 | 0.992 | 0.0117 | 0.077 |
| S4a one factor, CHIS | 2625.8 | 227 | 0.901 | 0.988 | 0.0188 | 0.096 |
| S6 CHIS mode interaction | 1556.1 | 202 | 0.944 | 0.992 | 0.0150 | 0.050 |
| S7 BRFSS 11 items, 3 factors | 1281.2 | 318 | 0.975 | 0.996 | 0.0092 | 0.042 |

**Primary and nativity models: all language parameters** (source: `analysis/primary_results.md`, `analysis/secondary/effects_s1.csv`, `effects_s2.csv`; replicate SEs)

| Model | Parameter | b (probit) | Replicate SE | 95% CI | OR-equiv. (95% CI) | p | Δ endorsement, Spanish (pp, 95% CI) |
|---|---|---:|---:|---|---|---:|---|
| BRFSS primary | Household dysfunction factor | −0.537 | 0.061 | −0.656, −0.418 | | <0.001 | |
| BRFSS primary | Physical/emotional abuse factor | −0.408 | 0.049 | −0.504, −0.312 | | <0.001 | |
| BRFSS primary | Household mental illness | −0.624 | 0.114 | −0.848, −0.401 | 0.35 (0.24, 0.51) | <0.001 | −6.0 (−7.9, −4.1) |
| BRFSS primary | Household drug use | −0.696 | 0.118 | −0.927, −0.466 | 0.31 (0.21, 0.45) | <0.001 | −3.1 (−4.2, −2.0) |
| BRFSS primary | Household incarceration | −0.655 | 0.088 | −0.826, −0.483 | 0.33 (0.25, 0.44) | <0.001 | −5.2 (−6.6, −3.8) |
| CHIS primary | Household dysfunction factor | −0.601 | 0.037 | −0.673, −0.528 | | <0.001 | |
| CHIS primary | Physical/emotional abuse factor | −0.270 | 0.025 | −0.318, −0.222 | | <0.001 | |
| CHIS primary | Household mental illness | −0.315 | 0.051 | −0.416, −0.214 | 0.59 (0.49, 0.70) | <0.001 | −4.4 (−5.8, −3.1) |
| CHIS primary | Household drug use | −0.266 | 0.082 | −0.426, −0.106 | 0.64 (0.48, 0.83) | 0.001 | −1.5 (−2.4, −0.6) |
| CHIS primary | Household incarceration | −0.493 | 0.086 | −0.662, −0.324 | 0.43 (0.32, 0.58) | <0.001 | −2.9 (−3.8, −1.9) |
| S1 CHIS + nativity | Household dysfunction factor | −0.441 | 0.041 | | | <0.001 | |
| S1 CHIS + nativity | Physical/emotional abuse factor | −0.234 | 0.030 | | | <0.001 | |
| S1 CHIS + nativity | Household mental illness | −0.231 | 0.059 | | 0.67 (0.55, 0.82) | <0.001 | |
| S1 CHIS + nativity | Household drug use | −0.066 | 0.091 | | 0.89 (0.66, 1.21) | 0.469 | |
| S1 CHIS + nativity | Household incarceration | −0.128 | 0.106 | | 0.81 (0.57, 1.15) | 0.228 | |
| S2 CHIS foreign-born (n = 11,439) | Household dysfunction factor | −0.375 | 0.056 | | | <0.001 | |
| S2 CHIS foreign-born | Physical/emotional abuse factor | −0.147 | 0.037 | | | <0.001 | |
| S2 CHIS foreign-born | Household mental illness | −0.217 | 0.072 | | 0.69 (0.54, 0.88) | 0.003 | |
| S2 CHIS foreign-born | Household drug use | −0.005 | 0.112 | | 0.99 (0.68, 1.44) | 0.967 | |
| S2 CHIS foreign-born | Household incarceration | 0.002 | 0.129 | | 1.00 (0.65, 1.54) | 0.990 | |

Holm-adjusted p-values for the six primary target tests: all ≤ 0.001. Replicates converged: BRFSS 100/100, CHIS 80/80.

## S4. Multigroup CFA by interview language (plan S3)

Source: `analysis/secondary/s3_fit.csv`, `s3_difftests.csv`, `s3_latent_means.csv`, `s3_score_tests.csv`. Binary items, theta parameterization, latent-response residual variances fixed at 1 in both groups. Scalar models: loadings and thresholds equal; Spanish latent means and variances free. Partial: as scalar but the three target items' loadings and thresholds free. Equality constraints were written explicitly because lavaan 0.7.2's `group.equal = "thresholds"` was not applied for these binary items (df checked: 38/50/44).

| Survey | Model | χ² (scaled) | df | CFI | RMSEA | SRMR |
|---|---|---:|---:|---:|---:|---:|
| BRFSS | configural | 317.3 | 38 | 0.983 | 0.0204 | 0.052 |
| BRFSS | scalar | 586.1 | 50 | 0.967 | 0.0246 | 0.056 |
| BRFSS | partial | 529.9 | 44 | 0.970 | 0.0250 | 0.055 |
| CHIS | configural | 487.8 | 38 | 0.982 | 0.0281 | 0.051 |
| CHIS | scalar | 698.5 | 50 | 0.973 | 0.0294 | 0.055 |
| CHIS | partial | 633.5 | 44 | 0.976 | 0.0299 | 0.052 |

| Survey | Comparison | Δχ² (scaled) | Δdf | p | ΔCFI | ΔRMSEA |
|---|---|---:|---:|---:|---:|---:|
| BRFSS | configural vs full scalar | 257.0 | 12 | <0.001 | −0.0160 | 0.0042 |
| BRFSS | configural vs partial scalar (targets free) | 190.4 | 6 | <0.001 | −0.0128 | 0.0046 |
| BRFSS | partial scalar vs full scalar | 79.5 | 6 | <0.001 | −0.0031 | −0.0004 |
| CHIS | configural vs full scalar | 217.9 | 12 | <0.001 | −0.0081 | 0.0013 |
| CHIS | configural vs partial scalar (targets free) | 139.1 | 6 | <0.001 | −0.0057 | 0.0018 |
| CHIS | partial scalar vs full scalar | 93.6 | 6 | <0.001 | −0.0024 | −0.0005 |

Latent mean of the Spanish-interview group (English = 0, SD 1): BRFSS scalar household dysfunction −0.605 (SE 0.052), abuse −0.453 (0.048); BRFSS partial −0.466 (0.060), −0.453 (0.048). CHIS scalar −0.674 (0.049), −0.449 (0.047); CHIS partial −0.578 (0.064), −0.449 (0.047).

**Score tests on the full scalar model** (eight largest per survey; one cross-group equality constraint per row):

| Survey | Constraint | χ² | scaled χ² | p (scaled) |
|---|---|---:|---:|---:|
| BRFSS | Verbal abuse: threshold | 121.2 | 217.1 | <0.001 |
| BRFSS | Household problem drinking: threshold | 112.7 | 129.5 | <0.001 |
| BRFSS | Physical abuse: threshold | 59.5 | 102.1 | <0.001 |
| BRFSS | Household mental illness: threshold | 54.7 | 61.2 | <0.001 |
| BRFSS | Household problem drinking: loading | 31.6 | 22.7 | <0.001 |
| BRFSS | Verbal abuse: loading | 25.0 | 38.2 | <0.001 |
| BRFSS | Witnessed parental violence: threshold | 13.4 | 22.9 | <0.001 |
| BRFSS | Household incarceration: threshold | 11.1 | 12.1 | <0.001 |
| CHIS | Physical abuse: threshold | 100.2 | 207.9 | <0.001 |
| CHIS | Household mental illness: threshold | 83.1 | 90.8 | <0.001 |
| CHIS | Verbal abuse: threshold | 82.5 | 147.3 | <0.001 |
| CHIS | Household problem drinking: threshold | 59.7 | 75.5 | <0.001 |
| CHIS | Physical abuse: loading | 38.8 | 56.4 | <0.001 |
| CHIS | Household incarceration: loading | 22.3 | 14.2 | <0.001 |
| CHIS | Household problem drinking: loading | 17.5 | 13.7 | <0.001 |
| CHIS | Verbal abuse: loading | 12.0 | 15.0 | <0.001 |

## S5. Anchor sensitivity and alignment (plan S4)

Source: `analysis/secondary/s4_effects.csv`, `s4b_purification_history.csv`, `s4d_alignment_*.csv`. lavaan weight-robust SEs.

| Survey | Analysis | Item | b | SE | p | OR-equiv. (95% CI) |
|---|---|---|---:|---:|---:|---|
| BRFSS | S4c one-at-a-time | Household problem drinking | 0.606 | 0.128 | <0.001 | 2.80 (1.83, 4.29) |
| BRFSS | S4c one-at-a-time | Parental separation/divorce | −0.255 | 0.050 | <0.001 | 0.65 (0.55, 0.77) |
| BRFSS | S4c one-at-a-time | Witnessed parental violence | 0.085 | 0.077 | 0.269 | 1.16 (0.89, 1.49) |
| BRFSS | S4c one-at-a-time | Physical abuse | 0.419 | 0.057 | <0.001 | 2.04 (1.69, 2.46) |
| BRFSS | S4c one-at-a-time | Verbal abuse | −0.691 | 0.078 | <0.001 | 0.31 (0.24, 0.40) |
| BRFSS | S4a one factor | Household mental illness | −0.677 | 0.086 | <0.001 | 0.32 (0.24, 0.42) |
| BRFSS | S4a one factor | Household drug use | −0.745 | 0.094 | <0.001 | 0.28 (0.21, 0.39) |
| BRFSS | S4a one factor | Household incarceration | −0.708 | 0.087 | <0.001 | 0.30 (0.22, 0.40) |
| BRFSS | S4b purified (freed: verbal, drinking, witnessed violence) | Household mental illness | −0.223 | 0.139 | 0.110 | 0.68 (0.43, 1.09) |
| BRFSS | S4b purified | Household drug use | −0.137 | 0.169 | 0.418 | 0.79 (0.45, 1.39) |
| BRFSS | S4b purified | Household incarceration | −0.219 | 0.138 | 0.113 | 0.69 (0.43, 1.09) |
| BRFSS | S4b purified | Verbal abuse | −0.872 | 0.089 | <0.001 | 0.23 (0.17, 0.30) |
| BRFSS | S4b purified | Household problem drinking | 0.606 | 0.128 | <0.001 | 2.80 (1.83, 4.30) |
| BRFSS | S4b purified | Witnessed parental violence | −0.289 | 0.085 | <0.001 | 0.61 (0.46, 0.81) |
| CHIS | S4c one-at-a-time | Household problem drinking | 0.247 | 0.125 | 0.048 | 1.52 (1.00, 2.31) |
| CHIS | S4c one-at-a-time | Parental separation/divorce | −0.092 | 0.045 | 0.042 | 0.86 (0.74, 0.99) |
| CHIS | S4c one-at-a-time | Witnessed parental violence | −0.186 | 0.057 | 0.001 | 0.73 (0.60, 0.88) |
| CHIS | S4c one-at-a-time | Physical abuse | 0.687 | 0.065 | <0.001 | 3.21 (2.59, 3.99) |
| CHIS | S4c one-at-a-time | Verbal abuse | −0.471 | 0.060 | <0.001 | 0.45 (0.37, 0.55) |
| CHIS | S4a one factor | Household mental illness | −0.517 | 0.058 | <0.001 | 0.42 (0.34, 0.50) |
| CHIS | S4a one factor | Household drug use | −0.547 | 0.082 | <0.001 | 0.39 (0.30, 0.52) |
| CHIS | S4a one factor | Household incarceration | −0.730 | 0.092 | <0.001 | 0.29 (0.21, 0.39) |
| CHIS | S4b purified (freed: physical abuse) | Household mental illness | −0.315 | 0.069 | <0.001 | 0.59 (0.47, 0.74) |
| CHIS | S4b purified | Household drug use | −0.266 | 0.102 | 0.009 | 0.64 (0.45, 0.89) |
| CHIS | S4b purified | Household incarceration | −0.493 | 0.109 | <0.001 | 0.43 (0.30, 0.62) |
| CHIS | S4b purified | Physical abuse | 0.687 | 0.065 | <0.001 | 3.21 (2.59, 3.99) |
| CHIS + nativity | S4c one-at-a-time | Household problem drinking | 0.133 | 0.150 | 0.374 | 1.25 (0.76, 2.06) |
| CHIS + nativity | S4c one-at-a-time | Parental separation/divorce | −0.048 | 0.054 | 0.370 | 0.92 (0.77, 1.10) |
| CHIS + nativity | S4c one-at-a-time | Witnessed parental violence | −0.191 | 0.070 | 0.006 | 0.72 (0.57, 0.91) |
| CHIS + nativity | S4c one-at-a-time | Physical abuse | 0.557 | 0.076 | <0.001 | 2.58 (2.00, 3.32) |
| CHIS + nativity | S4c one-at-a-time | Verbal abuse | −0.331 | 0.071 | <0.001 | 0.57 (0.45, 0.72) |

**Purification history** (flag: p < .01 and |b| ≥ 0.24; the largest flagged |b| freed each iteration, at least one anchor kept per factor): BRFSS iteration 1 flagged drinking, divorce, physical abuse, verbal abuse → freed verbal; iteration 2 flagged drinking, divorce, witnessed violence → freed drinking; iteration 3 flagged witnessed violence → freed; iteration 4 none. CHIS iteration 1 flagged physical abuse, verbal abuse → freed physical abuse; iteration 2 none.

**Alignment (anchor-free; Spanish − English aligned intercept on the probit scale; `sirt::invariance.alignment` on the configural two-group estimates, no covariates):**

| Survey | Factor | Item | Spanish − English |
|---|---|---|---:|
| BRFSS | Household dysfunction | Household mental illness | −0.47 |
| BRFSS | Household dysfunction | Household problem drinking | 0.47 |
| BRFSS | Household dysfunction | Household drug use | 0.01 |
| BRFSS | Household dysfunction | Household incarceration | −0.21 |
| BRFSS | Household dysfunction | Parental separation/divorce | −0.16 |
| BRFSS | Abuse | Witnessed parental violence | −0.01 |
| BRFSS | Abuse | Physical abuse | 0.05 |
| BRFSS | Abuse | Verbal abuse | −1.02 |
| CHIS | Household dysfunction | Household mental illness | −0.65 |
| CHIS | Household dysfunction | Household problem drinking | 0.00 |
| CHIS | Household dysfunction | Household drug use | 0.02 |
| CHIS | Household dysfunction | Household incarceration | −0.18 |
| CHIS | Household dysfunction | Parental separation/divorce | −0.11 |
| CHIS | Abuse | Witnessed parental violence | 0.00 |
| CHIS | Abuse | Physical abuse | 0.52 |
| CHIS | Abuse | Verbal abuse | −0.43 |

Aligned Spanish latent means (SD): BRFSS household dysfunction −0.578 (0.736), abuse −0.225 (1.078); CHIS household dysfunction −0.498 (0.905), abuse −0.409 (1.180). With only two groups alignment is weakly informative and is reported as a descriptive check.

## S6. Impact, mode and 11-item models; deviations from the plan

**S5 impact** (source: `analysis/secondary/s5_impact_*.csv`; 8 harmonized items; 50 simulation draws per respondent with common random numbers; replicate 95% CIs)

| Survey | Quantity | Observed | Model-implied (as estimated) | Target DIF removed | Change in gap | % of model-implied gap due to target DIF |
|---|---|---|---|---|---|---|
| BRFSS | Gap in mean 8-item count (Sp − En) | −0.95 (−1.03, −0.87) | −0.94 (−1.03, −0.86) | −0.80 (−0.90, −0.70) | 0.14 (0.11, 0.18) | 15.3 (11.1, 19.6) |
| BRFSS | Gap in % with ≥ 4 of 8 items (pp) | −14.8 (−16.5, −13.2) | −15.0 (−16.2, −13.8) | −12.2 (−13.7, −10.8) | 2.7 (2.1, 3.4) | 18.3 (13.4, 23.2) |
| CHIS | Gap in mean 8-item count (Sp − En) | −0.85 (−0.91, −0.79) | −0.84 (−0.90, −0.78) | −0.75 (−0.82, −0.68) | 0.09 (0.07, 0.11) | 10.3 (7.6, 13.1) |
| CHIS | Gap in % with ≥ 4 of 8 items (pp) | −12.7 (−14.0, −11.5) | −13.7 (−14.6, −12.7) | −12.1 (−13.1, −11.0) | 1.6 (1.2, 2.0) | 11.8 (8.6, 15.0) |

Spanish mean count / % ≥ 4: BRFSS observed 1.17 / 9.0%, model 1.19 / 8.6%, DIF removed 1.33 / 11.3% (English observed 2.12 / 23.8%). CHIS observed 1.29 / 11.1%, model 1.31 / 10.1%, DIF removed 1.39 / 11.7% (English observed 2.14 / 23.8%).

**S6 mode (CHIS)** (source: `analysis/secondary/s6_mode.csv`; Spanish × web interaction on the target direct effects; robust SEs)

| Item | Term | b | SE | p | OR-equiv. (95% CI) |
|---|---|---:|---:|---:|---|
| Household mental illness | Spanish direct effect, phone | −0.252 | 0.128 | 0.049 | 0.65 (0.43, 1.00) |
| Household drug use | Spanish direct effect, phone | −0.134 | 0.169 | 0.428 | 0.80 (0.45, 1.40) |
| Household incarceration | Spanish direct effect, phone | −0.144 | 0.173 | 0.404 | 0.78 (0.44, 1.39) |
| Household mental illness | Spanish direct effect, web | −0.316 | 0.077 | <0.001 | 0.58 (0.45, 0.76) |
| Household drug use | Spanish direct effect, web | −0.306 | 0.117 | 0.009 | 0.59 (0.40, 0.88) |
| Household incarceration | Spanish direct effect, web | −0.687 | 0.134 | <0.001 | 0.31 (0.20, 0.49) |
| Household mental illness | Spanish × web interaction | −0.064 | 0.141 | 0.649 | 0.90 (0.56, 1.44) |
| Household drug use | Spanish × web interaction | −0.172 | 0.190 | 0.365 | 0.75 (0.40, 1.40) |
| Household incarceration | Spanish × web interaction | −0.543 | 0.209 | 0.009 | 0.40 (0.20, 0.80) |
| Household mental illness | Web direct effect (English) | 0.129 | 0.065 | 0.048 | 1.24 (1.00, 1.55) |
| Household drug use | Web direct effect (English) | 0.039 | 0.087 | 0.654 | 1.07 (0.80, 1.43) |
| Household incarceration | Web direct effect (English) | −0.079 | 0.082 | 0.338 | 0.88 (0.67, 1.15) |

**S7 BRFSS 11 items, three-factor MIMIC** (source: `analysis/secondary/s7_effects.csv`; robust SEs)

| Parameter | b | SE | p | OR-equiv. (95% CI) | Δ endorsement (pp) |
|---|---:|---:|---:|---|---:|
| Physical/emotional abuse factor | −0.408 | 0.047 | <0.001 | | |
| Household dysfunction factor | −0.534 | 0.056 | <0.001 | | |
| Sexual abuse factor | −0.406 | 0.049 | <0.001 | | |
| Household drug use | −0.695 | 0.108 | <0.001 | 0.31 (0.21, 0.44) | −3.1 |
| Household incarceration | −0.655 | 0.092 | <0.001 | 0.33 (0.24, 0.45) | −5.4 |
| Household mental illness | −0.630 | 0.102 | <0.001 | 0.34 (0.24, 0.48) | −5.9 |

**Deviations from the frozen plan** (full text with reasons: `analysis/DEVIATIONS.md`)

1. BRFSS bootstrap: 749 single-PSU strata (of 2,837) were merged with the nearest multi-PSU stratum in the same year × file × state (or year × file) because Rao–Wu subbootstrap weights are undefined for 1-PSU strata; 2,088 bootstrap strata remained. Taylor-linearization analyses (Table 2) use the planned strata with lonely-PSU adjustment. Check: bootstrap SE of the weighted Spanish share 0.0054 vs 0.0058 by Taylor; of mental-illness prevalence 0.0044 vs 0.0041.
2. Integer PSU and stratum IDs were passed to `survey::as.svrepdesign` for speed; the algorithm is unchanged.
3. Clarifications fixed before fitting: BRFSS age DK/refused and education refused kept as categories; replicate variance with MSE = TRUE; two-sided Wald p; the partial-support rule read as the same items in both surveys (the alternative reading gives the same verdict); S3 binary-item identification; S4b one-item-per-iteration purification with at least one anchor per factor; S6 includes web main effects; S5 uses the 8 harmonized items; one labelled, non-pre-specified CHIS + nativity column added to Table 2.
4. Interpretive note (not a deviation): the plan assumed anchor bias could only be conservative; S4c shows problem drinking is over-endorsed in Spanish in BRFSS, so the primary BRFSS target estimates are not guaranteed to be conservative.

## S7. Exploratory analyses (not pre-specified; run 1 November 2026)

These analyses preceded the frozen plan and generated H1. They use approximate design-based variance (cluster-robust sandwich estimators; state × year or year × stratum × PSU clusters; no replicate weights) and were not corrected for multiplicity across analyses. Full results, scripts and caveats: `exploratory/*/RESULTS.md`, `scripts/exploratory/`.

### S7.1 BRFSS: logistic-regression DIF, two-parameter logistic anchor sensitivity, and the reconciliation of estimands

Source: `exploratory/dif/RESULTS.md`. Sample as in the main text (10,945 / 24,473), weights normalised to mean 1 within year.

**Logistic-regression DIF, matching on the rest score of the other 10 items (no covariates).** M1: item ~ S; M2: + Spanish; M3: + Spanish × S. Flag: BH-FDR q < .05 across 22 tests and ΔR² (M1→M2) ≥ .02 or ≥ 10% change in the rest-score coefficient.

| Item | Sp % | En % | Crude OR | Uniform-DIF OR [95% CI] | pp diff at matched score | ΔR² uniform | ΔR² non-uniform | Flag |
|---|---|---|---|---|---|---|---|---|
| Household mental illness | 4.2 | 22.2 | 0.15 | **0.21 [0.15, 0.29]** | −10.6 | 0.052 | 0.000 | yes |
| Household problem drinker | 16.8 | 25.5 | 0.59 | 1.06 [0.99, 1.12] | +0.6 | 0.000 | 0.001 | – |
| Household drug use | 3.2 | 14.5 | 0.19 | **0.33 [0.24, 0.44]** | −4.7 | 0.021 | 0.000 | yes |
| Household incarceration | 2.7 | 14.0 | 0.17 | **0.27 [0.19, 0.37]** | −5.8 | 0.031 | 0.000 | yes |
| Parents separated/divorced | 25.4 | 39.2 | 0.53 | 0.67 [0.54, 0.82] | −8.1 | 0.009 | 0.001 | – |
| Witnessed parental violence | 17.1 | 23.1 | 0.69 | 1.42 [1.25, 1.61] | +3.7 | 0.004 | 0.002 | – |
| Physical abuse | 30.2 | 34.1 | 0.84 | 1.50 [1.23, 1.83] | +6.9 | 0.007 | 0.005 | – |
| Verbal abuse | 17.7 | 40.9 | 0.31 | **0.42 [0.31, 0.55]** | −12.3 | 0.024 | 0.003 | yes |
| Sexual: touched | 6.8 | 13.9 | 0.45 | 1.06 [0.95, 1.19] | +0.3 | 0.000 | 0.008 | – |
| Sexual: made to touch | 6.0 | 10.7 | 0.53 | 1.34 [1.16, 1.53] | +1.2 | 0.002 | 0.005 | – |
| Sexual: forced sex | 4.4 | 6.8 | 0.64 | 1.98 [1.56, 2.53] | +1.9 | 0.009 | 0.005 | – |

With covariates (age, education, sex, income, year, state) the four ORs were 0.33, 0.34, 0.30 and 0.54; unweighted and purified (7-item matching) analyses flagged the same four items; recoding "parents not married" changed no OR by more than 0.02. Non-uniform DIF was negligible throughout (all ΔR² < .01).

**Two-group 2PL under alternative anchor sets** (uniform DIF OR at equal latent level; anchors constrained equal across groups; Spanish latent mean and SD free; point estimates only):

| Item | A1 purified 7 | A2 drinker only | A3 drink + divorce + sexual | A4 household 5 | X1 physical + witnessed (extreme) | X2 verbal + mental illness (extreme) |
|---|---|---|---|---|---|---|
| Household mental illness | 0.17 | 0.20 | 0.19 | *anchor* | 0.14 | *anchor* |
| Household problem drinker | *anchor* | *anchor* | *anchor* | *anchor* | 0.71 | 2.67 |
| Household drug use | 0.24 | 0.28 | 0.27 | *anchor* | 0.19 | 0.91 |
| Household incarceration | 0.22 | 0.24 | 0.24 | *anchor* | 0.18 | 0.61 |
| Parents separated/divorced | *anchor* | 0.67 | *anchor* | *anchor* | 0.58 | 1.02 |
| Witnessed parental violence | *anchor* | 1.30 | 1.32 | 3.63 | *anchor* | 3.97 |
| Physical abuse | *anchor* | 1.58 | 1.65 | 3.78 | *anchor* | 4.06 |
| Verbal abuse | 0.33 | 0.39 | 0.40 | 1.23 | 0.25 | *anchor* |
| Sexual: touched | *anchor* | 0.95 | *anchor* | 8.27 | 0.45 | 9.22 |
| Sexual: made to touch | *anchor* | 1.31 | *anchor* | 11.87 | 0.61 | 13.08 |
| Sexual: forced sex | *anchor* | 1.91 | *anchor* | 16.82 | 0.90 | 18.64 |
| *Spanish latent mean (English SD units)* | −0.38 | −0.46 | −0.52 | −1.00 | −0.23 | −1.06 |

The items fall into two clusters with different language gaps. Under anchors drawn from the small-gap cluster (A1–A3), the four large-gap items have ORs of 0.17–0.40 and the latent deficit is 0.4–0.5 SD; under household anchors (A4), the abuse and sexual items appear over-endorsed by ORs of 3.6–16.8 and the deficit is 1.0 SD. Internal data cannot choose between these. DIF-corrected Spanish 4+ prevalence ranges from 5.4% to 19.3% across anchor sets (observed 10.7%; English 25.5%); under A1–A3 it is 13.8–15.8%.

**Reconciling the odds ratios across analyses.** For household mental illness in BRFSS the repository reports a crude OR of 0.17, a rest-score logistic DIF OR of 0.21 (0.33 with covariates), 2PL ORs of 0.17–0.20, a MIMIC primary OR-equivalent of 0.35, and a MIMIC purified OR-equivalent of 0.68. These differ because they are different estimands: the logistic and 2PL analyses condition on a single dimension defined by all other items (including the abuse and sexual items, which anchor the latent deficit at 0.4–0.5 SD), whereas the MIMIC conditions on a separate household-dysfunction factor whose language effect is identified by drinking and divorce only, adjusts for covariates, and reports exp(1.7β) from a probit model. The purified MIMIC is relative to divorce alone. The ordering is the same in every analysis: mental illness, incarceration, drug use and verbal abuse are the most under-endorsed items relative to the rest.

**Spanish wording period.** The 2019 and 2020 CDC Spanish versions differed on the witnessed-violence item, and the 2021–2025 Spanish text is unpublished. The witnessed-violence DIF fell from 2019 to 2020 (OR ratio 0.64–0.76, p = .005–.08) as the wording change would predict, but items with unchanged wording moved as much (verbal abuse ×1.4–1.6; forced sex ×0.55–0.66). The four flagged items showed the same direction in all three periods. No wording effect is identifiable.

### S7.2 BRFSS: respondents' own mental-health reports versus the household item

Source: `exploratory/brfss_mh/RESULTS.md`. Sample A: Hispanic ACE-module respondents 2019–2025 (11,995 Spanish / 27,468 English; all valid responses per item). Adjusted for age, sex, education, income, state and year; clusters = year × stratum × PSU; weights normalised within year.

| Measure | wt% Spanish / English | Crude OR (95% CI) | Adjusted OR (95% CI) |
|---|---|---|---|
| ACE: lived with depressed/mentally ill/suicidal | 4.4 / 22.8 | 0.16 (0.13–0.19) | 0.20 (0.15–0.25) |
| ACE: lived with someone incarcerated | 2.8 / 14.5 | 0.17 (0.14–0.21) | 0.16 (0.12–0.21) |
| ACE: lived with drug user | 3.4 / 14.8 | 0.20 (0.17–0.25) | 0.20 (0.16–0.24) |
| ACE: sworn at/insulted | 18.4 / 41.8 | 0.32 (0.28–0.35) | 0.37 (0.32–0.42) |
| ACE: physically hurt by parent/adult | 31.3 / 35.0 | 0.84 (0.77–0.93) | 0.80 (0.70–0.91) |
| Own depression diagnosis | 9.3 / 19.3 | 0.43 (0.37–0.49) | 0.33 (0.28–0.40) |
| Frequent mental distress (≥ 14 poor mental-health days) | 10.5 / 16.1 | 0.61 (0.53–0.70) | 0.51 (0.43–0.62) |
| PHQ-8 ≥ 10 (2010–11 module, non-ACE states) | 9.4 / 11.8 | 0.78 (0.52–1.16) | 0.32 (0.21–0.49) |
| Fair/poor general health | 35.0 / 16.6 | 2.70 (2.44–2.99) | 1.18 (1.02–1.36) |

Ratio of adjusted ORs, household mental illness vs comparator, same respondents, stacked model: vs own depression diagnosis 0.59 (0.45–0.78); vs frequent mental distress 0.37 (0.29–0.48); vs physical abuse 0.24 (0.19–0.32); vs incarceration 1.22 (0.89–1.67). Adding own depression diagnosis and frequent mental distress to the household-item model moved its aOR from 0.19 to 0.25. The same item cluster replicated in BRFSS 2009–2012 (mental illness 0.24, drugs 0.23, incarceration 0.18), where Spanish respondents reported *more* physical abuse (aOR 1.44). Puerto Rico 2024 (Spanish interviews, n ≈ 4,150, descriptive): household mental illness 12.6%, own depression 18.1%, versus mainland Spanish 4.4% and 9.3%; Spanish administration per se does not suppress endorsement to mainland-Spanish levels.

**Differential prediction** (weighted logistic regression of the outcome on predictor × Spanish plus covariates; BRFSS complete-case sample):

| Outcome | Predictor | OR English (95% CI) | OR Spanish (95% CI) | Interaction p |
|---|---|---|---|---|
| Own depression diagnosis | ACE score (0–8) | 1.40 (1.36–1.44) | 1.41 (1.30–1.52) | 0.92 |
| Own depression diagnosis | Household mental-illness item | 4.63 (3.99–5.36) | 5.93 (3.70–9.51) | 0.33 |
| Frequent mental distress | ACE score (0–8) | 1.31 (1.27–1.35) | 1.35 (1.24–1.46) | 0.51 |
| Frequent mental distress | Household mental-illness item | 3.20 (2.76–3.70) | 4.14 (2.36–7.28) | 0.38 |

### S7.3 CHIS: exploratory odds ratios, mode and differential prediction

Source: `exploratory/chis/RESULTS.md`. Jackknife replicate SEs. Covariates: age, sex, education, poverty level, year; "+ nativity" adds US-born and percent of life in the US. The DIF column conditions on the sum of the other seven non-sexual items.

| Item | Sp % | En % | aOR | aOR + nativity (95% CI) | aOR, foreign-born only | Logistic DIF OR (rest score + nativity) |
|---|---|---|---|---|---|---|
| Household mental illness | 5.6 | 23.8 | 0.30 | 0.41 (0.34–0.49) | 0.44 (0.35–0.55) | 0.50 (0.40–0.62) |
| Household drug use | 4.6 | 14.5 | 0.28 | 0.45 (0.38–0.55) | 0.56 (0.43–0.73) | 0.63 (0.50–0.79) |
| Household incarceration | 2.6 | 13.1 | 0.19 | 0.40 (0.30–0.53) | 0.54 (0.35–0.82) | 0.57 (0.41–0.80) |
| Household problem drinker | 18.4 | 30.1 | 0.51 | 0.59 (0.54–0.66) | 0.64 (0.56–0.73) | 0.74 (0.65–0.83) |
| Parents separated/divorced | 21.0 | 30.5 | 0.61 | 0.71 (0.63–0.80) | 0.78 (0.67–0.91) | 0.80 (0.71–0.91) |
| Witnessed parental violence | 20.4 | 27.6 | 0.61 | 0.63 (0.56–0.72) | 0.69 (0.60–0.80) | 0.84 (0.73–0.96) |
| Physical abuse | 29.4 | 28.5 | 1.00 | 0.97 (0.88–1.07) | 1.09 (0.96–1.23) | 1.51 (1.33–1.71) |
| Verbal abuse | 27.3 | 45.8 | 0.53 | 0.60 (0.54–0.66) | 0.70 (0.62–0.80) | 0.74 (0.66–0.84) |
| 4+ ACEs | 13.6 | 26.1 | 0.48 | 0.58 (0.51–0.67) | 0.72 (0.61–0.86) | — |
| Serious psychological distress (K6, past month) | 4.9 | 11.2 | 0.48 | 0.58 (0.48–0.71) | 0.65 (0.52–0.81) | — |
| Fair/poor general health | 35.9 | 17.8 | 1.38 | 1.73 (1.53–1.95) | 1.81 (1.56–2.10) | — |

Spanish-vs-English ORs within mode (adjusted incl. nativity): household mental illness 0.31 phone / 0.44 web (interaction p = .13); drug use 0.29 / 0.48 (.44); incarceration 0.43 / 0.32 (.08); physical abuse 1.08 / 0.95 (.56). Differential prediction of serious psychological distress: OR per ACE 1.37 (English) vs 1.45 (Spanish), p = .29; household mental-illness item 3.29 vs 3.10, p = .75.

### S7.4 NSCH 2022–2024: Hispanic children in Spanish- versus English-primary-language households

Source: `exploratory/nsch_chis/RESULTS.md`. Census NSCH topical public-use files (current edited releases). Hispanic children (SC_HISPANIC_R = 1) in English- or Spanish-primary-language households (HHLANGUAGE; other/missing excluded, n = 756). Pooled 2022–2024: 16,676 English and 6,919 Spanish households (weighted Spanish share 40.4%). Weighted logistic regression (FWC) with sandwich SEs clustered on state (51 clusters; strata ignored); poverty level multiply imputed (6 implicates, Rubin's rules). M3 (primary): child age group, sex, year, highest adult education, poverty level and household generation. Sensitivity: first- and second-generation households only. Item contrasts: ratio of the M3 ORs for two items with a joint cluster sandwich.

Language and generation are heavily confounded: 0.4% of English-language vs 14.2% of Spanish-language households were first-generation, 27.9% vs 68.5% second-generation; 78.8% of responding adults in Spanish-language households were born outside the US; 38.9% had less than a high-school education (vs 6.0%).

| Measure | English HH % | Spanish HH % | Crude OR | aOR M3 (95% CI) | aOR, 1st/2nd-gen HH only |
|---|---|---|---|---|---|
| **ACE8: lived with anyone mentally ill, suicidal, severely depressed** | 9.6 | 2.9 | 0.28 (0.21–0.36) | **0.32 (0.21–0.49)** | 0.34 (0.20–0.57) |
| ACE9: lived with anyone with alcohol/drug problem | 9.6 | 4.5 | 0.44 (0.33–0.58) | 0.47 (0.32–0.69) | 0.59 (0.40–0.87) |
| ACE6: saw/heard adults hit each other at home | 6.3 | 2.7 | 0.40 (0.33–0.49) | 0.38 (0.31–0.45) | 0.46 (0.35–0.62) |
| ACE5: parent/guardian served time in jail | 7.5 | 2.5 | 0.32 (0.26–0.38) | 0.33 (0.24–0.43) | 0.36 (0.24–0.54) |
| ACE3: parent/guardian divorced/separated | 25.8 | 19.7 | 0.71 (0.58–0.87) | 0.73 (0.61–0.88) | 0.81 (0.67–0.98) |
| ACE4: parent/guardian died | 3.2 | 2.4 | 0.75 (0.54–1.04) | 0.58 (0.43–0.78) | 0.91 (0.58–1.44) |
| ACE7: victim/witness of neighborhood violence | 4.8 | 4.3 | 0.88 (0.68–1.14) | 0.57 (0.36–0.88) | 0.93 (0.52–1.66) |
| ACE10: treated unfairly because of race/ethnicity | 5.4 | 3.8 | 0.70 (0.57–0.85) | 0.77 (0.62–0.96) | 0.97 (0.72–1.29) |
| ACE1: hard to cover basics somewhat/very often | 17.0 | 19.3 | 1.16 (1.07–1.26) | 0.85 (0.73–0.99) | 1.04 (0.88–1.23) |
| **Responding adult's own mental health fair/poor** | 9.1 | 4.1 | 0.43 (0.36–0.50) | **0.39 (0.32–0.47)** | 0.46 (0.36–0.58) |
| Comparator: responding adult's physical health fair/poor | 9.1 | 9.8 | 1.08 (0.91–1.29) | 0.69 (0.57–0.83) | 0.79 (0.68–0.93) |
| Child depression, ever (age 3–17) | 5.8 | 4.5 | 0.77 (0.52–1.13) | 1.03 (0.78–1.36) | 1.36 (0.93–1.97) |
| Child anxiety, current (age 3–17) | 11.0 | 5.6 | 0.48 (0.39–0.59) | 0.59 (0.48–0.73) | 0.73 (0.60–0.88) |
| Comparator: ADHD, ever (age 3–17) | 11.3 | 5.9 | 0.49 (0.35–0.68) | 0.64 (0.42–0.98) | 0.85 (0.54–1.32) |
| Comparator: asthma, ever | 11.0 | 9.2 | 0.82 (0.76–0.89) | 0.99 (0.84–1.17) | 1.01 (0.86–1.18) |

ACE8 by year (English vs Spanish households, weighted %): 2022 10.1 vs 3.4; 2023 10.0 vs 2.9; 2024 8.5 vs 2.4.

Item contrasts (M3, ratio of ORs): ACE8 vs ACE9 (alcohol/drugs) 0.68 (0.52–0.89, p = .005); ACE8 vs ACE5 (jail) 0.98 (0.62–1.55); ACE8 vs ACE6 (domestic violence) 0.85 (0.51–1.42); ACE8 vs ACE3 (divorce) 0.44 (0.33–0.58); ACE8 vs mean of all nine other ACE items 0.53 (0.36–0.78, p = .001); parent mental health fair/poor vs parent physical health fair/poor 0.56 (0.47–0.67, p < .001); child current anxiety vs asthma 0.60 (0.50–0.72); child anxiety vs ADHD 0.92 (0.62–1.38).

Item nonresponse: Spanish-language households skipped every ACE item about 2 percentage points more often than English-language households (ACE8 7.0% vs 5.2%; other ACE items 7.0–7.6% vs 5.0–5.6%; parent mental health 6.6% vs 4.5%), with no mental-health-specific skipping.

Caveats: household language is a proxy for the language the questionnaire was completed in; NSCH ACEs are parent reports about the child's lifetime and the household item can include the respondent; NSCH has no abuse items; generation is a coarse acculturation adjustment and nearly collinear with language.

## S8. Literature search summary

Full logs with query strings and hit counts: `notes/01_novelty_verification_2026-11-01.md` and `notes/05_novelty_H1_2026-11-02.md`. Searches (1–2 November 2026): PubMed (E-utilities, 18 queries), Europe PMC full text including preprints (13 queries), OpenAlex (works, dissertations, preprints), Crossref posted content, Harvard DASH, and general web searches including Spanish- and Portuguese-language terms. SciELO, LILACS/BVS and Redalyc blocked programmatic access and were covered only indirectly; ProQuest was not searched directly.

| Novelty component | Verdict | Closest prior work |
|---|---|---|
| Item-level language DIF of ACE items in BRFSS | Not found | Alhalel 2018 (marginal prevalence by questionnaire language); Mei 2022, Ford 2014 (invariance, language untested); Umoga 2026 (race/ethnicity, embargoed); Zhang & Lippert 2026 (2PL scoring; full text unread) |
| Language DIF of ACE items in CHIS | Not found; no psychometric study of the CHIS ACE items | Kim 2016 (K6 DIF by language in CHIS) |
| Negative DIF concentrated in household mental illness, drug use and incarceration | Not found as a conditional finding or as a named mechanism | Same-direction prevalence precursors (Alhalel 2018; Grest 2021); contrary: Jensen 2024 (no raised Hispanic threshold for household mental illness in NSCH), LaBrenz 2019 (withdrawn SSWR abstract; no language difference on household items, unconditional tests), HCHS/SOL high endorsement (Llabre 2017) |
| Replication across independent Spanish translations | Not found | MacFadyen 2023 (qualitative Spanish cognitive testing of a BRFSS-derived PRAMS item set; no Spanish-specific problems) |
| Language DIF persisting after nativity adjustment | Not found for ACE items | Cooper & Nickodem 2021 (all-foreign-born; nativity constant); Kobayashi 2024 (language and nativity as covariates only) |

Residual risks to the novelty claim: the embargoed Umoga 2026 dissertation (full text unavailable until April 2027) and Zhang & Lippert 2026 (paywalled; abstract reports IRT scoring without group-specific parameters).
