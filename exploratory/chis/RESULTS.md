# CHIS 2021–2025: do the BRFSS language gaps survive an independent translation and a nativity adjustment?

First pass, 2026-11-01. Data: CHIS adult public-use files 2021–2025, pooled (weights ÷ 5). Hispanic adults (OMBSRR_P1 = 1) interviewed in English or Spanish (INTVLNGC_P1). Standard errors use jackknife replicate weights (RAKEDW1–80, multiplier 1, MSE).

**N:** 29,954 Hispanic adults. 5,536 were interviewed in Spanish (5,134 of them foreign-born; 1,844 by phone, 3,692 on the web). 24,418 were interviewed in English (6,305 foreign-born).

**Why CHIS matters:** it asks the same 11 BRFSS ACE items, but uses CHIS's own Spanish translation, and about 90% of interviews are self-administered on the web. It also records nativity and percent of life spent in the US, neither of which BRFSS has.

## 1. Item gaps, Spanish vs English interview (odds ratio < 1 = less endorsed in Spanish)

| Item | Sp % | En % | aOR, BRFSS-style covariates | aOR + nativity + % life in US [95% CI] | aOR, foreign-born only [95% CI] | DIF OR (rest score + nativity) [95% CI] | BRFSS DIF OR (covariate-adj.) |
|---|---|---|---|---|---|---|---|
| HH mental illness | 5.6 | 23.8 | 0.30 | **0.41 [0.34, 0.49]** | **0.44 [0.35, 0.55]** | **0.50 [0.40, 0.62]** | 0.33 |
| HH drug use | 4.6 | 14.5 | 0.28 | 0.45 [0.38, 0.55] | 0.56 [0.43, 0.73] | 0.63 [0.50, 0.79] | 0.34 |
| HH incarceration | 2.6 | 13.1 | 0.19 | 0.40 [0.30, 0.53] | 0.54 [0.35, 0.82] | 0.57 [0.41, 0.80] | 0.30 |
| HH problem drinker | 18.4 | 30.1 | 0.51 | 0.59 [0.54, 0.66] | 0.64 [0.56, 0.73] | 0.74 [0.65, 0.83] | 1.11 |
| Parents separated/divorced | 21.0 | 30.5 | 0.61 | 0.71 [0.63, 0.80] | 0.78 [0.67, 0.91] | 0.80 [0.71, 0.91] | 0.66 |
| Witnessed parental violence | 20.4 | 27.6 | 0.61 | 0.63 [0.56, 0.72] | 0.69 [0.60, 0.80] | 0.84 [0.73, 0.96] | 1.17 |
| Physical abuse | 29.4 | 28.5 | 1.00 | 0.97 [0.88, 1.07] | 1.09 [0.96, 1.23] | **1.51 [1.33, 1.71]** | 1.40 |
| Verbal abuse | 27.3 | 45.8 | 0.53 | 0.60 [0.54, 0.66] | 0.70 [0.62, 0.80] | 0.74 [0.66, 0.84] | 0.54 |
| Sexual abuse (any)* | 11.6 | 14.0 | 0.76 | 0.72 [0.61, 0.83] | 0.72 [0.61, 0.85] | 0.83 [0.70, 0.97] | 0.99–1.55 (3 items) |
| 4+ ACEs | 13.6 | 26.1 | 0.48 | 0.58 [0.51, 0.67] | 0.72 [0.61, 0.86] | — | — |
| Serious psych. distress (K6, past month) | 4.9 | 11.2 | 0.48 | 0.58 [0.48, 0.71] | 0.65 [0.52, 0.81] | — | — |
| Fair/poor general health | 35.9 | 17.8 | 1.38 | **1.73 [1.53, 1.95]** | 1.81 [1.56, 2.10] | — | — |

Covariates: age, sex, education, poverty level, year. The "+ nativity" column adds US-born and percent of life in the US. The DIF column conditions on the rest score: the sum of the other seven non-sexual items, with drinking and drugs counted separately. BRFSS DIF ORs come from `../dif/RESULTS.md` (covariate-adjusted, no nativity). *The sexual-abuse items are not released separately in the public file. "Any" is recovered from ACE8 minus the other seven categories (no inconsistencies found), but it is unknown for the 6,197 people with 4+ other ACEs, so it is biased toward low scorers.

## 2. Phone vs web

The Spanish-vs-English ORs are similar whether the interview was by phone (interviewer present) or on the web (self-administered):

| Item | Phone | Web |
|---|---|---|
| HH mental illness | 0.31 | 0.44 |
| HH drug use | 0.29 | 0.48 |
| HH incarceration | 0.43 | 0.32 |
| Physical abuse | 1.08 | 0.95 |
| Serious distress | 0.63 | 0.59 |

The interaction p-values are mostly above .05 (mental illness .13, drugs .44, jail .08). The exceptions are verbal abuse, where the gap is a little smaller on the web (interaction p < .001), and 4+ ACEs (p = .04). So the gap is **not mainly about saying it aloud to an interviewer.**

## 3. Differential prediction (outcome: serious psychological distress, adjusted incl. nativity)

- OR per ACE: 1.37 for English-interview vs 1.45 for Spanish-interview respondents (interaction p = .29).
- Household-mental-illness item → distress: 3.29 vs 3.10 (p = .75).

This repeats the BRFSS depression result: once endorsed, the items carry the same risk signal in both languages.

## Takeaways

1. **CHIS replicates the BRFSS pattern with a different Spanish translation and a mostly self-administered mode.** Household mental illness, drugs and incarceration show the largest Spanish deficits, and physical abuse is at parity.
2. **Nativity explains part of the gap, and the part varies by item.** Incarceration (0.19 → 0.54 among foreign-born) and drugs (0.28 → 0.56) are substantially explained by immigrant status. **Household mental illness is the most stubborn** (0.30 → 0.44 among foreign-born; DIF OR 0.48 within foreign-born). Language-specific under-reporting is most plausible there.
3. **Verbal abuse looks partly like a BRFSS translation artifact.** Spanish endorsement is 27% in CHIS vs 18% in BRFSS, while English is similar (46% vs 42%). The DIF OR is 0.74 in CHIS vs 0.42–0.54 in BRFSS. That fits the BRFSS Spanish wording "humillaba" (humiliated) setting a higher bar. It's a cross-survey comparison (California vs national, web vs phone), so treat it as suggestive.
4. **Spanish-interview respondents are not generally reticent.** They report *more* fair/poor health (aOR 1.73, the known "regular" translation effect) but *less* distress and less household mental illness. Whatever is happening is specific to the topic.
5. **ACEs predict distress equally in both languages,** a second dataset showing no differential prediction.

## Caveats

- **The anchor problem is unchanged.** These are relative DIF estimates; uniform under-reporting across all items would be invisible.
- **Imputed items.** CHIS public-file items have no missing values (they appear to have been imputed), so refusal patterns can't be studied.
- **California only.** The population differs from multi-state BRFSS.
- **Nativity reduces but can't remove confounding.** Real differences by childhood country (e.g., incarceration contexts) remain plausible.
- **This is now exploratory too.** The CHIS analysis was not pre-registered. A confirmatory test would need data not yet analysed (CHIS 2026 when released, or HCHS/SOL).

Scripts: `/home/mo2273/ace_tonight_scripts/chis/` (`build.py`, `analyze.py`). Tables: `out/or_table.csv`, `out/dif_table.csv`, `out/mode_table.csv`, `out/log.txt`.
