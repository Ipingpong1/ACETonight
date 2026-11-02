"""usage: python -I scan.py OUTCSV YEAR=path.dta ...  -> variable names+labels for each year"""
import sys, re, pandas as pd
out = sys.argv[1]; rows = []
for arg in sys.argv[2:]:
    y, p = arg.split('=', 1)
    with pd.io.stata.StataReader(p) as r:
        vl = r.variable_labels()
    for k, v in vl.items(): rows.append((y, k, v))
df = pd.DataFrame(rows, columns=['year', 'var', 'label']); df.to_csv(out, index=False)
print(df.groupby('year').size().to_string())
