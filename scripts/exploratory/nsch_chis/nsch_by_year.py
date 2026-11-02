"""Per-year crude weighted % (Spanish vs English households, Hispanic children) for key items."""
import sys
import numpy as np
import pandas as pd
rows = []
for path in sys.argv[1:]:
    r = pd.io.stata.StataReader(path)
    with r:
        cols = list(r.variable_labels().keys())
    orig = {c.upper(): c for c in cols}
    keep = ["YEAR", "SC_HISPANIC_R", "HHLANGUAGE", "FWC", "ACE8", "ACE9", "ACE6", "ACE5", "A1_MENTHEALTH", "A1_PHYSHEALTH"]
    d = pd.read_stata(path, convert_categoricals=False, columns=[orig[k] for k in keep])
    d.columns = [c.upper() for c in d.columns]
    d = d[(d.SC_HISPANIC_R == 1) & d.HHLANGUAGE.isin([1, 2])]
    for v in ["ACE8", "ACE9", "ACE6", "ACE5"]:
        d[v + "_b"] = d[v].map({1: 1.0, 2: 0.0})
    d["MH_fp"] = d.A1_MENTHEALTH.map({1: 0., 2: 0., 3: 0., 4: 1., 5: 1.})
    d["PH_fp"] = d.A1_PHYSHEALTH.map({1: 0., 2: 0., 3: 0., 4: 1., 5: 1.})
    for v in ["ACE8_b", "ACE9_b", "ACE6_b", "ACE5_b", "MH_fp", "PH_fp"]:
        for lang, g in d[d[v].notna()].groupby("HHLANGUAGE"):
            rows.append(dict(year=int(g.YEAR.iloc[0]), var=v, lang={1: "EN", 2: "SP"}[int(lang)],
                             pct=100 * np.average(g[v], weights=g.FWC)))
t = pd.DataFrame(rows).pivot_table(index=["var", "lang"], columns="year", values="pct").round(1)
print(t.to_string())
t.to_csv(sys.stdout if False else "/home/mo2273/ace_tonight/nsch_chis/nsch_by_year.csv")
