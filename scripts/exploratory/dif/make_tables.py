"""Build markdown tables for RESULTS.md from the DIF output CSVs.  usage: python -I make_tables.py OUTDIR"""
import sys
import numpy as np
import pandas as pd

o = sys.argv[1].rstrip('/') + '/'
ITEMS = ['ACEDEPRS', 'ACEDRINK', 'ACEDRUGS', 'ACEPRISN', 'ACEDIVRC', 'ACEPUNCH', 'ACEHURT', 'ACESWEAR', 'ACETOUCH', 'ACETTHEM', 'ACEHVSEX']
LAB = {'ACEDEPRS': 'HH mental illness', 'ACEDRINK': 'HH problem drinker', 'ACEDRUGS': 'HH drug use', 'ACEPRISN': 'HH incarceration',
       'ACEDIVRC': 'Parents sep./divorced', 'ACEPUNCH': 'Witnessed parental violence', 'ACEHURT': 'Physical abuse',
       'ACESWEAR': 'Verbal abuse', 'ACETOUCH': 'Sexual: touched', 'ACETTHEM': 'Sexual: made to touch', 'ACEHVSEX': 'Sexual: forced sex'}
d = pd.read_csv(o + 'dif_analytic_hisp_2019_2025.csv')
d['w'] = d.wt / d.groupby('year').wt.transform('mean')
r = pd.read_csv(o + 'dif_all_results.csv')
L = []


def ci(x, lo, hi):
    return f'{x:.2f} [{lo:.2f}, {hi:.2f}]'


def tab(df):
    s = '| ' + ' | '.join(df.columns) + ' |\n|' + '---|' * len(df.columns) + '\n'
    for _, row in df.iterrows():
        s += '| ' + ' | '.join(str(v) for v in row.values) + ' |\n'
    return s


# ---- main table ----
A0 = 'A0 all other items (unpurified)'
nc = r[(r.analysis == A0) & ~r['cov'] & r.weighted].set_index('item')
cv = r[(r.analysis == A0) & r['cov'] & r.weighted].set_index('item')
uw = r[(r.analysis == A0) & ~r['cov'] & ~r.weighted].set_index('item')
pu = r[(r.analysis == 'A1 purified') & ~r['cov'] & r.weighted].set_index('item')
rows = []
for k in ITEMS:
    sp, en = d.lang == 'Spanish', d.lang == 'English'
    ps, pe = np.average(d['e_' + k][sp], weights=d.w[sp]), np.average(d['e_' + k][en], weights=d.w[en])
    a, c, p = nc.loc[k], cv.loc[k], pu.loc[k]
    rows.append({'Item': f'{LAB[k]} ({k})', 'Sp %': f'{100 * ps:.1f}', 'En %': f'{100 * pe:.1f}', 'Crude OR': f'{ps / (1 - ps) / (pe / (1 - pe)):.2f}',
                 'Uniform-DIF OR [95% CI]': ci(a.OR, a.OR_lo, a.OR_hi), 'pp at matched score': f'{a.pp_diff:+.1f}',
                 'ΔR² unif (M1→M2)': f'{a.dR2_unif:.3f}', 'ΔR² non-unif (M2→M3)': f'{a.dR2_nonunif:.3f}', 'Δβ1': f'{100 * a.beta_chg:.0f}%',
                 'q unif / non-unif': f'{a.q_unif:.1g} / {a.q_nonunif:.1g}', 'JG (unif)': a.JG_unif.split(' ')[0],
                 'Flag': 'FLAG' if a.flag else '–',
                 'Cov-adj OR [95% CI]': ci(c.OR, c.OR_lo, c.OR_hi), 'Cov-adj ΔR²': f'{c.dR2_unif:.3f}', 'Cov flag': 'FLAG' if c.flag else '–',
                 'Unwtd OR': f'{uw.loc[k].OR:.2f}', 'Purified OR [95% CI]': ci(p.OR, p.OR_lo, p.OR_hi), 'Purified ΔR² (JG)': f'{p.dR2_unif:.3f} ({p.JG_unif.split(" ")[0]})',
                 'Purified flag': 'FLAG' if p.flag else '–'})
mt = pd.DataFrame(rows)
L.append('### MAIN\n' + tab(mt[['Item', 'Sp %', 'En %', 'Crude OR', 'Uniform-DIF OR [95% CI]', 'pp at matched score', 'ΔR² unif (M1→M2)',
                                'ΔR² non-unif (M2→M3)', 'Δβ1', 'q unif / non-unif', 'JG (unif)', 'Flag']]))
L.append('### MAIN-ROBUST\n' + tab(mt[['Item', 'Cov-adj OR [95% CI]', 'Cov-adj ΔR²', 'Cov flag', 'Unwtd OR', 'Purified OR [95% CI]', 'Purified ΔR² (JG)', 'Purified flag']]))

# ---- anchor sensitivity: 2PL ----
it = pd.read_csv(o + 'irt2pl_anchor_items.csv')
sc = pd.read_csv(o + 'irt2pl_anchor_schemes.csv')
order = ['A1 purified (7 items)', 'A2 problem drinker only', 'A3 drink+divorce+3 sexual', 'A4 household (non-violent) 5',
         'X1 illustrative: smallest-gap (HURT+PUNCH)', 'X2 illustrative: largest-gap (SWEAR+DEPRS)', 'All items invariant (no DIF)']
short = {'A1 purified (7 items)': 'A1 purified 7', 'A2 problem drinker only': 'A2 drinker only', 'A3 drink+divorce+3 sexual': 'A3 drink+div+sex',
         'A4 household (non-violent) 5': 'A4 household 5', 'X1 illustrative: smallest-gap (HURT+PUNCH)': 'X1 HURT+PUNCH',
         'X2 illustrative: largest-gap (SWEAR+DEPRS)': 'X2 SWEAR+DEPRS', 'All items invariant (no DIF)': 'No-DIF model'}
obs4, obsm = None, None
imp = pd.read_csv(o + 'impact.csv')
ob = imp.iloc[0]
rows = []
for k in ITEMS:
    row = {'Item': LAB[k]}
    for s in order[:-1]:
        x = it[(it.scheme == s) & (it.item == k)].iloc[0]
        row[short[s]] = '*anchor*' if x.anchor else (f'**{x.OR:.2f}**' if (x.OR < 0.67 or x.OR > 1.5) else f'{x.OR:.2f}')
    rows.append(row)
for lab, f in (('Spanish latent mean (En SD units)', lambda z: f'{z.mu_Spanish:.2f}'),
               ('DIF-corrected Sp mean count (obs 1.34; En 2.45)', lambda z: f'{ob.mean11_Sp + z.model_mean11_Sp_if_English_items - z.model_mean11_Sp:.2f}'),
               ('DIF-corrected Sp 4+ % (obs 10.7; En 25.5)', lambda z: f'{ob.pct4p_Sp + z.model_pct4p_Sp_if_English_items - z.model_pct4p_Sp:.1f}')):
    row = {'Item': f'*{lab}*'}
    for s in order[:-1]:
        row[short[s]] = f(sc[sc.scheme == s].iloc[0])
    rows.append(row)
L.append('### ANCHOR-2PL\n' + tab(pd.DataFrame(rows)))
L.append(f"No-DIF (all invariant) 2PL: Spanish latent mean {sc[sc.scheme == order[-1]].iloc[0].mu_Spanish:.2f}\n")
L.append('loglik by scheme: ' + '; '.join(f'{short[s]} {sc[sc.scheme == s].iloc[0].loglik:.0f} ({int(sc[sc.scheme == s].iloc[0].n_free_items)} free)' for s in order) + '\n')

# ---- anchor sensitivity: observed-score LR ----
lr_order = [A0, 'A1 purified', 'A2 problem drinker only', 'A3 drink+divorce+3 sexual', 'A4 household (non-violent) 5',
            'X1 illustrative: smallest-gap (HURT+PUNCH)', 'X2 illustrative: largest-gap (SWEAR+DEPRS)']
lshort = {A0: 'A0 all-other', 'A1 purified': 'A1 purified 7', 'A2 problem drinker only': 'A2 drinker only', 'A3 drink+divorce+3 sexual': 'A3 drink+div+sex',
          'A4 household (non-violent) 5': 'A4 household 5', 'X1 illustrative: smallest-gap (HURT+PUNCH)': 'X1 HURT+PUNCH', 'X2 illustrative: largest-gap (SWEAR+DEPRS)': 'X2 SWEAR+DEPRS'}
anch = {A0: [], 'A1 purified': ['ACEDRINK', 'ACEDIVRC', 'ACEPUNCH', 'ACEHURT', 'ACETOUCH', 'ACETTHEM', 'ACEHVSEX'], 'A2 problem drinker only': ['ACEDRINK'],
        'A3 drink+divorce+3 sexual': ['ACEDRINK', 'ACEDIVRC', 'ACETOUCH', 'ACETTHEM', 'ACEHVSEX'], 'A4 household (non-violent) 5': ['ACEDEPRS', 'ACEDRINK', 'ACEDRUGS', 'ACEPRISN', 'ACEDIVRC'],
        'X1 illustrative: smallest-gap (HURT+PUNCH)': ['ACEHURT', 'ACEPUNCH'], 'X2 illustrative: largest-gap (SWEAR+DEPRS)': ['ACESWEAR', 'ACEDEPRS']}
rows = []
for k in ITEMS:
    row = {'Item': LAB[k]}
    for s in lr_order:
        x = r[(r.analysis == s) & ~r['cov'] & r.weighted & (r.item == k)].iloc[0]
        if pd.isna(x.OR):
            row[lshort[s]] = 'n/a'
        else:
            row[lshort[s]] = (f'({x.OR:.2f})' if k in anch[s] else f'{x.OR:.2f}') + ('†' if x.flag else '')
    rows.append(row)
row = {'Item': '*DIF-corrected Sp 4+ % (LR, stochastic)*'}
for s in lr_order:
    z = imp[imp.scenario == f'DIF-corrected Spanish responses: {s}'].iloc[0]
    row[lshort[s]] = f'{z.pct4p_Sp:.1f}'
rows.append(row)
L.append('### ANCHOR-LR\n' + tab(pd.DataFrame(rows)))

# ---- impact ----
L.append('### IMPACT\n')
L.append(f"observed: Sp mean11 {ob.mean11_Sp:.2f} En {ob.mean11_En:.2f} gap {ob.gap_mean11:.2f}; mean8 {ob.mean8_Sp:.2f} vs {ob.mean8_En:.2f} gap {ob.gap_mean8:.2f}; "
         f"4+ {ob.pct4p_Sp:.1f} vs {ob.pct4p_En:.1f} gap {ob.gap_4p_pp:.1f} pp ratio {ob.ratio_4p:.2f}; SMD count11 {ob.smd_count11:.3f}\n")
for i in (1, 2):
    z = imp.iloc[i]
    L.append(f"{z.scenario}: crude {z.crude_gap:.3f} (SE {z.crude_se:.3f}); adjusted {z.adj_gap:.3f} (SE {z.adj_se:.3f})\n")
z = imp.iloc[3]
L.append(f"{z.scenario}: SMD {z.smd_count_reduced:.3f}; mean Sp {z.mean_red_Sp:.3f} En {z.mean_red_En:.3f}\n")
for i in range(4, len(imp)):
    z = imp.iloc[i]
    L.append(f"{z.scenario} [{z.items_changed}]: Sp mean11 {z.mean11_Sp:.2f} (gap {z.gap_mean11:.2f}); Sp 4+ {z.pct4p_Sp:.1f} (gap {z.gap_4p_pp:.1f}); mean8 {z.mean8_Sp:.2f}\n")

# ---- version split ----
vs = pd.read_csv(o + 'version_split.csv')
ix = pd.read_csv(o + 'version_2019_vs_2020_interaction.csv')
rows = []
for k in ITEMS:
    row = {'Item': LAB[k]}
    for s, sl in ((A0, 'all-other'), ('A1 purified', 'purified')):
        for p in ('2019', '2020', '2021-2025'):
            x = vs[(vs.analysis == s) & ~vs['cov'] & (vs.period == p) & (vs.item == k)].iloc[0]
            row[f'{sl} {p}'] = f'{x.OR:.2f}'
        y = ix[(ix.analysis == s) & ~ix['cov'] & (ix.item == k)].iloc[0]
        yc = ix[(ix.analysis == s) & ix['cov'] & (ix.item == k)].iloc[0]
        row[f'{sl}: 2020/2019 ratio (p); cov-adj'] = f'{y.ratio_OR_2020_vs_2019:.2f} ({y.p:.2f}); {yc.ratio_OR_2020_vs_2019:.2f} ({yc.p:.3f})'
    rows.append(row)
L.append('### VERSION\n' + tab(pd.DataFrame(rows)))
L.append('n: ' + '; '.join(f"{p}: Sp {g.n_sp.iloc[0]}, En {g.n_en.iloc[0]}" for p, g in vs.groupby('period')) + '\n')
x = vs[(vs.item == 'ACEPUNCH')][['analysis', 'cov', 'period', 'OR', 'OR_lo', 'OR_hi']]
L.append('ACEPUNCH detail:\n' + '\n'.join(f"{a.analysis} cov={a['cov']} {a.period}: {ci(a.OR, a.OR_lo, a.OR_hi)}" for _, a in x.iterrows()) + '\n')
open(o + 'tables_for_results.md', 'w').write('\n'.join(L))
print('\n'.join(L))
