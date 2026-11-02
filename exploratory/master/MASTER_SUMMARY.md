# Master comparison: BRFSS + CHIS, Spanish vs English interview (Hispanic adults)

All numbers come from data already analysed tonight (`ladder.csv`, `meta.csv` in this folder). First pass, 2026-11-01.

## 1. What is being compared

**Samples**

| Sample | Spanish interview | English interview |
|---|---|---|
| BRFSS 2019–2025, Hispanic adults, 50 states + DC (main + version files, all 11 ACE items answered) | 10,945 | 24,473 |
| CHIS 2021–2025, Hispanic adults, California | 5,536 | 24,418 |
| CHIS foreign-born only | 5,134 | 6,305 |
| CHIS by interview mode | 1,844 phone / 3,692 web | 3,104 phone / 21,314 web |

**Items.** The two surveys use the same English wording (CHIS copied the BRFSS module) but different Spanish translations. Each item is turned into yes/no and analysed separately.

| Category | Section | BRFSS variable | CHIS variable | Question (short) | Counted as "yes" |
|---|---|---|---|---|---|
| Household mental illness | Household dysfunction | ACEDEPRS | AQ1 | Lived with anyone depressed, mentally ill, or suicidal | Yes |
| Household problem drinking | Household dysfunction | ACEDRINK | AQ2 | Lived with a problem drinker/alcoholic | Yes |
| Household drug use | Household dysfunction | ACEDRUGS | AQ3 | Lived with anyone using illegal drugs or misusing prescriptions | Yes |
| **Household incarceration** | Household dysfunction | **ACEPRISN** | **AQ4** | Lived with anyone who served, or was sentenced to serve, time in prison/jail/corrections. **This is the only incarceration question.** | Yes |
| Parental separation/divorce | Household dysfunction | ACEDIVRC | AQ5 | Parents separated or divorced | Yes ("parents not married" = no; recoding it changes nothing) |
| Witnessed parental violence | Household dysfunction | ACEPUNCH | AQ6 | Parents/adults slapped, hit, kicked, punched or beat each other | Once or more |
| Physical abuse | Abuse | ACEHURT | AQ7 | Parent/adult hit, beat, kicked or physically hurt you (not spanking) | Once or more |
| Verbal/emotional abuse | Abuse | ACESWEAR | AQ8 | Parent/adult swore at, insulted or put you down | Once or more |
| Sexual abuse (any of 3) | Abuse | ACETOUCH, ACETTHEM, ACEHVSEX | not released separately | Touched sexually / made to touch / forced sex | Any once or more. In CHIS it's rebuilt from the ACE score; unknown for people with 4+ other ACEs |

The "stigmatized household conditions" label (mental illness, drugs, incarceration) is a grouping **suggested by the results**, not decided in advance. A pre-registration has to say so.

## 2. Step-by-step adjustment: how much of each gap do other variables explain?

Each cell is the Spanish-vs-English odds ratio. 1.0 = no difference; 0.5 = half the odds. "*" = statistically significant (95% CI excludes 1). [x%] = share of the crude gap (on the log scale) explained by that step.

**BRFSS**

| Item | Sp % / En % | Crude | + age, sex | + education, income | + year, state | + other ACE items (DIF) |
|---|---|---|---|---|---|---|
| Mental illness | 4.7 / 22.5 | 0.17* | 0.19* | 0.22* | 0.22* [15%] | 0.36* [42%] |
| Drug use | 3.5 / 14.8 | 0.21* | 0.22* | 0.19* | 0.21* [−1%] | 0.42* [45%] |
| Incarceration | 3.1 / 14.2 | 0.19* | 0.22* | 0.19* | 0.20* [3%] | 0.37* [40%] |
| Problem drinking | 16.6 / 25.8 | 0.57* | 0.58* | 0.54* | 0.56* [−4%] | 1.06 |
| Divorce | 25.4 / 39.4 | 0.53* | 0.56* | 0.54* | 0.53* [1%] | 0.68* |
| Witnessed violence | 16.1 / 23.0 | 0.64* | 0.65* | 0.56* | 0.57* | 1.17 |
| Physical abuse | 28.9 / 33.7 | 0.80* | 0.81* | 0.80* | 0.78* | 1.37* |
| Verbal abuse | 16.3 / 40.8 | 0.28* | 0.30* | 0.33* | 0.34* [14%] | 0.50* [45%] |
| Sexual (any) | 9.0 / 16.4 | 0.51* | 0.49* | 0.45* | 0.48* | 0.91 |

**CHIS (adds nativity and mode)**

| Item | Sp % / En % | Crude | + age, sex, educ, income, year | + nativity, % life in US | + mode | Foreign-born only | + other ACE items (DIF) |
|---|---|---|---|---|---|---|---|
| Mental illness | 5.6 / 23.8 | 0.19* | 0.30* [27%] | **0.41* [46%]** | 0.40* | 0.44* [51%] | 0.50* |
| Drug use | 4.6 / 14.5 | 0.28* | 0.28* [0%] | 0.45* [38%] | 0.44* | 0.56* [54%] | 0.63* |
| Incarceration | 2.6 / 13.1 | 0.18* | 0.19* [6%] | 0.40* [47%] | 0.37* | 0.54* [64%] | 0.57* |
| Problem drinking | 18.4 / 30.1 | 0.52* | 0.51* | 0.59* [20%] | 0.59* | 0.64* | 0.74* |
| Divorce | 21.0 / 30.5 | 0.61* | 0.61* | 0.71* [32%] | 0.67* | 0.78* | 0.80* |
| Witnessed violence | 20.3 / 27.6 | 0.67* | 0.61* | 0.63* | 0.62* | 0.69* | 0.84* |
| Physical abuse | 29.4 / 28.5 | 1.04 | 1.00 | 0.97 | 0.95 | 1.09 | 1.51* |
| Verbal abuse | 27.3 / 45.8 | 0.44* | 0.53* [22%] | 0.60* [37%] | 0.60* | 0.70* [57%] | 0.74* |
| Sexual (any) | 11.6 / 14.0 | 0.81* | 0.76* | 0.72* | 0.72* | 0.72* | 0.83* |

## 3. Combined (meta-analysis of BRFSS + CHIS, same covariates: age, sex, education, income, year)

| Item | BRFSS OR | CHIS OR | Pooled OR [95% CI] | Do the surveys disagree? (p) |
|---|---|---|---|---|
| Mental illness | 0.22 | 0.30 | 0.27 [0.24, 0.31] | 0.06 (borderline) |
| Drug use | 0.21 | 0.28 | 0.26 [0.22, 0.29] | 0.04 |
| Incarceration | 0.20 | 0.19 | 0.20 [0.16, 0.24] | 0.83 (agree) |
| Problem drinking | 0.56 | 0.51 | 0.52 [0.48, 0.57] | 0.24 |
| Divorce | 0.53 | 0.61 | 0.58 [0.54, 0.63] | 0.08 |
| Witnessed violence | 0.57 | 0.61 | 0.59 [0.54, 0.64] | 0.47 |
| Physical abuse | 0.78 | 1.00 | 0.93 [0.87, 0.99] | 0.001 (disagree) |
| **Verbal abuse** | **0.34** | **0.53** | 0.47 [0.44, 0.50] | **<0.001 (disagree)** |
| Sexual (any) | 0.48 | 0.76 | 0.65 [0.58, 0.72] | <0.001 (disagree; CHIS item is approximate) |

DIF-level pooled ORs: mental illness 0.44, incarceration 0.46, drugs 0.53, verbal 0.63, divorce 0.74, drinking 0.85, sexual 0.86, witnessed violence 0.97 (n.s.), physical abuse 1.45. Verbal (p < .001), drinking (p < .001), witnessed violence (p = .002) and drugs (p = .03) differ between surveys at the DIF level.

Caveat: pooling assumes both surveys estimate the same thing. Where they disagree (verbal, physical, sexual), the pooled number is less meaningful than the difference itself.
