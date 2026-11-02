# BRFSS feasibility: ACE item functioning by interview language (Spanish vs English): verified counts, coverage, covariates, and Spanish wording

All counts below were computed from the CDC BRFSS public-use SAS transport (XPT) files, downloaded 2026-11-01 for 2009–2025. I processed the main annual files plus the questionnaire-version files (V1/V2/V3), which hold module data for states that asked ACE on only one questionnaire version. "N" means **unweighted** respondent counts. "wt%" means weighted with each respondent's applicable final weight: `_FINALWT` for 2009–2010, `_LLCPWT` for the main file 2011+, `_LCPWTV1–3` for version files 2012+, and `_LNDWTV1–2` for the 2011 landline version files. All weighted figures are crude, descriptive and unadjusted, and they pool weights that were not designed to be pooled.

**Code and outputs (all reproducible):**
- Scripts are in `/home/mo2273/ace_brfss_scripts/`:
  - `download.sh`: downloads each zip into its own empty directory under `/home/mo2273/ace_brfss_data/<year>[_Vk]/`.
  - `extract_year.py`: reads the XPT in 50k-row chunks with `pandas.read_sas(format='xport')` and keeps only the ACE, language, weight, demographic and phone columns, plus any variable whose label matches nativity/language/birth/country/citizen terms.
  - `inspect_vars.py`: per-year variable and label inventory.
  - `cb_sections.py` and `html2txt.py`: codebook checks.
  - `check_versions.py`: version-file deduplication check.
  - `analyze_ace_language.py`: all main tables.
  - `supplement.py`: whole-module refusal and completeness on the items each state actually administered.
  - `item_coverage.py`, `extract_ace_section.py`, `docx2txt.py`: wording extraction.
- All Python was run as `/home/mo2273/miniforge3/bin/python -I script.py <data paths>`.
- The derived analytic file (ACE respondents only) is `/home/mo2273/ace_brfss_work/ace_pooled_analytic.csv`.
- CSV outputs, saved next to these notes:
  - `brfss_ace_language_counts.csv`: per year plus pooled.
  - `brfss_ace_language_by_state_year.csv`
  - `brfss_ace_dk_refused_by_language.csv`: per year and pooled, by item × language × ethnicity.
  - `brfss_ace_endorsement_hispanic_by_language.csv`
  - `brfss_ace_score_hispanic_by_language.csv`
  - `brfss_ace_completeness_by_language.csv`
  - `brfss_ace_complete_administered_pooled.csv`
  - `brfss_ace_module_refusal_by_state_language.csv`
  - `brfss_ace_states_data_vs_cdc_page.csv`
  - `brfss_ace_validation_vs_codebook.csv`

Core coding logic, verbatim from `analyze_ace_language.py`. These codes were verified against each year's codebook (see the first section).
```python
d['lang'] = np.select([q == 1, q == 2, (q >= 3) & (q <= 99)], ['English', 'Spanish', 'Other'], 'Missing')   # q = QSTLANG
h = d['HISPANC2'] if y <= 2012 else d['_HISPANC']      # 2009-12: 1=Yes,2=No ; 2019+: 1=Hispanic,2=Not,9=DK/Ref/Missing
d['hisp'] = np.select([h == 1, h == 2], ['Hispanic', 'Non-Hispanic'], 'Unknown')
d['ace_any'] = d[ITEMS].notna().any(axis=1)            # reached module: any of 11 ACE items non-blank (incl. DK/Ref)
valid: YN items in {1,2}; ACEDIVRC in {1,2,8}; frequency items in {1,2,3}  -> ace_complete = all 11 valid
endorse: YN==1; ACEDIVRC==1 (2 or 8 = not endorsed); frequency items in {2,3} (Once / More than once)
ace8 = depr + (drink|drugs) + prison + divorce + IPV + physical + emotional + (any of 3 sexual)   # complete cases only
# version files: respondents with ACE data in LLCPyyVk not already ACE-respondents in the main file (key = _STATE+SEQNO) are appended with weight _LCPWTVk/_LNDWTVk
```

## Q1. Which BRFSS years and states administered the ACE module, and did Puerto Rico?

### Takeaway
ACE item data appear in the public files for **2009, 2010, 2011, 2012 and 2019–2025**, and in none of 2013–2018. The 2023 module was *not* revised: the 11 core items are unchanged in English since 2019. The only change was two positive-childhood-experience items (ACEADSAF and ACEADNED), added in **2021**. **Puerto Rico administered ACE only in 2024**, with 4,174 respondents, essentially all in Spanish. A crucial technical point: in 2019–2025, states that asked ACE on a single questionnaire version (for example California 2020, New York, New Jersey, Arizona, Maryland, Ohio and Oklahoma) have **blank ACE data in the main LLCP file**. Their data exist only in the LLCPyyV1/V2/V3 files, and in 2011 California, Maine, Nebraska and Oregon exist only in the landline version files. Any count built from the main files alone misses 12–36% of ACE respondents in each 2019+ year (15% in 2019, 12% in 2020, 36% in 2021, 26% in 2022, 16% in 2023, 35% in 2024, 15% in 2025).

### Cited Findings
- **ACE variables by public file.** ACEDEPRS, ACEDRINK, ACEDRUGS, ACEPRISN, ACEDIVRC, ACEPUNCH, ACEHURT (renamed ACEHURT1 from 2019), ACESWEAR, ACETOUCH, ACETTHEM and ACEHVSEX are present in the 2009–2012 and 2019–2025 files. The 2013–2018 files contain **zero** variables starting with "ACE". ACEADSAF and ACEADNED are present from 2021 to 2025 — [CDC annual data files, e.g. 2013](https://www.cdc.gov/brfss/annual_data/annual_2013.html), [2021](https://www.cdc.gov/brfss/annual_data/annual_2021.html); variable inventory via `inspect_vars.py`.
- **Optional-module lists.** CDC's optional-module category pages list "Adverse Childhood Experience(s)" for 2009–2012 and 2019–2025 but not for 2013–2018 — [CDC module category 2013](https://www.cdc.gov/brfss/questionnaires/modules/category2013.htm), [2019](https://www.cdc.gov/brfss/questionnaires/modules/category2019.htm).
- **States with ACE data in the public files** (threshold ≥20 ACE respondents; main plus version files; V# marks a version-file state):
  - 2009 (2): Arkansas, Louisiana.
  - 2010 (5): DC, Hawaii, Nevada, Vermont, Wisconsin.
  - 2011 (9): California (landline V1/V2), Maine (landline V1), Minnesota, Montana, Nebraska (landline V1/V2), Oregon (landline V1/V2), Vermont, Washington, Wisconsin.
  - 2012 (5): Iowa, North Carolina, Oklahoma, Tennessee, Wisconsin.
  - 2019 (21): AL, DE, FL, IN, IA, KS (V2), MI, MS, MO, NM, NY (V3), ND, OH (V1), OK (V2), PA, RI, SC, TN, VA, WV, WI.
  - 2020 (28): AL, AZ, CA (V2), DC, FL, GA, HI, ID, IA, KS (V2), KY, MD (V3), MA (V1), MS, MO, MT, NV, NJ (V2), ND, OK (V2), RI, SC, SD, TX, UT, VA, WI, WY.
  - 2021 (16): AL, AR, IA, KS (V1), ME (V1), MS, NV, NH, NJ (V2), NY (V1), ND, OH (V1), OR, SC, VA, WI.
  - 2022 (12): AZ (V1), AR, FL, IA, NV, NJ (V2), ND, OH (V1), OK (V2), OR, SD, VA.
  - 2023 (12): DE, FL, GA, MD (V3), MO, NV, NJ, OH (V1), OR, RI, TN, VA.
  - 2024 (13): AZ (V2), FL, GA, HI, IA (V1), ME (V1), NV, ND, OH (V1), OK (V2), **Puerto Rico**, **U.S. Virgin Islands**, VA.
  - 2025 (11): IL, IN, KY, MO, MT, NH, NY (V1), OH (V1), SD, TN, VA.

  Source: [CDC annual data](https://www.cdc.gov/brfss/annual_data/annual_2024.html) and [version files, e.g. 2020](https://www.cdc.gov/brfss/annual_data/2020/llcp_multiq.html); `brfss_ace_language_by_state_year.csv`.
- **Agreement with CDC's state pages, 2019–2025.** With version files included, the data's state list matches CDC's "Modules by State" pages for every one of these years. Without version files, 28 state-years listed by CDC (for example California 2020 V2, New York 2019 V3, New Jersey 2020–2022 V2, Arizona 2022/2024) have no ACE data in the main file — [CDC modules by state 2020](https://www.cdc.gov/brfss/questionnaires/modules/state2020.htm), [2024](https://www.cdc.gov/brfss/questionnaires/modules/state2024.htm); `brfss_ace_states_data_vs_cdc_page.csv`.
- **Version-file contribution.** Version files contributed 28,918 ACE respondents in 2011, 19,226 (2019), 18,227 (2020), 33,475 (2021), 17,062 (2022), 10,498 (2023), 21,208 (2024) and 8,862 (2025). Of these, 1,432 / 237 / 543 / 478 / 355 / 185 / 402 / 316 were Spanish-interview — [CDC 2011 landline multiple-version files](https://www.cdc.gov/brfss/annual_data/2011/2011_landline_multiple.html), [2019+ version files](https://www.cdc.gov/brfss/annual_data/2019/llcp_multiq.html); `check_versions.py`. CDC's 2011 page states that "optional modules ... can be asked on either one or all versions" and that version-specific weights and data sets are provided for that case — [CDC 2011 landline multiple version page](https://www.cdc.gov/brfss/annual_data/2011/2011_landline_multiple.html).
- **CDC's ACE page lists more states than the public files contain.** The page (last reviewed June 29, 2023) lists states that "collected" ACE data each year from 2009 to 2021, including 2013–2018, for example: 2013 CA, IA, MI, OR, UT, WI; 2014, 16 states including AZ, FL, NC; 2015 including CA and TX; 2017 including CA and IL; 2018 including AZ and NJ. It also lists 2009 AR, CA, LA, NM, TN, WA; 2010, 12 states including FL, ME, NE, OH, PA, UT, WA; 2011 including Nevada; 2019 including New Jersey; and 2020 including Maine — [CDC BRFSS ACE Data page](https://www.cdc.gov/violenceprevention/aces/ace-brfss.html). The public files contain none of the 2013–2018 data. Also missing from the public files are 2009 CA/NM/TN/WA, 2010 FL/ME/NE/OH/PA/UT/WA, 2011 NV, 2019 NJ and 2020 ME (computed; see the CSV above).
- **2009 MMWR coverage.** The 2009 MMWR analyzed 26,229 adults in five states (AR, LA, NM, TN, WA) — [MMWR 2010;59(49):1609–13](https://www.cdc.gov/mmwr/preview/mmwrhtml/mm5949a1.htm). The 2009 public file has ACE data for only AR and LA, 12,120 respondents (computed).
- **Puerto Rico.** Puerto Rico's only ACE year in any public file is 2024: 4,174 respondents, 4,173 of them Spanish interviews, reaching 97.3% of PR's Spanish-interview sample. PR does not appear in CDC's 2009–2021 ACE state list, and PR 2025 has no ACE data — [CDC 2024 data](https://www.cdc.gov/brfss/annual_data/annual_2024.html), [modules by state 2024](https://www.cdc.gov/brfss/questionnaires/modules/state2024.htm), [CDC ACE page](https://www.cdc.gov/violenceprevention/aces/ace-brfss.html).
- **English wording changes.** The codebook question text for the 11 items is identical in 2019, 2023, 2024 and 2025, apart from a "Was it—" read-in stem. The 2021 and 2023 English questionnaires print identical ACE modules (13 items) — [2019 codebook](https://www.cdc.gov/brfss/annual_data/2019/pdf/codebook19_llcp-v2-508.HTML), [2023 codebook zip](https://www.cdc.gov/brfss/annual_data/2023/zip/codebook23_llcp-v2-508.zip), [2021 questionnaire](https://www.cdc.gov/brfss/questionnaires/pdf-ques/2021-BRFSS-Questionnaire-1-19-2022-508.pdf), [2023 questionnaire](https://www.cdc.gov/brfss/questionnaires/pdf-ques/2023-BRFSS-Questionnaire-508.pdf). In 2019 the physical-abuse item was reordered ("Not including spanking, (before age 18), how often did a parent or adult in your home ever hit, beat, kick, or physically hurt you in any way?") and renamed ACEHURT1 — [2019 codebook](https://www.cdc.gov/brfss/annual_data/2019/pdf/codebook19_llcp-v2-508.HTML), [2010 codebook](https://www.cdc.gov/brfss/annual_data/2010/pdf/codebook_10.pdf).
- **California 2011 omitted ACEPRISN.** The item is 0% non-blank among CA's 11,100 module respondents, so no CA 2011 respondent can be "complete on all 11" (computed, `item_coverage.py`).

### Inferences
- Researchers who build an "ACE states" sample from the main LLCP files alone will miss large, Hispanic-relevant samples: CA 2011/2020, NY, NJ, AZ, MD and OK. The version files are mandatory for this project.
- The 2013–2018 state-added ACE data (CA, TX, AZ, FL and IL among them) would roughly double the Spanish pool. They would have to be requested from state BRFSS coordinators and may use state-specific Spanish wording. This is a possible feasibility lever, not something available now.
- The premise of a "2023 revision" is not supported for the 11 core items. Item content is constant in English from 2019 to 2025, and 2009–2012 differ only in the ACEHURT ordering. The Spanish wording, however, changed repeatedly (see Q7).

### Gaps
- My automated parse of CDC's 2009–2012 "Modules by State" pages was incomplete: it found no ACE entries in the 2011 page and missed NC and OK in 2012. I relied on the data and on CDC's ACE page for those years and did not resolve whether the module pages themselves omit those states.
- I did not obtain any state-added (non-public) ACE data.

## Q2. How many Spanish-interview respondents answered the ACE module, by year, state and Hispanic ethnicity?

### Takeaway
Across all ACE years there are **19,226 Spanish-interview ACE respondents**; 16,507 are complete on all 11 items and 17,503 are complete on the items their state administered. **18,650 of the Spanish-interview respondents are Hispanic.** In 2019–2025 there are **16,702 Spanish-interview respondents (15,413 complete)**, but **4,173 of them (25%) are Puerto Rico 2024 alone**. Excluding territories leaves 12,517 Spanish-interview respondents (11,395 complete; 10,945 complete and Hispanic). The natural comparison group, English-interview Hispanics, numbers **27,565 in 2019–2025 (24,562 complete)**. 2009–2012 contribute only 2,524 Spanish-interview respondents, 1,365 of them from California 2011's landline version files.

### Cited Findings
**Table 1. ACE-module respondents by interview language and year (unweighted N unless marked wt%).**

Codebook checks used to build this table:
- QSTLANG is coded 1=English, 2=Spanish, 3–99=Other in every year.
- File-level QSTLANG frequencies reproduce the codebooks exactly, for example 2009: 405,625 / 12,594 / 306 / 14,082 blank; 2024: 435,803 / 21,867 — [2009 codebook](https://www.cdc.gov/brfss/annual_data/2009/pdf/codebook_09.pdf), [2024 codebook zip](https://www.cdc.gov/brfss/annual_data/2024/zip/codebook24_llcp-v2-508.zip); `brfss_ace_validation_vs_codebook.csv`.
- The ACE item frequencies also match: 2009 ACEDIVRC 2,577 / 9,252 / 42 / 109 / 135.

Source: [CDC annual and version files](https://www.cdc.gov/brfss/annual_data/annual_2024.html); `brfss_ace_language_counts.csv`.

| Year | States | ACE N | English | Spanish | Sp. complete (11) | Hispanic | Hisp-Eng | Hisp-Sp | Hisp-Eng complete | Hisp-Sp complete | wt% Spanish of ACE | wt% Spanish among Hisp. | Weight(s) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2009 | 2 | 12,120 | 12,081 | 39 | 39 | 286 | 247 | 39 | 225 | 39 | 0.73 | 21.8 | _FINALWT |
| 2010 | 5 | 24,406 | 24,367 | 39 | 36 | 906 | 868 | 38 | 803 | 35 | 0.54 | 8.9 | _FINALWT |
| 2011 | 9 | 77,444 | 75,563 | 1,881 | 484 (1,480 complete-on-administered) | 4,273 | 2,415 | 1,858 | 1,118 | 479 | 15.27* | 55.6* | _LLCPWT + _LNDWTV1/2 |
| 2012 | 5 | 32,824 | 32,259 | 565 | 535 | 1,168 | 611 | 557 | 570 | 528 | 2.36 | 43.8 | _LLCPWT |
| 2019 | 21 | 126,601 | 121,818 | 1,964 | 1,796 | 6,752 | 4,819 | 1,886 | 4,371 | 1,726 | 3.29 | 32.3 | _LLCPWT + _LCPWTV1–3 |
| 2020 | 28 | 147,616 | 144,178 | 3,438 | 3,136 | 11,783 | 8,507 | 3,276 | 7,607 | 2,995 | 8.23 | 38.2 | same |
| 2021 | 16 | 92,238 | 90,938 | 1,300 | 1,175 | 4,332 | 3,095 | 1,237 | 2,675 | 1,124 | 3.44 | 31.9 | same |
| 2022 | 12 | 65,348 | 63,967 | 1,381 | 1,245 | 4,261 | 2,920 | 1,341 | 2,581 | 1,214 | 5.21 | 33.7 | same |
| 2023 | 12 | 66,539 | 64,609 | 1,930 | 1,734 | 4,802 | 2,978 | 1,824 | 2,638 | 1,641 | 5.10 | 37.9 | same |
| 2024 | 13 | 60,492 | 55,303 | 5,189 | 4,923 | 8,145 | 3,002 | 5,143 | 2,723 | 4,879 | 9.93 | 50.7 | same |
| 2025 | 11 | 57,452 | 55,952 | 1,500 | 1,404 | 3,695 | 2,244 | 1,451 | 1,967 | 1,362 | 4.27 | 39.5 | same |
| **Pooled 2009–12** | | 146,794 | 144,270 | **2,524** | 1,094 (2,090 complete-on-administered) | 6,633 | 4,141 | **2,492** | 2,716 | 1,081 (2,062 complete-on-administered) | | | |
| **Pooled 2019–25** | | 616,286 | 596,765 | **16,702** | **15,413** | 43,770 | **27,565** | **16,158** | **24,562** | **14,941** | | | |
| Pooled 2019–25, excl. PR/VI/GU | | | | 12,517 | 11,395 | | 27,468 | 11,995 | 24,473 | 10,945 | | | |
| Pooled 2021–25 (13-item module) | | 342,069 | 330,769 | 11,300 | 10,481 | 25,235 | 14,239 | 10,996 | 12,584 | 10,220 | | | |
| Pooled 2021–25, excl. territories | | | | 7,115 | 6,463 | | | | | 6,224 | | | |
| **All years** | | 763,080 | 741,035 | **19,226** | 16,507 (17,503 complete-on-administered) | 50,403 | 31,706 | **18,650** | 27,278 | 16,022 (17,003 complete-on-administered) | | | |

\*The 2011 weighted shares are distorted because California, Maine, Nebraska and Oregon carry landline-only version weights.

Notes on Table 1:
- 2019: 2,819 ACE respondents, all from South Carolina, have blank QSTLANG and are counted as neither English nor Spanish.
- No ACE respondent in any year had QSTLANG 3–99.
- 544 Spanish-interview respondents in 2019–2025 were not coded Hispanic (Not Hispanic or Unknown).
- Source: [CDC data](https://www.cdc.gov/brfss/annual_data/annual_2020.html); `brfss_ace_language_counts.csv`, `brfss_ace_complete_administered_pooled.csv`.

- **Largest Spanish-interview contributors, all years.**

  | State | Spanish N | Years |
  |---|---|---|
  | Puerto Rico | 4,173 | 2024 |
  | Florida | 2,015 | 2019, 2020, 2022–2024 |
  | California | 1,599 | 1,365 in 2011 (landline V1/V2); 234 in 2020 (V2) |
  | Iowa | 1,397 | |
  | Texas | 1,042 | 2020 |
  | New Jersey | 992 | |
  | Illinois | 827 | 2025 |
  | New York | 795 | |
  | Arizona | 712 | |
  | Rhode Island | 673 | |
  | Nevada | 562 | |
  | Virginia | 537 | |

  The top 5 sources supply **53.2%** of all Spanish-interview ACE respondents — [CDC data](https://www.cdc.gov/brfss/annual_data/annual_2024.html); `brfss_ace_language_by_state_year.csv`.
- **Larger state-years.** 50 of 134 ACE state-years have ≥100 Spanish-interview ACE respondents. The largest single state-years after PR 2024 (4,173) are:

  | State-year | Spanish N |
  |---|---|
  | CA 2011 | 1,365 |
  | TX 2020 | 1,042 |
  | IL 2025 | 827 |
  | FL 2019 | 549 |
  | FL 2020 | 536 |
  | NJ 2023 | 516 |
  | IA 2022 | 430 |
  | IA 2021 | 406 |
  | NC 2012 | 403 |

  Source: `brfss_ace_language_by_state_year.csv`.
- **Puerto Rico 2024.** 4,174 ACE respondents: 4,173 Spanish, **0 English-interview Hispanics**, 4,006 complete — [CDC 2024 data](https://www.cdc.gov/brfss/annual_data/annual_2024.html).
- **Did Spanish-speakers in ACE states reach the module?** In ACE state-years with ≥30 Spanish interviews in the whole state sample, the share of Spanish interviews reaching the module was mostly 75–105% of the English share. The exceptions are Nebraska 2011 (ratio 0.33), Virginia 2021–2025 (0.37–0.72) and Florida 2022 (0.75). No state-year with ≥30 Spanish interviews skipped the module in Spanish (ratio <0.2). States with zero Spanish-interview ACE respondents (KS, OH, MI, PA, AL, MS, MO, ND, TN, WV, ME and others) had fewer than 30 Spanish interviews statewide — [CDC data](https://www.cdc.gov/brfss/annual_data/annual_2021.html); `brfss_ace_language_by_state_year.csv` (columns `pct_English/Spanish_interviews_reaching_ACE`).

### Inferences
- About two-thirds (12,517 of 19,226) of the Spanish-interview pool is the mainland 2019–2025 sample: about 11,000 complete Hispanic Spanish-interview respondents against about 24,500 English-interview Hispanics.
- Puerto Rico 2024 is a qualitatively different focal group: a territory with a near-100% Spanish sample and no within-territory English-interview Hispanic comparators. Pooling it with mainland Spanish speakers fully confounds language with place, and plausibly with Spanish variety and translation version.
- The 2009–2012 pool is dominated by California 2011 landline respondents. That sample lacks ACEPRISN and carries landline-only version weights, which makes 2009–2012 weak for item-level DIF.
- A 2018 Northwestern MPH thesis analyzed 2011–2012 BRFSS ACE data from nine states with 2,983 Hispanic respondents — [Alhalel 2018](https://prism.northwestern.edu/records/7mt6a-brh38). My count for 2011–2012 is 5,441 Hispanic ACE respondents. The difference is consistent with the thesis not using the 2011 landline version files (California etc.), but I did not verify their selection.

### Gaps
- I did not compute design-based standard errors. Weighted percentages pool `_LLCPWT`, version weights and landline-only weights, which CDC does not endorse for pooled multi-state, multi-year analysis without adjustment.

## Q3. Do "Don't know" / "Refused" rates differ by interview language?

### Takeaway
In **2019–2025**, item-level DK and Refused rates are low and, if anything, *lower* among Spanish-interview respondents. Among Hispanics, Refused was 0.4–1.1% in Spanish vs 1.1–2.6% in English, and whole-module refusal was 0.26% vs 0.88%. In **2009–2012**, Spanish-interview Hispanics refused about 13–14% of nearly every item vs 5–6% in English. Almost all of that comes from **California 2011, where 24.0% of Spanish vs 13.5% of English module respondents refused every item**, a language-differential module-level nonresponse.

### Cited Findings
**Table 2. Item non-substantive responses among Hispanic module respondents (% of non-blank responses, unweighted).**

| Item | 2009–12 DK En / Sp | 2009–12 Ref En / Sp | 2019–25 DK En / Sp | 2019–25 Ref En / Sp |
|---|---|---|---|---|
| ACEDEPRS | 0.51 / 0.28 | 5.43 / 13.68 | 0.96 / 0.42 | 1.36 / 0.43 |
| ACEDRINK | 0.29 / 0.08 | 5.43 / 13.25 | 0.35 / 0.24 | 1.25 / 0.44 |
| ACEDRUGS | 0.29 / 0.16 | 5.39 / 13.21 | 0.59 / 0.30 | 1.21 / 0.36 |
| ACEPRISN | 0.34 / 0.09 | 0.98 / 0.26 (CA not asked) | 0.37 / 0.11 | 1.14 / 0.38 |
| ACEDIVRC | 0.34 / 0.56 | 5.46 / 13.25 | 0.74 / 0.85 | 1.26 / 0.60 |
| ACEPUNCH | 1.28 / 0.72 | 5.89 / 13.38 | 1.69 / 1.38 | 2.05 / 0.75 |
| ACEHURT(1) | 0.46 / 0.28 | 5.78 / 13.46 | 0.61 / 0.75 | 2.21 / 0.77 |
| ACESWEAR | 0.65 / 0.16 | 5.83 / 13.42 | 0.75 / 0.70 | 1.99 / 0.70 |
| ACETOUCH | 0.22 / 0.12 | 6.41 / 13.95 | 0.37 / 0.41 | 2.61 / 1.02 |
| ACETTHEM | 0.31 / 0.04 | 6.17 / 13.79 | 0.36 / 0.40 | 2.42 / 0.94 |
| ACEHVSEX | 0.27 / 0.12 | 6.32 / 13.75 | 0.33 / 0.25 | 2.44 / 1.08 |
| ACEADSAF (2021+) | – | – | 0.38 / 0.77 | 1.58 / 0.82 |
| ACEADNED (2021+) | – | – | 0.48 / 0.72 | 1.50 / 0.77 |

Base N (Hispanic, non-blank): 2009–12 about 4,140 English / 2,490 Spanish; 2019–25 about 27,400 English / 16,100 Spanish. ACEDIVRC code 8 ("Parents not married"), all ethnicities: 2019–25 1.39% English vs 1.33% Spanish; 2009–12 0.63% vs 0.83%. Source: [CDC data](https://www.cdc.gov/brfss/annual_data/annual_2019.html); `brfss_ace_dk_refused_by_language.csv`, which also has per-year and all-ethnicity rows.

- **Module-level refusal (every non-blank item = 9).**
  - CA 2011: Spanish 328/1,365 (24.0%), English 1,316/9,735 (13.5%).
  - 2019–2025 pooled: Spanish 43/16,702 vs English 5,248/596,765.
  - Other cells with ≥5% module refusal are English-only (TN 2012 17.1%, MA 2020 8.8%, NV 2021 8.1%, SD 2020 5.4%) or small Spanish cells (OK 2019, 4/53; WI 2020, 2/32).

  Source: `brfss_ace_module_refusal_by_state_language.csv`.
- **Share with any DK/Ref on the 11 items.** 2019–25 Hispanics: 10.0% English vs 6.6% Spanish. 2009–12: 11.1% vs 17.1% — `brfss_ace_completeness_by_language.csv`.

### Inferences
- In 2019+ data, missingness is not a major barrier. Its direction (fewer refusals in Spanish) could itself reflect acquiescence or interviewer-administration differences worth reporting alongside DIF.
- The CA 2011 language-differential module refusal is a selection problem for any analysis that uses 2009–2012.
- The PCE items (ACEADSAF/ACEADNED) have higher DK in Spanish (about 0.75% vs 0.4–0.5%), the only items where DK runs higher in Spanish. That is consistent with harder-to-translate frequency anchors ("a little of the time" etc.), though this is speculative.

### Gaps
- DK/Ref rates are unweighted. I did not test differences statistically.

## Q4. Crude endorsement prevalence and ACE score by interview language among Hispanic respondents (descriptive, unadjusted)

### Takeaway
Spanish-interview Hispanics endorse almost every ACE item much less often than English-interview Hispanics. The gap is largest for **verbal abuse (18.4% vs 41.7%)**, household mental illness (5.1% vs 22.5%), drug use (3.9% vs 14.6%) and incarceration (3.1% vs 14.5%). Physical abuse is nearly equal (30.2% vs 34.7%). The weighted mean 8-category ACE score is 1.25 vs 2.19, and the 4+ ACE prevalence is 10.7% vs 25.3% (2019–2025). The pattern was similar in 2009–2012, where physical abuse was *higher* in Spanish (34.3% vs 23.4%). These are crude descriptive gaps confounded by nativity, age, origin and state; they are **not** evidence of DIF by themselves.

### Cited Findings
**Table 3. Hispanic respondents: weighted % endorsed (unweighted n endorsed / n valid). CRUDE, UNADJUSTED, DESCRIPTIVE ONLY.**

| Item | 2019–25 English | 2019–25 Spanish | 2019–25 Spanish excl. PR/VI/GU | 2009–12 English | 2009–12 Spanish |
|---|---|---|---|---|---|
| Depressed/mentally ill household (ACEDEPRS) | 22.5% (6,216/26,924) | 5.1% (1,076/16,020) | 4.2% (514/11,880) | 17.8% (675/3,895) | 4.8% (96/2,144) |
| Problem drinker (ACEDRINK) | 26.5% (7,613/27,055) | 18.0% (3,103/16,023) | 17.6% (2,134/11,876) | 30.5% (1,122/3,903) | 24.1% (535/2,158) |
| Drug use (ACEDRUGS) | 14.6% (4,228/26,985) | 3.9% (809/16,014) | 3.3% (447/11,871) | 14.9% (499/3,905) | 3.1% (82/2,157) |
| Incarceration (ACEPRISN) | 14.5% (3,896/27,031) | 3.1% (588/16,030) | 2.8% (332/11,879) | 13.9% (303/2,916) | 3.8% (40/1,139) |
| Parents separated/divorced (ACEDIVRC) | 40.0% (10,358/26,879) | 26.2% (4,249/15,862) | 25.4% (2,911/11,725) | 33.0% (1,255/3,900) | 19.7% (358/2,146) |
| Witnessed IPV (ACEPUNCH) | 23.6% (6,360/26,374) | 17.1% (2,611/15,736) | 17.6% (2,063/11,632) | 23.5% (924/3,843) | 25.5% (529/2,138) |
| Physical abuse (ACEHURT/1) | 34.7% (9,219/26,584) | 30.2% (4,425/15,817) | 31.4% (3,613/11,688) | 23.4% (858/3,880) | 34.3% (663/2,146) |
| Verbal abuse (ACESWEAR) | 41.7% (11,171/26,573) | 18.4% (2,770/15,813) | 18.8% (2,137/11,693) | 41.7% (1,444/3,867) | 35.5% (683/2,150) |
| Touched sexually (ACETOUCH) | 14.1% (4,094/26,484) | 7.2% (1,254/15,792) | 7.2% (905/11,673) | 13.1% (536/3,860) | 7.3% (167/2,138) |
| Made to touch (ACETTHEM) | 11.0% (3,179/26,516) | 6.2% (968/15,790) | 6.4% (743/11,673) | 9.6% (385/3,864) | 6.0% (131/2,144) |
| Forced sex (ACEHVSEX) | 6.9% (1,967/26,487) | 4.4% (678/15,779) | 4.6% (547/11,659) | 4.2% (208/3,858) | 2.8% (93/2,143) |
| Any sexual abuse (3 items) | 16.4% (4,689/26,384) | 10.2% (1,582/15,736) | 10.3% (1,182/11,622) | 16.0% (620/3,846) | 10.1% (234/2,136) |
| Household substance use (drink or drugs) | 31.4% (8,870/26,982) | 19.6% (3,404/15,997) | 19.0% (2,283/11,853) | 36.5% (1,290/3,901) | 24.8% (553/2,157) |

Endorsement means "Yes" for household items, "Once"/"More than once" for frequency items, and ACEDIVRC=1, with code 8 scored as not endorsed. Weights are the respondent's applicable final weight; see the header. Source: [CDC data](https://www.cdc.gov/brfss/annual_data/annual_2023.html); `brfss_ace_endorsement_hispanic_by_language.csv`. That file also includes rows for all Spanish-interview respondents regardless of ethnicity.

**Table 4. ACE score among complete cases (8-category score: mental illness, substance use, incarceration, divorce, IPV, physical, emotional, any sexual). CRUDE.**

| Period / group | n complete | Weighted mean ACE8 | Weighted % ACE8 ≥4 (unweighted n) | Weighted % ACE8 = 0 | Weighted mean 11-item count |
|---|---|---|---|---|---|
| 2009–12 Hispanic, English | 2,716 | 1.91 | 19.6% (535) | 28.5% | 2.15 |
| 2009–12 Hispanic, Spanish | 1,081 | 1.43 | 12.3% (131) | 40.0% | 1.54 |
| 2019–25 Hispanic, English | 24,562 | 2.19 | 25.3% (6,326) | 27.1% | 2.43 |
| 2019–25 Hispanic, Spanish | 14,941 | 1.25 | 10.7% (1,542) | 42.4% | 1.34 |
| 2019–25 excl. territories, English | 24,473 | 2.19 | 25.3% (6,311) | 27.1% | 2.43 |
| 2019–25 excl. territories, Spanish | 10,945 | 1.25 | 10.8% (1,118) | 42.7% | 1.34 |

Source: `brfss_ace_score_hispanic_by_language.csv`.

### Inferences
- The language gap is not uniform. It is very large for the verbal-abuse, mental-illness, drug and incarceration items and small for physical abuse and witnessed IPV. A non-uniform gap is the profile one would expect if some items function differently by language, and it coincides with the items whose Spanish wording shifts severity or scope (see Q7, e.g. "humillaba" for "put down"). It is equally consistent with real differences in exposure, with immigrant selection, or with differences in how different cultures construe "mental illness" or "drugs". The data alone cannot separate these.
- The Spanish physical-abuse estimate was *higher* in 2009–2012 (34.3% vs 23.4%) but slightly lower in 2019–2025. This change coincides with the change in the Spanish exclusion clause from "nalgadas" to "palmadas" and with a different state mix, so it is a candidate DIF signal worth examining by translation version.

### Gaps
- I made no adjustment for age, sex, education, state or survey year. Weighted figures pool non-poolable weights. I computed no confidence intervals.

## Q5. Feasibility verdict: is the Spanish N sufficient, including for low-prevalence items?

### Takeaway
**Sample size does not kill the project, provided it is restricted to 2019–2025 and built with the version files.** The mainland 2019–2025 sample gives about **10,945 complete Spanish-interview Hispanics vs 24,473 English-interview Hispanics**, 20–50× the roughly 200–500 focal-group sizes commonly cited for binary-item DIF (the benchmark given in the assignment brief). Even the rarest items have hundreds of Spanish endorsements. The real threats are design threats, not N:
1. Language is fully confounded with Puerto Rico in 2024.
2. No nativity or acculturation variable exists, so translation DIF cannot be separated from cultural or immigrant-selection DIF.
3. The Spanish wording changed between 2012, 2019 and 2020, and the 2021–2025 Spanish text is not publicly verifiable.
4. Spanish N is concentrated in a few state-years.

2009–2012 is **not viable** for primary item-level DIF.

### Cited Findings
- **2019–2025 Spanish-interview Hispanic endorsement counts (unweighted).** These are the numbers that drive DIF power for rare items:

  | Item | All Spanish-interview Hispanics | Excl. territories |
  |---|---|---|
  | ACEPRISN | 588 | 332 |
  | ACEHVSEX | 678 | 547 |
  | ACEDRUGS | 809 | 447 |
  | ACETTHEM | 968 | 743 |
  | ACEDEPRS | 1,076 | 514 |
  | ACETOUCH | 1,254 | 905 |
  | ACEPUNCH | 2,611 | 2,063 |
  | ACESWEAR | 2,770 | 2,137 |
  | ACEDRINK | 3,103 | 2,134 |
  | ACEDIVRC | 4,249 | 2,911 |
  | ACEHURT1 | 4,425 | 3,613 |

  Spanish 4+ ACE (8-category) complete cases: 1,542 (1,118 excluding territories). Source: [CDC data](https://www.cdc.gov/brfss/annual_data/annual_2025.html); `brfss_ace_endorsement_hispanic_by_language.csv`, `brfss_ace_score_hispanic_by_language.csv`.
- **2009–2012 Spanish-interview Hispanic endorsement counts.** ACEPRISN **40**, ACEDRUGS **82**, ACEHVSEX **93**, ACEDEPRS **96**, ACETTHEM 131, ACETOUCH 167. There are 1,081 complete cases on all 11 items, or 2,062 if California 2011's missing ACEPRISN is ignored. 1,347 of the 2,492 Hispanic Spanish-interview respondents are California 2011 landline respondents — `brfss_ace_endorsement_hispanic_by_language.csv`, `brfss_ace_language_by_state_year.csv`.
- **Smallest 2019–2025 year.** The smallest complete Spanish-interview Hispanic N in any single year is 1,124 (2021). Excluding PR, 2024 drops to 883 — `brfss_ace_language_counts.csv`.
- **PR share.** PR 2024 is 4,173 of 16,702 (25%) of 2019–2025 Spanish-interview respondents and has 0 English-interview Hispanic comparators — `brfss_ace_language_by_state_year.csv`.
- **No nativity or acculturation variables** exist in any public file (Q6), and **the Spanish item wording differs across 2012, 2019 and 2020** (Q7).

### Inferences
- **Recommended analytic frame:**
  - Hispanic adults, 2019–2025, main plus version files.
  - Exclude PR, VI and GU from the primary analysis, or analyze them as a separate focal group.
  - Restrict to state-years with both language groups, with state and year terms in the matching or conditioning model.
  - Stratify or test by Spanish translation version: 2019 (n about 1,900 Spanish) vs 2020 onward.
  - Treat 2009–2012 at most as a sensitivity or replication analysis for common items, since it uses a different (older) Spanish translation.
- **Power for rare items.** Logistic-regression or IRT-based DIF on items with 330–550 focal endorsements (mainland ACEPRISN, ACEDRUGS, ACEDEPRS, ACEHVSEX) is adequate for moderate uniform DIF. Cells become thin in high-score strata: only about 1,100 mainland Spanish respondents have 4+ ACEs. Non-uniform DIF tests on the sexual-abuse and incarceration items will be imprecise.
- **Matching-criterion problem.** The large, near-uniform depression of Spanish endorsement across most items means the total-score matching criterion may itself be contaminated. Purification or anchor selection, for example anchoring on items with equivalent wording such as ACEDRINK or the sexual items, is essential, and results will be sensitive to it.
- **Blunt bottom line.** Feasible on N; vulnerable on interpretation. Without nativity data, a positive DIF finding can be attributed to "interview language" only in the operational sense (translation plus who chooses Spanish), not to translation per se.

### Gaps
- I did not run any formal power calculation or DIF model.

## Q6. Which covariates are in the public files during ACE years, and is there any nativity or acculturation variable?

### Takeaway
Standard demographics are available in every ACE year: age, sex, education, income, marital status, race and Hispanic ethnicity, phone type, and metropolitan or urban/rural status (with caveats). **No nativity, country-of-birth, years-in-U.S., citizenship, language-preference (other than QSTLANG) or acculturation variable exists in any of the 17 public files (2009–2025) or the version files I processed.** Hispanic heritage subgroup (Mexican, Puerto Rican, Cuban, etc.) is also absent: 2009–2012 has a Yes/No item only and 2013+ has only the collapsed _HISPANC.

### Cited Findings
- **Variables present** (verified by name and label in each file's XPT header) — [CDC annual data files](https://www.cdc.gov/brfss/annual_data/annual_2019.html); `inspect_vars.py`, `/home/mo2273/ace_brfss_work/<year>/vars_<year>.csv`:
  - Age: `_AGEG5YR` in all years; `_AGE80` in 2013+.
  - Sex: `SEX` (2009–2017), `SEX1` (2018), `SEXVAR` and `_SEX` (2019+), `BIRTHSEX` (2019–2023).
  - Education: `EDUCA`.
  - Income: `INCOME2` and `_INCOMG` (2009–2020); `INCOME3` and `_INCOMG1` (2021+).
  - Marital status: `MARITAL`.
  - Race/ethnicity: `HISPANC2` (2009–2012, Yes/No); `_HISPANC` (2013+); `_RACEGR2/3/4`, `_MRACE(1/2)`, `_PRACE(1/2)`.
  - Phone: `QSTVER` (2011+: 10–13 landline, 20–23 cell; 2009–2010 files are landline only); `CELLFON*`, `LANDLINE`; `_DUALUSE` (2012+).
  - Urban/rural: `MSCODE` (metropolitan status) in all years; `_METSTAT` and `_URBSTAT` in 2018+.
- **Coding of QSTVER and Hispanic variables** — [2019 codebook](https://www.cdc.gov/brfss/annual_data/2019/pdf/codebook19_llcp-v2-508.HTML), [2012 codebook](https://www.cdc.gov/brfss/annual_data/2012/pdf/CODEBOOK12_LLCP.pdf):
  - QSTVER: 10 = landline single, 11–13 = landline multiple versions 1–3, 20 = cell single, 21–23 = cell versions 1–3.
  - HISPANC2 (2009–2012): 1 Yes, 2 No, 7 DK, 9 Refused.
  - _HISPANC (2019+): 1 Hispanic, 2 Not, 9 DK/Ref/Missing.
- **Nativity search.** A label search across all 17 main files for "born", "birth", "countr", "nativ", "citizen", "immigra", "accultur", "United States", "U.S.", "English", "Spanish", "Mexic" and "years in" returned only `_HISPANC`/`_CHISPNC` (Hispanic origin) and QSTLANG ("Language identifier") — `inspect_vars.py` output.
- **Coverage among ACE respondents.** MSCODE is populated only for landline interviews in the dual-frame years: 4.4% of 2019–2025 Spanish-interview ACE respondents vs 30.6% of English. `_URBSTAT` covers 99.8% of English but 74.9% of Spanish respondents, because it is 0% populated for Puerto Rico and the Virgin Islands in 2024. Cell-phone share among Hispanics in 2019–25 is 95.3% for Spanish and 88.1% for English interviews. Income is missing (77/99/blank) for 23.6% of Spanish-interview vs 15.7% of English-interview Hispanics. Education and marital missingness is ≤1.9% — `brfss_ace_completeness_by_language.csv`; PR/VI check computed from the [2024 file](https://www.cdc.gov/brfss/annual_data/annual_2024.html).

### Inferences
- Confounding of language with nativity, generation, time in the U.S. and national origin **cannot be addressed** with public BRFSS. Age, education, income, state and phone type are the only partial proxies. Some state-specific state-added questions (for example country of birth) may exist in restricted state files; I did not verify any.
- MSCODE is unusable for cell respondents. For 2019+, use `_URBSTAT`/`_METSTAT`, noting that they are missing for the territories.

### Gaps
- I did not inspect state-added questions, which are not in the public files, or other optional modules beyond variable-label searches. Nothing in the public files resembled a nativity item.

## Q7. Official English vs Spanish ACE item wording, and where the translation shifts meaning, scope or severity

### Takeaway
CDC has fielded **at least four different Spanish versions of the ACE module**: 2009, 2010–2011, 2012, and 2019, with 2020 differing from 2019 on the IPV item. All of them sit against an essentially fixed English text. The CDC "BRFSS ACE Module 2009–2020 (Spanish)" PDF that CDC's ACE page distributes is actually the **2011 Module 31** translation, not the 2019/2020 text. **No CDC Spanish questionnaire for 2021–2025 is publicly posted**, and those years hold 11,300 of the 19,226 Spanish-interview ACE respondents. The most consequential translation shifts are in the items with the largest crude language gaps:
- **Verbal abuse.** "put you down" became **"humilló / humillaba" (humiliated)**, a more severe threshold. "swear at you" became "dijo groserías" (2009–2012) and then "maldecía" (2019+).
- **Physical abuse.** The exclusion clause "spanking" became "nalgadas" and then **"palmadas"** (open-hand slaps or pats). 2012 added "azotaron" (whipped).
- **IPV.** Three different verb lists, including "azotaban".
- **Drugs.** "illegal street drugs" became "drogas ilícitas **adquiridas en la calle**" (narrower) in 2009–2012 and then plain "drogas ilícitas" (broader) in 2019+.

### Cited Findings
Sources for the wording:
- English: [2010 questionnaire](https://www.cdc.gov/brfss/questionnaires/pdf-ques/2010brfss.pdf), [2019](https://www.cdc.gov/brfss/questionnaires/pdf-ques/2019-BRFSS-Questionnaire-508.pdf), [2021](https://www.cdc.gov/brfss/questionnaires/pdf-ques/2021-BRFSS-Questionnaire-1-19-2022-508.pdf), [2023](https://www.cdc.gov/brfss/questionnaires/pdf-ques/2023-BRFSS-Questionnaire-508.pdf).
- Spanish: [2009](https://www.cdc.gov/brfss/questionnaires/pdf-ques/q2009span.pdf), [2010](https://www.cdc.gov/brfss/questionnaires/pdf-ques/q2010span.pdf), [2011](https://www.cdc.gov/brfss/questionnaires/pdf-ques/q2011span.pdf), [2012](https://www.cdc.gov/brfss/questionnaires/pdf-ques/2012_BRFSS_Spanish.pdf), [2019](https://www.cdc.gov/brfss/questionnaires/pdf-ques/2019-BRFSS-Questionnaire-Spanish-Verison-508.pdf), [2020](https://www.cdc.gov/brfss/questionnaires/pdf-ques/2020-BRFSS-Questionnaire-Spanish-Verison-508.pdf).
- Text was extracted with pdftotext; module text saved at `/home/mo2273/ace_brfss_work/qace/`.

**Table 5. Side-by-side wording.** English 2009–2012 equals 2010. English 2019–2025 is identical to 2010 except where noted. Spanish 2010 equals 2011. All columns cover the same 11 items.

| Item | English (2010; 2019–25 changes noted) | Spanish 2010–2011 (2009 differences noted) | Spanish 2012 | Spanish 2019 | Spanish 2020 | Flag |
|---|---|---|---|---|---|---|
| Intro/frame | "Now, looking back before you were 18 years of age—" | "Ahora, recuerde la época anterior a que cumpliera los 18 años:" | same | same | same | Equivalent |
| ACEDEPRS | "Did you live with anyone who was depressed, mentally ill, or suicidal?" | "¿Vivió con alguien que tenía depresión, una enfermedad mental o tendencias suicidas?" | same | same | same | Minor: "tenía depresión" (had depression) and "tendencias suicidas" may read as more clinical than "was depressed / suicidal". Large crude gap (5% vs 22.5%) |
| ACEDRINK | "...a problem drinker or alcoholic?" | "...tenía problemas con la bebida o que era alcohólico?" | same | same | same | Equivalent |
| ACEDRUGS | "...used illegal street drugs or who abused prescription medications?" | "...consumiera drogas ilícitas **adquiridas en la calle** o que abusara de medicamentos recetados?" (2009: consumía/abusaba) | "...consumía drogas ilícitas adquiridas en la calle o que abusara de medicinas recetadas?" | "...consumía **drogas ilícitas** o que abusara de medicamentos recetados?" | same as 2019 | **Scope shift.** "Acquired on the street" adds a purchase-location condition, which is narrower. 2019+ drops "street", which is broader than the English. Not stable across years |
| ACEPRISN | "...served time or was sentenced to serve time in a prison, jail, or other correctional facility?" | "...haya estado preso o que haya sido sentenciado a cárcel, a prisión o a algún otro centro correccional?" (2009: estuvo/fue) | "...estuvo preso o que fue sentenciado a cárcel, a prisión..." | "...estuvo preso o que fue sentenciado a pasar tiempo en la cárcel, prisión o algún otro centro correccional?" | same as 2019 | Minor: "estuvo preso" can include short detention, which is broader |
| ACEDIVRC | "Were your parents separated or divorced?" (8 = Parents not married) | "¿Sus padres estaban separados o divorciados?" (8 = "Los padres no estaban casados") | same | same | same | Near-equivalent. Both are ambiguous for consensual unions; code-8 use is similar (1.33% Sp vs 1.39% En, 2019+) |
| ACEPUNCH | "How often did your parents or adults in your home ever slap, hit, kick, punch or beat each other up?" (2019+: adds "Was it…") | "...se dieron **bofetadas, patadas, puñetazos o golpes**?" | "...se **pegaban, cacheteaban, golpeaban, pateaban o azotaban** entre ellos?" | same as 2012 + "¿Fue…?" | "...se **cacheteaban, pegaban, pateaban, se daban puñetazos o palizas**? ¿Fue…?" | **Three different Spanish verb sets.** "Azotaban" (whipped/flogged) adds an act not in the English. "Ever" is never translated. 2019 and 2020 Spanish differ |
| ACEHURT / ACEHURT1 | 2010: "Before age 18, how often did a parent or adult in your home ever hit, beat, kick, or physically hurt you in any way? Do not include spanking. Would you say—"; 2019+: "Not including spanking, (before age 18), how often did a parent or adult in your home ever hit, beat, kick, or physically hurt you in any way? Was it—" | "Antes de que usted cumpliera 18 años, ¿con qué frecuencia **un adulto en su hogar** le pegó, golpeó, pateó o lastimó físicamente **de alguna otra forma**? No incluya las **nalgadas**." | "...sus padres o un adulto en la casa le pegaron, golpearon, patearon, **azotaron** o lastimaron físicamente de alguna forma? No incluya las nalgadas." | "**Sin incluir palmadas**, antes de que usted cumpliera los 18 años, ¿con qué frecuencia sus padres o un adulto en la casa le pegaron, golpearon, patearon o lastimaron físicamente de alguna forma? ¿Fue…?" | same as 2019 ("de alguna manera") | **Scope/severity.** "Azotaron" (2012) explicitly includes whipping, a common disciplinary practice, which should raise endorsement. The 2019+ exclusion "palmadas" (open-hand slaps or pats) is a broader or vaguer exclusion than "spanking/nalgadas". 2009–2011 omit "parent" (adult only) |
| ACESWEAR | "How often did a parent or adult in your home ever swear at you, insult you, or put you down?" | "...uno de sus padres o un adulto en su casa **le dijo groserías**, le insultó o **le humilló**?" (**2009 omits "en su casa"**, i.e. any adult) | "...sus padres o un adulto en la casa le dijeron groserías, lo insultaron o lo humillaron?" | "...uno de sus padres o un adulto en su casa **lo maldecía**, insultaba o **humillaba**? ¿Fue…?" | same as 2019 | **Severity shift (largest flag).** "Humillar" (to humiliate) is a higher threshold than "put down". "Maldecir" can mean to curse or damn someone, which is stronger or less idiomatic than "swear at". The 2019+ imperfect tense ("maldecía", "insultaba") implies a habitual pattern, which conflicts with the "Una vez" (once) option. Largest crude gap: 18.4% vs 41.7% |
| ACETOUCH | "...anyone at least 5 years older than you or an adult, ever touch you sexually?" | "...alguna persona al menos 5 años mayor que usted o un adulto le tocó sexualmente?" | same | "...lo tocó sexualmente? ¿Fue…?" | same as 2019 | Equivalent. "Ever" is dropped. The 2019+ masculine "lo" replaces the neutral "le" |
| ACETTHEM | "...try to make you touch them sexually?" | "...intentó que usted le tocara sexualmente?" | same | "...intentó hacer que usted **la** tocara sexualmente?" | same as 2019 | Minor. "La" agrees with "persona" but can be heard as "touch *her*", implying a female perpetrator |
| ACEHVSEX | "...force you to have sex?" | "...le forzó a que tuviera relaciones sexuales?" | same | "...lo forzó a tener relaciones sexuales?" | same as 2019 | Equivalent ("relaciones sexuales" is about as narrow as "have sex") |
| Response options | Never / Once / More than once; DK; Refused | Nunca / Una vez / Más de una vez; "No sabe/No está seguro"; "Se niega a contestar" | same | same; "Se negó a contestar" | same | Equivalent |

Further wording findings:
- **CDC's standalone Spanish module PDF is the 2011 text.** The PDF CDC's ACE page labels "BRFSS ACE Module 2009–2020 (Spanish)" has PDF metadata titled "2011 BRFSS Questionnaire – Modulo 31 – Spanish version". Its text matches the 2010–2011 translation ("groserías", "humilló", "nalgadas", "adquiridas en la calle", "bofetadas"), and it contains a duplicated item 5 — [CDC Spanish ACE module PDF](https://www.cdc.gov/violenceprevention/pdf/BRFSS_Adverse_Module_Spanish.pdf), [CDC ACE page](https://www.cdc.gov/violenceprevention/aces/ace-brfss.html).
- **No 2021+ Spanish questionnaire is posted.** CDC's questionnaire index lists Spanish questionnaires through 2020 only; the 2021–2024 entries are English-only. Guessed 2021–2024 Spanish URLs returned HTTP 404 — [CDC questionnaires index](https://www.cdc.gov/brfss/questionnaires/index.htm). A BRFSS OMB supporting document indicates that Spanish versions are provided annually to state health departments and data collectors. This comes from a search snippet that I did not read in full — [OMB ICR document](https://omb.report/icr/202312-0920-004/doc/137910200.pdf).
- **English PCE items (2021+)** — [2021 questionnaire](https://www.cdc.gov/brfss/questionnaires/pdf-ques/2021-BRFSS-Questionnaire-1-19-2022-508.pdf):
  - ACEADSAF: "For how much of your childhood was there an adult in your household who made you feel safe and protected? Would you say never, a little of the time, some of the time, most of the time, or all of the time?"
  - ACEADNED: "...who tried hard to make sure your basic needs were met?..."
- **Utah's 2022 state-added Spanish questionnaire** (state questions STACE.01–09, not the CDC optional module) uses the 2010–2012 style wording ("le dijo groserías, le insultó o le humilló"; "Sin incluir las nalgadas"; "drogas ilícitas adquiridas en la calle"). It collapses the three sexual items into one, and translates the PCE item as "¿Durante cuánto tiempo durante su infancia hubo un adulto en su hogar que lo hizo sentir seguro y protegido?" — [Utah 2022 BRFSS Spanish questionnaire](https://healthassessment.utah.gov/wp-content/uploads/UT_2022_BRFSS_SPANISH_Questionnaire_ACCESSIBLE.docx).
- **Puerto Rico may have its own Spanish version.** CDC has posted a Puerto Rico-specific Spanish questionnaire in the past (2008: `q2008span_puertorico.pdf`) — [CDC questionnaires index](https://www.cdc.gov/brfss/questionnaires/index.htm).

### Inferences
- Item-level DIF must be analyzed **by Spanish translation version**: 2009, 2010–11, 2012, 2019, and 2020+ (assumed). Otherwise a DIF estimate averages over different stimuli. The 2019 vs 2020 change in ACEPUNCH offers a natural check: if Spanish ACEPUNCH functioning shifts between 2019 and 2020 while English is unchanged, that points to wording-driven DIF.
- The a priori DIF hypotheses best supported by the wording are:
  - ACESWEAR: Spanish harder to endorse, because of "humillar" and the habitual tense.
  - ACEHURT1: direction ambiguous, because of the "palmadas" exclusion. In 2012 Spanish should be easier to endorse because of "azotaron".
  - ACEDRUGS: harder in 2009–2012, then easier in 2019+.
  - ACEPUNCH: varies by year.
  
  ACEDRINK, ACEDIVRC and the sexual items look like reasonable anchor candidates on wording grounds.
- Puerto Rico 2024 may have used a PR-specific Spanish instrument, given the past PR-specific questionnaire, which is another reason to analyze PR separately. This is unverified.

### Gaps
- **The CDC Spanish ACE wording for 2021–2025 (including the PCE items) and for Puerto Rico 2024 could not be retrieved**; it is not posted publicly. It must be requested from the CDC BRFSS team or from state coordinators (for example Florida, New Jersey, Iowa, Illinois). Until then, the wording behind about 59% of all Spanish-interview ACE respondents is unverified.
- The translation-shift flags are my own linguistic reading. They have not been reviewed by a bilingual expert panel or checked against cognitive-testing evidence, and I found none for the BRFSS Spanish ACE module. No study testing BRFSS ACE measurement invariance by interview language turned up in my searches.
- I could not determine whether individual states may deviate from CDC's Spanish optional-module text.
