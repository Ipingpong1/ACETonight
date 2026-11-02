"""CHIS adult PUF (2021-2024): Spanish- vs English-interview Hispanic adults.

READY-TO-RUN TEMPLATE. CHIS PUFs could not be downloaded without an account tonight, so the
variable names below are DEFAULTS TO VERIFY against the CHIS adult PUF data dictionary. The
script first scans variable labels by keyword and prints candidates; if a configured variable is
missing it stops and tells you which ones to map in a JSON config.

Usage (after downloading the Stata adult PUFs, each into its own folder):
  python -I chis_analysis.py OUTDIR 2021=/path/adult_2021.dta 2022=/path/adult_2022.dta ... [--config cfg.json] [--fast]
  --scan-only : only print keyword candidates (do this first)
  --fast      : HC/cluster-free robust SEs instead of jackknife replicate weights

Config JSON (all keys optional; overrides DEFAULTS), e.g.
  {"ace": {"ACE_mental": "XXXX", "ACE_alcohol": "YYYY"}, "lang": "INTVLNGC_P1",
   "lang_english": [1], "lang_spanish": [2], "yes_codes": [1], "no_codes": [2]}

Variance: CHIS supplies 80 jackknife replicate weights (RAKEDW1-RAKEDW80) with final weight
RAKEDW0; Stata equivalent: svyset [pw=rakedw0], jkrweight(rakedw1-rakedw80, multiplier(1))
vce(jackknife) mse  (VERIFY in the CHIS 'Using replicate weights' guide). When pooling Y years, the
weights are divided by Y and 80*Y replicates are formed (year-y replicate r uses RAKEDWr for year
y rows and the full-sample weight for other years).
"""
import sys
import re
import json
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats

DEFAULTS = {
    "weight": "RAKEDW0",
    "rep_prefix": "RAKEDW",
    "n_reps": 80,
    "lang": "INTVLNGC_P1",          # language of interview (user-specified; verify codes)
    "lang_english": [1],
    "lang_spanish": [2],
    "hisp": "SRH",                  # VERIFY: self-reported Hispanic (1=yes) -- or OMBSRR_P1==1
    "hisp_codes": [1],
    "age": "SRAGE_P1",              # VERIFY: self-reported age (top-coded in PUF)
    "sex": "SRSEX",                 # VERIFY
    "educ": "AHEDUC",               # VERIFY: educational attainment
    "nativity": "CITIZEN2",         # VERIFY: citizenship/immigration status (US-born / naturalized / non-citizen)
    "k6_spd30": "DSTRS30",          # VERIFY: likely serious psychological distress past month (K6>=13)
    "k6_score": "DISTRESS",         # VERIFY: K6 score past 30 days (used if k6_spd30 missing)
    "yes_codes": [1],
    "no_codes": [2],
    # ACE item names are NOT known from the public pages: fill from the dictionary
    # (search labels for 'MENTALLY ILL', 'ALCOHOL', 'PRISON', 'DIVORCE', 'HIT', 'SWEAR', 'SEXUAL').
    "ace": {},
    # optional additional mental-health items (e.g., ever told depression/anxiety, saw MH professional)
    "mh_extra": {},
}

KEYWORDS = {
    "interview language": r"LANGUAGE.*INTERVIEW|INTERVIEW.*LANG",
    "hispanic": r"HISPANIC|LATINO",
    "nativity": r"BORN IN|CITIZEN|IMMIGRA|YEARS IN U",
    "K6/distress": r"DISTRESS|K6|NERVOUS|HOPELESS|RESTLESS|WORTHLESS|EVERYTHING AN EFFORT|DEPRESSED",
    "ACE": r"ADVERSE|CHILDHOOD|MENTALLY ILL|SUICID|ALCOHOL.*DRUG|PRISON|JAIL|DIVORC|SEPARATED|HIT|BEAT|SWEAR|INSULT|SEXUAL|TOUCH|BEFORE AGE 18|GROWING UP",
    "dep/anx dx": r"DEPRESS|ANXIETY|MENTAL HEALTH|EMOTIONAL",
    "weights": r"WEIGHT|RAKED",
    "education": r"EDUCATION|GRADE|DEGREE",
}

args = [a for a in sys.argv[1:] if not a.startswith("--")]
flags = [a for a in sys.argv[1:] if a.startswith("--")]
cfg = dict(DEFAULTS)
if "--config" in sys.argv:
    cpath = sys.argv[sys.argv.index("--config") + 1]
    args = [a for a in args if a != cpath]
    cfg.update(json.load(open(cpath)))
OUTDIR = args[0]
files = dict(a.split("=", 1) for a in args[1:])

frames, labels = [], {}
for yr, path in files.items():
    rdr = pd.io.stata.StataReader(path)
    with rdr:
        vl = rdr.variable_labels()
    labels.update({k.upper(): v for k, v in vl.items()})
    d = pd.read_stata(path, convert_categoricals=False)
    d.columns = [c.upper() for c in d.columns]
    d["SVYYEAR"] = int(yr)
    frames.append(d)
    print(f"{yr}: {len(d)} rows, {d.shape[1]} cols")

print("\n=== keyword scan of variable labels ===")
for k, pat in KEYWORDS.items():
    hits = [f"{v}: {lab}" for v, lab in labels.items() if re.search(pat, str(lab).upper())]
    print(f"--- {k} ({len(hits)})")
    for h in hits[:40]:
        print("   ", h)
if "--scan-only" in flags:
    sys.exit(0)

df = pd.concat(frames, ignore_index=True, sort=False)
need = [cfg[k] for k in ["weight", "lang", "hisp", "age", "sex", "educ", "nativity"]] + list(cfg["ace"].values()) + list(cfg["mh_extra"].values())
k6var = cfg["k6_spd30"] if cfg["k6_spd30"] in df.columns else cfg["k6_score"]
need.append(k6var)
miss = [v for v in need if v not in df.columns]
if miss or not cfg["ace"]:
    print("\nMISSING variables (map them in --config JSON):", miss, "| ACE items configured:", len(cfg["ace"]))
    sys.exit(1)

Y = df["SVYYEAR"].nunique()
d = df[df[cfg["hisp"]].isin(cfg["hisp_codes"]) & df[cfg["lang"]].isin(cfg["lang_english"] + cfg["lang_spanish"])].copy()
d["spanish"] = d[cfg["lang"]].isin(cfg["lang_spanish"]).astype(float)
d["w0"] = d[cfg["weight"]] / Y
print("\nHispanic adults by year x interview language (unweighted n):")
print(d.groupby(["SVYYEAR", "spanish"]).size().unstack())


def yn(s):
    return pd.Series(np.where(s.isin(cfg["yes_codes"]), 1.0, np.where(s.isin(cfg["no_codes"]), 0.0, np.nan)), index=s.index)


OUT = {}
for name, v in cfg["ace"].items():
    d[name] = yn(d[v]); OUT[name] = f"ACE item {v}"
if k6var == cfg["k6_spd30"]:
    d["K6_SPD"] = yn(d[k6var]); OUT["K6_SPD"] = f"K6 serious psychological distress ({k6var})"
else:
    d["K6_SPD"] = np.where(d[k6var] >= 13, 1.0, np.where(d[k6var] >= 0, 0.0, np.nan)); OUT["K6_SPD"] = "K6 score >=13"
for name, v in cfg["mh_extra"].items():
    d[name] = yn(d[v]); OUT[name] = f"MH item {v}"

# covariates as categorical dummies (age is already grouped in the PUF; otherwise grouped here)
d["age_c"] = d[cfg["age"]]
if d["age_c"].nunique() > 20:
    d["age_c"] = pd.cut(d["age_c"], [17, 29, 44, 64, 200]).astype(str)
COVS = ["age_c", cfg["sex"], cfg["educ"], cfg["nativity"], "SVYYEAR"]
d = d[d[COVS].notna().all(axis=1) & (d[cfg["nativity"]] >= 0) & (d[cfg["educ"]] >= 0)]


def X_of(sub, covs):
    parts = [pd.Series(1.0, index=sub.index, name="const"), sub["spanish"]]
    for c in covs:
        dm = pd.get_dummies(sub[c].astype(str), prefix=c).astype(float)
        dm = dm.drop(columns=dm.sum().idxmax())
        parts.append(dm)
    return pd.concat(parts, axis=1)


def logit_b(y, X, w):
    return sm.GLM(y, X, family=sm.families.Binomial(), var_weights=w / w.mean()).fit().params


def rep_weights(sub):
    """Yield pooled-year replicate weight vectors."""
    for yr in sorted(sub["SVYYEAR"].unique()):
        isy = (sub["SVYYEAR"] == yr).values
        for r in range(1, cfg["n_reps"] + 1):
            col = f"{cfg['rep_prefix']}{r}"
            wr = sub["w0"].values.copy()
            wr[isy] = sub.loc[isy, col].values / Y
            yield wr


rows = []
use_jk = "--fast" not in flags and f"{cfg['rep_prefix']}1" in d.columns
for name, lab in OUT.items():
    sub = d[d[name].notna()]
    r = {"var": name, "label": lab}
    for lang, g in sub.groupby("spanish"):
        k = "sp" if lang == 1 else "en"
        r[f"pct_{k}"] = 100 * np.average(g[name], weights=g["w0"]); r[f"n_{k}"] = len(g)
    for mname, covs in [("crude", []), ("adj", COVS)]:
        X = X_of(sub, covs)
        b0 = logit_b(sub[name].values, X, sub["w0"].values)["spanish"]
        if use_jk:
            reps = np.array([logit_b(sub[name].values, X, wr)["spanish"] for wr in rep_weights(sub)])
            se = np.sqrt(np.sum((reps - b0) ** 2))  # multiplier 1, mse
        else:
            m = sm.GLM(sub[name].values, X, family=sm.families.Binomial(), var_weights=sub["w0"].values / sub["w0"].mean()).fit(cov_type="HC1")
            se = m.bse["spanish"]
        r.update({f"{mname}_OR": np.exp(b0), f"{mname}_lo": np.exp(b0 - 1.96 * se), f"{mname}_hi": np.exp(b0 + 1.96 * se),
                  f"{mname}_p": 2 * stats.norm.sf(abs(b0 / se))})
    rows.append(r)
    print(f"{name:14s} EN {r['pct_en']:5.1f}%  SP {r['pct_sp']:5.1f}%  crude OR {r['crude_OR']:.2f}  "
          f"adj OR {r['adj_OR']:.2f} ({r['adj_lo']:.2f}-{r['adj_hi']:.2f})", flush=True)
pd.DataFrame(rows).to_csv(f"{OUTDIR}/chis_results.csv", index=False)
print("SE method:", "jackknife replicate weights (mse, multiplier 1)" if use_jk else "HC1 robust (approximate)")
