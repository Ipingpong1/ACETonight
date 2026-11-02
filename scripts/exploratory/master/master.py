"""usage: python -I master.py BRFSS_dif_analytic.csv CHIS_pooled.csv OUTDIR
Harmonized 9-item comparison, Spanish vs English interview, Hispanic adults; sequential adjustment; BRFSS+CHIS meta-analysis."""
import sys, os, numpy as np, pandas as pd, statsmodels.api as sm, warnings
from scipy.stats import norm, chi2
warnings.filterwarnings('ignore')
bf, cf, out = sys.argv[1:4]; os.makedirs(out, exist_ok=True)
ITEMS = ['mh', 'drink', 'drugs', 'jail', 'divorce', 'ipv', 'phys', 'verbal', 'sexual']
CORE = ITEMS[:-1]
def dummies(df, cols):
    return [pd.get_dummies(df[c].astype(int), prefix=c, drop_first=True, dtype=float) for c in cols]
# ---------- BRFSS ----------
b = pd.read_csv(bf)
m = {'mh': 'DEPRS', 'drink': 'DRINK', 'drugs': 'DRUGS', 'jail': 'PRISN', 'divorce': 'DIVRC', 'ipv': 'PUNCH', 'phys': 'HURT', 'verbal': 'SWEAR'}
for k, v in m.items(): b[k] = b['e_ACE' + v]
b['sexual'] = b[['e_ACETOUCH', 'e_ACETTHEM', 'e_ACEHVSEX']].max(axis=1)
b['sp'] = (b.lang == 'Spanish') * 1.0; b['female'] = (b.sex == 2) * 1.0
b['w'] = b.wt / b.groupby(['year', 'source']).wt.transform('mean')
b['clu'] = b.year.astype(str) + b.source + '_' + b._STSTR.astype(str) + '_' + b._PSU.astype(str)
# ---------- CHIS ----------
c = pd.read_csv(cf); c = c[(c.ombsrr_p1 == 1) & c.intvlngc_p1.isin([1, 2])].copy()
W = [f'rakedw{i}' for i in range(81)]
for x in W: c[x] = c[x] / c.year.nunique()
c['sp'] = (c.intvlngc_p1 == 2) * 1.0; c['female'] = (c.srsex == 2) * 1.0; c['fb'] = (c.ah33new == 2) * 1.0; c['web'] = (c.intv_mode2 == 2) * 1.0
for k, cond in {'mh': c.aq1 == 1, 'drink': c.aq2 == 1, 'drugs': c.aq3 == 1, 'jail': c.aq4 == 1, 'divorce': c.aq5 == 1,
                'ipv': c.aq6 >= 2, 'phys': c.aq7 >= 2, 'verbal': c.aq8 >= 2}.items(): c[k] = cond * 1.0
c['subst'] = ((c.drink + c.drugs) > 0) * 1.0
cnt7 = c[['mh', 'subst', 'jail', 'divorce', 'ipv', 'phys', 'verbal']].sum(axis=1); a8 = c.ace8 - 1
c['sexual'] = np.where(a8 < 4, a8 - cnt7, np.where(cnt7 == 3, 1, np.nan))
# model ladders (name, covariate blocks)
LAD_B = [('M0 crude', [], []), ('M1 +age,sex', ['_AGEG5YR'], ['female']), ('M2 +educ,income', ['_AGEG5YR', 'EDUCA', 'inc5'], ['female']),
         ('M3 +year,state', ['_AGEG5YR', 'EDUCA', 'inc5', 'year', 'state'], ['female'])]
LAD_C = [('M0 crude', [], []), ('M1 +age,sex', ['srage_p1'], ['female']), ('M2 +educ,income', ['srage_p1', 'ahedc_p1', 'povll'], ['female']),
         ('M3 +year', ['srage_p1', 'ahedc_p1', 'povll', 'year'], ['female']),
         ('M4 +nativity,%life US', ['srage_p1', 'ahedc_p1', 'povll', 'year', 'pctlf_p'], ['female', 'fb']),
         ('M5 +mode', ['srage_p1', 'ahedc_p1', 'povll', 'year', 'pctlf_p'], ['female', 'fb', 'web'])]
def X_of(df, cats, nums, extra=None):
    X = pd.concat([pd.DataFrame({'const': 1.0, 'sp': df.sp}, index=df.index)] + [df[nums]] + dummies(df, cats), axis=1)
    if extra is not None: X['rest'] = extra
    return X
def fit_b(df, y, cats, nums, rest=None):
    X = X_of(df, cats, nums, rest)
    r = sm.GLM(df[y], X, family=sm.families.Binomial(), var_weights=df.w).fit(cov_type='cluster', cov_kwds={'groups': pd.factorize(df.clu)[0]})
    return r.params['sp'], r.bse['sp']
def fit_c(df, y, cats, nums, rest=None):
    df = df[df[y].notna()]; X = X_of(df, cats, nums, None if rest is None else rest.loc[df.index])
    e = np.array([sm.GLM(df[y], X, family=sm.families.Binomial(), var_weights=df[w]).fit().params['sp'] for w in W])
    return e[0], np.sqrt(((e[1:] - e[0]) ** 2).sum())
rows = []
def wp(df, y, g, wcol):
    s = df[df[y].notna() & (df.sp == g)]; return 100 * np.average(s[y], weights=s[wcol])
for ds, df, lad, f, wcol in [('BRFSS', b, LAD_B, fit_b, 'w'), ('CHIS', c, LAD_C, fit_c, 'rakedw0')]:
    for y in ITEMS:
        base = {'dataset': ds, 'item': y, 'pct_sp': wp(df, y, 1, wcol), 'pct_en': wp(df, y, 0, wcol)}
        for name, cats, nums in lad:
            est, se = f(df, y, cats, nums); rows.append({**base, 'model': name, 'logOR': est, 'se': se}); print(ds, y, name, round(np.exp(est), 3), flush=True)
        rest = df[[i for i in CORE if i != y]].sum(axis=1)
        name, cats, nums = lad[-1] if ds == 'BRFSS' else lad[4]
        est, se = f(df, y, cats, nums, rest); rows.append({**base, 'model': 'DIF (' + name.split()[0] + ' + other items)', 'logOR': est, 'se': se})
        print(ds, y, 'DIF', round(np.exp(est), 3), flush=True)
    if ds == 'CHIS':  # foreign-born only, M4 covariates minus fb
        fbd = df[df.fb == 1]
        for y in ITEMS:
            est, se = f(fbd, y, ['srage_p1', 'ahedc_p1', 'povll', 'year', 'pctlf_p'], ['female'])
            rows.append({'dataset': 'CHIS', 'item': y, 'pct_sp': wp(fbd, y, 1, wcol), 'pct_en': wp(fbd, y, 0, wcol), 'model': 'FB-only (M4)', 'logOR': est, 'se': se})
            rest = fbd[[i for i in CORE if i != y]].sum(axis=1)
            est, se = f(fbd, y, ['srage_p1', 'ahedc_p1', 'povll', 'year', 'pctlf_p'], ['female'], rest)
            rows.append({'dataset': 'CHIS', 'item': y, 'pct_sp': np.nan, 'pct_en': np.nan, 'model': 'FB-only DIF', 'logOR': est, 'se': se})
R = pd.DataFrame(rows)
R['OR'] = np.exp(R.logOR); R['lo'] = np.exp(R.logOR - 1.96 * R.se); R['hi'] = np.exp(R.logOR + 1.96 * R.se)
R['p'] = 2 * (1 - norm.cdf(np.abs(R.logOR / R.se)))
crude = R[R.model == 'M0 crude'].set_index(['dataset', 'item']).logOR
R['pct_gap_explained'] = [100 * (1 - r.logOR / crude[(r.dataset, r.item)]) for r in R.itertuples()]
R.to_csv(f'{out}/ladder.csv', index=False)
# meta-analysis: BRFSS M3 vs CHIS M3 (same covariates), and BRFSS DIF vs CHIS DIF
meta = []
for y in ITEMS:
    for lab, mb, mc in [('adjusted (age,sex,educ,income,year)', 'M3 +year,state', 'M3 +year'), ('DIF', 'DIF (M3 + other items)', 'DIF (M4 + other items)')]:
        rb = R[(R.dataset == 'BRFSS') & (R.item == y) & (R.model == mb)].iloc[0]; rc = R[(R.dataset == 'CHIS') & (R.item == y) & (R.model == mc)].iloc[0]
        wb, wc = 1 / rb.se ** 2, 1 / rc.se ** 2; pooled = (wb * rb.logOR + wc * rc.logOR) / (wb + wc); pse = (wb + wc) ** -0.5
        Q = wb * (rb.logOR - pooled) ** 2 + wc * (rc.logOR - pooled) ** 2
        meta.append({'item': y, 'analysis': lab, 'OR_BRFSS': np.exp(rb.logOR), 'OR_CHIS': np.exp(rc.logOR), 'OR_pooled': np.exp(pooled),
                     'lo': np.exp(pooled - 1.96 * pse), 'hi': np.exp(pooled + 1.96 * pse), 'p_pooled': 2 * (1 - norm.cdf(abs(pooled / pse))),
                     'p_surveys_differ': 1 - chi2.cdf(Q, 1)})
pd.DataFrame(meta).to_csv(f'{out}/meta.csv', index=False); print(pd.DataFrame(meta).round(3).to_string())
