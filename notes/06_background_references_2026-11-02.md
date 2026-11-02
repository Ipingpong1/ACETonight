# Verified background, mechanism and methods references for a manuscript on interview-language DIF of ACE items among Hispanic adults (BRFSS 2019–2025; CHIS 2021–2025)

**How this list was built (2026-11-02)**
- **Citation details.** Every main-list citation (R1–R61) was checked against Crossref metadata (api.crossref.org/works/{doi}). PMIDs and PMCIDs came from PubMed E-utilities (esearch on the DOI) and the PMC ID converter.
  - Exceptions: Holm 1979 was checked via OpenAlex; Rao–Wu–Yue 1992 by OCR of the article's first page from Statistics Canada; Zumbo 1999 from the author's UBC page.
  - CDC and UCLA documents were downloaded and read directly.
  - Raw metadata and scripts are in `/home/mo2273/ace_refcheck_data/` and `/home/mo2273/ace_refcheck_scripts/`.
- **Fact labels.**
  - **[FT]** = read in the full text: PMC XML or HTML, an official PDF, or (Rao 1992) the OCR'd first page.
  - **[ABS]** = read only in the abstract (PubMed or OpenAlex) or a catalogue record.
  - **"prior notes"** = verified on 2026-11-01 in `/home/mo2273/research_notes/ACE language DIF verification and critique/` and reused here unchanged.
- **Where to cite.** I = Introduction, M = Methods, D = Discussion.
- **Style.** AMA 11th edition: all authors if 6 or fewer, otherwise the first 3 plus "et al"; NLM journal abbreviations.
- **Numbering.** The main list is **R1–R61**, running continuously across sections. Optional verified extras (O1–O28), unverified items (U1–U20) and attribution corrections are in Q8.

---

## Q1. ACE foundations and surveillance: overall prevalence, the share with 4+ ACEs, how group disparities are reported, and how the BRFSS ACE module was adopted

### Takeaway
- **Prevalence.** In the most comprehensive surveillance report, BRFSS 2011–2020 across all 50 states and DC, 63.9% of US adults report ≥1 ACE and 17.3% report ≥4.
- **Hispanic adults.** They appear as a single race/ethnicity stratum: 18.6% report ≥4 ACEs, and their household mental illness prevalence is lower than that of non-Hispanic White adults (12.5% vs 19.5%).
- **No language breakdown.** Neither CDC report (Merrick 2018; Swedo 2023) stratifies by interview language.
- **The BRFSS module.** It was adapted from the CDC-Kaiser ACE Study, is "available in English and Spanish", and has been fielded in all 50 states and DC in at least one year.

### Cited Findings
- **R1.** Felitti VJ, Anda RF, Nordenberg D, et al. Relationship of childhood abuse and household dysfunction to many of the leading causes of death in adults: the Adverse Childhood Experiences (ACE) Study. *Am J Prev Med*. 1998;14(4):245-258. doi:10.1016/S0749-3797(98)00017-8. PMID: 9635069.
  - **Supports:** the origin of the ACE construct. The original "household dysfunction" categories already contained the three stigmatized conditions studied here. **Cite in:** I ¶1.
  - **Facts [ABS, Methods/Results]:**
    - "A questionnaire about adverse childhood experiences was mailed to 13,494 adults who had completed a standardized medical evaluation at a large HMO; 9,508 (70.5%) responded."
    - Categories: "psychological, physical, or sexual abuse; violence against mother; or living with household members who were substance abusers, mentally ill or suicidal, or ever imprisoned."
    - "More than half of respondents reported at least one, and one-fourth reported ≥2 categories."
    - People with ≥4 categories (vs none) "had 4- to 12-fold increased health risks for alcoholism, drug abuse, depression, and suicide attempt."
  - Source: [PubMed 9635069](https://pubmed.ncbi.nlm.nih.gov/9635069/)
- **R2.** Merrick MT, Ford DC, Ports KA, Guinn AS. Prevalence of adverse childhood experiences from the 2011-2014 Behavioral Risk Factor Surveillance System in 23 states. *JAMA Pediatr*. 2018;172(11):1038-1044. doi:10.1001/jamapediatrics.2018.2537. PMID: 30242348; PMCID: PMC6248156.
  - **Supports:** multistate BRFSS ACE prevalence, and Hispanic adults' elevated mean ACE score. **Cite in:** I ¶1–2; D (comparison).
  - **Facts [ABS, Abstract and Key Points]:**
    - "The ACE module consists of 11 questions collapsed into the following 8 categories."
    - "Of the 214 157 respondents included in the sample (51.51% female), 61.55% had at least 1 and 24.64% reported 3 or more ACEs."
    - "Significantly higher ACE exposures were reported by participants who identified as black (mean score, 1.69; 95% CI, 1.62-1.76), Hispanic (mean score, 1.80; 95% CI, 1.70-1.91), or multiracial (mean score, 2.52; 95% CI, 2.36-2.67)."
    - Estimates were stratified by "sex, age group, race/ethnicity, annual household income, educational attainment, employment status, sexual orientation, and geographic region." Language is not among the strata.
  - **Caution:** the abstract reports ≥3 ACEs, not ≥4. I could not access the full text, so do not attribute a "4+" figure to Merrick 2018 (see U13).
  - Source: [PubMed 30242348](https://pubmed.ncbi.nlm.nih.gov/30242348/)
- **R3.** Swedo EA, Aslam MV, Dahlberg LL, et al. Prevalence of adverse childhood experiences among U.S. adults—Behavioral Risk Factor Surveillance System, 2011–2020. *MMWR Morb Mortal Wkly Rep*. 2023;72(26):707-715. doi:10.15585/mmwr.mm7226a2. PMID: 37384554; PMCID: PMC10328489.
  - **Supports:** current national ACE prevalence; Hispanic-specific item prevalences; CDC's own statement that ACEs may be under-reported. **Cite in:** I ¶1–2; D (limitations, surveillance implications).
  - **Headline facts [FT, Summary]:**
    - "Overall, 63.9% of U.S. adults reported at least one ACE; 17.3% reported four or more ACEs."
    - 4+ ACEs "was most common among females (19.2%), adults aged 25–34 years (25.2%), non-Hispanic American Indian or Alaska Native (AI/AN) adults (32.4%), non-Hispanic multiracial adults (31.5%), adults with less than a high school education (20.5%), and those who were unemployed (25.8%) or unable to work (28.8%)."
    - The jurisdiction range was "from 11.9% (New Jersey) to 22.7% (Oregon)."
    - "Disparities in ACEs are often attributable to social and economic environments in which some families live."
  - **Table 2 [FT], Hispanic or Latino (unweighted n = 16,995), ACE score 0 / 1 / 2–3 / ≥4:** 34.9% / 22.6% / 23.9% / **18.6% (95% CI 17.1–20.1)**. Total ≥4 = 17.3% (16.9–17.7); non-Hispanic White ≥4 = 16.8% (16.4–17.3).
  - **Table 3 [FT], Hispanic or Latino, weighted %:**

    | Item | Hispanic | Non-Hispanic White |
    |---|---|---|
    | Emotional abuse | 32.2 | 34.9 |
    | Physical abuse | 30.1 | 21.4 |
    | Sexual abuse | 13.3 | 12.0 |
    | Witnessed IPV | 21.3 | 15.3 |
    | Household substance use | 25.2 | 27.9 |
    | **Household mental illness** | **12.5 (11.3–13.7)** | **19.5 (19.0–20.0)** |
    | Parental separation/divorce | 30.7 | 26.2 |
    | Incarcerated household member | 9.5 (8.4–10.7) | 7.5 |

    - All-adult totals: physical abuse 23.3, sexual abuse 12.6, IPV 17.2, substance use 26.5, mental illness 17.3, divorce 28.4, incarceration 8.6.
    - Column order was taken from the two header rows of the PMC XML. The Total-row emotional-abuse cell reads "NA" in the XML, so check it against the PDF.
  - **Limitations quote [FT, Discussion]:** "recall and social desirability biases might reduce the accuracy of self-reported ACEs, leading to underestimation, because participants might no longer remember or be willing to disclose potentially traumatic events from their childhood."
  - **Other design notes [FT]:**
    - "respondents with missing ACEs data (79,797) were excluded."
    - Table footnote: "For jurisdictions that included ACE questions in >1 year, the most recent year was included."
    - A full-text search found no occurrence of "language" or "Spanish" (my search).
  - Source: [PMC10328489](https://pmc.ncbi.nlm.nih.gov/articles/PMC10328489/)
- **R4.** Centers for Disease Control and Prevention. *Preventing Adverse Childhood Experiences: Leveraging the Best Available Evidence*. National Center for Injury Prevention and Control, Centers for Disease Control and Prevention; 2019. CDC Stacks record cdc:82316.
  - **Supports:** CDC's prevention framing (I ¶1, D, "implications"). **Cite in:** I; D.
  - **Facts [FT, via R3]:**
    - Swedo 2023 cites it as reference 4: "CDC. Preventing adverse childhood experiences: leveraging the best available evidence. Atlanta, GA: US Department of Health and Human Services; CDC; 2019. https://www.cdc.gov/violenceprevention/pdf/preventingACEs.pdf".
    - Swedo's Summary: "CDC has released prevention resources, including Preventing Adverse Childhood Experiences: Leveraging the Best Available Evidence, to help provide jurisdictions and communities with the best available strategies to prevent violence and other ACEs."
    - Source: [PMC10328489](https://pmc.ncbi.nlm.nih.gov/articles/PMC10328489/)
  - **Status of the document itself:**
    - The original PDF URL now returns a "page has moved" redirect (my download, 2026-11-02). The CDC Stacks page is JavaScript-rendered and was not readable.
    - Catalogue details (2019; National Center for Injury Prevention and Control) are from a [CDC Stacks listing seen in search results](https://stacks.cdc.gov/view/cdc/82316).
    - I did not read the document itself (see U12).
- **R5.** Centers for Disease Control and Prevention. Behavioral Risk Factor Surveillance System ACE data. Violence Prevention, Injury Center. Last reviewed June 29, 2023. Accessed November 2, 2026. https://www.cdc.gov/violenceprevention/aces/ace-brfss.html
  - **Supports:** the module's origin, its adoption, and the availability of a Spanish version. **Cite in:** I ¶2; M (instrument).
  - **Facts [FT, read 2026-11-02; page `<title>` = "Behavioral Risk Factor Surveillance System ACE Data"]:**
    - "Since 2009, all 50 states and the District of Columbia have included ACE questions for at least one year on their survey."
    - The module is "adapted from the original CDC-Kaiser ACE study and is used to collect information on child abuse and neglect and household challenges. The module is available in English and Spanish."
    - Footnote 1: "Abuse Questions were modified from the original CDC-Kaiser ACE Study to make them more appropriate for a telephone survey."
    - The page links "BRFSS ACE Module 2021" and "BRFSS ACE Module 2009-2020". Prior notes found that the Spanish PDF CDC distributes is actually the 2011 "Módulo 31" translation.
  - Source: [CDC BRFSS ACE Data page](https://www.cdc.gov/violenceprevention/aces/ace-brfss.html)

### Inferences
- **Suggested Introduction sentence:** "In BRFSS 2011–2020, 63.9% of US adults reported ≥1 ACE and 17.3% reported ≥4 [R3]; Hispanic adults' ≥4 prevalence (18.6%) was close to the national figure [R3]."
- **National reports average over interview language.** Both CDC national reports present Hispanic adults as one stratum and do not split by language [R2, R3]. In the BRFSS ACE years, roughly a third to a half of Hispanic module respondents were interviewed in Spanish (Q3). National Hispanic ACE estimates therefore average over two interview languages.
- **Consistency with H1 (inference, not proof).** Swedo's Table 3 shows Hispanic adults with *lower* household mental illness (12.5% vs 19.5%) but *higher* physical abuse (30.1% vs 21.4%) than non-Hispanic White adults. That is the same item-specific shape as the language contrast the manuscript studies, consistent with H1, but it cannot separate exposure from reporting.
- **CDC's own caveat.** CDC already flags "social desirability" and unwillingness "to disclose" as sources of under-reporting [R3]. The manuscript can cite this as CDC's own caveat, and position the DIF analysis as a test of whether that bias differs by interview language.
- **Use the MMWR for adult figures.** CDC's current ACE web pages changed in 2024–2026. The "About ACEs" page is dated Mar 2, 2026 and now gives only YRBS high-school figures ("Three in four high school students reported experiencing one or more ACEs, and one in five experienced four or more ACEs"). The prevention page is dated Oct 8, 2024 and lists parenting resources and an online training rather than the 2019 document [FT via WebFetch: [About ACEs](https://www.cdc.gov/aces/about/index.html); [ACE prevention](https://www.cdc.gov/aces/prevention/index.html)]. Cite the MMWR (R3) for adult prevalence, not a CDC web page.

### Gaps
- Felitti 1998's percentage with ≥4 categories is in the full text only, which I did not access (U14).
- Merrick 2018's ≥4 prevalence was not verifiable (U13).
- The 2019 CDC prevention document was not opened (U12).

---

## Q2. ACE measurement and invariance: factor structure (where witnessed parental violence loads), prior invariance tests, the reflective/formative debate, and validity of retrospective reports

### Takeaway
- **Factor structure (Ford 2014, full text).** The BRFSS ACE items form three correlated factors. **Household Dysfunction** has 5 items: mental illness, alcohol, drugs, incarceration and separation/divorce. **Emotional/Physical Abuse** has 3 items: witnessed parental violence, physical abuse and verbal abuse. **Sexual Abuse** has 3 items.
- **Witnessed parental violence (item 6)** loads primarily on Emotional/Physical Abuse (0.57), with a 0.33 cross-loading on Household Dysfunction.
- **Prior invariance testing.** It covers gender and age (Ford), race/ethnicity and other demographics with omnibus fit only (Mei), and race/ethnicity in caregiver-reported NSCH data, where thresholds were non-invariant (Jensen). The only Spanish-vs-English test involving ACE items is embedded in a 59-item adversity model (Cooper & Nickodem).
- **Retrospective-report validity.** Agreement with prospective records is poor (κ = 0.19), and errors are dominated by false negatives.

### Cited Findings
- **R6.** Ford DC, Merrick MT, Parks SE, et al. Examination of the factorial structure of adverse childhood experiences and recommendations for three subscale scores. *Psychol Violence*. 2014;4(4):432-444. doi:10.1037/a0037723. PMID: 26430532; PMCID: PMC4587306.
  - **Supports:** the three-factor structure, which defines the "household dysfunction" factor used in H1, plus design-based CFA in BRFSS. **Cite in:** I ¶3; M (measurement model); D.
  - **Facts [FT]:**
    - **Data (Methods):** EFA on 2009 BRFSS (n = 27,545; AR, LA, NM, TN, WA; 8.5% Hispanic); CFA and MGCFA on 2010 BRFSS (n = 57,703; DC plus 10 states).
    - **Table 3, geomin-rotated EFA loadings (Household dysfunction / Emotional-physical abuse / Sexual abuse):**

      | Item | HD | EPA | SA |
      |---|---|---|---|
      | 1 Household mental illness | **0.41** | 0.28 | 0.07 |
      | 2 Alcohol | **0.62** | 0.27 | −0.08 |
      | 3 Drugs | **0.84** | 0.00 | 0.06 |
      | 4 Incarceration | **0.86** | −0.07 | 0.02 |
      | 5 Separation/divorce | **0.54** | 0.07 | 0.00 |
      | 6 "How often did your parents or adults in your home ever slap, hit, kick, punch, or beat each other up?" (labelled "Household physical violence") | 0.33 | **0.57** | −0.01 |
      | 7 Physical abuse | −0.01 | **0.93** | 0.01 |
      | 8 Emotional abuse | 0.11 | **0.76** | 0.02 |
      | 9–11 Sexual abuse items | — | — | **0.95 / 0.97 / 0.85** |

    - Table 3 also reports factor intercorrelations (HD–EPA 0.52; HD–SA 0.40; EPA–SA 0.56), EFA fit (RMSEA 0.012; CFI 0.997; TLI 0.994), and a footnote: "Factor loadings greater than 0.40 appear in bold."
    - **Results text:** "Factor 1 consists of 5 items describing disturbances in the childhood home environment such as family member substance use, parental separation or divorce, and parental incarceration… labeled Household Dysfunction. Factor 2, labeled Physical/Emotional Abuse, consisted of 3 items assessing violent behavior and emotional abuse."
    - **Table 4, 2010 BRFSS:** Household dysfunction, 5 items, α = 0.61; Emotional/physical abuse, 3 items, α = 0.70; Sexual abuse, 3 items, α = 0.80; all 11 items, α = 0.78.
    - **Table 2 tetrachorics:** drugs–incarceration 0.70; mental illness–drugs 0.56; alcohol–IPV 0.59; IPV–physical abuse 0.68; physical–emotional abuse 0.73.
    - **Invariance and design (Table 5; prior notes [FT]):** invariance was tested by gender and four age groups only. "This weight along with stratum and primary sampling unit variables were included in all analyses."
  - Source: [PMC4587306](https://pmc.ncbi.nlm.nih.gov/articles/PMC4587306/)
- **R7.** Mei X, Li J, Li ZS, et al. Psychometric evaluation of an Adverse Childhood Experiences (ACEs) measurement tool: an equitable assessment or reinforcing biases? *Health Justice*. 2022;10(1):34. doi:10.1186/s40352-022-00198-2. PMID: 36445502; PMCID: PMC9706892.
  - **Supports:** the claim that prior BRFSS invariance work ignored language. **Cite in:** I ¶3; D.
  - **Facts:**
    - [ABS] 2019 BRFSS, "97,314 responses"; the 11-item tool fits "a second-order factor with three subscales, all of which passed the measurement invariance tests at metric and scalar levels across age, race, sex, socioeconomic status, gender identity, and sexual orientation." Conclusion: "equitable and free from measurement bias."
    - [FT, prior notes] Hispanic respondents were one level of a 5-category race variable (9.1% of the sample). "Language" and "Spanish" do not appear in the paper. Only omnibus ΔCFI/ΔTLI was used, with no item-level DIF; use of weights is not stated. The text says "sixteen" states but lists 17.
  - Source: [PMC9706892](https://pmc.ncbi.nlm.nih.gov/articles/PMC9706892/)
- **R8.** Jensen TM, Bernard DL, Lanier P. Conceptualizing adverse childhood experiences as a latent factor: tests of measurement invariance across five racial and ethnic groups. *Child Dev*. 2024;95(3):e170-e185. doi:10.1111/cdev.14050. PMID: 38037724; PMCID: PMC11023799.
  - **Supports:** ACE item thresholds differ across racial/ethnic groups including Hispanic; language was untested. **Cite in:** I ¶3; D.
  - **Facts:**
    - [ABS] NSCH 2018–2020 (N = 93,759; Hispanic 14%). "Results support configural and full metric invariance across groups. However, several ACE item thresholds differed across groups."
    - [FT, prior notes] Scalar step ΔCFI = −.057; "thresholds for only three items could be constrained to equality"; unweighted; no language terms in the text.
  - **Name note:** Crossref lists the second author as "Bernard D"; the full text gives "Bernard DL".
  - Source: [PMC11023799](https://pmc.ncbi.nlm.nih.gov/articles/PMC11023799/)
- **R9.** Cooper DK, Nickodem K. Cumulative lifetime adversity in a national sample of Hispanic/Latino immigrants: exploring construct validity across six Hispanic/Latino groups using data from the HCHS/SOL Sociocultural Ancillary Study. *Eval Health Prof*. 2021;44(4):348-361. doi:10.1177/0163278720910470. PMID: 32166975; PMCID: PMC9993236.
  - **Supports:** the only prior Spanish-vs-English invariance test that includes ACE items. **Cite in:** I ¶3 (gap statement); D.
  - **Facts [FT, prior notes]:**
    - N = 3,296 foreign-born adults. "Interviews were conducted by bilingual staff and were offered in English or Spanish - the majority of which were completed in Spanish (92%)."
    - Ten ACE items formed one subscale in a 59-item bifactor model.
    - Strong invariance by language: "significant χ² difference test (Δχ²(132) = 299.00, p < .001) and lower CFI (Δ = −.009)". Support for interpreting language-group differences as true differences was "partially, but not strongly, supported."
  - Source: [PMC9993236](https://pmc.ncbi.nlm.nih.gov/articles/PMC9993236/)
- **R10.** Moriarity DP, Slavich GM. Theoretical and quantitative disconnect when modeling adverse childhood experiences using a common factor framework: an argument for causal indicator models in stressor research. *Child Dev*. 2025;96(4):1255-1259. doi:10.1111/cdev.14230. PMID: 40251931; PMCID: PMC12208002.
  - **Supports:** acknowledging the reflective-vs-causal-indicator critique. **Cite in:** M (rationale); D (limitations).
  - **Facts [FT, prior notes]:**
    - Argues that ACEs are "organic events stemming from a child's environment," so the common-factor model's local-independence assumption is questionable.
    - "This is not to say that we believe ACEs aggregation through measurement models is inappropriate."
    - Invariance "take[s] a different form for causal indicator models" (structure, slope and residual invariance).
  - Source: [PMC12208002](https://pmc.ncbi.nlm.nih.gov/articles/PMC12208002/)
- **R11.** LaNoue MD, Hass RW. Conceptualizing self-reported adverse childhood experiences: from epidemiologic exposure to psychometric latent variable. *Soc Sci Med*. 2025;366:117664. doi:10.1016/j.socscimed.2024.117664. PMID: 39847960.
  - **Supports:** framing ACE responses as *reports*. **Cite in:** I ¶3; D.
  - **Facts [ABS]:**
    - "srACEs cannot be both exposures and indicators of scales."
    - "the epidemiologic paradigm is not a good fit."
    - "We highlight the mismatch and limitations of the reflexive measurement model for srACEs and conclude by endorsing either a formative latent variable model or application of latent class analyses."
    - "We emphasize the importance of… formally testing competing measurement models."
  - Source: [PubMed 39847960](https://pubmed.ncbi.nlm.nih.gov/39847960/)
- **R12.** Baldwin JR, Reuben A, Newbury JB, Danese A. Agreement between prospective and retrospective measures of childhood maltreatment: a systematic review and meta-analysis. *JAMA Psychiatry*. 2019;76(6):584-593. doi:10.1001/jamapsychiatry.2019.0097. PMID: 30892562; PMCID: PMC6551848.
  - **Supports:** the poor validity of retrospective reports. **Cite in:** D (limitations; interpreting under-reporting).
  - **Facts:**
    - [ABS] "Of 450 studies with prospective measures of childhood maltreatment, 16 had paired retrospective data to compute the Cohen κ coefficient."
    - [FT, prior notes] N = 25,471; pooled κ = 0.19 (95% CI 0.14–0.24); 52% of those with prospective records did not report maltreatment retrospectively; 56% of retrospective reporters lacked prospective records; agreement was higher with interviews than with questionnaires.
  - Source: [PMC6551848](https://pmc.ncbi.nlm.nih.gov/articles/PMC6551848/)
- **R13.** Hardt J, Rutter M. Validity of adult retrospective reports of adverse childhood experiences: review of the evidence. *J Child Psychol Psychiatry*. 2004;45(2):260-273. doi:10.1111/j.1469-7610.2004.00218.x. PMID: 14982240.
  - **Supports:** under-reporting (false negatives) is the dominant error in retrospective ACE reports, and items that rest on interpretation are least reliable. **Cite in:** D.
  - **Facts [ABS, Results/Conclusion]:**
    - Retrospective reports "involve a substantial rate of false negatives, and substantial measurement error. On the other hand… false positive reports are probably rare."
    - "little weight can be placed on the retrospective reports of details of early experiences or on reports of experiences that rely heavily on judgement or interpretation."
    - The review covered studies from 1980–2001 with samples ≥40.
  - Source: [PubMed 14982240](https://pubmed.ncbi.nlm.nih.gov/14982240/)

### Inferences
- **Specifying the H1 model.**
  - Ford's "household dysfunction" factor is mental illness + alcohol + drugs + incarceration + separation/divorce. Witnessed IPV belongs to the abuse factor, with a non-trivial cross-loading of 0.33.
  - If H1's latent "household dysfunction" factor includes IPV, the Methods should justify the departure from Ford, or treat IPV as an abuse indicator.
  - Within Ford's factor, the three focal items are identified relative to the only non-focal household items: alcohol (0.62) and separation/divorce (0.54).
  - That makes the alcohol and divorce items the de facto anchors. Divorce is a structurally variable item in Latino samples (see R14 in Q3), which should be stated as an identification caveat (see R49 and R48 in Q6).
- **Interpretation item (my inference).** Household mental illness is the weakest-loading household item (0.41) and the item most dependent on "judgement or interpretation" [R13]. That fits a labelling/disclosure mechanism, but the cited sources do not test it.
- **Gap statement.** "Prior BRFSS invariance studies tested sex and age [R6] or race/ethnicity at the omnibus level [R7]; NSCH thresholds differed by race/ethnicity [R8]; and the only Spanish/English test involving ACE items embedded them in a broader adversity model among immigrants [R9]."
  - Prior notes also flag an embargoed 2026 Harvard dissertation (Umoga; BRFSS 2021–2023 multigroup latent class analysis across six racial/ethnic groups; embargoed until 2027-04-19) as a positioning risk.
- **Retrospective error.** Error in retrospective reports is mostly false negatives [R12, R13]. Language-specific DIF in the "lower endorsement" direction therefore matches the documented error structure, but internal data cannot tell differential under-reporting from true differences (see Q6, R49).

### Gaps
- I did not extract Ford's 2010 CFA standardized loadings (they may be in a figure). The IPV placement above comes from the 2009 EFA table and the factor definitions in the text.
- LaNoue & Hass full text: paywalled, abstract only.
- Two retrospective-consistency papers are verified but kept as optional extras: Reuben 2016 (O8) and Colman 2016 (O9).
- Dube 2004 (ACE Study test–retest reliability) could not be content-verified (U1).

---

## Q3. Hispanic and immigrant ACE patterns, the immigrant paradox, and the share of Hispanic adults interviewed in Spanish

### Takeaway
- **Immigrant paradox.** Data from different informants and designs agree that ACEs are less prevalent among immigrants and immigrant families than among US-born peers: parent-reported NSCH, NESARC, and in-person HCHS/SOL.
- **Caveats in the sources themselves.** Caballero et al. say the paradox "may not reflect a true health advantage" and that "ACE questions may not capture the adverse experiences specific to immigrant families". Llabre et al. found the prison and divorce items "did not cluster" in Latinos and raise political imprisonment as a reason.
- **Spanish-interview share in BRFSS.** In BRFSS 2003–2005, 40% of Hispanic respondents were interviewed in Spanish. In the BRFSS ACE module 2019–2025, the weighted Spanish share among Hispanic respondents was about 32–51% by year (my computation from microdata).
- **Spanish-interview share in CHIS.** In CHIS 2009, 52.4% of Hispanic adults in Kim et al.'s analytic sample were interviewed in Spanish.

### Cited Findings
- **R14.** Llabre MM, Schneiderman N, Gallo LC, et al. Childhood trauma and adult risk factors and disease in Hispanics/Latinos in the US: results from the Hispanic Community Health Study/Study of Latinos (HCHS/SOL) Sociocultural Ancillary Study. *Psychosom Med*. 2017;79(2):172-180. doi:10.1097/PSY.0000000000000394. PMID: 27606797; PMCID: PMC5285322.
  - **Supports:** ACE prevalence among US Latinos by nativity and heritage; the incarceration item's distinct meaning. **Cite in:** I ¶4; D.
  - **Facts [FT]:**
    - Analytic n = 5,117 [ABS].
    - "77.2% of the total sample reported experiencing at least one ACE, and 28.7% reported experiencing four or more ACEs."
    - 4+ ACEs: women 31.2% vs men 25.8%.
    - By heritage: "the highest prevalence of having 4 or more ACEs was reported by individuals of Puerto Rican ancestry (38.1%) or those who self-identified with more than one or 'other' heritage (46.1%)"; Cuban heritage was lowest (20.2%).
    - **By nativity:** "ACEs were significantly more common among those born in the US, with 37.6% reporting 4 or more ACEs, versus 26.3% for those born outside of the US mainland" (Results, Prevalence of ACEs).
    - **Measures section:** internal consistency .74; "two of the items, prison and divorce, did not cluster with the others in our data."
    - **Discussion:** "the political situation in the country of origin and the immigration experience may have led to having a parent go to prison. This item was more prevalent in our sample than in the earlier study."
    - **Methods:** analyses used "SAS PROC SURVEYREG using the sampling weights, clustering and stratification."
  - Source: [PMC5285322](https://pmc.ncbi.nlm.nih.gov/articles/PMC5285322/)
- **R15.** Caballero TM, Johnson SB, Buchanan CRM, DeCamp LR. Adverse childhood experiences among Hispanic children in immigrant families versus US-native families. *Pediatrics*. 2017;140(5):e20170297. doi:10.1542/peds.2017-0297. PMID: 28993445.
  - **Supports:** the immigrant paradox for ACEs, and the authors' own measurement caveat. **Cite in:** I ¶4; D.
  - **Facts [ABS]:**
    - NSCH 2011–2012, "12 162 Hispanic children."
    - "Thirty percent of children in US-native families reported high ACEs compared with only 16% of children in immigrant families"; OR 0.46 (95% CI 0.34–0.61).
    - This held despite more poverty in immigrant families: 80% vs 47% ≤200% of the federal poverty level.
    - "This may not reflect a true health advantage… or ACE questions may not capture the adverse experiences specific to immigrant families."
  - Source: [PubMed 28993445](https://pubmed.ncbi.nlm.nih.gov/28993445/)
- **R16.** Vaughn MG, Salas-Wright CP, Huang J, Qian Z, Terzis LD, Helton JJ. Adverse childhood experiences among immigrants to the United States. *J Interpers Violence*. 2017;32(10):1543-1564. doi:10.1177/0886260515589568. PMID: 26112971.
  - **Supports:** the adult-report immigrant paradox for ACEs. **Cite in:** I ¶4; D.
  - **Facts [ABS]:**
    - NESARC Waves I–II: "With the exception of neglect, the prevalence of ACE was markedly higher among native-born Americans and second-generation immigrants compared with first-generation immigrants."
    - "first-generation immigrants were more likely to report experiences that are deemed neglectful by Western standards."
  - Source: [PubMed 26112971](https://pubmed.ncbi.nlm.nih.gov/26112971/)
- **R17.** Campbell AG, Jacobs W. Correlates of adverse childhood experiences among children in non-Hispanic White, non-Hispanic Black and Hispanic immigrant households in the United States. *J Immigr Minor Health*. 2026;28(2):348-359. doi:10.1007/s10903-025-01785-9. PMID: 41152662; PMCID: PMC13083318.
  - **Supports:** language is tied to ACE reporting within immigrant households, and the authors flag possible under-reporting. **Cite in:** I ¶4; D.
  - **Facts:**
    - [ABS] NSCH 2016–2023, N = 32,094. "English as the primary household language was associated with increased odds of high ACEs exposure among all immigrant groups."
    - [FT, prior notes] For Hispanic children, high ACEs OR = 1.98 (95% CI 1.56–2.50).
    - [FT, prior notes] Limitation: "language barriers may hinder accurate comprehension of the survey, including the ACEs measures. Moreover, these households might be less likely to report ACEs (e.g., maltreatment) due to cultural norms and fear of legal repercussions."
  - Authors: Angela G. Campbell and Wura Jacobs (PMC XML).
  - Source: [PMC13083318](https://pmc.ncbi.nlm.nih.gov/articles/PMC13083318/)
- **R18.** Alhalel N. *Prevalence and Impact of Adverse Childhood Experiences in the Hispanic Community by Questionnaire Language Preference: Behavioral Risk Factor Surveillance System (BRFSS) 2011, 2012*. Master of Public Health culminating experience. Northwestern University; 2018. doi:10.18131/g3-a5x4-zh93.
  - Grey literature (not peer reviewed), but it is the direct BRFSS precedent.
  - **Supports:** the earlier descriptive finding of the same item-specific language pattern. **Cite in:** I ¶4 (precedent); D.
  - **Facts [FT, prior notes]:**
    - 9 states; 2,983 Hispanic respondents; "61% of the Hispanic/Latino respondents preferred the English survey."
    - 6 of 11 items differed (p < 0.01). The English-preference group more often reported household incarceration, household mental illness, household substance abuse, sexual touching and separation.
    - Physical abuse was 28.8% (Spanish) vs 15.9% (English).
    - The ACE-count distribution did not differ significantly between groups.
    - No measurement-equivalence test was done.
  - Source: [Northwestern PRISM](https://prism.northwestern.edu/records/7mt6a-brh38)
- **R19.** DuBard CA, Gizlice Z. Language spoken and differences in health status, access to care, and receipt of preventive services among US Hispanics. *Am J Public Health*. 2008;98(11):2021-2028. doi:10.2105/AJPH.2007.119008. PMID: 18799780; PMCID: PMC2636430.
  - **Supports:** the share of Hispanic BRFSS respondents interviewed in Spanish; Spanish-interview Hispanics are a distinct subpopulation. **Cite in:** I ¶5; M (population); D.
  - **Facts:**
    - [FT, Results, "Demographic Characteristics"] "During the 3-year study period, 17 827 of 45 076 (40%) of the Hispanic respondents to the BRFSS were interviewed with the Spanish-language survey instrument."
    - [FT] Only 6% of Spanish-speaking vs 21% of English-speaking Hispanics had completed college. Household income <$15,000 was 36% vs 15%.
    - [ABS] BRFSS 2003–2005, 23 states, "who represented 90% of the US Hispanic population"; "39% vs 17% in fair or poor health, 55% vs 23% uninsured, and 58% vs 29% without a personal doctor"; "Adjustment for demographic and socioeconomic factors did not mitigate the influence of language on these health indicators."
  - Source: [PMC2636430](https://pmc.ncbi.nlm.nih.gov/articles/PMC2636430/)
- **R20.** Alegría M, Canino G, Shrout PE, et al. Prevalence of mental illness in immigrant and non-immigrant U.S. Latino groups. *Am J Psychiatry*. 2008;165(3):359-369. doi:10.1176/appi.ajp.2007.07040704. PMID: 18245178; PMCID: PMC2712949.
  - **Supports:** an alternative explanation (true lower psychiatric morbidity in immigrant households) and heterogeneity by heritage. **Cite in:** D.
  - **Facts [ABS]:**
    - NLAAS plus NCS-R. "U.S.-born Latino subjects reported higher rates for most psychiatric disorders than Latino immigrants."
    - "The immigrant paradox consistently held for Mexican subjects across mood, anxiety, and substance disorders, while it was only evident among Cuban and other Latino subjects for substance disorders. No differences were found in lifetime prevalence rates between migrant and U.S.-born Puerto Rican subjects."
    - "Aggregating Latino subjects into a single group masks significant variability."
  - Source: [PubMed 18245178](https://pubmed.ncbi.nlm.nih.gov/18245178/)
- **Spanish-interview share facts, BRFSS and CHIS.** These come from prior notes and are documentary or own-computation facts, not literature.
  - **BRFSS 2019 codebook, QSTLANG (all respondents)** [FT, prior notes]: Spanish 16,772, 4.04% unweighted and 7.23% weighted. [2019 codebook](https://www.cdc.gov/brfss/annual_data/2019/pdf/codebook19_llcp-v2-508.HTML)
  - **BRFSS 2023 codebook:** Spanish 18,397, 4.25% unweighted and 7.42% weighted. [2023 codebook](https://www.cdc.gov/brfss/annual_data/2023/zip/codebook23_llcp-v2-508.zip)
  - **Own computation (prior notes, `brfss_feasibility.md`, Table 1).** Weighted Spanish share among Hispanic ACE-module respondents, main plus version files:

    | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
    |---|---|---|---|---|---|---|
    | 32.3% | 38.2% | 31.9% | 33.7% | 37.9% | 50.7%* | 39.5% |

    \*2024 includes Puerto Rico: 4,173 Spanish interviews and 0 English-interview Hispanics.
    - Unweighted pooled 2019–2025 Hispanic respondents: 16,158 Spanish vs 27,565 English (excluding territories: 11,995 vs 27,468).
    - Caveat: these figures pool weights that were not designed to be pooled; they are descriptive only.
  - **Own computation (prior notes, Table 3): crude weighted endorsement among Hispanic respondents 2019–2025, English vs Spanish:**

    | Item | English | Spanish |
    |---|---|---|
    | Household mental illness | 22.5% | 5.1% |
    | Drug use | 14.6% | 3.9% |
    | Incarceration | 14.5% | 3.1% |
    | Physical abuse | 34.7% | 30.2% |
    | Verbal abuse | 41.7% | 18.4% |

    These match the manuscript's exploratory figures.
  - **CHIS:**
    - Kim et al. 2016 (R33) [FT, Results]: in CHIS 2009, "Among Hispanics/Latinos, over half were interviewed in Spanish (52.4%)."
    - CHIS 2021 adult public-use file `INTVLNGC_P1` [FT, prior notes]: Spanish 1,116 of 24,453 adults (4.56%, unweighted). [CHIS 2021 PUF data dictionary](https://healthpolicy.ucla.edu/sites/default/files/2023-08/chis-2021-data-dictionary-adult-oct-2022.pdf)

### Inferences
- **What the paradox literature implies for the design.**
  - Part of the crude 5% vs 23% gap in household mental illness is plausibly a real exposure difference, given the immigrant paradox in ACEs [R15, R16, R14] and in psychiatric disorders [R20].
  - Conditioning on the latent level (MIMIC/DIF) removes only the part of that difference shared across the household items.
  - The Discussion must concede one alternative: lower true mental-illness prevalence in immigrant households, *relative to* their other household adversities, would also appear as DIF [R20]. The CHIS nativity adjustment partly addresses this.
- **Puerto Rico.** There is no immigrant paradox for Puerto Ricans [R20], and Puerto Ricans have high ACE prevalence [R14]. Together with the Puerto Rico 2024 confound in BRFSS (prior notes), this supports analysing Puerto Rico separately or excluding it.
- **Spanish share in the Introduction.** Cite DuBard (40% of Hispanic BRFSS respondents in 2003–2005) as the published figure, and give the manuscript's own 2019–2025 weighted share as a Results-section number, not a literature citation.
- **Precedent.** Alhalel's unpublished thesis already showed the item-specific BRFSS pattern (household items lower in Spanish, physical abuse higher). Cite it to pre-empt novelty objections, while noting it ran no measurement test.

### Gaps
- I found no peer-reviewed publication reporting the Spanish-interview share among Hispanic BRFSS respondents after 2005. Recent figures are own computations.
- Loria & Caughy 2018 (O10), Lee & Altschul 2015 (O12) and Klevens 2019 (O13) are verified but optional.

---

## Q4. Mechanism: mental-illness stigma among Latinos, cultural idioms ("nervios"), familismo and family privacy, stigma of family incarceration and drug use, and disclosure to interviewers

### Takeaway
- **Mental-illness stigma among Latinos** is documented empirically: focus groups, a screening study of 15,383 women, and a study of Spanish-speaking primary-care patients.
- **Labelling.** Mexican-American families prefer the folk label "nervios" partly to reduce the stigma of mental illness. That is a direct reason a Spanish-speaking respondent may not answer "yes" to "mentally ill" ("una enfermedad mental").
- **Courtesy stigma.** Stigma attaches to family members of people with drug dependence and of incarcerated parents.
- **Survey misreporting** on sensitive topics is common, situational, and motivated by avoiding embarrassment or "repercussions from third parties".
- **Limit of the evidence.** None of these studies tests reporting of *household members'* conditions by interview language. The mechanism is inferred from adjacent evidence and should be framed as a hypothesis.

### Cited Findings
- **R21.** Jenkins JH. Ethnopsychiatric interpretations of schizophrenic illness: the problem of nervios within Mexican-American families. *Cult Med Psychiatry*. 1988;12(3):301-329. doi:10.1007/BF00051972. PMID: 3234015.
  - **Supports:** idioms of distress, and labelling a relative's illness as "nervios" to reduce stigma. **Cite in:** I ¶6 (hypothesis); D.
  - **Facts [ABS]:**
    - "Among Mexican-American families, the concept of nervios (nerves) serves as a culturally meaningful illness category for a wide range of conditions, including schizophrenic disorders."
    - "a cultural preference for the term nervios is linked to the efforts of family members to reduce the stigma associated with a mental illness while also reinforcing the strength of family bonds and solidarity by fostering tolerant inclusion of the family member within the home."
  - Source: [PubMed 3234015](https://pubmed.ncbi.nlm.nih.gov/3234015/)
- **R22.** Interian A, Martinez IE, Guarnaccia PJ, Vega WA, Escobar JI. A qualitative analysis of the perception of stigma among Latinos receiving antidepressants. *Psychiatr Serv*. 2007;58(12):1591-1594. doi:10.1176/ps.2007.58.12.1591. PMID: 18048562.
  - **Supports:** mental-illness stigma among Latinos, and its conflict with cultural values. **Cite in:** I ¶6; D.
  - **Facts [ABS]:**
    - Six focus groups (N = 30) of Latino outpatients receiving antidepressants.
    - "antidepressant use was seen as implying more severe illness, weakness or failure to cope with problems."
    - "Stigma was a prominent concern among Latinos receiving antidepressants… culture is likely to play an important role in the communication of stigma."
  - Source: [PubMed 18048562](https://pubmed.ncbi.nlm.nih.gov/18048562/)
- **R23.** Nadeem E, Lange JM, Edge D, Fongwa M, Belin T, Miranda J. Does stigma keep poor young immigrant and U.S.-born Black and Latina women from seeking mental health care? *Psychiatr Serv*. 2007;58(12):1547-1554. doi:10.1176/ps.2007.58.12.1547. PMID: 18048555.
  - **Supports:** stigma is stronger and more consequential among immigrants. **Cite in:** I ¶6; D.
  - **Facts [ABS]:**
    - 15,383 low-income women screened for depression.
    - "There was a significant stigma-by-immigrant interaction predicting interest in treatment (p<.001). Stigma reduced the desire for mental health treatment for immigrant women with depression (OR=.35, p<.001) to a greater extent than it did for U.S.-born white women with depression (OR=.52, p=.24)."
    - "Stigma-related concerns are most common among immigrant women."
  - **Caution:** the same abstract reports that immigrant Latinas were *more* likely than US-born White women to want treatment (OR = 2.17, p = .02), and the stigma-concern ORs it highlights are for Black groups. Do not over-generalise to Latinas.
  - Source: [PubMed 18048555](https://pubmed.ncbi.nlm.nih.gov/18048555/)
- **R24.** Vega WA, Rodriguez MA, Ang A. Addressing stigma of depression in Latino primary care patients. *Gen Hosp Psychiatry*. 2010;32(2):182-191. doi:10.1016/j.genhosppsych.2009.10.008. PMID: 20302993.
  - **Supports:** stigma reduces disclosure of mental illness *within the family*, among Spanish-speaking Latinos specifically. **Cite in:** I ¶6; D.
  - **Facts [ABS]:**
    - "Two hundred low-income, Spanish-speaking, Latino patients in primary care."
    - "Patients reporting higher levels of perceived stigma… were less likely to disclose their depression diagnosis to their family and friends (P<.05) and also less likely to be taking depression medication (OR=.78; 95% CI, .62-.99)."
  - Source: [PubMed 20302993](https://pubmed.ncbi.nlm.nih.gov/20302993/)
- **R25.** Sabogal F, Marín G, Otero-Sabogal R, Marín BV, Perez-Stable EJ. Hispanic familism and acculturation: what changes and what doesn't? *Hisp J Behav Sci*. 1987;9(4):397-412. doi:10.1177/07399863870094003.
  - **Supports:** familismo as a core Hispanic value, part of which persists across acculturation. **Cite in:** I ¶6; D.
  - **Facts [ABS]:**
    - 452 Hispanics vs 227 non-Hispanic Whites.
    - "Three basic dimensions of familism were found: Familial obligations, perceived support from the family and family as referents."
    - "Familial obligations and the perception of the family as referents appear to diminish with the level of acculturation, but the perception of family support doesn't change… the attitudes of persons with high levels of acculturation are more familistic than those of white nonHispanics."
  - Source: [doi:10.1177/07399863870094003](https://doi.org/10.1177/07399863870094003) (abstract via OpenAlex)
- **R26.** Corrigan PW, Watson AC, Miller FE. Blame, shame, and contamination: the impact of mental illness and drug dependence stigma on family members. *J Fam Psychol*. 2006;20(2):239-246. doi:10.1037/0893-3200.20.2.239. PMID: 16756399.
  - **Supports:** family ("courtesy") stigma, strongest for drug dependence, which bears on the household drug-use item. **Cite in:** I ¶6; D.
  - **Facts [ABS]:**
    - National sample, N = 968, vignette design.
    - "Family stigma related to mental illnesses, such as schizophrenia, is not highly endorsed. Family stigma related to drug dependence, however, is worse than for other health conditions, with family members being blamed for both the onset and offset of a relative's disorder and likely to be socially shunned."
  - Source: [PubMed 16756399](https://pubmed.ncbi.nlm.nih.gov/16756399/)
- **R27.** Luther K. Stigma management among children of incarcerated parents. *Deviant Behav*. 2016;37(11):1264-1275. doi:10.1080/01639625.2016.1170551.
  - **Supports:** incarceration stigma extends to family members, who manage and conceal it; this bears on the incarceration item. **Cite in:** I ¶6; D.
  - **Facts [ABS]:**
    - "The stigma of incarceration can extend beyond the offender to his or her family."
    - "Using interviews with 32 college students whose parents were incarcerated during their childhood… participants separated themselves from their incarcerated parent, viewed their incarcerated parent as a role model, and framed parental incarceration positively."
  - Source: [doi:10.1080/01639625.2016.1170551](https://doi.org/10.1080/01639625.2016.1170551) (abstract via OpenAlex)
- **R28.** Tourangeau R, Yan T. Sensitive questions in surveys. *Psychol Bull*. 2007;133(5):859-883. doi:10.1037/0033-2909.133.5.859. PMID: 17723033.
  - **Supports:** the general theory of motivated misreporting to interviewers. **Cite in:** I ¶6; D.
  - **Facts [ABS]:**
    - "misreporting about sensitive topics is quite common and… largely situational. The extent of misreporting depends on whether the respondent has anything embarrassing to report and on design features of the survey."
    - Respondents "edit the information they report to avoid embarrassing themselves in the presence of an interviewer or to avoid repercussions from third parties."
  - Source: [PubMed 17723033](https://pubmed.ncbi.nlm.nih.gov/17723033/)

### Inferences
- **Proposed mechanism chain for the Introduction and Discussion (hypothesis, assembled from adjacent evidence):**
  1. **Labelling.** Relatives' conditions may be construed as "nervios" rather than "enfermedad mental" [R21].
  2. **Within-family concealment.** Stigma reduces disclosure of depression to family [R24]. A respondent may therefore never have *known* about a household member's illness, a knowledge pathway distinct from reluctance to report.
  3. **Courtesy stigma.** This applies to drug dependence [R26] and incarceration [R27].
  4. **Motivated editing.** Respondents edit answers to interviewers [R28], possibly heightened by "repercussions from third parties" concerns among immigrant families (compare the Campbell & Jacobs limitation, R17).
  5. **Familism.** Family as referent and obligation [R25] makes family problems especially private. That dimension weakens with acculturation, consistent with larger DIF in Spanish interviews.
- **Using the CHIS mode contrast.** CHIS adult interviews are about 90% web self-administered (prior notes), and self-administration increases reporting of sensitive information relative to CATI (Kreuter 2008, O3). If DIF persists in CHIS, interviewer presence alone is an unlikely explanation, which points toward labelling or knowledge pathways. This is my inference and cannot be tested within the cited sources.
- **The parity prediction for physical abuse** is consistent with corporal punishment being normative rather than stigmatized among Latino parents (Klevens 2019, O13: spanking "most frequent among Latinos (73%)"). Note that foreign-born Hispanic parents spank *less* than US-born ones (Lee & Altschul 2015, O12).

### Gaps
- **No direct test of the mechanism.** I found no empirical study of how adults report *household members'* mental illness, drug use or incarceration by interview language or acculturation. The mechanism remains a hypothesis built from adjacent evidence.
- **Incarceration stigma.** Other sources are only partly verified: Phillips & Gates 2011 (U2), Dallaire 2010 (U4) and Saunders 2018 (U5) had no retrievable abstracts. Luther 2016 is qualitative (n = 32).
- **Family privacy specifically.** Fontes 2007 ("Sin vergüenza"; U6) has no abstract in PubMed. Fontes & Plummer 2010 (O15) is a review of cultural issues in child sexual abuse disclosure, not of household conditions.

---

## Q5. Language-of-interview effects in surveys: self-rated health, question order, MIMIC language DIF, and invariance of mental-health scales by language

### Takeaway
- **Language effects are real but item-specific.** They are documented for self-rated health (the "fair"→"regular" translation, and question-order effects in CHIS that appear only in Spanish interviews), for Latino political attitudes (MIMIC), and for the K6 in CHIS (DIF on "nervous", "hopeless", "restless" and "depressed").
- **Many scales are equivalent.** The CES-D-10 (HCHS/SOL), PHQ-9 and GAD-7 show configural/metric and largely scalar equivalence across English and Spanish in Hispanic samples. Language DIF is therefore not inevitable, which supports an item-specific (stigmatized-content) hypothesis rather than a blanket language artefact.
- **Randomized language assignment** among bilinguals (NLAAS) found differences in only 1 of 15 diagnoses.

### Cited Findings
- **R29.** Viruell-Fuentes EA, Morenoff JD, Williams DR, House JS. Language of interview, self-rated health, and the other Latino health puzzle. *Am J Public Health*. 2011;101(7):1306-1313. doi:10.2105/AJPH.2009.175455. PMID: 21164101; PMCID: PMC3110226.
  - **Supports:** a translation-driven language effect in BRFSS itself. **Cite in:** I ¶5; D.
  - **Facts [ABS]:**
    - Data: Chicago Community Adult Health Study 2001–2003 and BRFSS 2003.
    - "Being interviewed in Spanish was associated with significantly higher odds of rating health as fair or poor in both data sets. Moreover, adjusting for language of interview substantially reduced the gap between Whites and Latinos."
    - "translation of the English word 'fair' to regular induces Spanish-language respondents to report poorer health than they would in English."
  - Source: [PubMed 21164101](https://pubmed.ncbi.nlm.nih.gov/21164101/)
- **R30.** Bzostek S, Goldman N, Pebley A. Why do Hispanics in the USA report poor health? *Soc Sci Med*. 2007;65(5):990-1003. doi:10.1016/j.socscimed.2007.04.028. PMID: 17574713.
  - **Supports:** interview language outperforms other acculturation measures in explaining a reporting gap. **Cite in:** I ¶5; D.
  - **Facts [ABS]:**
    - Data: L.A.FANS-1.
    - "they underscore the importance of language of interview over other measures of acculturation, suggesting that translation issues between the Spanish and English versions of the SRH question may give rise to some of the differences."
  - Source: [PubMed 17574713](https://pubmed.ncbi.nlm.nih.gov/17574713/)
- **R31.** Lee S, Grant D. The effect of question order on self-rated general health status in a multilingual survey context. *Am J Epidemiol*. 2009;169(12):1525-1530. doi:10.1093/aje/kwp070. PMID: 19363097; PMCID: PMC2727201.
  - **Supports:** context effects that appear only in Spanish interviews, in CHIS itself. **Cite in:** I ¶5; D (the order of the CHIS ACE section changed in 2023 per prior notes).
  - **Facts:**
    - [ABS] Split-half experiment in CHIS 2007. "Although no order effect was present in the English interviews, the authors found a significant and large effect with Spanish interviews: Self-rated health appeared much worse when asked before chronic conditions than when asked after them."
    - [FT, Methods] "we subsampled 1,191 English-speaking and 824 Spanish-speaking adults interviewed during the same time period."
    - [FT, Results] For Spanish interviews, asking self-rated health after the chronic conditions raised "very good" and "good" by 4.3 and 5.6 points, while "'fair' and 'poor' health decreased significantly (−7.5% and −4.5%, respectively)."
  - Source: [PMC2727201](https://pmc.ncbi.nlm.nih.gov/articles/PMC2727201/)
- **R32.** Pérez EO. The origins and implications of language effects in multilingual surveys: a MIMIC approach with application to Latino political attitudes. *Polit Anal*. 2011;19(4):434-454. doi:10.1093/pan/mpr029.
  - **Supports:** a MIMIC model that separates true language-group differences from language DIF, a direct methods precedent. **Cite in:** M (rationale for MIMIC); D.
  - **Facts [ABS]:**
    - Distinguishes "(1) differences in attitude and (2) differences in measures of attitude… formally known as Differential Item Functioning (DIF)."
    - Using the Latino National Survey (2006): "the language of interview systematically colors Latinos' interpretation of survey items, even after controlling for measurement error and individual differences in the latent variable being assessed."
  - Source: [doi:10.1093/pan/mpr029](https://doi.org/10.1093/pan/mpr029) (abstract via OpenAlex)
- **R33.** Kim G, DeCoster J, Bryant AN, Ford KL. Measurement equivalence of the K6 scale: the effects of race/ethnicity and language. *Assessment*. 2016;23(6):758-768. doi:10.1177/1073191115599639. PMID: 26282779; PMCID: PMC5468522.
  - **Supports:** language DIF on mental-health wording in CHIS. **Cite in:** I ¶5; D.
  - **Facts:**
    - [FT, Methods] "Participant data were drawn from the 2009 California Health Interview Survey (CHIS) that was conducted between September 2009 and April 2010."
    - [FT, Results] "The majority of the total sample included in the DIF analyses was interviewed in English (89.0%), followed by Spanish (6.9%)… Among Hispanics/Latinos, over half were interviewed in Spanish (52.4%)."
    - [ABS] N = 44,846. IRT-based DIF: "four items ('nervous,' 'hopeless,' 'restless,' and 'depressed') varied significantly across languages." Also: "the observed nonequivalence in the K6 appears to be driven by language rather than race/ethnicity."
    - [ABS] Effect-size analyses found "the Hispanic/Latino Spanish group was not different from the Hispanic/Latino English group". Report this tension accurately.
  - Source: [PMC5468522](https://pmc.ncbi.nlm.nih.gov/articles/PMC5468522/)
- **R34.** González P, Nuñez A, Merz E, et al. Measurement properties of the Center for Epidemiologic Studies Depression Scale (CES-D 10): findings from HCHS/SOL. *Psychol Assess*. 2017;29(4):372-381. doi:10.1037/pas0000330. PMID: 27295022; PMCID: PMC5154787.
  - **Supports:** a counterexample, namely full language invariance of a depression scale among Latinos. **Cite in:** D.
  - **Facts:**
    - [ABS] n = 16,415; "Participants completed interview administered measures in English or Spanish." "Multiple group analyses showed the 1-factor structure to be invariant across English and Spanish speaking responders and partially invariant across Hispanic/Latino background groups."
    - [FT] Tested "configural invariance, metric invariance, and scalar/threshold invariance."
  - Source: [PMC5154787](https://pmc.ncbi.nlm.nih.gov/articles/PMC5154787/)
- **R35.** Merz EL, Malcarne VL, Roesch SC, Riley N, Sadler GR. A multigroup confirmatory factor analysis of the Patient Health Questionnaire-9 among English- and Spanish-speaking Latinas. *Cultur Divers Ethnic Minor Psychol*. 2011;17(3):309-316. doi:10.1037/a0023883. PMID: 21787063; PMCID: PMC4210271.
  - **Supports:** a counterexample (PHQ-9 equivalence across English and Spanish). **Cite in:** D.
  - **Facts [ABS]:** "479 Latina women… completed the PHQ-9 in their preferred language of English or Spanish… Results support a similar one-factor structure with equivalent response patterns and variances."
  - Source: [PubMed 21787063](https://pubmed.ncbi.nlm.nih.gov/21787063/)
- **R36.** Mills SD, Fox RS, Malcarne VL, Roesch SC, Champagne BR, Sadler GR. The psychometric properties of the Generalized Anxiety Disorder-7 scale in Hispanic Americans with English or Spanish language preference. *Cultur Divers Ethnic Minor Psychol*. 2014;20(3):463-468. doi:10.1037/a0036523. PMID: 25045957; PMCID: PMC4129392.
  - **Supports:** a counterexample (GAD-7). **Cite in:** D.
  - **Facts [ABS]:** "436 Hispanic Americans with an English (n = 210) or Spanish (n = 226) language preference… a similar unidimensional factor structure with equivalent response patterns and item intercepts, but different variances, across language-preference groups."
  - Source: [PubMed 25045957](https://pubmed.ncbi.nlm.nih.gov/25045957/)
- **R37.** Shrout PE, Alegría M, Canino G, et al. Testing language effects in psychiatric epidemiology surveys with randomized experiments: results from the National Latino and Asian American Study. *Am J Epidemiol*. 2008;168(3):345-352. doi:10.1093/aje/kwn116. PMID: 18550562; PMCID: PMC2727260.
  - **Supports:** the design remedy (randomizing language among bilinguals) and the point that translation does not guarantee equivalence. **Cite in:** D (future research).
  - **Facts [ABS, prior notes]:**
    - "Bilingual respondents from the Latino section of the NLAAS (n = 332) were randomly assigned to receive either a Spanish- or English-language version." Only 1 of 15 diagnostic comparisons differed (lifetime GAD was more prevalent with English).
    - "Translation and back-translation of surveys does not guarantee that response probabilities are exactly equivalent. Randomized survey experiments should be incorporated…"
  - Source: [PubMed 18550562](https://pubmed.ncbi.nlm.nih.gov/18550562/)
- **Translation context for the two surveys [FT, prior notes].**
  - The CHIS 2021 public-use file note says `ACE_A` is an "11 POINT ACE SCALE [that] MIRRORS 2009-2020 BRFSS ACE MODULE".
  - CHIS uses its own Spanish translation. Household mental illness reads "¿Vivió con alguien que estaba deprimido/a, era enfermo/a mental o suicida?" ([CHIS 2023 Spanish CATI questionnaire](https://healthpolicy.ucla.edu/sites/default/files/2024-09/chis-2023-spanish-cati-v.3.01-21aug2024-adult-questionnaire_clean.pdf)).
  - BRFSS (2010–2020 Spanish) reads "¿Vivió con alguien que tenía depresión, una enfermedad mental o tendencias suicidas?"
  - BRFSS verbal abuse renders "put you down" as "le humilló/humillaba" ([BRFSS 2019 Spanish questionnaire](https://www.cdc.gov/brfss/questionnaires/pdf-ques/2019-BRFSS-Questionnaire-Spanish-Verison-508.pdf)).

### Inferences
- **Item-specificity is the expected pattern.** Language effects attach to particular words and contexts ("fair/regular" [R29]; question order [R31]; "depressed"/"nervous" in the K6 [R33]), not to whole instruments [R34–R36]. That supports the manuscript's item-specific design.
  - Physical abuse at parity serves as an internal comparison item. The verbal-abuse result (larger DIF with CDC's "humilló" wording than with CHIS's) is a translation signature in the spirit of [R29, R30].
- **Lexical overlap (my inference).** The household mental-illness item contains "depressed", and "depressed" showed language DIF in the CHIS K6 [R33]. This lexical overlap is worth noting as a possible translation pathway that competes with stigma.
- **Context effects.** Spanish-language responses in CHIS are more sensitive to context [R31]. When pooling CHIS 2021–2022 with 2023+, the 2023 change in ACE-section order (ACE awareness items placed before the screener; prior notes) should be checked as a context effect.
- **Methods precedents.** Pérez [R32] and Jones (R41, Q6) are the clearest precedents for using MIMIC to separate language DIF from true group differences.

### Gaps
- I did not retrieve the full texts of Pérez 2011 and Viruell-Fuentes 2011, so their effect sizes are not reported here.
- Lee & Schwarz 2014 (O16) and Lee, Nguyen & Tsui 2011 (O17) are verified extras.
- The CHIS Spanish verbal-abuse wording was not extracted, so the "CDC vs CHIS wording" contrast relies on the manuscript's own instrument review.

---

## Q6. DIF and invariance methods: MIMIC origin and performance, categorical identification, fit criteria, anchors and approximate invariance, logistic-regression DIF, software, survey variance and multiplicity

### Takeaway
- **MIMIC as primary.** MIMIC (Muthén 1989) is well supported for uniform DIF when the focal group is small (Woods 2009), and has precedent for Spanish/English language DIF (Jones 2006; Pérez 2011).
- **MIMIC's limits.**
  - It lets only a subset of parameters vary (Bauer 2017), which justifies the secondary multigroup CFA for loading/non-uniform DIF.
  - It can produce false positives with contaminated anchors (Finch 2005).
- **Categorical invariance** needs careful identification (Millsap & Yun-Tein 2004; Wu & Estabrook 2016). Fit-change criteria behave differently with unequal group sizes (Chen 2007) and with categorical data in large samples (Rutkowski & Svetina 2017).
- **DIF is relative.** Only relative item difficulties are identified (Bechger & Maris 2015). There is "unavoidable ambiguity" in comparisons when invariance fails (Robitzsch & Lüdtke 2023).
- **Support literature.** lordif/Zumbo for logistic-regression effect sizes; lavaan and survey for software; Rao–Wu–Yue for replication variance; Holm for multiplicity; Bieler for design-based adjusted prevalence ratios.

### Cited Findings
- **R38.** Muthén BO. Latent variable modeling in heterogeneous populations. *Psychometrika*. 1989;54(4):557-585. doi:10.1007/BF02296397.
  - **Supports:** MIMIC for detecting group heterogeneity (direct effects). **Cite in:** M.
  - **Facts [ABS]:** "MIMIC structural modeling is shown to be a useful method for detecting and describing heterogeneity that cannot be handled in regular multiple-group analysis."
  - Source: [doi:10.1007/BF02296397](https://doi.org/10.1007/BF02296397) (abstract via OpenAlex)
  - Jöreskog & Goldberger 1975, the original MIMIC model, is verified as O1.
- **R39.** Woods CM. Evaluation of MIMIC-model methods for DIF testing with comparison to two-group analysis. *Multivariate Behav Res*. 2009;44(1):1-27. doi:10.1080/00273170802620121. PMID: 26795105.
  - **Supports:** MIMIC as primary when the focal group is small relative to the reference group. **Cite in:** M.
  - **Facts [ABS]:** "With small focal-group samples, tests of uniform DIF with binary or 5-category ordinal responses were more accurate with MIMIC models than 2-group IRT."
  - Source: [PubMed 26795105](https://pubmed.ncbi.nlm.nih.gov/26795105/)
- **R40.** Finch H. The MIMIC model as a method for detecting DIF: comparison with Mantel-Haenszel, SIBTEST, and the IRT likelihood ratio. *Appl Psychol Meas*. 2005;29(4):278-295. doi:10.1177/0146621605275728.
  - **Supports:** MIMIC DIF performance and its anchor-contamination risk. **Cite in:** M; D (limitations).
  - **Facts [ABS]:**
    - The simulation manipulated "level of DIF contamination of the anchor items."
    - "MIMIC model is effective for DIF identification for 50 items or when the two-parameter logistic model underlies the data but has a very high rate of incorrect DIF identification for 20 items with three-parameter logistic data."
  - Source: [doi:10.1177/0146621605275728](https://doi.org/10.1177/0146621605275728)
- **R41.** Jones RN. Identification of measurement differences between English and Spanish language versions of the Mini-Mental State Examination: detecting differential item functioning using MIMIC modeling. *Med Care*. 2006;44(11 suppl 3):S124-S133. doi:10.1097/01.mlr.0000245250.50114.0f. PMID: 17060819.
  - **Supports:** a MIMIC language-DIF precedent, and evidence that DIF can explain much of a group gap. **Cite in:** M; D.
  - **Facts [ABS]:**
    - "dementia case registry study (n = 1546), 42% of whom were examined with the Spanish language MMSE."
    - "Twelve of 21 items were identified as having significant uniform DIF… DIF accounted for two-thirds of the observed difference in underlying level of cognitive functioning between Spanish- and English-language administration groups."
    - "Failing to account for measurement differences may lead to spurious inferences."
  - Source: [PubMed 17060819](https://pubmed.ncbi.nlm.nih.gov/17060819/)
- **R42.** Millsap RE, Yun-Tein J. Assessing factorial invariance in ordered-categorical measures. *Multivariate Behav Res*. 2004;39(3):479-515. doi:10.1207/S15327906MBR3903_4.
  - **Supports:** identification of multigroup categorical CFA. **Cite in:** M.
  - **Facts [ABS]:**
    - "a comprehensive statement of identification conditions for the multiple-population case seems absent in the literature… New results on identification are given."
    - LISREL and Mplus "are shown to have different model specifications for this method, leading to different fit results in some cases."
  - Source: [doi:10.1207/S15327906MBR3903_4](https://doi.org/10.1207/S15327906MBR3903_4)
- **R43.** Wu H, Estabrook R. Identification of confirmatory factor analysis models of different levels of invariance for ordered categorical outcomes. *Psychometrika*. 2016;81(4):1014-1045. doi:10.1007/s11336-016-9506-0. PMID: 27402166; PMCID: PMC5458787.
  - **Supports:** the identification choices for the MGCFA with binary items. **Cite in:** M.
  - **Facts [ABS]:**
    - Under baseline identification, "Once an invariance condition is imposed on a parameter, these identification conditions may become restrictions and define statistically non-equivalent models, leading to different conclusions."
    - Their tests "do not depend on the specific identification condition chosen for the baseline model."
  - Source: [PubMed 27402166](https://pubmed.ncbi.nlm.nih.gov/27402166/)
- **R44.** Bauer DJ. A more general model for testing measurement invariance and differential item functioning. *Psychol Methods*. 2017;22(3):507-526. doi:10.1037/met0000077. PMID: 27266798; PMCID: PMC5140785.
  - **Supports:** the limits of MIMIC versus multigroup models, and MNLFA as a generalization. **Cite in:** M (why MGCFA is secondary); D.
  - **Facts [ABS]:**
    - "The multiple groups model allows 1 to examine the invariance of all model parameters but only across levels of a single categorical individual difference variable… the MIMIC model permits both categorical and continuous individual difference variables… but permits only a subset of the model parameters to vary."
    - "MNLFA subsumes and combines the strengths of the multiple group and MIMIC models."
  - Source: [PubMed 27266798](https://pubmed.ncbi.nlm.nih.gov/27266798/)
- **R45.** Chen FF. Sensitivity of goodness of fit indexes to lack of measurement invariance. *Struct Equ Modeling*. 2007;14(3):464-504. doi:10.1080/10705510701301834.
  - **Supports:** fit-change criteria, and the warning about unequal group sizes (the Spanish group is the smaller one). **Cite in:** M.
  - **Facts [ABS]:**
    - "CFI and RMSEA appear to be equally sensitive to all 3 types of lack of invariance."
    - "Unequal sample sizes affect changes across all 3 levels of invariance: Changes are bigger when sample sizes are equal rather than when they are unequal."
    - "Cutoff points for testing invariance at different levels are recommended." The numeric cutoffs were not verified here (U10).
  - Source: [doi:10.1080/10705510701301834](https://doi.org/10.1080/10705510701301834)
- **R46.** Rutkowski L, Svetina D. Measurement invariance in international surveys: categorical indicators and fit measure performance. *Appl Meas Educ*. 2017;30(1):39-51. doi:10.1080/08957347.2016.1243540.
  - **Supports:** criteria for categorical indicators in large samples. **Cite in:** M.
  - **Facts [ABS]:**
    - "classic measures and associated criteria were either unsuitable in a large-group and varied sample-size context or should be adjusted, particularly when observed variables were not normally distributed."
    - "We provide specific recommendations for revising currently used criteria… based on the chi-square test, root mean-squared error of approximation, and comparative fit index (CFI)."
    - The specific values (ΔCFI ≥ −0.004 and ΔRMSEA ≤ 0.01, from a secondary summary in prior notes) are **not** verified from the primary source (U9).
  - Source: [doi:10.1080/08957347.2016.1243540](https://doi.org/10.1080/08957347.2016.1243540)
- **R47.** Asparouhov T, Muthén B. Multiple-group factor analysis alignment. *Struct Equ Modeling*. 2014;21(4):495-508. doi:10.1080/10705511.2014.919210.
  - **Supports:** alignment as an approximate-invariance sensitivity analysis. **Cite in:** M (sensitivity); D.
  - **Facts [ABS]:** "The alignment method can be used to estimate group-specific factor means and variances without requiring exact measurement invariance… the alignment method is based on the configural model."
  - Source: [doi:10.1080/10705511.2014.919210](https://doi.org/10.1080/10705511.2014.919210)
- **R48.** Robitzsch A, Lüdtke O. Why full, partial, or approximate measurement invariance are not a prerequisite for meaningful and valid group comparisons. *Struct Equ Modeling*. 2023;30(6):859-870. doi:10.1080/10705511.2023.2191292.
  - **Supports:** the interpretive stance on DIF and the ambiguity of group comparisons. **Cite in:** D.
  - **Facts [ABS]:**
    - "measurement invariance is not necessary for meaningful and valid comparisons across groups."
    - "There is unavoidable ambiguity in how researchers can define comparisons if measurement invariance is violated."
    - "there is no support for preferring the partial invariance approach over competing approaches, such as invariance alignment, robust linking, or Bayesian approximate invariance."
  - Source: [doi:10.1080/10705511.2023.2191292](https://doi.org/10.1080/10705511.2023.2191292)
- **R49.** Bechger TM, Maris G. A statistical test for differential item pair functioning. *Psychometrika*. 2015;80(2):317-340. doi:10.1007/s11336-014-9408-y. PMID: 25223228.
  - **Supports:** DIF is identified only relative to other items, so uniform under-reporting across all items is not identifiable. **Cite in:** D (key limitation); M (anchor choice).
  - **Facts [ABS]:**
    - "DIF is defined in terms of the relative difficulties of pairs of items and not in terms of the difficulties of individual items."
    - "the difficulty of an item is not identified from the observations, whereas the relative difficulties are."
  - Source: [PubMed 25223228](https://pubmed.ncbi.nlm.nih.gov/25223228/)
- **R50.** Choi SW, Gibbons LE, Crane PK. lordif: an R package for detecting differential item functioning using iterative hybrid ordinal logistic regression/item response theory and Monte Carlo simulations. *J Stat Softw*. 2011;39(8):1-30. doi:10.18637/jss.v039.i08. PMID: 21572908; PMCID: PMC3093114.
  - **Supports:** logistic-regression DIF with IRT purification, and its effect-size conventions. **Cite in:** M (sensitivity DIF method).
  - **Facts:**
    - [ABS] "a Monte Carlo simulation approach was incorporated to derive empirical criteria for various DIF statistics and effect size measures."
    - [FT, prior notes] Pseudo-R² guidelines credited to Zumbo: negligible < 0.13, moderate 0.13–0.26, large > 0.26. "a 10% change in β1 is roughly equivalent to 0.02 in Nagelkerke's R²."
  - **Attribution note:** the brief's "Crane et al. 2011 (lordif)" is first-authored by **Choi SW**; Crane PK is the last author.
  - Source: [PMC3093114](https://pmc.ncbi.nlm.nih.gov/articles/PMC3093114/)
- **R51.** Zumbo BD. *A Handbook on the Theory and Methods of Differential Item Functioning (DIF): Logistic Regression Modeling as a Unitary Framework for Binary and Likert-Type (Ordinal) Item Scores*. Directorate of Human Resources Research and Evaluation, Department of National Defense; 1999.
  - **Supports:** the logistic-regression DIF framework and R² effect sizes. **Cite in:** M.
  - **Facts [ABS-level, catalogue/author page]:**
    - The citation as given on the author's page: "Zumbo, B. D. (1999)… Ottawa ON: Directorate of Human Resources Research and Evaluation, Department of National Defense."
    - PDF at http://faculty.educ.ubc.ca/zumbo/DIF/handbook.pdf. I did not open it (U11).
  - Source: [UBC Zumbo DIF page](https://faculty.educ.ubc.ca/zumbo/DIF/)
- **R52.** Rosseel Y. lavaan: an R package for structural equation modeling. *J Stat Softw*. 2012;48(2). doi:10.18637/jss.v048.i02.
  - **Supports:** software (WLSMV/MIMIC/MGCFA in R). **Cite in:** M.
  - **Facts [ABS]:** lavaan provides "a free, fully open-source, but commercial-quality package for latent variable modeling."
  - Crossref gives no page range; the commonly cited 1–36 is unverified (U8).
  - Source: [doi:10.18637/jss.v048.i02](https://doi.org/10.18637/jss.v048.i02)
- **R53.** Lumley T. Analysis of complex survey samples. *J Stat Softw*. 2004;9(8). doi:10.18637/jss.v009.i08.
  - **Supports:** design-based estimation and replicate-weight designs in R. **Cite in:** M.
  - **Facts [ABS]:** "The sampling scheme can be explicitly described or represented by replication weights. Variance estimation uses either replication or linearisation."
  - Page range not in Crossref (U8).
  - Source: [doi:10.18637/jss.v009.i08](https://doi.org/10.18637/jss.v009.i08)
- **R54.** Rao JNK, Wu CFJ, Yue K. Some recent work on resampling methods for complex surveys. *Surv Methodol*. 1992;18(2):209-217.
  - **Supports:** replication and bootstrap variance for complex designs (cited for the rescaled bootstrap). **Cite in:** M.
  - **Facts [FT, OCR of p. 209]:**
    - Header: "Survey Methodology, December 1992, Vol. 18, No. 2, pp. 209-217, Statistics Canada."
    - Abstract: "Resampling methods for inference with complex survey data include the jackknife, balanced repeated replication (BRR) and the bootstrap. We review some recent work on these methods for standard error and confidence interval estimation."
  - **Note:** the abstract does not use the term "rescaled bootstrap". That attribution (rescaling applied to the weights) comes from secondary sources (U15).
  - Source: [Statistics Canada 12-001-X199200214486](https://www150.statcan.gc.ca/n1/en/catalogue/12-001-X199200214486)
- **R55.** Holm S. A simple sequentially rejective multiple test procedure. *Scand J Stat*. 1979;6:65-70. JSTOR: 4615733.
  - **Supports:** familywise error control across items and tests. **Cite in:** M.
  - **Facts [ABS, OpenAlex]:**
    - "a simple and widely applicable multiple test procedure of the sequentially rejective type, i.e. hypotheses are rejected one at a time until no further rejections can be done."
    - "the test has a prescribed level of significance protection against error of the first kind for any combination of true hypotheses."
  - The issue number is not verified (U7).
  - Source: [OpenAlex record, DOI 10.2307/4615733](https://api.openalex.org/works/doi:10.2307/4615733)
- **R56.** Bieler GS, Brown GG, Williams RL, Brogan DJ. Estimating model-adjusted risks, risk differences, and risk ratios from complex survey data. *Am J Epidemiol*. 2010;171(5):618-623. doi:10.1093/aje/kwp440. PMID: 20133516.
  - **Supports:** design-based adjusted prevalence ratios via predictive margins. **Cite in:** M.
  - **Facts [ABS]:**
    - "model-adjusted risks, risk differences, and risk ratio estimates can be obtained directly from logistic regression models in the complex sample survey setting."
    - "Point estimates… are obtained from average marginal predictions in the fitted logistic regression model." Standard errors come "via linearization or a replication method."
  - Source: [PubMed 20133516](https://pubmed.ncbi.nlm.nih.gov/20133516/)

### Inferences
- **Methods justification paragraph:**
  - MIMIC with WLSMV is primary because the Spanish group is the smaller focal group, and MIMIC detects uniform DIF more accurately than two-group IRT in that setting [R39].
  - MIMIC has direct precedent for Spanish/English DIF [R41, R32].
  - It cannot capture loading (non-uniform) DIF [R44], hence the secondary MGCFA with categorical identification [R42, R43] and size-aware fit criteria [R45, R46].
  - Anchor contamination can produce false positives [R40], so anchor-sensitivity or alignment analyses [R47] are warranted.
- **Key Discussion limitation.**
  - Because only relative item difficulties are identified [R49], a uniform Spanish-language shift across all household items would be absorbed into the latent mean and could not be detected.
  - The OR estimates (about 0.36–0.63) are therefore *relative* to whatever items serve as anchors. If the household-dysfunction factor follows Ford (R6), those are alcohol and divorce; this depends on the manuscript's actual model specification, which I have not seen.
  - "unavoidable ambiguity" [R48] should be acknowledged.
- **Effect sizes.** Jones's finding that DIF explained two-thirds of a language gap [R41] gives a natural way to report impact: the share of the crude language gap explained by DIF.

### Gaps
- Numeric fit-change cutoffs (Chen 2007; Rutkowski & Svetina 2017) were not verified from primary full texts (U9, U10).
- The Zumbo handbook PDF was not opened (U11).
- I found no MIMIC simulation study tailored to complex-survey, design-weighted WLSMV with about 25–30% focal groups (my search was not exhaustive).

---

## Q7. Data documentation: BRFSS overview, weighting, module and version files, and pooling; CHIS sample design, languages, replicate weights and pooling; STROBE

### Takeaway
- **BRFSS Spanish wording varies by state.** CDC's 2023 BRFSS Overview states that "Specific wording of the Spanish version of the questionnaire may be adapted by the states". This closes an open question in the prior notes.
- **BRFSS weights and module data.** BRFSS raking margins do not include language. Module data must be analysed with version-specific weights (_LCPWTV1–3) plus _STSTR and _PSU.
- **No CDC multi-year pooling guidance.** I found none for BRFSS. A CDC-coauthored paper states that CDC provides no guidance on re-weighting aggregated state samples (Iachan 2016, O2).
- **CHIS.** Six interview languages; variance from 80 paired-jackknife (JK2) replicate weights. UCLA documents how to divide base and replicate weights when pooling years.

### Cited Findings
- **R57.** Centers for Disease Control and Prevention. *Behavioral Risk Factor Surveillance System: 2023 BRFSS Overview*. Centers for Disease Control and Prevention; 2024. Accessed November 2, 2026. https://www.cdc.gov/brfss/annual_data/2023/pdf/Overview_2023-508.pdf
  - **Supports:** the description of BRFSS, Spanish translation practice and weighting. **Cite in:** M (data); D (translation heterogeneity).
  - **Publication date:** the year is inferred from release with the 2023 annual data; the PDF date was not checked.
  - **Facts [FT]:**
    - **p. 4:** "If a significant portion of any state's population does not speak English, states have the option of translating the questionnaire into other languages. Currently, CDC provides a Spanish version of the core questionnaire and optional modules. Specific wording of the Spanish version of the questionnaire may be adapted by the states to fit the needs of their Hispanic populations."
    - **p. 2:** "In 2011, a new weighting methodology called iterative proportional fitting (or 'raking') replaced the poststratification method… The 2023 BRFSS raking method includes categories of age by sex, detailed race and ethnicity groups, education levels, marital status, regions within states, sex by race or ethnicity, telephone source, renter or owner status, and age by race or ethnicity." Language is not a margin.
    - **p. 1:** "All the responses were self-reported; proxy interviews are not conducted."
    - **p. 5:** "The core portion of the questionnaire lasts an average of 17 minutes"; modules "generally… add 5 to 10 minutes."
    - **Coverage:** "During 2023, 48 states, the District of Columbia, Guam, Puerto Rico, and the US Virgin Islands collected BRFSS data."
  - Source: [CDC BRFSS 2023 Overview (PDF)](https://www.cdc.gov/brfss/annual_data/2023/pdf/Overview_2023-508.pdf)
- **R58.** Centers for Disease Control and Prevention. *Complex Sampling Weights and Preparing 2023 BRFSS Module Data for Analysis*. July 2024. Accessed November 2, 2026. https://www.cdc.gov/brfss/annual_data/2023/pdf/Complex-Sampling-Weights-and-Preparing-Module-Data-for-Analysis-2023-508.pdf
  - **Supports:** using version files and weights for ACE module data, and the design variables. **Cite in:** M.
  - **Facts [FT, p. 3]:**
    - "Use Version 1, Version 2, and/or Version 3 Combined Landline Telephone and Cell Phone data sets if states collected multiple version questionnaires."
    - "researchers conducting complex sampling analyses from the core-only section should use the variable _LLCPWT for weighting, _STSTR for stratification, and the variable _PSU for primary sampling unit."
    - Version weights are _LCPWTV1/_LCPWTV2/_LCPWTV3.
    - Example 1 (p. 5) shows "how to combine and reweight data from multiple data sets."
  - My search of this document found no guidance on pooling multiple **years**.
  - Annual editions exist (e.g., a [2025 edition](https://www.cdc.gov/brfss/annual_data/2025/pdf/Complex-Sampling-Weights-and-Preparing-Module-Data-for-Analysis-2025-508.pdf)); cite the edition for each year used, or this one as representative.
  - Source: [CDC 2023 module-weights document (PDF)](https://www.cdc.gov/brfss/annual_data/2023/pdf/Complex-Sampling-Weights-and-Preparing-Module-Data-for-Analysis-2023-508.pdf)
- **R59.** California Health Interview Survey. *CHIS 2023 Methodology Series: Report 5—Weighting and Variance Estimation*. Prepared by Sherr S, Best J, Goyle A, Langdale K, Engle-Bauer M (SSRS). UCLA Center for Health Policy Research; September 2024. Accessed November 2, 2026. https://healthpolicy.ucla.edu/sites/default/files/2024-09/chis_2023_methodologyreport5_weighting_final_082924.pdf
  - **Supports:** CHIS languages and replicate-weight variance estimation. **Cite in:** M.
  - **Facts [FT]:**
    - **p. 14, §1.4:** "interviews were conducted in six languages: English, Spanish, Chinese (Mandarin and Cantonese dialect), Vietnamese, Korean, and Tagalog. These languages were chosen based on analysis of ACS 2021 5-year data."
    - **p. 87, §9.2:** "CHIS 2023 employed similar methodology as in past rounds of CHIS—a paired-unit grouped jackknife (GJK) replication with R=80 replicates." Variance can alternatively use "Taylor Series linearization."
    - **p. 88, §9.3:** "A paired jackknife replication method (JK2) was used for computing variances in CHIS 2023… A total of 80 replicates were created to maintain the same degrees of freedom as in previous rounds."
  - Companion report from prior notes: [CHIS 2021–2022 Report 2 (Data Collection)](https://healthpolicy.ucla.edu/sites/default/files/2023-09/chis_2021_2022_methodologyreport2_datacollection_final_09112023.pdf), Table 6-12: Spanish adult interviews = 2,154 (645 CATI, 1,509 web) (O25).
- **R60.** UCLA Center for Health Policy Research. CHIS data resources: weighting and pooling guidance. Webpage. Accessed November 2, 2026. https://healthpolicy.ucla.edu/our-work/california-health-interview-survey-chis/access-chis-data/resources
  - **Supports:** how CHIS 2021–2025 was pooled and how replicate-weight variance was specified. **Cite in:** M.
  - **Facts [FT, read via WebFetch]:**
    - "There are 80 replicate weights for each CHIS data set, and all 80 should be used simultaneously."
    - Pooling two one-year files: "For both years, the new base weight will be half of the original base weight", and the replicate weights are halved too.
    - "The final number of replicate weights created after pooling equals the number of data files used" × 80.
    - Stata: `svyset [pw=fnwgt0], jkrw(fnwgt1-fnwgt160, multiplier(1)) vce(jack) mse`. R: `type = "other"`, `scale = 1`, `rscales = 1`, `mse = TRUE`.
  - The older URL (`/chis/analyze/Pages/sample-code-pooling.aspx`) returned 403 to WebFetch.
  - Source: [CHIS Resources page](https://healthpolicy.ucla.edu/our-work/california-health-interview-survey-chis/access-chis-data/resources)
- **R61.** von Elm E, Altman DG, Egger M, Pocock SJ, Gøtzsche PC, Vandenbroucke JP; STROBE Initiative. The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. *Lancet*. 2007;370(9596):1453-1457. doi:10.1016/S0140-6736(07)61602-X. PMID: 18064739.
  - **Supports:** the reporting guideline for this cross-sectional study. **Cite in:** M.
  - **Facts [ABS]:** "a checklist of 22 items (the STROBE statement)… 18 items are common to all three study designs and four are specific for cohort, case-control, or cross-sectional studies."
  - Source: [PubMed 18064739](https://pubmed.ncbi.nlm.nih.gov/18064739/)

### Inferences
- **Methods wording for BRFSS.**
  - "ACE module data were taken from the combined landline/cell files and, for states fielding the module on a split questionnaire, from version files, using the corresponding final weights with _STSTR and _PSU [R58]."
  - "CDC provides no published guidance for pooling multiple BRFSS years; we divided weights by the number of pooled years (a common convention) and examined sensitivity." That the convention is common comes from community sources, not CDC. If cited, use Iachan 2016 (O2) only for the narrower point about state aggregation.
- **Translation heterogeneity.** State-adaptable Spanish wording [R57] means the BRFSS "Spanish" condition may bundle several translations. This is a Discussion limitation, and an argument for the CHIS replication, which uses a single centrally produced translation [R59].
- **Weights do not calibrate to language.** BRFSS raking margins exclude language [R57]. Weighted estimates by language therefore rest on calibration to other margins.

### Gaps
- **BRFSS 2024 and 2025 documents** were not retrieved; the 2023 documents serve as representative.
- **CHIS 2024 and 2025.** Report 5 and the language counts for these years were not retrieved. Whether CHIS 2025 data have been released was not verified.
- **CDC data-quality report.** The BRFSS Data Quality Report (response rates) was not retrieved. Pierannunzi 2013 (O23) is an optional verified review of BRFSS reliability and validity.

---

## Q8. Optional verified extras, unverified or partially verified items, and attribution corrections

### Takeaway
- **Optional extras.** O1–O28 below are verified (Crossref/PubMed metadata; facts as labelled) but optional. They expand the main list beyond about 60 if needed.
- **Partially verified.** U1–U20 are references or facts whose metadata or content could not be fully verified. Do not quote their numbers until checked.
- **Attribution corrections.**
  - The lordif paper is first-authored by Choi SW.
  - "Woods 2009" is ambiguous (two papers).
  - Kim 2016 used CHIS **2009**.
  - The 46.1% in Llabre 2017 belongs to the "more than one/other heritage" group, not Puerto Ricans (38.1%).

### Cited Findings
**Optional verified extras (AMA; facts labelled)**
- **O1.** Jöreskog KG, Goldberger AS. Estimation of a model with multiple indicators and multiple causes of a single latent variable. *J Am Stat Assoc*. 1975;70(351a):631-639. doi:10.1080/01621459.1975.10482485.
  - [ABS] The model has "multiple indicators and multiple causes of a single latent variable", with ML estimators derived.
  - Origin of MIMIC (M). — [doi](https://doi.org/10.1080/01621459.1975.10482485)
- **O2.** Iachan R, Pierannunzi C, Healey K, Greenlund KJ, Town M. National weighting of data from the Behavioral Risk Factor Surveillance System (BRFSS). *BMC Med Res Methodol*. 2016;16(1):155. doi:10.1186/s12874-016-0255-7. PMID: 27842500; PMCID: PMC5109644.
  - [FT, Background] "Currently, CDC provides no additional guidance to BRFSS data users on how to adjust the weights provided for each individual state sample when they try to aggregate the state samples."
  - [ABS] Aggregating states without accounting for state-level sampling "could introduce bias."
  - Use in: M. — [PMC5109644](https://pmc.ncbi.nlm.nih.gov/articles/PMC5109644/)
- **O3.** Kreuter F, Presser S, Tourangeau R. Social desirability bias in CATI, IVR, and web surveys: the effects of mode and question sensitivity. *Public Opin Q*. 2008;72(5):847-865. doi:10.1093/poq/nfn063.
  - [ABS] Random assignment to CATI, IVR or Web, validated against university records: "Web administration increased the level of reporting of sensitive information and reporting accuracy relative to conventional CATI."
  - Use in: D (CHIS web vs BRFSS phone). — [doi](https://doi.org/10.1093/poq/nfn063)
- **O4.** Villatoro AP, Morales ES, Mays VM. Family culture in mental health help-seeking and utilization in a nationally representative sample of Latinos in the United States: the NLAAS. *Am J Orthopsychiatry*. 2014;84(4):353-363. doi:10.1037/h0099844. PMID: 24999521; PMCID: PMC4194077.
  - [ABS] Among Latinos with need (N = 527), "One-third… used any type of service." "High behavioral familismo was significantly associated with increased odds of using informal or religious services, but not specialty or medical services."
  - Use in: D (familismo). — [PubMed 24999521](https://pubmed.ncbi.nlm.nih.gov/24999521/)
- **O5.** Barry CL, McGinty EE, Pescosolido BA, Goldman HH. Stigma, discrimination, treatment effectiveness, and policy: public views about drug addiction and mental illness. *Psychiatr Serv*. 2014;65(10):1269-1272. doi:10.1176/appi.ps.201400140. PMID: 25270497; PMCID: PMC4285770.
  - [ABS] N = 709. "Respondents held significantly more negative views toward persons with drug addiction"; more were "unwilling to have a person with drug addiction marry into their family."
  - Use in: D. — [PubMed 25270497](https://pubmed.ncbi.nlm.nih.gov/25270497/)
- **O6.** Merrick MT, Ford DC, Ports KA, et al. Vital signs: estimated proportion of adult health problems attributable to adverse childhood experiences and implications for prevention—25 states, 2015–2017. *MMWR Morb Mortal Wkly Rep*. 2019;68(44):999-1005. doi:10.15585/mmwr.mm6844e1. PMID: 31697656; PMCID: PMC6837472.
  - [ABS] "Nearly one in six adults in the study population (15.6%) reported four or more types." Population attributable fractions ranged up to "44.1% for depression."
  - Use in: I ¶1. — [PubMed 31697656](https://pubmed.ncbi.nlm.nih.gov/31697656/)
- **O7.** Centers for Disease Control and Prevention (CDC). Adverse childhood experiences reported by adults—five states, 2009. *MMWR Morb Mortal Wkly Rep*. 2010;59(49):1609-1613. PMID: 21160456.
  - PubMed lists CDC as corporate author. The MMWR byline reads "Reported by L Bynum… T Griffin… DL Ridings… KS Wynkoop… RF Anda… VJ Edwards… TW Strine… Y Liu… LR McKnight-Eily… JB Croft."
  - [FT] "26,229 adults in five states using the 2009 ACE module of the Behavioral Risk Factor Surveillance System (BRFSS)… 59.4% of respondents reported having at least one ACE, and 8.7% reported five or more ACEs."
  - Use in: I (module history). — [MMWR mm5949a1](https://www.cdc.gov/mmwr/preview/mmwrhtml/mm5949a1.htm)
- **O8.** Reuben A, Moffitt TE, Caspi A, et al. Lest we forget: comparing retrospective and prospective assessments of adverse childhood experiences in the prediction of adult health. *J Child Psychol Psychiatry*. 2016;57(10):1103-1112. doi:10.1111/jcpp.12621. PMID: 27647050; PMCID: PMC5234278.
  - [ABS] Dunedin cohort, N = 1,037: "moderate agreement (r = .47, p < .001; weighted Kappa = .31, 95% CI: .27-.35)."
  - Use in: D. — [PubMed 27647050](https://pubmed.ncbi.nlm.nih.gov/27647050/)
- **O9.** Colman I, Kingsbury M, Garad Y, et al. Consistency in adult reporting of adverse childhood experiences. *Psychol Med*. 2016;46(3):543-549. doi:10.1017/S0033291715002032. PMID: 26511669.
  - [ABS] 7,466 Canadian adults reporting in 1994/95 and 2006/07: "39% were inconsistent in their reports." Depression and distress were associated with new reporting.
  - Use in: D. — [PubMed 26511669](https://pubmed.ncbi.nlm.nih.gov/26511669/)
- **O10.** Loria H, Caughy M. Prevalence of adverse childhood experiences in low-income Latino immigrant and nonimmigrant children. *J Pediatr*. 2018;192:209-215.e1. doi:10.1016/j.jpeds.2017.09.056. PMID: 29246345.
  - [ABS] 2+ ACEs: "Latino immigrant children had a lower prevalence (13%…) compared with nonimmigrant Latino children (40%…)."
  - Use in: I/D. — [PubMed 29246345](https://pubmed.ncbi.nlm.nih.gov/29246345/)
- **O11.** Vega WA, Kolody B, Aguilar-Gaxiola S, Alderete E, Catalano R, Caraveo-Anduaga J. Lifetime prevalence of DSM-III-R psychiatric disorders among urban and rural Mexican Americans in California. *Arch Gen Psychiatry*. 1998;55(9):771-778. doi:10.1001/archpsyc.55.9.771. PMID: 9736002.
  - [ABS] Any disorder: "24.9% [immigrants], compared with 48.1% among US-born respondents."
  - Use in: D. — [PubMed 9736002](https://pubmed.ncbi.nlm.nih.gov/9736002/)
- **O12.** Lee SJ, Altschul I. Spanking of young children: do immigrant and U.S.-born Hispanic parents differ? *J Interpers Violence*. 2015;30(3):475-498. doi:10.1177/0886260514535098. PMID: 24923887.
  - [ABS] "FB Hispanic mothers and fathers used less spanking toward their young children" (n = 1,089 mothers; 650 fathers).
  - Use in: D (physical-abuse parity). — [PubMed 24923887](https://pubmed.ncbi.nlm.nih.gov/24923887/)
- **O13.** Klevens J, Mercer Kollar L, Rizzo G, O'Shea G, Nguyen J, Roby S. Commonalities and differences in social norms related to corporal punishment among Black, Latino and White parents. *Child Adolesc Soc Work J*. 2019;36(1):19-28. doi:10.1007/s10560-018-0591-z. PMID: 32327878; PMCID: PMC7177180.
  - [ABS] "Spanking was most frequent among Latinos (73%) and lowest among White parents (59%)."
  - Use in: D. — [PubMed 32327878](https://pubmed.ncbi.nlm.nih.gov/32327878/)
- **O14.** Guarnaccia PJ, Lewis-Fernández R, Marano MR. Toward a Puerto Rican popular nosology: nervios and ataque de nervios. *Cult Med Psychiatry*. 2003;27(3):339-366. doi:10.1023/A:1025303315932. PMID: 14510098.
  - [ABS] "nervios is more than a diffuse idiom of distress… there are different categories and experiences of nervios."
  - Use in: D. — [PubMed 14510098](https://pubmed.ncbi.nlm.nih.gov/14510098/)
- **O15.** Fontes LA, Plummer C. Cultural issues in disclosures of child sexual abuse. *J Child Sex Abus*. 2010;19(5):491-518. doi:10.1080/10538712.2010.512520. PMID: 20924908.
  - [ABS] "Cultural norms affect the likelihood that child sexual abuse will be discovered by an adult or disclosed by a child… [and] whether abused children's families will report."
  - Use in: D. — [PubMed 20924908](https://pubmed.ncbi.nlm.nih.gov/20924908/)
- **O16.** Lee S, Schwarz N. Question context and priming meaning of health: effect on differences in self-rated health between Hispanics and non-Hispanic Whites. *Am J Public Health*. 2014;104(1):179-185. doi:10.2105/AJPH.2012.301055. PMID: 23678900; PMCID: PMC3910022.
  - [ABS, prior notes] Context "influenced SRH reports of Spanish speakers (and Hispanics) significantly but not of English speakers."
  - Use in: D. — [PubMed 23678900](https://pubmed.ncbi.nlm.nih.gov/23678900/)
- **O17.** Lee S, Nguyen HA, Tsui J. Interview language: a proxy measure for acculturation among Asian Americans in a population-based survey. *J Immigr Minor Health*. 2011;13(2):244-252. doi:10.1007/s10903-009-9278-z. PMID: 19639411; PMCID: PMC3056132.
  - [ABS] CHIS 2003: "Interview language may serve as a better measure for acculturation especially among foreign-born populations."
  - Use in: M/D (interpreting language as an exposure). — [PubMed 19639411](https://pubmed.ncbi.nlm.nih.gov/19639411/)
- **O18.** Crane PK, Gibbons LE, Jolley L, van Belle G. Differential item functioning analysis with ordinal logistic regression techniques: DIFdetect and difwithpar. *Med Care*. 2006;44(11 suppl 3):S115-S123. doi:10.1097/01.mlr.0000245183.28384.ed. PMID: 17060818.
  - [ABS] On the MMSE, "Five items were found to have DIF related to language," using IRT-purified ordinal logistic regression.
  - Use in: M/D. — [PubMed 17060818](https://pubmed.ncbi.nlm.nih.gov/17060818/)
- **O19.** Woods CM. Empirical selection of anchors for tests of differential item functioning. *Appl Psychol Meas*. 2009;33(1):42-57. doi:10.1177/0146621607314044.
  - [ABS, prior notes] "Group-invariant anchors were more difficult to identify as the percentage of differentially functioning items increased."
  - Use in: M. — [doi](https://doi.org/10.1177/0146621607314044)
- **O20.** Flora DB, Curran PJ. An empirical evaluation of alternative methods of estimation for confirmatory factor analysis with ordinal data. *Psychol Methods*. 2004;9(4):466-491. doi:10.1037/1082-989X.9.4.466. PMID: 15598100; PMCID: PMC3153362.
  - [ABS] "robust WLS performed well across all conditions"; full WLS "performed adequately only at the largest sample size."
  - Use in: M (WLSMV). — [PubMed 15598100](https://pubmed.ncbi.nlm.nih.gov/15598100/)
- **O21.** Oberski D. lavaan.survey: an R package for complex survey analysis of structural equation models. *J Stat Softw*. 2014;57(1). doi:10.18637/jss.v057.i01.
  - Metadata only (Crossref). Use in: M (design-based SEM in R). — [doi](https://doi.org/10.18637/jss.v057.i01)
- **O22.** Asparouhov T. Sampling weights in latent variable modeling. *Struct Equ Modeling*. 2005;12(3):411-434. doi:10.1207/s15328007sem1203_4.
  - Metadata only (Crossref). Use in: M (weights in WLSMV). — [doi](https://doi.org/10.1207/s15328007sem1203_4)
- **O23.** Pierannunzi C, Hu SS, Balluz L. A systematic review of publications assessing reliability and validity of the Behavioral Risk Factor Surveillance System (BRFSS), 2004–2011. *BMC Med Res Methodol*. 2013;13:49. doi:10.1186/1471-2288-13-49. PMID: 23522349; PMCID: PMC3622569.
  - [ABS] "BRFSS prevalence rates were comparable to other national surveys which rely on self-reports."
  - Use in: M. — [PubMed 23522349](https://pubmed.ncbi.nlm.nih.gov/23522349/)
- **O24.** Centers for Disease Control and Prevention. *2023 BRFSS Weighting Description*.
  - [FT, p. 2] "BRFSS rakes the design weight to 8 margins (sex by age group, race/ethnicity, education, marital status, tenure, sex by race/ethnicity, age group by race/ethnicity, and phone ownership)", plus regional and county margins where applicable.
  - Use in: M. — [PDF](https://www.cdc.gov/brfss/annual_data/2023/pdf/2023-Weightning-Description-508.pdf)
- **O25.** California Health Interview Survey. *CHIS 2021-2022 Methodology Series: Report 2—Data Collection Methods*. UCLA Center for Health Policy Research; 2023.
  - [FT, prior notes] Instruments were administered in "English, Spanish, Chinese (Mandarin and Cantonese dialects), Vietnamese, Korean, and Tagalog." Table 6-12: Spanish adult interviews 2,154 (CATI 645; web 1,509).
  - The report's narrative counts conflict with its tables (see prior notes).
  - Use in: M. — [PDF](https://healthpolicy.ucla.edu/sites/default/files/2023-09/chis_2021_2022_methodologyreport2_datacollection_final_09112023.pdf)
- **O26.** Cheung GW, Rensvold RB. Evaluating goodness-of-fit indexes for testing measurement invariance. *Struct Equ Modeling*. 2002;9(2):233-255. doi:10.1207/S15328007SEM0902_5.
  - Metadata only; the ΔCFI ≤ −.01 convention is per prior notes. Use in: M.
- **O27.** Thissen D, Steinberg L, Kuang D. Quick and easy implementation of the Benjamini-Hochberg procedure for controlling the false positive rate in multiple comparisons. *J Educ Behav Stat*. 2002;27(1):77-83. doi:10.3102/10769986027001077.
  - Metadata only. Use in: M (if FDR is used instead of Holm).
- **O28.** Meredith W. Measurement invariance, factor analysis and factorial invariance. *Psychometrika*. 1993;58(4):525-543. doi:10.1007/BF02294825.
  - Metadata only. Use in: M (definition of invariance).

**Unverified or partially verified (what is missing)**
- **U1.** Dube SR, Williamson DF, Thompson T, Felitti VJ, Anda RF. Assessing the reliability of retrospective reports of adverse childhood experiences among adult HMO members attending a primary care clinic. *Child Abuse Negl*. 2004;28(7):729-737. doi:10.1016/j.chiabu.2003.08.009. PMID: 15261468.
  - Metadata verified. **No abstract** in PubMed, Crossref or OpenAlex, and ScienceDirect returned 403. The test–retest κ values are **not verified**.
- **U2.** Phillips SD, Gates T. A conceptual framework for understanding the stigmatization of children of incarcerated parents. *J Child Fam Stud*. 2011;20(3):286-294. doi:10.1007/s10826-010-9391-6.
  - Metadata verified. No abstract retrievable (Springer login redirect). Content unverified.
- **U3.** Krumpal I. Determinants of social desirability bias in sensitive surveys: a literature review. *Qual Quant*. 2013;47(4):2025-2047. doi:10.1007/s11135-011-9640-9.
  - Metadata verified; content unverified.
- **U4.** Dallaire DH, Ciccone A, Wilson LC. Teachers' experiences with and expectations of children with incarcerated parents. *J Appl Dev Psychol*. 2010;31(4):281-290. doi:10.1016/j.appdev.2010.04.001.
  - Metadata verified; no abstract retrieved.
- **U5.** Saunders V. What does your dad do for a living? Children of prisoners and their experiences of stigma. *Child Youth Serv Rev*. 2018;90:21-27. doi:10.1016/j.childyouth.2018.05.012.
  - Metadata verified; no abstract retrieved.
- **U6.** Fontes LA. Sin vergüenza: addressing shame with Latino victims of child sexual abuse and their families. *J Child Sex Abus*. 2007;16(1):61-83. doi:10.1300/J070v16n01_04. PMID: 17255077.
  - Metadata verified; no abstract in PubMed.
- **U7.** Holm 1979 issue number. Volume 6 and pages 65–70 are verified (OpenAlex). The issue (commonly cited as 2) is not; the JSTOR DOI 10.2307/4615733 returns 404 at Crossref.
- **U8.** Page ranges for Rosseel 2012 (commonly 1–36) and Lumley 2004 (commonly 1–19) are not in Crossref metadata.
- **U9.** Rutkowski & Svetina 2017 numeric criteria (ΔCFI ≥ −0.004; ΔRMSEA ≤ 0.01). These come only from a secondary summary (prior notes); the primary abstract gives no numbers.
- **U10.** Chen 2007 numeric cutoffs were not extracted (full text not accessed).
- **U11.** Zumbo 1999 handbook contents. The PDF was not opened. Pseudo-R² thresholds (< 0.13 / 0.13–0.26 / > 0.26) are known only via Choi et al. 2011 [FT, prior notes].
- **U12.** CDC 2019 *Preventing ACEs* document. The citation is verified via Swedo 2023's reference list and a CDC Stacks catalogue listing. The document was not opened, and its original URL now redirects.
- **U13.** Merrick 2018 ≥4-ACE prevalence. Not in the abstract; full text not accessible (PMC HTML blocked; JAMA site not tried). Use Swedo 2023 for ≥4 figures.
- **U14.** Felitti 1998 percentage with ≥4 categories. Full text not accessed.
- **U15.** Rao–Wu–Yue 1992 "rescaled bootstrap" attribution. The article's abstract mentions the jackknife, BRR and bootstrap but not "rescaling". The description of the method (scale adjustment applied to the survey weights) is secondary (search snippet). Verify in the article body if the Methods text says "rescaled bootstrap (Rao, Wu & Yue 1992)".
- **U16.** CHIS 2024/2025 methodology reports (weighting; languages) and CHIS 2025 data availability were not retrieved.
- **U17.** BRFSS 2024/2025 Overview and module-weight documents were not read; the 2023 editions were used.
- **U18.** The CDC Spanish ACE module wording for BRFSS 2021–2025 is not publicly posted (prior notes). Combined with R57 (state adaptation), the exact Spanish stimulus is unknown for most Spanish-interview respondents.
- **U19.** Umoga 2026 Harvard dissertation (BRFSS 2021–2023 multigroup latent class analysis across six racial/ethnic groups). Abstract only; embargoed until 2027-04-19 (prior notes).
- **U20.** Jensen 2024 second author's middle initial: Crossref "Bernard D" vs full text "Bernard DL". Use the full-text form.

### Inferences
- **Attribution corrections to apply in the manuscript:**
  - **lordif:** cite Choi SW, Gibbons LE, Crane PK (2011), not "Crane et al. 2011". Crane et al. 2006 (O18) is a separate *Med Care* paper on OLR-DIF with language-of-administration DIF in the MMSE.
  - **"Woods 2009":** specify the paper. The MIMIC paper is *Multivariate Behav Res* 44(1):1-27 (R39); the anchor-selection paper is *Appl Psychol Meas* 33(1):42-57 (O19).
  - **Kim et al. 2016:** used **CHIS 2009** (fielded Sept 2009–Apr 2010), not a recent CHIS cycle.
  - **Llabre 2017:** Puerto Rican ancestry 38.1%, "more than one/'other'" heritage 46.1%, Cuban 20.2%. Do not attribute 46.1% to Puerto Ricans.
  - **Merrick 2018:** the headline is "61.55% ≥1 and 24.64% ≥3", not ≥4.
  - **Mei 2022:** the text says "sixteen states" but lists 17. Cite as "2019 BRFSS (N = 97,314)" rather than repeating the state count.
- **If the main list must be cut to about 50:** move R38 (keep O1 or R38, not both), R52/R53 (keep only the software actually used), R55 (if FDR is used instead), R36 (keep R34 and R35 as counterexamples) and R18 (grey literature) to the optional list.

### Gaps
- **Not reached:** SciELO and Redalyc, ProQuest, and a direct JSTOR check for Holm 1979 (prior notes give the same coverage limits).
- **Paywalled:** Pérez 2011, Chen 2007, Rutkowski & Svetina 2017 and LaNoue & Hass 2025 were read only at abstract level, so their internal numbers are not reported.
- **Coverage:** all main-list metadata (authors, title, journal, year, volume, issue, pages, DOI, PMID) were machine-checked against Crossref and PubMed on 2026-11-02. AMA formatting (sentence-case titles, NLM abbreviations) was applied by hand, so a final proofread against the journal's style is advised.
