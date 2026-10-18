"""Finite checks of conditional synthesis by stochastic orthogonal copy mixing.

This implementation tests the reflection construction, not the reduced
single-output convolution circuit. The main theorem is qubit-based; selected
prime-dimensional examples test the supporting algebra as well.
"""
from collections import Counter
from itertools import combinations, product
import argparse
import json
from pathlib import Path
import numpy as np
from verify_converse import rref, stabilizer_orbit, save_results


def affine_solve(a,b,p):
    a,b = np.asarray(a,dtype=int),np.asarray(b,dtype=int)
    k = a.shape[1]
    z,piv = rref(np.column_stack([a,b]),p)
    if k in piv:
        return None
    free = [i for i in range(k) if i not in piv]
    c = np.zeros(k,dtype=int)
    basis = np.zeros((k,len(free)),dtype=int)
    for i,j in enumerate(piv):
        c[j] = z[i,-1]
        for h,f in enumerate(free):
            basis[j,h] = -z[i,f] % p
    for h,f in enumerate(free):
        basis[f,h] = 1
    assert np.array_equal(a @ c % p,b % p)
    assert not np.any(a @ basis % p)
    return c,basis


def binary_quadratic_root(c,basis):
    dim = basis.shape[1]
    def shifted(base,indices):
        return (base+basis[:,list(indices)].sum(axis=1)) % 2
    def good_q(v):
        return int(v.sum()) % 4 == 1
    first = c.copy() if good_q(c) else None
    if first is None:
        for size in (1,2):
            for inds in combinations(range(dim),size):
                cand = shifted(c,inds)
                if good_q(cand):
                    first = cand
                    break
            if first is not None:
                break
    if first is None:
        return None
    if not np.all(first == 1):
        return first
    for size in (1,2):
        for inds in combinations(range(dim),size):
            cand = shifted(first,inds)
            if good_q(cand):
                return cand
    if dim >= 3:
        cand = shifted(first,(0,1,2))
        assert good_q(cand)
        return cand
    return None


def find_binary_c(z):
    k = z.shape[0]
    a = np.vstack([z.T,np.ones(k,dtype=int)])
    b = np.r_[np.zeros(z.shape[1],dtype=int),1]
    sol = affine_solve(a,b,2)
    if sol is None:
        return None
    c = binary_quadratic_root(*sol)
    if c is not None:
        assert c.sum() % 4 == 1 and not np.all(c == 1)
        assert not np.any(c @ z % 2)
    return c


def allowed_cs(p,k):
    out = []
    for entry in product(range(p),repeat=k):
        c = np.array(entry,dtype=int)
        if np.all(c==1) or c.sum()%p != 1:
            continue
        if (p == 2 and c.sum()%4==1) or (p != 2 and c@c%p==1):
            out.append(c)
    return out


def synthesize(c,p):
    k = len(c)
    i = next(i for i in range(k) if c[i] != 1)
    e = np.zeros(k,dtype=int)
    e[i] = 1
    perm = np.eye(k,dtype=int)
    perm[[0,i]] = perm[[i,0]]
    if p == 2:
        v = (e+c) % 2
        assert v.sum()%4 == 2
        refl = (np.eye(k,dtype=int)+np.outer(v,v))%2
    else:
        u = (e-c)%p
        assert u.sum()%p == 0
        norm = int(u@u%p)
        assert norm != 0
        refl = (np.eye(k,dtype=int)-2*pow(norm,-1,p)*np.outer(u,u))%p
    o = (refl @ perm).T % p
    assert np.array_equal(o[0],c)
    assert np.array_equal(o.T @ o % p,np.eye(k,dtype=int))
    assert np.array_equal(o @ np.ones(k,dtype=int)%p,np.ones(k,dtype=int))
    if p == 2:
        assert all(o[:,j].sum()%4 == 1 for j in range(k))
    return o


def mix_copies(state,o,p,m):
    k = len(o)
    digits = np.indices((p,)*(k*m)).reshape(k*m,-1).T.reshape(-1,k,m)
    transformed = np.einsum('ij,ajm->aim',o,digits)%p
    powers = p**np.arange(k*m-1,-1,-1)
    perm = transformed.reshape(-1,k*m) @ powers
    result = np.empty_like(state)
    result[perm] = state
    return result


def tensor_vectors(vectors):
    result = np.ones(1,dtype=complex)
    for v in vectors:
        result = np.kron(result,v)
    return result


def exhaustive_binary_existence():
    k,r = 6,2
    candidates = allowed_cs(2,k)
    counts = Counter()
    for data in product(range(2),repeat=k*r):
        z = np.array(data,dtype=int).reshape(k,r)
        c = find_binary_c(z)
        brute = [v for v in candidates if not np.any(v @ z % 2)]
        assert (c is not None) == bool(brute)
        if c is None:
            counts['failure'] += 1
        else:
            synthesize(c,2)
            counts['success'] += 1
            counts['nontrivial_selected'] += int(c.sum()>1)
    return dict(k=k,r=r,matrices=2**(k*r),candidate_count=len(candidates),
                counts=dict(counts),failure=float(counts['failure']/2**(k*r)),
                second_moment_bound=2**r/len(candidates),all_checks_pass=True)


def physical_prediction_check(p,N,m,k):
    rng = np.random.default_rng(20261018+p+N+m+k)
    d,n = p**m,N-m
    states = stabilizer_orbit(p,N)
    candidates = None if p==2 else allowed_cs(p,k)
    counts = Counter()
    worst_error = 0.
    for state in states:
        blocks = state.reshape(p**n,d)
        probabilities = np.sum(abs(blocks)**2,axis=1)
        support = np.flatnonzero(probabilities>1e-9)
        assert np.max(abs(probabilities[support]-1/len(support)))<1e-8
        vals = rng.choice(support,size=k+1)
        x = np.array(np.unravel_index(vals,(p,)*n)).T if n else np.zeros((k+1,0),dtype=int)
        z = (x[:k]-x[k])%p
        c = find_binary_c(z) if p==2 else next((v for v in candidates if not np.any(v @ z % p)),None)
        r = round(np.log(len(support))/np.log(p))
        counts[f'rank_{r}_total'] += 1
        if c is None:
            counts[f'rank_{r}_failure'] += 1
            continue
        o = synthesize(c,p)
        training = [blocks[j]/np.linalg.norm(blocks[j]) for j in vals[:k]]
        target = blocks[vals[k]]/np.linalg.norm(blocks[vals[k]])
        transformed = mix_copies(tensor_vectors(training),o,p,m).reshape(d,-1)
        fidelity = np.linalg.norm(target.conj() @ transformed)**2
        worst_error = max(worst_error,abs(fidelity-1))
        assert abs(fidelity-1)<1e-9
        counts['certified_success'] += 1
        counts['nonpermutation_selected'] += int(np.count_nonzero(c)>1)
    return dict(p=p,N=N,m=m,k=k,states=len(states),counts=dict(counts),
                max_infidelity_on_success=worst_error,all_checks_pass=True)


def entangled_basis_covariance(p,k):
    m,d = 2,p**2
    w = np.exp(2j*np.pi/p)
    h = w**np.outer(np.arange(p),np.arange(p))/np.sqrt(p)
    s = np.diag([1,1j]) if p==2 else np.diag([w**((a*a*pow(2,-1,p))%p) for a in range(p)])
    cadd = np.zeros((d,d),dtype=complex)
    for a,b in product(range(p),repeat=2):
        cadd[a*p+(a+b)%p,a*p+b] = 1
    u = np.kron(h,s) @ cadd @ np.kron(s,h) @ cadd
    c = next(c for c in allowed_cs(p,k) if np.count_nonzero(c)>1)
    o = synthesize(c,p)
    labels = np.random.default_rng(19+p).integers(p,size=(k,m))
    newlabels = o @ labels % p
    vin = tensor_vectors([u[:,row[0]*p+row[1]] for row in labels])
    expected = tensor_vectors([u[:,row[0]*p+row[1]] for row in newlabels])
    actual = mix_copies(vin,o,p,m)
    error = np.max(abs(actual-expected))
    assert error<1e-10
    return dict(p=p,k=k,m=m,c=c.tolist(),max_statevector_error=float(error),all_checks_pass=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parent / "actual" / "synthesis.json",
        help="Generated JSON path (default: verification/actual/synthesis.json).",
    )
    args = parser.parse_args()
    results = {"binary_existence": exhaustive_binary_existence()}
    print(json.dumps(results), flush=True)
    results["physical"] = [
        physical_prediction_check(*q) for q in [(2,3,1,6),(3,2,1,4)]
    ]
    results["entangled_basis"] = [
        entangled_basis_covariance(*q) for q in [(2,6),(3,4)]
    ]
    print(
        json.dumps({key: value for key, value in results.items()
                    if key != "binary_existence"}),
        flush=True,
    )
    save_results(results, args.output)


if __name__ == "__main__":
    main()
