"""BRFSS: Spanish- vs English-interview differences among Hispanic respondents in own mental-health reports and ACE items.
usage: python -I analyze_mh.py WORK MHDIR OUTDIR SCRIPTDIR
  WORK   = /home/mo2273/ace_brfss_work   (extract_<tag>.csv with ACE items + covariates)
  MHDIR  = extract_mh_<tag>.csv dir      (from extract_mh.py)
Weights: final weights rescaled to mean 1 within each survey year of each analysis sample (main + version-file
respondents of a year together; version weights are on the same state-population scale as _LLCPWT).
SEs: GLM with var_weights + cluster-robust sandwich, clusters = year x _STSTR x _PSU (approximate design-based)."""
import sys, os, warnings
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats

work, mhdir, out, sdir = sys.argv[1:5]
sys.path.insert(0, sdir)
import mhcommon as mc

warnings.filterwarnings('ignore', category=pd.errors.PerformanceWarning)
os.makedirs(out, exist_ok=True)
COV = ' + C(agegrp) + C(sex) + C(educ) + C(income) + C(state) + C(year)'
ACEV = ['ACEDEPRS', 'ACEDRINK', 'ACEDRUGS', 'SUBST', 'ACEPRISN', 'ACEDIVRC', 'ACEPUNCH', 'ACEHURT', 'ACESWEAR', 'ACETOUCH',
        'ACETTHEM', 'ACEHVSEX', 'SEXANY']
LAB = {'dep': 'Own depression dx (ever told)', 'fmd': 'Frequent mental distress (MENTHLTH>=14)', 'mdays': 'Mean poor-MH days (0-30)',
       'fairpoor': 'Fair/poor general health', 'anx': 'Anxiety disorder dx (ever told)', 'phq10': 'PHQ-8 >= 10',
       'spd': 'K6 >= 13 (serious psych. distress)', 'lsat_dis': 'Dissatisfied with life', 'emo_low': 'Emotional support rarely/never',
       'lonely': 'Lonely always/usually', 'stress': 'Stress always/usually', 'ace4': 'ACE score (8-cat) >= 4',
       'e_ACEDEPRS': 'ACE: lived w/ depressed/mentally ill/suicidal', 'e_ACEDRINK': 'ACE: lived w/ problem drinker',
       'e_ACEDRUGS': 'ACE: lived w/ drug user', 'e_SUBST': 'ACE: household substance use (drink|drugs)',
       'e_ACEPRISN': 'ACE: lived w/ someone incarcerated', 'e_ACEDIVRC': 'ACE: parents separated/divorced',
       'e_ACEPUNCH': 'ACE: witnessed adults hit each other', 'e_ACEHURT': 'ACE: physically hurt by parent/adult',
       'e_ACESWEAR': 'ACE: sworn at/insulted', 'e_ACETOUCH': 'ACE: touched sexually', 'e_ACETTHEM': 'ACE: made to touch sexually',
       'e_ACEHVSEX': 'ACE: forced sex', 'e_SEXANY': 'ACE: any sexual abuse'}

# ---------------- load ----------------
mains, aces = [], []
for y in [2009, 2010, 2011, 2012, 2019, 2020, 2021, 2022, 2023, 2024, 2025]:
    main, ace = mc.load(work, mhdir, y)
    keep = lambda d: d[(d.hisp == 'Hispanic') | (d.state == 72)]
    mains.append(keep(main))
    aces.append(keep(ace))
    print(y, 'main Hisp/PR rows', len(mains[-1]), 'ACE Hisp/PR rows', len(aces[-1]), flush=True)
    del main, ace
M = pd.concat(mains, ignore_index=True)
A = pd.concat(aces, ignore_index=True)
for d in (M, A):
    d['ace4'] = np.where(d.ace8.notna(), (d.ace8 >= 4).astype(float), np.nan)
base = lambda d: d[(d.hisp == 'Hispanic') & ~d.terr & d.lang.isin(['English', 'Spanish']) & (d.wt > 0)].copy()
SA = base(A[A.year >= 2019])                       # (a) ACE respondents 2019-2025
SB = base(M[M.year >= 2019])                       # (b) all Hispanic respondents 2019-2025
SC = base(A[A.year <= 2012])                       # secondary: ACE respondents 2009-2012
SK = base(M[M.year.isin([2009, 2012])])            # K6 module years
SP = base(M[M.year.isin([2010, 2011])])            # PHQ-8 / anxiety module years
PR = A[(A.state == 72) & (A.year == 2024) & (A.lang == 'Spanish')].copy()


def nw(d):
    return d.wt / d.groupby('year').wt.transform('mean')


def cov_for(d):
    """Drop C(year) when year is nested in state (state-year graph disconnected -> state and year dummies collinear)."""
    sy = d[['state', 'year']].drop_duplicates()
    Z = pd.get_dummies(sy.astype(str)).astype(float).values
    full = sy.state.nunique() + sy.year.nunique() - 1
    return COV if np.linalg.matrix_rank(Z) >= full else COV.replace(' + C(year)', '')


def fit(d, y, adjust=True, extra='', fam='binomial', terms=('spanish',)):
    d = d[d[y].notna()].copy()
    rhs = 'spanish' + (cov_for(d) if adjust else '') + extra
    f = sm.families.Binomial() if fam == 'binomial' else sm.families.Gaussian()
    g = pd.factorize(d['cluster'])[0]
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        r = smf.glm(f'{y} ~ {rhs}', data=d, family=f, var_weights=nw(d)).fit(cov_type='cluster', cov_kwds={'groups': g})
    return r, d


def or_row(d, y, adjust, extra=''):
    fam = 'gaussian' if y == 'mdays' else 'binomial'
    try:
        r, dd = fit(d, y, adjust, extra, fam)
    except Exception as e:
        return {'est': np.nan, 'lo': np.nan, 'hi': np.nan, 'p': np.nan, 'err': str(e)[:60]}
    b, se = r.params['spanish'], r.bse['spanish']
    tr = (lambda x: x) if fam == 'gaussian' else np.exp
    return {'est': tr(b), 'lo': tr(b - 1.96 * se), 'hi': tr(b + 1.96 * se), 'p': r.pvalues['spanish']}


def wmean(x, w):
    m = x.notna()
    return float((x[m] * w[m]).sum() / w[m].sum()) if m.any() else np.nan


def key_rows(d, outcomes, sample):
    rows = []
    d = d.copy()
    d['w_n'] = nw(d)
    for y in outcomes:
        ok = d[y].notna()
        sp, en = ok & (d.lang == 'Spanish'), ok & (d.lang == 'English')
        if sp.sum() == 0:
            continue
        rec = {'sample': sample, 'measure': y, 'label': LAB.get(y, y), 'n_Sp': int(sp.sum()), 'n_En': int(en.sum()),
               'events_Sp': int((d.loc[sp, y] > 0).sum()) if y != 'mdays' else np.nan,
               'wprev_Sp': wmean(d.loc[sp, y], d.loc[sp, 'w_n']), 'wprev_En': wmean(d.loc[en, y], d.loc[en, 'w_n'])}
        c, a = or_row(d, y, False), or_row(d, y, True)
        rec.update({'crude': c['est'], 'crude_lo': c['lo'], 'crude_hi': c['hi'], 'adj': a['est'], 'adj_lo': a['lo'], 'adj_hi': a['hi'],
                    'adj_p': a['p'], 'scale': 'diff in days' if y == 'mdays' else 'OR', 'err': a.get('err', '')})
        rows.append(rec)
        print(sample, y, rec['n_Sp'], rec['n_En'], round(rec['wprev_Sp'], 3), round(rec['wprev_En'], 3), round(rec['crude'], 2), round(rec['adj'], 2), flush=True)
    return rows


MH = ['dep', 'fmd', 'mdays', 'fairpoor', 'lsat_dis', 'emo_low', 'lonely', 'stress']
AC = ['e_' + v for v in ACEV] + ['ace4']
rows = []
rows += key_rows(SA, MH + AC, 'A: ACE resp 2019-25')
rows += key_rows(SB, MH, 'B: all Hisp 2019-25')
rows += key_rows(SC, ['dep', 'fmd', 'mdays'] + ['e_' + v for v in ACEV], 'C: ACE resp 2009-12')
SK, SP = SK[SK.spd.notna()].copy(), SP[SP.phq10.notna()].copy()   # module respondents with valid scale
rows += key_rows(SK, ['spd', 'fmd', 'dep'], 'D1: K6 module resp 2009+2012 (dep: 2012 only)')
rows += key_rows(SK[SK.ace_any], ['spd'], 'D1a: K6 module, ACE resp')
rows += key_rows(SP, ['phq10', 'anx', 'dep', 'fmd'], 'D2: AD (PHQ-8) module resp 2010+2011')
rows += key_rows(SP[SP.ace_any], ['phq10', 'anx'], 'D2a: AD module, ACE resp')
KT = pd.DataFrame(rows)
KT.to_csv(f'{out}/key_or_table.csv', index=False)

# ---------------- sensitivity: depression dx + health-care access; ACEDEPRS adjusted for own MH ----------------
sens = []
for nm, d in [('A: ACE resp 2019-25', SA), ('B: all Hisp 2019-25', SB)]:
    for y in ['dep', 'fmd']:
        a = or_row(d, y, True, ' + C(insured) + C(persdoc)')
        sens.append({'sample': nm, 'model': f'{y} | covariates + insurance + personal doctor', **a})
dd = SA[SA.dep.notna() & SA.fmd.notna()]
sens.append({'sample': 'A', 'model': 'ACEDEPRS | covariates (same n as next row)', **or_row(dd, 'e_ACEDEPRS', True)})
sens.append({'sample': 'A', 'model': 'ACEDEPRS | covariates + own dep dx + FMD', **or_row(dd, 'e_ACEDEPRS', True, ' + dep + fmd')})
sens.append({'sample': 'A', 'model': 'ACEDEPRS | covariates + insurance + personal doctor', **or_row(SA, 'e_ACEDEPRS', True, ' + C(insured) + C(persdoc)')})
SENS = pd.DataFrame(sens)
SENS.to_csv(f'{out}/sensitivity.csv', index=False)
print(SENS.to_string())


# ---------------- ratio of adjusted ORs (stacked, same respondents) ----------------
def stacked(d, ya, yb):
    d = d[d[ya].notna() & d[yb].notna()].copy()
    d['w_n'] = nw(d)
    L = pd.concat([d.assign(yy=d[ya], k='a'), d.assign(yy=d[yb], k='b')], ignore_index=True)
    g = pd.factorize(L['cluster'])[0]
    rhs = 'C(k) * (spanish' + COV + ')'
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        r = smf.glm(f'yy ~ {rhs}', data=L, family=sm.families.Binomial(), var_weights=L['w_n']).fit(cov_type='cluster', cov_kwds={'groups': g})
    t = 'C(k)[T.b]:spanish'
    b, se = r.params[t], r.bse[t]
    # ratio reported as OR(ya)/OR(yb)  => exp(-b)
    return {'pair': f'{ya} vs {yb}', 'n': len(d), 'OR_a': np.exp(r.params['spanish']), 'OR_b': np.exp(r.params['spanish'] + b),
            'ratio_a_over_b': np.exp(-b), 'lo': np.exp(-b - 1.96 * se), 'hi': np.exp(-b + 1.96 * se), 'p': r.pvalues[t]}


st = []
for yb in ['dep', 'fmd', 'e_SUBST', 'e_ACEPRISN', 'e_ACEDIVRC', 'e_ACEPUNCH', 'e_ACEHURT', 'e_ACESWEAR', 'e_SEXANY']:
    st.append(stacked(SA, 'e_ACEDEPRS', yb))
    print(st[-1], flush=True)
st.append(stacked(SA, 'dep', 'e_ACEHURT'))
ST = pd.DataFrame(st)
ST.to_csv(f'{out}/ratio_of_ORs_stacked.csv', index=False)


# ---------------- differential prediction ----------------
def dp(d, y, x, extra=''):
    d = d[d[y].notna() & d[x].notna()].copy()
    g = pd.factorize(d['cluster'])[0]
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        r = smf.glm(f'{y} ~ {x} * spanish' + COV + extra, data=d, family=sm.families.Binomial(), var_weights=nw(d)).fit(
            cov_type='cluster', cov_kwds={'groups': g})
    it = f'{x}:spanish'
    V = r.cov_params()
    bE, seE = r.params[x], r.bse[x]
    bS = bE + r.params[it]
    seS = np.sqrt(V.loc[x, x] + V.loc[it, it] + 2 * V.loc[x, it])
    sp = d.spanish == 1
    return {'outcome': y, 'predictor': x, 'extra': extra.strip(), 'n_Sp': int(sp.sum()), 'n_En': int((~sp).sum()),
            'events_Sp': int(d.loc[sp, y].sum()), 'OR_En': np.exp(bE), 'OR_En_lo': np.exp(bE - 1.96 * seE), 'OR_En_hi': np.exp(bE + 1.96 * seE),
            'OR_Sp': np.exp(bS), 'OR_Sp_lo': np.exp(bS - 1.96 * seS), 'OR_Sp_hi': np.exp(bS + 1.96 * seS),
            'ratio_Sp_over_En': np.exp(r.params[it]), 'p_interaction': r.pvalues[it],
            'main_Spanish_OR_at_x0': np.exp(r.params['spanish'])}


SAc = SA[SA.ace_complete].copy()
dps = []
for y in ['dep', 'fmd']:
    for x, extra in [('ace8', ''), ('ace7_noDEPRS', ''), ('e_ACEDEPRS', ''), ('e_ACEDEPRS', ' + ace7_noDEPRS')]:
        dps.append(dp(SAc, y, x, extra))
        print(dps[-1], flush=True)
DP = pd.DataFrame(dps)
DP.to_csv(f'{out}/differential_prediction.csv', index=False)

# ---------------- N table ----------------
nt = []
for nm, d in [('A: ACE-module respondents 2019-25 (mainland)', SA), ('A, complete 11 ACE items (diff. prediction)', SAc),
              ('B: all Hispanic respondents 2019-25 (mainland)', SB), ('C: ACE-module respondents 2009-12', SC),
              ('D1: K6 module years 2009+2012, K6 valid', SK[SK.spd.notna()]), ('D1a: ...of which ACE respondents', SK[SK.spd.notna() & SK.ace_any]),
              ('D2: AD module years 2010+2011, PHQ-8 valid', SP[SP.phq10.notna()]), ('D2a: ...of which ACE respondents', SP[SP.phq10.notna() & SP.ace_any])]:
    nt.append({'analysis': nm, 'n_Spanish': int((d.lang == 'Spanish').sum()), 'n_English': int((d.lang == 'English').sum()),
               'wpct_Spanish': round(100 * wmean(d.spanish, nw(d)), 1),
               'states': d.state.nunique(), 'years': ','.join(str(v) for v in sorted(d.year.unique()))})
# SDOH availability within A and B
for nm, d in [('A', SA), ('B', SB)]:
    for v in ['lsat_dis', 'emo_low', 'lonely', 'stress']:
        ok = d[v].notna()
        nt.append({'analysis': f'{nm}: {v} valid', 'n_Spanish': int((ok & (d.lang == 'Spanish')).sum()), 'n_English': int((ok & (d.lang == 'English')).sum()),
                   'wpct_Spanish': np.nan, 'states': d[ok].state.nunique(), 'years': ','.join(str(v) for v in sorted(d[ok].year.unique()))})
NT = pd.DataFrame(nt)
NT.to_csv(f'{out}/n_table.csv', index=False)

# ---------------- Puerto Rico 2024 (descriptive) ----------------
PR['w_n'] = PR.wt / PR.wt.mean()
pr = []
for y in ['dep', 'fmd', 'mdays', 'e_ACEDEPRS', 'e_SUBST', 'e_ACEHURT', 'e_ACESWEAR', 'e_ACEPUNCH', 'e_ACEDIVRC', 'e_SEXANY', 'ace4']:
    ok = PR[y].notna()
    pr.append({'measure': y, 'label': LAB.get(y, y), 'n': int(ok.sum()), 'wprev_PR2024_Spanish': wmean(PR[y], PR.w_n)})
PRT = pd.DataFrame(pr)
PRT.to_csv(f'{out}/pr2024_descriptive.csv', index=False)

# ---------------- check: statsmodels var_weights cluster SE == manual linearization sandwich ----------------
r, d = fit(SA, 'e_ACEDEPRS', True)
X = r.model.exog
w = r.model.var_weights
mu = r.fittedvalues.values
yv = r.model.endog
S = X * (w * (yv - mu))[:, None]
H = (X * (w * mu * (1 - mu))[:, None]).T @ X
g = pd.factorize(d['cluster'])[0]
Sc = pd.DataFrame(S).groupby(g).sum().values
G, N, K = Sc.shape[0], X.shape[0], X.shape[1]
Hi = np.linalg.pinv(H)
Vm = Hi @ (Sc.T @ Sc) @ Hi * (G / (G - 1)) * ((N - 1) / (N - K))
j = r.model.exog_names.index('spanish')
print('SE check spanish: statsmodels', r.bse['spanish'], 'manual', np.sqrt(Vm[j, j]), 'G', G, 'N', N)

with pd.option_context('display.width', 250, 'display.max_columns', 40, 'display.max_rows', 400):
    print(NT.to_string(index=False)); print(KT.to_string(index=False)); print(ST.to_string(index=False)); print(DP.to_string(index=False)); print(PRT.to_string(index=False))
