"""usage: python -I codes.py path.dta var1 var2 ... -> value labels + frequency"""
import sys, pandas as pd
p = sys.argv[1]; vs = sys.argv[2:]
with pd.io.stata.StataReader(p) as r:
    labs = r.value_labels(); r._ensure_open() if hasattr(r,'_ensure_open') else None
    m = dict(zip(r._varlist, r._lbllist))
df = pd.read_stata(p, columns=vs, convert_categoricals=False)
for v in vs:
    vc = df[v].value_counts(dropna=False).sort_index()
    L = labs.get(m.get(v), {})
    s = '; '.join(f'{k:g}={L.get(k, "")[:28]}:{n}' for k, n in vc.items()) if len(vc) < 40 else f'{len(vc)} values, min {df[v].min()} max {df[v].max()}'
    print(f'-- {v}: {s[:700]}')
