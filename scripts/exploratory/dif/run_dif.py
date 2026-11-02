"""Logistic-regression DIF (Swaminathan & Rogers / lordif-style) of 11 BRFSS ACE items by interview language,
Hispanic respondents, 2019-2025, mainland, complete on 11 items.
usage: python -I run_dif.py ANALYTIC_CSV OUTDIR
M1: item ~ S (+cov);  M2: + spanish (uniform DIF);  M3: + spanish x S (non-uniform DIF).  S = matching score.
Weights: final weight normalized to mean 1 within survey year (pools main + version files of a year, which share a
population scale). SEs: cluster-robust sandwich, clusters = state x year (approximate; PSU is unique per respondent).
Nagelkerke R2 from weighted log-likelihoods (n = sum of normalized weights)."""
import sys, os
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.multitest import multipletests
from scipy import stats

inp, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
ITEMS = ['ACEDEPRS', 'ACEDRINK', 'ACEDRUGS', 'ACEPRISN', 'ACEDIVRC', 'ACEPUNCH', 'ACEHURT', 'ACESWEAR', 'ACETOUCH', 'ACETTHEM', 'ACEHVSEX']
LAB = {'ACEDEPRS': 'Household mental illness', 'ACEDRINK': 'Household problem drinker', 'ACEDRUGS': 'Household drug use',
       'ACEPRISN': 'Household incarceration', 'ACEDIVRC': 'Parents separated/divorced', 'ACEPUNCH': 'Witnessed parental violence',
       'ACEHURT': 'Physical abuse', 'ACESWEAR': 'Verbal abuse', 'ACETOUCH': 'Sexual: touched', 'ACETTHEM': 'Sexual: made to touch',
       'ACEHVSEX': 'Sexual: forced sex'}
ANCHORS = {
    'A0 all other items (unpurified)': None,          # None = all other items
    'A2 problem drinker only': ['ACEDRINK'],
    'A3 drink+divorce+3 sexual': ['ACEDRINK', 'ACEDIVRC', 'ACETOUCH', 'ACETTHEM', 'ACEHVSEX'],
    'A4 household (non-violent) 5': ['ACEDEPRS', 'ACEDRINK', 'ACEDRUGS', 'ACEPRISN', 'ACEDIVRC'],
    'X1 illustrative: smallest-gap (HURT+PUNCH)': ['ACEHURT', 'ACEPUNCH'],
    'X2 illustrative: largest-gap (SWEAR+DEPRS)': ['ACESWEAR', 'ACEDEPRS'],
}
D_R2, BETA_CHG, Q = 0.02, 0.10, 0.05

d0 = pd.read_csv(inp)
d0['sp'] = (d0.lang == 'Spanish').astype(float)


def prep(d, divrc='main', cov_vars=('_AGEG5YR', 'EDUCA', 'sex', 'inc5', 'year', 'st')):
    d = d.copy()
    if divrc == 'endorsed':
        d['e_ACEDIVRC'] = np.where(d.ACEDIVRC.isin([1, 8]), 1.0, 0.0)
    elif divrc == 'excluded':
        d = d[d.ACEDIVRC != 8].copy()
    d['w'] = d.wt / d.groupby('year').wt.transform('mean')
    d['clu'] = pd.factorize(d.state.astype(str) + '_' + d.year.astype(str))[0]
    stn = d.state.value_counts()
    d['st'] = np.where(d.state.map(stn) >= 150, d.state, 0)
    d = d.reset_index(drop=True)
    cv = d[list(cov_vars)].fillna(-1).astype(int).astype(str)
    cov = pd.get_dummies(cv, drop_first=True).astype(float).values
    return d, cov


def wll(y, p, w):
    p = np.clip(p, 1e-12, 1 - 1e-12)
    return float(np.sum(w * (y * np.log(p) + (1 - y) * np.log(1 - p))))


def fit(y, X, w, clu):
    m = sm.GLM(y, X, family=sm.families.Binomial(), var_weights=w).fit(tol=1e-10, maxiter=200)
    b = np.asarray(m.params)
    p = 1 / (1 + np.exp(-X @ b))
    H = X.T @ (X * (w * p * (1 - p))[:, None])
    Hi = np.linalg.pinv(H)
    sc = X * (w * (y - p))[:, None]
    G = clu.max() + 1
    S = np.zeros((G, X.shape[1]))
    np.add.at(S, clu, sc)
    N, K = X.shape
    V = Hi @ (S.T @ S) @ Hi * G / (G - 1) * (N - 1) / (N - K)
    return b, V, p, wll(y, p, w)


def r2n(ll, ll0, n):
    cs = 1 - np.exp(2 * (ll0 - ll) / n)
    return cs / (1 - np.exp(2 * ll0 / n))


def dif_item(d, cov, item, S, use_cov, weighted):
    y = d['e_' + item].values
    w = d.w.values if weighted else np.ones(len(d))
    clu = d.clu.values
    sp = d.sp.values
    n = w.sum()
    p0 = np.sum(w * y) / n
    ll0 = wll(y, np.full(len(y), p0), w)
    base = [np.ones(len(d)), S] + ([cov] if use_cov else [])
    X1 = np.column_stack(base)
    X2 = np.column_stack([X1, sp])
    X3 = np.column_stack([X2, sp * S])
    b1, V1, _, ll1 = fit(y, X1, w, clu)
    b2, V2, p2, ll2 = fit(y, X2, w, clu)
    b3, V3, _, ll3 = fit(y, X3, w, clu)
    bl, sel = b2[-1], np.sqrt(V2[-1, -1])
    bi, sei = b3[-1], np.sqrt(V3[-1, -1])
    # 2-df Wald (lordif-style M1 vs M3)
    bb, VV = b3[-2:], V3[-2:, -2:]
    w2 = float(bb @ np.linalg.pinv(VV) @ bb)
    eta_sp, eta_en = X2 @ b2 + (1 - sp) * bl, X2 @ b2 - sp * bl
    pS, pE = 1 / (1 + np.exp(-eta_sp)), 1 / (1 + np.exp(-eta_en))
    m = sp == 1
    R1, R2, R3 = r2n(ll1, ll0, n), r2n(ll2, ll0, n), r2n(ll3, ll0, n)
    return dict(item=item, n=len(d), b_S_M1=b1[1], b_S_M2=b2[1], beta_chg=abs(b2[1] - b1[1]) / abs(b1[1]),
                b_lang=bl, se_lang=sel, OR=np.exp(bl), OR_lo=np.exp(bl - 1.96 * sel), OR_hi=np.exp(bl + 1.96 * sel),
                p_unif=2 * stats.norm.sf(abs(bl / sel)), b_int=bi, se_int=sei, p_nonunif=2 * stats.norm.sf(abs(bi / sei)),
                p_2df=stats.chi2.sf(w2, 2), R2_M1=R1, R2_M2=R2, R2_M3=R3, dR2_unif=R2 - R1, dR2_nonunif=R3 - R2, dR2_2df=R3 - R1,
                pp_diff=100 * np.average(pS[m] - pE[m], weights=w[m])), (pS, pE)


def matching(d, item, anchors):
    a = [k for k in (ITEMS if anchors is None else anchors) if k != item]
    if not a:
        return None, a
    return d[['e_' + k for k in a]].sum(axis=1).values.astype(float), a


def jg(x):
    return 'A (negl.)' if x < 0.035 else ('B (moderate)' if x < 0.070 else 'C (large)')


def run(d, cov, anchors, use_cov=False, weighted=True, label=''):
    rows, preds = [], {}
    for it in ITEMS:
        S, a = matching(d, it, anchors)
        if S is None:
            rows.append(dict(item=it, anchor_items='(none)'))
            continue
        r, pr = dif_item(d, cov, it, S, use_cov, weighted)
        r['anchor_items'] = '+'.join(x.replace('ACE', '') for x in a)
        r['is_anchor'] = anchors is not None and it in anchors
        rows.append(r)
        preds[it] = pr
    res = pd.DataFrame(rows)
    ok = res.p_unif.notna()
    pv = np.concatenate([res.p_unif[ok].values, res.p_nonunif[ok].values])
    q = multipletests(pv, method='fdr_bh')[1]
    k = ok.sum()
    res.loc[ok, 'q_unif'], res.loc[ok, 'q_nonunif'] = q[:k], q[k:]
    res['flag_unif'] = (res.q_unif < Q) & ((res.dR2_unif >= D_R2) | (res.beta_chg >= BETA_CHG))
    res['flag_nonunif'] = (res.q_nonunif < Q) & (res.dR2_nonunif >= D_R2)
    res['flag'] = res.flag_unif | res.flag_nonunif
    res['JG_unif'] = [jg(x) if pd.notna(x) else '' for x in res.dR2_unif]
    res['JG_nonunif'] = [jg(x) if pd.notna(x) else '' for x in res.dR2_nonunif]
    res.insert(0, 'analysis', label)
    res['cov'], res['weighted'] = use_cov, weighted
    return res, preds


def purify(d, cov, use_cov=False, weighted=True, label=''):
    anchors, hist = list(ITEMS), []
    for it in range(1, 11):
        res, preds = run(d, cov, None if len(anchors) == len(ITEMS) else anchors, use_cov, weighted, f'{label} iter{it}')
        flagged = list(res.item[res.flag.fillna(False).astype(bool)])
        new = [k for k in ITEMS if k not in flagged]
        hist.append(dict(analysis=label, iteration=it, n_anchor=len(anchors), anchors='+'.join(a.replace('ACE', '') for a in anchors),
                         flagged='+'.join(f.replace('ACE', '') for f in flagged)))
        if new == anchors or len(new) < 2:
            break
        anchors = new
    return res, preds, anchors, pd.DataFrame(hist)


def ace8(E):
    """E: DataFrame of e_ columns -> 8-category ACE count."""
    return (E.e_ACEDEPRS + np.maximum(E.e_ACEDRINK, E.e_ACEDRUGS) + E.e_ACEPRISN + E.e_ACEDIVRC + E.e_ACEPUNCH + E.e_ACEHURT
            + E.e_ACESWEAR + np.maximum.reduce([E.e_ACETOUCH, E.e_ACETTHEM, E.e_ACEHVSEX]))


def wstats(d, E, w):
    c11 = E[['e_' + k for k in ITEMS]].sum(axis=1)
    c8 = ace8(E)
    out = {}
    for lg, m in (('Sp', d.sp == 1), ('En', d.sp == 0)):
        out[f'mean11_{lg}'] = np.average(c11[m], weights=w[m])
        out[f'mean8_{lg}'] = np.average(c8[m], weights=w[m])
        out[f'pct4p_{lg}'] = 100 * np.average(c8[m] >= 4, weights=w[m])
    out['gap_mean11'] = out['mean11_Sp'] - out['mean11_En']
    out['gap_mean8'] = out['mean8_Sp'] - out['mean8_En']
    out['gap_4p_pp'] = out['pct4p_Sp'] - out['pct4p_En']
    out['ratio_4p'] = out['pct4p_Sp'] / out['pct4p_En']
    return out


def smd(x, d, w):
    m1, m0 = d.sp == 1, d.sp == 0
    a, b = np.average(x[m1], weights=w[m1]), np.average(x[m0], weights=w[m0])
    v = np.average((x - np.average(x, weights=w)) ** 2, weights=w)
    return (a - b) / np.sqrt(v)


def corrected(d, preds, items_to_fix, w, M=50, seed=1):
    """Expected-score + stochastic correction: for each item to fix, Spanish responses are moved so E[y*|S] = P_English(S)."""
    rng = np.random.default_rng(seed)
    E0 = d[['e_' + k for k in ITEMS]].copy()
    m = (d.sp == 1).values
    exp_shift = sum(np.average((preds[k][1] - preds[k][0])[m], weights=w[m]) for k in items_to_fix) if items_to_fix else 0.0
    acc = []
    for _ in range(M):
        E = E0.copy()
        for k in items_to_fix:
            pS, pE = preds[k]
            y = E['e_' + k].values.copy()
            dlt = pE - pS
            u = rng.random(len(y))
            up = m & (y == 0) & (dlt > 0) & (u < dlt / np.clip(1 - pS, 1e-9, None))
            dn = m & (y == 1) & (dlt < 0) & (u < -dlt / np.clip(pS, 1e-9, None))
            y[up], y[dn] = 1.0, 0.0
            E['e_' + k] = y
        acc.append(wstats(d, E, w))
    r = pd.DataFrame(acc).mean().to_dict()
    r['expected_shift_mean11_Sp'] = exp_shift
    return r


if __name__ == '__main__':
    d, cov = prep(d0)
    w = d.w.values
    print('N', len(d), d.sp.sum(), flush=True)
    allres, hists = [], []

    # ---- 1. main analyses ----
    main_nc, preds_nc = run(d, cov, None, False, True, 'A0 all other items (unpurified)')
    main_cv, _ = run(d, cov, None, True, True, 'A0 all other items (unpurified)')
    main_uw, _ = run(d, cov, None, False, False, 'A0 all other items (unpurified)')
    allres += [main_nc, main_cv, main_uw]
    print(main_nc[['item', 'OR', 'OR_lo', 'OR_hi', 'dR2_unif', 'dR2_nonunif', 'beta_chg', 'q_unif', 'flag']].round(4).to_string(), flush=True)

    # ---- 2. purification + anchor sets ----
    pur_nc, preds_pur, anch_nc, h = purify(d, cov, False, True, 'Purified (no cov)')
    hists.append(h)
    pur_cv, preds_pur_cv, anch_cv, h = purify(d, cov, True, True, 'Purified (cov)')
    hists.append(h)
    pur_uw, _, anch_uw, h = purify(d, cov, False, False, 'Purified (no cov, unweighted)')
    hists.append(h)
    for r, lab in ((pur_nc, 'A1 purified'), (pur_cv, 'A1 purified'), (pur_uw, 'A1 purified')):
        r['analysis'] = lab
        allres.append(r)
    print('purified anchors', anch_nc, anch_cv, anch_uw, flush=True)
    scheme_preds = {'A0 all other items (unpurified)': (preds_nc, list(main_nc.item[main_nc.flag])),
                    'A1 purified': (preds_pur, [k for k in ITEMS if k not in anch_nc])}
    anchor_smd = {'A0 all other items (unpurified)': smd(d[['e_' + k for k in ITEMS]].sum(axis=1), d, w),
                  'A1 purified': smd(d[['e_' + k for k in anch_nc]].sum(axis=1), d, w)}
    for lab, a in ANCHORS.items():
        if a is None:
            continue
        r, pr = run(d, cov, a, False, True, lab)
        rc, _ = run(d, cov, a, True, True, lab)
        allres += [r, rc]
        scheme_preds[lab] = (pr, [k for k in ITEMS if k not in a])
        anchor_smd[lab] = smd(d[['e_' + k for k in a]].sum(axis=1), d, w)

    res = pd.concat(allres, ignore_index=True)
    res['label'] = res.item.map(LAB)
    res.to_csv(f'{out}/dif_all_results.csv', index=False)
    pd.concat(hists).to_csv(f'{out}/purification_history.csv', index=False)

    # ---- 3. impact ----
    imp = []
    obs = wstats(d, d[['e_' + k for k in ITEMS]], w)
    imp.append(dict(scenario='Observed (all 11 items)', items_changed='', smd_count11=smd(d[['e_' + k for k in ITEMS]].sum(axis=1), d, w), **obs))
    # adjusted observed gap (weighted linear / linear-probability with covariates, cluster SE)
    for nm, yv in (('count11', d[['e_' + k for k in ITEMS]].sum(axis=1).values), ('ace8_4plus', (ace8(d) >= 4).astype(float).values)):
        X = np.column_stack([np.ones(len(d)), d.sp.values, cov])
        mm = sm.WLS(yv, X, weights=w).fit(cov_type='cluster', cov_kwds={'groups': d.clu.values})
        Xu = np.column_stack([np.ones(len(d)), d.sp.values])
        mu = sm.WLS(yv, Xu, weights=w).fit(cov_type='cluster', cov_kwds={'groups': d.clu.values})
        imp.append(dict(scenario=f'Regression gap {nm}: crude vs covariate-adjusted (cluster SE)', items_changed='',
                        crude_gap=mu.params[1], crude_se=mu.bse[1], adj_gap=mm.params[1], adj_se=mm.bse[1]))
    # drop flagged (purified) items, standardized
    keep = anch_nc
    red = d[['e_' + k for k in keep]].sum(axis=1)
    imp.append(dict(scenario=f'Drop purified-flagged items: count on {len(keep)} anchor items', items_changed='+'.join(k for k in ITEMS if k not in keep),
                    smd_count_reduced=smd(red, d, w), mean_red_Sp=np.average(red[d.sp == 1], weights=w[d.sp == 1]),
                    mean_red_En=np.average(red[d.sp == 0], weights=w[d.sp == 0])))
    # corrected scores under each scheme
    for lab, (pr, fix) in scheme_preds.items():
        r = corrected(d, pr, fix, w)
        imp.append(dict(scenario=f'DIF-corrected Spanish responses: {lab}', items_changed='+'.join(k.replace('ACE', '') for k in fix),
                        anchor_smd=anchor_smd[lab], **r))
    pd.DataFrame(imp).to_csv(f'{out}/impact.csv', index=False)

    # sections 4 (version split) and 5 (ACEDIVRC code-8 sensitivity): see run_dif_part2.py
    print('done', flush=True)
