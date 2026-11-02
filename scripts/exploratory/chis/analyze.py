"""usage: python -I analyze.py chis_pooled.csv OUTDIR
CHIS 2021-25 Hispanic adults, Spanish vs English interview. Jackknife replicate SEs (rakedw1-80, multiplier 1, mse)."""
import sys, os, numpy as np, pandas as pd, statsmodels.api as sm, warnings
warnings.filterwarnings('ignore')
src, out = sys.argv[1], sys.argv[2]; os.makedirs(out, exist_ok=True)
d = pd.read_csv(src)
d = d[(d.ombsrr_p1 == 1) & d.intvlngc_p1.isin([1, 2])].copy()
NY = d.year.nunique()
W = [f'rakedw{i}' for i in range(81)]
for c in W: d[c] = d[c] / NY
d['sp'] = (d.intvlngc_p1 == 2).astype(float)
d['fb'] = (d.ah33new == 2).astype(float)
d['web'] = (d.intv_mode2 == 2).astype(float)
it = {'mh': d.aq1 == 1, 'drink': d.aq2 == 1, 'drugs': d.aq3 == 1, 'jail': d.aq4 == 1, 'divorce': d.aq5 == 1,
      'ipv': d.aq6 >= 2, 'phys': d.aq7 >= 2, 'verbal': d.aq8 >= 2}
for k, v in it.items(): d[k] = v.astype(float)
d['subst'] = ((d.drink + d.drugs) > 0).astype(float)
d['count7'] = d[['mh', 'subst', 'jail', 'divorce', 'ipv', 'phys', 'verbal']].sum(axis=1)
d['ace8c'] = d.ace8 - 1  # 0..4 (4=4+)
sx = np.where(d.ace8c < 4, d.ace8c - d.count7, np.where(d.count7 == 3, 1, np.where(d.count7 < 3, -9, np.nan)))
d['sexchk'] = sx
d['sexual'] = np.where(np.isin(sx, [0, 1]), sx, np.nan)
d['ace4'] = (d.ace8c == 4).astype(float)
d['spd'] = (d.dstrs30 == 1).astype(float); d.loc[d.dstrs30 < 0, 'spd'] = np.nan
d['fairpoor'] = (d.ab1 >= 4).astype(float)
log = open(f'{out}/log.txt', 'w')
def P(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); log.write(s + '\n')
P('sexual derivation check (ace8c - count7 when ace8<4):', pd.Series(sx).value_counts(dropna=False).to_dict())
P('N Hispanic', len(d), 'Spanish', int(d.sp.sum()), 'English', int((1 - d.sp).sum()))
P(pd.crosstab([d.sp, d.fb], d.web, margins=True).to_string())

def dm(df, cov):
    X = pd.DataFrame({'const': 1.0}, index=df.index)
    for c in cov:
        if c in ('sp', 'fb', 'web', 'srsex2', 'rest', 'acec', 'spxacec', 'spxweb') or c.startswith('num_'):
            X[c] = df[c.replace('num_', '')] if c.startswith('num_') else df[c]
        else:
            X = X.join(pd.get_dummies(df[c].astype(int), prefix=c, drop_first=True, dtype=float))
    return X
def fit(df, y, cov, terms):
    df = df[df[y].notna()]
    X = dm(df, cov); Y = df[y].values
    est = []
    for w in W:
        try:
            r = sm.GLM(Y, X, family=sm.families.Binomial(), var_weights=df[w].values).fit()
            est.append([r.params[t] for t in terms])
        except Exception:
            est.append([np.nan] * len(terms))
    est = np.array(est); b0 = est[0]; se = np.sqrt(np.nansum((est[1:] - b0) ** 2, axis=0))
    return b0, se, len(df)
def wpct(df, y, g):
    s = df[df[y].notna()]
    return 100 * np.average(s.loc[s.sp == g, y], weights=s.loc[s.sp == g, 'rakedw0'])
d['srsex2'] = (d.srsex == 2).astype(float)
base = ['sp', 'srage_p1', 'srsex2', 'ahedc_p1', 'povll', 'year']
nat = base + ['fb', 'pctlf_p']
items = ['mh', 'drink', 'drugs', 'jail', 'divorce', 'ipv', 'phys', 'verbal', 'sexual', 'ace4', 'spd', 'fairpoor']
rows = []
fbonly = d[d.fb == 1]
for y in items:
    r = {'item': y, 'pct_sp': wpct(d, y, 1), 'pct_en': wpct(d, y, 0),
         'fb_pct_sp': wpct(fbonly, y, 1), 'fb_pct_en': wpct(fbonly, y, 0)}
    for lab, df, cov in [('crude', d, ['sp']), ('adj_brfss', d, base), ('adj_nat', d, nat),
                         ('fb_only', fbonly, base + ['pctlf_p']), ('adj_nat_mode', d, nat + ['web'])]:
        b, s, n = fit(df, y, cov, ['sp'])
        r[f'OR_{lab}'] = np.exp(b[0]); r[f'lo_{lab}'] = np.exp(b[0] - 1.96 * s[0]); r[f'hi_{lab}'] = np.exp(b[0] + 1.96 * s[0])
    rows.append(r); P(y, {k: round(v, 2) for k, v in r.items() if k != 'item'})
res = pd.DataFrame(rows); res.to_csv(f'{out}/or_table.csv', index=False)

# DIF: item ~ rest score (other 7 non-sexual binary items, substance split) + sp + covariates incl nativity
P('\nDIF (rest score = other non-sexual items), adjusted for base + nativity:')
core = ['mh', 'drink', 'drugs', 'jail', 'divorce', 'ipv', 'phys', 'verbal']
drows = []
for y in core + ['sexual']:
    others = [c for c in core if c != y]
    d['rest'] = d[others].sum(axis=1)
    out_r = {'item': y}
    for lab, df, cov in [('dif_base', d, base + ['rest']), ('dif_nat', d, nat + ['rest']), ('dif_fb', d[d.fb == 1], base + ['pctlf_p', 'rest'])]:
        b, s, n = fit(df, y, cov, ['sp'])
        out_r[f'OR_{lab}'] = np.exp(b[0]); out_r[f'lo_{lab}'] = np.exp(b[0] - 1.96 * s[0]); out_r[f'hi_{lab}'] = np.exp(b[0] + 1.96 * s[0])
    drows.append(out_r); P(y, {k: round(v, 2) for k, v in out_r.items() if k != 'item'})
pd.DataFrame(drows).to_csv(f'{out}/dif_table.csv', index=False)

# language x mode
P('\nSpanish vs English OR within mode (adj base+nativity):')
mrows = []
for y in ['mh', 'drugs', 'jail', 'verbal', 'phys', 'divorce', 'ace4', 'spd']:
    r = {'item': y}
    for lab, m in [('phone', 0), ('web', 1)]:
        b, s, n = fit(d[d.web == m], y, nat, ['sp'])
        r[f'OR_{lab}'] = np.exp(b[0]); r[f'lo_{lab}'] = np.exp(b[0] - 1.96 * s[0]); r[f'hi_{lab}'] = np.exp(b[0] + 1.96 * s[0])
    d['spxweb'] = d.sp * d.web
    b, s, n = fit(d, y, nat + ['web', 'spxweb'], ['spxweb'])
    r['p_int'] = float(2 * (1 - __import__('scipy').stats.norm.cdf(abs(b[0] / s[0]))))
    mrows.append(r); P(y, {k: round(v, 3) for k, v in r.items() if k != 'item'})
pd.DataFrame(mrows).to_csv(f'{out}/mode_table.csv', index=False)

# differential prediction: SPD ~ ACE count x language
d['acec'] = d.count7 + d.sexual.fillna(0)  # approx 8-cat count (sexual unknown for some 4+ -> 0)
d['spxacec'] = d.sp * d.acec
b, s, n = fit(d, 'spd', nat + ['acec', 'spxacec'], ['acec', 'spxacec'])
from scipy.stats import norm
P('\nDifferential prediction SPD: OR per ACE English', round(np.exp(b[0]), 3), 'Spanish', round(np.exp(b[0] + b[1]), 3),
  'interaction p', round(2 * (1 - norm.cdf(abs(b[1] / s[1]))), 3))
d['acec_mh'] = d.mh; d['spxacec'] = d.sp * d.mh
dd = d.copy(); dd['acec'] = dd.mh
b, s, n = fit(dd, 'spd', nat + ['acec', 'spxacec'], ['acec', 'spxacec'])
P('Differential prediction SPD on household-MH item: OR English', round(np.exp(b[0]), 3), 'Spanish', round(np.exp(b[0] + b[1]), 3),
  'interaction p', round(2 * (1 - norm.cdf(abs(b[1] / s[1]))), 3))
# mean ACE count by language
for lab, df in [('all', d), ('foreign-born', fbonly.assign(acec=d.loc[fbonly.index, 'acec']))]:
    P(f'mean approx ACE count {lab}: Spanish', round(np.average(df.loc[df.sp == 1, 'acec'], weights=df.loc[df.sp == 1, 'rakedw0']), 2),
      'English', round(np.average(df.loc[df.sp == 0, 'acec'], weights=df.loc[df.sp == 0, 'rakedw0']), 2))
log.close()
