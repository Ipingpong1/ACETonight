# Interview language and the reporting of adverse childhood experiences among Hispanic adults

Working repository for a preprint on differential item functioning (DIF) of the BRFSS adverse childhood experience (ACE) items by Spanish versus English interview, in BRFSS 2019–2025 and CHIS 2021–2025, with exploratory triangulation in NSCH 2022–2024.

**Status:** working draft, version 0.1, 2 November 2026. Not peer reviewed. The first commit of this repository is the external timestamp of the analysis plan, results and manuscript.

## Read this first

| What | Where |
|---|---|
| The preprint (manuscript) | [`preprint/preprint.md`](preprint/preprint.md) · [PDF](preprint/preprint.pdf) · [HTML](preprint/preprint.html) |
| Supplement (all tables, deviations, exploratory analyses, literature search) | [`preprint/supplement.md`](preprint/supplement.md) · [PDF](preprint/supplement.pdf) |
| Adversarial review of the project (what holds, what does not, what a PI will ask) | [`REVIEW.md`](REVIEW.md) |
| Frozen analysis plan and its hash | [`prereg/`](prereg/) |
| Deviations from the plan | [`analysis/DEVIATIONS.md`](analysis/DEVIATIONS.md) |
| Full results of the pre-specified analyses | [`analysis/RESULTS.md`](analysis/RESULTS.md) |

## One-paragraph summary

Hispanic adults interviewed in Spanish report household mental illness, drug use and incarceration one-fifth to one-third as often as those interviewed in English. Conditional on the other household items, all three are under-endorsed in both surveys, but the estimates depend on which items are assumed invariant. Only the household mental-illness item is under-endorsed in every specification that matters: after nativity adjustment and among the foreign-born (CHIS), by phone and by web, in an anchor-free alignment analysis, and, in an exploratory analysis of NSCH parent reports, with a different informant and no interviewer. Item-level DIF accounts for at most 10–18% of the language gap in ACE scores.

## Repository layout

```
preprint/        preprint.md, supplement.md, build.py (md -> HTML/PDF), figures/, archive/ (earlier draft)
prereg/          H1_analysis_plan.md (frozen 2026-11-02T06:38:47Z) and its SHA-256
analysis/        RESULTS.md, DEVIATIONS.md, STATUS.md, tables, primary/ and secondary/ model outputs (CSV/JSON), logs/
scripts/
  manuscript/    R (lavaan, survey) and Python code for the pre-specified analyses, run via run.sh
  exploratory/   Python code for the 1 November exploratory analyses (BRFSS logistic DIF and 2PL, CHIS, NSCH, BRFSS mental health)
exploratory/     results of the exploratory analyses (RESULTS.md and CSV per module)
notes/           literature search logs, novelty verification, adversarial methods notes, venue research
REVIEW.md        adversarial review of the whole project
```

## Data

No microdata are in this repository.

- **BRFSS** public-use files (2009–2012, 2019–2025, main and questionnaire-version files): https://www.cdc.gov/brfss/annual_data/ . The extraction scripts in `scripts/exploratory/` (and the earlier `extract_year.py` pipeline they depend on) rebuild the analytic files.
- **CHIS** adult public-use files 2021–2025: free after registration at https://healthpolicy.ucla.edu/ ; the terms of use do not permit redistribution.
- **NSCH** 2022–2024 topical files: https://www2.census.gov/programs-surveys/nsch/datasets/ .

## Reproducing the pre-specified analyses

1. Build the BRFSS analytic file with `scripts/exploratory/dif/build_dif_data.py` and the CHIS pooled file with `scripts/exploratory/chis/build.py`.
2. `scripts/manuscript/run.sh 01_prep.R BRFSS_CSV CHIS_CSV`, then `02_table1.R`, `03_table2.R`, `04_primary_mimic.R brfss|chis CORES`, `04b_verdict.R`, `05_secondary.R s1|s2|s3|s4 brfss|chis|chisnat|s4combine|s6|s7 CORES`, `06_s5_impact.R brfss|chis CORES`, `make_results.py`, `make_figures.py`.
3. Paths in `scripts/manuscript/common.R` are absolute to the original analysis machine; edit `ROOT` and the data paths.

Environment: R 4.5.3 with lavaan 0.7.2, survey 4.5, sirt 4.2, data.table, jsonlite; Python 3 with pandas, numpy, scipy, statsmodels, matplotlib. The BRFSS bootstrap (100 replicates × lavaan refits) takes about an hour on 10 cores.

## Rendering the preprint

```
pip install markdown
python preprint/build.py      # writes preprint.html/.pdf and supplement.html/.pdf (needs Google Chrome or Chromium)
```

## Open items

- Author list, affiliations, ORCID and contributions in `preprint/preprint.md`.
- OSF registration of `prereg/H1_analysis_plan.md` (under embargo; disclose the 1 November exploratory work).
- NYU HRPP "not human subjects research" determination.
- Licence (suggested: CC BY 4.0 for the manuscript, MIT for code).
- See `REVIEW.md` §7 for the full pre-posting checklist.

## Citation

[Author name]. Does interview language change how Hispanic adults report childhood household adversity? Differential item functioning of adverse childhood experience items by Spanish versus English interview in two US surveys. Working draft v0.1, 2 November 2026. https://github.com/Ipingpong1/ace-language-dif
