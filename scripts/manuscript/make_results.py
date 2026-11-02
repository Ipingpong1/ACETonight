"""Assemble /home/mo2273/ace_manuscript/analysis/RESULTS.md from the stage outputs.
usage: python -I make_results.py ANALYSIS_DIR FIGURE_DIR
"""
import sys, os, json
import numpy as np
import pandas as pd

AN, FIG = sys.argv[1], sys.argv[2]
SEC = os.path.join(AN, 'secondary')
LAB = {'mh': 'Household mental illness', 'drugs': 'Household drug use', 'jail': 'Household incarceration',
       'drink': 'Household problem drinking', 'divorce': 'Parental separation/divorce', 'ipv': 'Witnessed parental violence',
       'phys': 'Physical abuse', 'verbal': 'Verbal abuse', 'HD': 'Household dysfunction factor', 'AB': 'Physical/emotional abuse factor',
       'SX': 'Sexual abuse factor', 'ACE': 'Single ACE factor'}
T = ['mh', 'drugs', 'jail']


def rd(p):
    p = os.path.join(AN, p)
    return open(p).read().strip() if os.path.exists(p) else f'_(missing: {p})_'


def jl(p):
    p = os.path.join(AN, p)
    return json.load(open(p)) if os.path.exists(p) else None


def f(x, k=2):
    return '' if x is None or (isinstance(x, float) and np.isnan(x)) else f'{x:.{k}f}'


def pv(p):
    return '' if p is None or (isinstance(p, float) and np.isnan(p)) else ('<0.001' if p < 0.001 else f'{p:.3f}')


def orci(b, lo, hi):
    return f'{np.exp(1.7 * b):.2f} ({np.exp(1.7 * lo):.2f}, {np.exp(1.7 * hi):.2f})'


out = []
P = out.append
v = jl('H1_verdict.json')
P('# H1 confirmatory analysis: results\n')
P('Plan: `/home/mo2273/ace_manuscript/prereg/H1_analysis_plan.md`, frozen 2026-11-02T06:38:47Z, SHA-256 `031cd72089936e1d4f332bbdbab7071fa6100b346b778cda34480571b3d420fa` (verified, unchanged). '
  'Analysis run 2026-11-02. Samples: BRFSS 2019-2025 Hispanic adults, 10,945 Spanish-interview / 24,473 English-interview; '
  'CHIS 2021-2025 Hispanic adults, 5,536 / 24,418 (both exactly as expected in the plan).\n')

# ---------------------------------------------------------------- verdict
P('## 1. H1 verdict (pre-specified decision rule)\n')
if v:
    P(f"**H1: {v['verdict']}.** Rule: all three direct effects < 0 with Holm-adjusted p < .05 (6 tests) and b ≤ −0.24 in both surveys = supported; "
      f"≥ 2 items in both surveys or all 3 in one survey = partially supported; otherwise not supported.\n")
    tt = pd.DataFrame(v['tests'])
    P('| Survey | Target item | b (probit) | replicate SE | 95% CI | OR-equiv. (95% CI) | p | Holm p | b ≤ −0.24 | Meets all | Model-implied Δ endorsement, Spanish (pp, 95% CI) |')
    P('|---|---|---:|---:|---|---|---:|---:|---|---|---|')
    for _, r in tt.iterrows():
        P(f"| {r.survey} | {LAB[r['item']]} | {f(r.b, 3)} | {f(r.se_rep, 3)} | {f(r.ci_lo, 3)}, {f(r.ci_hi, 3)} | {f(r.OR_eq)} ({f(r.OR_lo)}, {f(r.OR_hi)}) | "
          f"{pv(r.p)} | {pv(r.p_holm)} | {'yes' if r.big else 'no'} | {'**yes**' if r.meets else 'no'} | {f(r.pdiff_pp, 1)} ({f(r.pdiff_lo, 1)}, {f(r.pdiff_hi, 1)}) |")
    P('')
    P(f"Items meeting every criterion in both surveys: {', '.join(LAB[i] for i in v['items_meeting_in_both']) or 'none'}. "
      f"Per survey: {', '.join(f'{k} {n}/3' for k, n in v['per_survey_items_meeting'].items())}. "
      + ('The verdict is the same under both readings of the partial-support rule.' if v['verdict'] == v['verdict_alt_reading'] else
         f"Under the alternative reading of the partial rule (≥ 2 items per survey, not necessarily the same) the verdict would be {v['verdict_alt_reading']}.") + '\n')
pr = pd.read_csv(os.path.join(AN, 'primary_results.csv'))
P('Language → factor effects (replicate SEs): ' + '; '.join(
    f"{r.survey} {LAB[r.lhs]} b = {f(r.est, 3)} (SE {f(r.se_rep, 3)}, 95% CI {f(r.ci_lo, 3)} to {f(r.ci_hi, 3)})"
    for _, r in pr[pr.lhs.isin(['HD', 'AB'])].iterrows()) + '. '
  'Variance: CHIS jackknife (80 RAKEDW replicates, scale 1, MSE); BRFSS 100 Rao-Wu rescaled bootstrap replicates (subbootstrap; singleton strata collapsed, see Deviations). '
  f"Replicates converged: BRFSS {int(pr[pr.survey=='BRFSS'].n_rep_ok.iloc[0])}/100, CHIS {int(pr[pr.survey=='CHIS'].n_rep_ok.iloc[0])}/80. "
  'Lavaan weight-robust SEs for the same parameters are in `primary_results.csv` (se_lavaan).\n')

# ---------------------------------------------------------------- summary and caveats (numbers read from the result files)
s4e = pd.read_csv(os.path.join(SEC, 's4_effects.csv'))
s1e = pd.read_csv(os.path.join(SEC, 'effects_s1.csv')).set_index('lhs')
s2e = pd.read_csv(os.path.join(SEC, 'effects_s2.csv')).set_index('lhs')
s6e = pd.read_csv(os.path.join(SEC, 's6_mode.csv'))
ph = pd.read_csv(os.path.join(SEC, 's4b_purification_history.csv'))
al = ph[ph.already_freed.astype(str).str.startswith('ALIGNMENT HD')].set_index(['survey', 'item'])
imp = {sv: pd.read_csv(os.path.join(SEC, f's5_impact_{sv}.csv')).set_index('quantity') for sv in ('brfss', 'chis')}
def g(df, sv, an, it):
    q = df[(df.survey == sv) & df.analysis.str.startswith(an) & (df.lhs == it)]
    return q.iloc[0] if len(q) else None
c4 = lambda sv, it: g(s4e, sv, 'S4c', it)
b4 = lambda sv, it: g(s4e, sv, 'S4b', it)
P('## 2. Summary and caveats\n')
P(f"- **The confirmatory test passes.** In the primary MIMIC, all six target direct effects are negative, Holm-significant and beyond the b ≤ −0.24 threshold "
  f"(BRFSS b = {', '.join(f(pr[(pr.survey=='BRFSS')&(pr.lhs==i)].est.iloc[0], 2) for i in T)}; CHIS b = {', '.join(f(pr[(pr.survey=='CHIS')&(pr.lhs==i)].est.iloc[0], 2) for i in T)} "
  "for mental illness, drug use, incarceration). The weakest is CHIS drug use, whose point estimate only just passes the magnitude criterion (its 95% CI includes values above −0.24).")
P(f"- **H1b fails.** After adding nativity and % of life in the US (CHIS S1), only household mental illness keeps a significant negative direct effect "
  f"(b = {f(s1e.loc['mh','est'])}, p {pv(s1e.loc['mh','pvalue'])}). Drug use (b = {f(s1e.loc['drugs','est'])}, p = {pv(s1e.loc['drugs','pvalue'])}) and incarceration "
  f"(b = {f(s1e.loc['jail','est'])}, p = {pv(s1e.loc['jail','pvalue'])}) do not. The same pattern holds among foreign-born respondents only (S2): mental illness "
  f"b = {f(s2e.loc['mh','est'])}, drugs {f(s2e.loc['drugs','est'])}, incarceration {f(s2e.loc['jail','est'])}. In CHIS, therefore, the drug-use and incarceration DIF is "
  "largely accounted for by nativity, i.e. it may reflect real exposure differences tied to immigration rather than language-specific reporting.")
P(f"- **Anchor dependence (BRFSS).** The plan assumed anchor bias could only be conservative, i.e. that anchors would at worst be under-reported in Spanish. S4c contradicts this in BRFSS: "
  f"problem drinking, a primary anchor, is *over*-endorsed in Spanish relative to the factor (b = {f(c4('BRFSS','drink').est)}, OR-equiv. {f(c4('BRFSS','drink').OR_eq)}), "
  f"while separation/divorce is under-endorsed (b = {f(c4('BRFSS','divorce').est)}). Pre-specified purification (S4b) freed {b4('BRFSS','mh').analysis.split('freed: ')[1].rstrip(')')}, "
  f"leaving divorce as the only household anchor. In that model the BRFSS target effects shrink to b = {f(b4('BRFSS','mh').est)} / {f(b4('BRFSS','drugs').est)} / {f(b4('BRFSS','jail').est)} "
  f"(p = {pv(b4('BRFSS','mh').pvalue)} / {pv(b4('BRFSS','drugs').pvalue)} / {pv(b4('BRFSS','jail').pvalue)}). The magnitude of the BRFSS primary estimates therefore depends on treating problem drinking as invariant. "
  f"In CHIS the household anchors show smaller relative DIF (drinking b = {f(c4('CHIS','drink').est)}, p = {pv(c4('CHIS','drink').pvalue)}; divorce {f(c4('CHIS','divorce').est)}, p = {pv(c4('CHIS','divorce').pvalue)}). "
  "Neither met the purification criterion, and S4b, which freed only physical abuse, leaves the CHIS target estimates unchanged.")
P(f"- **Anchor-free alignment (S4d, household factor; Spanish − English aligned intercepts).** Mental illness BRFSS {f(al.loc[('BRFSS','mh'),'est'])} / CHIS {f(al.loc[('CHIS','mh'),'est'])}; "
  f"incarceration {f(al.loc[('BRFSS','jail'),'est'])} / {f(al.loc[('CHIS','jail'),'est'])}; drug use {f(al.loc[('BRFSS','drugs'),'est'])} / {f(al.loc[('CHIS','drugs'),'est'])}; "
  f"problem drinking {f(al.loc[('BRFSS','drink'),'est'])} / {f(al.loc[('CHIS','drink'),'est'])}. The anchor-free check thus supports negative DIF for mental illness, gives weaker support for incarceration and none for drug use.")
P("- **DIF is not specific to the three target items.** The full scalar MGCFA is rejected in both surveys. Freeing the target items does not restore fit, and score tests flag thresholds of verbal abuse, problem drinking and physical abuse as strongly as mental illness. "
  f"Verbal abuse is strongly under-endorsed in Spanish (S4c b = {f(c4('BRFSS','verbal').est)} BRFSS, {f(c4('CHIS','verbal').est)} CHIS), and physical abuse is over-endorsed "
  f"(b = {f(c4('BRFSS','phys').est)}, {f(c4('CHIS','phys').est)}).")
mode = s6e.set_index(['item', 'term'])
P(f"- **Mode (CHIS S6).** The target DIF is present in self-administered web interviews (b = {f(mode.loc[('mh','Spanish direct effect, web'),'est'])}, "
  f"{f(mode.loc[('drugs','Spanish direct effect, web'),'est'])}, {f(mode.loc[('jail','Spanish direct effect, web'),'est'])}) and is not larger with an interviewer present. "
  f"The Spanish × web interaction is significant only for incarceration (larger DIF on the web, p = {pv(mode.loc[('jail','Spanish x web interaction'),'pvalue'])}). "
  "Interviewer presence therefore does not explain the DIF.")
P(f"- **Impact (S5).** Setting the target direct effects to zero would close {f(imp['brfss'].loc['pct_gap_mean_due_DIF','estimate'],1)}% (BRFSS) and "
  f"{f(imp['chis'].loc['pct_gap_mean_due_DIF','estimate'],1)}% (CHIS) of the model-implied Spanish−English gap in the mean 8-item count, and "
  f"{f(imp['brfss'].loc['pct_gap_p4_due_DIF','estimate'],1)}% / {f(imp['chis'].loc['pct_gap_p4_due_DIF','estimate'],1)}% of the gap in ≥ 4 items. "
  "Most of the observed gap would remain. Because these figures inherit the primary model's anchor assumption, the BRFSS figure is an upper-range estimate given the S4b result.\n")

# ---------------------------------------------------------------- fit
P('## 3. Model fit (WLSMV, theta; reported, not decision criteria)\n')
P('| Model | χ² (scaled) | df | CFI | TLI | RMSEA | SRMR |')
P('|---|---:|---:|---:|---:|---:|---:|')
for lab, p in (('Primary MIMIC, BRFSS', 'primary/fit_indices_brfss.json'), ('Primary MIMIC, CHIS', 'primary/fit_indices_chis.json'),
               ('S1 CHIS + nativity', 'secondary/fit_indices_s1.json'), ('S2 CHIS foreign-born', 'secondary/fit_indices_s2.json'),
               ('S4a one factor, BRFSS', 'secondary/fit_indices_s4a_brfss.json'), ('S4a one factor, CHIS', 'secondary/fit_indices_s4a_chis.json'),
               ('S6 CHIS mode interaction', 'secondary/fit_indices_s6.json'), ('S7 BRFSS 11 items, 3 factors', 'secondary/fit_indices_s7.json')):
    j = jl(p)
    if j:
        P(f"| {lab} | {f(j.get('chisq.scaled'), 1)} | {int(j.get('df.scaled', 0))} | {f(j.get('cfi.scaled'), 3)} | {f(j.get('tli.scaled'), 3)} | {f(j.get('rmsea.scaled'), 4)} | {f(j.get('srmr'), 3)} |")
P('\nScaled (mean- and variance-adjusted) indices. Robust CFI/RMSEA (Savalei) are not available from lavaan for these conditional.x models with sampling weights. '
  'CFI/TLI here are computed against a baseline that is conditional on the covariates.\n')

# ---------------------------------------------------------------- tables
P('## 4. Descriptive tables\n')
P(rd('table1.md').replace('## Table 1.', '### Table 1.'))
P('')
P(rd('table2.md').replace('## Table 2.', '### Table 2.'))
P('')

# ---------------------------------------------------------------- secondary
P('## 5. Secondary analyses\n')
P('### S1 (H1b): CHIS + nativity and % life in US; S2: CHIS foreign-born only (jackknife replicate SEs)\n')
P('| Analysis | Parameter | b | replicate SE | p | OR-equiv. (95% CI) | lavaan SE |')
P('|---|---|---:|---:|---:|---|---:|')
for k, lab in (('s1', 'S1 + nativity, % life in US'), ('s2', 'S2 foreign-born only')):
    p = os.path.join(SEC, f'effects_{k}.csv')
    if os.path.exists(p):
        e = pd.read_csv(p)
        for it in T + ['HD', 'AB']:
            q = e[e.lhs == it]
            if len(q):
                r = q.iloc[0]
                P(f"| {lab} (n = {int(r.n):,}; Spanish {int(r.n_spanish):,}) | {LAB[it]} | {f(r.est, 3)} | {f(r.se, 3)} | {pv(r.pvalue)} | "
                  f"{orci(r.est, r['ci.lower'], r['ci.upper']) if it in T else ''} | {f(r.se_lavaan, 3)} |")
h1b = jl('secondary/h1b_verdict.json')
if h1b:
    P(f"\n**H1b: {'SUPPORTED' if h1b['H1b_supported'] else 'NOT SUPPORTED'}** (pre-specified: all three CHIS direct effects < 0 with p < .05 after adjusting for nativity and % of life in the US).\n")

P('### S3: multigroup CFA by interview language (WLSMV, theta, weights; no covariates)\n')
s3f, s3d, s3m, s3s = [os.path.join(SEC, x) for x in ('s3_fit.csv', 's3_difftests.csv', 's3_latent_means.csv', 's3_score_tests.csv')]
if os.path.exists(s3f):
    a = pd.read_csv(s3f)
    P('| Survey | Model | χ² (scaled) | df | CFI | RMSEA | SRMR |')
    P('|---|---|---:|---:|---:|---:|---:|')
    for _, r in a.iterrows():
        P(f"| {r.survey} | {r.model} | {f(r['chisq.scaled'], 1)} | {int(r['df.scaled'])} | {f(r['cfi.scaled'], 3)} | {f(r['rmsea.scaled'], 4)} | {f(r.srmr, 3)} |")
    b = pd.read_csv(s3d)
    P('\n| Survey | Comparison | Δχ² (scaled) | Δdf | p | ΔCFI | ΔRMSEA |')
    P('|---|---|---:|---:|---:|---:|---:|')
    for _, r in b.iterrows():
        P(f"| {r.survey} | {r.comparison} | {f(r.chisq_diff, 1)} | {int(r.df_diff)} | {pv(r.p)} | {f(r.dCFI, 4)} | {f(r.dRMSEA, 4)} |")
    m = pd.read_csv(s3m)
    P('\nLatent mean of the Spanish-interview group (English = 0, SD 1): ' + '; '.join(
        f"{r.survey} {r.model} {r.factor} {f(r.est, 3)} (SE {f(r.se, 3)})" for _, r in m.iterrows()) + '.')
    s = pd.read_csv(s3s)
    P('\nScore tests on the full scalar model, the 8 largest per survey (univariate, 1 df; each row is one cross-group equality constraint on an item threshold or loading):\n')
    P('| Survey | Constraint (parameter) | χ² | scaled χ² | p (scaled) |')
    P('|---|---|---:|---:|---:|')
    for sv, g_ in s.groupby('survey'):
        for _, r in g_.sort_values('X2', ascending=False).head(8).iterrows():
            nm = (f"{LAB.get(r.par.split('|')[0], r.par)}: threshold" if '|' in r.par else
                  f"{LAB.get(r.par.split('=~')[1], r.par)}: loading" if '=~' in r.par else r.par)
            P(f"| {sv} | {nm} | {f(r.X2, 1)} | {f(r['X2.scaled'], 1)} | {pv(r['p.value.scaled'])} |")
    P('')

P('### S4: anchor sensitivity (lavaan weight-robust SEs)\n')
s4 = os.path.join(SEC, 's4_effects.csv')
if os.path.exists(s4):
    e = pd.read_csv(s4)
    P('| Survey | Analysis | Item | b | SE | p | OR-equiv. (95% CI) |')
    P('|---|---|---|---:|---:|---:|---|')
    for _, r in e.iterrows():
        if r.lhs in LAB and r.lhs not in ('HD', 'AB', 'ACE', 'SX'):
            P(f"| {r.survey} | {r.analysis} | {LAB[r.lhs]} | {f(r.est, 3)} | {f(r.se, 3)} | {pv(r.pvalue)} | {orci(r.est, r['ci.lower'], r['ci.upper'])} |")
    ph = pd.read_csv(os.path.join(SEC, 's4b_purification_history.csv'))
    pur = ph[~ph.already_freed.astype(str).str.startswith('ALIGNMENT')]
    P('\nS4b purification history (p < .01 and |b| ≥ 0.24 flags; the largest flagged |b| was freed each iteration): ' + '; '.join(
        f"{sv} iteration {int(g.iteration.iloc[0])} (already freed: {g.already_freed.iloc[0] if isinstance(g.already_freed.iloc[0], str) and g.already_freed.iloc[0] else 'none'}): flagged "
        f"{', '.join(g[g.flag == True]['item']) or 'none'}" for (sv, it), g in pur.groupby(['survey', 'iteration'])) + '.')
    al = ph[ph.already_freed.astype(str).str.startswith('ALIGNMENT')]
    if len(al):
        P('\nS4d alignment (anchor-free; Spanish − English aligned intercept, probit scale, per factor): ' + '; '.join(
            f"{sv} {fac.replace('ALIGNMENT ', '')}: " + ', '.join(f"{LAB[r['item']]} {f(r.est, 2)}" for _, r in g.iterrows())
            for (sv, fac), g in al.groupby(['survey', 'already_freed'])) + '.')
        for fn in sorted(os.listdir(SEC)):
            if fn.startswith('s4d_alignment_'):
                a = pd.read_csv(os.path.join(SEC, fn))
                P(f"  - {a.survey.iloc[0]} {a.factor.iloc[0]}: aligned Spanish latent mean {f(a.aligned_mean_Sp.iloc[0], 3)}, SD {f(a.aligned_sd_Sp.iloc[0], 3)}; "
                  f"invariance R² loadings {f(a.R2_lambda.iloc[0], 3)}, intercepts {f(a.R2_nu.iloc[0], 3)}.")
    P('')

P('### S5: impact on the Spanish-English gap (8 harmonized items; replicate 95% CIs)\n')
P('| Survey | Quantity | Observed | Model-implied (as estimated) | Model-implied, target DIF removed | Change in gap | % of model-implied gap due to target DIF |')
P('|---|---|---|---|---|---|---|')
for sv in ('brfss', 'chis'):
    p = os.path.join(SEC, f's5_impact_{sv}.csv')
    if os.path.exists(p):
        m = pd.read_csv(p).set_index('quantity')
        c = lambda k, d=2: f"{f(m.loc[k, 'estimate'], d)} ({f(m.loc[k, 'ci_lo'], d)}, {f(m.loc[k, 'ci_hi'], d)})"
        P(f"| {sv.upper()} | Gap in mean 8-item count (Sp − En) | {c('gap_mean_obs')} | {c('gap_mean_model')} | {c('gap_mean_noDIF')} | {c('change_gap_mean')} | {c('pct_gap_mean_due_DIF', 1)} |")
        P(f"| {sv.upper()} | Gap in % with ≥ 4 of 8 items (pp) | {c('gap_p4_obs', 1)} | {c('gap_p4_model', 1)} | {c('gap_p4_noDIF', 1)} | {c('change_gap_p4', 1)} | {c('pct_gap_p4_due_DIF', 1)} |")
        P(f"| {sv.upper()} | Spanish mean count / % ≥ 4: observed; model; DIF removed | {f(m.loc['mean_Sp_obs','estimate'])} / {f(m.loc['p4_Sp_obs','estimate'],1)}% | "
          f"{f(m.loc['mean_Sp_model','estimate'])} / {f(m.loc['p4_Sp_model','estimate'],1)}% | {f(m.loc['mean_Sp_noDIF','estimate'])} / {f(m.loc['p4_Sp_noDIF','estimate'],1)}% | "
          f"English: obs {f(m.loc['mean_En_obs','estimate'])} / {f(m.loc['p4_En_obs','estimate'],1)}%; model {f(m.loc['mean_En_model','estimate'])} / {f(m.loc['p4_En_model','estimate'],1)}% | |")
P('')

P('### S6: interview mode (CHIS; Spanish × web interaction on the target direct effects; lavaan robust SEs)\n')
p6 = os.path.join(SEC, 's6_mode.csv')
if os.path.exists(p6):
    m = pd.read_csv(p6)
    P('| Item | Term | b | SE | p | OR-equiv. (95% CI) |')
    P('|---|---|---:|---:|---:|---|')
    for _, r in m.iterrows():
        if r['item'] in T:
            P(f"| {LAB[r['item']]} | {r.term} | {f(r.est, 3)} | {f(r.se, 3)} | {pv(r.pvalue)} | {orci(r.est, r['ci.lower'], r['ci.upper'])} |")
    P('')

P('### S7: BRFSS 11 items, three-factor MIMIC (lavaan robust SEs)\n')
p7 = os.path.join(SEC, 's7_effects.csv')
if os.path.exists(p7):
    m = pd.read_csv(p7)
    P('| Parameter | b | SE | p | OR-equiv. (95% CI) | Model-implied Δ endorsement (pp) |')
    P('|---|---:|---:|---:|---|---:|')
    for _, r in m.iterrows():
        P(f"| {LAB.get(r.lhs, r.lhs)} | {f(r.est, 3)} | {f(r.se, 3)} | {pv(r.pvalue)} | {orci(r.est, r['ci.lower'], r['ci.upper']) if r.lhs in T else ''} | {f(r.get('pdiff_pp', np.nan), 1)} |")
    P('')

# ---------------------------------------------------------------- deviations / files
P('## 6. Deviations and clarifications\n')
P('Full list with reasons: `analysis/DEVIATIONS.md`. In brief:')
P('- **Deviations:** (1) For the BRFSS Rao-Wu bootstrap only, 749 single-PSU strata were collapsed into the nearest multi-PSU stratum in the same year × file × state, because subbootstrap weights are undefined for 1-PSU strata. Taylor analyses use the planned strata with lonely PSU = adjust. (2) Integer PSU/stratum IDs were passed to `as.svrepdesign`; this is a speed-only change to the same algorithm.')
P('- **No deviation needed:** Ford et al. (2014) places witnessed parental violence on the abuse factor, as planned. lavaan 0.7.2 supports WLSMV with sampling weights for ordered items, so no fallback was used.')
P('- **Clarifications** (open details fixed before fitting): missing BRFSS age/education kept as categories; replicate variance MSE = TRUE; two-sided Wald p; the partial-support rule was read as the same items in both surveys (alternative reading reported); S3 binary-item identification; S4b one-item-per-iteration purification; S6 includes web main effects; S5 uses 8 harmonized items; Table 2 has one extra, labelled CHIS + nativity column.')
P('- **Implementation note (S3):** lavaan 0.7.2 did not apply `group.equal = "thresholds"` for these binary items (scalar df 44 instead of 50; latent means stayed fixed). The MGCFA models were therefore re-specified with explicit equality labels and verified by their df (38/50/44). The first S3 run is marked superseded in STATUS.md; only the corrected run is reported.\n')
P('## 7. Files\n')
P('- Scripts: `/home/mo2273/ace_manuscript/scripts/` (`common.R`, `01_prep.R`, `02_table1.R`, `03_table2.R`, `04_primary_mimic.R`, `04b_verdict.R`, `05_secondary.R`, `06_s5_impact.R`, `make_figures.py`, `make_results.py`, `run.sh`)')
P('- Analytic data: `analysis/data/brfss_analytic.{rds,csv}`, `analysis/data/chis_analytic.{rds,csv}`, `analysis/data/brfss_boot100_weights.rds`')
P('- Tables: `analysis/table1.{csv,md}`, `analysis/table2.{csv,md}`')
P('- Primary: `analysis/primary_results.{csv,md}`, `analysis/H1_verdict.json`, `analysis/primary/` (fits, all parameters, replicate coefficient matrices, fit indices, logs)')
P('- Secondary: `analysis/secondary/` (`effects_s1.csv`, `effects_s2.csv`, `h1b_verdict.json`, `s3_*.csv`, `s4_effects.csv`, `s4b_purification_history.csv`, `s4d_alignment_*.csv`, `s5_impact_*.csv`, `s6_mode.csv`, `s7_effects.csv`)')
P('- Figures: `figures/fig1_item_prevalence_by_language`, `fig2_dif_estimates_all_items`, `fig3_robustness_target_dif`, `fig4_impact_gap` (each .png at 300 dpi, .pdf and .csv of the plotted numbers)')
P('- Log: `analysis/STATUS.md`; deviations: `analysis/DEVIATIONS.md`')
open(os.path.join(AN, 'RESULTS.md'), 'w').write('\n'.join(out) + '\n')
print('RESULTS.md written', len(out), 'lines')
