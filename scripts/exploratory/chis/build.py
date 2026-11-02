"""usage: python -I build.py OUT.csv YEAR=path.dta ... : pooled analytic extract (all adults; raw codes)"""
import sys, pandas as pd
out = sys.argv[1]
base = ['intvlngc_p1','intv_mode2','ombsrr_p1','ah33new','pctlf_p','spk_eng','ahedc_p1','srage_p1','srsex','latin2tp',
        'povll','aq1','aq2','aq3','aq4','aq5','aq6','aq7','aq8','ace8','ace_a','distress','dstrs30',
        'aj29','aj30','aj31','aj32','aj33','aj34','ab1','ins','citizen2','lnghm_p1'] + [f'rakedw{i}' for i in range(81)]
parts = []
for arg in sys.argv[2:]:
    y, p = arg.split('=', 1)
    d = pd.read_stata(p, columns=base, convert_categoricals=False)
    d['year'] = int(y); parts.append(d)
    print(y, len(d), 'spanish', int((d.intvlngc_p1 == 2).sum()), 'hisp', int((d.ombsrr_p1 == 1).sum()), flush=True)
pd.concat(parts, ignore_index=True).to_csv(out, index=False)
