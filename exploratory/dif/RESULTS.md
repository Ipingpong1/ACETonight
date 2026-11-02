# BRFSS ACE item-level DIF by interview language (Spanish vs English) among Hispanic adults: first pass

*Prepared 2026-11-01. Preliminary: the SEs are approximate and nothing here has been externally reviewed.*

**N = 35,418 Hispanic respondents: 10,945 Spanish-interview and 24,473 English-interview.** Sample: BRFSS 2019–2025, main files plus questionnaire-version files, 41 states plus DC. PR, VI and GU are excluded. All respondents gave a substantive answer on all 11 core ACE items. Spanish respondents come from 26 states; the largest are FL 1,777, IA 1,205, TX 900, NJ 829, IL 776 and NY 678. By period (Spanish / English): 2019 1,726 / 4,371; 2020 2,995 / 7,607; 2021–2025 6,224 / 12,495. 57% of Spanish respondents fall in the years whose Spanish wording is unpublished. There are 111 state×year clusters.

## Methods (brief)

**Coding and models**
- Items use the existing `e_*` coding: yes = 1, and for frequency items "once" or "more than once" = 1. In the main analysis ACEDIVRC = 8 ("parents not married") counts as not endorsed.
- Logistic DIF models:
  - M1: item ~ S
  - M2: M1 + Spanish (uniform DIF)
  - M3: M2 + Spanish×S (non-uniform DIF)
- S is the rest score: the sum of the other 10 items, unless noted.
- Each model is a weighted binomial GLM. Weights are the final weight (`_LLCPWT` or `_LCPWTVk`) rescaled to mean 1 within each survey year.
- SEs are cluster-robust sandwich estimates with state×year clusters, and they are **approximate**. PSU is unique per respondent in these files, so stratum-PSU clustering would amount to ordinary heteroskedasticity-robust SEs. State-year clustering is the more conservative choice.
- Nagelkerke R² is computed from weighted log-likelihoods. Unweighted results are reported as a check.

**Flagging rule**
- A uniform-DIF flag needs both:
  - BH-FDR q < .05, applied across 22 Wald tests (11 uniform + 11 non-uniform) per analysis
  - an effect-size gate: ΔR²(M1→M2) ≥ .02 **or** a change of at least 10% in the rest-score coefficient (Δβ1)
- A non-uniform flag needs q < .05 and ΔR²(M2→M3) ≥ .02.
- Jodoin–Gierl (JG) categories are A < .035, B .035–.070, C ≥ .070. These are the commonly cited cutoffs; they were **not verified against the primary article** (see adversarial_methods.md).

**Covariate version**
- Covariates: age group (5-year bands, plus missing), education (plus refused), sex, harmonized income (5 groups plus missing), year, and state (states with fewer than 150 respondents pooled into one category).

**Anchor analyses**
- Purification: flagged items are dropped from S and the models refit, repeating until the flagged set stops changing.
- Anchor sets:
  - A0: all other items (unpurified)
  - A1: purified set
  - A2: problem drinker only
  - A3: drinking + divorce + the three sexual items (the a-priori "equivalent wording" anchors from brfss_feasibility.md Q7)
  - A4: the 5 non-violent household items
  - X1 (HURT+PUNCH) and X2 (SWEAR+DEPRS): two deliberately extreme sets, included only to show how far results can move
- Each anchor set is run two ways:
  - observed-score LR, matching on the anchor sum
  - a two-group unidimensional **2PL** (uniform DIF only). Anchor items have equal parameters across groups; the Spanish latent mean and SD are free; slopes are common to both groups. It is fit by weighted marginal maximum likelihood, and only point estimates are produced.
- The 2PL is the primary anchor analysis because observed-score LR with a short anchor is biased (Section 2).

## 1. Main DIF table (matching = rest score of the other 10 items, weighted, no covariates)

| Item | Sp % | En % | Crude OR | Uniform-DIF OR [95% CI] | pp diff at matched score | ΔR² uniform (M1→M2) | ΔR² non-uniform (M2→M3) | Δβ1 | BH q uniform / non-uniform | JG (uniform) | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|
| HH mental illness (DEPRS) | 4.2 | 22.2 | 0.15 | **0.21 [0.15, 0.29]** | −10.6 | **0.052** | 0.000 | 6% | <1e-15 / 0.7 | B | **FLAG** |
| HH problem drinker (DRINK) | 16.8 | 25.5 | 0.59 | 1.06 [0.99, 1.12] | +0.6 | 0.000 | 0.001 | 1% | 0.10 / 0.03 | A | – |
| HH drug use (DRUGS) | 3.2 | 14.5 | 0.19 | **0.33 [0.24, 0.44]** | −4.7 | **0.021** | 0.000 | 5% | <1e-12 / 0.7 | A | **FLAG** |
| HH incarceration (PRISN) | 2.7 | 14.0 | 0.17 | **0.27 [0.19, 0.37]** | −5.8 | **0.031** | 0.000 | 7% | <1e-12 / 1.0 | A | **FLAG** |
| Parents sep./divorced (DIVRC) | 25.4 | 39.2 | 0.53 | 0.67 [0.54, 0.82] | −8.1 | 0.009 | 0.001 | 6% | 2e-4 / 2e-5 | A | – |
| Witnessed parental violence (PUNCH) | 17.1 | 23.1 | 0.69 | 1.42 [1.25, 1.61] | +3.7 | 0.004 | 0.002 | 4% | 2e-7 / 5e-5 | A | – |
| Physical abuse (HURT) | 30.2 | 34.1 | 0.84 | 1.50 [1.23, 1.83] | +6.9 | 0.007 | 0.005 | 6% | 1e-4 / 9e-10 | A | – |
| Verbal abuse (SWEAR) | 17.7 | 40.9 | 0.31 | **0.42 [0.31, 0.55]** | −12.3 | **0.024** | 0.003 | 3% | 7e-9 / 2e-6 | A | **FLAG** |
| Sexual: touched (TOUCH) | 6.8 | 13.9 | 0.45 | 1.06 [0.95, 1.19] | +0.3 | 0.000 | 0.008 | 0% | 0.34 / 3e-7 | A | – |
| Sexual: made to touch (TTHEM) | 6.0 | 10.7 | 0.53 | 1.34 [1.16, 1.53] | +1.2 | 0.002 | 0.005 | 2% | 6e-5 / 4e-8 | A | – |
| Sexual: forced sex (HVSEX) | 4.4 | 6.8 | 0.64 | 1.98 [1.56, 2.53] | +1.9 | 0.009 | 0.005 | 7% | 1e-7 / 2e-4 | A | – |

How to read the table:
- OR < 1 means Spanish-interview respondents are *less* likely to endorse the item than English-interview respondents with the same rest score.
- "pp diff" is the model-based average difference in endorsement probability (Spanish minus English) among Spanish respondents at their own rest score.
- Crude percentages are complete-case and use the year-normalized weights. They differ slightly from the earlier 18.4% vs 41.7% for verbal abuse, which used raw weights and all valid responses.
- Δβ1 never reached 10%, so every flag came from ΔR².
- Non-uniform DIF is negligible for every item (all ΔR² < .01), even though many q-values are tiny at this N.

**Robustness of the main result**

| Item | Covariate-adjusted OR [95% CI] | Covariate-adjusted ΔR² | Covariate flag | Unweighted OR | Purified OR [95% CI] (7-item matching) | Purified ΔR² (JG) | Purified flag |
|---|---|---|---|---|---|---|---|
| HH mental illness | 0.33 [0.24, 0.45] | 0.015 | – | 0.21 | 0.17 [0.12, 0.24] | 0.075 (C) | FLAG |
| HH problem drinker | 1.11 [0.94, 1.30] | 0.000 | – | 0.99 | 0.74 [0.68, 0.80] | 0.004 (A) | – |
| HH drug use | 0.34 [0.25, 0.46] | 0.012 | – | 0.37 | 0.24 [0.18, 0.31] | 0.043 (B) | FLAG |
| HH incarceration | 0.30 [0.21, 0.43] | 0.016 | – | 0.28 | 0.21 [0.15, 0.29] | 0.052 (B) | FLAG |
| Parents sep./divorced | 0.66 [0.53, 0.82] | 0.005 | – | 0.69 | 0.58 [0.46, 0.71] | 0.018 (A) | – |
| Witnessed parental violence | 1.17 [1.01, 1.36] | 0.000 | – | 1.41 | 0.96 [0.84, 1.09] | 0.000 (A) | – |
| Physical abuse | 1.40 [1.18, 1.67] | 0.003 | – | 1.53 | 1.12 [0.93, 1.35] | 0.001 (A) | – |
| Verbal abuse | 0.54 [0.42, 0.70] | 0.006 | – | 0.41 | 0.33 [0.25, 0.43] | 0.041 (B) | FLAG |
| Sexual: touched | 0.99 [0.86, 1.13] | 0.000 | – | 1.02 | 0.66 [0.58, 0.74] | 0.004 (A) | – |
| Sexual: made to touch | 1.33 [1.11, 1.60] | 0.001 | – | 1.20 | 0.85 [0.72, 0.99] | 0.001 (A) | – |
| Sexual: forced sex | 1.55 [1.14, 2.09] | 0.002 | – | 1.84 | 1.25 [1.01, 1.54] | 0.001 (A) | – |

- **Covariates.** With covariates *no* item passes the ΔR² ≥ .02 gate (the highest is DEPRS at .015), yet the ORs for the four items stay at 0.30–0.54. ΔR² falls because language is collinear with education, income and state, which are already in M1. Adjusting for covariates barely changes the *observed* gap: the 11-item count gap goes from −1.10 to −1.04, and the 4+ gap from −14.8 pp to −14.2 pp.
- **ACEDIVRC code 8.** Recoding code 8 as endorsed, or excluding those 676 respondents, changes no OR by more than 0.02 and no flag. Code 8 covers 1.5% of Spanish and 2.1% of English respondents; see `divrc8_sensitivity.csv`.
- **Weighting.** Unweighted results reach the same final purified set. The first iteration flagged 3 items; the second added DRUGS.

## 2. Purification and anchor sensitivity (the central point)

**Purification.** Iteration 1 flagged DEPRS, DRUGS, PRISN and SWEAR. Iteration 2 matched on the remaining 7 items (DRINK, DIVRC, PUNCH, HURT, TOUCH, TTHEM, HVSEX) and flagged the same 4, so the procedure converged. These 7 "anchors" passed the effect-size gate; they are *not* DIF-free relative to each other. Under purified matching, DIVRC has OR 0.58, TOUCH 0.66 and HVSEX 1.25, all with tiny q-values.

**Anchor sensitivity: 2PL with anchor constraints (primary).** Each cell is the DIF OR at equal latent ACE level. Bold marks OR < 0.67 or > 1.5; *anchor* marks items constrained to be equal across groups.

| Item | A1 purified 7 | A2 drinker only | A3 drink + divorce + sexual | A4 household 5 | X1 HURT+PUNCH (extreme) | X2 SWEAR+DEPRS (extreme) |
|---|---|---|---|---|---|---|
| HH mental illness | **0.17** | **0.20** | **0.19** | *anchor* | **0.14** | *anchor* |
| HH problem drinker | *anchor* | *anchor* | *anchor* | *anchor* | 0.71 | **2.67** |
| HH drug use | **0.24** | **0.28** | **0.27** | *anchor* | **0.19** | 0.91 |
| HH incarceration | **0.22** | **0.24** | **0.24** | *anchor* | **0.18** | **0.61** |
| Parents sep./divorced | *anchor* | 0.67 | *anchor* | *anchor* | **0.58** | 1.02 |
| Witnessed parental violence | *anchor* | 1.30 | 1.32 | **3.63** | *anchor* | **3.97** |
| Physical abuse | *anchor* | **1.58** | **1.65** | **3.78** | *anchor* | **4.06** |
| Verbal abuse | **0.33** | **0.39** | **0.40** | 1.23 | **0.25** | *anchor* |
| Sexual: touched | *anchor* | 0.95 | *anchor* | **8.27** | **0.45** | **9.22** |
| Sexual: made to touch | *anchor* | 1.31 | *anchor* | **11.87** | **0.61** | **13.08** |
| Sexual: forced sex | *anchor* | **1.91** | *anchor* | **16.82** | 0.90 | **18.64** |
| *Spanish latent mean (English SD units)* | −0.38 | −0.46 | −0.52 | **−1.00** | −0.23 | **−1.06** |

For reference, the model that treats all 11 items as invariant gives a Spanish latent mean of −0.65 SD.

**Observed-score LR under the same anchor sets (secondary).** Matching is the sum of the anchor items, excluding the studied item. Values in parentheses are anchor items tested against the other anchors. † marks a flagged item.

| Item | A0 all-other | A1 purified 7 | A2 drinker only | A3 drink + div + sex | A4 household 5 | X1 HURT+PUNCH | X2 SWEAR+DEPRS |
|---|---|---|---|---|---|---|---|
| HH mental illness | 0.21† | 0.17† | 0.16† | 0.18† | (0.22)† | 0.15† | (0.22)† |
| HH problem drinker | 1.06 | (0.74) | n/a | (0.70) | (1.03) | 0.63 | 1.06 |
| HH drug use | 0.33† | 0.24† | 0.22† | 0.24† | (0.44) | 0.20† | 0.40 |
| HH incarceration | 0.27† | 0.21† | 0.19† | 0.21† | (0.34) | 0.18† | 0.29† |
| Parents sep./divorced | 0.67 | (0.58) | 0.56† | (0.57) | (0.68) | 0.55† | 0.68† |
| Witnessed parental violence | 1.42 | (0.96) | 0.81 | 0.92 | 1.25 | (0.71) | 1.39 |
| Physical abuse | 1.50 | (1.12) | 0.94 | 1.06 | 1.23 | (0.94) | 1.60 |
| Verbal abuse | 0.42† | 0.33† | 0.32† | 0.36† | 0.46† | 0.25† | (0.42)† |
| Sexual: touched | 1.06 | (0.66) | 0.51 | (0.72) | 0.80 | 0.49 | 0.89 |
| Sexual: made to touch | 1.34 | (0.85) | 0.60 | (0.98) | 0.92 | 0.58 | 1.05 |
| Sexual: forced sex | 1.98 | (1.25) | 0.75 | (1.53) | 1.21 | 0.72 | 1.39 |

**What the two tables show**

1. **Four items behave consistently.** DEPRS, DRUGS, PRISN and SWEAR have OR ≈ 0.14–0.40 under every anchor set that does not include them as anchors, in both LR and 2PL. With the 7-item purified anchor, LR and 2PL agree almost exactly (0.17/0.17, 0.24/0.24, 0.21/0.22, 0.33/0.33).
2. **The sign for the other items depends on the anchor.**
   - Physical abuse, parental violence and the sexual items look roughly invariant, or mildly *over*-endorsed in Spanish (OR 1.3–1.9), when the anchors come from the "small-gap" cluster.
   - They look strongly over-endorsed (OR 3.6–18.6) when the anchors are the household items or SWEAR+DEPRS. In that case the anchors imply a Spanish latent deficit of about 1.0 SD instead of 0.4–0.5 SD.
   - Equally, if HURT+PUNCH are taken as invariant, every other item looks under-reported, including drinking (0.71) and sexual touching (0.45).
   - The items therefore fall into two clusters with different language gaps: {DEPRS, DRUGS, PRISN, SWEAR} and {DRINK, DIVRC, PUNCH, HURT, sexual items}. The data cannot say which cluster carries the bias. All single-anchor 2PL models fit identically by construction, and the multi-anchor sets differ only in how consistent their anchors are with *each other* (log-likelihoods are in `irt2pl_anchor_schemes.csv`).
3. **Why the 2PL is primary.** With a short anchor (1–2 items), observed-score LR leaves much of the latent-mean difference unmatched. The estimates are then pulled toward the crude Spanish-lower gap.
   - With the drinker-only anchor, LR gives OR 0.51 for sexual touching; the 2PL gives 0.95.
   - With the household anchors, LR gives about 1.2 for physical abuse; the 2PL gives 3.8.
   - The LR anchor columns other than A0 and A1 should not be shown on their own.

## 3. Impact on the headline language gap

Observed (weighted): mean 11-item ACE count 1.34 for Spanish vs 2.45 for English, a gap of −1.10. On the 8-category score, 4+ ACE prevalence is **10.7% vs 25.5% (−14.8 pp; ratio 0.42)**.

| Scenario | Spanish mean count (11 items) | Gap vs English (% of observed) | Spanish ACE8 4+ % | 4+ gap, pp (% of observed) |
|---|---|---|---|---|
| Observed | 1.34 | −1.10 (100%) | 10.7 | −14.8 (100%) |
| Covariate-adjusted regression gap | – | −1.04 (94%) | – | −14.2 (96%) |
| **Drop the 4 purified-flagged items** (7-item score) | 1.07 vs 1.53 | standardized gap −0.30 SD vs −0.47 SD for the 11-item count (62% retained) | – | – |
| LR-corrected, purified anchors (flagged items moved to the English curve) | 1.79 | −0.65 (59%) | 15.8 | −9.7 (66%) |
| 2PL-corrected, A1 purified 7 | 1.71 | −0.74 (67%) | 15.8 | −9.7 (66%) |
| 2PL-corrected, A2 drinker only | 1.63 | −0.82 (74%) | 14.4 | −11.1 (75%) |
| 2PL-corrected, A3 drink + divorce + sexual | 1.56 | −0.89 (81%) | 13.8 | −11.7 (79%) |
| 2PL-corrected, A4 household 5 | 0.94 | −1.51 (137%) | 5.9 | −19.5 (132%) |
| 2PL-corrected, X1 HURT+PUNCH (extreme) | 2.00 | −0.45 (41%) | 19.3 | −6.1 (42%) |
| 2PL-corrected, X2 SWEAR+DEPRS (extreme) | 0.88 | −1.57 (142%) | 5.4 | −20.1 (136%) |

How the corrections were done:
- **LR correction.** For each item being corrected, Spanish respondents' answers are stochastically re-drawn (M = 50) so that E[y | S] equals the English curve. The ACE8 score is then recomputed.
- **2PL correction.** Observed value + (model-implied Spanish value under English item parameters − model-implied value under Spanish parameters), using Spanish latent draws.
- There are no CIs on the impact rows.
- **What it means.** Under the purified or a-priori anchors (A1–A3), item-specific DIF accounts for about 20–35% of the 4+ gap, and a gap of 10–12 pp remains. Under household anchors the "true" gap would be *larger* than observed. The headline gap is therefore only bounded, between about 6 and 20 pp, until the anchor assumption is defended.

## 4. Version split (Spanish wording: 2019 ≠ 2020 on ACEPUNCH; 2021–2025 unpublished)

Each cell is the uniform-DIF OR (weighted, no covariates). The ratio columns are OR(2020)/OR(2019) from the pooled 2019–2020 interaction model (item ~ S + Sp + Y2020 + Sp×Y2020 + S×Y2020), with p and the covariate-adjusted version.

| Item | All-other: 2019 | 2020 | 2021–25 | All-other: 2020/2019 ratio (p); cov-adj (p) | Purified: 2019 | 2020 | 2021–25 | Purified: 2020/2019 ratio (p); cov-adj (p) |
|---|---|---|---|---|---|---|---|---|
| HH mental illness | 0.37 | 0.18 | 0.19 | 0.49 (0.18); 0.49 (0.11) | 0.29 | 0.15 | 0.15 | 0.52 (0.24); 0.50 (0.15) |
| HH problem drinker | 0.91 | 1.03 | 1.12 | 1.13 (0.14); 1.03 (0.72) | 0.64 | 0.79 | 0.74 | 1.23 (0.07); 1.08 (0.50) |
| HH drug use | 0.33 | 0.30 | 0.35 | 0.91 (0.86); 0.86 (0.81) | 0.25 | 0.23 | 0.24 | 0.93 (0.90); 0.89 (0.84) |
| HH incarceration | 0.30 | 0.20 | 0.31 | 0.66 (0.41); 0.65 (0.36) | 0.24 | 0.16 | 0.22 | 0.67 (0.47); 0.65 (0.40) |
| Parents sep./divorced | 0.68 | 0.49 | 0.78 | 0.72 (0.11); 0.83 (0.34) | 0.59 | 0.42 | 0.68 | 0.71 (0.09); 0.81 (0.28) |
| **Witnessed parental violence** | **2.00** | **1.40** | **1.26** | **0.70 (0.02); 0.64 (0.005)** | **1.35** | **1.02** | **0.82** | **0.76 (0.08); 0.68 (0.03)** |
| Physical abuse | 1.10 | 1.99 | 1.40 | 1.81 (0.13); 1.75 (0.15) | 0.84 | 1.49 | 1.04 | 1.76 (0.10); 1.68 (0.13) |
| Verbal abuse | 0.38 | 0.62 | 0.32 | 1.62 (0.03); 1.49 (0.09) | 0.31 | 0.48 | 0.25 | 1.54 (0.02); 1.42 (0.08) |
| Sexual: touched | 1.00 | 1.11 | 1.06 | 1.12 (0.50); 0.96 (0.80) | 0.64 | 0.73 | 0.62 | 1.14 (0.43); 0.95 (0.73) |
| Sexual: made to touch | 1.39 | 1.55 | 1.21 | 1.11 (0.60); 0.96 (0.83) | 0.93 | 1.06 | 0.71 | 1.14 (0.54); 0.97 (0.87) |
| Sexual: forced sex | 2.33 | 1.44 | 2.28 | 0.62 (0.10); 0.55 (0.009) | 1.53 | 1.02 | 1.31 | 0.66 (0.12); 0.58 (0.01) |

- **ACEPUNCH.** Relative Spanish endorsement fell from 2019 to 2020 in every specification: the ratio is 0.64–0.76, with p from .005 to .08. Unpurified ORs were 2.00 [1.61, 2.47] in 2019, 1.40 [1.13, 1.74] in 2020 and 1.26 in 2021–25. This is the direction expected if the 2019 verb list, which included "azotaban" (whipped), made the item easier to endorse.
- **But the shift is not specific to ACEPUNCH.** Items whose Spanish wording did not change moved as much or more: SWEAR ×1.4–1.6, HVSEX ×0.55–0.66, HURT ×1.7–1.8 (not significant).
- **Common-state check.** Restricting to the 5 states with ≥ 30 Spanish respondents in both years (FL, IA, OK, RI, VA; 1,861 Spanish respondents) gives ACEPUNCH ×0.64–0.67, but also HURT ×1.8–2.0, DEPRS ×0.4 and TTHEM ×1.8–2.1. With only 10 clusters, those p-values are not trustworthy; see `version_2019_vs_2020_common_states.csv`.
- **Conclusion.** Item-level language DIF moves around between years and state mixes (2020 was also the COVID year, and TX enters the sample only that year). The ACEPUNCH change is suggestive but **cannot be attributed to the wording change**.
- The four flagged items show the same direction in all three periods.

## Takeaways

1. **Four items stand out: household mental illness, household drug use, household incarceration and verbal abuse.** Spanish-interview Hispanics endorse them at roughly 0.2–0.4 times the odds expected from their answers to the other items, which is 5–12 percentage points lower at a matched level. This holds:
   - with and without weights
   - after purification
   - under either ACEDIVRC coding
   - in every wording period
   - under every anchor set that does not include these items, in both LR and 2PL
   - with covariates, where the ORs are 0.30–0.54

   Non-uniform DIF is negligible.
2. **Which items are biased is not identified.** The items form two clusters with different language gaps. Taking the small-gap cluster as anchors means Spanish respondents under-report the four items, and the latent deficit is about 0.4–0.5 SD. Taking the household items as anchors means Spanish respondents over-report physical abuse, parental violence and sexual abuse by ORs of 4–19, and the deficit is about 1.0 SD. Internal data cannot choose between these. The four items' wording (for example "humillaba") and stigma make the first reading more plausible on substantive grounds, but that is a judgment, not a result.
3. **The headline gap depends on the anchor.** After DIF correction, Spanish 4+ prevalence ranges from 5.4% to 19.3% (observed 10.7%; English 25.5%). Under the purified or a-priori wording-based anchors it is 13.8–15.8%. On that reading about 20–35% of the 4+ gap is item-specific, and a gap of 10–12 pp remains.
4. **Whether an item gets flagged depends on the convention used.** Without covariates, ΔR² flags four items (JG: one moderate, three negligible; purified: one large, three moderate). With covariates nothing is flagged, even though the ORs barely move, and Δβ1 never reaches 10%. Lead with ORs, pp differences and impact, not flags.
5. **No wording signal is identifiable.** The 2019→2020 fall in ACEPUNCH DIF goes the way the wording change predicts, but items with unchanged wording shifted as much.

## Caveats

- **Identification.** DIF here is relative only. A uniform under-reporting of all items in Spanish is undetectable and is absorbed into the latent mean. Every number in Sections 2–3 is conditional on an anchor assumption.
- **No nativity variable.** "Language DIF" here bundles translation with who chooses a Spanish interview (nativity, upbringing abroad, acculturation, Hispanic subgroup). Lower household incarceration and drug exposure among people raised outside the US would be a *real* domain-specific difference. A unidimensional model would still flag it as DIF. The flagged items are exactly the ones where such real differences are plausible, so they are not proof of measurement bias.
- **Model.** The 2PL is unidimensional, but the ACE items are multidimensional (three factors). A Spanish shortfall on one dimension specifically, such as household dysfunction, would show up as DIF. The 2PL also models uniform DIF only, with common slopes, and gives no SEs.
- **Survey design.** SEs are approximate: sandwich estimates with state-year clusters, normalized pooled weights (main and version weights mixed), and no strata. The impact rows have no CIs. BH correction is applied within each analysis, not across the many sensitivity runs.
- **Sample.** Complete cases only. DK/refusal and module break-off may differ by language and are not modeled.
- **Covariates.** They may be proxies for, or mediators of, language. Covariate-adjusted DIF is a different estimand, not a "better" one.
- **Spanish wording.** The 2021–2025 Spanish text (57% of the Spanish sample) is unpublished. Texas contributes Spanish respondents only in 2020 (900, or 30% of that year's Spanish sample), and the state mix varies by year.
- **Effect-size cutoffs.** The JG cutoffs are unverified. Nagelkerke ΔR² tends to be small for low-prevalence items, which disadvantages the sexual-abuse, drug and incarceration items.

## Files

- Scripts in `/home/mo2273/ace_tonight_scripts/dif/`:
  - `build_dif_data.py`: rebuilds the analytic file with sex, income, `_STSTR`, `_PSU` and SEQNO, using the dedup logic from `analyze_ace_language.py`
  - `run_dif.py`: sections 1–3
  - `run_dif_part2.py`: version split and ACEDIVRC sensitivity
  - `version_common_states.py`
  - `irt_anchor_check.py`: 2PL
  - `make_tables.py`
- Outputs in `/home/mo2273/ace_tonight/dif/`:
  - `dif_analytic_hisp_2019_2025.csv`: analytic sample
  - `dif_all_results.csv`: every LR fit, with ORs, CIs, ΔR², Δβ1, q-values, JG categories and flags, for weighted/unweighted and with/without covariates
  - `purification_history.csv`
  - `irt2pl_anchor_items.csv`, `irt2pl_anchor_schemes.csv`
  - `impact.csv`
  - `version_split.csv`, `version_2019_vs_2020_interaction.csv`, `version_2019_vs_2020_common_states.csv`
  - `divrc8_sensitivity.csv`
  - `tables_for_results.md`
