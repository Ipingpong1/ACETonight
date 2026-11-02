"""NSCH 2022-2024: Spanish- vs English-primary-language households among Hispanic children.

Crude weighted % and covariate-adjusted ORs (Spanish vs English household) for ACE items,
child depression/anxiety diagnoses, parent (Adult 1) mental health, and comparators.

Design: weighted logistic regression (FWC), Taylor-linearized sandwich SEs clustered on state
(FIPSST) = approximate design-based (strata ignored, state treated as PSU -> conservative).
FPL is multiply imputed in NSCH (FPL_I1..FPL_I6); adjusted models are fit on all 6
implicates and combined with Rubin's rules.

Usage: python -I nsch_analysis.py OUTDIR DTA2022 DTA2023 DTA2024
"""
import sys
import json
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats

ARGS = [a for a in sys.argv[1:] if not a.startswith("--")]
CONTRASTS_ONLY = "--contrasts-only" in sys.argv
OUTDIR = ARGS[0]
PATHS = ARGS[1:]

FPLS = [f"FPL_I{i}" for i in range(1, 7)]
KEEP = ["HHID", "FIPSST", "STRATUM", "FWC", "YEAR", "SC_HISPANIC_R", "HHLANGUAGE", "SC_AGE_YEARS",
        "SC_SEX", "HIGRADE_TVIS", "HOUSE_GEN", "A1_BORN", "A1_RELATION", "A1_MENTHEALTH",
        "A1_PHYSHEALTH", "ACE1", "ACE3", "ACE4", "ACE5", "ACE6", "ACE7", "ACE8", "ACE9", "ACE10",
        "ACE11", "K2Q32A", "K2Q32B", "K2Q33A", "K2Q33B", "K2Q31A", "K2Q34A", "K2Q40A", "K4Q22_R",
        "S4Q01", "K4Q01", "CURRCOV"] + FPLS


def load(path):
    rdr = pd.io.stata.StataReader(path)
    with rdr:
        cols = list(rdr.variable_labels().keys())
    orig = {c.upper(): c for c in cols}
    use = [orig[k] for k in KEEP if k in orig]
    missing = [k for k in KEEP if k not in orig]
    if missing:
        print(path, "MISSING", missing)
    d = pd.read_stata(path, convert_categoricals=False, columns=use)
    d.columns = [c.upper() for c in d.columns]
    return d


df = pd.concat([load(p) for p in PATHS], ignore_index=True)
df["YEAR"] = df["YEAR"].astype(int)
print("All children:", len(df), df.groupby("YEAR").size().to_dict())

hisp = df[df["SC_HISPANIC_R"] == 1].copy()
print("Hispanic children:", len(hisp))
lang_tab = hisp.groupby(["YEAR", "HHLANGUAGE"], dropna=False).agg(n=("FWC", "size"), w=("FWC", "sum")).reset_index()
d = hisp[hisp["HHLANGUAGE"].isin([1, 2])].copy()
d["spanish"] = (d["HHLANGUAGE"] == 2).astype(float)
d["w"] = d["FWC"] / d["FWC"].mean()


def yn(s):
    """1=Yes ->1, 2=No ->0, else NaN."""
    return s.map({1: 1.0, 2: 0.0})


# ---- outcomes ----
OUT = {}  # name -> (label, group, age_min)
for v, lab in [("ACE8", "ACE: lived with anyone mentally ill, suicidal, or severely depressed"),
               ("ACE9", "ACE: lived with anyone with alcohol/drug problem"),
               ("ACE6", "ACE: saw/heard adults hit each other in home"),
               ("ACE5", "ACE: parent/guardian served time in jail"),
               ("ACE3", "ACE: parent/guardian divorced/separated"),
               ("ACE4", "ACE: parent/guardian died"),
               ("ACE7", "ACE: victim/witness of neighborhood violence"),
               ("ACE10", "ACE: treated unfairly because of race/ethnicity"),
               ("ACE11", "ACE: treated unfairly because of health condition/disability")]:
    d[v + "_b"] = yn(d[v])
    OUT[v + "_b"] = (lab, "ACE", 0)
d["ACE1_b"] = d["ACE1"].map({1: 0.0, 2: 0.0, 3: 1.0, 4: 1.0})
OUT["ACE1_b"] = ("ACE: hard to cover basics on income somewhat/very often", "ACE", 0)

d["dep_ever"] = yn(d["K2Q32A"])
d["dep_curr"] = np.where(d["K2Q32A"] == 2, 0.0, np.where(d["K2Q32B"] == 1, 1.0, np.where(d["K2Q32B"] == 2, 0.0, np.nan)))
d["anx_ever"] = yn(d["K2Q33A"])
d["anx_curr"] = np.where(d["K2Q33A"] == 2, 0.0, np.where(d["K2Q33B"] == 1, 1.0, np.where(d["K2Q33B"] == 2, 0.0, np.nan)))
d["depanx_curr"] = np.where((d["dep_curr"] == 1) | (d["anx_curr"] == 1), 1.0,
                            np.where((d["dep_curr"] == 0) & (d["anx_curr"] == 0), 0.0, np.nan))
OUT["dep_ever"] = ("Child depression, ever told by provider (age 3-17)", "MH-dx", 3)
OUT["dep_curr"] = ("Child depression, current (age 3-17)", "MH-dx", 3)
OUT["anx_ever"] = ("Child anxiety problems, ever told by provider (age 3-17)", "MH-dx", 3)
OUT["anx_curr"] = ("Child anxiety problems, current (age 3-17)", "MH-dx", 3)
OUT["depanx_curr"] = ("Child current depression or anxiety (age 3-17)", "MH-dx", 3)
d["a1_mh_fp"] = d["A1_MENTHEALTH"].map({1: 0.0, 2: 0.0, 3: 0.0, 4: 1.0, 5: 1.0})
d["a1_mh_gfp"] = d["A1_MENTHEALTH"].map({1: 0.0, 2: 0.0, 3: 1.0, 4: 1.0, 5: 1.0})
d["a1_ph_fp"] = d["A1_PHYSHEALTH"].map({1: 0.0, 2: 0.0, 3: 0.0, 4: 1.0, 5: 1.0})
OUT["a1_mh_fp"] = ("Responding adult's own mental/emotional health fair/poor", "Parent-MH", 0)
OUT["a1_mh_gfp"] = ("Responding adult's own mental/emotional health good/fair/poor (not exc/VG)", "Parent-MH", 0)
OUT["a1_ph_fp"] = ("Comparator: responding adult's own physical health fair/poor", "Comparator", 0)
d["adhd"] = yn(d["K2Q31A"])
d["behav"] = yn(d["K2Q34A"])
d["asthma"] = yn(d["K2Q40A"])
d["mhtx"] = d["K4Q22_R"].map({1: 1.0, 2: 0.0, 3: 0.0})
d["mh_unmet"] = d["K4Q22_R"].map({1: 0.0, 2: 1.0, 3: 0.0})
d["anyvisit"] = yn(d["S4Q01"])
d["usualplace"] = yn(d["K4Q01"])
OUT["adhd"] = ("Comparator: ADHD ever told (age 3-17)", "Comparator", 3)
OUT["behav"] = ("Comparator: behavioral/conduct problems ever told (age 3-17)", "Comparator", 3)
OUT["asthma"] = ("Comparator: asthma ever told (age 0-17)", "Comparator", 0)
OUT["mhtx"] = ("Access: received MH professional treatment, past 12 mo (age 3-17)", "Access", 3)
OUT["mh_unmet"] = ("Access: needed but did not get MH care, past 12 mo (age 3-17)", "Access", 3)
OUT["anyvisit"] = ("Access: any health care visit, past 12 mo", "Access", 0)
OUT["usualplace"] = ("Access: has usual place for sick care", "Access", 0)

# ---- covariates ----
d["agecat"] = pd.cut(d["SC_AGE_YEARS"], [-1, 2, 5, 11, 17], labels=["0-2", "3-5", "6-11", "12-17"]).astype(str)
d["female"] = (d["SC_SEX"] == 2).astype(float)
d["educ"] = d["HIGRADE_TVIS"].astype(int)
d["gen"] = d["HOUSE_GEN"]  # 1=1st gen, 2=2nd gen, 3=3rd+, 4=other


def fplcat(s):
    return pd.cut(s, [0, 99, 199, 399, 1000], labels=["<100", "100-199", "200-399", "400+"]).astype(str)


def design(sub, fpl, covset):
    parts = [pd.Series(1.0, index=sub.index, name="const"), sub["spanish"]]
    if "age" in covset:
        parts.append(pd.get_dummies(sub["agecat"], prefix="age", drop_first=False).astype(float))
    if "sex" in covset:
        parts.append(sub["female"])
    if "year" in covset:
        parts.append(pd.get_dummies(sub["YEAR"], prefix="yr").astype(float))
    if "educ" in covset:
        parts.append(pd.get_dummies(sub["educ"], prefix="ed").astype(float))
    if "fpl" in covset:
        parts.append(pd.get_dummies(fplcat(sub[fpl]), prefix="fpl").astype(float))
    if "gen" in covset:
        parts.append(pd.get_dummies(sub["gen"].astype(int), prefix="gen").astype(float))
    X = pd.concat(parts, axis=1)
    # drop reference level of each dummy block + empty/constant columns
    drop = []
    for pre in ["age_", "yr_", "ed_", "fpl_", "gen_"]:
        cs = [c for c in X.columns if c.startswith(pre)]
        cs = [c for c in cs if X[c].sum() > 0]
        if cs:
            # reference: largest category for stability
            drop.append(max(cs, key=lambda c: X[c].sum()))
        drop += [c for c in X.columns if c.startswith(pre) and X[c].sum() == 0]
    return X.drop(columns=drop)


def fit_logit(y, X, w, cl):
    """Weighted logit; returns params, cluster-robust (linearization) covariance."""
    m = sm.GLM(y, X, family=sm.families.Binomial(), var_weights=w).fit()
    b = m.params.values
    Xv = X.values
    p = 1 / (1 + np.exp(-Xv @ b))
    H = (Xv * (w * p * (1 - p))[:, None]).T @ Xv
    Hinv = np.linalg.pinv(H)
    U = Xv * (w * (y - p))[:, None]
    Ug = pd.DataFrame(U).groupby(cl.values).sum().values
    G = Ug.shape[0]
    n, k = Xv.shape
    meat = Ug.T @ Ug * G / (G - 1)
    V = Hinv @ meat @ Hinv
    return pd.Series(b, index=X.columns), pd.DataFrame(V, index=X.columns, columns=X.columns)


COVSETS = {
    "crude": [],
    "M1": ["age", "sex", "year"],
    "M2": ["age", "sex", "year", "educ", "fpl"],
    "M3": ["age", "sex", "year", "educ", "fpl", "gen"],
}


def or_spanish(sub, yname, covset, cl_col="FIPSST"):
    sub = sub[sub[yname].notna()]
    if covset and "gen" in covset:
        sub = sub[sub["gen"].notna()]
    ests, vars_ = [], []
    imps = FPLS if "fpl" in covset else FPLS[:1]
    for fpl in imps:
        X = design(sub, fpl, covset)
        b, V = fit_logit(sub[yname].values, X, sub["w"].values, sub[cl_col])
        ests.append(b["spanish"])
        vars_.append(V.loc["spanish", "spanish"])
    m = len(ests)
    qbar = np.mean(ests)
    ubar = np.mean(vars_)
    bvar = np.var(ests, ddof=1) if m > 1 else 0.0
    T = ubar + (1 + 1 / m) * bvar
    se = np.sqrt(T)
    z = qbar / se
    return dict(logor=qbar, se=se, OR=np.exp(qbar), lo=np.exp(qbar - 1.96 * se), hi=np.exp(qbar + 1.96 * se),
                p=2 * stats.norm.sf(abs(z)), n=len(sub))


def wpct(sub, yname):
    s = sub[sub[yname].notna()]
    res = {}
    for lang, g in s.groupby("spanish"):
        res["sp" if lang == 1 else "en"] = (100 * np.average(g[yname], weights=g["w"]), len(g), int(g[yname].sum()))
    return res


rows = []
for yname, (lab, grp, amin) in ([] if CONTRASTS_ONLY else OUT.items()):
    sub = d[d["SC_AGE_YEARS"] >= amin]
    pc = wpct(sub, yname)
    r = dict(var=yname, label=lab, group=grp, pct_en=pc["en"][0], n_en=pc["en"][1], cases_en=pc["en"][2],
             pct_sp=pc["sp"][0], n_sp=pc["sp"][1], cases_sp=pc["sp"][2])
    r["ratio_sp_en"] = r["pct_sp"] / r["pct_en"]
    for mname, cs in COVSETS.items():
        o = or_spanish(sub, yname, cs)
        r.update({f"{mname}_OR": o["OR"], f"{mname}_lo": o["lo"], f"{mname}_hi": o["hi"], f"{mname}_p": o["p"],
                  f"{mname}_n": o["n"], f"{mname}_logor": o["logor"], f"{mname}_se": o["se"]})
    # sensitivity: immigrant (1st/2nd gen) households only, M2 covariates
    imm = sub[sub["gen"].isin([1, 2])]
    o = or_spanish(imm, yname, COVSETS["M2"])
    r.update({"IMM_OR": o["OR"], "IMM_lo": o["lo"], "IMM_hi": o["hi"], "IMM_n": o["n"]})
    # sensitivity: HC-type robust (cluster = household) for M3
    o = or_spanish(sub, yname, COVSETS["M3"], cl_col="HHID")
    r.update({"M3hh_lo": o["lo"], "M3hh_hi": o["hi"]})
    rows.append(r)
    print(f"{yname:12s} en={r['pct_en']:5.1f}% sp={r['pct_sp']:5.1f}% ratio={r['ratio_sp_en']:.2f} "
          f"cOR={r['crude_OR']:.2f} M3 OR={r['M3_OR']:.2f} ({r['M3_lo']:.2f}-{r['M3_hi']:.2f}) "
          f"IMM={r['IMM_OR']:.2f} ({r['IMM_lo']:.2f}-{r['IMM_hi']:.2f})", flush=True)

if not CONTRASTS_ONLY:
    res = pd.DataFrame(rows)
    res.to_csv(f"{OUTDIR}/nsch_results.csv", index=False)

# ---- item nonresponse by language (ACE + MH items) ----
nr = []
for v in ["ACE1", "ACE3", "ACE4", "ACE5", "ACE6", "ACE7", "ACE8", "ACE9", "ACE10", "ACE11", "K2Q32A", "K2Q33A", "A1_MENTHEALTH"]:
    for lang, g in d.groupby("spanish"):
        gg = g if not v.startswith("K2Q3") else g[g["SC_AGE_YEARS"] >= 3]
        nr.append(dict(var=v, lang="Spanish" if lang == 1 else "English",
                       pct_missing=100 * np.average(gg[v].isna(), weights=gg["w"]), n=len(gg)))
nr = pd.DataFrame(nr).pivot(index="var", columns="lang", values="pct_missing")
nr.to_csv(f"{OUTDIR}/nsch_item_nonresponse.csv")
print(nr.round(2))

# ---- covariate distribution by language ----
cov = {}
for lang, g in d.groupby("spanish"):
    k = "Spanish" if lang == 1 else "English"
    cov[k] = {
        "n": len(g),
        "wt_share_pct": 100 * g["FWC"].sum() / d["FWC"].sum(),
        "gen1_pct": 100 * np.average(g["gen"] == 1, weights=g["w"]),
        "gen2_pct": 100 * np.average(g["gen"] == 2, weights=g["w"]),
        "gen3_pct": 100 * np.average(g["gen"] == 3, weights=g["w"]),
        "gen_other_or_missing_pct": 100 * np.average(~g["gen"].isin([1, 2, 3]), weights=g["w"]),
        "educ_lt_hs_pct": 100 * np.average(g["educ"] == 1, weights=g["w"]),
        "fpl_lt100_pct": 100 * np.average(g["FPL_I1"] < 100, weights=g["w"]),
        "a1_born_outside_us_pct": 100 * np.average(g["A1_BORN"] == 2, weights=g["w"]),
        "uninsured_pct": 100 * np.average(g["CURRCOV"] == 2, weights=g["w"]),
        "mean_age": np.average(g["SC_AGE_YEARS"], weights=g["w"]),
    }
json.dump(dict(cov=cov, lang_tab=lang_tab.to_dict(orient="records")), open(f"{OUTDIR}/nsch_descriptives.json", "w"), indent=1, default=float)
print(json.dumps(cov, indent=1, default=float))
print(lang_tab)

# ---- contrasts: is the Spanish OR for ACE8 (or parent MH) different from other items? ----
# Memory-light joint sandwich: fit each item separately (M3), keep per-cluster influence values for
# the 'spanish' coefficient; cov(b_j, b_l) = G/(G-1) * sum_g IF_jg * IF_lg (cluster = FIPSST).
# Combine across the 6 FPL implicates with Rubin's rules.
def spanish_influence(sub, yname, fpl, covset, cl_col="FIPSST"):
    sub = sub[sub[yname].notna() & sub["gen"].notna()]
    X = design(sub, fpl, covset)
    y = sub[yname].values
    w = sub["w"].values
    m = sm.GLM(y, X, family=sm.families.Binomial(), var_weights=w).fit()
    b = m.params.values
    Xv = X.values
    p = 1 / (1 + np.exp(-Xv @ b))
    H = (Xv * (w * p * (1 - p))[:, None]).T @ Xv
    h = np.linalg.pinv(H)[list(X.columns).index("spanish"), :]
    infl = (Xv @ h) * w * (y - p)
    return b[list(X.columns).index("spanish")], pd.Series(infl).groupby(sub[cl_col].values).sum()


CONTRASTS = (
    [("ACE8_b", o) for o in ["ACE9_b", "ACE6_b", "ACE5_b", "ACE3_b", "ACE4_b", "ACE7_b", "ACE10_b", "ACE11_b", "ACE1_b"]]
    + [("ACE8_b", ("ACE9_b", "ACE6_b", "ACE5_b", "ACE3_b")),
       ("ACE8_b", ("ACE9_b", "ACE6_b", "ACE5_b", "ACE3_b", "ACE4_b", "ACE7_b", "ACE10_b", "ACE11_b", "ACE1_b")),
       ("a1_mh_fp", "a1_ph_fp"), ("anx_curr", "asthma"), ("anx_curr", "adhd"), ("depanx_curr", "asthma"),
       ("dep_ever", "asthma")]
)
needed = sorted({a for a, _ in CONTRASTS} | {x for _, o in CONTRASTS for x in ((o,) if isinstance(o, str) else o)})
cres = {i: [] for i in range(len(CONTRASTS))}
for fpl in FPLS:
    B, IF = {}, {}
    for yname in needed:
        amin = OUT[yname][2]
        sub = d[d["SC_AGE_YEARS"] >= amin]
        B[yname], IF[yname] = spanish_influence(sub, yname, fpl, COVSETS["M3"])
    IFdf = pd.DataFrame(IF).fillna(0.0)
    G = len(IFdf)
    S = IFdf.T @ IFdf * G / (G - 1)
    for i, (a, o) in enumerate(CONTRASTS):
        others = (o,) if isinstance(o, str) else o
        c = pd.Series(0.0, index=IFdf.columns)
        c[a] += 1.0
        for x in others:
            c[x] -= 1.0 / len(others)
        est = sum(c[k] * B[k] for k in c.index)
        var = float(c @ S @ c)
        cres[i].append((est, var))
crow = []
for i, (a, o) in enumerate(CONTRASTS):
    e = np.array([x[0] for x in cres[i]]); v = np.array([x[1] for x in cres[i]])
    m = len(e); T = v.mean() + (1 + 1 / m) * e.var(ddof=1)
    se = np.sqrt(T); q = e.mean()
    oname = o if isinstance(o, str) else ("mean of household ACE9/6/5/3" if len(o) == 4 else "mean of all 9 other ACE items")
    crow.append(dict(contrast=f"{a} vs {oname}", ratio_of_ORs=np.exp(q), lo=np.exp(q - 1.96 * se),
                     hi=np.exp(q + 1.96 * se), p=2 * stats.norm.sf(abs(q / se))))
crow = pd.DataFrame(crow)
crow.to_csv(f"{OUTDIR}/nsch_contrasts.csv", index=False)
print(crow.round(3).to_string())
