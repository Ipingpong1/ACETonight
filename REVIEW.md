# Adversarial review: interview-language DIF of ACE items (BRFSS + CHIS)

*Reviewer stance: a hostile methodologist who is also a prospective PI deciding whether to supervise this. Date: 2 November 2026. Scope: everything under `ace_tonight/`, `ace_manuscript/` and `research_notes/`. I read every script and results file, re-derived the headline counts from the output CSVs, and verified the frozen-plan hash. I did not refit the lavaan models.*

## 1. Bottom line

The project is in far better shape than a two-day project has any right to be: two surveys, a locked specification, replicate-weight variance, seven pre-specified sensitivity analyses, an honest deviations log and a reference list checked against Crossref. The weakness is not rigour; it is that the draft's *framing* (title, hypothesis, "H1 supported", impact figures) carries a broader claim than the evidence supports, while the evidence that supports the narrower claim is partly missing from the draft.

**What survives every test in the repository:** relative to the other ACE items, Hispanic adults interviewed in Spanish under-endorse the *household mental illness* item. This holds in BRFSS and CHIS (independent Spanish translations), after nativity adjustment and among the foreign-born (CHIS), by phone and by web, in an anchor-free alignment analysis in both surveys, and (exploratory) in NSCH parent reports with no interviewer and a different informant.

**What does not survive:** the "three stigmatized household items" story. Drug use and incarceration lose significance after nativity adjustment and vanish among the foreign-born. In BRFSS all three target effects shrink to non-significance under purified anchors, because the two household anchors (problem drinking, separation/divorce) disagree with each other in sign.

**Recommendation:** lead with mental illness; present drug use and incarceration as nativity-related; present the anchor problem as the central methodological point rather than as a limitation; add the NSCH and own-mental-health triangulation; drop the "supported/not supported" vocabulary from the abstract. The preprint in `preprint/` does all of this. The underlying analyses do not need to be rerun to show the work to PIs.

## 2. What is genuinely strong

- **Design.** Two surveys with the same English items, different Spanish translations, different modes (CATI vs mostly web), one with nativity. This is the right design for separating translation from everything else, and it is novel (see `notes/01`, `notes/05`: 55 logged searches, nothing comparable found).
- **Transparency.** The plan was frozen and hashed before the MIMIC models were fitted; every deviation is logged with a reason; the first wrong S3 run is marked superseded rather than deleted; the exploratory origin of H1 is disclosed in the plan itself.
- **Variance.** Replicate-weight SEs (CHIS jackknife; BRFSS Rao–Wu bootstrap) for the primary estimates, with the singleton-stratum workaround documented and checked against Taylor SEs.
- **Sensitivity breadth.** One-factor, purified anchors, one-at-a-time, alignment, MGCFA with score tests, 11-item model, mode interaction, impact simulation. Few published invariance papers in this literature do half of this (Mei 2022 did none of it).
- **Honesty of the interpretive note** in `DEVIATIONS.md` §C: the plan said anchor bias could only be conservative; the data showed otherwise; the note says so plainly.

## 3. Issues, ranked by how much they damage the claim

### 3.1 The anchor assumption *is* the result, and the draft buries it (HIGH)

Every DIF estimate here is relative to the anchor items. In the primary MIMIC the household factor's language effect is identified by problem drinking and separation/divorce. S4c shows these two anchors disagree: in BRFSS, problem drinking is *over*-endorsed in Spanish relative to the factor (b = +0.61, OR-eq 2.80) and divorce is under-endorsed (b = −0.26, OR-eq 0.65). The primary target estimates are therefore an average of "relative to drinking" and "relative to divorce". Purification (S4b) frees verbal abuse, drinking and witnessed violence, leaves divorce as the only household anchor, and the BRFSS target effects fall to b = −0.14 to −0.22 (p ≥ .11).

The exploratory 2PL in `exploratory/dif/RESULTS.md` §2 shows the same structure from another angle: the 11 items form two clusters with different language gaps, {mental illness, drugs, incarceration, verbal abuse} and {drinking, divorce, witnessed violence, physical abuse, sexual items}, and **the data cannot say which cluster carries the bias.** Taking the second cluster as anchors gives a latent deficit of 0.4–0.5 SD and large negative DIF on the first; taking household items as anchors gives a deficit of 1.0 SD and ORs of 4–19 on the abuse items.

*What a PI will say:* "Your headline odds ratio is whatever your anchor says it is. Why these anchors?"

*What the draft does:* acknowledges it in Results and Limitations, but the title, H1, abstract and Figure 1 all present the primary estimates as the finding.

*What the preprint does:* adds a "How to read a DIF estimate" box in Methods; reports the primary, purified and alignment estimates side by side in Results; uses "non-equivalence relative to the other items" throughout; states in the abstract that BRFSS effects are anchor-dependent.

### 3.2 "H1 SUPPORTED" reads as confirmatory; it is not (HIGH for credibility)

Timeline from `STATUS.md` and the hash file: plan frozen 06:38 UTC on 2 Nov; first model fitted 06:48 UTC; all of 1 Nov spent on exploratory logistic and 2PL DIF of the same data, which showed the same four items. The secondary-data preregistration template the draft cites (van den Akker 2021) says explicitly that with direct knowledge of the hypothesized association one should not call the analysis confirmatory. The draft's Methods say this honestly, but the Results header, the Holm-adjusted decision rule and the word "supported" in the Discussion give the opposite impression. A sceptical PI will see confirmatory theatre.

Second problem: a SHA-256 hash proves nothing until the hashed document is public somewhere with an independent timestamp. Until the OSF registration exists, the GitHub commit of `prereg/` is the only external timestamp. That is one reason this repository matters.

*What the preprint does:* keeps the locked specification as a transparency device ("pre-specified analyses of the discovery data"); reports that the criterion was met in one sentence and moves on; removes "supported/not supported" from the abstract and discussion; states the timeline in the pre-specification paragraph.

### 3.3 "Language DIF" is interview-language-*group* DIF (HIGH for interpretation; irreducible in BRFSS)

Interview language bundles nativity, country of childhood, acculturation, education, income and interviewer pool. BRFSS has no nativity variable. CHIS does, and S1/S2 are the right analyses, but "foreign-born" and "percent of life in the US" are coarse: they do not capture *where* the childhood household was. Lower (recognized, diagnosed) mental illness in households in Mexico or Central America, relative to the other adversities those households had, would appear as DIF in every model here. Alegría 2008 shows real immigrant-paradox differences in psychiatric morbidity.

*What a PI will say:* "You have shown non-equivalence, not reporting bias."

*What the preprint does:* names the exposure as interview-language group; presents two readings (differential labelling/disclosure vs real conditional differences) with the evidence for each; argues that for surveillance the distinction does not matter (the item is not comparable either way), while for mechanism it does.

### 3.4 The strongest triangulating evidence was left out of the draft (MEDIUM; easy win)

`ace_tonight/` contains three results that answer the two most obvious objections and none of them is in `manuscript_draft.md`:

1. **NSCH 2022–2024** (self-administered web/paper; parent report about the child; household language; 24,351 Hispanic children): "lived with anyone mentally ill, suicidal or severely depressed" 2.9% vs 9.6%, aOR 0.32 (0.21–0.49), stable across years, 0.34 within 1st/2nd-generation households; incarceration 0.33, alcohol/drugs 0.47, divorce 0.73; mental illness vs alcohol/drugs ratio of ORs 0.68 (0.52–0.89). The responding parent's *own* mental health fair/poor: aOR 0.39, versus physical health fair/poor on the identical scale: 0.69 (ratio 0.56, 0.47–0.67). No mental-health-specific item skipping.
2. **BRFSS own mental health:** the ACEDEPRS gap (aOR 0.20) is larger than the gap in the respondent's own depression diagnosis (0.33) or frequent mental distress (0.51); ratio of aORs 0.59 and 0.37; conditioning on own depression/distress moves the ACEDEPRS aOR only to 0.25.
3. **No differential prediction:** ACE scores and the mental-illness item predict depression (BRFSS) and serious distress (CHIS) with the same slopes in both languages (interaction p ≥ .25).

(1) answers "it is interviewer social desirability" and "it is an anchor artifact of the adult retrospective items" (different informant, no interviewer, no anchors needed for the marginal contrast, and a within-respondent physical-health control). (2) shows the household item gap is not simply the broader mental-health reporting gap. (3) shows endorsed items carry the same meaning.

These are exploratory, with approximate SEs, and NSCH language is household language, not instrument language. They belong in a clearly labelled triangulation subsection and the supplement, not in the primary results.

*What the preprint does:* adds §3.7 and Supplement S7.

### 3.5 Three different odds ratios for the same item across the project (MEDIUM; legibility)

For household mental illness in BRFSS a reader of the repository will find: crude OR 0.17; rest-score logistic DIF OR 0.21; 2PL purified anchors 0.17; MIMIC primary OR-equivalent 0.35; MIMIC purified 0.68; covariate-adjusted logistic DIF 0.33. They are different estimands (conditional on an observed rest score vs a latent factor; one vs two factors; with vs without covariates; different anchors; probit-to-logit approximation), but nothing in the draft says so. Likewise five Spanish prevalences for the same item (4.0, 4.2, 4.4, 4.7, 5.1%) appear across documents, because of different weight normalisations and samples.

*What the preprint does:* one paragraph in Supplement S7.1 reconciling the estimands; one prevalence (4.0%, weights ÷ 7) used throughout with a footnote.

### 3.6 The impact figures inherit the primary anchors (MEDIUM)

"Removing the DIF would close 10–18% of the gap" is conditional on drinking and divorce being invariant. Under purified BRFSS anchors the target effects are ~0.2 probit, so the BRFSS impact would be roughly half or less. The draft says "upper-range estimate" in Results but the abstract states 10–18% without qualification.

*What the preprint does:* "at most 10–18%" in the abstract; the conditionality stated where the numbers appear.

### 3.7 Complete-case BRFSS sample; item nonresponse by language not modelled (LOW–MEDIUM)

The BRFSS analytic sample requires valid answers on all 11 items, dropping 9% of Spanish and 11% of English ACE respondents. Nonresponse is known to rise through the module and could differ by language. Two reassurances exist but are not in the draft: the per-item analysis in `exploratory/brfss_mh/` (all valid responses, not complete cases) gives ACEDEPRS aOR 0.20, identical to the complete-case figure; and NSCH shows Spanish households skip every item about 2 points more often, with no item-specific pattern.

*What the preprint does:* states both in Limitations.

### 3.8 CHIS imputes item nonresponse (LOW–MEDIUM; direction unknown)

CHIS public-use items have no missing values. If the imputation model excluded interview language, imputed values dilute DIF toward zero; if it included language and nativity, the imputation could in principle manufacture a group difference. The draft lists imputation as a limitation but not this mechanism. Worth one email to UCLA CHPR or a check of the methodology report (imputation rates for AQ1–AQ8 by language).

### 3.9 Spanish wording instability in BRFSS (MEDIUM; irreducible)

The 2021–2025 CDC Spanish text is unpublished (57% of the Spanish sample); 2019 ≠ 2020 wording on the witnessed-violence item; states may adapt wording. The exploratory version split (`exploratory/dif/RESULTS.md` §4) shows the witnessed-violence DIF fell from 2019 to 2020 as the wording change predicts, but items with unchanged wording moved as much. The draft handles this correctly. A PI from survey methodology will want the actual Spanish text of both surveys' mental-illness item in the paper; it is not there. (CDC 2011 module: "¿Vivió con alguien que estaba deprimido, enfermo mental o suicida?" should be verified against the PDF before being quoted; CHIS wording not retrieved.)

### 3.10 The "stigmatized household conditions" grouping is post hoc (LOW; framing)

`exploratory/master/MASTER_SUMMARY.md` says so: "a grouping suggested by the results, not decided in advance." The plan then pre-specifies it. Fine, but say "a grouping suggested by exploratory results and then pre-specified", and note that verbal abuse, which is not a household item, shows DIF as large as the targets (BRFSS 0.31, CHIS 0.45), which the stigma story does not predict (the "humilló" translation does).

### 3.11 The mode result for incarceration cuts against the disclosure story (LOW)

Incarceration DIF is larger on the *web* (0.31) than by phone (0.78; p = .009). Interviewer presence should increase, not reduce, under-reporting of a stigmatised item. Either chance (one of three interaction tests) or evidence that whatever drives the incarceration gap is not disclosure. Say which.

### 3.12 Presentational problems (fixed in the preprint)

- Figure numbering: draft Figure 1 = file `fig2`, draft Figure 2 = file `fig3`; files `fig1`, `fig4` were "eFigures". The preprint uses the file order (Figures 1–4).
- Placeholders: author list, IRB determination, OSF link, repository. Author list remains the one thing I cannot fill.
- The draft's "Author notes" section (venues, open items) does not belong in a circulated preprint; moved to this review and the README.
- Figure PNGs carry headline titles; captions in the draft repeat them. Kept the headlines (useful for PIs skimming) and made captions technical.

### 3.13 Reference list provenance (LOW, but check before posting)

The 46 references were assembled with automated help and checked against Crossref/PubMed (`notes/06`). Three are weaker: Umoga 2026 (dissertation, abstract only, embargoed to April 2027); CDC 2019 prevention document (cited via Swedo 2023, not opened); the AJPM-style "CDC 2024 BRFSS overview" (PDF, fine). I added three references in the preprint: Alegría 2008 (verified in `notes/06` as R20), Choi, Gibbons & Crane 2011 (lordif; verified in `notes/02`), and a Census NSCH data citation (URL). Before medRxiv, spot-check five references by hand, including page ranges.

## 4. Checks performed

| Check | Result |
|---|---|
| SHA-256 of `prereg/H1_analysis_plan.md` vs recorded hash | Match (`031cd720…420fa`) |
| "Mental-illness DIF significant in 10 of 11 specifications; drug use and incarceration 7 of 11" | Reproduced from `s4_effects.csv`, `s6_mode.csv`, `s7_effects.csv`, `effects_s1/s2.csv`, `primary_results.csv` (b < 0 and p < .05): mh 10/11, drugs 7/11, jail 7/11 |
| Abstract numbers vs `primary_results.csv` / `H1_verdict.json` | All match (OR-eq 0.35/0.31/0.33 BRFSS; 0.59/0.64/0.43 CHIS; S1 mh 0.67 [0.55–0.82]; S2 0.69 [0.54–0.88]) |
| Table 1 collapsed rows (65+, ≤8th grade, low income, foreign-born, English proficiency) vs full Table 1 | All sums match |
| S3 Δχ², ΔCFI, latent means; S4d alignment shifts; S5 percentages; S6 mode ORs | Match `RESULTS.md` |
| Sample sizes across `ace_tonight`, plan, `01_prep_log.txt`, manuscript | 10,945/24,473 and 5,536/24,418 everywhere |
| CHIS sexual-abuse derivation (ACE8 minus 7 known categories) | No impossible values (0: 20,039; 1: 3,718; unknown for 6,197 with 4+ other ACEs), per `exploratory/chis/out/log.txt` |
| BRFSS version-file dedup and weight handling | Read `build_dif_data.py`, `mhcommon.py`, `01_prep.R`; consistent; version weights share the state-population scale |
| Microdata in the repository | None (CHIS PUF, BRFSS extracts, analytic files and `.rds` fits excluded) |

## 5. Code review notes (no conclusion-changing bugs found)

- `scripts/exploratory/dif/run_dif.py`: cluster-robust sandwich with G/(G−1)·(N−1)/(N−K) correction, state×year clusters; Nagelkerke R² from weighted log-likelihoods; BH across 22 tests per analysis. Correct as described. The JG cutoffs are labelled unverified; keep that label.
- `scripts/exploratory/dif/irt_anchor_check.py`: two-group 2PL by weighted MML with 41-point Gauss–Hermite quadrature; analytic gradients (checked the μ and log-σ terms); point estimates only. Fine for a sensitivity display; should never be reported with CIs.
- `scripts/exploratory/master/master.py` normalises BRFSS weights within year×file; `run_dif.py` within year. Both defensible; the manuscript stage uses weight ÷ 7 instead. This is the source of the 4.0/4.7% discrepancy. Pick one convention per document.
- `scripts/manuscript/common.R`: `std.lv = TRUE` with endogenous factors fixes factor *residual* variances to 1, as `DEVIATIONS.md` §B5 states; `implied_pdiff` uses Φ((λη̂ + b − τ)/√(λ²ψ + θ)) with θ = 1 under theta parameterisation; correct.
- `05_secondary.R` S3: explicit equality labels because `group.equal = "thresholds"` was not applied; df checked (38/50/44). Good catch, correctly documented.
- `05_secondary.R` S4b: with a single anchor per factor the language→factor effect is just-identified; estimates are "relative to divorce" (BRFSS) and should be described that way.
- `06_s5_impact.R`: common random numbers across scenarios and replicates; 50 draws per respondent; CIs from replicate coefficient sets. Fine. The reported "observed" vs "model-implied" agreement (−0.95 vs −0.94) is a useful calibration check and should be in the supplement (it is).
- `scripts/exploratory/nsch_chis/nsch_analysis.py`: strata ignored, state as cluster (51 clusters), Rubin's rules over six FPL implicates, joint cluster sandwich for item contrasts. Conservative; fine for exploratory. The 2-pp higher item nonresponse in Spanish households is in `nsch_item_nonresponse.csv`.
- `scripts/exploratory/brfss_mh/analyze_mh.py`: statsmodels cluster SE reproduced by a manual sandwich (0.12911); stacked models for ratios of ORs. Fine.
- Absolute paths (`/home/mo2273/...`) are hard-coded in the R scripts; the README says so. Not a correctness issue.

## 6. What the preprint changes relative to `preprint/archive/manuscript_draft_2026-11-02.md`

1. Adds a Key Points box and a "What this study adds / does not claim" box.
2. Restructures the abstract and Discussion around the mental-illness finding; drug use and incarceration presented as nativity-related; "supported" vocabulary removed.
3. Adds a "How to read a DIF estimate" box and an explicit two-cluster description of the anchor problem.
4. Adds §3.7 "Exploratory triangulation" (NSCH; BRFSS own mental health; differential prediction) and Supplement S7 with the tables.
5. Renumbers figures to match the files (1 prevalence, 2 DIF, 3 robustness, 4 impact).
6. Adds "Directions for future work" with concrete, cheap next studies (the PI hook).
7. Resolves placeholders: repository URL, pre-specification timeline, OSF pending, ethics wording; author list left as a flagged placeholder.
8. Adds a Supplement with the full tables (S1–S7), deviations, exploratory results, estimand reconciliation and the literature-search summary.
9. Three references added (see §3.13).

## 7. Before showing PIs / before posting to medRxiv

- [ ] **Author line.** Fill in name(s), affiliation(s), ORCID.
- [ ] Push this repository to GitHub (the first commit is the external timestamp) and paste the URL into `preprint.md` §Declarations.
- [ ] Register `prereg/H1_analysis_plan.md` on OSF under embargo with the secondary-data template, disclosing the 1 November exploratory work; paste the registration DOI.
- [ ] Verify the Spanish wording of the mental-illness item in the CDC module PDF and in the CHIS Spanish questionnaire, and quote both in Methods.
- [ ] Ask UCLA CHPR how AQ1–AQ8 item nonresponse was imputed and whether language entered the model.
- [ ] Spot-check five references by hand; read Zhang & Lippert 2026 through NYU Libraries; email Umoga's advisor about any language analysis.
- [ ] Decide a licence (CC BY 4.0 for text; MIT for code is conventional) and add `LICENSE`.
- [ ] Optional but valuable: hold out NSCH 2025 (already released) or CHIS 2026 as a genuinely confirmatory test of the locked specification.

## 8. How to pitch it to a PI

This is a survey-methods and measurement paper, not a prevalence paper. The pitch in three sentences: *Nobody has tested whether the ACE items work the same way in Spanish, even though a third to a half of Hispanic BRFSS respondents answer them in Spanish. In two surveys with independent translations, plus a third with a different informant, the household mental-illness item is the one item that is consistently under-endorsed relative to the others, after nativity, in both modes and without anchors. The next step is cheap and concrete: cognitive interviews and a split-ballot test of the Spanish item, and a held-out confirmatory test in NSCH 2025 or CHIS 2026.*
