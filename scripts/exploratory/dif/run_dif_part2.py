"""Sections 4-5 of the language-DIF first pass: version split (2019 / 2020 / 2021-25) and ACEDIVRC code-8 sensitivity.
usage: python -I run_dif_part2.py ANALYTIC_CSV OUTDIR   (imports functions from run_dif.py in the same directory)"""
import sys, os, warnings
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import pandas as pd
from scipy import stats
import run_dif as R

out = sys.argv[2]
d0 = R.d0
h = pd.read_csv(f'{out}/purification_history.csv')
last = h[h.analysis == 'Purified (no cov)'].iloc[-1]
ANCH_PUR = ['ACE' + a for a in last.anchors.split('+')]
print('purified anchors', ANCH_PUR, flush=True)
SCHEMES = (('A0 all other items (unpurified)', None), ('A1 purified', ANCH_PUR),
           ('A3 drink+divorce+3 sexual', R.ANCHORS['A3 drink+divorce+3 sexual']))


def run_w(*a, **k):
    with warnings.catch_warnings(record=True) as wl:
        warnings.simplefilter('always')
        r, p = R.run(*a, **k)
    r['n_warnings'] = len(wl)
    r['warnings'] = '; '.join(sorted(set(f'{w.category.__name__}: {str(w.message)[:60]}' for w in wl)))
    return r, p


# ---- 4. version split ----
vs = []
for pn, yrs in (('2019', [2019]), ('2020', [2020]), ('2021-2025', [2021, 2022, 2023, 2024, 2025])):
    dd, cc = R.prep(d0[d0.year.isin(yrs)])
    for lab, a in SCHEMES:
        for uc in (False, True):
            r, _ = run_w(dd, cc, a, uc, True, lab)
            r['period'], r['n_sp'], r['n_en'] = pn, int(dd.sp.sum()), int((dd.sp == 0).sum())
            vs.append(r)
            print(pn, lab, uc, r.n_warnings.iloc[0], flush=True)
pd.concat(vs, ignore_index=True).to_csv(f'{out}/version_split.csv', index=False)

# 2019 vs 2020 change in uniform DIF: item ~ S + sp + y20 + sp:y20 + S:y20 (+ cov without year dummies)
dd, cc = R.prep(d0[d0.year.isin([2019, 2020])], cov_vars=('_AGEG5YR', 'EDUCA', 'sex', 'inc5', 'st'))
y20 = (dd.year == 2020).astype(float).values
inter = []
for lab, a in SCHEMES:
    for uc in (False, True):
        for it in R.ITEMS:
            S, _ = R.matching(dd, it, a)
            X = np.column_stack([np.ones(len(dd)), S, dd.sp.values, y20, dd.sp.values * y20, S * y20] + ([cc] if uc else []))
            with warnings.catch_warnings(record=True) as wl:
                warnings.simplefilter('always')
                b, V, _, _ = R.fit(dd['e_' + it].values, X, dd.w.values, dd.clu.values)
            se = np.sqrt(V[4, 4])
            inter.append(dict(analysis=lab, cov=uc, item=it, OR_2019=np.exp(b[2]), OR_2020=np.exp(b[2] + b[4]),
                              ratio_OR_2020_vs_2019=np.exp(b[4]), lo=np.exp(b[4] - 1.96 * se), hi=np.exp(b[4] + 1.96 * se),
                              p=2 * stats.norm.sf(abs(b[4] / se)), n_warnings=len(wl)))
pd.DataFrame(inter).to_csv(f'{out}/version_2019_vs_2020_interaction.csv', index=False)
print('interaction done', flush=True)

# ---- 5. ACEDIVRC code-8 sensitivity ----
sens = []
for mode in ('endorsed', 'excluded'):
    dd, cc = R.prep(d0, mode)
    r, _ = run_w(dd, cc, None, False, True, 'A0 all other items (unpurified)')
    r['divrc8'] = mode
    sens.append(r)
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        r, _, an, _ = R.purify(dd, cc, False, True, f'Purified divrc8={mode}')
    r['divrc8'], r['analysis'], r['purified_anchors'] = mode, 'A1 purified', '+'.join(an)
    sens.append(r)
pd.concat(sens, ignore_index=True).to_csv(f'{out}/divrc8_sensitivity.csv', index=False)
print('done', flush=True)
