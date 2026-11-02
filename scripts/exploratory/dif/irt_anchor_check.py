"""Anchor-sensitivity check with a two-group unidimensional 2PL (uniform DIF only), marginal ML on weighted response patterns.
usage: python -I irt_anchor_check.py ANALYTIC_CSV OUTDIR
English: theta ~ N(0,1); Spanish: theta ~ N(mu, sigma^2). P(y_j=1) = expit(a_j*theta + c_j + delta_j*Spanish).
Slopes a_j common to both groups; delta_j = 0 for anchor items, free otherwise. exp(delta_j) = DIF odds ratio at equal theta.
Point estimates only (no SEs). Weights: final weight normalized to mean 1 within year."""
import sys, os
import numpy as np
import pandas as pd
from scipy.optimize import minimize
from numpy.polynomial.hermite_e import hermegauss

inp, out = sys.argv[1], sys.argv[2]
ITEMS = ['ACEDEPRS', 'ACEDRINK', 'ACEDRUGS', 'ACEPRISN', 'ACEDIVRC', 'ACEPUNCH', 'ACEHURT', 'ACESWEAR', 'ACETOUCH', 'ACETTHEM', 'ACEHVSEX']
J = len(ITEMS)
SCHEMES = {
    'All items invariant (no DIF)': ITEMS,
    'A1 purified (7 items)': ['ACEDRINK', 'ACEDIVRC', 'ACEPUNCH', 'ACEHURT', 'ACETOUCH', 'ACETTHEM', 'ACEHVSEX'],
    'A2 problem drinker only': ['ACEDRINK'],
    'A3 drink+divorce+3 sexual': ['ACEDRINK', 'ACEDIVRC', 'ACETOUCH', 'ACETTHEM', 'ACEHVSEX'],
    'A4 household (non-violent) 5': ['ACEDEPRS', 'ACEDRINK', 'ACEDRUGS', 'ACEPRISN', 'ACEDIVRC'],
    'X1 illustrative: smallest-gap (HURT+PUNCH)': ['ACEHURT', 'ACEPUNCH'],
    'X2 illustrative: largest-gap (SWEAR+DEPRS)': ['ACESWEAR', 'ACEDEPRS'],
}
d = pd.read_csv(inp)
d['w'] = d.wt / d.groupby('year').wt.transform('mean')
d['g'] = (d.lang == 'Spanish').astype(int)
pat = d.groupby(['g'] + ['e_' + k for k in ITEMS]).w.sum().reset_index()
G = pat.g.values
Y = pat[['e_' + k for k in ITEMS]].values
W = pat.w.values
x, v = hermegauss(41)
v = v / v.sum()


def unpack(par, free):
    a, c = par[:J], par[J:2 * J]
    dl = np.zeros(J)
    dl[free] = par[2 * J:2 * J + len(free)]
    mu, ls = par[-2], par[-1]
    return a, c, dl, mu, ls


def negll(par, free):
    a, c, dl, mu, ls = unpack(par, free)
    sg = np.exp(ls)
    ll, grad = 0.0, np.zeros_like(par)
    ga, gc, gd, gmu, gls = np.zeros(J), np.zeros(J), np.zeros(J), 0.0, 0.0
    for g in (0, 1):
        m = G == g
        th = x if g == 0 else mu + sg * x                          # Q
        eta = np.outer(a, th) + (c + g * dl)[:, None]              # J x Q
        p = 1 / (1 + np.exp(-eta))
        lp, lq = np.log(np.clip(p, 1e-300, None)), np.log(np.clip(1 - p, 1e-300, None))
        L = Y[m] @ lp + (1 - Y[m]) @ lq + np.log(v)[None, :]       # P x Q
        mx = L.max(axis=1, keepdims=True)
        post = np.exp(L - mx)
        tot = post.sum(axis=1, keepdims=True)
        ll += np.sum(W[m] * (np.log(tot[:, 0]) + mx[:, 0]))
        post = post / tot * W[m][:, None]                          # P x Q weighted posterior
        # dLL/deta_jq = sum_p post_pq (y_pj - p_jq)
        Geta = Y[m].T @ post - p * post.sum(axis=0)[None, :]       # J x Q
        ga += Geta @ th
        gc += Geta.sum(axis=1)
        if g == 1:
            gd += Geta.sum(axis=1)
            gmu += np.sum(a[:, None] * Geta)
            gls += np.sum(a[:, None] * Geta * (sg * x)[None, :])
    grad[:J], grad[J:2 * J], grad[2 * J:2 * J + len(free)] = ga, gc, gd[free]
    grad[-2], grad[-1] = gmu, gls
    return -ll, -grad


def fit(anchors):
    free = [j for j, k in enumerate(ITEMS) if k not in anchors]
    pE = Y[G == 0].T @ W[G == 0] / W[G == 0].sum()
    par0 = np.concatenate([np.full(J, 1.5), np.log(pE / (1 - pE)) - 0.5, np.zeros(len(free)), [0.0, 0.0]])
    r = minimize(negll, par0, args=(free,), jac=True, method='L-BFGS-B', options=dict(maxiter=5000, maxfun=20000, gtol=1e-6))
    a, c, dl, mu, ls = unpack(r.x, free)
    return dict(a=a, c=c, dl=dl, mu=mu, sigma=np.exp(ls), ll=-r.fun, conv=r.success, msg=str(r.message), nfree=len(free))


def ace8(E):
    ix = {k: i for i, k in enumerate(ITEMS)}
    e = lambda k: E[:, ix[k]]
    return (e('ACEDEPRS') + np.maximum(e('ACEDRINK'), e('ACEDRUGS')) + e('ACEPRISN') + e('ACEDIVRC') + e('ACEPUNCH') + e('ACEHURT')
            + e('ACESWEAR') + np.maximum.reduce([e('ACETOUCH'), e('ACETTHEM'), e('ACEHVSEX')]))


rng = np.random.default_rng(7)
Z = rng.standard_normal(200000)
U = rng.random((200000, J))
rows, items = [], []
for lab, anc in SCHEMES.items():
    f = fit(anc)
    th = f['mu'] + f['sigma'] * Z
    pS = 1 / (1 + np.exp(-(np.outer(th, f['a']) + f['c'] + f['dl'])))     # Spanish item functioning
    pE = 1 / (1 + np.exp(-(np.outer(th, f['a']) + f['c'])))               # English item functioning, same Spanish thetas
    thE = Z
    pEE = 1 / (1 + np.exp(-(np.outer(thE, f['a']) + f['c'])))
    cS, cE, cEE = (U < pS).astype(float), (U < pE).astype(float), (U < pEE).astype(float)
    rows.append(dict(scheme=lab, anchors='+'.join(k.replace('ACE', '') for k in anc), n_free_items=f['nfree'], converged=f['conv'],
                     loglik=f['ll'], mu_Spanish=f['mu'], sigma_Spanish=f['sigma'],
                     model_mean11_Sp=pS.sum(1).mean(), model_mean11_Sp_if_English_items=pE.sum(1).mean(), model_mean11_En=pEE.sum(1).mean(),
                     model_pct4p_Sp=100 * (ace8(cS) >= 4).mean(), model_pct4p_Sp_if_English_items=100 * (ace8(cE) >= 4).mean(),
                     model_pct4p_En=100 * (ace8(cEE) >= 4).mean()))
    for j, k in enumerate(ITEMS):
        items.append(dict(scheme=lab, item=k, anchor=k in anc, a=f['a'][j], c=f['c'][j], delta=f['dl'][j], OR=np.exp(f['dl'][j]),
                          pp_diff=100 * (pS[:, j] - pE[:, j]).mean()))
    print(lab, round(f['mu'], 3), round(f['sigma'], 3), f['conv'], flush=True)
pd.DataFrame(rows).to_csv(f'{out}/irt2pl_anchor_schemes.csv', index=False)
pd.DataFrame(items).to_csv(f'{out}/irt2pl_anchor_items.csv', index=False)
# observed (weighted) values for comparison
obs = {}
for g, nm in ((1, 'Sp'), (0, 'En')):
    m = d.g == g
    E = d.loc[m, ['e_' + k for k in ITEMS]].values
    obs[nm] = (np.average(E.sum(1), weights=d.w[m]), 100 * np.average(ace8(E) >= 4, weights=d.w[m]))
print('observed mean11/4+ Sp', obs['Sp'], 'En', obs['En'])
