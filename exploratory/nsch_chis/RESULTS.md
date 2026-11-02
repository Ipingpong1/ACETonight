# Language and mental-health measures beyond BRFSS: NSCH 2022–2024, CHIS access, literature

First pass, 2026-11-01, for a same-night project discussion. All estimates are **approximate design-based** (see Methods).

**BRFSS reference point** (from the earlier analysis; Hispanic adults, 2019–2025, crude): the household mental illness ACE was 5.1% among Spanish-interview respondents vs 22.5% among English-interview respondents (ratio 0.23). Physical abuse was near parity.

---

## 1. NSCH 2022–2024: data and methods

- **Files:** Census NSCH topical public-use Stata files, downloaded without a login from `https://www2.census.gov/programs-surveys/nsch/datasets/<year>/`. The current edited releases are `nsch_2022e_topical.dta`, `nsch_2023e_topical.dta` and `nsch_2024e_topical.dta`. The 2025 topical file is also posted now but was not analyzed.
- **Variable names and wording** were checked against each year's Topical Variable List and Frequencies PDFs:
  - **The household mental illness item is `ACE8`, not ACE9.** Wording: "To the best of your knowledge, has this child EVER experienced… *Lived with anyone who was mentally ill, suicidal, or severely depressed*." `ACE9` is the alcohol/drug item.
  - There are no abuse or neglect items in NSCH.
  - `HHLANGUAGE` comes from the screener: "What is the primary language spoken in the household?" (1 English, 2 Spanish, 3 Other). **It is household language, not the language the questionnaire was completed in.** The public file has no instrument-language variable.
- **Population:** Hispanic children (`SC_HISPANIC_R`=1) in English- or Spanish-primary-language households. Other-language and missing households are excluded (n=756).
- **Outcomes:**
  - ACE items, coded 1=yes, 2=no. `ACE1` (hard to cover basics) is coded positive for "somewhat/very often".
  - Child diagnoses, ages 3–17: depression `K2Q32A` (ever) and `K2Q32B` (current); anxiety `K2Q33A` (ever) and `K2Q33B` (current).
  - Responding adult's own mental/emotional health, `A1_MENTHEALTH` ("In general, how is *your* mental or emotional health?"), coded fair/poor.
  - Comparators: `A1_PHYSHEALTH` (same scale, physical health), ADHD `K2Q31A`, behavior problems `K2Q34A`, asthma `K2Q40A`.
  - Access items: `K4Q22_R` (MH treatment or unmet MH need), `S4Q01` (any visit), `K4Q01` (usual place of care).
- **Models:** weighted logistic regression using `FWC`, with Taylor-linearized sandwich SEs clustered on state (`FIPSST`, 51 clusters).
  - Strata are ignored and state is treated as the PSU. Household-clustered CIs, which are closer to the NSCH PSU=HHID design, are slightly narrower (stored in `nsch_results.csv`).
  - FPL is multiply imputed (`FPL_I1`–`FPL_I6`). All models are fit on the 6 implicates and combined with Rubin's rules.
  - **Crude** model.
  - **M1:** child age group, sex, survey year.
  - **M3 (primary):** M1 + highest adult education (`HIGRADE_TVIS`) + FPL category (<100/100–199/200–399/400+) + household generation (`HOUSE_GEN`: 1st/2nd/3rd+/other).
  - **Sensitivity model:** 1st- and 2nd-generation households only, with M2 covariates (M3 without generation).
  - **Item contrasts:** ratio of the M3 Spanish ORs for two items, using a joint cluster sandwich (same children, cross-item covariance).

### N table (unweighted)

| Year | Hispanic children (all) | English HH | Spanish HH | Other/missing (excluded) | Weighted % Spanish (of EN+SP) |
|---|---|---|---|---|---|
| 2022 | 8,370 | 5,774 | 2,339 | 257 | 37.8% |
| 2023 | 8,170 | 5,653 | 2,262 | 255 | 40.1% |
| 2024 | 7,811 | 5,249 | 2,318 | 244 | 43.4% |
| **Pooled** | 24,351 | 16,676 | 6,919 | 756 | 40.4% |

| Weighted characteristic | English HH | Spanish HH |
|---|---|---|
| 1st-gen household | 0.4% | 14.2% |
| 2nd-gen household | 27.9% | 68.5% |
| 3rd+-gen household | 63.0% | 7.7% |
| Responding adult born outside US | 18.1% | 78.8% |
| Highest adult education < HS | 6.0% | 38.9% |
| FPL < 100% | 18.0% | 40.5% |
| Child currently uninsured | 7.2% | 15.4% |

Language and generation are heavily confounded: only 7.7% of Spanish households are 3rd+ generation. The within-immigrant-household sensitivity analysis is the cleaner comparison.

## 2. Key table: NSCH, Spanish vs English household, Hispanic children, pooled 2022–2024

Values are weighted %; ORs are Spanish vs English with 95% CI.

| Measure | English HH % (n) | Spanish HH % (n) | Ratio Sp/En | Crude OR | aOR M1 | **aOR M3 (primary)** | aOR, 1st/2nd-gen HH only |
|---|---|---|---|---|---|---|---|
| **ACE8: lived with anyone mentally ill, suicidal, severely depressed** | 9.6 (15,867) | 2.9 (6,430) | **0.30** | 0.28 (0.21–0.36) | 0.26 (0.20–0.34) | **0.32 (0.21–0.49)** | 0.34 (0.20–0.57) |
| ACE9: lived with anyone with alcohol/drug problem | 9.6 (15,871) | 4.5 (6,433) | 0.46 | 0.44 (0.33–0.58) | 0.41 (0.32–0.53) | **0.47 (0.32–0.69)** | 0.59 (0.40–0.87) |
| ACE6: saw/heard adults hit each other at home | 6.3 (15,875) | 2.7 (6,423) | 0.42 | 0.40 (0.33–0.49) | 0.38 (0.32–0.46) | **0.38 (0.31–0.45)** | 0.46 (0.35–0.62) |
| ACE5: parent/guardian served time in jail | 7.5 (15,902) | 2.5 (6,436) | 0.33 | 0.32 (0.26–0.38) | 0.30 (0.24–0.36) | **0.33 (0.24–0.43)** | 0.36 (0.24–0.54) |
| ACE3: parent/guardian divorced/separated | 25.8 (15,940) | 19.7 (6,431) | 0.77 | 0.71 (0.58–0.87) | 0.65 (0.54–0.79) | **0.73 (0.61–0.88)** | 0.81 (0.67–0.98) |
| ACE4: parent/guardian died | 3.2 (15,922) | 2.4 (6,447) | 0.75 | 0.75 (0.54–1.04) | 0.69 (0.50–0.95) | **0.58 (0.43–0.78)** | 0.91 (0.58–1.44) |
| ACE7: victim/witness of neighborhood violence | 4.8 (15,882) | 4.3 (6,428) | 0.89 | 0.88 (0.68–1.14) | 0.82 (0.64–1.05) | **0.57 (0.36–0.88)** | 0.93 (0.52–1.66) |
| ACE10: treated unfairly because of race/ethnicity | 5.4 (15,872) | 3.8 (6,416) | 0.71 | 0.70 (0.57–0.85) | 0.65 (0.54–0.78) | **0.77 (0.62–0.96)** | 0.97 (0.72–1.29) |
| ACE11: treated unfairly because of health condition | 2.9 (15,911) | 1.5 (6,432) | 0.53 | 0.52 (0.40–0.68) | 0.49 (0.37–0.65) | **1.10 (0.74–1.62)** | 1.34 (0.73–2.45) |
| ACE1: hard to cover basics somewhat/very often | 17.0 (16,297) | 19.3 (6,671) | 1.13 | 1.16 (1.07–1.26) | 1.17 (1.08–1.27) | **0.85 (0.73–0.99)** | 1.04 (0.88–1.23) |
| Child depression, ever (3–17) | 5.8 (13,939) | 4.5 (5,950) | 0.78 | 0.77 (0.52–1.13) | 0.71 (0.49–1.05) | **1.03 (0.78–1.36)** | 1.36 (0.93–1.97) |
| Child depression, current (3–17) | 4.7 (13,925) | 2.7 (5,945) | 0.56 | 0.55 (0.36–0.84) | 0.51 (0.34–0.78) | **0.76 (0.52–1.13)** | 1.18 (0.69–2.02) |
| Child anxiety, ever (3–17) | 12.6 (13,929) | 7.7 (5,926) | 0.61 | 0.58 (0.47–0.71) | 0.55 (0.44–0.67) | **0.71 (0.57–0.90)** | 0.85 (0.69–1.04) |
| Child anxiety, current (3–17) | 11.0 (13,868) | 5.6 (5,908) | 0.51 | 0.48 (0.39–0.59) | 0.46 (0.37–0.57) | **0.59 (0.48–0.73)** | 0.73 (0.60–0.88) |
| **Responding adult's own mental health fair/poor** | 9.1 (15,968) | 4.1 (6,482) | **0.45** | 0.43 (0.36–0.50) | 0.43 (0.37–0.50) | **0.39 (0.32–0.47)** | 0.46 (0.36–0.58) |
| Responding adult's mental health good/fair/poor | 34.9 (15,968) | 28.9 (6,482) | 0.83 | 0.76 (0.68–0.85) | 0.75 (0.68–0.83) | **0.68 (0.62–0.74)** | 0.72 (0.65–0.81) |
| *Comparator:* responding adult's physical health fair/poor | 9.1 (15,956) | 9.8 (6,480) | **1.07** | 1.08 (0.91–1.29) | 1.05 (0.89–1.24) | **0.69 (0.57–0.83)** | 0.79 (0.68–0.93) |
| *Comparator:* ADHD, ever (3–17) | 11.3 (13,906) | 5.9 (5,897) | 0.52 | 0.49 (0.35–0.68) | 0.47 (0.34–0.66) | **0.64 (0.42–0.98)** | 0.85 (0.54–1.32) |
| *Comparator:* behavior/conduct problems, ever (3–17) | 9.5 (13,971) | 5.7 (5,977) | 0.60 | 0.57 (0.45–0.74) | 0.57 (0.45–0.73) | **0.60 (0.42–0.86)** | 0.75 (0.50–1.12) |
| *Comparator:* asthma, ever (0–17) | 11.0 (16,526) | 9.2 (6,807) | 0.84 | 0.82 (0.76–0.89) | 0.78 (0.71–0.86) | **0.99 (0.84–1.17)** | 1.01 (0.86–1.18) |
| *Access:* MH professional treatment, past 12 mo (3–17) | 12.6 (13,942) | 7.3 (5,932) | 0.58 | 0.54 (0.46–0.64) | 0.52 (0.44–0.61) | **0.75 (0.62–0.91)** | 0.81 (0.61–1.07) |
| *Access:* needed but did not get MH care (3–17) | 3.2 (13,942) | 2.7 (5,932) | 0.86 | 0.85 (0.49–1.49) | 0.83 (0.48–1.46) | **0.94 (0.51–1.70)** | 1.59 (0.78–3.23) |
| *Access:* usual place for sick care | 75.8 (16,605) | 56.5 (6,851) | 0.75 | 0.41 (0.37–0.47) | 0.41 (0.37–0.46) | **0.66 (0.56–0.77)** | 0.63 (0.50–0.79) |

The Spanish-household ACE8 gap was stable across years (weighted %, English vs Spanish):

| Year | English HH | Spanish HH |
|---|---|---|
| 2022 | 10.1 | 3.4 |
| 2023 | 10.0 | 2.9 |
| 2024 | 8.5 | 2.4 |

Parent mental health fair/poor (English vs Spanish) was 9.6/3.7, 8.9/4.7 and 8.8/4.0 across the same three years. Parent *physical* health fair/poor was 9.2/8.9, 9.5/11.5 and 8.6/9.0. See `nsch_by_year.csv`.

### Is the deficit disproportionately large for mental-health items? Item contrasts (M3)

A ratio of ORs below 1 means the Spanish deficit is larger for the first item.

| Contrast | Ratio of ORs | 95% CI | p |
|---|---|---|---|
| ACE8 vs ACE9 (alcohol/drugs, the closest analog) | 0.68 | 0.52–0.89 | 0.005 |
| ACE8 vs ACE6 (domestic violence) | 0.85 | 0.51–1.42 | 0.54 |
| ACE8 vs ACE5 (jail) | 0.98 | 0.62–1.55 | 0.94 |
| ACE8 vs ACE3 (divorce) | 0.44 | 0.33–0.58 | <0.001 |
| ACE8 vs ACE7 / ACE10 / ACE11 / ACE1 | 0.57 / 0.41 / 0.29 / 0.37 | all CIs exclude 1 | ≤0.001 |
| ACE8 vs mean of household items ACE9/6/5/3 | 0.71 | 0.51–0.98 | 0.037 |
| ACE8 vs mean of all 9 other ACE items | 0.53 | 0.36–0.78 | 0.001 |
| **Parent mental health fair/poor vs parent physical health fair/poor** | **0.56** | 0.47–0.67 | <0.001 |
| Child current anxiety vs asthma | 0.60 | 0.50–0.72 | <0.001 |
| Child current anxiety vs ADHD | 0.92 | 0.62–1.38 | 0.69 |
| Child depression ever vs asthma | 1.04 | 0.84–1.29 | 0.71 |

**Item nonresponse:** Spanish households skip every ACE item about 2 percentage points more often than English households (ACE8: 7.0% vs 5.2%; other ACE items 7.0–7.6% vs 5.0–5.6%; `A1_MENTHEALTH` 6.6% vs 4.5%). There is **no mental-health-specific skipping**, so the gap is in endorsement, not refusal.

## 3. CHIS 2021–2024 adult PUF: access status

**Not downloadable without an account right now** (checked 2026-11-01). I did not register, log in, or try to get past the site's bot check.

- **Evidence:**
  - On the PUF landing page (`https://healthpolicy.ucla.edu/our-work/public-use-files`), every collection is linked only through a login redirect, e.g. `/user/login?destination=/our-work/public-use-files/one-year-public-use-files-pufs`, and the same for `two-year-public-use-files-pufs`.
  - Requesting those pages directly returned HTTP 403 or a "Checking connection" bot challenge.
  - CHIS describes the PUF as "Available as free download in SAS and STATA format" (CHIS data release slides, Oct 2024, `https://healthpolicy.ucla.edu/sites/default/files/2024-10/chis-data-release-october-2024.pdf`). So it is free, but requires an account.
- **To do it tonight:**
  1. Create a free account at **`https://healthpolicy.ucla.edu/user/register`**. The form asks for username, email, first/last name, organization, planned use of data and work ZIP, plus a CAPTCHA; an email confirmation is likely.
  2. Log in and go to Public Use Files → **One-Year PUFs**. Download the **Adult** Stata files for 2021, 2022, 2023 and 2024, plus each year's **adult data dictionary** (PDF). The two-year 2021–2022 and 2023–2024 adult PUFs are an alternative.
  3. Put each year in its own empty folder, e.g. `/home/mo2273/ace_tonight_data/chis_2021/`.
  4. Run the prepared script. First pass `--scan-only`: it lists variables whose labels match interview language, Hispanic, nativity, K6/distress, ACE, depression/anxiety, weights and education. Then put the ACE variable names in a JSON config and run the full analysis: crude % and adjusted ORs with the same outcome set, adjusted for age, sex, education, nativity and year, using jackknife replicate-weight SEs.
     `/home/mo2273/ace_venv/bin/python -I /home/mo2273/ace_tonight_scripts/nsch_chis/chis_analysis.py OUTDIR 2021=/path/adult_2021.dta 2022=... --scan-only`
     The script was tested on synthetic data only.
- **Variables.** I could not see the 2021–2024 dictionaries (they are behind the login). **Treat every name except the researcher-supplied one as "verify":**
  - Interview language: `INTVLNGC_P1` (researcher-supplied; codes to confirm).
  - Weights: `RAKEDW0`, with jackknife replicates `RAKEDW1`–`RAKEDW80`. Expected Stata setup: `svyset [pw=rakedw0], jkrweight(rakedw1-rakedw80, multiplier(1)) vce(jackknife) mse`.
  - K6: `DISTRESS` (score), `DSTRS30` / `DSTRS12` (serious psychological distress), items `AJ29`–`AJ34`.
  - Demographics: `SRAGE_P1`, `SRSEX`, `AHEDUC`, `SRH` or `OMBSRR_P1` (Hispanic), `CITIZEN2` (US-born / naturalized / non-citizen).
  - These names come from my knowledge of earlier CHIS public files, not from the current dictionaries.
- **ACE content:** CHIS adult ACEs form an 8-item scale: parental separation/divorce, household incarceration, witnessed domestic violence, household mental illness, household substance abuse, and physical, emotional and sexual abuse. Source: kidsdata.org's CDPH tabulation of CHIS 2021.
  - Item variable names are not public. Search the dictionary for "MENTALLY ILL", "PRISON", "HIT" and similar terms.
  - A PCE scale built from `AQ16`–`AQ22` exists (CHIS 2021 errata), so the ACE items are probably in the same AQ section. That is unconfirmed.
- **Why CHIS matters:** it records *interview* language, adult self-reported ACEs including **physical abuse**, nativity/citizenship, and the K6, which has a published CHIS DIF analysis by language (Kim 2016). It is the only one of these datasets that can test the BRFSS pattern (MH item low, physical abuse at parity) with a nativity adjustment.

## 4. Literature (all PMIDs checked in Europe PMC)

1. **Kim G et al. 2016, *Assessment*, PMID 26282779.** CHIS (n=44,846): K6 items "nervous", "hopeless", "restless" and "depressed" showed DIF by language. In effect-size analyses, Hispanic-Spanish did not differ from Hispanic-English; both differed from White-English. **Formal DIF: yes (IRT).**
2. **Merz EL et al. 2011, *Cultur Divers Ethnic Minor Psychol*, PMID 21787063.** PHQ-9 in 479 Latinas: equal structure, loadings and variance in English vs Spanish; cutoff rates 11% vs 15% (not significant). **Yes (multigroup CFA; intercepts not tested).**
3. **González P et al. 2017, *Psychol Assess*, PMID 27295022.** HCHS/SOL (n=16,415): CES-D-10 fully invariant between English and Spanish, including thresholds. Invariance was only partial across Hispanic background groups. **Yes (multigroup CFA).**
4. **Mills SD et al. 2014, *Cultur Divers Ethnic Minor Psychol*, PMID 25045957.** GAD-7 in Hispanic Americans: equal loadings and intercepts by language preference. **Yes (multigroup CFA).**
5. **Nguyen HT et al. 2007, *Nurs Res*, PMID 17495578.** Hispanic pregnant women, CES-D by completion language: no DIF on depressed-affect items. DIF on 4 of 7 somatic and 3 of 4 positive-affect items; Spanish completers endorsed somatic items *less*. **Yes (logistic-regression DIF).** Companion study: McCabe 2011, PMID 21677596.
6. **Azocar F et al. 2001, *J Clin Psychol*, PMID 11241365.** Spanish BDI: at equal severity, Spanish speakers endorsed tearfulness and punishment more and work inhibition less. Language is confounded with ethnicity. **Yes (Mantel-Haenszel DIF).**
7. **Alegría M et al. 2007, *AJPH*, PMID 17138910.** NLAAS: psychiatric disorder rates were higher among US-born, English-proficient and later-generation Latinos (the immigrant paradox). This suggests part of any language gap is real. **No (prevalence).**
8. **Guarnaccia PJ et al. 2010, *Int J Soc Psychiatry*, PMID 19592438.** NLAAS: ataque de nervios was reported by about 7–15% of Latinos and was linked to DSM disorders. **No.**
9. **Vega WA et al. 2010, *Gen Hosp Psychiatry*, PMID 20302993.** Spanish-speaking primary-care patients: greater depression stigma was linked to less disclosure of a depression diagnosis to family and friends. Also Nadeem 2007, PMID 18048555: stigma concerns were highest among immigrant Latinas. **No.** This is the most direct support for a proxy-report mechanism behind household-MI items.
10. **Alhalel N 2018, Northwestern MPH thesis (grey literature),** `https://prism.northwestern.edu/records/7mt6a-brh38`. BRFSS 2011–12, 9 states, 2,983 Hispanics: most individual ACE prevalences differed significantly by questionnaire language. Item-level numbers are in the full text, not re-verified. **No (prevalence).** It is the only ACE-by-interview-language study found.
11. Older or tangential:
    - Guarnaccia 1989, *Soc Sci Med*, PMID 2740931: CES-D factor structure differed by interview language in Hispanic HANES. Exploratory factor analysis only.
    - Kim 2009, *J Am Geriatr Soc*, PMID 19484834: CES-D DIF in Mexican-American elders.

**Gap:** no peer-reviewed DIF or measurement-invariance study of ACE items by interview language was found.

## 5. Takeaways

1. **NSCH reproduces the BRFSS signal in a different design, with no interviewer.** NSCH is self-administered by web or paper and the items are parent reports about the child, yet the household mental illness ACE is 2.9% in Spanish households vs 9.6% in English households (ratio 0.30; BRFSS 0.23). The adjusted OR is 0.32 (0.21–0.49), stable across 2022–2024 and similar within immigrant households (0.34).
2. **The gap is at the extreme, but it is not unique to mental illness.** Incarceration (aOR 0.33) and domestic violence (0.38) show equally large Spanish deficits (ACE8 vs ACE5 ratio 0.98; vs ACE6 0.85). ACE8 is significantly more extreme than substance use (0.68), divorce, neighborhood violence, discrimination and hardship (vs all other ACEs 0.53). The pattern is a gradient: the most stigmatized or private household-dysfunction items show the biggest gaps, with mental illness at the top along with jail and violence. NSCH has no abuse items, so the BRFSS "physical abuse at parity" contrast cannot be tested here; that needs CHIS.
3. **The clearest mental-health-specific signal is the responding parent's own rating.** Fair/poor mental health is 4.1% vs 9.1% (aOR 0.39), while fair/poor *physical* health on the identical scale is at crude parity (9.8% vs 9.1%; aOR 0.69). The ratio of ORs is 0.56 (0.47–0.67). This is within the same respondents, and the usual Spanish "regular" = "fair" translation effect pushes *toward* fair/poor, which makes the MH deficit more notable. It is consistent with MH-specific under-reporting, a real immigrant mental-health advantage, or both.
4. **Child diagnosis items mostly reflect access and diagnosis, not terminology.** After adjustment, depression-ever shows no gap (1.03). Current anxiety (0.59) is lower, but by about as much as ADHD (0.64) and behavior problems (0.60), not asthma (0.99); anxiety vs ADHD ratio is 0.92. Spanish households also have less MH treatment (0.75) and a usual source of care less often (0.66). These items cannot separate under-recognition, under-reporting and true prevalence.
5. **Research design implication.** Formal DIF studies of symptom scales (PHQ-9, CES-D-10, GAD-7) mostly find scale-level language invariance, with item-level DIF (somatic and positive-affect items; K6 nervous, hopeless, restless and depressed). Proxy household items like "lived with someone mentally ill" require recognition, labeling and disclosure, and have never been DIF-tested by language. A MIMIC or multigroup IRT model across all ACE items with interview language as the DIF covariate, adjusted for nativity, is the natural design. CHIS adult PUFs are the best next dataset.

## 6. Caveats

- **NSCH language is household primary language, not questionnaire language.** It is a proxy for BRFSS's interview language, and misclassification in either direction is possible.
- **NSCH ACEs are parent-reported, about the child's lifetime** (mean age about 9). ACE8 includes the respondent themselves, so it is mechanically linked to the parent's own mental-health report. This is a different construct from adult retrospective self-report in BRFSS and CHIS.
- **True differences are plausible** (immigrant paradox, family structure, selection). Generation (`HOUSE_GEN`) is a coarse acculturation adjustment, and language and generation are nearly collinear (only 7.7% of Spanish households are 3rd+ generation).
- **SEs are approximate:** state-clustered sandwich, strata ignored, conservative relative to household-level CIs. There are many comparisons, and some Spanish cell counts are small (ACE11: 99 cases; ACE4: 140).
- **Not checked:** CHIS variable names and codes (all marked "verify"), and NSCH 2025 data.

## Files

- **Results** (in `/home/mo2273/ace_tonight/nsch_chis/`):
  - `nsch_results.csv`: all models, including the M2 and household-clustered CIs
  - `nsch_contrasts.csv`
  - `nsch_item_nonresponse.csv`
  - `nsch_by_year.csv`
  - `nsch_descriptives.json`
  - `nsch_tables.md`
  - `nsch_stdout.txt`, `nsch_contrasts_stdout.txt`
- **Scripts** (in `/home/mo2273/ace_tonight_scripts/nsch_chis/`):
  - `nsch_inspect.py`
  - `nsch_analysis.py`: the main analysis; `--contrasts-only` re-runs the contrasts alone
  - `nsch_by_year.py`
  - `make_tables.py`
  - `chis_analysis.py`: CHIS template
- **Data** (in `/home/mo2273/ace_tonight_data/`):
  - `nsch_2022/`, `nsch_2023/`, `nsch_2024/`: zip, `extract/`, and `codebook/` with PDFs and text versions
  - `chis_docs/`: public CHIS PDFs
