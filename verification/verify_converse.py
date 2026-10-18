"""Finite algebra and state-ensemble checks for conditional stabilizer learning.

These checks verify explicit small cases; they do not replace the general proofs.
"""
from collections import Counter, deque
from fractions import Fraction
from itertools import combinations, product
import argparse
import json
from pathlib import Path
import numpy as np


if not __debug__:
    raise RuntimeError("Verification requires assertions; do not use python -O.")


def rref(a, p):
    a = np.array(a, dtype=np.int64, copy=True) % p
    r = 0
    pivots = []
    for c in range(a.shape[1]):
        rr = next((i for i in range(r, a.shape[0]) if a[i, c]), None)
        if rr is None:
            continue
        a[[r, rr]] = a[[rr, r]]
        a[r] = a[r] * pow(int(a[r, c]), -1, p) % p
        for i in range(a.shape[0]):
            if i != r and a[i, c]:
                a[i] = (a[i] - a[i, c] * a[r]) % p
        pivots.append(c)
        r += 1
        if r == a.shape[0]:
            break
    return a, pivots


def rank(a, p):
    return len(rref(a, p)[1])


def inverse(a, p):
    k = a.shape[0]
    z, piv = rref(np.concatenate([a, np.eye(k, dtype=int)], axis=1), p)
    assert piv[:k] == list(range(k))
    return z[:, k:]


def gram_audit(p, n, k):
    reps = {}
    good = 0
    good_fibers = set()
    for entries in product(range(p), repeat=n*k):
        x = np.array(entries, dtype=np.int64).reshape(k, n)
        g = x.T @ x % p
        ell = x.T @ np.ones(k, dtype=np.int64) % p
        key = tuple(g.flat) + (() if p == 2 else tuple(ell))
        is_good = rank(x, p) == k
        assert (rank(g, p) == k) == is_good
        if key not in reps:
            if is_good:
                piv = rref(x, p)[1]
                reps[key] = (True, x.copy(), piv, inverse(x[:, piv], p))
            else:
                reps[key] = (False,)
        assert reps[key][0] == is_good
        if is_good:
            good += 1
            good_fibers.add(key)
            _, x0, piv, inv = reps[key]
            o = x[:, piv] @ inv % p
            assert np.array_equal(o @ x0 % p, x)
            assert np.array_equal(o.T @ o % p, np.eye(k, dtype=int))
            assert np.array_equal(o @ np.ones(k, dtype=int) % p, np.ones(k, dtype=int))
            fx = np.column_stack([x, np.ones(k, dtype=int)])
            e = np.array([0]*n + [1], dtype=int)
            assert rank(np.vstack([fx, e]), p) == k+1
    total = p**(n*k)
    expected_good = Fraction(1)
    for j in range(k):
        expected_good *= 1 - Fraction(p**j, p**n)
    assert Fraction(good, total) == expected_good
    return dict(p=p,n=n,k=k,total=total,good=good,bad=total-good,
                bad_probability=float(1-expected_good),moment_fibers=len(reps),
                good_fibers=len(good_fibers),all_checks_pass=True)


def subspaces(p, dim, r):
    for piv in combinations(range(dim), r):
        free = [(i,j) for i in range(r) for j in range(dim)
                if j not in piv and j > piv[i]]
        for vals in product(range(p), repeat=len(free)):
            a = np.zeros((r,dim), dtype=int)
            for i,c in enumerate(piv):
                a[i,c] = 1
            for (i,j),v in zip(free, vals):
                a[i,j] = v
            yield a


def span(a,p):
    return frozenset(tuple(np.array(c,dtype=int) @ a % p)
                     for c in product(range(p), repeat=a.shape[0]))


def dimension_from_size(size,p):
    d = 0
    while size > 1:
        assert size % p == 0
        size //= p
        d += 1
    return d


def quotient_frame_audit(p,N,m):
    z = tuple([0]*(2*N))
    j = np.block([[np.zeros((N,N),dtype=int),np.eye(N,dtype=int)],
                  [-np.eye(N,dtype=int),np.zeros((N,N),dtype=int)]]) % p
    wb = np.zeros((N-m,2*N),dtype=int)
    for i in range(N-m):
        wb[i,N+i] = 1
    w = span(wb,p)
    lags = [span(a,p) for a in subspaces(p,2*N,N) if not np.any(a @ j @ a.T % p)]
    frames = [f for f in lags if w <= f]
    reports = [span(a,p) for a in subspaces(p,2*N,m)
               if not np.any(a @ j @ a.T % p)
               and not np.any(a @ j @ wb.T % p) and span(a,p)&w == {z}]
    hist = Counter()
    incidence = Counter()
    report_pairs = 0
    expected_degree = p**(m*(m+1)//2)
    for l in lags:
        t = l & w
        td = dimension_from_size(len(t),p)
        hist[td] += 1
        compatible = [f for f in frames if l&f == t]
        assert len(compatible) == expected_degree
        for f in compatible:
            incidence[(t,f)] += 1
        def coset(v):
            return min(tuple((np.array(v)+np.array(u)) % p) for u in t)
        ql, qw = {coset(v) for v in l},{coset(v) for v in w}
        qzero = coset(z)
        assert ql & qw == {qzero}
        for r in reports:
            qr = {coset(v) for v in r}
            assert len(qr) == p**m
            assert qr & qw == {qzero}
            assert (r <= l) == (qr <= ql)
            report_pairs += 1
    for (t,f),count in incidence.items():
        residual_N = N - dimension_from_size(len(t),p)
        assert count == p**(residual_N*(residual_N+1)//2)
    moment = sum(Fraction(count*p**t,len(lags)) for t,count in hist.items())
    expected = 1+Fraction(p**(N-m)-1,p**N+1)
    assert moment == expected
    return dict(p=p,N=N,m=m,lagrangians=len(lags),frames=len(frames),
                reports=len(reports),report_pairs_checked=report_pairs,
                intersection_histogram=dict(hist),moment=str(moment),
                degree=expected_degree,all_checks_pass=True)


def kron_all(ops):
    z = np.ones((1,1),dtype=complex)
    for a in ops:
        z = np.kron(z,a)
    return z


def stabilizer_orbit(p,N):
    D = p**N
    omega = np.exp(2j*np.pi/p)
    h = omega**np.outer(np.arange(p),np.arange(p))/np.sqrt(p)
    s = np.diag([1,1j]) if p == 2 else np.diag([omega**((x*x*pow(2,-1,p))%p) for x in range(p)])
    x = np.roll(np.eye(p),1,axis=0)
    gen = []
    for i in range(N):
        for single in (h,s,x):
            gen.append(kron_all([single if t==i else np.eye(p) for t in range(N)]))
    basis = list(product(range(p),repeat=N))
    lookup = {b:i for i,b in enumerate(basis)}
    for control in range(N):
        for target in range(N):
            if control == target:
                continue
            u = np.zeros((D,D),dtype=complex)
            for col,b in enumerate(basis):
                c = list(b)
                c[target] = (c[target]+c[control]) % p
                u[lookup[tuple(c)],col] = 1
            gen.append(u)
    def canon(v):
        v = v/np.linalg.norm(v)
        t = next(z for z in v if abs(z)>1e-8)
        v = v*np.conj(t)/abs(t)
        key = tuple(np.round(np.r_[v.real,v.imag],8))
        return key,v
    v = np.zeros(D,dtype=complex)
    v[0] = 1
    key,v = canon(v)
    states = {key:v}
    queue = deque([v])
    expected = D
    for i in range(1,N+1):
        expected *= p**i+1
    while queue:
        v = queue.popleft()
        for u in gen:
            key,w = canon(u @ v)
            if key not in states:
                states[key] = w
                queue.append(w)
                assert len(states) <= expected
    assert len(states) == expected
    return list(states.values())


def one_copy_channel_audit(p,N,m):
    states = stabilizer_orbit(p,N)
    D,d = p**N,p**m
    branches = D//d
    rx = np.zeros((D*d,D*d),dtype=complex)
    for v in states:
        rho = np.outer(v,v.conj())
        b = v[:d]
        conditional_unnormalized = np.outer(b,b.conj())
        rx += np.kron(rho.T,conditional_unnormalized)/len(states)
    vb = np.zeros(D*d,dtype=complex)
    for i in range(d):
        vb[i*d+i] = 1
    q = np.outer(vb,vb.conj())
    pb = np.diag([1]*d+[0]*(D-d))
    theoretical = (np.eye(D*d)+q)/(D*(D+1))
    primal = q+np.kron(np.eye(D)-pb,np.eye(d)/d)
    dual = (np.eye(D)+d*pb)/(D*(D+1))
    partial_trace = np.einsum('iaja->ij',primal.reshape(D,d,D,d))
    dual_slack = np.kron(dual,np.eye(d))-rx
    upper = branches*np.trace(dual).real
    lower = branches*np.trace(primal @ rx).real
    exact_quantum = 1/d+(d*d-1)/(d*(D+1))
    exact_report = (D/d+1)/(D+1)
    assert np.max(np.abs(rx-theoretical)) < 1e-10
    assert np.max(np.abs(partial_trace-np.eye(D))) < 1e-10
    assert np.linalg.eigvalsh(primal)[0] > -1e-10
    assert np.linalg.eigvalsh(dual_slack)[0] > -1e-10
    assert abs(upper-lower) < 1e-10
    assert abs(upper-exact_quantum) < 1e-10
    # A fixed output-Z report K, measured on the one training copy.
    report_score = 0.
    for v in states:
        probabilities = np.sum(np.abs(v.reshape(branches,d))**2,axis=0)
        report_score += probabilities @ probabilities/len(states)
    assert abs(report_score-exact_report) < 1e-10
    return dict(p=p,N=N,m=m,states=len(states),
                adaptive_quantum_optimum=exact_quantum,
                fixed_report_optimum=exact_report,
                ensemble_moment_error=float(np.max(np.abs(rx-theoretical))),
                SDP_primal_dual_gap=float(upper-lower),
                dual_slack_min_eigenvalue=float(np.linalg.eigvalsh(dual_slack)[0]),
                all_checks_pass=True)


def save_results(results, output):
    """Write generated JSON while protecting the checked-in expected baselines."""
    output = Path(output).expanduser().resolve()
    expected = (Path(__file__).resolve().parent / "expected").resolve()
    if output == expected or expected in output.parents:
        raise ValueError("Generated output must not be written inside expected/.")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(results, indent=2, allow_nan=False) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parent / "actual" / "converse.json",
        help="Generated JSON path (default: verification/actual/converse.json).",
    )
    args = parser.parse_args()
    results = {}
    results["gram"] = [gram_audit(*q) for q in [(2,4,4),(3,3,3),(5,2,2)]]
    print(json.dumps({"gram": results["gram"]}), flush=True)
    results["quotient_frames"] = [
        quotient_frame_audit(*q) for q in [(2,3,1),(2,3,2),(3,2,1)]
    ]
    print(json.dumps({"quotient_frames": results["quotient_frames"]}), flush=True)
    results["one_copy"] = [
        one_copy_channel_audit(*q) for q in [(2,2,1),(2,3,1),(2,3,2),(3,2,1)]
    ]
    print(json.dumps({"one_copy": results["one_copy"]}), flush=True)
    save_results(results, args.output)


if __name__ == "__main__":
    main()
