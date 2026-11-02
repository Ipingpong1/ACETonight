"""Render markdown tables from NSCH outputs."""
import sys, json
import pandas as pd
od = sys.argv[1]
r = pd.read_csv(f"{od}/nsch_results.csv")
desc = json.load(open(f"{od}/nsch_descriptives.json"))
lt = pd.DataFrame(desc["lang_tab"])
lt["lang"] = lt["HHLANGUAGE"].map({1.0: "English", 2.0: "Spanish", 3.0: "Other"}).fillna("Missing")
n = lt.pivot_table(index="YEAR", columns="lang", values="n", aggfunc="sum")
w = lt.pivot_table(index="YEAR", columns="lang", values="w", aggfunc="sum")
print("| Year | Hispanic children (all) | English HH | Spanish HH | Other/missing (excluded) | Weighted % Spanish (of EN+SP) |")
print("|---|---|---|---|---|---|")
for y in n.index:
    tot = int(n.loc[y].sum())
    print(f"| {y} | {tot:,} | {int(n.loc[y,'English']):,} | {int(n.loc[y,'Spanish']):,} | {int(n.loc[y,'Other']+n.loc[y,'Missing'])} | {100*w.loc[y,'Spanish']/(w.loc[y,'Spanish']+w.loc[y,'English']):.1f}% |")
T = n.sum()
W = w.sum()
print(f"| **Pooled** | {int(T.sum()):,} | {int(T['English']):,} | {int(T['Spanish']):,} | {int(T['Other']+T['Missing'])} | {100*W['Spanish']/(W['Spanish']+W['English']):.1f}% |")
print()
c = desc["cov"]
print("| Weighted characteristic | English HH | Spanish HH |\n|---|---|---|")
for k, lab in [("gen1_pct", "1st-gen household (HOUSE_GEN=1)"), ("gen2_pct", "2nd-gen household"), ("gen3_pct", "3rd+-gen household"),
               ("a1_born_outside_us_pct", "Responding adult born outside US"), ("educ_lt_hs_pct", "Highest adult education < HS"),
               ("fpl_lt100_pct", "FPL < 100% (implicate 1)"), ("uninsured_pct", "Child currently uninsured")]:
    print(f"| {lab} | {c['English'][k]:.1f}% | {c['Spanish'][k]:.1f}% |")
print()
f = lambda x, m: f"{x[m+'_OR']:.2f} ({x[m+'_lo']:.2f}-{x[m+'_hi']:.2f})"
print("| Measure (NSCH variable) | English HH % (n) | Spanish HH % (n) | Ratio Sp/En | Crude OR | aOR M1 (age, sex, yr) | **aOR M3 (full)** | aOR, 1st/2nd-gen HH only |")
print("|---|---|---|---|---|---|---|---|")
for _, x in r.iterrows():
    print(f"| {x.label} ({x['var'].replace('_b','')}) | {x.pct_en:.1f} ({x.n_en:,}) | {x.pct_sp:.1f} ({x.n_sp:,}) | {x.ratio_sp_en:.2f} | {f(x,'crude')} | {f(x,'M1')} | **{f(x,'M3')}** | {x.IMM_OR:.2f} ({x.IMM_lo:.2f}-{x.IMM_hi:.2f}) |")
print()
cc = pd.read_csv(f"{od}/nsch_contrasts.csv")
print("| Contrast (M3) | Ratio of ORs | 95% CI | p |\n|---|---|---|---|")
for _, x in cc.iterrows():
    print(f"| {x.contrast.replace('_b','')} | {x.ratio_of_ORs:.2f} | {x.lo:.2f}-{x.hi:.2f} | {x.p:.3g} |")
print()
nr = pd.read_csv(f"{od}/nsch_item_nonresponse.csv")
print("| Item | % missing, English HH | % missing, Spanish HH |\n|---|---|---|")
for _, x in nr.iterrows():
    print(f"| {x['var']} | {x.English:.1f} | {x.Spanish:.1f} |")
