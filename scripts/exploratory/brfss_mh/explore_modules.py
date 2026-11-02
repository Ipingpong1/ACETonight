"""Quick look: module coverage (K6, PHQ-8, anxiety dx, depression dx) by year among Hispanic respondents by language.
usage: python -I explore_modules.py WORK MHDIR SCRIPTDIR"""
import sys
work, mhdir, sdir = sys.argv[1:4]
sys.path.insert(0, sdir)
import mhcommon as mc
import pandas as pd
rows = []
for y in [2009, 2010, 2011, 2012]:
    main, ace = mc.load(work, mhdir, y)
    for nm, d in [('ACE resp', ace), ('All main', main)]:
        h = d[(d.hisp == 'Hispanic') & ~d.terr & d.lang.isin(['English', 'Spanish'])]
        for v in ['spd', 'phq10', 'anx', 'dep', 'fmd', 'e_ACEDEPRS', 'lsat_dis', 'emo_low']:
            ok = h[v].notna()
            if ok.sum() == 0: continue
            st = h[ok].groupby('state').size()
            rows.append({'year': y, 'sample': nm, 'var': v, 'n_Sp': int((ok & (h.lang == 'Spanish')).sum()),
                         'n_En': int((ok & (h.lang == 'English')).sum()), 'events_Sp': int(((h[v] == 1) & (h.lang == 'Spanish')).sum()),
                         'n_states': len(st), 'top_states_Sp': h[ok & (h.lang == 'Spanish')].groupby('state').size().nlargest(4).to_dict()})
with pd.option_context('display.width', 250, 'display.max_rows', 200, 'display.max_colwidth', 80):
    print(pd.DataFrame(rows).to_string(index=False))
