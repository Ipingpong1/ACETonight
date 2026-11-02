# Does interview language change how Hispanic adults report childhood household adversity? Differential item functioning of ACE items in two US surveys

*Working draft* · Nov 2, 2026 · @Matias

## Abstract

**Introduction:** Adverse childhood experience (ACE) prevalence is compared across groups, but whether the items work the same way in Spanish-language interviews is unknown. This study tested whether Hispanic adults interviewed in Spanish endorse household mental illness, drug use and incarceration less often at the same level of household adversity.

**Methods:** Secondary analysis of BRFSS 2019–2025 (10,945 Spanish- and 24,473 English-interview Hispanic adults) and CHIS 2021–2025 (5,536 and 24,418), two surveys with the same English ACE items and independent Spanish translations. MIMIC models with survey weights estimated item-level differential item functioning (DIF) by interview language, with replicate-weight variance for the primary models. The hypothesis came from exploratory analyses; the model specification was locked before fitting. Analyses were conducted in 2026.

**Results:** Spanish-interview respondents reported household mental illness in 4.0% vs 21.9% (BRFSS) and 5.6% vs 23.8% (CHIS). At the same level of household dysfunction, all three items were endorsed less often in Spanish in both surveys (odds-ratio equivalents 0.31–0.35 in BRFSS and 0.43–0.64 in CHIS). After nativity adjustment in CHIS, only the mental-illness DIF remained significant, though attenuated (0.67; 95% CI 0.55–0.82), including among foreign-born adults (0.69; 0.54–0.88). Mental-illness DIF was significant in 10 of 11 sensitivity specifications, but all three BRFSS effects lost significance with purified anchors; drug-use and incarceration DIF also depended on nativity. Removing the DIF would close 10%–18% of the model-implied language gap in 8-item ACE counts.

**Conclusions:** The household mental-illness ACE item functions differently by interview language. ACE comparisons across interview languages should account for this, and the Spanish item should be retested.

## Introduction

Adverse childhood experiences (ACEs), meaning abuse and household dysfunction before age 18, are among the most widely used exposures in population health (Felitti et al. 1998). The Behavioral Risk Factor Surveillance System (BRFSS) has made them a surveillance measure: in 2011–2020, 63.9% of US adults reported at least one ACE and 17.3% reported four or more (Swedo et al. 2023). These estimates are compared across population groups to target prevention (CDC 2019; Swedo et al. 2023).

Group comparisons assume each question works the same way in every group. For the BRFSS items, this has been tested by gender and age (Ford et al. 2014), and by age, sex, race and ethnicity, income, sexual orientation and gender identity (Mei et al. 2022). Parent-reported child ACEs failed scalar invariance across racial and ethnic groups (Jensen et al. 2024). A 2026 dissertation found the BRFSS items non-invariant across racial and ethnic groups, with differences concentrated in the household mental illness, incarceration and alcohol items (Umoga 2026). None of these studies examined the language of the interview.

Language matters because many Hispanic adults are interviewed in Spanish: about 40% of Hispanic BRFSS respondents in 2003–2005 (DuBard & Gizlice 2008) and 52% of Hispanic CHIS adults in 2009 (Kim et al. 2016). Interview language shifts answers to other survey questions. Spanish-language respondents rate their health worse partly because "regular" is not equivalent to "fair" (Viruell-Fuentes et al. 2011; Bzostek et al. 2007), and item-level language effects have been found for psychological distress (Kim et al. 2016), cognitive screening (Jones 2006) and political attitudes (Pérez 2011).

For ACEs, six of 11 BRFSS items differed in prevalence by questionnaire language among Hispanic respondents (Alhalel 2018), and immigrant families report fewer household adversities than US-born families (Caballero et al. 2017; Grest et al. 2021). These studies did not ask whether lower prevalence reflects less adversity or different reporting at the same level of adversity. The only Spanish–English invariance test involving ACE items embedded them in a broader adversity model in an all-immigrant sample (Cooper & Nickodem 2021).

Three household items may be especially sensitive to language: whether someone in the household was mentally ill, used drugs, or was incarcerated. These items ask respondents to label a family member's condition, and each condition carries stigma that extends to the family (Corrigan et al. 2006; Luther 2016). Among Latinos, mental-illness stigma discourages disclosure (Interian et al. 2007; Vega et al. 2010), and families may describe distress as "nervios" rather than mental illness (Jenkins 1988).

Survey research shows that embarrassing answers are under-reported (Tourangeau & Yan 2007), especially about criminal-justice involvement (Yan & Cantor 2019). Proxy reports of household mental illness are also low: parents report it far less often than their teenagers do (Ng et al. 2025).

We therefore tested whether Spanish-interview Hispanic adults are less likely than English-interview Hispanic adults to endorse these three "stigmatized household condition" items at the same latent level of household dysfunction (H1). We used two surveys that ask the same English questions with independent Spanish translations, BRFSS 2019–2025 and the California Health Interview Survey (CHIS) 2021–2025, and in CHIS we tested whether any difference persists after accounting for nativity. To our knowledge, no previous study has tested whether ACE items function differently by interview language (literature searched through 2 November 2026).

## Methods

### Study design and data sources

This is a cross-sectional secondary analysis of two population surveys that ask the same English-language ACE questions but use different Spanish translations. The confirmatory models followed an analysis plan frozen before they were fitted (see Pre-specification).

**BRFSS.** The Behavioral Risk Factor Surveillance System is a state-based telephone survey of noninstitutionalized US adults, run by state health departments with CDC (CDC 2024). States may add an optional ACE module. We used the 2019–2025 public-use files and the questionnaire-version files. States that fielded the module on only one questionnaire version have blank ACE fields in the main file, so main-file-only analyses lose 12–36% of ACE respondents per year. Interviews are in English or Spanish, and the questionnaire language is recorded.

**CHIS.** The California Health Interview Survey samples California adults; most complete it on the web, the rest by telephone (California Health Interview Survey 2024). CHIS asked the BRFSS ACE items in every year from 2021 to 2025, with its own Spanish translation. We used the 2021–2025 adult public-use files, which record interview language (English, Spanish or other), nativity and percentage of life lived in the US.

### Analytic samples

Both samples were restricted to Hispanic adults interviewed in English or Spanish.

- **BRFSS:** respondents in 41 states and the District of Columbia (11–28 per year) with valid answers to all 11 ACE items: 10,945 Spanish-interview and 24,473 English-interview. Territories were excluded because Puerto Rico's 2024 sample had no English-interview respondents.
- **CHIS:** 5,536 Spanish-interview and 24,418 English-interview adults. CHIS imputes item nonresponse in its public files, so no one was excluded for missing ACE data.

### Measures

**ACE items.** Eight items are worded identically in English in both surveys and were coded 1 if endorsed. Following Ford et al. (2014), they form two correlated factors: household dysfunction and physical/emotional abuse. BRFSS also asks three sexual-abuse items, which CHIS does not release individually; these enter only a BRFSS secondary model and the 4+ ACE summary.

| Item | Question (abbreviated) | Coded 1 if | Role in H1 |
| --- | --- | --- | --- |
| Household mental illness | Lived with anyone depressed, mentally ill or suicidal | Yes | Target |
| Household drug use | Lived with anyone who used illegal street drugs or misused prescription medications | Yes | Target |
| Household incarceration | Lived with anyone who served, or was sentenced to serve, time in a prison, jail or other correctional facility | Yes | Target |
| Problem drinking | Lived with a problem drinker or alcoholic | Yes | Anchor |
| Parental separation or divorce | Parents separated or divorced | Yes ("parents not married" = no) | Anchor |
| Witnessed parental violence | Parents or adults in the home slapped, hit, kicked, punched or beat each other up | Once or more | Anchor |
| Physical abuse | A parent or adult in the home hit, beat, kicked or physically hurt you (not spanking) | Once or more | Anchor |
| Verbal abuse | A parent or adult in the home swore at, insulted or put you down | Once or more | Anchor |

The three target items describe stigmatized conditions of household members. Problem drinking and separation/divorce are the household items they are compared against.

**4+ ACEs.** The standard 8-category score counts household substance use (drinking or drugs) once and sexual abuse (any of three items) once. We computed it in BRFSS. CHIS releases only the summary score (ACE8, top-coded at 4+), which includes three sexual-abuse items that CHIS does not release individually.

**Exposure.** Interview language, Spanish vs English.

**Covariates.** Age group, sex, education, survey year, and household income (BRFSS) or poverty level (CHIS), all categorical; in BRFSS, nonresponse on age, education and income formed separate categories. BRFSS models add Census region. CHIS secondary models add nativity, percentage of life in the US and interview mode.

### Statistical analysis

**Descriptive comparison.** We estimated weighted item prevalence by interview language with design-based 95% CIs, and adjusted prevalence ratios from survey-weighted Poisson working models. BRFSS variance used Taylor linearization with year × file × stratum and primary sampling unit; CHIS variance used its 80 jackknife replicate weights. Weights were divided by the number of pooled years.

**Primary DIF model (H1).** In each survey we fitted a multiple-indicators multiple-causes (MIMIC) model (Muthén 1989; Finch 2005; Woods 2009). Each binary item j reflects a continuous latent response:

```latex
y_{ij}^{*} = \lambda_j \eta_{i} + \beta_j \,\mathrm{Spanish}_i + \varepsilon_{ij}, \qquad y_{ij} = 1 \iff y_{ij}^{*} > \tau_j
```

```latex
\eta_{ki} = \gamma_k \,\mathrm{Spanish}_i + \boldsymbol{\delta}_k^{\top}\mathbf{x}_i + \zeta_{ki}, \qquad k \in \{\text{household dysfunction}, \text{abuse}\}
```

Here η is the factor item j loads on, x the covariates, and β the direct effect of interview language on the item. A negative β means Spanish-interview respondents endorse the item less often than English-interview respondents with the same factor level and covariates: uniform DIF.

Direct effects were estimated for the three target items only; the other five items served as anchors. The household factor's language effect is therefore identified by problem drinking and separation/divorce. If those two items were themselves under-reported in Spanish, the target estimates would be biased toward zero; if over-reported, away from zero. The anchor-sensitivity analyses (S4) examine both possibilities.

Models used WLSMV estimation with theta parameterization and survey weights (lavaan; Rosseel 2012). We report β on the probit scale; an approximate odds-ratio equivalent, exp(1.7β), from the logistic approximation to the probit (Camilli 1994); and the model-implied change in endorsement probability. The odds-ratio equivalent is conditional on the latent factor and is not comparable with the prevalence ratios in Table 2.

**Decision rule.** H1 is supported if, in both surveys, all three direct effects are negative, Holm-adjusted p < .05 across six tests (three items × two surveys; Holm 1979), and β ≤ −0.24 (≈ OR ≤ 0.67). It is partially supported if these hold for at least two items in both surveys, or for all three in one survey. H1b, a key secondary hypothesis, was that in CHIS all three direct effects remain negative (p < .05) after adjustment for nativity and percentage of life in the US.

**Design-based standard errors.** Standard errors for the primary, S1 and S2 models came from replicate weights: CHIS's 80 jackknife replicates and 100 Rao–Wu rescaled bootstrap replicates for BRFSS (Rao et al. 1992). For the bootstrap only, 749 strata with a single primary sampling unit were merged with neighboring strata, a deviation from the plan (Supplement). Models S3, S4, S6 and S7 used lavaan's weight-robust standard errors, which ignore stratification and clustering.

**Secondary analyses (pre-specified).**

- S1: CHIS model adding nativity and percentage of life in the US (tests H1b).
- S2: CHIS foreign-born respondents only.
- S3: two-group confirmatory factor analysis by interview language (configural, full scalar, partial scalar), with scaled difference tests (Satorra 2000) and score tests that flag the most violated constraints without reference to H1. Equality constraints were coded explicitly because lavaan's group-equality option did not constrain the binary thresholds.
- S4: anchor sensitivity: a one-factor model, purified anchors, each non-target item freed in turn, and alignment optimization (Asparouhov & Muthén 2014).
- S5: impact: the model-implied Spanish–English gap in mean ACE count and 4+ prevalence, with and without the target direct effects.
- S6: CHIS interview mode (phone vs web) by language interaction.
- S7: BRFSS 11-item, three-factor model.

Fit indices (CFI, TLI, RMSEA, SRMR) are reported but were not decision criteria.

**Pre-specification and prior exposure.** H1 came from exploratory analyses of the same data on 1 November 2026: item-level logistic DIF, two-group 2PL models and covariate-adjusted odds ratios. The plan for the models above was frozen on 2 November 2026 before they were fitted (SHA-256 031cd720…420fa) and will be registered on OSF with the secondary-data template (van den Akker et al. 2021) after the analyses were run; the hash lets readers verify that the registered plan is unchanged \[link TBD\]. These are therefore pre-specified analyses of the data that generated H1, not a confirmatory test or an independent replication. Exploratory results are in the Supplement.

**Software, ethics and reporting.** Analyses used R 4.5.3 (lavaan 0.7.2; survey 4.5, Lumley 2004; sirt 4.2) and Python (pandas, matplotlib); code will be shared at \[repository TBD\]. Both datasets are public and de-identified \[NYU IRB determination to confirm\]. Data were analyzed in November 2026. Reporting follows STROBE (von Elm et al. 2007).

## Results

### Sample

The BRFSS sample included 35,418 Hispanic adults, 10,945 of them interviewed in Spanish; the CHIS sample included 29,954, 5,536 interviewed in Spanish (Table 1). In both surveys, Spanish-interview respondents were older, had less education and had lower incomes than English-interview respondents. In CHIS, 92.2% of Spanish-interview respondents were born outside the US (vs 27.7% of English-interview respondents), and 59.4% spoke English not well or not at all.

### Spanish-interview respondents reported the three household conditions one-fifth to one-third as often

In BRFSS, Spanish-interview respondents reported household mental illness in 4.0% of cases vs 21.9% (adjusted prevalence ratio \[aPR\] 0.24; 95% CI 0.19–0.31), household drug use in 3.1% vs 14.2% (aPR 0.21; 0.17–0.26) and household incarceration in 2.6% vs 14.0% (aPR 0.20; 0.16–0.26) (Table 2). CHIS showed the same pattern: 5.6% vs 23.8% (aPR 0.35), 4.6% vs 14.5% (aPR 0.32) and 2.6% vs 13.1% (aPR 0.22).

The other items differed less (aPRs 0.51–0.70), and physical abuse barely differed (aPR 0.88 in BRFSS, 1.00 in CHIS). Four or more ACEs were reported by 10.8% vs 25.3% in BRFSS (aPR 0.43) and 13.6% vs 26.1% in CHIS (aPR 0.56).

### H1: all three items showed negative DIF in both surveys

At the same level of household dysfunction and the same covariate values, Spanish-interview respondents were less likely to endorse each target item (Figure 1):

- **Mental illness:** BRFSS b = −0.62 (OR-equivalent 0.35; 95% CI 0.24–0.51); CHIS b = −0.31 (0.59; 0.49–0.70).
- **Drug use:** BRFSS b = −0.70 (0.31; 0.21–0.45); CHIS b = −0.27 (0.64; 0.48–0.83).
- **Incarceration:** BRFSS b = −0.65 (0.33; 0.25–0.44); CHIS b = −0.49 (0.43; 0.32–0.58).

All six estimates met the pre-specified criteria (Holm-adjusted p ≤ .002 and b ≤ −0.24), so H1 was supported. Among Spanish-interview respondents, the DIF lowered expected endorsement by 6.0 (mental illness), 3.1 (drug use) and 5.2 (incarceration) percentage points in BRFSS, and by 4.4, 1.5 and 2.9 points in CHIS.

Spanish-interview respondents also had lower latent household dysfunction (b = −0.54 in BRFSS, −0.60 in CHIS) and lower latent abuse (−0.41, −0.27). Fit was mixed: RMSEA (0.011 and 0.015) and SRMR (0.050) indicated close fit, but CFI (0.946 and 0.942) fell just below the conventional 0.95.

### Nativity attenuated all three effects; only the mental-illness DIF remained (H1b)

In CHIS, adding nativity and percentage of life in the US attenuated but did not remove the mental-illness DIF (b = −0.23; OR-equivalent 0.67; 95% CI 0.55–0.82; p < .001). The drug-use (0.89; 0.66–1.21; p = .47) and incarceration (0.81; 0.57–1.15; p = .23) DIF were attenuated and no longer significant. Among foreign-born adults only (5,134 Spanish- vs 6,305 English-interview), the mental-illness DIF remained (0.69; 0.54–0.88; p = .003), with none for drug use (0.99) or incarceration (1.00). H1b, which required all three effects to persist, was therefore not supported; only the mental-illness DIF remained significant.

### Sensitivity analyses

- **Invariance tests.** Full scalar invariance across languages was rejected by scaled χ² difference tests in both surveys (Δχ²\[12\] = 257 in BRFSS and 218 in CHIS; ΔCFI −0.016 and −0.008), and freeing the target items did not restore fit (Δχ²\[6\] relative to the configural model = 190 and 139). Score tests, which do not use H1, ranked the mental-illness threshold among the four most violated constraints in both surveys, alongside verbal abuse, physical abuse and problem drinking. The drug-use threshold was not flagged in BRFSS (p = .72).
- **Latent gap.** Freeing the three target items reduced the estimated Spanish–English gap in latent household dysfunction from −0.61 to −0.47 in BRFSS and from −0.67 to −0.58 in CHIS.
- **Anchors.** The mental-illness DIF was negative and significant in 10 of 11 specifications (Figure 2). The exception was the pre-specified BRFSS model with purified anchors (separation/divorce and physical abuse only), in which none of the three target effects remained significant (OR-equivalents 0.68–0.79; p ≥ .11). Drug-use and incarceration DIF held in 7 of 11 specifications each.
- **Alignment.** This anchor-free check, which assumes most items are invariant, placed the largest negative shift on mental illness in both surveys (−0.47 and −0.65), a smaller one on incarceration (−0.21, −0.18) and none on drug use (0.01, 0.02).
- **Other items.** At the same latent level, Spanish-interview respondents endorsed physical abuse more often (OR-equivalent 2.04 in BRFSS, 3.21 in CHIS) and verbal abuse less often (0.31, 0.45). Problem drinking was endorsed more often relative to separation/divorce (2.80, 1.52), so the two household anchors disagree.
- **Eleven-item model.** The BRFSS three-factor model with the sexual-abuse items gave the same target estimates (b from −0.63 to −0.70).
- **Interview mode (CHIS).** Mental-illness DIF was similar by phone and on the web (OR-equivalents 0.65 and 0.58; interaction p = .65). Incarceration DIF appeared only on the web (0.31 vs 0.78; p = .009).

### Impact on ACE summary scores

Removing the three target direct effects would shrink the model-implied Spanish–English gap in the mean 8-item count by 15% in BRFSS (−0.94 to −0.80) and 10% in CHIS (−0.84 to −0.75). The gap in reporting 4 or more of the 8 items would shrink by 18% (−15.0 to −12.2 percentage points) and 12% (−13.7 to −12.1). Most of the language gap in ACE scores therefore remains after accounting for the target-item DIF. The BRFSS figures assume that problem drinking is an invariant anchor, which the one-at-a-time analysis contradicts, so they are an upper-range estimate.

## Figures and tables

**Table 1. Sample characteristics by interview language, Hispanic adults (weighted %)**

| Characteristic | BRFSS, English | BRFSS, Spanish | CHIS, English | CHIS, Spanish |
| --- | --- | --- | --- | --- |
| Unweighted n | 24,473 | 10,945 | 24,418 | 5,536 |
| Age 65 or older | 9.6 | 15.4 | 10.9 | 16.5 |
| Female | 49.3 | 55.5 | 50.3 | 52.9 |
| Eighth grade or less | 3.6 | 38.7 | 7.0 | 39.9 |
| Bachelor's degree or more | 24.1 | 6.7 | 28.7 | 6.1 |
| Low income | 18.3 | 47.6 | 38.9 | 67.7 |
| Born outside the US | — | — | 27.7 | 92.2 |
| Speaks English not well or not at all | — | — | 5.4 | 59.4 |
| Interviewed by telephone | 100 | 100 | 13.3 | 34.1 |

Low income: BRFSS household income below $25,000; CHIS below 200% of the federal poverty level. — = not collected in BRFSS. The full table is in the Supplement.

**Table 2. Weighted prevalence of ACE items by interview language and adjusted prevalence ratios (aPR), Hispanic adults**

| Item | BRFSS English % | BRFSS Spanish % | BRFSS aPR (95% CI) | CHIS English % | CHIS Spanish % | CHIS aPR (95% CI) |
| --- | --- | --- | --- | --- | --- | --- |
| Household mental illness | 21.9 | 4.0 | 0.24 (0.19–0.31) | 23.8 | 5.6 | 0.35 (0.30–0.40) |
| Household drug use | 14.2 | 3.1 | 0.21 (0.17–0.26) | 14.5 | 4.6 | 0.32 (0.27–0.37) |
| Household incarceration | 14.0 | 2.6 | 0.20 (0.16–0.26) | 13.1 | 2.6 | 0.22 (0.17–0.28) |
| Household problem drinking | 25.3 | 16.8 | 0.68 (0.60–0.77) | 30.1 | 18.4 | 0.60 (0.56–0.65) |
| Parental separation/divorce | 39.0 | 24.7 | 0.66 (0.60–0.72) | 30.5 | 21.0 | 0.70 (0.65–0.75) |
| Witnessed parental violence | 23.1 | 17.1 | 0.67 (0.59–0.76) | 27.6 | 20.3 | 0.69 (0.63–0.75) |
| Physical abuse | 33.8 | 30.4 | 0.88 (0.80–0.97) | 28.5 | 29.4 | 1.00 (0.94–1.05) |
| Verbal abuse | 40.8 | 18.1 | 0.51 (0.45–0.57) | 45.8 | 27.3 | 0.67 (0.63–0.70) |
| 4+ ACEs (8-category score) | 25.3 | 10.8 | 0.43 (0.37–0.51) | 26.1 | 13.6 | 0.56 (0.51–0.62) |

aPR: survey-weighted Poisson models adjusted for age group, sex, education, income (BRFSS) or poverty level (CHIS), survey year and, in BRFSS, Census region. Design-based CIs for the prevalence estimates are in the Supplement.

&#91;embedded content: Primary and one-at-a-time MIMIC models · BRFSS 2019–2025 (n = 35,418), CHIS 2021–2025 (n = 29,954)\]

**Figure 1. Item-level DIF by interview language.** Odds-ratio equivalents, exp(1.7b), of the direct effect of a Spanish interview on each item at the same latent level, from MIMIC models adjusted for age, sex, education, income or poverty, survey year and (BRFSS) region. The three target items come from the primary model (model S1 in the right panel), with replicate-weight CIs. Each other item was freed in turn with the rest as anchors (robust CIs). The right panel adds nativity and percentage of life in the US.

&#91;embedded content: Pre-specified primary and secondary models · BRFSS 2019–2025, CHIS 2021–2025\]

**Figure 2. Robustness of the three target items' DIF.** One factor: all eight items on a single factor. Purified anchors: anchors with significant DIF freed iteratively (BRFSS: verbal abuse, problem drinking, witnessed violence; CHIS: physical abuse). 11 items: BRFSS model with the sexual-abuse items. Phone and web: estimates from a CHIS model with a language × mode interaction. CIs use replicate weights for the primary, nativity and foreign-born models and robust standard errors otherwise.

**Supplement.** eFigure 1: item prevalence by interview language. eFigure 2: impact of the target DIF on ACE summary scores. eTables: full sample characteristics, prevalence CIs, multigroup CFA fit and score tests, and deviations from the analysis plan.

## Discussion

In two surveys with independent Spanish translations, Spanish-interview Hispanic adults were less likely than English-interview Hispanic adults to report a mentally ill, drug-using or incarcerated household member, even at the same level of household dysfunction. The pre-specified test supported this for all three items in both surveys. Only the mental-illness difference, however, remained significant after nativity adjustment, among immigrants alone and in most alternative anchor sets. The drug-use and incarceration differences tracked nativity in CHIS, and in BRFSS all three depended on treating problem drinking as an anchor.

### Interpretation

**Mental illness.** A language-specific reporting difference is one plausible reading. The item asks respondents to label a household member as depressed, mentally ill or suicidal. In Spanish, that label carries stigma, and families may describe the same distress as "nervios" rather than mental illness (Jenkins 1988; Interian et al. 2007; Vega et al. 2010). The translated label itself may also matter: the K6 item "depressed" showed language DIF in CHIS (Kim et al. 2016).

The difference persisted among foreign-born adults, where interview language reflects English proficiency and acculturation rather than birthplace. It also persisted in self-administered web interviews, which argues against interviewer-driven social desirability as the only cause. Lower recognition of a relative's condition is an alternative to unwillingness to disclose: proxy reports of household mental illness are low even in English (Ng et al. 2025). In exploratory analyses, ACE counts predicted depression (BRFSS) and serious psychological distress (CHIS) equally in both languages, so items that are endorsed appear to carry the same meaning.

**Drug use and incarceration.** Once nativity was accounted for, these differences disappeared, and they were absent within foreign-born adults. They may reflect real differences in childhood environments outside the US, nativity-related reporting, or both; these data cannot separate the two. High household-incarceration reports in an immigrant cohort, partly attributed to political imprisonment in countries of origin, caution against assuming that immigrants under-report this item (Llabre et al. 2017).

**Abuse items.** Physical abuse was endorsed more often, and verbal abuse less often, in Spanish at the same latent level. This is consistent with earlier prevalence differences by questionnaire language (Alhalel 2018). The verbal-abuse difference was larger in BRFSS than in CHIS, which fits CDC's Spanish wording "humillaba" (humiliated) setting a higher bar than "put you down"; this comparison was exploratory.

### Relation to prior work

Earlier invariance studies of the BRFSS items did not examine language (Ford et al. 2014; Mei et al. 2022), and Mei et al. pooled Hispanic respondents across interview languages and relied on omnibus fit indices. Our item-level results align with a dissertation that located racial and ethnic non-invariance in the same household items (Umoga 2026) and with threshold non-invariance in parent-reported child ACEs (Jensen et al. 2024). The only earlier Spanish–English test, of a broader adversity model, found only partial scalar invariance (Cooper & Nickodem 2021).

### Implications for ACE surveillance

- **Comparisons by language.** Household mental-illness reports may not be comparable across interview languages, so comparisons on this item by language or ethnicity need caution.
- **Summary scores.** In model-implied estimates, the three items' DIF accounts for only 10–18% of the language gap in 8-item ACE counts. The remaining gap is consistent with lower adversity among immigrants (Caballero et al. 2017; Vaughn et al. 2017), but uniform under-reporting cannot be ruled out.
- **Instrument documentation.** CDC has not posted the 2021–2025 Spanish questionnaires, and states may adapt the Spanish wording (CDC 2024). Publishing the Spanish text used each year would let analysts account for wording changes.
- **Item revision.** The Spanish mental-illness item is a priority for cognitive testing, for example wording that describes behaviors or mentions "nervios".

### Limitations

- **Relative DIF.** Uniform under-reporting across all items cannot be detected (Bechger & Maris 2015), and the estimates depend on the anchors. Our two household anchors disagreed, and purified anchors removed the BRFSS effects.
- **Non-random language.** Interview language bundles acculturation, education and nativity. BRFSS lacks nativity, and residual confounding is likely in both surveys. The BRFSS sample covers only the 11–28 states per year that fielded the ACE module, so it is not nationally representative.
- **Not confirmatory.** The hypothesis came from exploratory analyses of the same data. The specification was locked before fitting, but this is not a confirmatory test.
- **Retrospective self-report.** Retrospective ACE reports agree only modestly with prospective records (Baldwin et al. 2019; Hardt & Rutter 2004).
- **Varying instruments.** Spanish wording varies across years, states and surveys; the BRFSS 2021–2025 Spanish text is unpublished.
- **CHIS specifics.** CHIS imputes item nonresponse, withholds individual sexual-abuse items, covers only California and is mostly web-based.
- **Model choice.** Whether ACEs fit a reflective latent model is debated (Moriarity & Slavich 2025; LaNoue & Hass 2025). We interpret DIF as differential reporting, not as evidence about a latent trait.

### Conclusion

The household mental-illness ACE item functions differently by interview language among Hispanic adults. The difference appears in two surveys with independent translations and remains, attenuated, after nativity adjustment in CHIS. ACE comparisons involving Spanish-speaking respondents should account for this item, and its Spanish wording should be retested.

## References

All entries were checked against Crossref or PubMed on 2 November 2026. They are listed alphabetically to match the author–year citations in this draft; renumber in citation order for an AMA-style journal.

1. Alhalel N. *Prevalence and Impact of Adverse Childhood Experiences in the Hispanic Community by Questionnaire Language Preference: Behavioral Risk Factor Surveillance System (BRFSS) 2011, 2012*. Master of Public Health culminating experience. Northwestern University; 2018. doi:10.18131/g3-a5x4-zh93
2. Asparouhov T, Muthén B. Multiple-group factor analysis alignment. *Struct Equ Modeling*. 2014;21(4):495-508. doi:10.1080/10705511.2014.919210
3. Baldwin JR, Reuben A, Newbury JB, Danese A. Agreement between prospective and retrospective measures of childhood maltreatment: a systematic review and meta-analysis. *JAMA Psychiatry*. 2019;76(6):584-593. doi:10.1001/jamapsychiatry.2019.0097
4. Bechger TM, Maris G. A statistical test for differential item pair functioning. *Psychometrika*. 2015;80(2):317-340. doi:10.1007/s11336-014-9408-y
5. Bzostek S, Goldman N, Pebley A. Why do Hispanics in the USA report poor health? *Soc Sci Med*. 2007;65(5):990-1003. doi:10.1016/j.socscimed.2007.04.028
6. Caballero TM, Johnson SB, Buchanan CRM, DeCamp LR. Adverse childhood experiences among Hispanic children in immigrant families versus US-native families. *Pediatrics*. 2017;140(5):e20170297. doi:10.1542/peds.2017-0297
7. Camilli G. Origin of the scaling constant d = 1.7 in item response theory. *J Educ Behav Stat*. 1994;19(3):293. doi:10.2307/1165298
8. California Health Interview Survey. *CHIS 2023 Methodology Series: Report 5—Weighting and Variance Estimation*. UCLA Center for Health Policy Research; 2024.
9. Centers for Disease Control and Prevention. *Preventing Adverse Childhood Experiences: Leveraging the Best Available Evidence*. National Center for Injury Prevention and Control; 2019.
10. Centers for Disease Control and Prevention. *Behavioral Risk Factor Surveillance System: 2023 BRFSS Overview*. Centers for Disease Control and Prevention; 2024. [PDF](https://www.cdc.gov/brfss/annual_data/2023/pdf/Overview_2023-508.pdf)
11. Cooper DK, Nickodem K. Cumulative lifetime adversity in a national sample of Hispanic/Latino immigrants: exploring construct validity across six Hispanic/Latino groups using data from the HCHS/SOL Sociocultural Ancillary Study. *Eval Health Prof*. 2021;44(4):348-361. doi:10.1177/0163278720910470
12. Corrigan PW, Watson AC, Miller FE. Blame, shame, and contamination: the impact of mental illness and drug dependence stigma on family members. *J Fam Psychol*. 2006;20(2):239-246. doi:10.1037/0893-3200.20.2.239
13. DuBard CA, Gizlice Z. Language spoken and differences in health status, access to care, and receipt of preventive services among US Hispanics. *Am J Public Health*. 2008;98(11):2021-2028. doi:10.2105/AJPH.2007.119008
14. Felitti VJ, Anda RF, Nordenberg D, et al. Relationship of childhood abuse and household dysfunction to many of the leading causes of death in adults: the Adverse Childhood Experiences (ACE) Study. *Am J Prev Med*. 1998;14(4):245-258. doi:10.1016/S0749-3797(98)00017-8
15. Finch H. The MIMIC model as a method for detecting DIF: comparison with Mantel-Haenszel, SIBTEST, and the IRT likelihood ratio. *Appl Psychol Meas*. 2005;29(4):278-295. doi:10.1177/0146621605275728
16. Ford DC, Merrick MT, Parks SE, et al. Examination of the factorial structure of adverse childhood experiences and recommendations for three subscale scores. *Psychol Violence*. 2014;4(4):432-444. doi:10.1037/a0037723
17. Grest CV, Finno-Velasquez M, Cederbaum JA, et al. Adverse childhood experiences among 3 generations of Latinx youth. *Am J Prev Med*. 2021;60(1):20-28. doi:10.1016/j.amepre.2020.07.007
18. Hardt J, Rutter M. Validity of adult retrospective reports of adverse childhood experiences: review of the evidence. *J Child Psychol Psychiatry*. 2004;45(2):260-273. doi:10.1111/j.1469-7610.2004.00218.x
19. Holm S. A simple sequentially rejective multiple test procedure. *Scand J Stat*. 1979;6:65-70.
20. Interian A, Martinez IE, Guarnaccia PJ, Vega WA, Escobar JI. A qualitative analysis of the perception of stigma among Latinos receiving antidepressants. *Psychiatr Serv*. 2007;58(12):1591-1594. doi:10.1176/ps.2007.58.12.1591
21. Jenkins JH. Ethnopsychiatric interpretations of schizophrenic illness: the problem of nervios within Mexican-American families. *Cult Med Psychiatry*. 1988;12(3):301-329. doi:10.1007/BF00051972
22. Jensen TM, Bernard DL, Lanier P. Conceptualizing adverse childhood experiences as a latent factor: tests of measurement invariance across five racial and ethnic groups. *Child Dev*. 2024;95(3):e170-e185. doi:10.1111/cdev.14050
23. Jones RN. Identification of measurement differences between English and Spanish language versions of the Mini-Mental State Examination: detecting differential item functioning using MIMIC modeling. *Med Care*. 2006;44(11 suppl 3):S124-S133. doi:10.1097/01.mlr.0000245250.50114.0f
24. Kim G, DeCoster J, Bryant AN, Ford KL. Measurement equivalence of the K6 scale: the effects of race/ethnicity and language. *Assessment*. 2016;23(6):758-768. doi:10.1177/1073191115599639
25. LaNoue MD, Hass RW. Conceptualizing self-reported adverse childhood experiences: from epidemiologic exposure to psychometric latent variable. *Soc Sci Med*. 2025;366:117664. doi:10.1016/j.socscimed.2024.117664
26. Llabre MM, Schneiderman N, Gallo LC, et al. Childhood trauma and adult risk factors and disease in Hispanics/Latinos in the US: results from the Hispanic Community Health Study/Study of Latinos (HCHS/SOL) Sociocultural Ancillary Study. *Psychosom Med*. 2017;79(2):172-180. doi:10.1097/PSY.0000000000000394
27. Lumley T. Analysis of complex survey samples. *J Stat Softw*. 2004;9(8). doi:10.18637/jss.v009.i08
28. Luther K. Stigma management among children of incarcerated parents. *Deviant Behav*. 2016;37(11):1264-1275. doi:10.1080/01639625.2016.1170551
29. Mei X, Li J, Li ZS, et al. Psychometric evaluation of an Adverse Childhood Experiences (ACEs) measurement tool: an equitable assessment or reinforcing biases? *Health Justice*. 2022;10(1):34. doi:10.1186/s40352-022-00198-2
30. Moriarity DP, Slavich GM. Theoretical and quantitative disconnect when modeling adverse childhood experiences using a common factor framework: an argument for causal indicator models in stressor research. *Child Dev*. 2025;96(4):1255-1259. doi:10.1111/cdev.14230
31. Muthén BO. Latent variable modeling in heterogeneous populations. *Psychometrika*. 1989;54(4):557-585. doi:10.1007/BF02296397
32. Ng AE, Swedo E, Zablotsky B, et al. Parent-teen concordance of selected adverse childhood experiences in a national sample of teenagers: findings from National Health Interview Survey–Teen. *Child Abuse Negl*. 2025;163:107339. doi:10.1016/j.chiabu.2025.107339
33. Pérez EO. The origins and implications of language effects in multilingual surveys: a MIMIC approach with application to Latino political attitudes. *Polit Anal*. 2011;19(4):434-454. doi:10.1093/pan/mpr029
34. Rao JNK, Wu CFJ, Yue K. Some recent work on resampling methods for complex surveys. *Surv Methodol*. 1992;18(2):209-217.
35. Rosseel Y. lavaan: an R package for structural equation modeling. *J Stat Softw*. 2012;48(2). doi:10.18637/jss.v048.i02
36. Satorra A. Scaled and adjusted restricted tests in multi-sample analysis of moment structures. In: Heijmans RDH, Pollock DSG, Satorra A, eds. *Innovations in Multivariate Statistical Analysis*. Springer; 2000:233-247. doi:10.1007/978-1-4615-4603-0\_17
37. Swedo EA, Aslam MV, Dahlberg LL, et al. Prevalence of adverse childhood experiences among U.S. adults—Behavioral Risk Factor Surveillance System, 2011–2020. *MMWR Morb Mortal Wkly Rep*. 2023;72(26):707-715. doi:10.15585/mmwr.mm7226a2
38. Tourangeau R, Yan T. Sensitive questions in surveys. *Psychol Bull*. 2007;133(5):859-883. doi:10.1037/0033-2909.133.5.859
39. Umoga C. *Beyond Adversity Alone: Heterogeneity in Childhood Experiences and Implications for Mental and Behavioral Health*. Dissertation. Harvard University; 2026. Harvard DASH handle 1/42760678 (embargoed until April 2027).
40. van den Akker OR, Weston SJ, Campbell L, et al. Preregistration of secondary data analysis: a template and tutorial. *Meta-Psychology*. 2021;5. doi:10.15626/MP.2020.2625
41. Vaughn MG, Salas-Wright CP, Huang J, Qian Z, Terzis LD, Helton JJ. Adverse childhood experiences among immigrants to the United States. *J Interpers Violence*. 2017;32(10):1543-1564. doi:10.1177/0886260515589568
42. Vega WA, Rodriguez MA, Ang A. Addressing stigma of depression in Latino primary care patients. *Gen Hosp Psychiatry*. 2010;32(2):182-191. doi:10.1016/j.genhosppsych.2009.10.008
43. Viruell-Fuentes EA, Morenoff JD, Williams DR, House JS. Language of interview, self-rated health, and the other Latino health puzzle. *Am J Public Health*. 2011;101(7):1306-1313. doi:10.2105/AJPH.2009.175455
44. von Elm E, Altman DG, Egger M, Pocock SJ, Gøtzsche PC, Vandenbroucke JP; STROBE Initiative. The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. *Lancet*. 2007;370(9596):1453-1457. doi:10.1016/S0140-6736(07)61602-X
45. Woods CM. Evaluation of MIMIC-model methods for DIF testing with comparison to two-group analysis. *Multivariate Behav Res*. 2009;44(1):1-27. doi:10.1080/00273170802620121
46. Yan T, Cantor D. Asking survey questions about criminal justice involvement. *Public Health Rep*. 2019;134(1 suppl):46S-56S. doi:10.1177/0033354919826566

## Author notes (remove before submission)

**Novelty: confirmed** as of 2 November 2026, after 55 logged searches across PubMed, Europe PMC (including preprints), OpenAlex, Crossref, Harvard's repository and the web. No paper, preprint, dissertation or abstract tests ACE item functioning by interview language, nativity or acculturation. All five claims hold: language DIF in BRFSS, language DIF in CHIS, the stigmatized-household pattern, replication across two Spanish translations, and DIF that persists after nativity adjustment.

- **Closest works (must cite):** Alhalel 2018 (BRFSS prevalence by questionnaire language, not conditional on other items); Cooper & Nickodem 2021 (Spanish–English invariance of a broader adversity model, all-immigrant sample); Umoga 2026 (BRFSS non-invariance across race groups, concentrated in the mental illness, incarceration and alcohol items; embargoed until April 2027).
- **What to claim:** the first *conditional* (DIF) test by interview language, and the two-survey, nativity-adjusted replication. Do not claim the first evidence of lower reporting: Alhalel 2018 and Grest et al. 2021 already show lower raw prevalence.
- **Before submission:** read Zhang & Lippert 2026 (BRFSS IRT scoring, paywalled) through NYU Libraries; email Umoga or her advisor about any language analysis; run a manual SciELO/LILACS search, which blocked automated tools.

**What the pre-specified test found.** H1 was supported: all six target effects met the decision rule. H1b was not: after nativity adjustment in CHIS, only household mental illness stayed significant. The BRFSS effects also lost significance with purified anchors. Lead with mental illness in the title and the cover letter, and present drug use and incarceration as nativity-related.

**Files on the analysis machine** (`/home/mo2273/ace_manuscript/`):

- `prereg/`: the frozen analysis plan and its SHA-256 hash, ready to upload to OSF
- `analysis/`: RESULTS.md, DEVIATIONS.md, Tables 1–2, and every model output
- `figures/`: publication versions of all four figures (PNG at 300 dpi, PDF, plotted data as CSV); figures 2 and 3 there match Figures 1 and 2 here, and figures 1 and 4 are eFigures 1 and 2
- `scripts/`: R and Python code for the full analysis

**Where to submit.** Recommended: *American Journal of Preventive Medicine* (AJPM), as a Research Article, or as a Research Brief if we cut to 1,200 words. Post a medRxiv preprint first.

| Journal | Format | Words | Display items | Cost to NYU authors | Why |
| --- | --- | --- | --- | --- | --- |
| AJPM (top pick) | Research Article / Research Brief | 3,000 / 1,200 | 4 / 4 + online appendix | No fee for regular articles | Prevention audience, appendix holds DIF detail, preprints allowed anywhere |
| Preventing Chronic Disease (backup) | Original Research / Research Brief | 3,500 / 1,200 | 5 / 3 | No fees | Long record of BRFSS ACE papers; risk: CDC editorial staff cuts reported Oct 2026 |
| PLOS ONE (backup) | Research Article | No limit | No limit | Free via NYU–PLOS agreement (list $2,477) | Fast, no length limits, preprints encouraged |
| JSSAM or *Survey Research Methods* (alternative) | Research note / article | \~3,000 | — | Varies | If we pitch it as a survey-methods paper on language effects |

Limits for Elsevier, APHA, SAGE and APA journals came partly from secondary summaries; check the live author guidelines before submitting.

**Do "letters" work here?** Research letters exist (JAMA Network Open: 800 words, 2 display items; AJPM: 700 words, 1 display item), but they cannot hold item-level DIF results for two surveys plus sensitivity analyses. The public-health version of a substantive math letter is the *research brief*: about 1,200 words, structured abstract, 3–4 display items and an online appendix. In this field, speed and priority come from a preprint (medRxiv screens in 2–4 days and issues a DOI), not from the short format.

**Pre-registration framing.** OSF's secondary-data template (van den Akker et al. 2021) asks each author about prior access and knowledge. It also advises against calling an analysis confirmatory when the authors already know the hypothesized association. We therefore register the locked specification and present the study as an exploratory finding replicated across two independent surveys, not as a confirmatory test.

**Ethics.** NYU's IRB decision tree classes public-use data as not human-subjects research, with no application needed. Some journals want a written determination, so request one from NYU's human research protection office (ask.humansubjects@nyu.edu). Check whether CHIS's click-through terms of use change that.

**Open items**

- [ ] Choose journal and format (AJPM Research Article vs Research Brief)
- [ ] Register the frozen analysis plan on OSF, disclosing prior exposure
- [ ] Request a written NYU determination
- [ ] Author list, affiliations, funding, conflicts of interest
- [ ] Public code repository
- [ ] Co-author review of the anchor choice and factor structure
- [ ] Trim the main text to AJPM's 3,000-word limit (currently about 3,300)
- [ ] Convert author–year citations to AMA numbering
- [ ] Build the Supplement: sample-flow diagram (STROBE), eFigures 1–2, full Table 1, prevalence CIs, MGCFA tables, deviations, exploratory results, literature search log
- [ ] Add funding, conflict-of-interest and data/code availability statements
- [ ] When registering on OSF, state that the registration postdates the analysis; upload the frozen plan, its SHA-256 hash and DEVIATIONS.md
- [ ] Post a medRxiv preprint no later than submission, and before Umoga's dissertation opens on 19 April 2027
