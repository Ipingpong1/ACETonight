# H1 confirmatory analysis: results

Plan: `/home/mo2273/ace_manuscript/prereg/H1_analysis_plan.md`, frozen 2026-11-02T06:38:47Z, SHA-256 `031cd72089936e1d4f332bbdbab7071fa6100b346b778cda34480571b3d420fa` (verified, unchanged). Analysis run 2026-11-02. Samples: BRFSS 2019-2025 Hispanic adults, 10,945 Spanish-interview / 24,473 English-interview; CHIS 2021-2025 Hispanic adults, 5,536 / 24,418 (both exactly as expected in the plan).

## 1. H1 verdict (pre-specified decision rule)

**H1: SUPPORTED.** Rule: all three direct effects < 0 with Holm-adjusted p < .05 (6 tests) and b ≤ −0.24 in both surveys = supported; ≥ 2 items in both surveys or all 3 in one survey = partially supported; otherwise not supported.

| Survey | Target item | b (probit) | replicate SE | 95% CI | OR-equiv. (95% CI) | p | Holm p | b ≤ −0.24 | Meets all | Model-implied Δ endorsement, Spanish (pp, 95% CI) |
|---|---|---:|---:|---|---|---:|---:|---|---|---|
| BRFSS | Household drug use | -0.696 | 0.118 | -0.927, -0.466 | 0.31 (0.21, 0.45) | <0.001 | <0.001 | yes | **yes** | -3.1 (-4.2, -2.0) |
| BRFSS | Household incarceration | -0.655 | 0.088 | -0.826, -0.483 | 0.33 (0.25, 0.44) | <0.001 | <0.001 | yes | **yes** | -5.2 (-6.6, -3.8) |
| BRFSS | Household mental illness | -0.624 | 0.114 | -0.848, -0.401 | 0.35 (0.24, 0.51) | <0.001 | <0.001 | yes | **yes** | -6.0 (-7.9, -4.1) |
| CHIS | Household drug use | -0.266 | 0.082 | -0.426, -0.106 | 0.64 (0.48, 0.83) | 0.001 | 0.001 | yes | **yes** | -1.5 (-2.4, -0.6) |
| CHIS | Household incarceration | -0.493 | 0.086 | -0.662, -0.324 | 0.43 (0.32, 0.58) | <0.001 | <0.001 | yes | **yes** | -2.9 (-3.8, -1.9) |
| CHIS | Household mental illness | -0.315 | 0.051 | -0.416, -0.214 | 0.59 (0.49, 0.70) | <0.001 | <0.001 | yes | **yes** | -4.4 (-5.8, -3.1) |

Items meeting every criterion in both surveys: Household drug use, Household incarceration, Household mental illness. Per survey: BRFSS 3/3, CHIS 3/3. The verdict is the same under both readings of the partial-support rule.

Language → factor effects (replicate SEs): BRFSS Physical/emotional abuse factor b = -0.408 (SE 0.049, 95% CI -0.504 to -0.312); BRFSS Household dysfunction factor b = -0.537 (SE 0.061, 95% CI -0.656 to -0.418); CHIS Physical/emotional abuse factor b = -0.270 (SE 0.025, 95% CI -0.318 to -0.222); CHIS Household dysfunction factor b = -0.601 (SE 0.037, 95% CI -0.673 to -0.528). Variance: CHIS jackknife (80 RAKEDW replicates, scale 1, MSE); BRFSS 100 Rao-Wu rescaled bootstrap replicates (subbootstrap; singleton strata collapsed, see Deviations). Replicates converged: BRFSS 100/100, CHIS 80/80. Lavaan weight-robust SEs for the same parameters are in `primary_results.csv` (se_lavaan).

## 2. Summary and caveats

- **The confirmatory test passes.** In the primary MIMIC, all six target direct effects are negative, Holm-significant and beyond the b ≤ −0.24 threshold (BRFSS b = -0.62, -0.70, -0.65; CHIS b = -0.31, -0.27, -0.49 for mental illness, drug use, incarceration). The weakest is CHIS drug use, whose point estimate only just passes the magnitude criterion (its 95% CI includes values above −0.24).
- **H1b fails.** After adding nativity and % of life in the US (CHIS S1), only household mental illness keeps a significant negative direct effect (b = -0.23, p <0.001). Drug use (b = -0.07, p = 0.469) and incarceration (b = -0.13, p = 0.228) do not. The same pattern holds among foreign-born respondents only (S2): mental illness b = -0.22, drugs -0.00, incarceration 0.00. In CHIS, therefore, the drug-use and incarceration DIF is largely accounted for by nativity, i.e. it may reflect real exposure differences tied to immigration rather than language-specific reporting.
- **Anchor dependence (BRFSS).** The plan assumed anchor bias could only be conservative, i.e. that anchors would at worst be under-reported in Spanish. S4c contradicts this in BRFSS: problem drinking, a primary anchor, is *over*-endorsed in Spanish relative to the factor (b = 0.61, OR-equiv. 2.80), while separation/divorce is under-endorsed (b = -0.26). Pre-specified purification (S4b) freed verbal+drink+ipv, leaving divorce as the only household anchor. In that model the BRFSS target effects shrink to b = -0.22 / -0.14 / -0.22 (p = 0.110 / 0.418 / 0.113). The magnitude of the BRFSS primary estimates therefore depends on treating problem drinking as invariant. In CHIS the household anchors show smaller relative DIF (drinking b = 0.25, p = 0.048; divorce -0.09, p = 0.042). Neither met the purification criterion, and S4b, which freed only physical abuse, leaves the CHIS target estimates unchanged.
- **Anchor-free alignment (S4d, household factor; Spanish − English aligned intercepts).** Mental illness BRFSS -0.47 / CHIS -0.65; incarceration -0.21 / -0.18; drug use 0.01 / 0.02; problem drinking 0.47 / 0.00. The anchor-free check thus supports negative DIF for mental illness, gives weaker support for incarceration and none for drug use.
- **DIF is not specific to the three target items.** The full scalar MGCFA is rejected in both surveys. Freeing the target items does not restore fit, and score tests flag thresholds of verbal abuse, problem drinking and physical abuse as strongly as mental illness. Verbal abuse is strongly under-endorsed in Spanish (S4c b = -0.69 BRFSS, -0.47 CHIS), and physical abuse is over-endorsed (b = 0.42, 0.69).
- **Mode (CHIS S6).** The target DIF is present in self-administered web interviews (b = -0.32, -0.31, -0.69) and is not larger with an interviewer present. The Spanish × web interaction is significant only for incarceration (larger DIF on the web, p = 0.009). Interviewer presence therefore does not explain the DIF.
- **Impact (S5).** Setting the target direct effects to zero would close 15.3% (BRFSS) and 10.3% (CHIS) of the model-implied Spanish−English gap in the mean 8-item count, and 18.3% / 11.8% of the gap in ≥ 4 items. Most of the observed gap would remain. Because these figures inherit the primary model's anchor assumption, the BRFSS figure is an upper-range estimate given the S4b result.

## 3. Model fit (WLSMV, theta; reported, not decision criteria)

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

Scaled (mean- and variance-adjusted) indices. Robust CFI/RMSEA (Savalei) are not available from lavaan for these conditional.x models with sampling weights. CFI/TLI here are computed against a baseline that is conditional on the covariates.

## 4. Descriptive tables

### Table 1. Sample characteristics by interview language (Hispanic adults)

**BRFSS 2019-2025** (English interview n = 24,473; Spanish interview n = 10,945)

| Characteristic | English n | English % (wtd) | Spanish n | Spanish % (wtd) |
|---|---:|---:|---:|---:|
| *Age group* | | | | |
| 18-24 | 4,175 | 21.7 | 747 | 8.5 |
| 25-34 | 5,186 | 22.9 | 2,126 | 19.0 |
| 35-44 | 4,536 | 18.9 | 2,687 | 23.6 |
| 45-54 | 3,731 | 13.9 | 2,154 | 18.3 |
| 55-64 | 3,202 | 12.3 | 1,565 | 15.0 |
| 65+ | 3,450 | 9.6 | 1,625 | 15.4 |
| Don't know/refused | 193 | 0.8 | 41 | 0.3 |
| *Sex* | | | | |
| Male | 11,873 | 50.7 | 4,880 | 44.5 |
| Female | 12,600 | 49.3 | 6,065 | 55.5 |
| *Education* | | | | |
| Never attended/kindergarten | 43 | 0.2 | 307 | 2.4 |
| Grades 1-8 | 571 | 3.4 | 3,665 | 36.3 |
| Grades 9-11 | 1,468 | 8.9 | 1,899 | 21.8 |
| Grade 12/GED | 7,425 | 29.9 | 2,856 | 23.4 |
| College 1-3 years | 7,218 | 33.1 | 948 | 8.6 |
| College 4+ years | 7,692 | 24.1 | 1,149 | 6.7 |
| Refused | 56 | 0.3 | 121 | 1.0 |
| *Household income* | | | | |
| <$15,000 | 1,644 | 6.8 | 2,115 | 22.2 |
| $15,000-24,999 | 2,934 | 11.5 | 2,920 | 25.4 |
| $25,000-34,999 | 2,664 | 10.7 | 1,694 | 14.2 |
| $35,000-49,999 | 3,277 | 12.6 | 1,052 | 9.6 |
| $50,000+ | 10,463 | 44.2 | 625 | 6.2 |
| Missing/DK/refused | 3,491 | 14.2 | 2,539 | 22.4 |
| *Survey year* | | | | |
| 2019 | 4,371 | 14.0 | 1,726 | 11.9 |
| 2020 | 7,607 | 36.2 | 2,995 | 40.6 |
| 2021 | 2,675 | 9.3 | 1,124 | 7.9 |
| 2022 | 2,581 | 10.9 | 1,214 | 9.7 |
| 2023 | 2,638 | 10.9 | 1,641 | 11.7 |
| 2024 | 2,634 | 11.3 | 883 | 9.1 |
| 2025 | 1,967 | 7.4 | 1,362 | 9.1 |
| *Census region* | | | | |
| Northeast | 3,498 | 18.0 | 2,056 | 19.7 |
| Midwest | 5,038 | 12.0 | 2,368 | 6.8 |
| South | 8,638 | 42.8 | 4,441 | 43.1 |
| West | 7,299 | 27.2 | 2,080 | 30.5 |

**CHIS 2021-2025** (English interview n = 24,418; Spanish interview n = 5,536)

| Characteristic | English n | English % (wtd) | Spanish n | Spanish % (wtd) |
|---|---:|---:|---:|---:|
| *Age group* | | | | |
| 18-25 | 2,755 | 25.4 | 189 | 5.9 |
| 26-34 | 3,778 | 20.0 | 449 | 9.4 |
| 35-44 | 4,476 | 17.6 | 1,029 | 22.9 |
| 45-54 | 4,247 | 14.3 | 1,388 | 24.9 |
| 55-64 | 4,321 | 11.8 | 1,347 | 20.4 |
| 65+ | 4,841 | 10.9 | 1,134 | 16.5 |
| *Sex* | | | | |
| Male | 9,789 | 49.7 | 2,190 | 47.1 |
| Female | 14,629 | 50.3 | 3,346 | 52.9 |
| *Education* | | | | |
| No formal education or grades 1-8 | 660 | 7.0 | 1,428 | 39.9 |
| Grades 9-11 | 777 | 8.7 | 741 | 22.7 |
| Grade 12/high school diploma | 4,263 | 31.4 | 1,386 | 23.8 |
| Some college | 4,515 | 13.7 | 555 | 4.5 |
| Vocational school | 2,006 | 4.7 | 404 | 2.3 |
| AA/AS degree | 2,205 | 5.8 | 121 | 0.8 |
| BA/BS degree or some graduate school | 6,137 | 18.7 | 692 | 4.7 |
| MA/MS degree | 2,923 | 7.6 | 142 | 1.0 |
| PhD or equivalent | 932 | 2.4 | 67 | 0.4 |
| *Poverty level (FPL)* | | | | |
| 0-99% FPL | 3,659 | 18.5 | 1,848 | 35.0 |
| 100-199% FPL | 4,305 | 20.4 | 1,833 | 32.7 |
| 200-299% FPL | 3,509 | 15.4 | 845 | 15.2 |
| 300%+ FPL | 12,945 | 45.7 | 1,010 | 17.1 |
| *Survey year* | | | | |
| 2021 | 4,921 | 20.2 | 1,105 | 20.3 |
| 2022 | 4,581 | 20.5 | 1,136 | 19.7 |
| 2023 | 4,934 | 20.8 | 1,064 | 19.3 |
| 2024 | 5,482 | 19.2 | 1,324 | 19.9 |
| 2025 | 4,500 | 19.3 | 907 | 20.8 |
| *Nativity* | | | | |
| Born in US | 18,113 | 72.3 | 402 | 7.8 |
| Born outside US | 6,305 | 27.7 | 5,134 | 92.2 |
| *Percent of life in US* | | | | |
| 0-20% | 230 | 1.2 | 606 | 10.3 |
| 21-40% | 494 | 2.2 | 964 | 15.4 |
| 41-60% | 1,094 | 5.8 | 1,959 | 36.6 |
| 61-80% | 2,040 | 10.1 | 1,457 | 27.4 |
| 81-100% (incl. all US-born) | 20,560 | 80.7 | 550 | 10.3 |
| *Interview mode* | | | | |
| Phone (interviewer) | 3,104 | 13.3 | 1,844 | 34.1 |
| Web (self-administered) | 21,314 | 86.7 | 3,692 | 65.9 |
| *English proficiency* | | | | |
| Speaks only English | 9,669 | 32.4 | 29 | 0.5 |
| Very well/well | 14,070 | 62.3 | 2,640 | 40.1 |
| Not well/not at all | 679 | 5.4 | 2,867 | 59.4 |

n = unweighted count; % = weighted column percentage (BRFSS final weight / 7; CHIS RAKEDW0 / 5). Age groups are collapsed for display only; models use the native 5-year groups (BRFSS _AGEG5YR 1-13 plus DK/refused; CHIS SRAGE_P1 14 groups).

### Table 2. Weighted prevalence of ACE items by interview language and Spanish-vs-English prevalence ratios

**BRFSS 2019-2025** (Taylor linearization; strata = year x file x _STSTR, PSU = _PSU, nest = TRUE, lonely PSU = adjust)

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

**CHIS 2021-2025** (jackknife replicate weights RAKEDW1-80, scale 1, MSE)

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

Prevalence CIs: logit-transformed design-based intervals (svyciprop). PR = Spanish vs English prevalence ratio from a survey-weighted Poisson working model (log link), Wald 95% CI. Adjusted: BRFSS age group, sex, education, income (missing as category), survey year, Census region; CHIS age group, sex, education, poverty level, survey year. 4+ ACEs: standard 8-category score including sexual abuse (BRFSS: any of the 3 sexual items; CHIS: ACE8 = 4+). *Not pre-specified for Table 2; added as context for H1b (adds born outside US and percent of life in US).

## 5. Secondary analyses

### S1 (H1b): CHIS + nativity and % life in US; S2: CHIS foreign-born only (jackknife replicate SEs)

| Analysis | Parameter | b | replicate SE | p | OR-equiv. (95% CI) | lavaan SE |
|---|---|---:|---:|---:|---|---:|
| S1 + nativity, % life in US (n = 29,954; Spanish 5,536) | Household mental illness | -0.231 | 0.059 | <0.001 | 0.67 (0.55, 0.82) | 0.080 |
| S1 + nativity, % life in US (n = 29,954; Spanish 5,536) | Household drug use | -0.066 | 0.091 | 0.469 | 0.89 (0.66, 1.21) | 0.123 |
| S1 + nativity, % life in US (n = 29,954; Spanish 5,536) | Household incarceration | -0.128 | 0.106 | 0.228 | 0.81 (0.57, 1.15) | 0.135 |
| S1 + nativity, % life in US (n = 29,954; Spanish 5,536) | Household dysfunction factor | -0.441 | 0.041 | <0.001 |  | 0.059 |
| S1 + nativity, % life in US (n = 29,954; Spanish 5,536) | Physical/emotional abuse factor | -0.234 | 0.030 | <0.001 |  | 0.042 |
| S2 foreign-born only (n = 11,439; Spanish 5,134) | Household mental illness | -0.217 | 0.072 | 0.003 | 0.69 (0.54, 0.88) | 0.090 |
| S2 foreign-born only (n = 11,439; Spanish 5,134) | Household drug use | -0.005 | 0.112 | 0.967 | 0.99 (0.68, 1.44) | 0.133 |
| S2 foreign-born only (n = 11,439; Spanish 5,134) | Household incarceration | 0.002 | 0.129 | 0.990 | 1.00 (0.65, 1.54) | 0.144 |
| S2 foreign-born only (n = 11,439; Spanish 5,134) | Household dysfunction factor | -0.375 | 0.056 | <0.001 |  | 0.068 |
| S2 foreign-born only (n = 11,439; Spanish 5,134) | Physical/emotional abuse factor | -0.147 | 0.037 | <0.001 |  | 0.046 |

**H1b: NOT SUPPORTED** (pre-specified: all three CHIS direct effects < 0 with p < .05 after adjusting for nativity and % of life in the US).

### S3: multigroup CFA by interview language (WLSMV, theta, weights; no covariates)

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
| BRFSS | configural vs full scalar | 257.0 | 12 | <0.001 | -0.0160 | 0.0042 |
| BRFSS | configural vs partial scalar (targets free) | 190.4 | 6 | <0.001 | -0.0128 | 0.0046 |
| BRFSS | partial scalar vs full scalar | 79.5 | 6 | <0.001 | -0.0031 | -0.0004 |
| CHIS | configural vs full scalar | 217.9 | 12 | <0.001 | -0.0081 | 0.0013 |
| CHIS | configural vs partial scalar (targets free) | 139.1 | 6 | <0.001 | -0.0057 | 0.0018 |
| CHIS | partial scalar vs full scalar | 93.6 | 6 | <0.001 | -0.0024 | -0.0005 |

Latent mean of the Spanish-interview group (English = 0, SD 1): BRFSS scalar HD -0.605 (SE 0.052); BRFSS scalar AB -0.453 (SE 0.048); BRFSS partial HD -0.466 (SE 0.060); BRFSS partial AB -0.453 (SE 0.048); CHIS scalar HD -0.674 (SE 0.049); CHIS scalar AB -0.449 (SE 0.047); CHIS partial HD -0.578 (SE 0.064); CHIS partial AB -0.449 (SE 0.047).

Score tests on the full scalar model, the 8 largest per survey (univariate, 1 df; each row is one cross-group equality constraint on an item threshold or loading):

| Survey | Constraint (parameter) | χ² | scaled χ² | p (scaled) |
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

### S4: anchor sensitivity (lavaan weight-robust SEs)

| Survey | Analysis | Item | b | SE | p | OR-equiv. (95% CI) |
|---|---|---|---:|---:|---:|---|
| BRFSS | S4c one-at-a-time | Household problem drinking | 0.606 | 0.128 | <0.001 | 2.80 (1.83, 4.29) |
| BRFSS | S4c one-at-a-time | Parental separation/divorce | -0.255 | 0.050 | <0.001 | 0.65 (0.55, 0.77) |
| BRFSS | S4c one-at-a-time | Witnessed parental violence | 0.085 | 0.077 | 0.269 | 1.16 (0.89, 1.49) |
| BRFSS | S4c one-at-a-time | Physical abuse | 0.419 | 0.057 | <0.001 | 2.04 (1.69, 2.46) |
| BRFSS | S4c one-at-a-time | Verbal abuse | -0.691 | 0.078 | <0.001 | 0.31 (0.24, 0.40) |
| BRFSS | S4a one factor | Household mental illness | -0.677 | 0.086 | <0.001 | 0.32 (0.24, 0.42) |
| BRFSS | S4a one factor | Household drug use | -0.745 | 0.094 | <0.001 | 0.28 (0.21, 0.39) |
| BRFSS | S4a one factor | Household incarceration | -0.708 | 0.087 | <0.001 | 0.30 (0.22, 0.40) |
| BRFSS | S4b purified anchors (freed: verbal+drink+ipv) | Household mental illness | -0.223 | 0.139 | 0.110 | 0.68 (0.43, 1.09) |
| BRFSS | S4b purified anchors (freed: verbal+drink+ipv) | Household drug use | -0.137 | 0.169 | 0.418 | 0.79 (0.45, 1.39) |
| BRFSS | S4b purified anchors (freed: verbal+drink+ipv) | Household incarceration | -0.219 | 0.138 | 0.113 | 0.69 (0.43, 1.09) |
| BRFSS | S4b purified anchors (freed: verbal+drink+ipv) | Verbal abuse | -0.872 | 0.089 | <0.001 | 0.23 (0.17, 0.30) |
| BRFSS | S4b purified anchors (freed: verbal+drink+ipv) | Household problem drinking | 0.606 | 0.128 | <0.001 | 2.80 (1.83, 4.30) |
| BRFSS | S4b purified anchors (freed: verbal+drink+ipv) | Witnessed parental violence | -0.289 | 0.085 | <0.001 | 0.61 (0.46, 0.81) |
| CHIS | S4c one-at-a-time | Household problem drinking | 0.247 | 0.125 | 0.048 | 1.52 (1.00, 2.31) |
| CHIS | S4c one-at-a-time | Parental separation/divorce | -0.092 | 0.045 | 0.042 | 0.86 (0.74, 0.99) |
| CHIS | S4c one-at-a-time | Witnessed parental violence | -0.186 | 0.057 | 0.001 | 0.73 (0.60, 0.88) |
| CHIS | S4c one-at-a-time | Physical abuse | 0.687 | 0.065 | <0.001 | 3.21 (2.59, 3.99) |
| CHIS | S4c one-at-a-time | Verbal abuse | -0.471 | 0.060 | <0.001 | 0.45 (0.37, 0.55) |
| CHIS | S4a one factor | Household mental illness | -0.517 | 0.058 | <0.001 | 0.42 (0.34, 0.50) |
| CHIS | S4a one factor | Household drug use | -0.547 | 0.082 | <0.001 | 0.39 (0.30, 0.52) |
| CHIS | S4a one factor | Household incarceration | -0.730 | 0.092 | <0.001 | 0.29 (0.21, 0.39) |
| CHIS | S4b purified anchors (freed: phys) | Household mental illness | -0.315 | 0.069 | <0.001 | 0.59 (0.47, 0.74) |
| CHIS | S4b purified anchors (freed: phys) | Household drug use | -0.266 | 0.102 | 0.009 | 0.64 (0.45, 0.89) |
| CHIS | S4b purified anchors (freed: phys) | Household incarceration | -0.493 | 0.109 | <0.001 | 0.43 (0.30, 0.62) |
| CHIS | S4b purified anchors (freed: phys) | Physical abuse | 0.687 | 0.065 | <0.001 | 3.21 (2.59, 3.99) |
| CHIS + nativity | S4c one-at-a-time | Household problem drinking | 0.133 | 0.150 | 0.374 | 1.25 (0.76, 2.06) |
| CHIS + nativity | S4c one-at-a-time | Parental separation/divorce | -0.048 | 0.054 | 0.370 | 0.92 (0.77, 1.10) |
| CHIS + nativity | S4c one-at-a-time | Witnessed parental violence | -0.191 | 0.070 | 0.006 | 0.72 (0.57, 0.91) |
| CHIS + nativity | S4c one-at-a-time | Physical abuse | 0.557 | 0.076 | <0.001 | 2.58 (2.00, 3.32) |
| CHIS + nativity | S4c one-at-a-time | Verbal abuse | -0.331 | 0.071 | <0.001 | 0.57 (0.45, 0.72) |

S4b purification history (p < .01 and |b| ≥ 0.24 flags; the largest flagged |b| was freed each iteration): BRFSS iteration 1 (already freed: none): flagged drink, divorce, phys, verbal; BRFSS iteration 2 (already freed: verbal): flagged drink, divorce, ipv; BRFSS iteration 3 (already freed: verbal+drink): flagged ipv; BRFSS iteration 4 (already freed: verbal+drink+ipv): flagged none; CHIS iteration 1 (already freed: none): flagged phys, verbal; CHIS iteration 2 (already freed: phys): flagged none.

S4d alignment (anchor-free; Spanish − English aligned intercept, probit scale, per factor): BRFSS AB: Witnessed parental violence -0.01, Physical abuse 0.05, Verbal abuse -1.02; BRFSS HD: Household mental illness -0.47, Household problem drinking 0.47, Household drug use 0.01, Household incarceration -0.21, Parental separation/divorce -0.16; CHIS AB: Witnessed parental violence 0.00, Physical abuse 0.52, Verbal abuse -0.43; CHIS HD: Household mental illness -0.65, Household problem drinking 0.00, Household drug use 0.02, Household incarceration -0.18, Parental separation/divorce -0.11.
  - BRFSS AB: aligned Spanish latent mean -0.225, SD 1.078; invariance R² loadings 0.998, intercepts 0.940.
  - BRFSS HD: aligned Spanish latent mean -0.578, SD 0.736; invariance R² loadings 0.988, intercepts 0.994.
  - CHIS AB: aligned Spanish latent mean -0.409, SD 1.180; invariance R² loadings 0.999, intercepts 0.970.
  - CHIS HD: aligned Spanish latent mean -0.498, SD 0.905; invariance R² loadings 0.978, intercepts 0.991.

### S5: impact on the Spanish-English gap (8 harmonized items; replicate 95% CIs)

| Survey | Quantity | Observed | Model-implied (as estimated) | Model-implied, target DIF removed | Change in gap | % of model-implied gap due to target DIF |
|---|---|---|---|---|---|---|
| BRFSS | Gap in mean 8-item count (Sp − En) | -0.95 (-1.03, -0.87) | -0.94 (-1.03, -0.86) | -0.80 (-0.90, -0.70) | 0.14 (0.11, 0.18) | 15.3 (11.1, 19.6) |
| BRFSS | Gap in % with ≥ 4 of 8 items (pp) | -14.8 (-16.5, -13.2) | -15.0 (-16.2, -13.8) | -12.2 (-13.7, -10.8) | 2.7 (2.1, 3.4) | 18.3 (13.4, 23.2) |
| BRFSS | Spanish mean count / % ≥ 4: observed; model; DIF removed | 1.17 / 9.0% | 1.19 / 8.6% | 1.33 / 11.3% | English: obs 2.12 / 23.8%; model 2.13 / 23.6% | |
| CHIS | Gap in mean 8-item count (Sp − En) | -0.85 (-0.91, -0.79) | -0.84 (-0.90, -0.78) | -0.75 (-0.82, -0.68) | 0.09 (0.07, 0.11) | 10.3 (7.6, 13.1) |
| CHIS | Gap in % with ≥ 4 of 8 items (pp) | -12.7 (-14.0, -11.5) | -13.7 (-14.6, -12.7) | -12.1 (-13.1, -11.0) | 1.6 (1.2, 2.0) | 11.8 (8.6, 15.0) |
| CHIS | Spanish mean count / % ≥ 4: observed; model; DIF removed | 1.29 / 11.1% | 1.31 / 10.1% | 1.39 / 11.7% | English: obs 2.14 / 23.8%; model 2.14 / 23.8% | |

### S6: interview mode (CHIS; Spanish × web interaction on the target direct effects; lavaan robust SEs)

| Item | Term | b | SE | p | OR-equiv. (95% CI) |
|---|---|---:|---:|---:|---|
| Household mental illness | Spanish direct effect, phone | -0.252 | 0.128 | 0.049 | 0.65 (0.43, 1.00) |
| Household drug use | Spanish direct effect, phone | -0.134 | 0.169 | 0.428 | 0.80 (0.45, 1.40) |
| Household incarceration | Spanish direct effect, phone | -0.144 | 0.173 | 0.404 | 0.78 (0.44, 1.39) |
| Household mental illness | Spanish direct effect, web | -0.316 | 0.077 | <0.001 | 0.58 (0.45, 0.76) |
| Household drug use | Spanish direct effect, web | -0.306 | 0.117 | 0.009 | 0.59 (0.40, 0.88) |
| Household incarceration | Spanish direct effect, web | -0.687 | 0.134 | <0.001 | 0.31 (0.20, 0.49) |
| Household mental illness | Spanish x web interaction | -0.064 | 0.141 | 0.649 | 0.90 (0.56, 1.44) |
| Household drug use | Spanish x web interaction | -0.172 | 0.190 | 0.365 | 0.75 (0.40, 1.40) |
| Household incarceration | Spanish x web interaction | -0.543 | 0.209 | 0.009 | 0.40 (0.20, 0.80) |
| Household mental illness | Web direct effect (English) | 0.129 | 0.065 | 0.048 | 1.24 (1.00, 1.55) |
| Household drug use | Web direct effect (English) | 0.039 | 0.087 | 0.654 | 1.07 (0.80, 1.43) |
| Household incarceration | Web direct effect (English) | -0.079 | 0.082 | 0.338 | 0.88 (0.67, 1.15) |

### S7: BRFSS 11 items, three-factor MIMIC (lavaan robust SEs)

| Parameter | b | SE | p | OR-equiv. (95% CI) | Model-implied Δ endorsement (pp) |
|---|---:|---:|---:|---|---:|
| Physical/emotional abuse factor | -0.408 | 0.047 | <0.001 |  |  |
| Household dysfunction factor | -0.534 | 0.056 | <0.001 |  |  |
| Sexual abuse factor | -0.406 | 0.049 | <0.001 |  |  |
| Household drug use | -0.695 | 0.108 | <0.001 | 0.31 (0.21, 0.44) | -3.1 |
| Household incarceration | -0.655 | 0.092 | <0.001 | 0.33 (0.24, 0.45) | -5.4 |
| Household mental illness | -0.630 | 0.102 | <0.001 | 0.34 (0.24, 0.48) | -5.9 |

## 6. Deviations and clarifications

Full list with reasons: `analysis/DEVIATIONS.md`. In brief:
- **Deviations:** (1) For the BRFSS Rao-Wu bootstrap only, 749 single-PSU strata were collapsed into the nearest multi-PSU stratum in the same year × file × state, because subbootstrap weights are undefined for 1-PSU strata. Taylor analyses use the planned strata with lonely PSU = adjust. (2) Integer PSU/stratum IDs were passed to `as.svrepdesign`; this is a speed-only change to the same algorithm.
- **No deviation needed:** Ford et al. (2014) places witnessed parental violence on the abuse factor, as planned. lavaan 0.7.2 supports WLSMV with sampling weights for ordered items, so no fallback was used.
- **Clarifications** (open details fixed before fitting): missing BRFSS age/education kept as categories; replicate variance MSE = TRUE; two-sided Wald p; the partial-support rule was read as the same items in both surveys (alternative reading reported); S3 binary-item identification; S4b one-item-per-iteration purification; S6 includes web main effects; S5 uses 8 harmonized items; Table 2 has one extra, labelled CHIS + nativity column.
- **Implementation note (S3):** lavaan 0.7.2 did not apply `group.equal = "thresholds"` for these binary items (scalar df 44 instead of 50; latent means stayed fixed). The MGCFA models were therefore re-specified with explicit equality labels and verified by their df (38/50/44). The first S3 run is marked superseded in STATUS.md; only the corrected run is reported.

## 7. Files

- Scripts: `/home/mo2273/ace_manuscript/scripts/` (`common.R`, `01_prep.R`, `02_table1.R`, `03_table2.R`, `04_primary_mimic.R`, `04b_verdict.R`, `05_secondary.R`, `06_s5_impact.R`, `make_figures.py`, `make_results.py`, `run.sh`)
- Analytic data: `analysis/data/brfss_analytic.{rds,csv}`, `analysis/data/chis_analytic.{rds,csv}`, `analysis/data/brfss_boot100_weights.rds`
- Tables: `analysis/table1.{csv,md}`, `analysis/table2.{csv,md}`
- Primary: `analysis/primary_results.{csv,md}`, `analysis/H1_verdict.json`, `analysis/primary/` (fits, all parameters, replicate coefficient matrices, fit indices, logs)
- Secondary: `analysis/secondary/` (`effects_s1.csv`, `effects_s2.csv`, `h1b_verdict.json`, `s3_*.csv`, `s4_effects.csv`, `s4b_purification_history.csv`, `s4d_alignment_*.csv`, `s5_impact_*.csv`, `s6_mode.csv`, `s7_effects.csv`)
- Figures: `figures/fig1_item_prevalence_by_language`, `fig2_dif_estimates_all_items`, `fig3_robustness_target_dif`, `fig4_impact_gap` (each .png at 300 dpi, .pdf and .csv of the plotted numbers)
- Log: `analysis/STATUS.md`; deviations: `analysis/DEVIATIONS.md`
