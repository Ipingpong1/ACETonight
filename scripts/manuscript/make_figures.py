"""Publication figures for the H1 confirmatory analysis (static PNG 300 dpi + PDF + CSV of plotted numbers).
usage: python -I make_figures.py ANALYSIS_DIR FIGURE_DIR
Design (dataviz skill, emphasis form): de-emphasis grey for context, ONE accent hue for the three target items;
validated pair (#898781 / #2a78d6, CVD dE 15.9, normal 17.8, both >= 3:1 on white); thin marks, >= 8px markers with a
surface ring, solid hairline grid, legend for >= 2 series, selective direct labels, CIs as whiskers, finding-stating titles.
"""
import sys, os, json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import FixedLocator, NullLocator, FuncFormatter

AN, FIG = sys.argv[1], sys.argv[2]
WHICH = sys.argv[3] if len(sys.argv) > 3 else '1234'
os.makedirs(FIG, exist_ok=True)
SURF, INK, INK2, MUTED, GRID, AXIS = '#ffffff', '#0b0b0b', '#52514e', '#898781', '#e1e0d9', '#c3c2b7'
GREY, ACC = '#898781', '#2a78d6'
plt.rcParams.update({'font.family': 'sans-serif', 'font.sans-serif': ['DejaVu Sans', 'Liberation Sans', 'Arial'],
                     'font.size': 8.5, 'axes.edgecolor': AXIS, 'axes.linewidth': 0.6, 'axes.labelcolor': INK2,
                     'xtick.color': INK2, 'ytick.color': INK, 'xtick.major.width': 0.6, 'ytick.major.width': 0,
                     'axes.titlecolor': INK, 'figure.facecolor': SURF, 'axes.facecolor': SURF, 'savefig.facecolor': SURF,
                     'pdf.fonttype': 42, 'ps.fonttype': 42})
TARGETS = ['mh', 'drugs', 'jail']
ORDER = ['mh', 'drugs', 'jail', 'drink', 'divorce', 'ipv', 'phys', 'verbal']
LAB = {'mh': 'Household mental illness', 'drugs': 'Household drug use', 'jail': 'Household incarceration',
       'drink': 'Household problem drinking', 'divorce': 'Parental separation/divorce', 'ipv': 'Witnessed parental violence',
       'phys': 'Physical abuse', 'verbal': 'Verbal abuse', 'ace4': '4+ ACEs (8-category score)'}
LBOX = dict(facecolor=SURF, edgecolor='none', pad=0.8)   # label backing so grid/reference lines pass behind text
MS = 6.2          # marker size (pt) ~ 26 px at 300 dpi; >= 8 px on screen
RING = 1.1        # surface ring around filled markers


def style_ax(ax, xgrid=True):
    for s in ('top', 'right', 'left'):
        ax.spines[s].set_visible(False)
    ax.spines['bottom'].set_color(AXIS)
    if xgrid:
        ax.grid(axis='x', color=GRID, linewidth=0.5, linestyle='-')
    ax.set_axisbelow(True)
    ax.tick_params(axis='y', length=0, pad=4)
    ax.tick_params(axis='x', colors=INK2, labelsize=7.5)


def titles(fig, title, subtitle, y=0.985, panel_title=True):
    """Title + subtitle in a reserved band; moves the axes top below it (computed in points, so no overlap)."""
    import textwrap
    t = textwrap.fill(title, 84, break_on_hyphens=False); st = textwrap.fill(subtitle, 125, break_on_hyphens=False)
    H = fig.get_figheight() * 72.0
    fig.text(0.01, y, t, ha='left', va='top', fontsize=10, fontweight='bold', color=INK, linespacing=1.15)
    nl = t.count('\n') + 1; ns = st.count('\n') + 1
    ys = y - (nl * 10 * 1.2 + 5) / H
    fig.text(0.01, ys, st, ha='left', va='top', fontsize=7.5, color=INK2, linespacing=1.25)
    top = ys - (ns * 7.5 * 1.3 + (24 if panel_title else 8)) / H
    fig.subplots_adjust(top=top)
    return top


def save(fig, name, df):
    fig.savefig(os.path.join(FIG, name + '.png'), dpi=300, bbox_inches='tight', pad_inches=0.12)
    fig.savefig(os.path.join(FIG, name + '.pdf'), bbox_inches='tight', pad_inches=0.12)
    df.to_csv(os.path.join(FIG, name + '.csv'), index=False)
    plt.close(fig)


def or_axis(ax, lo=0.15, hi=2.5, ticks=(0.25, 0.5, 1, 2, 4)):
    ax.set_xscale('log')
    ax.set_xlim(lo, hi)
    ticks = [t for t in ticks if lo <= t <= hi]
    ax.xaxis.set_major_locator(FixedLocator(ticks))
    ax.xaxis.set_minor_locator(NullLocator())
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, p: f'{v:g}'))
    ax.axvline(1, color=INK2, linewidth=0.8, zorder=1)
    ax.axvline(np.exp(1.7 * -0.24), color=MUTED, linewidth=0.6, zorder=1)


# ------------------------------------------------------------------ Figure 1: prevalence by language
def fig1():
    t2 = pd.read_csv(os.path.join(AN, 'table2.csv'))
    rows = ORDER + ['ace4']
    recs = []
    for sv in ('BRFSS', 'CHIS'):
        for it in rows:
            r = t2[(t2.survey == sv) & (t2['item'] == it)].iloc[0]
            for lang in ('English', 'Spanish'):
                k = 'En' if lang == 'English' else 'Sp'
                recs.append(dict(panel=sv, item=it, item_label=LAB[it], interview_language=lang, target_item=it in TARGETS,
                                 prevalence_pct=r[f'{k}_pct'], ci_lo=r[f'{k}_lo'], ci_hi=r[f'{k}_hi']))
    f1 = pd.DataFrame(recs)
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 4.6), sharey=True)
    fig.subplots_adjust(left=0.235, right=0.985, top=0.765, bottom=0.16, wspace=0.08)
    ypos = {it: i for i, it in enumerate(rows)}
    ypos = {it: (len(rows) - 1 - i) - (0.5 if it == 'ace4' else 0) - (0.35 if it not in TARGETS and it != 'ace4' else 0) for i, it in enumerate(rows)}
    for ax, sv in zip(axes, ('BRFSS', 'CHIS')):
        style_ax(ax)
        d = f1[f1.panel == sv]
        for it in rows:
            c = ACC if it in TARGETS else GREY
            e = d[(d['item'] == it) & (d.interview_language == 'English')].iloc[0]
            s = d[(d['item'] == it) & (d.interview_language == 'Spanish')].iloc[0]
            y = ypos[it]
            ax.plot([s.prevalence_pct, e.prevalence_pct], [y, y], color=c, linewidth=1.0, alpha=0.45, zorder=2, solid_capstyle='round')
            for row, yy, filled in ((e, y + 0.17, False), (s, y - 0.17, True)):
                ax.errorbar(row.prevalence_pct, yy, xerr=[[row.prevalence_pct - row.ci_lo], [row.ci_hi - row.prevalence_pct]],
                            fmt='none', ecolor=c, elinewidth=1.0, capsize=0, zorder=3)
                ax.plot(row.prevalence_pct, yy, 'o', ms=MS, color=c, mfc=c if filled else SURF, mec=c if not filled else SURF,
                        mew=1.3 if not filled else RING, zorder=4)
            if it in TARGETS:   # selective direct label (target items): Spanish vs English, in the free space right of the pair
                ax.annotate(f'{s.prevalence_pct:.1f}% vs {e.prevalence_pct:.1f}%', (max(e.ci_hi, s.ci_hi), y), xytext=(7, 0),
                            textcoords='offset points', ha='left', va='center', fontsize=7, color=INK2, zorder=6, bbox=LBOX)
        ax.set_xlim(-1, 50)
        ax.set_xticks([0, 10, 20, 30, 40, 50])
        ax.set_title(f'{sv} {"2019-2025" if sv == "BRFSS" else "2021-2025"}', loc='left', fontsize=9, color=INK, fontweight='bold', pad=6)
        ax.set_xlabel('Weighted prevalence, % (95% CI)', fontsize=8)
    axes[0].set_yticks([ypos[i] for i in rows])
    axes[0].set_yticklabels([LAB[i] for i in rows], fontsize=8)
    for lbl, it in zip(axes[0].get_yticklabels(), rows):
        lbl.set_color(INK if it in TARGETS else INK2)
    tf = f1[f1.target_item]
    rat = {sv: (tf[(tf.panel == sv) & (tf.interview_language == 'English')].prevalence_pct.values /
                tf[(tf.panel == sv) & (tf.interview_language == 'Spanish')].prevalence_pct.values) for sv in ('BRFSS', 'CHIS')}
    allr = np.concatenate(list(rat.values()))
    titles(fig, 'Spanish-interview respondents report the three target household items about one-fifth to one-third as often as English-interview respondents',
           'Hispanic adults, weighted prevalence by interview language (95% CI). Blue = target items: household mental illness, drug use, incarceration. '
           'Labels: Spanish vs English.')
    leg = [Line2D([0], [0], marker='o', ls='', ms=MS, mfc=SURF, mec=INK2, mew=1.3, label='English interview'),
           Line2D([0], [0], marker='o', ls='', ms=MS, mfc=INK2, mec=SURF, mew=RING, label='Spanish interview'),
           Line2D([0], [0], marker='s', ls='', ms=MS, mfc=ACC, mec=ACC, label='Target item'),
           Line2D([0], [0], marker='s', ls='', ms=MS, mfc=GREY, mec=GREY, label='Other item')]
    fig.legend(handles=leg, loc='lower center', ncol=4, frameon=False, fontsize=7.5, bbox_to_anchor=(0.6, 0.0), labelcolor=INK2)
    save(fig, 'fig1_item_prevalence_by_language', f1)


# ------------------------------------------------------------------ Figure 2: DIF estimates, every item
def fig2():
    s1p = os.path.join(AN, 'secondary', 'effects_s1.csv')
    recs = []
    for panel in ('BRFSS', 'CHIS', 'CHIS + nativity'):
        for it in ORDER:
            if it in TARGETS:
                if panel == 'CHIS + nativity':
                    if not os.path.exists(s1p):
                        continue
                    r = pd.read_csv(s1p).query('lhs == @it').iloc[0]
                    b, lo, hi, src = r.est, r['ci.lower'], r['ci.upper'], 'S1 (target, replicate SE)'
                else:
                    r = pr[(pr.survey == panel) & (pr.lhs == it)].iloc[0]
                    b, lo, hi, src = r.est, r.ci_lo, r.ci_hi, 'Primary MIMIC (target, replicate SE)'
            else:
                q = s4[(s4.analysis == 'S4c one-at-a-time') & (s4.survey == panel) & (s4.lhs == it)]
                if not len(q):
                    continue
                r = q.iloc[0]
                b, lo, hi, src = r.est, r['ci.lower'], r['ci.upper'], 'S4c one-at-a-time (non-target, lavaan robust SE)'
            recs.append(dict(panel=panel, item=it, item_label=LAB[it], target_item=it in TARGETS, b_probit=b, b_lo=lo, b_hi=hi,
                             OR_equiv=np.exp(1.7 * b), OR_lo=np.exp(1.7 * lo), OR_hi=np.exp(1.7 * hi), source=src))
    f2 = pd.DataFrame(recs)
    panels = [p for p in ('BRFSS', 'CHIS', 'CHIS + nativity') if p in set(f2.panel)]
    fig, axes = plt.subplots(1, len(panels), figsize=(7.2, 4.9), sharey=True)
    fig.subplots_adjust(left=0.235, right=0.985, bottom=0.15, wspace=0.10)
    yp = {it: (len(ORDER) - 1 - i) - (0.5 if it not in TARGETS else 0) for i, it in enumerate(ORDER)}
    for ax, pn in zip(np.atleast_1d(axes), panels):
        style_ax(ax)
        or_axis(ax, 0.15, 5.0)
        d = f2[f2.panel == pn]
        for _, r in d.iterrows():
            c = ACC if r.target_item else GREY
            y = yp[r['item']]
            ax.errorbar(r.OR_equiv, y, xerr=[[r.OR_equiv - r.OR_lo], [r.OR_hi - r.OR_equiv]], fmt='none', ecolor=c, elinewidth=1.2, capsize=0, zorder=3)
            ax.plot(r.OR_equiv, y, 'o', ms=MS, color=c, mec=SURF, mew=RING, zorder=4)
            if r.target_item:
                ax.annotate(f'{r.OR_equiv:.2f}', (r.OR_hi, y), xytext=(4, 0), textcoords='offset points', ha='left', va='center', fontsize=7, color=INK2, zorder=6, bbox=LBOX)
        ax.set_title(pn, loc='left', fontsize=9, color=INK, fontweight='bold', pad=6)
    ax0 = np.atleast_1d(axes)[0]
    ytop = max(yp.values())
    for a in np.atleast_1d(axes):
        a.set_ylim(min(yp.values()) - 0.6, ytop + 1.0)
    ax0.text(np.exp(1.7 * -0.24) * 1.05, ytop + 0.62, 'OR 0.67 (b = \u22120.24)', ha='left', va='center', fontsize=6.5, color=MUTED, zorder=6,
                 bbox=dict(facecolor=SURF, edgecolor='none', pad=1.2))
    ax0.set_yticks([yp[i] for i in ORDER]); ax0.set_yticklabels([LAB[i] for i in ORDER], fontsize=8)
    for lbl, it in zip(ax0.get_yticklabels(), ORDER):
        lbl.set_color(INK if it in TARGETS else INK2)
    fig.supxlabel('DIF odds-ratio equivalent, exp(1.7b), 95% CI (log scale)', x=0.61, y=0.075, fontsize=7.5, color=INK2)
    tg = f2[f2.target_item & f2.panel.isin(['BRFSS', 'CHIS'])]
    titles(fig, f'The target items show negative DIF in both surveys (OR-equivalent {tg.OR_equiv.min():.2f}\u2013{tg.OR_equiv.max():.2f}), '
                f'but so does verbal abuse, and physical abuse is over-endorsed',
           'Uniform DIF by interview language (Spanish vs English), probit MIMIC with covariates; < 1 = less endorsed in Spanish at the same factor level. '
           'Non-target items: each freed one at a time (S4c), so their anchors differ from the primary model. CHIS + nativity: S1 covariates.')
    leg = [Line2D([0], [0], marker='o', ls='-', lw=1.2, ms=MS, color=ACC, mec=SURF, mew=RING, label='Target item, primary model (replicate CI)'),
           Line2D([0], [0], marker='o', ls='-', lw=1.2, ms=MS, color=GREY, mec=SURF, mew=RING, label='Other item, freed one at a time (robust CI)'),
           Line2D([0], [0], ls='-', lw=0.8, color=MUTED, label='Threshold OR 0.67 (b = \u22120.24)')]
    fig.legend(handles=leg, loc='lower center', ncol=3, frameon=False, fontsize=7, bbox_to_anchor=(0.5, 0.0), labelcolor=INK2, columnspacing=1.2)
    save(fig, 'fig2_dif_estimates_all_items', f2)


# ------------------------------------------------------------------ Figure 3: robustness of the target DIF estimates
def fig3():
    spec_rows = []
    def add(survey, spec, df, est='est', lo='ci.lower', hi='ci.upper', setype=''):
        for it in TARGETS:
            q = df[df.lhs == it] if 'lhs' in df.columns else df[df['item'] == it]
            if len(q):
                r = q.iloc[0]
                spec_rows.append(dict(survey=survey, specification=spec, item=it, item_label=LAB[it], b_probit=r[est], b_lo=r[lo], b_hi=r[hi],
                                      OR_equiv=np.exp(1.7 * r[est]), OR_lo=np.exp(1.7 * r[lo]), OR_hi=np.exp(1.7 * r[hi]), se_type=setype,
                                      primary=spec.startswith('Primary')))
    for sv in ('BRFSS', 'CHIS'):
        add(sv, 'Primary (2 factors)', pr[pr.survey == sv], 'est', 'ci_lo', 'ci_hi', 'replicate')
        if sv == 'CHIS':
            for k, lab in (('s1', 'S1 + nativity, % life in US'), ('s2', 'S2 foreign-born only')):
                p = os.path.join(AN, 'secondary', f'effects_{k}.csv')
                if os.path.exists(p):
                    add(sv, lab, pd.read_csv(p), setype='replicate')
        q = s4[(s4.survey == sv) & (s4.analysis == 'S4a one factor')]
        add(sv, 'S4a one factor', q, setype='lavaan robust')
        q = s4[(s4.survey == sv) & s4.analysis.str.startswith('S4b')]
        if len(q):
            add(sv, 'S4b purified anchors', q, setype='lavaan robust')
        if sv == 'CHIS':
            p = os.path.join(AN, 'secondary', 's6_mode.csv')
            if os.path.exists(p):
                m = pd.read_csv(p)
                add(sv, 'S6 phone interviews', m[m.term == 'Spanish direct effect, phone'], setype='lavaan robust')
                add(sv, 'S6 web interviews', m[m.term == 'Spanish direct effect, web'], setype='lavaan robust')
        if sv == 'BRFSS':
            p = os.path.join(AN, 'secondary', 's7_effects.csv')
            if os.path.exists(p):
                add(sv, 'S7 11 items, 3 factors', pd.read_csv(p), setype='lavaan robust')
    f3 = pd.DataFrame(spec_rows)
    specs = []
    for sv in ('BRFSS', 'CHIS'):
        for s in f3[f3.survey == sv].specification.unique():
            specs.append((sv, s))
    yy = {}
    y = 0
    for i, (sv, s) in enumerate(reversed(specs)):
        if i > 0 and reversed_prev != sv:
            y += 0.7
        yy[(sv, s)] = y; y += 1; reversed_prev = sv
    fig, axes = plt.subplots(1, 3, figsize=(7.2, 5.0), sharey=True)
    fig.subplots_adjust(left=0.27, right=0.985, bottom=0.14, wspace=0.10)
    for ax, it in zip(axes, TARGETS):
        style_ax(ax)
        or_axis(ax, 0.15, 2.0, ticks=(0.25, 0.5, 1, 2))
        d = f3[f3['item'] == it]
        for _, r in d.iterrows():
            c = ACC if r.primary else GREY
            yv = yy[(r.survey, r.specification)]
            ax.errorbar(r.OR_equiv, yv, xerr=[[r.OR_equiv - r.OR_lo], [r.OR_hi - r.OR_equiv]], fmt='none', ecolor=c, elinewidth=1.2, capsize=0, zorder=3)
            ax.plot(r.OR_equiv, yv, 'D' if r.primary else 'o', ms=MS if not r.primary else MS - 0.4, color=c, mec=SURF, mew=RING, zorder=4)
        ax.set_title({'mh': 'Mental illness', 'drugs': 'Drug use', 'jail': 'Incarceration'}[it], loc='left', fontsize=9, color=INK, fontweight='bold', pad=6)
    ytop3 = max(yy.values())
    for a in axes:
        a.set_ylim(min(yy.values()) - 0.6, ytop3 + 1.0)
    axes[0].text(np.exp(1.7 * -0.24) / 1.05, ytop3 + 0.62, 'OR 0.67 (b = \u22120.24)', ha='right', va='center', fontsize=6.5, color=MUTED, zorder=6,
                 bbox=dict(facecolor=SURF, edgecolor='none', pad=1.2))
    axes[0].set_yticks(list(yy.values())); axes[0].set_yticklabels([f'{sv}: {s}' for (sv, s) in yy.keys()], fontsize=7.5)
    for lbl, k in zip(axes[0].get_yticklabels(), yy.keys()):
        lbl.set_color(INK if k[1].startswith('Primary') else INK2)
    k = {it: (int((f3[f3['item'] == it].OR_hi < 1).sum()), int((f3['item'] == it).sum())) for it in TARGETS}
    titles(fig, f'Mental-illness DIF holds in {k["mh"][0]} of {k["mh"][1]} specifications; drug-use ({k["drugs"][0]}/{k["drugs"][1]}) and '
                f'incarceration ({k["jail"][0]}/{k["jail"][1]}) DIF depend on anchors (BRFSS) and nativity (CHIS)',
           'Direct effect of Spanish interview on each household target item (OR-equivalent, 95% CI, log scale) across the pre-specified specifications.')
    fig.supxlabel('OR-equivalent, exp(1.7b), 95% CI (log scale)', x=0.63, y=0.07, fontsize=7.5, color=INK2)
    leg = [Line2D([0], [0], marker='D', ls='-', lw=1.2, ms=MS - 0.4, color=ACC, mec=SURF, mew=RING, label='Primary (replicate CI)'),
           Line2D([0], [0], marker='o', ls='-', lw=1.2, ms=MS, color=GREY, mec=SURF, mew=RING, label='Secondary (S1, S2 replicate CI; others robust CI)'),
           Line2D([0], [0], ls='-', lw=0.8, color=MUTED, label='Threshold OR 0.67 (b = \u22120.24)')]
    fig.legend(handles=leg, loc='lower center', ncol=3, frameon=False, fontsize=7, bbox_to_anchor=(0.5, 0.0), labelcolor=INK2, columnspacing=1.2)
    save(fig, 'fig3_robustness_target_dif', f3)


# ------------------------------------------------------------------ Figure 4: impact
def fig4():
    recs = []
    for sv in ('brfss', 'chis'):
        p = os.path.join(AN, 'secondary', f's5_impact_{sv}.csv')
        if not os.path.exists(p):
            continue
        m = pd.read_csv(p).set_index('quantity')
        for metric, unit in (('mean', 'difference in mean 8-item count'), ('p4', 'difference in % with >= 4 of 8 items (pp)')):
            for scen, key in (('Observed', f'gap_{metric}_obs'), ('Model-implied, as estimated', f'gap_{metric}_model'),
                              ('Model-implied, target DIF removed', f'gap_{metric}_noDIF')):
                r = m.loc[key]
                recs.append(dict(survey=sv.upper(), metric=unit, scenario=scen, spanish_minus_english=r.estimate, ci_lo=r.ci_lo, ci_hi=r.ci_hi))
    f4 = pd.DataFrame(recs)
    if len(f4):
        fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.6))
        fig.subplots_adjust(left=0.10, right=0.985, top=0.72, bottom=0.21, wspace=0.30)
        sc_style = {'Observed': dict(c=GREY, filled=False), 'Model-implied, as estimated': dict(c=GREY, filled=True),
                    'Model-implied, target DIF removed': dict(c=ACC, filled=True)}
        for ax, (metric, xl) in zip(axes, (('difference in mean 8-item count', 'Spanish - English, mean count (95% CI)'),
                                            ('difference in % with >= 4 of 8 items (pp)', 'Spanish - English, percentage points (95% CI)'))):
            style_ax(ax)
            d = f4[f4.metric == metric]
            ylab = {}
            for j, sv in enumerate(('BRFSS', 'CHIS')):
                for k, scen in enumerate(sc_style):
                    q = d[(d.survey == sv) & (d.scenario == scen)]
                    if not len(q):
                        continue
                    r = q.iloc[0]; st = sc_style[scen]
                    yv = (1 - j) * 4 + (2 - k) * 0.9
                    ax.errorbar(r.spanish_minus_english, yv, xerr=[[r.spanish_minus_english - r.ci_lo], [r.ci_hi - r.spanish_minus_english]],
                                fmt='none', ecolor=st['c'], elinewidth=1.2, capsize=0, zorder=3)
                    ax.plot(r.spanish_minus_english, yv, 'o', ms=MS, color=st['c'], mfc=st['c'] if st['filled'] else SURF,
                            mec=SURF if st['filled'] else st['c'], mew=RING if st['filled'] else 1.3, zorder=4)
                    if scen != 'Observed':
                        ax.annotate(f'{r.spanish_minus_english:.2f}' if 'count' in metric else f'{r.spanish_minus_english:.1f}',
                                    (r.ci_lo, yv), xytext=(-4, 0), textcoords='offset points', ha='right', va='center', fontsize=6.5, color=INK2, zorder=6, bbox=LBOX)
                ylab[(1 - j) * 4 + 0.9] = sv
            ax.axvline(0, color=INK2, linewidth=0.8, zorder=1)
            ax.set_yticks(list(ylab.keys())); ax.set_yticklabels(list(ylab.values()), fontsize=8.5, fontweight='bold')
            ax.set_xlabel(xl, fontsize=7.5)
            ax.set_title('Mean 8-item ACE count' if 'count' in metric else '4+ of the 8 items', loc='left', fontsize=9, color=INK, fontweight='bold', pad=6)
            lo = min(d.ci_lo.min(), 0); ax.set_xlim(lo * 1.25, max(0.02, d.ci_hi.max()) + abs(lo) * 0.05)
        imp, imp4 = {}, {}
        for sv in ('BRFSS', 'CHIS'):
            p = os.path.join(AN, 'secondary', f's5_impact_{sv.lower()}.csv')
            m = pd.read_csv(p).set_index('quantity')
            imp[sv] = m.loc['pct_gap_mean_due_DIF', 'estimate']; imp4[sv] = m.loc['pct_gap_p4_due_DIF', 'estimate']
        titles(fig, f'Removing the target-item DIF would close {min(imp.values()):.0f}\u2013{max(imp.values()):.0f}% of the Spanish\u2013English gap in the 8-item ACE count '
                    f'and {min(imp4.values()):.0f}\u2013{max(imp4.values()):.0f}% of the gap in 4+ ACEs',
               'Spanish minus English interview, Hispanic adults. Model-implied values simulate the primary MIMIC with and without the three target direct effects.', y=0.985)
        leg = [Line2D([0], [0], marker='o', ls='', ms=MS, mfc=SURF, mec=GREY, mew=1.3, label='Observed'),
               Line2D([0], [0], marker='o', ls='', ms=MS, mfc=GREY, mec=SURF, mew=RING, label='Model-implied, as estimated'),
               Line2D([0], [0], marker='o', ls='', ms=MS, mfc=ACC, mec=SURF, mew=RING, label='Model-implied, target DIF removed')]
        fig.legend(handles=leg, loc='lower center', ncol=3, frameon=False, fontsize=7.5, bbox_to_anchor=(0.55, 0.0), labelcolor=INK2)
        save(fig, 'fig4_impact_gap', f4)


pr = pd.read_csv(os.path.join(AN, 'primary_results.csv')) if os.path.exists(os.path.join(AN, 'primary_results.csv')) else None
s4 = pd.read_csv(os.path.join(AN, 'secondary', 's4_effects.csv')) if os.path.exists(os.path.join(AN, 'secondary', 's4_effects.csv')) else None
for k in WHICH:
    globals()['fig' + k]()
print('figures written to', FIG)
