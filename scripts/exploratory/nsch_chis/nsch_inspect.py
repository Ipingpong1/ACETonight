"""Inspect NSCH topical Stata files: verify variable presence and value labels."""
import sys
import pandas as pd

VARS = ["HHID", "FIPSST", "STRATUM", "FWC", "YEAR", "SC_HISPANIC_R", "HHLANGUAGE", "SC_AGE_YEARS",
        "SC_SEX", "HIGRADE", "HIGRADE_TVIS", "FPL_I1", "HOUSE_GEN", "BORNUSA", "A1_BORN",
        "A1_RELATION", "A1_MENTHEALTH", "A2_MENTHEALTH", "A1_GRADE", "A1_SEX",
        "ACE1", "ACE3", "ACE4", "ACE5", "ACE6", "ACE7", "ACE8", "ACE9", "ACE10", "ACE11", "ACE12",
        "K2Q32A", "K2Q32B", "K2Q33A", "K2Q33B", "FORMTYPE", "INSGAP", "CURRCOV", "S4Q01",
        "K4Q01", "MEMORYCOND", "K2Q31A", "K2Q34A", "MPC_YN", "K4Q22_R", "TREATNEED", "K4Q23", "K4Q28X04", "K5Q31_R"]
for path in sys.argv[1:]:
    print("=" * 30, path)
    rdr = pd.io.stata.StataReader(path)
    with rdr:
        varlist = rdr.varlist if hasattr(rdr, "varlist") else None
        vlabels = rdr.variable_labels()
        vallabs = rdr.value_labels()
        lblist = rdr._lbllist if hasattr(rdr, "_lbllist") else None
    cols = [c.upper() for c in vlabels.keys()]
    orig = {c.upper(): c for c in vlabels.keys()}
    vlabels = {k.upper(): v for k, v in vlabels.items()}
    print("ncols", len(cols))
    lmap = dict(zip(cols, lblist)) if lblist is not None else {}
    df = pd.read_stata(path, convert_categoricals=False, columns=[orig[v] for v in VARS if v in cols])
    df.columns = [c.upper() for c in df.columns]
    print("nrows", len(df))
    for v in VARS:
        if v not in cols:
            print(f"  MISSING {v}")
            continue
        lab = vlabels.get(v, "")
        vl = vallabs.get(lmap.get(v, ""), {})
        s = df[v]
        if s.dtype == object or s.nunique() <= 12:
            vc = s.value_counts(dropna=False).sort_index()
            items = "; ".join(f"{k}={vl.get(k, '')!s:.25}:{n}" for k, n in vc.items())
            print(f"  {v} [{lab}] {items}")
        else:
            print(f"  {v} [{lab}] min={s.min()} max={s.max()} nmiss={s.isna().sum()} dtype={s.dtype}")
