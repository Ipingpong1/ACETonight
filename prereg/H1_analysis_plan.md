# Pre-specified analysis plan: H1 (stigmatized household conditions)

Frozen 2026-11-02 (UTC timestamp and SHA-256 recorded in `H1_analysis_plan.sha256.txt`) before any of the confirmatory models below were fitted. Intended for registration on OSF using the secondary-data preregistration template.

## Disclosure of prior exposure to the data

On 2026-11-01 the authors ran exploratory analyses of the same data:
- weighted item prevalence by interview language;
- logistic-regression item-level DIF with a rest score;
- two-group 2PL models under several anchor sets;
- odds ratios adjusted step by step for covariates.

Those analyses suggested H1. They are not confirmatory and are reported as exploratory (`/home/mo2273/ace_tonight/`). None of the latent-variable models specified below (MIMIC, MGCFA, replicate-weight variance) had been fitted when this plan was frozen.

## Hypothesis

**H1.** Among Hispanic adults, Spanish-interview respondents are less likely than English-interview respondents to endorse three household-dysfunction items. This holds at the same level of the latent household-dysfunction factor and the same covariate values. The three items describe stigmatized conditions of household members:
- mental illness (BRFSS ACEDEPRS / CHIS AQ1);
- illicit drug use (ACEDRUGS / AQ3);
- incarceration (ACEPRISN / AQ4).

The comparison is relative to the non-stigmatized household items, problem drinking and parental separation/divorce. In other words, the three items show negative uniform DIF by interview language.

**H1b (key secondary).** In CHIS, the negative DIF for the three items remains (direct effect < 0, p < .05) after additionally adjusting for nativity (born in the US) and percent of life lived in the US.

## Data and samples

- **BRFSS 2019–2025** public-use files, including the questionnaire-version files (V1–V3). Main and version files are de-duplicated as in `/home/mo2273/ace_tonight_scripts/dif/build_dif_data.py`.
  - Sample: Hispanic adults in the 50 states and DC (territories excluded), interviewed in English (QSTLANG = 1) or Spanish (QSTLANG = 2), with valid responses on all 11 ACE items.
  - Expected n = 10,945 Spanish and 24,473 English.
  - Analytic file: `/home/mo2273/ace_tonight/dif/dif_analytic_hisp_2019_2025.csv`.
- **CHIS 2021–2025** adult public-use files.
  - Sample: Hispanic adults (OMBSRR_P1 = 1) interviewed in English or Spanish (INTVLNGC_P1 = 1 or 2).
  - Expected n = 5,536 Spanish and 24,418 English.
  - Analytic file: `/home/mo2273/ace_tonight/chis/chis_pooled.csv`.

## Items and coding (harmonized, binary)

1 = endorsed:
- household mental illness (ACEDEPRS / AQ1 = yes);
- problem drinking (ACEDRINK / AQ2 = yes);
- drug use (ACEDRUGS / AQ3 = yes);
- incarceration (ACEPRISN / AQ4 = yes);
- separation/divorce (ACEDIVRC / AQ5 = yes; "parents not married" = 0);
- witnessed parental violence (ACEPUNCH / AQ6 once or more);
- physical abuse (ACEHURT / AQ7 once or more);
- verbal abuse (ACESWEAR / AQ8 once or more).

The BRFSS-only secondary model adds the three sexual abuse items (each once or more).

## Measurement model

Two correlated factors following Ford et al. (2014):
- **Household dysfunction:** mental illness, drinking, drugs, incarceration, separation/divorce.
- **Physical/emotional abuse:** witnessed parental violence, physical abuse, verbal abuse.

If Ford et al.'s published structure places an item differently, Ford's placement is used and the deviation is recorded. The BRFSS 11-item secondary model adds a sexual-abuse factor.

## Primary analysis (tests H1)

The primary analysis is a MIMIC model:
- Estimator WLSMV, theta parameterization, survey weights.
- Both factors regressed on Spanish interview (1/0) and covariates: age group, sex, education, income (BRFSS; missing as a category) or poverty level (CHIS), and survey year. BRFSS also includes Census region.
- Direct effects of Spanish interview on the three target items (= uniform DIF).
- Anchors: all other items (no direct effects). The household factor's language effect is therefore identified by problem drinking and separation/divorce.

If those anchors are themselves under-reported in Spanish, the target DIF estimates are biased toward zero, i.e. conservatively.

- **Effect size:** the direct effect b on the probit scale. Report an approximate odds-ratio equivalent, exp(1.7·b), and the model-implied difference in endorsement probability for Spanish-interview respondents with versus without the direct effect.
- **Decision rule:** H1 is supported if, in both surveys, all three direct effects are negative, Holm-adjusted p < .05 across the 6 tests (3 items × 2 surveys), and b ≤ −0.24 (≈ OR ≤ 0.67).
  - Partially supported: these criteria hold for at least 2 items in both surveys, or for all 3 items in one survey.
  - Not supported: otherwise.
- **Variance:** design-based replicate variance for the target direct effects.
  - CHIS: jackknife with RAKEDW1–80 (multiplier 1, MSE).
  - BRFSS: 100 bootstrap replicates (Rao–Wu rescaled), strata = year × file × _STSTR, PSU = _PSU, lonely PSUs adjusted.
  - Fallback if replicate refits are infeasible: lavaan's weight-robust standard errors, with that limitation stated.
- **Fit indices** (CFI, TLI, RMSEA, SRMR) are reported but are not decision criteria.

## Pre-specified secondary analyses

- **S1. Nativity (CHIS).** Primary model plus nativity and percent of life in the US as covariates (tests H1b).
- **S2. Foreign-born only (CHIS).** Primary model plus percent of life in the US, foreign-born respondents only.
- **S3. Multigroup CFA by interview language** (WLSMV, theta parameterization, weights). Fit configural, full scalar (loadings and thresholds equal) and partial scalar (target items' loadings and thresholds free) models. Report:
  - scaled chi-square difference tests and ΔCFI/ΔRMSEA;
  - latent mean differences under full vs partial scalar;
  - score tests on the full scalar model, to show which constraints are most violated without reference to H1.
- **S4. Anchor sensitivity:**
  - (a) one-factor model of the 8 items, all 5 non-target items as anchors;
  - (b) purified anchors: iteratively free any non-target item whose freed direct effect has p < .01 and |b| ≥ 0.24;
  - (c) each non-target item freed one at a time, to produce a DIF estimate for every item;
  - (d) alignment optimization, if available, as an anchor-free check.
- **S5. Impact.** Model-implied, simulation-based change in the Spanish–English gap in mean ACE count and in 4+ ACE prevalence if Spanish-interview respondents' target-item direct effects were zero.
- **S6. Mode (CHIS).** Spanish × web-interview interaction on the target direct effects.
- **S7. BRFSS 11 items.** Three-factor (11-item) MIMIC with the same target items.

## Descriptive analyses

- Weighted prevalence of each item by interview language.
- Design-based adjusted prevalence ratios (Poisson working model) with the same covariates.

## Deviations

Any deviation from this plan is listed in the manuscript.
