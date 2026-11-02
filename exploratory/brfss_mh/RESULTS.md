# BRFSS: Spanish- vs English-interview differences among Hispanic respondents in own mental-health reports vs ACE items (first pass, 2026-11-01)

**Question.** Hispanic respondents interviewed in Spanish rarely endorse ACEDEPRS ("lived with anyone depressed, mentally ill, or suicidal"). Is that a mental-health-specific reporting gap, and does it also appear in respondents' reports about their *own* mental health?

**Short answer.** Spanish-interview Hispanics do report much less of their own mental-health burden: own depression diagnosis has an adjusted OR (aOR) of 0.33–0.34, frequent mental distress 0.43–0.51, PHQ-8≥10 0.32, life dissatisfaction 0.28 and stress 0.43. **But the ACEDEPRS gap (aOR 0.20) is not mental-health-specific.**
- It is about as large as the gaps for the other two "stigmatized household member" items: drug use (aOR 0.20) and incarceration (aOR 0.16).
- It is significantly larger than the gap in own depression (ratio of ORs 0.59) and in frequent mental distress (0.37).
- Conditioning on a respondent's own depression and distress barely changes it.
- ACEs predict own depression and distress equally well in both languages, so there is no differential prediction.

## Methods (brief)
- **Data.** CDC BRFSS public XPT files. The mental-health variables were re-extracted from the original zips (`extract_mh.py`) and merged on `_STATE`+`SEQNO` to the existing ACE/covariate extracts.
- **ACE respondents and coding.** Main-file vs version-file dedup and all ACE coding are reused verbatim from `analyze_ace_language.py`. Mental-health values come from the *same* file (main or Vk) as the ACE row, so version-only states keep their version weights.
- **Validation.** Unweighted ACE endorsement counts reproduce the earlier `brfss_ace_endorsement_hispanic_by_language.csv` exactly (e.g., ACEDEPRS 514/11,880 Spanish and 6,207/26,827 English, 2019–25, territories excluded).
- **Sample.** Hispanic (`_HISPANC`=1 for 2019+, `HISPANC2`=1 for ≤2012). QSTLANG 1=English, 2=Spanish. Territories (PR/VI/GU) are excluded; PR is reported separately.
- **Outcomes** (codes checked in the codebooks):
  - Depression diagnosis: ADDEPEV3 (2019+), ADDEPEV2 (2011–12) or ADDEPEV (2010 module); 1 vs 2.
  - Frequent mental distress (FMD): `_MENT14D`=3 vs 1–2. For ≤2012 it is computed as MENTHLTH ≥14.
  - Poor mental-health days: MENTHLTH, with 88→0 and 77/99→missing.
  - K6 (2009/2012 Mental Illness & Stigma module): MIS items scored 1=All→4 through 5=None→0. All 6 items required; serious distress = K6≥13.
  - PHQ-8 (2010/2011 Anxiety & Depression module): days 88→0; 0–1 days→0, 2–6→1, 7–11→2, 12–14→3. All 8 items required; current depression = PHQ-8≥10.
  - Anxiety diagnosis: ADANXEV.
  - Social Determinants module (2022+): LSATISFY 3–4, EMTSUPRT 4–5, SDLONELY 1–2, SDHSTRE1 1–2. SDHSTRE1 exists only in 2022–23 and SDLONELY only in 2023–25.
  - The ACE items and the 8-category score are coded as in prior work.
- **Models.** Weighted logistic GLM (Gaussian for days). Final weights are rescaled to mean 1 within each survey year of each analysis sample; main and version-file weights of a year share the same state-population scale.
  - **Adjusted models** include age group (6 + missing), sex, education (4 + missing), income (5 + missing), state FE and year FE. Year FE are dropped automatically when year is nested in state (the 2010+2011 module sample).
  - **SEs** are cluster-robust on year×stratum×PSU. This is an *approximate* design-based linearization that ignores stratification. A manual sandwich reproduces the statsmodels SE exactly (0.12911).
- **Ratios of ORs** come from stacked models (same respondents, all covariates interacted with outcome, clustered).

## N table (unweighted; Hispanic, mainland)

| Analysis | Spanish | English | wt% Spanish | States | Years |
|---|---|---|---|---|---|
| A: ACE-module respondents | 11,995 | 27,468 | 35.5 | 42 | 2019–25 |
| A, complete on 11 ACE items (differential prediction) | 10,945 | 24,473 | 36.3 | 42 | 2019–25 |
| B: all Hispanic BRFSS respondents (core questions) | 81,960 | 164,857 | 35.3 | 51 | 2019–25 |
| C: ACE-module respondents (mostly CA 2011 landline, NC 2012) | 2,492 | 4,141 | 45.7 | 18 | 2009–12 |
| D1: K6 module respondents (K6 valid), all states | 2,128 | 6,194 | 38.2 | 19 | 2009, 2012 |
| D1a: …who were also ACE respondents | **79** (4 K6≥13) | 115 | | 1 (IA) | 2012 |
| D2: PHQ-8 module respondents, all states | 848 | 4,404 | 21.2 | 14 | 2010, 2011 |
| D2a: …who were also ACE respondents | **36** (5 PHQ≥10) | 699 | | 4 (Sp: NV only) | 2010 |
| A: Social Determinants (SDOH) items (life satisfaction / support / loneliness / stress) | 2,795 / 2,782 / 1,726 / 2,355 | 5,757 / 5,745 / 3,822 / 3,834 | | 13–16 | 2022–25 |
| B: same SDOH items | 20,713 / 20,379 / 14,567 / 12,157 | 42,209 / 42,061 / 27,601 / 26,218 | | 41–45 | 2022–25 |

The K6 and PHQ-8 modules were **effectively not co-fielded with ACE** among Spanish-interview Hispanics: 2009 ACE states (AR, LA) did not field K6, and only 36–79 Spanish respondents overlap. Within-person K6/PHQ-8 vs ACEDEPRS comparisons are therefore not feasible. The D1 and D2 rows below use all module respondents (non-ACE states) to show how symptom scales behave by language.

## Key table: Spanish vs English interview, Hispanic respondents
Prevalences use year-normalized weights. OR < 1 means Spanish-interview respondents report less. The aOR adjusts for age, sex, education, income, state and year. The mean-days row gives a difference in days instead of an OR. The full table with p-values is in `key_or_table.csv`.

| Sample | Measure | n Sp / En | wt% Sp / En | Crude OR (95% CI) | **Adjusted OR (95% CI)** |
|---|---|---|---|---|---|
| **A (ACE resp. 2019–25)** | **ACE: lived w/ depressed/mentally ill/suicidal (ACEDEPRS)** | 11,880 / 26,827 | 4.4 / 22.8 | 0.16 (0.13–0.19) | **0.20 (0.15–0.25)** |
| A | ACE: lived w/ someone incarcerated | 11,879 / 26,936 | 2.8 / 14.5 | 0.17 (0.14–0.21) | **0.16 (0.12–0.21)** |
| A | ACE: lived w/ drug user | 11,871 / 26,888 | 3.4 / 14.8 | 0.20 (0.17–0.25) | **0.20 (0.16–0.24)** |
| A | ACE: sworn at/insulted | 11,693 / 26,479 | 18.4 / 41.8 | 0.32 (0.28–0.35) | 0.37 (0.32–0.42) |
| A | ACE: touched sexually | 11,673 / 26,391 | 7.3 / 14.2 | 0.47 (0.41–0.55) | 0.43 (0.34–0.53) |
| A | ACE: made to touch sexually | 11,673 / 26,422 | 6.4 / 11.0 | 0.55 (0.46–0.65) | 0.49 (0.39–0.62) |
| A | ACE: forced sex | 11,659 / 26,393 | 4.7 / 7.0 | 0.65 (0.54–0.79) | 0.50 (0.39–0.62) |
| A | ACE: any sexual abuse | 11,622 / 26,292 | 10.3 / 16.5 | 0.58 (0.50–0.67) | 0.51 (0.42–0.62) |
| A | ACE: parents separated/divorced | 11,725 / 26,785 | 26.1 / 40.3 | 0.52 (0.48–0.58) | 0.50 (0.44–0.57) |
| A | ACE: household substance use (drink or drugs) | 11,853 / 26,885 | 19.1 / 31.6 | 0.51 (0.46–0.57) | 0.50 (0.44–0.58) |
| A | ACE: lived w/ problem drinker | 11,876 / 26,958 | 17.7 / 26.6 | 0.59 (0.53–0.66) | 0.59 (0.52–0.68) |
| A | ACE: witnessed adults hit each other | 11,632 / 26,280 | 17.5 / 23.5 | 0.69 (0.62–0.77) | 0.61 (0.52–0.70) |
| A | ACE: physically hurt by parent/adult | 11,688 / 26,489 | 31.3 / 35.0 | 0.84 (0.77–0.93) | 0.80 (0.70–0.91) |
| A | ACE score (8-category) ≥4 | 10,945 / 24,473 | 10.7 / 25.5 | 0.35 (0.31–0.40) | 0.33 (0.28–0.40) |
| A | **Own depression diagnosis** | 11,925 / 27,292 | 9.3 / 19.3 | 0.43 (0.37–0.49) | **0.33 (0.28–0.40)** |
| A | **Frequent mental distress** | 11,549 / 26,965 | 10.5 / 16.1 | 0.61 (0.53–0.70) | **0.51 (0.43–0.62)** |
| A | Mean poor-mental-health days | 11,549 / 26,965 | 3.1 / 5.1 d | −2.0 d (−2.4, −1.6) | −2.5 d (−3.0, −2.0) |
| A | Dissatisfied with life (2022–25) | 2,795 / 5,757 | 3.3 / 7.6 | 0.43 (0.29–0.64) | 0.29 (0.19–0.45) |
| A | Stress always/usually (2022–23) | 2,355 / 3,834 | 12.2 / 19.2 | 0.61 (0.47–0.79) | 0.43 (0.32–0.58) |
| A | Emotional support rarely/never (2022–25) | 2,782 / 5,745 | 12.5 / 11.0 | 1.19 (0.93–1.52) | 0.63 (0.45–0.88) |
| A | Lonely always/usually (2023–25) | 1,726 / 3,822 | 17.6 / 9.4 | 2.04 (1.56–2.67) | 1.32 (0.90–1.93) |
| A | Fair/poor general health | 11,931 / 27,398 | 35.0 / 16.6 | 2.70 (2.44–2.99) | 1.18 (1.02–1.36) |
| **B (all Hisp. 2019–25)** | **Own depression diagnosis** | 81,440 / 163,820 | 9.2 / 20.1 | 0.40 (0.38–0.42) | **0.34 (0.32–0.37)** |
| B | **Frequent mental distress** | 79,073 / 161,629 | 9.5 / 17.3 | 0.50 (0.47–0.53) | **0.43 (0.40–0.46)** |
| B | Mean poor-mental-health days | 79,073 / 161,629 | 2.9 / 5.4 d | −2.4 d (−2.6, −2.3) | −2.8 d (−3.0, −2.6) |
| B | Dissatisfied with life | 20,713 / 42,209 | 3.1 / 6.9 | 0.43 (0.37–0.51) | 0.28 (0.23–0.34) |
| B | Stress always/usually | 12,157 / 26,218 | 10.7 / 18.0 | 0.55 (0.48–0.62) | 0.44 (0.37–0.51) |
| B | Emotional support rarely/never | 20,379 / 42,061 | 14.3 / 13.0 | 1.14 (1.03–1.26) | 0.61 (0.52–0.70) |
| B | Lonely always/usually | 14,567 / 27,601 | 11.7 / 8.9 | 1.37 (1.22–1.55) | 0.87 (0.73–1.03) |
| B | Fair/poor general health | 81,576 / 164,471 | 34.8 / 17.9 | 2.45 (2.35–2.55) | 1.23 (1.17–1.30) |
| **C (ACE resp. 2009–12)** | ACEDEPRS | 2,144 / 3,895 | 4.8 / 17.6 | 0.24 (0.17–0.33) | **0.24 (0.16–0.37)** |
| C | ACE: lived w/ drug user | 2,157 / 3,905 | 3.8 / 15.1 | 0.22 (0.15–0.32) | 0.23 (0.14–0.36) |
| C | ACE: lived w/ someone incarcerated (CA 2011 did not ask) | 1,139 / 2,916 | 3.7 / 12.7 | 0.24 (0.15–0.37) | 0.18 (0.10–0.31) |
| C | ACE: parents separated/divorced | 2,146 / 3,900 | 19.3 / 32.8 | 0.49 (0.40–0.60) | 0.41 (0.32–0.54) |
| C | ACE: household substance use | 2,157 / 3,901 | 25.7 / 35.0 | 0.64 (0.53–0.77) | 0.50 (0.38–0.65) |
| C | ACE: any sexual abuse | 2,136 / 3,846 | 10.3 / 15.4 | 0.63 (0.50–0.81) | 0.64 (0.45–0.91) |
| C | ACE: sworn at/insulted | 2,150 / 3,867 | 34.8 / 40.6 | 0.78 (0.65–0.93) | 0.77 (0.60–0.99) |
| C | ACE: witnessed adults hit each other | 2,138 / 3,843 | 25.0 / 22.5 | 1.15 (0.95–1.40) | 0.78 (0.60–1.01) |
| C | ACE: physically hurt by parent/adult | 2,146 / 3,880 | 34.7 / 22.6 | 1.81 (1.49–2.19) | 1.44 (1.09–1.90) |
| C | Own depression diagnosis | 2,447 / 3,754 | 10.5 / 11.9 | 0.87 (0.68–1.11) | 0.67 (0.49–0.93) |
| C | Frequent mental distress | 2,463 / 4,094 | 11.2 / 12.2 | 0.91 (0.71–1.17) | 0.53 (0.38–0.75) |
| **D1 (K6 module 2009+2012, non-ACE)** | K6 ≥13 | 2,128 / 6,194 | 6.4 / 5.5 | 1.18 (0.77–1.83) | 0.59 (0.30–1.19) |
| D1 | Frequent mental distress | 2,090 / 6,118 | 11.6 / 14.0 | 0.80 (0.58–1.11) | 0.50 (0.33–0.75) |
| D1 | Own depression diagnosis (2012 only) | 1,993 / 4,806 | 17.8 / 17.3 | 1.03 (0.78–1.37) | 0.59 (0.43–0.83) |
| **D2 (PHQ-8 module 2010+2011, non-ACE)** | PHQ-8 ≥10 | 848 / 4,404 | 9.4 / 11.8 | 0.78 (0.52–1.16) | 0.32 (0.21–0.49) |
| D2 | Anxiety disorder diagnosis | 846 / 4,391 | 7.4 / 14.9 | 0.46 (0.31–0.68) | 0.33 (0.22–0.52) |
| D2 | Own depression diagnosis | 847 / 4,388 | 13.9 / 17.8 | 0.75 (0.56–1.00) | 0.56 (0.39–0.79) |
| D2 | Frequent mental distress | 837 / 4,347 | 11.5 / 12.4 | 0.92 (0.63–1.35) | 0.56 (0.37–0.85) |

Sample C also includes the other 2009–12 items in `key_or_table.csv`: problem drinker 0.59, touched 0.57, made to touch 0.75, forced sex 0.61. The ACE-co-fielded module subsets D1a/D2a (Spanish n = 79/36, 4–5 events) are uninterpretable; aORs with CIs spanning about 0.05–25 are in the CSV.

**Is the ACEDEPRS gap disproportionate? Ratio of aORs, same respondents, stacked model (sample A).** A ratio below 1 means the ACEDEPRS gap is larger than the comparison measure's gap.

| ACEDEPRS vs | aOR ACEDEPRS | aOR comparator | Ratio (95% CI) | p |
|---|---|---|---|---|
| Own depression dx | 0.19 | 0.33 | 0.59 (0.45–0.78) | 0.0001 |
| Frequent mental distress | 0.19 | 0.52 | 0.37 (0.29–0.48) | <1e-13 |
| Household substance use | 0.20 | 0.51 | 0.39 (0.30–0.51) | <1e-11 |
| Parents divorced | 0.19 | 0.51 | 0.38 (0.29–0.50) | <1e-11 |
| Witnessed IPV | 0.20 | 0.61 | 0.32 (0.24–0.43) | <1e-14 |
| Physical abuse | 0.19 | 0.79 | 0.24 (0.19–0.32) | <1e-25 |
| Emotional abuse | 0.19 | 0.37 | 0.52 (0.41–0.67) | <1e-6 |
| Any sexual abuse | 0.20 | 0.51 | 0.39 (0.31–0.50) | <1e-13 |
| **Incarceration** | 0.20 | 0.16 | **1.22 (0.89–1.67)** | 0.22 |

(Own depression vs physical abuse: 0.41 (0.34–0.51).) The drug-use item has the same aOR as ACEDEPRS (0.20 vs 0.20), so its stacked test was not run.

**Sensitivity analyses** (`sensitivity.csv`):
- Adding insurance and a personal doctor barely moves the estimates. Own depression dx aOR: 0.33→0.37 in A and 0.34→0.39 in B. FMD aOR: 0.51→0.53 in A and 0.43→0.44 in B. ACEDEPRS aOR: 0.20→0.21.
- Adding own depression dx + FMD to the ACEDEPRS model moves its aOR only from 0.19 (0.15–0.25) to 0.25 (0.19–0.32). Individual-level own mental-health reporting explains little of the ACEDEPRS gap.

**Puerto Rico 2024** (Spanish interviews, n≈4,150, descriptive, weighted). These are not directly comparable to the mainland: PR may use its own Spanish instrument, and the population differs.

| Measure | PR | Mainland Spanish | Mainland English |
|---|---|---|---|
| ACEDEPRS | 12.6% | 4.4% | 22.8% |
| Own depression dx | 18.1% | 9.3% | 19.3% |
| FMD | 11.8% | 10.5% | 16.1% |
| Physical abuse | 18.9% | 31.3% | 35.0% |
| Household substance use | 24.9% | 19.1% | 31.6% |
| ACE score ≥4 | 10.0% | 10.7% | 25.5% |

Spanish-language administration *per se* does not suppress ACEDEPRS (or own-depression) endorsement to mainland-Spanish levels.

## Differential prediction (sample A, complete on 11 ACE items; n Sp/En = 10,894/24,353 for depression and 10,588/24,105 for FMD)
Each model is a weighted logistic regression of the outcome on predictor × Spanish plus all covariates. The table gives the OR per unit of the predictor within each language.

| Outcome | Predictor | OR English (95% CI) | OR Spanish (95% CI) | Interaction p |
|---|---|---|---|---|
| Own depression dx | ACE score (0–8) | 1.40 (1.36–1.44) | 1.41 (1.30–1.52) | 0.92 |
| Own depression dx | ACE score without ACEDEPRS (0–7) | 1.41 (1.36–1.45) | 1.39 (1.28–1.51) | 0.82 |
| Own depression dx | ACEDEPRS | 4.63 (3.99–5.36) | 5.93 (3.70–9.51) | 0.33 |
| Own depression dx | ACEDEPRS, adjusted for the other 7 categories | 2.94 (2.50–3.46) | 3.93 (2.45–6.31) | 0.25 |
| FMD | ACE score (0–8) | 1.31 (1.27–1.35) | 1.35 (1.24–1.46) | 0.51 |
| FMD | ACE score without ACEDEPRS | 1.32 (1.27–1.37) | 1.34 (1.24–1.45) | 0.72 |
| FMD | ACEDEPRS | 3.20 (2.76–3.70) | 4.14 (2.36–7.28) | 0.38 |
| FMD | ACEDEPRS, adjusted for the other 7 categories | 2.12 (1.79–2.50) | 2.87 (1.60–5.15) | 0.32 |

The slopes are equal across languages. The intercepts differ: at ACE=0 the Spanish-vs-English OR is about 0.47 for depression and 0.68 for FMD. The point estimates for ACEDEPRS are somewhat *steeper* in Spanish, which fits a higher endorsement threshold: Spanish endorsers may be a more severe group. The difference is not significant, though, and the Spanish CI is wide.

## Takeaways
- **A broad own-mental-health gap exists.** Spanish-interview Hispanics report less depression diagnosis (aOR 0.33–0.34), FMD (0.43–0.51), about 2.5–2.8 fewer poor-mental-health days, less life dissatisfaction (0.28) and less stress (0.43–0.44). The gap appears in symptom scales too (PHQ-8≥10 aOR 0.32 in 2010–11), not only in "ever told" diagnoses, and adjusting for insurance and a personal doctor does not remove it. The direction is not universal: loneliness is null or higher in Spanish, and fair/poor health is higher (the known "regular" translation effect).
- **The ACEDEPRS gap is substantially larger than the own-mental-health gap.** On the log-OR scale it is about 1.5× the own-depression gap and 2.4× the FMD gap (ratio of aORs 0.59 vs own depression, 0.37 vs FMD) and barely shrinks when conditioning on own depression/FMD. It "tracks" the broader mental-health gap in direction only, not in size.
- **It is not mental-health-specific among ACE items.** The three "stigmatized household member" items cluster together: mental illness 0.20, drug use 0.20, incarceration 0.16. Alcohol (0.59), divorce (0.50), IPV (0.61) and especially physical abuse (0.80) are much closer to parity. The same cluster replicates in 2009–12 (0.24 / 0.23 / 0.18), where Spanish respondents even report *more* physical abuse (aOR 1.44). For a DIF study, this argues for treating "household member with a stigmatized condition" as the candidate DIF domain (plausibly item wording/recognition such as *deprimido/enfermo mental*, *drogas*, *cárcel*, or true differences in immigrant households), rather than a mental-health-reporting factor.
- **No differential prediction.** The ACE score and ACEDEPRS predict own depression and FMD with the same slopes in both languages (all interaction p > 0.25). Whatever lowers Spanish endorsement looks like a level (threshold or true-prevalence) shift, not a change in what an endorsed item means for health.
- **Feasibility.** K6 and PHQ-8 were not co-fielded with ACE in enough Spanish-interview respondents (79 and 36) for within-person tests. PR 2024 (Spanish; ACEDEPRS 12.6%) is a useful contrast group for separating language from migrant context.

## Caveats
- Interview language is a proxy for nativity and acculturation. The BRFSS public files have no nativity or years-in-US variable, so true prevalence differences (the immigrant health paradox, lower household drug use and incarceration in immigrant families of origin) cannot be separated from reporting or translation effects. The differences shown are associations, not measurement-bias estimates.
- The adjustment set is limited to age, sex, education, income, state and year. Income is missing more often among Spanish respondents (handled with a missing category). Several crude-to-adjusted shifts are large, e.g. PHQ-8 0.78→0.32 and K6 1.18→0.59, because Spanish-interview respondents are much lower-SES. Residual confounding is likely.
- SEs are approximate. Weights are year-normalized pooled final weights (main + version-file weights), clustering is year×stratum×PSU, and stratification is ignored. Many tests were run without multiplicity correction; the headline contrasts have p < 1e-4.
- The prevalences here use year-normalized weights and exclude territories (ACEDEPRS 4.4% vs 22.8%). The earlier 5.1% Spanish figure appears to include PR 2024. The earlier table with raw weights, also excluding territories, gives 4.2% vs 22.5%. With territories excluded, incarceration (2.8% vs 14.5%) is as extreme as ACEDEPRS.
- The Social Determinants (SDOH) outcomes cover few states (13–16 ACE states) and differ by year. The 2009–12 panel C is dominated by California 2011 landline version files, which did not ask ACEPRISN.
- PR 2024 results are descriptive only, and I did not verify whether PR's Spanish questionnaire wording matches the mainland CDC Spanish version.

## Files
- Scripts, in `/home/mo2273/ace_tonight_scripts/brfss_mh/`:
  - `extract_mh.py`: zip → temp XPT → chunked read → CSV; the XPT is deleted afterwards.
  - `mhcommon.py`: loading and coding, reusing `analyze_ace_language.py` logic.
  - `analyze_mh.py`: all models.
  - `explore_modules.py`: module coverage check.
- Outputs, in `/home/mo2273/ace_tonight/brfss_mh/`:
  - `key_or_table.csv`, `ratio_of_ORs_stacked.csv`, `differential_prediction.csv`, `sensitivity.csv`, `n_table.csv`, `pr2024_descriptive.csv`
  - `analysis_stdout.txt`, `extract_log.txt`
  - `extracts/extract_mh_<tag>.csv`: 38 files, 385 MB.
- Run with: `/home/mo2273/ace_venv/bin/python -I analyze_mh.py /home/mo2273/ace_brfss_work /home/mo2273/ace_tonight/brfss_mh/extracts /home/mo2273/ace_tonight/brfss_mh /home/mo2273/ace_tonight_scripts/brfss_mh`
