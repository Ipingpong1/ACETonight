"""Rebuild 2019-2025 Hispanic ACE analytic file with sex/income/design vars for language DIF.
usage: python -I build_dif_data.py WORKDIR OUTCSV
prep()/load() logic copied from ace_brfss_scripts/analyze_ace_language.py (main file + version-file-only ACE respondents,
dedup on _STATE+SEQNO; version respondents keep _LCPWTVk). Extra columns kept: _SEX, income group, _STSTR, _PSU, SEQNO.
Codes (CDC codebooks): _SEX 1=Male 2=Female; _INCOMG (2019-20) 1:<15k 2:15-25k 3:25-35k 4:35-50k 5:50k+ 9:DK/Ref/miss;
_INCOMG1 (2021+) 1-4 same, 5:50-100k 6:100-200k 7:200k+ 9:miss -> harmonized to 1-5 (+9 missing).
_AGEG5YR 1-13 (14 = DK/Ref); EDUCA 1-6 (9 = Ref)."""
import sys, os
import numpy as np
import pandas as pd

work, outcsv = sys.argv[1], sys.argv[2]
YEARS = [2019, 2020, 2021, 2022, 2023, 2024, 2025]
TERR = {66, 72, 78}
YN = ['ACEDEPRS', 'ACEDRINK', 'ACEDRUGS', 'ACEPRISN']
FREQ = ['ACEPUNCH', 'ACEHURT', 'ACESWEAR', 'ACETOUCH', 'ACETTHEM', 'ACEHVSEX']
ITEMS = YN + ['ACEDIVRC'] + FREQ


def prep(d, y, wtcol, source):
    if 'ACEHURT1' in d.columns:
        d = d.rename(columns={'ACEHURT1': 'ACEHURT'})
    d['year'] = y
    d['wt'] = d[wtcol]
    d['wt_var'] = wtcol
    d['source'] = source
    d['key'] = d['_STATE'].round().astype(int).astype(str) + '_' + d['SEQNO'].astype(str).str.replace(r'\.0$', '', regex=True)
    q = d['QSTLANG']
    d['lang'] = np.select([q == 1, q == 2, (q >= 3) & (q <= 99)], ['English', 'Spanish', 'Other'], 'Missing')
    h = d['_HISPANC']
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
    inc = d['_INCOMG1'] if '_INCOMG1' in d.columns else d['_INCOMG']
    d['inc5'] = np.where(inc.isin([1, 2, 3, 4]), inc, np.where(inc.isin([5, 6, 7]), 5, 9))
    d['sex'] = d['_SEX']
    return d


def load(y):
    main = prep(pd.read_csv(f'{work}/{y}/extract_{y}.csv', low_memory=False), y, '_LLCPWT', 'main')
    mk = set(main.key[main.ace_any])
    adds = []
    for k in (1, 2, 3):
        p = f'{work}/{y}_V{k}/extract_{y}_V{k}.csv'
        if not os.path.exists(p):
            continue
        v = pd.read_csv(p, low_memory=False)
        wtc = next(c for c in (f'_LCPWTV{k}', f'_LNDWTV{k}') if c in v.columns)
        v = prep(v, y, wtc, f'V{k}')
        new = v[v.ace_any & ~v.key.isin(mk)]
        mk |= set(new.key)
        adds.append(new)
    return pd.concat([main[main.ace_any]] + adds, ignore_index=True)


keep = ['year', 'source', 'wt_var', 'key', 'SEQNO', '_STSTR', '_PSU', 'state', 'terr', 'lang', 'hisp', 'wt', 'ace_complete',
        '_AGEG5YR', 'EDUCA', 'sex', 'inc5', 'QSTVER'] + ITEMS + ['e_' + v for v in ITEMS]
frames = []
for y in YEARS:
    a = load(y)
    frames.append(a[keep])
    print(y, len(a), flush=True)
ace = pd.concat(frames, ignore_index=True)
ace.to_csv(outcsv.replace('.csv', '_allace.csv'), index=False)
an = ace[(ace.hisp == 'Hispanic') & ~ace.terr & ace.ace_complete & ace.lang.isin(['English', 'Spanish'])].copy()
an.to_csv(outcsv, index=False)
print(an.groupby(['year', 'lang']).size().unstack())
print(an.lang.value_counts())
