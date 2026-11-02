# Novelty verification: has anyone tested measurement invariance / DIF of ACE items by interview or questionnaire language (Spanish vs English)?

Verification labels used throughout:
- **[FT]** = verified from full text, read in this session (PMC XML via E-utilities, or repository PDF)
- **[ABS]** = verified from abstract, repository metadata, or search snippet only
- **[NF]** = not found (the databases and queries searched are listed in the systematic-search section below)

Search date: 2026-11-01. All PubMed, Europe PMC and OpenAlex hit counts are as of that date.

---

## Q1. Mei et al. 2022 (Health & Justice): what exactly was tested, and was language or Hispanic ethnicity examined?

### Takeaway
Mei et al. ran an EFA and then a sequential MGCFA (categorical WLSMV, theta parameterization, inside an IFA/IRT framing) on the 11 BRFSS ACE items from 2019 BRFSS (N = 97,314). Six grouping variables were tested: age, race/ethnicity (Hispanic was one level of a 5-category race variable), sex, income, transgender identity and sexual orientation. Invariance was judged only by omnibus ΔCFI/ΔTLI. **Language (QSTLANG) was never examined**: the words "language" and "Spanish" do not appear in the paper. Survey weights were never stated to be applied. No item-level DIF statistics or effect sizes were reported.

### Cited Findings
- **Citation [FT]:** Mei X, Li J, Li ZS, Huang S, Li LL, Huang YH, Liu J. "Psychometric evaluation of an Adverse Childhood Experiences (ACEs) measurement tool: an equitable assessment or reinforcing biases?" *Health & Justice* 2022;10(1):34. doi:10.1186/s40352-022-00198-2 — [PMC9706892](https://pmc.ncbi.nlm.nih.gov/articles/PMC9706892/)
- **Sample [FT]:** "We used the 2019 BRFSS sample (N = 97,314) from the BRFSS, which collected ACEs assessments from sixteen states, including Alabama, Delaware, Florida, Indiana, Iowa, Michigan, Mississippi, Missouri, New Mexico, North Dakota, Pennsylvania, Rhode Island, South Carolina, Tennessee, Virginia, West Virginia, and Wisconsin." The text says "sixteen" but lists **17** states. A separate CDC-authored analysis reports that the 2019 BRFSS ACE module data came from 21 states. — [Mei 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9706892/); [Besera et al. 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11752077/)
- **Groups tested [FT]:** "we used six nominal grouping variables, including age, race, sex, socioeconomic status, sexual identity, and sexual orientation." Race was "operationalized into five categories, including 'white only, non-Hispanic,' 'black only, non-Hispanic,' 'other race only, non-Hispanic,' 'multiracial, non-Hispanic,' 'Hispanic.'" In Table 1, Hispanic = 9.1% of the sample. Sexual orientation is 43.9% missing and gender identity 43.6% missing. — [Mei 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9706892/)
- **Method [FT]:** "we conducted a sequential Multi-group Confirmatory Factor Analysis (MGCFA)… we tested three essential forms of measurement bias or invariances, including configural, metric, and scalar." Further: "The Weighted Least Square Mean and Variance Adjusted (MLSMV) [sic] is the preferred estimator… The 'Theta' parameterizations is selected… we conducted all tests within the Item Factor Analysis (IFA)/Item Response Theory (IRT) framework." Missing data were handled by "FIML… with MLSMV estimator." No software is named, but the references cite Mplus Web Notes. — [Mei 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9706892/)
- **Model structure [FT]:** The model was a second-order factor over three first-order factors (household dysfunction, emotional/physical abuse, sexual abuse). Loadings were constrained **equal within each first-order factor**: Table 3 footnote, "First-order within-factor items are constrained to be equal but allowed to vary across groups". Table 2 accordingly shows identical λ for every item within a factor (.731, .827, .952). — [Mei 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9706892/)
- **Fit and invariance criteria [FT]:** "Model fit is 'acceptable' if… CFI/TLI… ≥ .90 and… RMSEA ≤ .08… 'good' when CFI/TLI ≥ .95 and RMSEA ≤ .05." And: "Higher-order models and those with additional measurement invariance constraints were retained if the ∆CFI and ∆TLI values were equal/less than .01." The Results text contradicts this: "passed all three levels of invariances… as the ∆CFI and ∆TLI did not exceed **.10**." In Table 3, the race comparison has ΔTLI = .010 at the second-order step, and income has ΔTLI = .011, slightly above the stated .01 rule. Every metric and scalar step has |ΔCFI| ≤ .003 and |ΔTLI| ≤ .003. — [Mei 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9706892/)
- **Decisive conclusion sentence [FT]:** "The ACEs measurement scale from the BRFSS is equitable and free from measurement bias regardless of one's age, race, sex, socioeconomic status, gender identity, and sexual orientation." — [Mei 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9706892/)
- **Latent mean differences [FT]:** Compared with non-Hispanic White respondents, Hispanic respondents scored d = .06 higher (p = .001). All group differences were d < 0.20. — [Mei 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9706892/)
- **Item-level DIF [FT]:** None. Only omnibus model comparisons were run. There were no partial-invariance searches (none were triggered, because all steps passed), no item-level threshold differences, and no DIF effect sizes. — [Mei 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9706892/)
- **Survey weights [FT]:** The word "weight" appears only in the description of BRFSS ("a stratified random sampling approach with a weighting protocol") and in unrelated contexts. The paper never states that weights, strata or PSUs were used in the models. — [Mei 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9706892/)
- **Language [FT]:** Zero occurrences of "language", "Spanish", "translat", "QSTLANG" or "DIF" in the full text. — [Mei 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9706892/)
- **Stated limitations [FT]:** Not all states collected ACEs, so generalizability is limited. Predictive accuracy is untested. Sexual minorities are likely underrepresented in a household sample, and the transgender sample was small. Recall bias may affect older respondents. EFA and CFA were run on the same sample. The 11-item content is limited ("it still lacks content validity because of the limited items (n = 11)"). Language and translation are not mentioned as limitations. — [Mei 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9706892/)
- **Other errors noticed [FT]:** In Table 2, items 3 (illegal drugs) and 4 (prison) show identical counts (91,194 / 6,120) but different percentages (91.3/8.7 vs 93.7/6.3), which looks like a copy error. The Results narrative reports the transgender difference as d = .18, but Table 4 gives d = .06 (latent mean difference .21, p = .19). The .18 appears to be copied from the sexual-orientation row. — [Mei 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9706892/)

### Inferences
- Mei et al. do not occupy the language gap. They did not test Spanish vs English. Their "Hispanic" group mixed English- and Spanish-interviewed Hispanic respondents and was compared with four other race groups in a single 5-group MGCFA.
- Three features of the method limit sensitivity to item-level DIF, especially for a small focal group (Spanish interviews are only a few percent of the BRFSS):
  - Loadings were constrained equal within each factor before testing across groups.
  - Decisions rested only on omnibus ΔCFI/ΔTLI in a very large sample.
  - No item-level thresholds were inspected.
- A proposal can therefore cite Mei as "invariance across race/ethnicity at the omnibus level, language untested, no item-level DIF, unweighted (apparently)", rather than as evidence that Hispanic respondents' items function equivalently.
- The ΔCFI/ΔTLI typo (.10 vs .01) and the ΔTLI = .011 for income are minor, but they are fair to note in a critique.

### Gaps
- It cannot be confirmed whether Mei et al. applied survey weights silently. The paper is silent, and no supplement or code exists ("pmc-prop-has-supplement no").
- The software is not stated. Mplus is inferred only from the reference list.

---

## Q2. Ford et al. 2014 (Psychology of Violence): exact citation, data, method and groups

### Takeaway
Confirmed: Ford DC, Merrick MT, Parks SE, Breiding MJ, Gilbert LK, Edwards VJ, Dhingra SS, Barile JP, Thompson WW. "Examination of the Factorial Structure of Adverse Childhood Experiences and Recommendations for Three Subscale Scores." *Psychology of Violence* 2014;4(4):432–444. doi:10.1037/a0037723 (CDC authors). The EFA used 2009 BRFSS (5 states); the CFA and MGCFA used 2010 BRFSS (DC plus 10 states). Items were dichotomized and analysed with WLSMV, with weights, strata and PSU included. **Invariance was tested only by gender and four age groups**, with no race/ethnicity and no language.

### Cited Findings
- **Citation and availability [FT]:** NIH author manuscript at [PMC4587306](https://pmc.ncbi.nlm.nih.gov/articles/PMC4587306/), PMID 26430532.
- **Data [FT]:** "Sample 1… 27,545 noninstitutionalized adults surveyed during the 2009 [BRFSS]… residents of… Arkansas, Louisiana, New Mexico, Tennessee, or Washington… 8.5% Hispanic." "Sample 2… 57,703… 2010… District of Columbia or… Hawaii, Maine, Nebraska, Nevada, Ohio, Pennsylvania, Utah, Washington, Wisconsin, or Vermont… 3.5% Hispanic." — [Ford 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC4587306/)
- **Item handling [FT]:** "the responses to the ACE items… were dichotomized to convey exposure." — [Ford 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC4587306/)
- **Weights [FT]:** "This weight along with stratum and primary sampling unit variables were included in all analyses. Data analyses were conducted in R version 3.01… and Mplus Version 7.0." — [Ford 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC4587306/)
- **Estimator and fit [FT]:** EFA "using… (WLSMV) on the tetrachoric correlations." Model-fit guidelines were "0.06 and 0.95 for RMSEA and TLI/CFI." The 2nd-order factor is just-identified, so a 3 correlated-factor model was fitted. — [Ford 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC4587306/)
- **Invariance method [FT]:** "Configural and metric measurement invariance was examined by estimating a series of nested MGCFA models using the 2010 BRFSS… Configural and metric measurement invariance were first tested by gender and then by age using four groups (18–34, 35–49, 50–64, >65 years)." The "metric" model was "a model constraining both the factor loadings and item thresholds to be equivalent across groups." For binary items this is effectively a joint loading-plus-threshold (scalar-type) test, following the Mplus User's Guide p. 485. — [Ford 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC4587306/)
- **Invariance criteria [FT]:** These were changes in fit indices without a pre-stated numeric cut-off: "a change in RMSEA of 0.001 and no change in CFI or TLI… constitute metric equivalence (Chen, 2007; Cheung & Rensvold, 2002)". Chi-square differences "were deemed to have little interpretive value." There was no item-level DIF. — [Ford 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC4587306/)
- **Language and race [FT]:** "language" appears only in an R reference. No race/ethnicity or language invariance was tested. — [Ford 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC4587306/)
- **Stated limitations [FT]:** Self-report and retrospective recall ("retrospective reports… often underestimate"). Omitted domains (bullying, community violence, neglect, parental death). Only internal structure was studied. — [Ford 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC4587306/)

### Inferences
- The earlier session's summary ("invariant across gender and age") is correct. More precisely, Ford's "metric" step already constrained thresholds, so Ford supports loading-plus-threshold equivalence across gender and age in 11 states (2009–2010) for dichotomized items.
- Ford is weighted and design-adjusted, which Mei apparently is not.
- Neither Ford nor Mei touches language.

### Gaps
- None material. The full text was accessible.

---

## Q3. Jensen, Bernard & Lanier 2024 (Child Development): citation, data, method, and whether language was considered

### Takeaway
Confirmed: Jensen TM, Bernard DL, Lanier P. "Conceptualizing adverse childhood experiences as a latent factor: Tests of measurement invariance across five racial and ethnic groups." *Child Development* 2024;95(3):e170–e185. doi:10.1111/cdev.14050. The study used NSCH 2018–2020 (N = 93,759; 9 caregiver-reported ACE items) and ran an unweighted MGCFA with WLSMV across Hispanic, NH White, NH Black, NH Asian and NH AIAN children. It found configural and full metric invariance but **failed scalar invariance**: only 3 of 11 thresholds were invariant. **Neither household language nor survey language was examined**: zero occurrences of "language" in the full text.

### Cited Findings
- **Data and groups [FT]:** "Drawing from the 2018–2020 National Survey of Children's Health (N = 93,759…), we assess the measurement invariance of a latent-factor ACE model across five groups: Hispanic children (14%) and non-Hispanic White (73%), Black (7%), Asian/Pacific Islander (5%), and American Indian/Alaskan Native (1%) children." Multiracial, "some other race" and NHPI children were excluded. — [Jensen 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11023799/)
- **Estimator [FT]:** "We implemented the… (WLSMV) estimator and a polychoric correlation input matrix… eight dichotomous items [ace3–ace10], one ordinal item [ace1]." — [Jensen 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11023799/)
- **Criteria [FT]:** "a change of less than or equal to .002-units (ΔCFI ≤ .002) being indicative of a negligible shift… (Cheung & Rensvold, 2002; Meade et al., 2008)." ΔCFI ≤ .01 was used as a sensitivity check, followed by item-by-item partial-invariance testing. — [Jensen 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11023799/)
- **Weights [FT]:** "We opted to conduct unweighted analyses… [we] simply aimed to assess equivalence of model parameters." — [Jensen 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11023799/)
- **Results [FT]:** "Full scalar invariance was unsupported… constraining all item thresholds to be equal across groups yielded a substantial decline in model CFI (ΔCFI = −.057)… thresholds for only three items could be constrained to equality." And: "only 60% of measurement parameters were invariant (12 out of 20 total parameters)", below the 80% standard for partial invariance. — [Jensen 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11023799/)
- **Language and nativity [FT]:** Nativity is reported only descriptively ("78% of participants were 3rd generation… 14%… 2nd generation"). There are no language terms anywhere. Stated limitations include treating race/ethnicity as "a single dimension of social identity, ignoring the variation within these groups", caregiver report, and the exclusion of "two or more races". — [Jensen 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11023799/)

### Inferences
- Jensen et al. are the strongest published evidence that ACE item thresholds differ across racial/ethnic groups, including Hispanic children, in a large US survey. That directly contradicts a reading of Mei as "BRFSS ACE items are bias-free for Hispanics", although the instrument (NSCH caregiver report) and criteria (ΔCFI ≤ .002 vs ≤ .01) differ.
- Because the NSCH is fielded in English and Spanish (see Campbell & Jacobs 2026 below), part of the Hispanic threshold non-invariance could be language-driven. Jensen did not test this, so it is an open question rather than a competitor finding.

### Gaps
- Jensen did not report the share of NSCH Hispanic respondents who completed the Spanish instrument. No public statement was found.

---

## Q4. Identify and characterize the Alhalel 2018 thesis, the 2026 Harvard dissertation, and the 2025 J Interpers Violence paper

### Takeaway
- **Alhalel:** Nathan Alhalel's 2018 Northwestern MPH culminating-experience paper (BRFSS 2011–2012, 9 states, 2,983 Hispanic respondents) compared weighted ACE item prevalence by questionnaire language. It found that 6 of 11 items differed and attributed this to acculturation. **No measurement-equivalence test was done.**
- **Harvard 2026:** This is almost certainly Chinyere Umoga's Harvard PhD dissertation (deposited 19 Oct 2026, embargoed until 19 Apr 2027). It used multigroup latent class analysis to test invariance of 9 BRFSS ACE indicators (2021–2023) across six racial/ethnic groups and found **non-invariant** class-defining item probabilities. Language is not mentioned in the abstract.
- **JIV 2025:** Two JIV papers first published online in 2025 fit the description. Moore, Herrenkohl & Stoddard (FFCWS; EFA/CFA plus invariance by poverty status only) and Chipalo et al. (NSCH 2022 non-English-speaking households; ACE–food insecurity regressions only). **Neither tests invariance by language.**

### Cited Findings
**Alhalel 2018 [FT, PDF read]**
- **Title:** "Prevalence and Impact of Adverse Childhood Experiences in the Hispanic Community by Questionnaire Language Preference: Behavioral Risk Factor Surveillance System (BRFSS) 2011, 2012." Culminating Experience, Northwestern University Master of Public Health. The PDF filename gives the author as Nathan Alhalel, 2018. — [Northwestern PRISM record](https://prism.northwestern.edu/records/7mt6a-brh38); DOI [10.18131/g3-a5x4-zh93](https://doi.org/10.18131/g3-a5x4-zh93)
- **Data:** 2011–2012 BRFSS from 9 states: Iowa, Minnesota, Montana, North Carolina, Oklahoma, Tennessee, Vermont, Washington and Wisconsin (2012 data only for Wisconsin). 2,983 Hispanic respondents, a weighted population of 1,855,212. "Overall, 61% of the Hispanic/Latino respondents preferred the English survey." — [Alhalel 2018](https://prism.northwestern.edu/records/7mt6a-brh38)
- **Methods:** "Chi square tests were used to determine the statistical significance of language preference differences in individual ACE items… Multiple logistic regression…" Stata 14 survey commands were used. — [Alhalel 2018](https://prism.northwestern.edu/records/7mt6a-brh38)
- **Results:** "Weighted prevalence of individual reported adverse childhood experiences were significantly different (p<0.01) in 6 of the 11 ACE items between the English and Spanish questionnaire preference groups." The English-preference group more often reported being touched sexually, living with a substance abuser, household incarceration, household mental illness and parental separation. "Those in the Spanish preference cohort were almost twice as likely to experience physical abuse (28.8% versus 15.9%)." Yet "the prevalence of Hispanic respondents in each ACE count category did not differ significantly between the two language-preference groups (data not shown)." — [Alhalel 2018](https://prism.northwestern.edu/records/7mt6a-brh38)
- **Interpretation and limitations:** The differences "may stem from differences in cultural and social norms" and acculturation (the "Hispanic paradox"). The limitations treat language preference only "as a single measure of acculturation". There are no psychometric, invariance or translation analyses. — [Alhalel 2018](https://prism.northwestern.edu/records/7mt6a-brh38)
- **Disambiguation:** OpenAlex lists a *Jonathan* Alhalel affiliated with Northwestern. His indexed works concern limited-English-proficiency and clinical topics, not this thesis, so the thesis author should be cited as Nathan Alhalel. — [OpenAlex author record](https://api.openalex.org/authors/A5078218563)

**Umoga 2026 Harvard dissertation [ABS: repository metadata and abstract; full text embargoed]**
- **Citation:** Umoga, Chinyere. 2026. "Beyond Adversity Alone: Heterogeneity in Childhood Experiences and Implications for Mental and Behavioral Health." Doctoral dissertation (PhD, Population Health Sciences), Harvard University GSAS. Advisor: Shoba Ramanadhan. Committee: Natalie Slopen and Dana McCoy. Subject keywords include "Measurement Invariance" and "Racial and Ethnic Disparities". Embargo until 2027-04-19. — [Harvard DASH handle 1/42760678](https://dash.harvard.edu/handle/1/42760678)
- **Study 1 (abstract):** "examined whether latent patterns of nine ACEs were structured similarly across six racial and ethnic groups (n = 216,439)… multigroup latent class analysis demonstrated that the class-defining probabilities were not fully invariant… between-group heterogeneity was concentrated more strongly in some ACE indicators… particularly witnessing violence between adults, and alcohol misuse, mental illness… incarceration… parental separation or divorce, emotional abuse, and physical abuse." The data were pooled 2021–2023 BRFSS. Language and Spanish are not mentioned in the abstract. — [DASH](https://dash.harvard.edu/handle/1/42760678)

**JIV candidate A [FT]:** Moore CR, Herrenkohl TI, Stoddard SA. "Factor Analysis of Adverse Childhood Experiences in the Future of Families and Child Wellbeing Study Sample." *J Interpers Violence* 2026;41(15–16):5370–5391. Epub 24 Jul 2025. doi:10.1177/08862605251355626.
- 7 early-childhood ACEs, N = 3,021, with split-half EFA then CFA (Mplus WLSMV). The result was a two-factor structure (maltreatment vs parent challenges).
- MGCFA by poverty at birth only: "Measurement invariance (including configural, metric and scalar) across our subgroups was confirmed."
- No language or ethnicity invariance was tested.
- [PMC12313238](https://pmc.ncbi.nlm.nih.gov/articles/PMC12313238/)

**JIV candidate B [ABS]:** Chipalo E, Nkwanzi V, Odii IO, Malele KP. "Parent-Reported Adverse Childhood Experiences and Food Insecurity Among Children in Non-English-Speaking Households in the United States." *J Interpers Violence* 2026;41(3–4):608–635. Epub 22 Feb 2025. doi:10.1177/08862605251315774.
- NSCH 2022, weighted sample of 4,677 children in non-English-speaking households.
- Logistic regression of food insecurity on individual and cumulative ACEs.
- No measurement analysis.
- [PubMed 39985397](https://pubmed.ncbi.nlm.nih.gov/39985397/)

### Inferences
- **Alhalel** is a direct precedent for the descriptive question: Spanish vs English BRFSS ACE item prevalences differ, with a different item profile but a similar total. It is exactly the pattern that item-level DIF analysis is designed to separate from true differences. The proposal can cite it as motivation; it is not a competitor on methods.
- **Umoga** is the closest **method** competitor in BRFSS: invariance of ACE indicators across groups including Hispanic, using recent BRFSS. However, the grouping is race/ethnicity, the framework is LCA rather than factor/IRT DIF, and language is not mentioned in the abstract. Its finding of non-invariance in BRFSS 2021–2023 contradicts Mei's "bias-free" conclusion and strengthens the rationale for a language-specific test. Because the full text is embargoed, a language sensitivity analysis inside it cannot be ruled out. Say so plainly in the proposal, and consider contacting the author.
- **JIV:** If the flagged "2025 JIV paper" was Moore et al., it overlaps only on "ACE factor structure plus invariance". If it was Chipalo et al., it overlaps only on "ACEs in non-English-speaking households". Neither tests language DIF.

### Gaps
- The full text of Umoga 2026 is embargoed. Whether any chapter or sensitivity analysis stratifies by BRFSS interview language is unknown.
- The earlier session's exact "2025 JIV" reference could not be confirmed, because two candidates match.

---

## Q5. Systematic search: is there ANY ACE invariance/DIF study by language, translation, or language of interview (any dataset or country), including Hispanic subgroups by language preference and Spanish-language literature?

### Takeaway
Exactly **one** published study was found that formally tested measurement invariance by Spanish vs English survey language in a model that includes ACE items: **Cooper & Nickodem 2021** (*Evaluation & the Health Professions*; HCHS/SOL Sociocultural Ancillary Study). Its target is a 59-item "cumulative lifetime adversity" bifactor model in which the 10-item ACE scale is one specific factor, not the ACE instrument on its own. It found weak (metric) invariance and only "partially, but not strongly, supported" strong (scalar) invariance by language preference.

No study was found that tests DIF or invariance of the **BRFSS ACE module** (or any stand-alone ACE instrument) by interview or questionnaire language, in any US survey (BRFSS, NSCH, YRBS, PRAMS, NHIS, CHIS) or in any bilingual or multi-country setting (Canada English/French, Hong Kong, Israel, South Africa, ACE-IQ multi-country). Spanish-language literature (Dialnet, Redalyc-indexed journals, SciELO-indexed journals found through web and PubMed searches) contains single-language Spanish validations, not cross-language equivalence tests.

### Cited Findings
**Closest competitor: Cooper & Nickodem 2021 [FT]**
- **Citation:** Cooper DK, Nickodem K. "Cumulative Lifetime Adversity in a National Sample of Hispanic/Latino Immigrants: Exploring Construct Validity Across Six Hispanic/Latino Groups Using Data From the HCHS/SOL Sociocultural Ancillary Study." *Eval Health Prof* 2021;44(4):348–361 (online 2020). doi:10.1177/0163278720910470 — [PMC9993236](https://pmc.ncbi.nlm.nih.gov/articles/PMC9993236/)
- **Sample:** N = 3,296 Hispanic/Latino adults born outside the mainland US. "Interviews were conducted by bilingual staff and were offered in English or Spanish - the majority of which were completed in Spanish (92%)." The ACE measure was the 10-item ACE scale (emotional, physical and sexual abuse; emotional and physical neglect; household items). It is one of five subscales in a 59-item bifactor model. — [Cooper 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC9993236/)
- **Rationale for the language test:** "only 71% of Puerto Ricans completed Spanish surveys. In order to determine that cumulative lifetime adversity group differences were not due to language differences, we performed invariance testing between the Spanish and English versions of the survey." — [Cooper 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC9993236/)
- **Criteria:** "ΔCFI ≥ −.02, ΔRMSEA ≤ .03, and ΔSRMR ≤ .03, between configural and weak invariance models and ΔCFI ≥ −.01, ΔRMSEA ≤ .01, and ΔSRMR ≤ .01 between weak and strong," plus Satorra-Bentler scaled Δχ². The approach followed Bowen & Masa (2015) for ordinal data. — [Cooper 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC9993236/)
- **Language results:** Configural CFI = .927, RMSEA = .030, SRMR = .073. Weak invariance: ΔCFI = +.017, Δχ²(112) = 123.00, p = .225. Strong invariance: "significant χ² difference test (Δχ²(132) = 299.00, p < .001) and lower CFI (Δ = −.009)." Conclusion: "interpretation of differences in a cumulative lifetime adversity score based on language preference as true differences between English and Spanish dominant speakers is partially, but not strongly, supported." — [Cooper 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC9993236/)
- **What it did not do [FT]:** It did not isolate the ACE items, report ACE item-level DIF, use BRFSS or the 11-item BRFSS wording, or analyse a US-born or non-immigrant population. Stated limitations include older immigrants in four metropolitan areas and composite Central/South American groups. — [Cooper 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC9993236/)

**Other ACE invariance/DIF studies found: none by language**
- **Rancher, Bernard & Moreland 2024 [FT]:** BRFSS 11-item ACE measure in 605 early-childhood teachers (46% White, 53% Black). MGCFA in lavaan; invariant across age and race. No Hispanic group, no language. *J Aggress Maltreat Trauma* 33(6):727–742. — [PMC11207200](https://pmc.ncbi.nlm.nih.gov/articles/PMC11207200/)
- **Krushas, Kulig & Goslar 2025 [ABS]:** 10 ACE subscales in 993 young non-college women. "Measurement invariance tests supported the psychometric equivalence of the ACEs construct across race/ethnicity" (White, Black, Hispanic). Language not mentioned. *Justice Quarterly* 42(7):1373–1409. — [doi:10.1080/07418825.2025.2451311](https://doi.org/10.1080/07418825.2025.2451311)
- **Dorri et al. 2026 [ABS: title and snippet]:** SGM-ACE scale invariance across sexual orientation and gender identity. *Psychol Sex Orientat Gend Divers*. — [doi:10.1037/sgd0000940](https://doi.org/10.1037/sgd0000940)
- **Zhang & Lippert 2026 [ABS; full text 403-blocked]:** BRFSS ACE items scored with a "two-parameter Item Response Theory (IRT) model and multiple plausible values." The abstract does not mention DIF or language. *Soc Sci Med* 395:119056. — [doi:10.1016/j.socscimed.2026.119056](https://doi.org/10.1016/j.socscimed.2026.119056)
- **Inanoglu et al. 2026 [ABS]:** ACE-IQ among 5,945 students in seven countries, including Spanish-language sites in Argentina, Spain and Uruguay, plus the US, England, Canada and South Africa. The authors tested "cross-national invariance of these associations", i.e., the ACE→mental-health paths, not item measurement invariance by language. *Child Abuse Negl* 178:108150. — [PubMed 42250494](https://pubmed.ncbi.nlm.nih.gov/42250494/)
- **Díaz-Faes, Rajan & Branas 2026 [ABS]:** Ising network of 2023 YRBS items, with network invariance (Network Comparison Test) by sex, sexual orientation and race/ethnicity including Hispanic. Not measurement invariance; no language. *Epidemiology*. — [PubMed 42725720](https://pubmed.ncbi.nlm.nih.gov/42725720/)
- **Ye et al. 2023 (PEARLS) [FT]:** Eligible caregivers were "English and/or Spanish speaking", but invariance was tested only by "age group…, gender, and PEARLS screening format." *BMC Pediatr*. — [PMC10351141](https://pmc.ncbi.nlm.nih.gov/articles/PMC10351141/)
- **Prakash et al. 2026 [ABS]:** A review or commentary calling for invariance and DIF testing of trauma measures in minoritized populations. No empirical language test. *J Trauma Stress*, doi:10.1002/jts.70097. — [PubMed 42332405](https://pubmed.ncbi.nlm.nih.gov/42332405/)
- **Sanchis et al. 2026 [ABS]:** COSMIN systematic review of 20 ACE instrument psychometric studies. Cross-language equivalence is not mentioned among the evaluated evidence. *Children* 13(8):1045. — [PubMed 42650383](https://pubmed.ncbi.nlm.nih.gov/42650383/)

**Spanish-language and Latin American literature [ABS]: single-language validations only**
- **Spain:** Villanueva, Gomis-Pomares & Basto-Pereira 2026 validated the ACE Questionnaire in 648 Spanish young adults (validity and 6-month test–retest). No cross-language comparison. *Current Psychology* 45(6). — [doi:10.1007/s12144-026-09071-z](https://doi.org/10.1007/s12144-026-09071-z)
- **Mexico:** An ACE questionnaire adaptation in 672 adults found a two-factor structure (*Psicología y Salud*). — [psicologiaysalud.uv.mx](https://psicologiaysalud.uv.mx/index.php/psicysalud/article/view/2742)
- **Mexico (ACE-IQ):** Casas-Muñoz et al. 2024, extended ACE-IQ validation in Mexican adolescents. — [PubMed 37805276](https://pubmed.ncbi.nlm.nih.gov/37805276/)
- **Ecuador:** The ACE-ASF in Ecuadorian youth showed invariance by sex. — [UPS repository](https://pure.ups.edu.ec/es/publications/psychometric-properties-of-the-adverse-childhood-experiences-abus-2/)
- **Ecuador (2026):** Ramírez et al. 2026, ACE-ASF in homosexual and heterosexual samples. — [doi:10.1186/s40359-026-04907-6](https://doi.org/10.1186/s40359-026-04907-6)
- **Chile:** Santelices et al. 2025, ACE-IQ in a Chilean community sample. — [PubMed 40150622](https://pubmed.ncbi.nlm.nih.gov/40150622/)
- **Spain (CAI):** A doctoral validation of the Cuestionario de Adversidad en la Infancia. — [Dialnet tesis 322965](https://dialnet.unirioja.es/servlet/tesis?codigo=322965)
- **Summary:** None of these compares Spanish and English versions or tests DIF by language.

#### Search log (reproducible; date 2026-11-01)

**PubMed (E-utilities esearch; [tiab] unless noted). Query → hits:**
1. `("adverse childhood experiences" OR "ACE" OR "ACEs") AND ("measurement invariance" OR "differential item functioning" OR "measurement equivalence")` → **20**. Relevant: Ford 2014, Mei 2022, Jensen 2024, Rancher 2024, Cooper 2021, Moore 2026, Meinck 2017 (ACE-ASF Romania). None by language except Cooper 2021.
2. Query 1 restricted to adverse childhood experiences AND (language OR Spanish OR translation OR Hispanic OR Latino OR Latinx) → **4**: Prakash 2026, Jensen 2024, Mersky 2023 (adverse *adult* experiences), Cooper 2021.
3. `"adverse childhood experiences" AND Spanish AND language` → **5**. None were invariance studies (QUIC-SP, Gianola 2023, Wohrer 2024, Parmar 2023, Koita 2018).
4. ACEs AND (BRFSS) AND (invariance OR "factor structure" OR "item response" OR "confirmatory factor" OR psychometric*) → **8**. Ford, Mei, Rancher, Zhang 2026, Dharma 2024, Westmore 2024, Decrop 2024, Hoadley 2024. None by language.
5. ACEs AND (invariance OR DIF) AND (NSCH) → **1** (Jensen 2024).
6. CTQ AND (Spanish OR Latino* OR Hispanic) AND (invariance OR DIF OR equivalence) → **3** (Thombs 2007, Rodriguez 2019, Aizpurua 2024).
7. ACEs AND ("interview language" OR "language of interview" OR "survey language" OR "language preference" OR "primary language" OR "household language" OR "language spoken") → **9**. None were invariance studies (Campbell 2026, Gianola 2023, Ghandour 2024, Akinyemi 2024, Hinson-Enslin 2026 [Deaf ASL users], Muench 2018, Dembo 2022, Soundararajan 2023, Wohrer 2024).
8. (ACEs OR ACE-IQ) AND (invariance OR DIF) AND (countries OR cross-cultural OR cross-national) → **1** (Inanoglu 2026).
9. ACEs AND ("cognitive interview*" OR "cognitive testing") → **8**. None tested the BRFSS ACE module.
10. ACEs AND (invariance OR DIF) AND (race OR ethnicity OR racial) → **5** (Mei, Jensen, Rancher, Mersky 2023, Díaz-Faes 2026).
11. ACEs/AFEs AND (NSCH) AND (Spanish OR "primary language" OR "language spoken" OR "household language" OR "non-English") → **5** (Chipalo 2026, Campbell 2026, Crouch 2026, Ghandour 2024, Soundararajan 2023). None tested equivalence.
12. ACEs AND (Hispanic OR Latino*) AND (acculturation OR "language preference" OR nativity) AND (BRFSS) → **0**.
13. (ACEs OR "childhood adversity" OR "childhood trauma") AND (invariance OR DIF) AND (French OR Chinese OR Cantonese OR Hebrew OR Arabic OR Afrikaans OR isiZulu OR bilingual OR "language versions") → **5**. None compared ACE language versions (Fung 2024 tested invariance of a dissociation scale, not of the trauma items).
14. CTQ AND (invariance OR DIF) AND (language OR translation OR cross-cultural OR countries) → **1** (irrelevant).
15. ACEs AND ("Hispanic Community Health Study" OR HCHS/SOL) → **12**. Only Cooper 2021 tested invariance.
16. ("experiencias adversas" OR "experiencias infantiles adversas" OR "adversidad infantil") AND (invarianza OR validación OR psicométric* OR validation) → **2** (Dutch ACE-IQ-10 with a Spanish translated title; Brazilian ACE-IQ adaptation).
17. ACEs AND ("item response theory" OR Rasch OR MIMIC OR "moderated nonlinear factor analysis") → **28**, mostly ACE-inhibitor noise. Relevant: Zhang 2026, MACE scale papers. None by language.
18. ACEs AND ("mode effect" OR "mode of administration" OR interviewer) AND (disclosure OR reporting) → **1** (irrelevant).

**Europe PMC REST (full-text BODY search). Query → hits:**
- `(BODY:"differential item functioning") AND ("adverse childhood experiences") AND (BODY:"Spanish")` → **22**. These were conference abstract books and unrelated instruments; no ACE language DIF.
- `(BODY:"measurement invariance") AND (TITLE_ABS:"adverse childhood experiences") AND (BODY:"Spanish")` → **9**. Only Cooper 2021 tested language. Ye 2023 PEARLS tested format, age and gender.
- `(BODY:"measurement invariance" OR BODY:"differential item functioning") AND (TITLE_ABS:"adverse childhood") AND (BODY:"language of interview" OR "interview language" OR "survey language" OR "language preference" OR "language version")` → **3**: Cooper 2021, plus Polish and Chinese MACE adaptations (single-language).
- `(TITLE_ABS:"adverse childhood") AND (BODY:"QSTLANG" OR BODY:"questionnaire language")` → **0**.
- `(TITLE_ABS:"adverse childhood") AND BODY:"BRFSS" AND BODY:"Spanish" AND BODY:"interview"` → **9**. No invariance studies.
- `(TITLE_ABS:"Childhood Trauma Questionnaire") AND BODY:"Spanish" AND BODY:"English" AND (BODY:invariance OR DIF)` → **6**. Single-language validations and reviews.
- `(TITLE_ABS:"adverse childhood") AND (TITLE_ABS:invariance OR DIF) AND (TITLE_ABS: language OR translation OR cross-cultural OR Hispanic OR Latino)` → **6**: Prakash, Díaz-Faes, Michael 2025, Jensen, Cooper, Mersky.
- `(TITLE_ABS:"ACE-IQ") AND (invariance OR DIF OR validation OR psychometric)` → **20**. Single-country validations (Malawi, China, Chile, Mexico, Netherlands, Italy, Bhutan, Serbia). No cross-language invariance.
- Childhood trauma/maltreatment/CTQ AND (invariance OR DIF) AND (Spanish OR Latino OR Latina OR Hispanic) → **5** (Aizpurua, Rodriguez, Thombs, plus 2 irrelevant).
- ACE/maltreatment/trauma AND (invariance OR DIF) AND (French OR Canada OR Canadian OR Hong Kong OR Israel OR South Africa) → **1** (Inanoglu 2026).
- ACE-IQ/ACE AND invariance AND (countries OR cross-national OR cross-cultural OR multinational) → **2**.
- ACE AND BODY Spanish-language AND underreport AND NSCH → **0**.
- ACE AND (Spanish-speaking OR limited English OR non-English) in title/abstract → **18**. None were measurement studies.

**OpenAlex. Filter → hits:**
- `title_and_abstract.search:"adverse childhood" AND (invariance OR "differential item functioning")`, 2025–2026 → **30**. Yielded Umoga 2026, Krushas 2025, Dorri 2026 and Moore 2025. None by language.
- `type:dissertation` + ACE + (invariance OR DIF OR psychometric) → **26**. Umoga 2026 was the only invariance-relevant hit.
- ACE AND (Spanish OR Hispanic OR Latino) AND (invariance OR DIF OR equivalence) → **9**. Jensen, Cooper, Krushas, Umoga and others; only Cooper tested language.
- ACE AND ("language of interview" OR "interview language" OR "survey language" OR "language preference") → **4**: Alhalel 2018, Gianola 2023, Hinson-Enslin 2026, and a sleep abstract.
- Harvard (I136199984) + ACE + dissertation, 2025–2026 → **1** (Zahrah 2026, BCEs in football players, irrelevant). Umoga is indexed under the DASH source rather than the institution.

**Harvard DASH API (`/server/api/discover/search/objects`). Relevance-ranked totals:**
- "adverse childhood experiences measurement invariance" → 55
- "adverse childhood experiences differential item functioning" → 425
- "adverse childhood experiences Spanish" → 76
- "adverse childhood experiences Latino measurement" → 65
- "childhood adversity measurement invariance" → 66
- Umoga 2026 was the top or only relevant record.

**Web searches (general engine):**
- "Alhalel adverse childhood experiences language Northwestern thesis" → PRISM record.
- "dissertation 2026 Harvard ACE measurement invariance Hispanic language" → nothing new.
- "Harvard DASH dissertation 2026 ACE DIF BRFSS" → nothing new.
- "Journal of Interpersonal Violence 2025 ACE Hispanic Spanish language BRFSS measurement" → nothing new.
- "cognitive testing ACE questions Spanish-speaking respondents survey translation" → Koita 2018 PEARLS.
- "site:wwwn.cdc.gov qbank report adverse childhood experiences cognitive interview" → Massey 2018, Massey & Virkar 2022, MacFadyen 2023.
- "Q-Bank cognitive interviewing ACE questions NCHS report" → Massey 2018.
- Spanish-language: "experiencias adversas en la infancia" invarianza factorial validación cuestionario → Dialnet, Psicología y Salud, UPS Ecuador.

**Databases attempted but not usable:**
- SciELO's search page (search.scielo.org) returned a JavaScript shell with no parseable results.
- The Q-Bank report listing (wwwn.cdc.gov/QBank/Report.aspx) is JavaScript-rendered.
- Redalyc was not queried directly; it was covered only through the general web search.
- Semantic Scholar was not used, because of rate limits.
- ProQuest was not directly searchable; it was covered via OpenAlex and DASH.

### Inferences
- The specific gap remains open: no published or grey-literature study tests DIF or measurement invariance of the **BRFSS ACE module** by interview language (QSTLANG), or of any stand-alone ACE instrument by Spanish vs English administration.
- The novelty claim must still acknowledge **Cooper & Nickodem 2021** as a partial precedent. It is a formal Spanish-vs-English invariance test of a model containing ACE items, in Hispanic immigrants, and its scalar result was ambiguous, hinting at language non-invariance.
- Overclaiming phrases such as "no one has ever examined ACE measurement by language" would be incorrect. Accurate phrasing: "no study has tested item-level DIF of the BRFSS ACE items by interview language. The only language-invariance test involving ACE items (Cooper & Nickodem 2021) embedded them in a 59-item lifetime-adversity bifactor model in a 92%-Spanish immigrant sample, and found only partial scalar support."
- An inference from Cooper's 92% Spanish figure: the English group was roughly 260 of 3,296 respondents. Their invariance test therefore had limited power for the English group, which a BRFSS-based study could improve on.

### Gaps
- SciELO and Redalyc could not be queried programmatically, so Spanish-language coverage relies on PubMed, Europe PMC, OpenAlex and a general web search. A manual SciELO and Redalyc check with "invarianza" + "experiencias adversas" + "inglés" is advisable before submission.
- Unpublished conference abstracts (APHA, SSR, ISTSS) were sampled only through Europe PMC abstract books. ProQuest Dissertations was not searched directly.
- California's CHIS has fielded ACE items in Spanish and other languages. No CHIS ACE invariance or DIF study was found, but no CHIS-specific query was run beyond the general terms above.

---

## Q6. Adjacent precedents: maltreatment-instrument invariance/DIF by language in US Latinos, and studies showing Spanish-speaking respondents report fewer (or different) ACEs

### Takeaway
- **Maltreatment instruments:** No CTQ (or other maltreatment-instrument) study tests Spanish vs English equivalence in US Latinos. Existing CTQ DIF work in US samples tests race and ethnicity (Hispanic vs non-Hispanic, Black vs Hispanic), not language.
- **Prevalence studies:** Several studies show lower or different ACE reporting among Spanish-preferring or non-English-household respondents: BRFSS (Alhalel 2018) and NSCH (Campbell & Jacobs 2026; Chipalo 2026). All compare prevalence or associations, and none tests measurement equivalence. Campbell & Jacobs explicitly name language comprehension and under-reporting as an untested threat.

### Cited Findings
- **Rodriguez et al. 2019 [ABS]:** CTQ-SF, N = 1,319 (26.3% Hispanic). "non-uniform DIF was identified in five items by race, and no items by ethnicity." No language analysis appears in the abstract. *Child Abuse Negl* 94:104030. — [PubMed 31181398](https://pubmed.ncbi.nlm.nih.gov/31181398/)
- **Thombs et al. 2007 [ABS]:** CTQ-SF in 693 San Antonio injection-drug users, Black vs Hispanic, with partial invariance. "compared to Hispanics, Blacks tended to report having been 'punished with hard objects' at higher rates than expected." Language not addressed in the abstract. *J Psychosom Res* 63(4):391–398. — [PubMed 17905047](https://pubmed.ncbi.nlm.nih.gov/17905047/)
- **Aizpurua et al. 2024 [ABS]:** CTQ-SF invariance among incarcerated men and women **in Spain**, by gender. Not a cross-language test. — [PubMed 37950962](https://pubmed.ncbi.nlm.nih.gov/37950962/)
- **Fung et al. 2024 [ABS]:** Chinese-speaking (N = 781) vs English-speaking (N = 468) adults. Measurement invariance was established for the *dissociation* scale (MDI), not for the childhood-trauma items (Brief Betrayal Trauma Survey). This is the closest non-Spanish cross-language precedent found, and it does not test the trauma measure itself. — [PubMed 39332139](https://pubmed.ncbi.nlm.nih.gov/39332139/)
- **Campbell & Jacobs 2026 [FT]:** NSCH 2016–2023 immigrant households (N = 32,094). "English as the primary household language was associated with increased odds of high ACEs exposure among all immigrant groups." For Hispanic children, high ACEs OR = 1.98 (95% CI 1.56–2.50). Limitation: "Although the NSCH survey is also administered in Spanish, language barriers may hinder accurate comprehension of the survey, including the ACEs measures. Moreover, these households might be less likely to report ACEs (e.g., maltreatment) due to cultural norms and fear of legal repercussions." No equivalence test. *J Immigr Minor Health* 28(2):348–359. — [PMC13083318](https://pmc.ncbi.nlm.nih.gov/articles/PMC13083318/)
- **Alhalel 2018 [FT]:** BRFSS Spanish- vs English-questionnaire Hispanic respondents differed on 6 of 11 items. Physical abuse was higher in the Spanish group (28.8% vs 15.9%); the other five differing items were higher in the English group. See Q4. — [PRISM](https://prism.northwestern.edu/records/7mt6a-brh38)
- **Chipalo et al. 2026 [ABS]:** NSCH 2022 non-English-speaking households. 22.4% had at least one ACE. Association analysis only. — [PubMed 39985397](https://pubmed.ncbi.nlm.nih.gov/39985397/)
- **BRFSS ACE nonresponse [FT]:** Besera et al. 2024 (*Am J Prev Med* 67(6):941–950) found module nonresponse of 1.2% in 2019 and 2.4% in 2021, higher among NH Black, NH Asian, unemployed and low-income respondents. "Spanish" and "QSTLANG" appear zero times, so nonresponse was not analysed by interview language. — [PMC11752077](https://pmc.ncbi.nlm.nih.gov/articles/PMC11752077/)
- **Grigsby et al. 2024 [FT]:** BRFSS 2021 ACE nonresponse, *Prev Med Rep* 42:102749. The authors only speculate that "language barriers, limited health literacy… can also impede accurate and comprehensive responses." There is no language analysis. — [PMC11089347](https://pmc.ncbi.nlm.nih.gov/articles/PMC11089347/)

### Inferences
- The adjacent literature repeatedly raises, but never tests, the possibility that language-of-administration effects contaminate ACE prevalence comparisons. That supports the proposal's rationale.
- Alhalel's item-profile pattern also supports a specific prediction. Spanish-interview respondents may show uniform DIF on some household-dysfunction or sexual-abuse items (lower endorsement at equal latent adversity) and the opposite on the physical-abuse item. The physical-abuse prediction is plausibly linked to physical-discipline norms (compare the "punished with hard objects" DIF in Thombs 2007, and the YRBS cognitive finding in Q7).

### Gaps
- The share of NSCH Hispanic respondents using the Spanish instrument, and the share of BRFSS ACE-module respondents interviewed in Spanish per state and year, were not extracted. QSTLANG is available (see Q7) but was not tabulated for the ACE subsample.

---

## Q7. Cognitive testing: did CDC/NCHS (CCQDER, Q-Bank) or anyone else cognitively test the BRFSS ACE module, in English or Spanish?

### Takeaway
- **BRFSS adult module itself:** No CCQDER or Q-Bank report was found that cognitively tested the **BRFSS adult ACE module** in either language. CDC's BRFSS ACE page says the module "is available in English and Spanish" but describes no translation or testing process.
- **Related CCQDER tests (2018–2023):**
  - **NHIS:** child adverse-life-event items, English.
  - **YRBS:** teen ACE items adapted from BRFSS, English only.
  - **PRAMS Phase 9:** a BRFSS-derived adult ACE item set, tested in **English (n = 30) and Spanish (n = 20)**. The ACE set "performed well", with no Spanish-specific problems reported, although a Spanish positive-childhood-experience item was misinterpreted.

### Cited Findings
- **CDC BRFSS ACE page [FT]:** "The module is available in English and Spanish." It links "BRFSS ACE Module 2009-2020 (Spanish)". It also says "Abuse Questions were modified from the original CDC-Kaiser ACE Study to make them more appropriate for a telephone survey," and "all 50 states and the District of Columbia have included ACE questions for at least one year." Translation and cognitive testing are not mentioned. — [CDC ACE BRFSS page](https://www.cdc.gov/violenceprevention/aces/ace-brfss.html)
- **BRFSS language variable [FT]:** The 2019 LLCP codebook lists `QSTLANG` ("Language identifier"): English 398,354 (95.96% unweighted; 92.76% weighted); Spanish 16,772 (4.04%; 7.23% weighted); Other 13. These counts cover the full 2019 BRFSS, not the ACE subsample. — [BRFSS 2019 codebook](https://www.cdc.gov/brfss/annual_data/2019/pdf/codebook19_llcp-v2-508.HTML)
- **Massey, Reynolds, Jamoom & Creamer, January 2018 (NHIS) [FT]:** 25 cognitive interviews in September 2017 at the CCQDER lab, face to face. The "section on Adverse Childhood Events asked respondents about potentially sensitive topics related to their children's environment." Quote: "no respondent asked to skip any questions… Respondents who answered 'yes'… had a harder time discussing their responses. Several respondents cried." Subgroups examined were "age, education, race and gender". No Spanish interviews are mentioned. — [Q-Bank Massey 2018](https://wwwn.cdc.gov/QBank/report/Massey_2018_NCHS_NHIS.pdf)
- **Massey & Virkar, June 2022 (YRBS ACEs) [FT]:** 40 interviews with teens aged 12–17 (November 2021 to January 2022) on ACE items that were "originally developed as part of the CDC-Kaiser ACE Study, and subsequently used in the [BRFSS] ACEs Module" and adapted for YRBS. Findings:
  - Middle-schoolers misread terms: one "thought *swear*… meant to hit with a stick".
  - "minority respondents were more likely to discount incidents of physical punishment… several African American respondents described being spanked or beaten as punishment but did not include these incidents in their responses."
  - The report contains no mention of Spanish or of language.
  - [Q-Bank Massey & Virkar 2022](https://wwwn.cdc.gov/QBank/report/Massey_2022_NCHS_ACES.pdf)
- **MacFadyen, March 2023 (PRAMS Phase 9) [FT]:** "A total of 50 interviews were conducted… Thirty interviews were conducted in English and 20 were conducted in Spanish." The interview team included Alisú Schoua-Glusberg. ACE item set A20 (yes/no; household mental illness, substance use, incarceration-related separation, IPV, physical abuse, verbal abuse, sexual abuse, plus new items) "performed well to capture respondents' experiences". Respondents counted undiagnosed mental illness and counted disciplinary violence "depending on the respondents' outlook". **No "Spanish-language considerations" subsection appears for the ACE item** (the report has 16 such subsections elsewhere). For the PCE item, "Some Spanish-language respondents interpreted a 'sense of belonging' ('sentido de pertenencia') as referring to ownership." — [Q-Bank MacFadyen 2023](https://wwwn.cdc.gov/qbank/report/MacFadyen_2023_NCHS_PRAMS.pdf)
- **Observation from the PRAMS instrument text [FT, own reading]:** The Spanish IPV item reads "¿Sus padres u otros adultos en su hogar se daban bofetadas, golpeaban, pateaban, **apuñalaban** o peleaban físicamente entre ellos?" The English is "slap, hit, kick, punch, or beat each other up". "Apuñalar" means *to stab*; the probable intended word was "puñetazo" (punch). — [Q-Bank MacFadyen 2023](https://wwwn.cdc.gov/qbank/report/MacFadyen_2023_NCHS_PRAMS.pdf)
- **Observation from the official BRFSS Spanish ACE module PDF [FT, own reading]:** Comparing CDC's Spanish module with the English module shows several non-literal renderings:
  - Verbal abuse: "swear at you, insult you, or put you down" becomes "le dijo groserías, le insultó o le **humilló**" ("humiliated", arguably stronger than "put down").
  - Physical abuse: "a **parent or** adult in your home" becomes "**un adulto** en su hogar" (no "parent").
  - The Spanish PDF prints the separation/divorce item twice (items 5 and 6, with different codes), so it has 12 numbered items against 11 in English.
  - [Spanish module PDF](https://www.cdc.gov/violenceprevention/pdf/BRFSS_Adverse_Module_Spanish.pdf); [English module PDF](https://www.cdc.gov/violenceprevention/pdf/BRFSS_Adverse_Module.pdf)
- **Koita et al. 2018 (PEARLS) [ABS/snippet]:** A pediatric ACE screener (not BRFSS) was professionally translated and back-translated. "Cognitive interviews with caregivers, providers, and clinic staff checked item interpretation, clarity, and language equivalence," leading to rewording. — [PMC6291095](https://pmc.ncbi.nlm.nih.gov/articles/PMC6291095/)

### Inferences
- The "no Spanish cognitive testing of the BRFSS ACE module" statement survives verification for the BRFSS module itself. It should be refined to say that CCQDER tested a closely related BRFSS-derived ACE item set in Spanish for PRAMS in 2022 and found no Spanish-specific interpretation problems. That was a small qualitative sample (n = 20, self-administered or interviewer-administered via Zoom, postpartum women), with different wording and a yes/no format.
- The wording discrepancies in CDC's own Spanish materials ("humilló" vs "put you down"; omission of "parent" in the physical-abuse item; "apuñalaban" in PRAMS) are concrete, citable a-priori hypotheses for item-level DIF. Note that they are the author's own reading of primary documents, not published findings.
- The YRBS finding that respondents discount physical punishment, and the CTQ "punished with hard objects" DIF (Thombs 2007), point to physical-abuse items as a likely DIF locus across cultural or linguistic groups. This is consistent with Alhalel's Spanish-preference excess in physical-abuse endorsement.

### Gaps
- The Q-Bank search interface is JavaScript-rendered and could not be queried exhaustively. Coverage relies on site-restricted web searches, so an older CCQDER report on the BRFSS module cannot be fully excluded.
- The year or version of the CDC Spanish module PDF is unclear. Its header reads "Módulo 31" and it is linked as "2009–2020 (Spanish)". Whether state CATI scripts used identical Spanish wording in every year was not verified.
- No BRFSS documentation was found on the BRFSS translation process for the ACE module (e.g., committee translation or back-translation).

---

## Q8. Overall verdict: is the "ACE invariance by interview language" gap genuinely open, and who are the closest competitors?

### Takeaway
**Yes, for the specific question.** No study has tested measurement invariance or item-level DIF of the BRFSS ACE module (or any stand-alone ACE instrument) by Spanish vs English interview language. The space around it is crowded, however, and the proposal must position itself against at least five works:
1. **Cooper & Nickodem 2021:** the only formal Spanish/English invariance test involving ACE items; partial scalar support.
2. **Umoga 2026:** BRFSS 2021–2023 multigroup LCA across race/ethnicity; non-invariant; full text embargoed.
3. **Jensen et al. 2024:** NSCH thresholds non-invariant across race/ethnicity including Hispanic.
4. **Mei et al. 2022:** BRFSS 2019 omnibus invariance by race including Hispanic; language untested.
5. **Alhalel 2018:** BRFSS prevalence differences by questionnaire language; no measurement test.

### Cited Findings
- **Cooper & Nickodem 2021:** Spanish vs English strong invariance "partially, but not strongly, supported" (Δχ²(132) = 299, p < .001; ΔCFI = −.009) for a 59-item adversity bifactor model including 10 ACE items, in HCHS/SOL immigrants (92% Spanish). — [PMC9993236](https://pmc.ncbi.nlm.nih.gov/articles/PMC9993236/)
- **Umoga 2026:** BRFSS 2021–2023 (n = 216,439). "class-defining probabilities were not fully invariant" across six racial/ethnic groups. Language not mentioned in the abstract. — [DASH](https://dash.harvard.edu/handle/1/42760678)
- **Jensen et al. 2024:** NSCH 2018–2020. Scalar invariance failed (ΔCFI = −.057); only 3 of 11 thresholds were invariant across five groups including Hispanic. No language variable. — [PMC11023799](https://pmc.ncbi.nlm.nih.gov/articles/PMC11023799/)
- **Mei et al. 2022:** BRFSS 2019. Omnibus configural, metric and scalar invariance across age, race (including Hispanic), sex, income, gender identity and sexual orientation. Language absent; no item-level DIF; weights not reported. — [PMC9706892](https://pmc.ncbi.nlm.nih.gov/articles/PMC9706892/)
- **Ford et al. 2014:** BRFSS 2009–2010, weighted. Invariance by gender and age only. — [PMC4587306](https://pmc.ncbi.nlm.nih.gov/articles/PMC4587306/)
- **Alhalel 2018:** BRFSS 2011–2012, 9 states. 6 of 11 items differ by questionnaire language; similar ACE-count distribution; no invariance test. — [PRISM](https://prism.northwestern.edu/records/7mt6a-brh38)
- **MacFadyen 2023:** Spanish and English cognitive testing of a BRFSS-derived PRAMS ACE set; no Spanish-specific ACE problems reported. — [Q-Bank](https://wwwn.cdc.gov/qbank/report/MacFadyen_2023_NCHS_PRAMS.pdf)

### Inferences
- **Defensible novelty statement:** "To our knowledge, this is the first test of item-level measurement invariance/DIF of the BRFSS ACE module by interview language (QSTLANG). It is also the first to separate language-of-administration from Hispanic ethnicity, by comparing Spanish- and English-interviewed Hispanic respondents and English-interviewed non-Hispanic respondents."
  - Cooper & Nickodem 2021 should be named as the sole prior language-invariance test involving ACE items, with its limitations stated: a bifactor lifetime-adversity model, not ACE-specific; immigrants only; an English group of roughly 8%; no item-level DIF.
- **Methodological value-add over competitors** (from the gaps in Mei, Ford and Jensen):
  - item-level DIF effect sizes, e.g., threshold differences, MIMIC/MNLFA, or IRT-based DIF with impact on ACE sum scores;
  - design-weighted estimation (Mei unweighted or unreported; Jensen unweighted);
  - stricter or simulation-informed cut-offs (ΔCFI ≤ .002 as in Jensen, or alignment);
  - disentangling language from ethnicity and nativity;
  - pre-specified hypotheses grounded in documented translation discrepancies and cognitive-interview evidence.
- **Main risk to novelty:** the embargoed Umoga dissertation, which could contain a language stratification, and any work in press from that group. Checking with the author or advisor (Harvard Population Health Sciences) is advisable.

### Gaps
- Full texts not obtainable this session: Umoga 2026 (embargoed), Zhang & Lippert 2026 (paywalled), Krushas et al. 2025 (paywalled), and Dorri et al. 2026 (abstract not indexed).
- Sources and populations not exhaustively searched: SciELO and Redalyc by direct query, ProQuest Dissertations by direct query, CHIS-specific ACE psychometrics, and Canadian French/English childhood-maltreatment items (CCHS-MH 2012). These were covered only by the generic database queries listed in Q5, which returned no language-invariance hits.
