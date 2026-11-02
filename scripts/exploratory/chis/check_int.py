"""usage: python -I check_int.py chis_pooled.csv : diagnose verbal language x mode interaction SE"""
import sys, numpy as np, pandas as pd, statsmodels.api as sm, warnings
warnings.filterwarnings('ignore')
d = pd.read_csv(sys.argv[1]); d = d[(d.ombsrr_p1 == 1) & d.intvlngc_p1.isin([1, 2])].copy()
W = [f'rakedw{i}' for i in range(81)]
for c in W: d[c] = d[c] / 5
d['sp'] = (d.intvlngc_p1 == 2) * 1.0; d['web'] = (d.intv_mode2 == 2) * 1.0; d['fb'] = (d.ah33new == 2) * 1.0
d['y'] = (d.aq8 >= 2) * 1.0; d['spxweb'] = d.sp * d.web; d['f'] = (d.srsex == 2) * 1.0
X = pd.concat([pd.DataFrame({'const': 1.0, 'sp': d.sp, 'web': d.web, 'spxweb': d.spxweb, 'fb': d.fb, 'f': d.f})] +
              [pd.get_dummies(d[c].astype(int), prefix=c, drop_first=True, dtype=float) for c in ['srage_p1', 'ahedc_p1', 'povll', 'year', 'pctlf_p']], axis=1)
est = []
for w in W:
    try: est.append(sm.GLM(d.y, X, family=sm.families.Binomial(), var_weights=d[w]).fit().params['spxweb'])
    except Exception as e: est.append(np.nan)
est = np.array(est); print('b0', est[0], 'n_nan', np.isnan(est[1:]).sum(), 'jk SE', np.sqrt(np.nansum((est[1:] - est[0]) ** 2)))
print('replicate spread', np.nanmin(est[1:]), np.nanmax(est[1:]))
