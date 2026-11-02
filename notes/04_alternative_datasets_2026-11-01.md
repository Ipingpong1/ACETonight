# Alternative and replication datasets for studying ACE measurement invariance by interview language, plus status checks on two secondary ideas (2023 YRBS ACE psychometrics; birth-cohort invariance in BRFSS)

Labels used throughout:
- **[VERIFIED-DOC]**: read directly in an official questionnaire, codebook, data dictionary, or methodology report.
- **[VERIFIED-LIT]**: read in a peer-reviewed abstract or full text.
- **[SEARCH-SUMMARY]**: comes only from a search-engine summary. The page itself was not opened.
- **[INFERRED]**: my reasoning, not stated by a source.

Searches ran on 2026-11-01 and used PubMed E-utilities, Europe PMC, PMC full text, official PDFs from UCLA, Census and CDC, and web search.

---

## Key Question 1: California Health Interview Survey (CHIS). Which years have adult ACE items, what items and formats, which languages, is interview language in the PUF, how many non-English ACE respondents, any psychometric work, and are nativity, years in US and English proficiency available?

### Takeaway
CHIS is the strongest replication dataset found. It asked adults the 11 BRFSS ACE items with the same wording (plus 4 extra adversity items) in 2021, 2022, 2023 and 2024. It runs in English, Spanish, Chinese (Mandarin and Cantonese), Korean, Vietnamese and Tagalog. The free 2021 adult public-use file (PUF) contains a collapsed interview-language variable, `INTVLNGC_P1` (English / Spanish / Other), alongside nativity, years in the US, percent of life in the US, English proficiency, home language and citizenship. That lets interview language be separated from nativity and acculturation, which BRFSS cannot do.

There are two main limits. First, the three sexual-abuse items (AQ9–AQ11) are not released individually in the PUF, only as part of summary scores. Second, the detailed language variable (`INTVLANG`) appears to be restricted to the Data Access Center (DAC). I found no published psychometric or invariance work on the CHIS ACE items.

### Cited Findings

**Years and placement**
- "Adverse childhood experiences (ACEs), past ACEs assessment, importance of ACEs, positive childhood experiences" appear under "New Adult Questionnaire Topics in 2021-2022". They carry footnotes 1, 2 and 3: available in the PUF, available in AskCHIS, and some content confidential/DAC only. Data were collected March 2021–November 2022, and about 90% of adult interviews were completed on the web. [VERIFIED-DOC] — [CHIS What's New 2021-2022](https://healthpolicy.ucla.edu/sites/default/files/2023-09/whatsnewchis2021-2022_final_09182023.pdf)
- The CHIS 2023 adult questionnaire retains "Section Q: Adverse Childhood Experiences" with AQ1–AQ15 (as QA23_Q8–QA23_Q22). It adds AQ30 (an adult made you feel safe and protected) and AQ31 (an adult tried hard to meet your basic needs), each on a 5-point Never…All of the time scale. The positive-childhood-experience items AQ16–AQ22 from 2021 are not in the 2023 section. [VERIFIED-DOC] — [CHIS 2023 Adult CAWI Questionnaire v3.06](https://healthpolicy.ucla.edu/sites/default/files/2024-11/chis-2023-cawi-v.3.06-14nov2024-adult-questionnaire_clean.pdf)
- New in CHIS 2023: "Adverse Childhood Experiences (ACEs) awareness" and "Provider discussed strengths, resilience during ACEs assessment". [VERIFIED-DOC] — [CHIS What's New 2023](https://healthpolicy.ucla.edu/sites/default/files/2024-09/whatsnewchis2023_v4_09062024.pdf)
- The CHIS 2024 Spanish web questionnaire contains the ACE block ("Antes de los 18 años de edad...", "experiencias adversas de la infancia"). So the items continued into 2024. [VERIFIED-DOC] — [CHIS 2024 Spanish CAWI Adult Questionnaire](https://healthpolicy.ucla.edu/sites/default/files/2024-09/chis-2024-spanish-cawi-v.3.01-23aug2024-adult-questionnaire_clean.pdf)
- Order change between years: in 2021 the ACE screener (AQ1–AQ15) came first and the "past ACEs assessment" questions (AQ23–AQ25) came after. In 2023 an ACE definition, an awareness item ("Have you heard the term Adverse Childhood Experiences or ACEs before?", AQ28) and the assessment items come *before* the ACE screener. [VERIFIED-DOC] — [CHIS 2021 Adult Questionnaire with Q names](https://healthpolicy.ucla.edu/sites/default/files/2024-11/chis-2021-cati-v1.34-5nov2024-adult-questionnaire-q-names.pdf); [CHIS 2023 Adult CAWI](https://healthpolicy.ucla.edu/sites/default/files/2024-11/chis-2023-cawi-v.3.06-14nov2024-adult-questionnaire_clean.pdf)

**Exact items and response formats (CHIS 2021, QA21_Q1–Q15, PUF names AQ1–AQ15)** [VERIFIED-DOC] — [CHIS 2021 Adult Questionnaire](https://healthpolicy.ucla.edu/sites/default/files/2024-11/chis-2021-cati-v1.34-5nov2024-adult-questionnaire-q-names.pdf)
- Stem: "Before you were 18 years of age..."
- Yes/No items:
  - AQ1: lived with anyone depressed, mentally ill, or suicidal
  - AQ2: lived with a problem drinker or alcoholic
  - AQ3: lived with anyone who used illegal street drugs or abused prescription medications
  - AQ4: lived with anyone who served time or was sentenced to serve time in prison, jail or another correctional facility
- AQ5: parents separated or divorced (Yes / No / Parents not married).
- Never/Once/More than once items:
  - AQ6: parents or adults in your home slapped, hit, kicked, punched or beat each other up
  - AQ7: a parent or adult hit, beat, kicked or physically hurt you; "Do not include spanking"
  - AQ8: swore at you, insulted you, or put you down
  - AQ9: anyone at least 5 years older than you, or an adult, touched you sexually
  - AQ10: tried to make you touch them sexually
  - AQ11: forced you to have sex
- AQ1–AQ11 match the wording of the 2009–2020 BRFSS ACE module.
- Items beyond BRFSS:
  - AQ12: victim of or witness to neighborhood violence (Y/N)
  - AQ13: treated or judged unfairly because of race or ethnic group (Y/N)
  - AQ14: lived with a parent or guardian who died (Y/N)
  - AQ15: how often it was very hard to get by on family income (very often / somewhat often / not very often / never)
- The questionnaire lets respondents refuse or answer "don't know" on every item (-7 / -8).
- The PUF dictionary note for the derived scale `ACE_A` reads: "11 POINT ACE SCALE MIRRORS 2009-2020 BRFSS ACE MODULE" (input variables AQ1–AQ11). `ACE8` "COMBINES TWO ACE MODULE QUESTIONS ON HOUSEHOLD SUBSTANCE ABUSE INTO ONE ITEM AND THREE ACE MODULE QUESTIONS ON SEXUAL ABUSE INTO ONE ITEM." [VERIFIED-DOC] — [CHIS 2021 Adult PUF Data Dictionary (Oct 2022)](https://healthpolicy.ucla.edu/sites/default/files/2023-08/chis-2021-data-dictionary-adult-oct-2022.pdf)
- Unweighted 2021 PUF distribution of `ACE_A`: 0 ACEs 8,154 (33.35%); 1 ACE 4,925 (20.14%); 2 ACEs 3,453 (14.12%); 3 ACEs 2,668 (10.91%); 4+ ACEs 5,253 (21.48%). Universe: all adults (n = 24,453). [VERIFIED-DOC] — [CHIS 2021 Adult PUF Data Dictionary](https://healthpolicy.ucla.edu/sites/default/files/2023-08/chis-2021-data-dictionary-adult-oct-2022.pdf)
- The Spanish wording is an independent CHIS translation, not BRFSS's. Example, AQ1: "¿Vivió con alguien que estaba deprimido/a, era enfermo/a mental o suicida?" AQ2: "¿Vivió con alguien que era un/a bebedora problemática o era alcohólico/a?" [VERIFIED-DOC] — [CHIS 2023 Spanish CATI Adult Questionnaire](https://healthpolicy.ucla.edu/sites/default/files/2024-09/chis-2023-spanish-cati-v.3.01-21aug2024-adult-questionnaire_clean.pdf)

**What is and is not in the PUF**
- The 2021 PUF dictionary lists AQ1–AQ8 and AQ12–AQ27 as individual variables. **AQ9, AQ10 and AQ11 (sexual abuse) appear only as inputs to `ACE_A` and `ACE8`**, not as standalone variables. [VERIFIED-DOC] — [CHIS 2021 Adult PUF Data Dictionary](https://healthpolicy.ucla.edu/sites/default/files/2023-08/chis-2021-data-dictionary-adult-oct-2022.pdf). This is consistent with footnote 3 ("Confidential data only available through the Data Access Center") on the ACE topic. [VERIFIED-DOC] — [CHIS What's New 2021-2022](https://healthpolicy.ucla.edu/sites/default/files/2023-09/whatsnewchis2021-2022_final_09182023.pdf)
- In the PUF, item-level ACE variables have no missing categories. For example, AQ7 is Never 19,110 / Once 1,431 / More than once 3,912, which sums to all 24,453 adults, even though the questionnaire offered refused and don't-know options. [VERIFIED-DOC] — [CHIS 2021 Adult PUF Data Dictionary](https://healthpolicy.ucla.edu/sites/default/files/2023-08/chis-2021-data-dictionary-adult-oct-2022.pdf)

**Interview-language variable**
- **2021 adult PUF: `INTVLNGC_P1`, "LANGUAGE OF INTERVIEW (PUF 1 YR RECODE)"**: 1 = English 22,606 (92.45%); 2 = Spanish 1,116 (4.56%); 3 = Other language 731 (2.99%). Universe: all adults. Input variable: `INTVLANG`. Note: "INTVLANG Categories Collapsed." [VERIFIED-DOC] — [CHIS 2021 Adult PUF Data Dictionary](https://healthpolicy.ucla.edu/sites/default/files/2023-08/chis-2021-data-dictionary-adult-oct-2022.pdf)
- The 2022 teen PUF dictionary reportedly lists `INTVLNGT_P1` (language of interview, PUF 1-year recode). The 2022 adult PUF dictionary (Feb 2025 version) is a login-protected file and I could not open it. [SEARCH-SUMMARY] — [CHIS 2022 Teen PUF Data Dictionary](https://healthpolicy.ucla.edu/sites/default/files/protected/chis-2022-data-dictionary-puf-teen-oct-2023.pdf); [CHIS 2022 Adult PUF Data Dictionary (protected)](https://healthpolicy.ucla.edu/sites/default/files/protected/chis-2022-data-dictionary-adult-puf-feb-2025.pdf)
- Historical precedent: the CHIS 2005 adult PUF released the full `INTVLANG` (English 38,476; Spanish 3,141; Vietnamese 371; Korean 430; Cantonese 269; Mandarin 333). Recent PUFs release only the collapsed recode. [VERIFIED-DOC] — [CHIS 2005 Adult PUF Data Dictionary](https://faculty.washington.edu/tlumley/old-svybook/CHIS_PUF_dictionary.pdf)

**Languages and sample sizes by language**
- 2021-2022 instruments were administered in "English, Spanish, Chinese (Mandarin and Cantonese dialects), Vietnamese, Korean, and Tagalog", and translations were adjudicated by language teams. [VERIFIED-DOC] — [CHIS 2021-2022 Methodology Report 2: Data Collection](https://healthpolicy.ucla.edu/sites/default/files/2023-09/chis_2021_2022_methodologyreport2_datacollection_final_09112023.pdf)
- Adult extended interviews in 2021-2022, all sample types, from Table 6-12 (counts with CATI / CAWI split) [VERIFIED-DOC] — [CHIS 2021-2022 Methodology Report 2](https://healthpolicy.ucla.edu/sites/default/files/2023-09/chis_2021_2022_methodologyreport2_datacollection_final_09112023.pdf):

| Language | Total | CATI | CAWI |
|---|---|---|---|
| English | 42,593 | 3,742 | 38,851 |
| Spanish | 2,154 | 645 | 1,509 |
| Chinese | 785 | 112 | 673 |
| Korean | 471 | 61 | 410 |
| Vietnamese | 204 | 78 | 126 |
| Tagalog | 14 | 3 | 11 |

- Internal inconsistencies in that report:
  - The narrative says "981 adult interviews … were conducted in Spanish, which was 4.7 percent", but Table 6-10 shows 1,633 Spanish interviews in the main-sample subtotal.
  - The narrative says "No adult interviews were administered in Tagalog", yet Table 6-12 lists 14.
  - The report also says "Nearly 8 percent of the adult interviews were completed in a language other than English."

  [VERIFIED-DOC] — [CHIS 2021-2022 Methodology Report 2](https://healthpolicy.ucla.edu/sites/default/files/2023-09/chis_2021_2022_methodologyreport2_datacollection_final_09112023.pdf)
- Spanish interviews were most concentrated in Imperial County (25.5% of the stratum's adult interviews) and in the prepaid-cell (28.3%) and MLK (23.0%) oversamples. [VERIFIED-DOC] — same source.
- The CHIS 2023 PUF contains 1,493 variables and is a free SAS/Stata download. The survey is conducted in English, Spanish, Chinese (Cantonese and Mandarin), Korean, Vietnamese and Tagalog. [VERIFIED-DOC] — [CHIS Data Release Oct 2024 slides](https://healthpolicy.ucla.edu/sites/default/files/2024-10/chis-data-release-october-2024.pdf)

**Nativity, acculturation and language covariates in the 2021 adult PUF** [VERIFIED-DOC] — [CHIS 2021 Adult PUF Data Dictionary](https://healthpolicy.ucla.edu/sites/default/files/2023-08/chis-2021-data-dictionary-adult-oct-2022.pdf)
- `AH33NEW` born in US: 18,122 born in US; 6,331 born outside the US.
- `AH34NEW` / `AH35NEW`: mother / father born in US.
- `YRUS_P1`: years lived in US (collapsed categories).
- `PCTLF_P`: percent of life lived in US (0–20 … 81+).
- `CITIZEN2`: citizenship status (3 levels).
- `AH37`: English proficiency (very well / well / not well / not at all). Universe: adults who speak another language at home and/or were interviewed in a non-English language.
- `SPK_ENG`: English use and proficiency (speaks only English 16,283; very well/well 6,902; not well/not at all 1,268).
- `LNGHM_P1`: language spoken at home. Codes include Spanish-only 882, English & Spanish 3,340, Chinese 584, Vietnamese 200 and Korean 196.
- `SRAGE_P1`: age.
- The 2021–2023 revision errata also reference `LANGHOME`, `LNGHMC_P1` and `CH17*`. [VERIFIED-DOC] — [CHIS 2021–2023 Data Revisions Errata (Feb 2025)](https://healthpolicy.ucla.edu/sites/default/files/2025-02/2021-2023-chis-data-revisions_errata_02272025.pdf)

**Published CHIS ACE work. None is psychometric or invariance-focused** [VERIFIED-LIT]
- PubMed ("California Health Interview Survey" AND ACE) returned 8 papers, all substantive association studies:
  - [Kotz et al. 2026, Fam Med Community Health](https://pubmed.ncbi.nlm.nih.gov/42628986/): 2021 CHIS, n = 24,453; ACEs, PCEs and adult factors.
  - [Chwa et al. 2026, J Immigr Minor Health](https://pubmed.ncbi.nlm.nih.gov/41709070/): 2021 CHIS, Asian Americans n = 4,345. English proficiency and US-born used as covariates.
  - [Haro-Ramos et al. 2026, Prev Med Rep](https://pubmed.ncbi.nlm.nih.gov/41631104/): 2021–2022 CHIS, Latinos aged 50+, n = 5,493. The relative ACE–self-rated-health association was smaller among immigrant Latinos than US-born Latinos.
  - [Jang & Gonzales 2025, JGIM](https://pubmed.ncbi.nlm.nih.gov/39482476/): 2021–2022 CHIS, 5,744 Asian Americans, "Fifteen different ACEs". 65.4% of second-generation vs 47.5% of first-generation reported 1+ ACE.
  - [Alcalá 2024, JABFM](https://pubmed.ncbi.nlm.nih.gov/38272536/): ACE screening disparities.
  - [Pereira et al. 2025, SSM Pop Health](https://pubmed.ncbi.nlm.nih.gov/40386444/)
- No CHIS paper tested measurement invariance or DIF of the ACE items by language, nativity or anything else.

### Inferences
- [INFERRED] CHIS lets a BRFSS language-DIF result be replicated with the **same English items but a different, independent Spanish translation**. If the same items show DIF in both surveys, that points to language or culture rather than one translation's wording. DIF in only one survey points to translation.
- [INFERRED] Because the PUF has nativity, years in US, percent of life in US, home language and English proficiency, a CHIS model can test whether "Spanish interview" DIF survives conditioning on nativity and acculturation. Latinos who are foreign-born and interviewed in English, versus US-born and interviewed in Spanish, give partial deconfounding. This is the main advantage over BRFSS, which has no nativity variable in its core.
- [INFERRED] Expected PUF sample for a Spanish-vs-English contrast: about 1,000–1,100 Spanish-interview adults per year (2021 PUF: 1,116). Pooling 2021–2024 would give roughly 4,000+ Spanish-interview ACE respondents. 2023 and 2024 language counts were not retrieved, so this is an extrapolation.
- [INFERRED] Asian-language DIF (Chinese, Korean, Vietnamese) needs the DAC because the PUF collapses them into "Other". Combined across 2021–2022 there are about 785 Chinese, 471 Korean and 204 Vietnamese interviews; Tagalog (n = 14) is unusable.
- [INFERRED] Gaps in the PUF matter for a full 11-item replication:
  1. **The sexual-abuse items (AQ9–AQ11) are DAC-only.** A PUF analysis would cover 8 items plus the AQ12–AQ15 extras.
  2. **Missing ACE responses appear to have been filled in the PUF**, most likely by CHIS's standard hot-deck imputation. That would change DK/refusal patterns, which are themselves a language-DIF signal. The DAC is needed for raw item nonresponse and imputation flags.
- [INFERRED] CHIS is about 90% self-administered web (CAWI), while BRFSS uses telephone interviewers. The 645 Spanish CATI and 1,509 Spanish CAWI interviews in 2021-2022 allow a language × mode check that BRFSS cannot provide. Mode differences also mean CHIS is a "conceptual" rather than "exact" replication of BRFSS.
- [INFERRED] The 2023 order change (ACE awareness and assessment items placed before the screener) is a context effect to account for, or test, when pooling 2021–2022 with 2023+.

### Gaps
- I could not open the 2022, 2023 or 2024 adult PUF dictionaries (2022 is login-protected), so I have not confirmed that `INTVLNGC_P1` (or an equivalent) and the ACE variables are in every later PUF, or that AQ9–AQ11 remain DAC-only.
- I did not retrieve the exact DAC variable list or access terms (fees; remote vs on-site) for the uncollapsed `INTVLANG` and the sexual-abuse items.
- I did not obtain counts of ACE respondents by interview language for 2023 or 2024.
- I did not verify the CHIS imputation method for ACE items or whether imputation flags are released.
- I did not compare the CHIS Spanish ACE wording with the BRFSS Spanish module wording.

---

## Key Question 2: National Survey of Children's Health (NSCH). Is it in Spanish, does the public file have language of response or household language, and is there published DIF/invariance work by language or Hispanic subgroup?

### Takeaway
NSCH is fielded in English and Spanish (web and paper), but the public file has **no language-of-response variable**. It has only `HHLANGUAGE` (primary household language from the screener). The web instrument also lets respondents toggle languages on every page. The only published ACE invariance work found is Jensen, Bernard & Lanier (2024), which tested race/ethnicity groups, including Hispanic children as one group, not language. NSCH ACEs are parent-reported child ACEs, a different construct from adult retrospective self-report.

### Cited Findings
- "The NSCH paper and web instruments were available in both English and Spanish." Respondents could request a Spanish questionnaire, and about 40 interviews were completed with an agent using the Spanish web instrument. "The web instrument included a toggle on every page that allowed respondents to switch between the English and Spanish-language versions of the instrument." An operational disposition code "Spanish questionnaire completed" exists in the methodology documentation. [VERIFIED-DOC] — [2024 NSCH Methodology Report](https://www2.census.gov/programs-surveys/nsch/technical-documentation/methodology/2024-NSCH-Methodology-Report.pdf)
- 2024 topical public-use variable list:
  - `HHLANGUAGE`, "Primary Household Language (S1)": "What is the primary language spoken in the household?" with 2 = Spanish. No other language-of-response variable appears.
  - Nativity and immigration variables: `A1_BORN`, `A2_BORN` (where caregiver born), `BORNUSA` (child born in US), `LIVEUSA_YR` / `LIVEUSA_MO` (how long the child has lived in US), and `HOUSE_GEN` (1st / 2nd / 3rd+ generation household).
  - Also `SC_HISPANIC_R`.

  [VERIFIED-DOC] — [2024 NSCH Topical Variable List](https://www2.census.gov/programs-surveys/nsch/technical-documentation/codebook/2024-NSCH-Topical-Variable-List.pdf)
- 2024 unweighted `HHLANGUAGE`: English 46,724 (90.9%); Spanish 2,408 (4.7%; weighted 11.9%); Other 1,988 (3.9%); no valid response 255. [VERIFIED-DOC] — [NSCH 2024 Topical Frequencies](https://www2.census.gov/programs-surveys/nsch/technical-documentation/codebook/NSCH_2024_Topical_Frequencies.pdf)
- 2024 NSCH ACE items (asked of all form types T1/T2/T3):
  - ACE1: since child was born, how often hard to cover basics like food or housing (Never / Rarely / Somewhat often / Very often).
  - Yes/No "To the best of your knowledge, has this child EVER experienced…" items:
    - ACE3: parent or guardian divorced/separated
    - ACE4: parent or guardian died
    - ACE5: parent or guardian served time in jail or prison
    - ACE6: saw or heard adults slap, hit, kick, punch one another in the home
    - ACE7: victim of or witness to neighborhood violence
    - ACE8: lived with anyone mentally ill, suicidal or severely depressed
    - ACE9: lived with anyone with an alcohol or drug problem
    - ACE10: treated unfairly because of race/ethnic group
    - ACE11: treated unfairly because of a health condition or disability
  - There are no abuse or neglect items.

  [VERIFIED-DOC] — [2024 NSCH Topical Variable List](https://www2.census.gov/programs-surveys/nsch/technical-documentation/codebook/2024-NSCH-Topical-Variable-List.pdf)
- Jensen, Bernard & Lanier (2024, *Child Development*) used 2018–2020 NSCH (N = 93,759) across Hispanic (14%), White, Black, Asian/Pacific Islander and AI/AN children. They found configural and full metric invariance, "However, several ACE item thresholds differed across groups." [VERIFIED-LIT] — [Jensen et al. 2024](https://pubmed.ncbi.nlm.nih.gov/38037724/)
- Europe PMC search ("National Survey of Children's Health" AND "adverse childhood" AND DIF / measurement invariance) returned only Jensen 2024 plus two unrelated or LCA papers, e.g. [Zhang & Monnat 2022, racial/ethnic ACE clusters](https://pubmed.ncbi.nlm.nih.gov/34984220/). I found no NSCH ACE DIF study by language or by Hispanic heritage subgroup. [VERIFIED-LIT, search result]
- Brown & Anda (2026) published a "synthetic imputation" of abuse items for NSCH, which addresses the missing abuse domain, not invariance. [VERIFIED-LIT, title only] — [Brown & Anda 2026](https://pubmed.ncbi.nlm.nih.gov/42792451/)

### Inferences
- [INFERRED] NSCH can support a **household-language** invariance analysis: Spanish-primary-language vs English households among Hispanic children, about 2,400 Spanish households per year, pooled across years. Because of the web language toggle and the lack of a response-language flag, it cannot separate interview language from household language. It therefore answers a different question (cultural/linguistic household context) and tests parent-proxy items.
- [INFERRED] NSCH's `HOUSE_GEN` and parent-nativity variables allow a Hispanic-subgroup or generation analysis that partly mirrors the CHIS acculturation design. Jensen's threshold non-invariance finding is the closest published precedent for an "intercept/threshold DIF" hypothesis in a language study.
- [INFERRED] The NSCH household-dysfunction items share content and near-identical wording with BRFSS/CHIS items: ACE6 ↔ BRFSS adults hitting each other, ACE8 ↔ mental illness, ACE9 ↔ substance use, ACE5 ↔ incarceration, ACE1 ↔ CHIS AQ15. A cross-survey comparison of whether the *same household items* show language-related threshold shifts is feasible. Respondent (parent vs self) and recall period differ.

### Gaps
- I did not check whether a restricted-use NSCH file (Census RDC) contains the questionnaire-language disposition flag.
- I did not verify `HHLANGUAGE` coding across all years 2016–2025, though the variable list naming suggests continuity.

---

## Key Question 3: Other datasets with ACE or childhood-adversity items, substantial Spanish-language interviews, and nativity/acculturation measures (HCHS/SOL SCAS, NLAAS, NESARC-III, Add Health, NSFG, MIDUS, MHAS, Puerto Rico BRFSS)

### Takeaway
- **HCHS/SOL's Sociocultural Ancillary Study (SCAS)** is the best Hispanic-only option. About 5,200 adults have the original 10-item Felitti ACE scale, about 75% preferred a Spanish interview, and it has rich acculturation and nativity data. Published invariance work exists across Hispanic heritage groups but not by language.
- **NLAAS** has a unique **randomized language experiment** (bilingual Latinos randomly assigned a Spanish or English interview, n = 332). Its childhood-adversity item content needs verification.
- **NESARC-III** has ACE items and many immigrants, but I could not verify its interview languages or language variable.
- **Add Health** records interview language, but Spanish interviews were rare and retrospective maltreatment items come from adult waves.
- For NSFG, MIDUS, MHAS and Puerto Rico BRFSS I could not verify usable ACE-plus-language data in this session.

### Cited Findings

**HCHS/SOL Sociocultural Ancillary Study (SCAS)**
- The ACE measure is "the original ACE scale (Felitti et al., 1998)". "A total score was calculated by summing the number of events experienced ranging from 0 to 10." It was collected at Visit 1 (2008–2011), and 5,230 participants have ACE data. Covariates include "years in the U.S. (continuous), nativity (i.e., U.S. born or not U.S. born), language preference (Spanish or English)", and Hispanic/Latino background. The CES-D-10 reliability is reported for both English and Spanish. [VERIFIED-LIT] — [Kobayashi et al. 2024, Health Psychology (PMC full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12004413/)
- In SCAS (n = 5,154), "Most adults (78.1%) were born outside of the US and preferred Spanish (75.4%)." The stress–COPD relationship "was significantly stronger among Hispanic/Latino adults who preferred to be interviewed in Spanish (compared to English)". Models control for social acculturation (SASH social subscale), years in US and background. [VERIFIED-LIT] — [Gianola et al. 2023, Med Res Arch (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11156427/)
- Cooper & Nickodem (2021) fitted a five-factor bifactor model of "cumulative lifetime adversity", which includes ACEs among other components, in SCAS foreign-born participants (N = 3,296). "Multigroup confirmatory factor analyses suggested that the measurement model functioned similarly across Hispanic/Latino subgroups" (Mexican, Cuban, Puerto Rican, Dominican, Central American, South American). They did not test invariance by language. [VERIFIED-LIT] — [Cooper & Nickodem 2021](https://pubmed.ncbi.nlm.nih.gov/32166975/)
- Other SCAS ACE papers:
  - [Chen et al. 2025](https://pubmed.ncbi.nlm.nih.gov/39883977/): ACE → epigenetic aging, with weaker associations among foreign- or territory-born participants than US-born.
  - [Niño et al. 2023](https://pubmed.ncbi.nlm.nih.gov/37223581/): latent classes of ACEs.
  - [Cooper et al. 2021, PLoS One](https://pubmed.ncbi.nlm.nih.gov/34662358/): Puerto Ricans vs Mexican immigrants.

  [VERIFIED-LIT]
- Access: HCHS/SOL data are typically obtained through the HCHS/SOL Coordinating Center (manuscript proposal) or NHLBI BioLINCC. [INFERRED; I did not open the access pages, so verify at https://sites.cscc.unc.edu/hchs/ and BioLINCC.]

**NLAAS (National Latino and Asian American Study, 2002–2003; part of CPES)**
- The interview was offered in English, Spanish, Chinese, Vietnamese or Tagalog. The final sample was 2,554 Latino and 2,095 Asian American respondents. Public data are ICPSR 20240 (CPES). The questionnaire documents include a "Language of Interview" module and Childhood Demographics, Conduct Disorder and Migration modules. [SEARCH-SUMMARY] — [Mongan Institute NLAAS documents](https://www.massgeneral.org/mongan-institute/centers/dru/research/past/nlaas-docs); [GHDx NLAAS record](https://ghdx.healthdata.org/node/13364)
- "Bilingual respondents from the Latino section of the NLAAS (n = 332) were randomly assigned to receive either a Spanish- or English-language version" of the WMH-CIDI. Only one of 15 diagnostic comparisons differed (lifetime GAD was more prevalent in the English-assigned group). The authors conclude: "Translation and back-translation of surveys does not guarantee that response probabilities are exactly equivalent. Randomized survey experiments should be incorporated…" [VERIFIED-LIT] — [Shrout, Alegría, Canino et al. 2008, AJE](https://pubmed.ncbi.nlm.nih.gov/18550562/)
- NLAAS has been used for childhood-abuse analyses among Latinos. [VERIFIED-LIT, titles only] — [Ai et al. 2016](https://pubmed.ncbi.nlm.nih.gov/27098665/); [Ai et al. 2018](https://pubmed.ncbi.nlm.nih.gov/29624121/)

**NESARC-III (2012–2013)**
- 6,131 adult immigrants in NESARC-III, with childhood and recent adversities analysed by latent class. "Neglect was the most commonly-reported childhood adversity among immigrant men and women." [VERIFIED-LIT] — [Cano & Takeuchi 2020](https://pubmed.ncbi.nlm.nih.gov/33312137/)
- NESARC-III ACE items exist (e.g., swore at or insulted you), and the total NESARC-III sample is 36,309. [SEARCH-SUMMARY] — [CDC Stacks appendix listing NESARC-III ACE items](https://stacks.cdc.gov/view/cdc/88397/cdc_88397_DS5.docx). Recent Hispanic-focused work: [Espinosa 2026](https://pubmed.ncbi.nlm.nih.gov/40167978/).
- I found nothing in this session confirming that NESARC-III interviews were conducted in Spanish or that a language variable is released. Access is through an NIAAA data-use application (from background knowledge; not verified here).

**Add Health**
- The Add Health Navigator lists "LANGUAGE OF INTERVIEW" items. Wave I recorded 444 Spanish-language interviews (about 2.14%) and Wave II 24 (about 0.16%). [SEARCH-SUMMARY] — [Add Health Navigator: Language of interview W1](https://addhealth-navigator.cpc.unc.edu/item/example.org/61ea5aab-d067-4f5e-8d0a-a58aab158e01); [W2](https://addhealth-navigator.cpc.unc.edu/item/example.org/c1d04095-98b8-4e37-9adb-c2dcf6aa260d)
- Add Health childhood-abuse analyses exist (e.g., [Simpson 2026](https://pubmed.ncbi.nlm.nih.gov/42703219/)). [VERIFIED-LIT, title only]

**Health and Retirement Study (HRS), not on the original list**
- HRS includes retrospective childhood trauma items, such as childhood physical abuse and parental substance abuse, and has many Hispanic respondents. [SEARCH-SUMMARY] — [HRS bibliography entry](https://hrs.isr.umich.edu/bibcite/reference/15600). HRS Hispanic/ACE papers exist (e.g., [Walters 2026](https://pubmed.ncbi.nlm.nih.gov/42083879/); [García 2026](https://pubmed.ncbi.nlm.nih.gov/41701154/)). [VERIFIED-LIT, titles only] I did not verify the HRS interview-language variable or whether the trauma items are fielded in Spanish.

**NSFG, MIDUS, MHAS, Puerto Rico BRFSS**
- I did not verify any of these with documentation in this session:
  - NSFG: retrieved no ACE-module evidence.
  - MIDUS: retrieved no Spanish-administration evidence.
  - MHAS: no documentation retrieved.
  - Puerto Rico BRFSS: a targeted search found no BRFSS-based Puerto Rico ACE estimate. The closest island data come from the Boricua Youth Study, a research cohort using an adapted ACE questionnaire with 8 overlapping items. [SEARCH-SUMMARY] — [ACEs and sleep among Puerto Rican young adults (PMC11036138)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11036138/)

### Inferences
- [INFERRED] HCHS/SOL SCAS is the best within-Hispanic replication of Spanish-vs-English DIF:
  - large Spanish-preferring share (about 75%)
  - nativity, years in US and SASH acculturation
  - heritage-group variety
  - an ACE scale that includes emotional and physical neglect

  Limits: it has the original Felitti wording (not BRFSS wording, and yes/no rather than Never/Once/More than once), no non-Hispanic comparison group, data from 2008–2011, and controlled access. A Cooper-style MGCFA could be re-run by language preference.
- [INFERRED] The NLAAS randomized-language subsample is the only design found that separates *language* from *person* experimentally. If childhood-adversity questions were in the randomized instrument and the assignment flag is in the CPES public file, even n = 332 would give a causal check on language effects for adversity items. Both conditions are unverified.
- [INFERRED] NESARC-III could be strong (large n, ACE items, many immigrants, likely Spanish interviews) if a language variable exists. This is the first item to verify in the NESARC-III codebook.
- [INFERRED] Add Health is weak for this question. Retrospective maltreatment items are in the adult waves (III–V), when Spanish interviews were likely negligible, so it cannot replicate interview-language DIF.
- [INFERRED] Spanish-only surveys (MHAS in Mexico; Puerto Rico BRFSS, which I believe is mostly Spanish-language) give no within-survey language contrast. Language would be confounded with country or territory context. At most they serve as external Spanish-language benchmarks.

### Gaps
- I did not verify HCHS/SOL SCAS ACE item wording, its Spanish translation, or the exact data-access route and variable name for interview-language preference.
- I did not verify whether NLAAS childhood-adversity items were in the randomized-language portion, or whether the randomization indicator is public (ICPSR 20240).
- I did not verify NESARC-III interview languages or a language variable.
- I did not verify which childhood-adversity items, interview-language variable and Spanish administration exist for HRS, NSFG, MIDUS or MHAS.
- I did not verify whether Puerto Rico fielded the BRFSS ACE module in any year, which would need the CDC module-by-state tables.

---

## Key Question 4: YRBS 2023. Exact ACE items, psychometric/invariance studies 2024–2026, the "38.6% vs 18.5%" LGBTQ+ figure, which ACE items 2025 kept, and whether a Spanish version exists

### Takeaway
2023 YRBS added eight self-reported ACE items.
- I found no factor-analytic, IRT or DIF study of them. The nearest is a 2026 Ising network analysis that tested *network* invariance by sex, sexual orientation and race/ethnicity.
- **The "38.6% vs 18.5%" figure is mis-specified.** In the CDC MMWR, 38.6% is 4+ ACEs among students who "describe their identity in some other way" (one LGBQ+ subgroup), and 18.5% is the *total* student population. Heterosexual students were 13.3%.
- **The 2025 national YRBS kept only 3 of the 8 ACE items** (emotional abuse, physical abuse, basic needs), all in the national-only section, and dropped sexual abuse and all household items.
- The national YRBS is administered in English and Spanish, but the public data guide has no questionnaire-language variable.

### Cited Findings
- **2023 ACE items and coding** [VERIFIED-LIT] — [Swedo et al. 2024, MMWR Suppl 73(4) (PMC full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11559682/):

| ACE | Question | Response options | Coded as "yes" |
|---|---|---|---|
| Emotional abuse | "During your life, how often has a parent or other adult in your home insulted you or put you down?" | Never, rarely, sometimes, most of the time, always | rarely or more vs never |
| Physical abuse | "…hit, beat, kicked, or physically hurt you in any way?" | Same 5-point scale | rarely or more vs never |
| Sexual abuse | "Has an adult or person at least 5 years older than you ever forced you to do sexual things that you did not want to do? (Count such things as kissing, touching, or being made to have sexual intercourse.)" | Yes/No | Yes |
| Physical neglect | "…how often has there been an adult in your household who tried hard to make sure your basic needs were met…?" | Same 5-point scale | **never or rarely** (reverse-coded) |
| Witnessed IPV | "…parents or other adults in your home slapped, hit, kicked, punched, or beat each other up?" | Same 5-point scale | rarely or more vs never |
| Household substance use | "Have you ever lived with a parent or guardian who was having a problem with alcohol or drug use?" | Yes/No | Yes |
| Household poor mental health | lived with a parent or guardian with "severe depression, anxiety, or another mental illness, or was suicidal" | Yes/No | Yes |
| Incarcerated parent | "separated from a parent or guardian because they went to jail, prison, or a detention center" | Yes/No | Yes |

  The cumulative count runs 0–8. The analysis was restricted to students under 18.
- Headline results: 76.1% had 1+ ACE and 18.5% had 4+. Emotional abuse was 61.5%, physical abuse 31.8% and household poor mental health 28.4%. [VERIFIED-LIT] — [Swedo et al. 2024](https://pubmed.ncbi.nlm.nih.gov/39378222/)
- **Table 3, 4+ ACEs by sexual identity** (weighted %, 95% CI) [VERIFIED-LIT] — [Swedo et al. 2024, Table 3](https://pmc.ncbi.nlm.nih.gov/articles/PMC11559682/):

| Sexual identity | 4+ ACEs |
|---|---|
| Heterosexual | **13.3%** (12.1–14.6) |
| Gay or lesbian | 25.7% (20.7–31.4) |
| Bisexual | 35.1% (31.7–38.6) |
| Questioning | 26.3% (21.9–31.3) |
| Describe identity in some other way | **38.6%** (29.9–48.2) |
| **Total** | **18.5%** (16.5–20.6) |

  The text says 4+ ACEs prevalence was highest in "LGBQ+ students, particularly students who describe their identity in some other way (38.6%) and bisexual students (35.1%)." Hispanic or Latino students: 19.1%.
- Mittleman (2025, AJPH) used the 2023 national YRBS (n = 12,131), screened for mischievous respondents and included gender identity. 4+ ACEs: gender minorities 46.1% (39.7–52.5), cisgender sexual minorities 34.5% (30.9–38.0), cisgender-heterosexual 15.4% (14.2–16.7). Mean ACE score was 3.0 for LGBTQ+ vs 1.8 for cishet students. [VERIFIED-LIT] — [Mittleman 2025](https://pubmed.ncbi.nlm.nih.gov/40340463/)
- The closest psychometric-type work is Díaz-Faes, Rajan & Branas (2026, *Epidemiology*, online Sept 2026). It is an Ising network of 26 items from 2023 YRBS (N = 20,103), including ACEs, with Network Comparison Tests by sex, sexual orientation and race/ethnicity. They report "broadly similar network structure and global strength across sex, sexual orientation, and most racial/ethnic comparisons, with the strongest evidence of structural differences for Black/African American versus White respondents." This is network invariance, not item-level measurement invariance or DIF. [VERIFIED-LIT] — [Díaz-Faes et al. 2026](https://pubmed.ncbi.nlm.nih.gov/42725720/)
- Other 2024–2026 papers on 2023 YRBS ACEs are prevalence or association studies, not psychometric:
  - [Swedo et al. 2026, Inj Prev](https://pubmed.ncbi.nlm.nih.gov/42493237/): 16 jurisdictions; emotional abuse 49.3%–64.0%.
  - [Azagba 2025](https://pubmed.ncbi.nlm.nih.gov/40525333/)
  - [Kim 2026](https://pubmed.ncbi.nlm.nih.gov/41880738/)
  - [Powers 2026](https://pubmed.ncbi.nlm.nih.gov/42699626/)
  - [Harris 2026](https://pubmed.ncbi.nlm.nih.gov/42155625/)

  A Europe PMC full-text query (YRBS AND ACE AND measurement invariance / CFA / IRT / DIF / factor structure / latent class, 2024–2026) returned 9 hits, none of which was a psychometric evaluation of the YRBS ACE items. [VERIFIED-LIT, search result]
- **2025 YRBS.** The national YRBS Data User's Guide (dated September 2026), Appendix B "National High School YRBS Site-Added Questions", lists:
  - **Q88** "During your life, how often has a parent or other adult in your home insulted you or put you down?" (variable label "Insulted at home")
  - **Q89** "…hit, beat, kicked, or physically hurt you in any way?" ("Physically abused at home")
  - **Q99** "…an adult in your household who tried hard to make sure your basic needs were met…" ("Household adult tried hard to meet basic needs ACEs")

  Each uses Never / Rarely / Sometimes / Most of the time / Always. A text search of the whole guide found **no** sexual-abuse ("5 years older"), witnessed-IPV ("slap… each other"), household substance-use, household mental-illness or incarcerated-parent ("jail / detention") ACE items. Sexual identity and transgender (Q63) items are retained. [VERIFIED-DOC] — [2025 YRBS Data User's Guide](https://www.cdc.gov/yrbs/files/2025/2025-YRBS-Data-Users-Guide-Final.pdf)
- The 2025 overview reports:
  - "The 2025 questionnaire contained 106 questions": 86 in the standard questionnaire, the rest national-only.
  - Items are removed under a "one-in, one-out" rule.
  - "the national YRBS questionnaire was administered in both English and Spanish."
  - 10,710 usable questionnaires from 108 schools; overall response rate 30.6% ("the lowest in the survey's history").

  The overview does not discuss ACE items. [VERIFIED-DOC] — [MMWR Suppl 75(1): Overview and Methods for YRBSS, 2025](https://www.cdc.gov/mmwr/volumes/75/su/su7501a1.htm)
- A state-facing "YRBS 2025 Optional Question List" includes an ACE section that sites may add. This is a third-party-hosted document. [SEARCH-SUMMARY] — [YRBS 2025 Optional Question List (upforlearning.org)](https://www.upforlearning.org/wp-content/uploads/2026/04/YRBS-2025-Optional-Question-List.pdf)
- The 2025 Data User's Guide contains no questionnaire-language variable; a text search for "Spanish" and "language" found no hits. [VERIFIED-DOC] — [2025 YRBS Data User's Guide](https://www.cdc.gov/yrbs/files/2025/2025-YRBS-Data-Users-Guide-Final.pdf)

### Inferences
- [INFERRED] The earlier session's claim that "the 2025 YRBS dropped most ACE items" is **confirmed for the national survey**: 5 of 8 dropped, and the 3 survivors sit in the national-only section. Some states and localities may still field more ACE items through the optional list. A "2023 psychometrics" paper would therefore describe a one-time national eight-item measure. The emotional/physical-abuse/neglect sub-battery could be tracked 2023→2025 for longitudinal invariance of those three items only.
- [INFERRED] The LGBTQ+ ACE gap is real in both CDC and Mittleman analyses, but the correct contrast is about **13–15% (heterosexual or cishet) vs 26–46% (sexual/gender-minority subgroups)**, not "38.6% vs 18.5%". Any proposal should cite the subgroup-specific figures.
- [INFERRED] Item-level DIF of the 2023 YRBS ACE items by sexual identity remains an open, publishable gap. Díaz-Faes 2026 covers network structure only. It is low value for a *language* study, because there is no language-of-administration variable and the national sample's Spanish-administered share is unknown.

### Gaps
- I did not retrieve the 2023 YRBS standard vs national questionnaire placement of the 8 ACE items, or whether all 8 were on the standard questionnaire in 2023. The 2026 Inj Prev paper says 16 jurisdictions "included ACEs questions on their survey".
- The number of Spanish-administered 2023 or 2025 national questionnaires is unknown, and no language variable appears to be released.
- I did not see the official 2025 questionnaire PDF on CDC Stacks (stacks.cdc.gov/view/cdc/252280). The verification relies on the 2025 Data User's Guide.

---

## Key Question 5: Birth cohort. Has anyone tested ACE item invariance or DIF by birth cohort or survey era in BRFSS, or done age-period-cohort (APC) analyses of ACE prevalence?

### Takeaway
**The prevalence half of the proposed idea has now been published.** Brown, Anda & Porter (Sept 2026, *Behavioral Sciences*) pooled BRFSS 2009–2012 and 2019–2024 (n = 517,296; 1925–2003 birth cohorts) in an APC model. They found strong cohort increases and a large period ("disclosure") effect. They did **not** test measurement invariance or DIF. Item-level invariance by birth cohort or survey era in BRFSS appears untested. Existing invariance tests cover age within single years (Ford 2014; Mei 2022) and age in a non-BRFSS teacher sample (Rancher 2024).

### Cited Findings
- Brown, Anda & Porter (2026) design:
  - "We pooled Behavioral Risk Factor Surveillance System (BRFSS) data from 2009-2012 and 2019-2024 (1925-2003 birth cohorts) and analyzed them using an Age-Period-Cohort (APC) model."
  - Score restricted to 8 dichotomous ACEs present in all years: physical, emotional and sexual abuse; household substance use, mental illness, incarceration, separation/divorce and IPV. Neglect items added 2021–2024 were excluded.
  - "Constraint-based fixed effects": quadratic age, survey-year fixed effects (2019 reference), categorical cohorts.

  Findings:
  - Early cohorts (circa 1930) had a mean ACE score < 1 (4+ ACEs about 1 in 20); late-1990s/early-2000s cohorts had a mean > 2 (about 1 in 4).
  - The 1955–1979 cohorts had IRR about 1.50 vs pre-1930 cohorts.
  - Period effect: "ACE reporting was ~25% lower in 2009 than in 2019 (IRR = 0.75)", and 2022 was IRR = 1.10 vs 2019.

  Data notes:
  - "of the identified 213 instances where states included the ACE module between 2009 and 2024, 120 were not included in the CDC's public-use data files", including "a complete absence of ACE module data in the national PUF during the years 2013–2018."
  - The full text contains no mention of measurement invariance, DIF, Spanish or interview language.

  [VERIFIED-LIT] — [Brown, Anda & Porter 2026 (PMC13603429)](https://pubmed.ncbi.nlm.nih.gov/42792486/)
- Hartwell et al. (2023) computed mean ACEs by birth year in 2020 BRFSS (n = 116,378): 0.79 among those born ≤1940 vs 2.74 in the 1998 cohort, then an ARIMA forecast. A single cross-section confounds age and cohort. [VERIFIED-LIT] — [Hartwell et al. 2023, J Osteopath Med](https://pubmed.ncbi.nlm.nih.gov/36947857/)
- Ford et al. (2014) ran EFA on 2009 BRFSS and CFA on 2010 BRFSS, with a 3-factor solution (household dysfunction, emotional/physical abuse, sexual abuse). "Measurement invariance was supported across both gender and age." The abstract does **not** mention race, contrary to the background summary's "sex, age, race". [VERIFIED-LIT] — [Ford et al. 2014](https://pubmed.ncbi.nlm.nih.gov/26430532/)
- Mei et al. (2022) used 2019 BRFSS (97,314 respondents, 16 states). The 11-item ACE tool was a second-order factor with three subscales that "passed the measurement invariance tests at metric and scalar levels across age, race, sex, socioeconomic status, gender identity, and sexual orientation". Language was not tested. [VERIFIED-LIT] — [Mei et al. 2022](https://pubmed.ncbi.nlm.nih.gov/36445502/)
- Rancher, Bernard & Moreland (2024) tested the BRFSS 11-item ACE measure among 605 early-childhood teachers (2018–2021). It replicated the three-factor solution, and "Multigroup confirmatory factor analyses demonstrated measurement invariance across teacher age and race." [VERIFIED-LIT] — [Rancher et al. 2024](https://pubmed.ncbi.nlm.nih.gov/38939647/)
- PubMed and Europe PMC searches (ACE AND birth cohort / APC / cohort effect / generational AND BRFSS) returned Brown 2026 and Hartwell 2023 as the only BRFSS cohort analyses. None tested invariance by cohort or era. [VERIFIED-LIT, search results]

### Inferences
- [INFERRED] Idea (3) should be **re-scoped**. The APC prevalence decomposition with exactly the proposed pooling (2009–2012 plus 2019+) is done. What remains open is whether the *items* function the same way across survey eras and cohorts:
  - scalar/threshold invariance 2009–2012 vs 2019–2024
  - item-specific period shifts
  - cohort-by-item DIF that could produce Brown's "disclosure" period effect
- [INFERRED] Brown et al. read the 2009→2019 IRR as "greater disclosure". That is a testable measurement claim. If disclosure drives the effect, the more stigmatized items (emotional abuse, sexual abuse, household mental illness) should show larger threshold shifts by era than "factual" items (divorce, incarceration). An MNLFA or era-DIF model on the pooled BRFSS file would test this directly. It remains a gap and is a natural extension of, or critique of, Brown 2026.
- [INFERRED] Existing age invariance (Ford 2014; Mei 2022; Rancher 2024) was tested within single cross-sections, where age equals cohort. Those results do not speak to period or era invariance.
- [INFERRED] A cohort-by-language interaction could link ideas (1) and (3). Spanish-interview BRFSS respondents are disproportionately foreign-born and older cohorts.

### Gaps
- I did not check the BRFSS module-year list in Brown 2026 Table 1 for Puerto Rico or for which states contribute to each era. Changes in state composition across eras could confound period effects.
- I did not find APC work on ACEs in other US surveys (NSCH, CHIS, NESARC) and did not search exhaustively for dissertations or preprints.

---

## Key Question 6: How do the replication and extension datasets rank for usefulness in a language-invariance study, and why?

### Takeaway
1. CHIS
2. HCHS/SOL SCAS
3. NLAAS (conditional on verification)
4. NSCH
5. NESARC-III (conditional)
6. YRBS
7. Add Health, HRS, NSFG, MIDUS, MHAS, Puerto Rico BRFSS (low or unverified)

### Cited Findings
- CHIS:
  - BRFSS-identical ACE wording (AQ1–AQ11) in 2021–2024
  - a six-language survey
  - a PUF interview-language variable (`INTVLNGC_P1`: English 22,606 / Spanish 1,116 / Other 731 in 2021)
  - PUF nativity, years in US, percent of life in US, English proficiency and home language

  [VERIFIED-DOC] — [CHIS 2021 Adult PUF Data Dictionary](https://healthpolicy.ucla.edu/sites/default/files/2023-08/chis-2021-data-dictionary-adult-oct-2022.pdf); [CHIS 2023 Adult Questionnaire](https://healthpolicy.ucla.edu/sites/default/files/2024-11/chis-2023-cawi-v.3.06-14nov2024-adult-questionnaire_clean.pdf)
- HCHS/SOL SCAS: 10-item ACE, n ≈ 5,230, 75.4% Spanish-preferring, nativity and acculturation measures, invariance across heritage groups already shown. [VERIFIED-LIT] — [Kobayashi 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC12004413/); [Gianola 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC11156427/); [Cooper & Nickodem 2021](https://pubmed.ncbi.nlm.nih.gov/32166975/)
- NLAAS: randomized Spanish/English assignment of 332 bilingual Latinos. [VERIFIED-LIT] — [Shrout et al. 2008](https://pubmed.ncbi.nlm.nih.gov/18550562/)
- NSCH: English/Spanish instruments, but only `HHLANGUAGE` in the PUF and a per-page language toggle. [VERIFIED-DOC] — [2024 NSCH Methodology Report](https://www2.census.gov/programs-surveys/nsch/technical-documentation/methodology/2024-NSCH-Methodology-Report.pdf); [2024 NSCH Topical Variable List](https://www2.census.gov/programs-surveys/nsch/technical-documentation/codebook/2024-NSCH-Topical-Variable-List.pdf)
- YRBS: administered in English and Spanish, but no language variable in the Data User's Guide, and only 3 ACE items in 2025. [VERIFIED-DOC] — [2025 YRBS overview](https://www.cdc.gov/mmwr/volumes/75/su/su7501a1.htm); [2025 YRBS Data User's Guide](https://www.cdc.gov/yrbs/files/2025/2025-YRBS-Data-Users-Guide-Final.pdf)

### Inferences
1. **CHIS (best).** Same English items as BRFSS, an independent Spanish translation, a free PUF language flag, and, uniquely, nativity and acculturation variables to separate language from immigrant status. About 1,100 Spanish interviews per year can be pooled over 2021–2024. Asian-language DIF is possible via the DAC.
   - Drawbacks: sexual-abuse items and uncollapsed language are DAC-only; missing values appear filled in the PUF; California only; web-dominant mode.
   - Use as a **direct replication plus deconfounding test** of the BRFSS finding.
2. **HCHS/SOL SCAS.** Best for a *within-Hispanic* language test with rich acculturation data and heritage-group variety, including emotional/physical neglect items.
   - Drawbacks: different instrument (Felitti yes/no), no non-Hispanic group, 2008–2011, controlled access.
   - Use as a **conceptual replication** that answers whether DIF follows language preference after holding ethnicity constant.
3. **NLAAS (conditional).** Potentially the only *experimental* evidence on language effects (random language assignment). Value depends on confirming that childhood-adversity items were in the randomized instrument and that the flag is public. The subsample is small (n = 332) and the data are old (2002–2003). Use as a **causal check** if feasible.
4. **NSCH.** Large, national, annual, with Spanish households (about 2,400 per year) and generation and nativity variables. But the items are parent-reported *child* ACEs, there is no response-language variable, and the language toggle blurs instrument language. Use as a **household-language/proxy-report extension**, not a replication. Jensen 2024 already found threshold non-invariance by race/ethnicity.
5. **NESARC-III (conditional).** Large adult sample with ACE items and many immigrants. Ranking depends on unverified interview-language data.
6. **YRBS 2023/2025.** Useful for SOGI-DIF (the open gap in Key Question 4), not language. It has no language variable, and the ACE battery was cut to 3 items in 2025.
7. **Add Health, HRS, NSFG, MIDUS, MHAS, Puerto Rico BRFSS (low or unverified).**
   - Add Health: few Spanish interviews; maltreatment items come from adult waves.
   - HRS: plausible (Spanish interviews plus childhood trauma items) but unverified.
   - MIDUS: I believe English-only (unverified here).
   - MHAS and Puerto Rico BRFSS: largely or entirely Spanish, so no within-survey contrast and language is confounded with place.

### Gaps
- The ranking of NLAAS, NESARC-III and HRS is provisional pending codebook checks: adversity items in the randomized NLAAS module, a NESARC-III interview-language variable, and HRS Spanish administration of trauma items.
- I did not attempt any data downloads requiring registration (CHIS PUF, ICPSR, BioLINCC), so sample sizes for ACE-by-language cells in those files are estimates.
