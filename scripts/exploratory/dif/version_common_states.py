"""2019 vs 2020 change in uniform language DIF restricted to states with >=30 Spanish-interview respondents in BOTH years.
usage: python -I version_common_states.py ANALYTIC_CSV OUTDIR"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, pandas as pd
from scipy import stats
import run_dif as R
out = sys.argv[2]
d0 = R.d0[R.d0.year.isin([2019, 2020])]
c = d0[d0.sp == 1].groupby(['state', 'year']).size().unstack(fill_value=0)
common = c[(c[2019] >= 30) & (c[2020] >= 30)].index.tolist()
print('common states', common, c.loc[common].to_dict('index'))
dd, cc = R.prep(d0[d0.state.isin(common)], cov_vars=('_AGEG5YR', 'EDUCA', 'sex', 'inc5', 'st'))
print('n', len(dd), 'Sp', int(dd.sp.sum()), dd.groupby(['year', 'sp']).size().to_dict())
y20 = (dd.year == 2020).astype(float).values
anch_pur = ['ACEDRINK', 'ACEDIVRC', 'ACEPUNCH', 'ACEHURT', 'ACETOUCH', 'ACETTHEM', 'ACEHVSEX']
rows = []
for lab, a in (('A0 all other items (unpurified)', None), ('A1 purified', anch_pur)):
    for uc in (False, True):
        for it in R.ITEMS:
            S, _ = R.matching(dd, it, a)
            X = np.column_stack([np.ones(len(dd)), S, dd.sp.values, y20, dd.sp.values * y20, S * y20] + ([cc] if uc else []))
            b, V, _, _ = R.fit(dd['e_' + it].values, X, dd.w.values, dd.clu.values)
            se = np.sqrt(V[4, 4])
            rows.append(dict(analysis=lab, cov=uc, item=it, OR_2019=np.exp(b[2]), OR_2020=np.exp(b[2] + b[4]), ratio=np.exp(b[4]),
                             lo=np.exp(b[4] - 1.96 * se), hi=np.exp(b[4] + 1.96 * se), p=2 * stats.norm.sf(abs(b[4] / se)),
                             states='+'.join(map(str, common)), n_clusters=int(dd.clu.max() + 1)))
r = pd.DataFrame(rows)
r.to_csv(f'{out}/version_2019_vs_2020_common_states.csv', index=False)
pd.set_option('display.width', 200)
print(r.drop(columns=['states']).round(3).to_string())
