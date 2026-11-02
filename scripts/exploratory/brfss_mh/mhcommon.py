"""Shared loading/coding for the BRFSS mental-health x interview-language analysis.
prep() and load() are copied from /home/mo2273/ace_brfss_scripts/analyze_ace_language.py (same codes, same
main-vs-version-file dedup); load_mh() adds the mental-health extract from the SAME source file as each row.
"""
import os
import numpy as np
import pandas as pd

TERR = {66, 72, 78}
YN = ['ACEDEPRS', 'ACEDRINK', 'ACEDRUGS', 'ACEPRISN']
FREQ = ['ACEPUNCH', 'ACEHURT', 'ACESWEAR', 'ACETOUCH', 'ACETTHEM', 'ACEHVSEX']
ITEMS = YN + ['ACEDIVRC'] + FREQ
PCE = ['ACEADSAF', 'ACEADNED']


def prep(d, y, wtcol, source):
    if 'ACEHURT1' in d.columns:
        d = d.rename(columns={'ACEHURT1': 'ACEHURT'})
    for v in ITEMS:                      # 2013-2018-style safety; ACE years always have them
        if v not in d.columns:
            d[v] = np.nan
    d['year'] = y
    d['wt'] = d[wtcol]
    d['wt_var'] = wtcol
    d['source'] = source
    d['key'] = d['_STATE'].round().astype(int).astype(str) + '_' + d['SEQNO'].astype(str).str.replace(r'\.0$', '', regex=True)
    q = d['QSTLANG']
    d['lang'] = np.select([q == 1, q == 2, (q >= 3) & (q <= 99)], ['English', 'Spanish', 'Other'], 'Missing')
    h = d['HISPANC2'] if y <= 2012 else d['_HISPANC']
    d['hisp'] = np.select([h == 1, h == 2], ['Hispanic', 'Non-Hispanic'], 'Unknown')
    d['state'] = d['_STATE'].round().astype(int)
    d['terr'] = d['state'].isin(TERR)
    d['ace_any'] = d[ITEMS].notna().any(axis=1)
    valid = pd.DataFrame({v: d[v].isin([1, 2]) for v in YN})
    valid['ACEDIVRC'] = d['ACEDIVRC'].isin([1, 2, 8])
    for v in FREQ:
        valid[v] = d[v].isin([1, 2, 3])
    d['ace_complete'] = valid.all(axis=1)
    for v in YN:
        d['e_' + v] = np.where(d[v] == 1, 1.0, np.where(d[v] == 2, 0.0, np.nan))
    d['e_ACEDIVRC'] = np.where(d['ACEDIVRC'] == 1, 1.0, np.where(d['ACEDIVRC'].isin([2, 8]), 0.0, np.nan))
    for v in FREQ:
        d['e_' + v] = np.where(d[v].isin([2, 3]), 1.0, np.where(d[v] == 1, 0.0, np.nan))
    sx = d[['e_ACETOUCH', 'e_ACETTHEM', 'e_ACEHVSEX']]
    d['e_SEXANY'] = np.where((sx == 1).any(axis=1), 1.0, np.where((sx == 0).all(axis=1), 0.0, np.nan))
    sb = d[['e_ACEDRINK', 'e_ACEDRUGS']]
    d['e_SUBST'] = np.where((sb == 1).any(axis=1), 1.0, np.where((sb == 0).all(axis=1), 0.0, np.nan))
    cats = ['e_ACEDEPRS', 'e_SUBST', 'e_ACEPRISN', 'e_ACEDIVRC', 'e_ACEPUNCH', 'e_ACEHURT', 'e_ACESWEAR', 'e_SEXANY']
    d['ace8'] = np.where(d['ace_complete'], d[cats].sum(axis=1), np.nan)
    d['ace7_noDEPRS'] = d['ace8'] - d['e_ACEDEPRS']
    return d


def harmonize(d, y):
    """Covariates and outcomes. Codes verified against the CDC codebooks (see RESULTS.md, Methods)."""
    d = d.copy()
    a = d['_AGEG5YR']
    d['agegrp'] = np.select([a == 1, a.isin([2, 3]), a.isin([4, 5]), a.isin([6, 7]), a.isin([8, 9]), a.between(10, 13)],
                            ['18-24', '25-34', '35-44', '45-54', '55-64', '65+'], 'Missing')
    sx = d['_SEX'] if '_SEX' in d.columns else d['SEX']
    d['sex'] = np.select([sx == 1, sx == 2], ['M', 'F'], 'Missing')
    e = d['_EDUCAG']
    d['educ'] = np.select([e == 1, e == 2, e == 3, e == 4], ['<HS', 'HS', 'SomeColl', 'CollGrad'], 'Missing')
    if '_INCOMG1' in d.columns:          # 2021+: 1..7 (5=50-<100k, 6=100-<200k, 7=200k+), 9 missing
        i = d['_INCOMG1'].where(~d['_INCOMG1'].isin([6, 7]), 5)
    else:                                # <=2020: 1..5 (5=50k+), 9 missing
        i = d['_INCOMG']
    d['income'] = np.select([i == 1, i == 2, i == 3, i == 4, i == 5], ['<15k', '15-25k', '25-35k', '35-50k', '50k+'], 'Missing')
    # outcomes
    dep = next((c for c in ('ADDEPEV3', 'ADDEPEV2', 'ADDEPEV') if c in d.columns), None)
    d['dep'] = np.where(d[dep] == 1, 1.0, np.where(d[dep] == 2, 0.0, np.nan)) if dep else np.nan
    m = d['MENTHLTH']
    d['mdays'] = np.where(m == 88, 0.0, np.where(m.between(1, 30), m, np.nan))
    if '_MENT14D' in d.columns:
        d['fmd'] = np.where(d['_MENT14D'] == 3, 1.0, np.where(d['_MENT14D'].isin([1, 2]), 0.0, np.nan))
    else:
        d['fmd'] = np.where(d['mdays'] >= 14, 1.0, np.where(d['mdays'].notna(), 0.0, np.nan))
    g = d['GENHLTH']
    d['fairpoor'] = np.where(g.isin([4, 5]), 1.0, np.where(g.isin([1, 2, 3]), 0.0, np.nan))
    def rec(col, yes, no):
        if col not in d.columns:
            return np.nan
        return np.where(d[col].isin(yes), 1.0, np.where(d[col].isin(no), 0.0, np.nan))
    d['anx'] = rec('ADANXEV', [1], [2])
    d['lsat_dis'] = rec('LSATISFY', [3, 4], [1, 2])
    d['emo_low'] = rec('EMTSUPRT', [4, 5], [1, 2, 3])
    d['lonely'] = rec('SDLONELY', [1, 2], [3, 4, 5])
    d['stress'] = rec('SDHSTRE1', [1, 2], [3, 4, 5])
    # K6 (MIS module): 1=All..5=None -> 4..0 ; complete 6 items ; SPD = K6>=13
    k6 = ['MISNERVS', 'MISHOPLS', 'MISRSTLS', 'MISDEPRD', 'MISEFFRT', 'MISWTLES']
    if all(c in d.columns for c in k6):
        sc = pd.DataFrame({c: np.where(d[c].between(1, 5), 5 - d[c], np.nan) for c in k6})
        d['k6'] = sc.sum(axis=1, min_count=6)
        d['spd'] = np.where(d['k6'] >= 13, 1.0, np.where(d['k6'].notna(), 0.0, np.nan))
    else:
        d['k6'] = d['spd'] = np.nan
    # PHQ-8 (AD module): days in last 2 weeks, 88=none ; points 0-1d=0, 2-6=1, 7-11=2, 12-14=3 ; current depression = PHQ8>=10
    p8 = ['ADPLEASR', 'ADDOWN', 'ADSLEEP', 'ADENERGY', 'ADEAT1', 'ADFAIL', 'ADTHINK', 'ADMOVE']
    if all(c in d.columns for c in p8):
        def pts(x):
            days = np.where(x == 88, 0, np.where(x.between(1, 14), x, np.nan))
            return np.select([days <= 1, days <= 6, days <= 11, days <= 14], [0, 1, 2, 3], np.nan)
        sc = pd.DataFrame({c: pts(d[c]) for c in p8})
        d['phq8'] = sc.sum(axis=1, min_count=8)
        d['phq10'] = np.where(d['phq8'] >= 10, 1.0, np.where(d['phq8'].notna(), 0.0, np.nan))
    else:
        d['phq8'] = d['phq10'] = np.nan
    # health-care access (sensitivity covariates)
    ins = next((c for c in ('_HLTHPL2', '_HLTHPL1', '_HLTHPLN', 'HLTHPLN1', 'HLTHPLAN') if c in d.columns), None)
    d['insured'] = np.select([d[ins] == 1, d[ins] == 2], ['Yes', 'No'], 'Missing') if ins else 'Missing'
    pd_ = next((c for c in ('PERSDOC3', 'PERSDOC2') if c in d.columns), None)
    d['persdoc'] = np.select([d[pd_].isin([1, 2]), d[pd_] == 3], ['Yes', 'No'], 'Missing') if pd_ else 'Missing'
    d = d.copy()
    d['spanish'] = (d['lang'] == 'Spanish').astype(float)
    d['cluster'] = d['year'].astype(str) + '_' + d['_STSTR'].astype('Int64').astype(str) + '_' + d['_PSU'].astype('Int64').astype(str)
    return d


def _mh(mhdir, tag):
    m = pd.read_csv(f'{mhdir}/extract_mh_{tag}.csv', low_memory=False)
    m['key'] = m['_STATE'].round().astype(int).astype(str) + '_' + m['SEQNO'].astype(str).str.replace(r'\.0$', '', regex=True)
    assert m.key.is_unique, tag
    return m.drop(columns=['_STATE', 'SEQNO', 'QSTLANG', 'QSTVER'])


def load(work, mhdir, y):
    """Returns (main_all, ace): main_all = every main-file respondent; ace = ACE-module respondents
    (main-file ACE respondents + version-file-only ACE respondents with their version weights).
    Mental-health columns come from the same file (main or Vk) as the row."""
    mainraw = pd.read_csv(f'{work}/{y}/extract_{y}.csv', low_memory=False)
    main = prep(mainraw, y, '_FINALWT' if y <= 2010 else '_LLCPWT', 'main')
    n0 = len(main)
    main = main.merge(_mh(mhdir, str(y)), on='key', how='left', validate='1:1')
    assert len(main) == n0
    mk = set(main.key[main.ace_any])
    adds = []
    for k in (1, 2, 3):
        p = f'{work}/{y}_V{k}/extract_{y}_V{k}.csv'
        if not os.path.exists(p):
            continue
        v = pd.read_csv(p, low_memory=False)
        wtc = next(c for c in (f'_LCPWTV{k}', f'_LNDWTV{k}') if c in v.columns)
        v = prep(v, y, wtc, f'V{k}')
        new = v[v.ace_any & ~v.key.isin(mk)].copy()
        mk |= set(new.key)
        new = new.merge(_mh(mhdir, f'{y}_V{k}'), on='key', how='left', validate='1:1')
        adds.append(new)
    main = harmonize(main, y)
    ace = pd.concat([main[main.ace_any]] + [harmonize(a, y) for a in adds], ignore_index=True)
    return main, ace
