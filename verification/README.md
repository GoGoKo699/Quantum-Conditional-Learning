# Finite verification

These programs check explicit finite-field identities, small stabilizer ensembles, and a conditional synthesis construction. They complement the analytical proofs; finite examples do not establish the asymptotic copy-rate separation.

## Requirements and command

Use Python 3.10 or later with NumPy. No quantum simulator, symbolic algebra package, or SDP solver is required. The reference environment is Python 3.12.14 and NumPy 2.3.5.

From the repository root:

    python -m pip install numpy
    python verification/run_all.py

The runner executes both programs and exits with a nonzero status if an assertion, execution, or baseline comparison fails. Assertions must remain enabled: do not use Python's -O option or set PYTHONOPTIMIZE.

The programs may also be run individually:

    python verification/verify_converse.py
    python verification/verify_synthesis.py

Individual commands perform their internal assertions and write generated JSON; run_all.py additionally compares that JSON with the stored reference files.

## Results and baseline comparison

| File | Purpose |
| --- | --- |
| [expected/converse.json](expected/converse.json) | Stored output for the converse-related finite checks |
| [expected/synthesis.json](expected/synthesis.json) | Stored output for the synthesis checks |
| actual/converse.json | Fresh output produced by the converse program |
| actual/synthesis.json | Fresh output produced by the synthesis program |

The runner never refreshes the expected files. Both programs reject generated output paths inside expected/. Fresh results are kept in the ignored actual/ directory, which may be changed with:

    python verification/run_all.py --output-dir /tmp/conditional-learning-results

Object keys, list lengths and order, integers, Boolean flags, and exact fraction strings must match. Floating-point fields use absolute tolerance $`10^{-10}`$ and relative tolerance $`10^{-12}`$. The absolute tolerance accommodates tiny state-vector and eigensolver residuals near zero; stored residuals are of order $`10^{-15}`$ or smaller. Exact counts must still agree, and each program retains its original numerical assertions: $`10^{-10}`$ for the one-copy certificates and covariance checks, and $`10^{-9}`$ for conditional prediction fidelity. The comparison rejects nonfinite numerical output.

## What verify_converse.py checks

The output has three arrays: **gram** with 3 records, **quotient_frames** with 3 records, and **one_copy** with 4 records.

### Gram fibers

For each listed $`(p,n,k)`$, enumerate every $`k\times n`$ input matrix over $`\mathbb F_p`$:

| $`p,n,k`$ | Matrices | Full-row-rank matrices |
| --- | ---: | ---: |
| $`2,4,4`$ | 65,536 | 20,160 |
| $`3,3,3`$ | 19,683 | 11,232 |
| $`5,2,2`$ | 625 | 480 |

The checks cover the full-row-rank Gram criterion, orthogonal orbit reconstruction, preservation of the all-ones vector, the affine offset direction, and the exact rank-failure probability. For odd primes, fibers retain **both** $`X^\top X`$ and $`X^\top\mathbf1`$.

### Quotient and frame incidence

The cases $`(p,N,m)=(2,3,1),(2,3,2),(3,2,1)`$ exhaustively enumerate the relevant Lagrangians, frames, and admissible report subspaces. They check the incidence degree, quotient transversality, report injectivity, and equivalence of exact report validity before and after quotienting. The intersection moment is checked with rational arithmetic.

The stored output contains 135, 135, and 40 Lagrangians and respectively 1,620, 8,100, and 480 report-pair checks.

### One-copy physical ensembles

The cases $`(p,N,m)=(2,2,1),(2,3,1),(2,3,2),(3,2,1)`$ generate complete stabilizer orbits of sizes 60, 1,080, 1,080, and 360. They check the ensemble moment, an explicit channel's trace-preserving and positivity constraints, dual feasibility, and agreement of primal and dual values for the one-copy quantum prediction problem.

The field **fixed_report_optimum** stores the analytic reference value checked against a fixed output-Pauli report strategy. It is a different comparator from the unrestricted classical density descriptions issued after the query in the main theorem. This routine does not establish the asymptotic entanglement-breaking converse.

## What verify_synthesis.py checks

This module imports finite-field elimination, stabilizer-orbit generation, and the JSON writer from verify_converse.py; importing it does not run the converse cases.

The output contains one **binary_existence** object, a **physical** array with 2 records, and an **entangled_basis** array with 2 records.

### Exhaustive binary coefficient search

All 4,096 binary $`6\times2`$ centered outcome matrices are checked. The polynomial coefficient solver is compared with brute force over the same admissible coefficient set, and every returned coefficient is extended to a valid stochastic orthogonal transformation.

The baseline has 3,817 successes, 279 failures, and 450 nontrivial selected combinations. This implementation excludes the all-ones coefficient vector because it uses the reflection construction. The reduced convolution protocol in the analysis can also accept that vector.

### Physical conditional-state prediction

The cases $`(p,N,m,k)=(2,3,1,6)`$ and $`(3,2,1,4)`$ include every stabilizer state in their respective orbits. For **each state**, one tuple of supported training outcomes and a supported test outcome is sampled with a fixed seed. Whenever coefficient selection succeeds, the program applies the copy-mixing transformation to explicit tensor-product state vectors and checks the fidelity of the first output with the requested conditional state.

The baseline records 1,029 successful flagged cases among 1,080 qubit states and 325 among 360 qutrit states. It covers deterministic and nontrivial measurement supports. The state enumeration is exhaustive; the outcome tuples are sampled, not exhaustive.

### Entangled output-basis covariance

One fixed, entangled two-output basis is checked for each of $`(p,k)=(2,6)`$ and $`(3,4)`$, using a fixed label seed and a nonpermutation coefficient. The full transformed state vector is compared with the expected transformed-label product.

## Scope limits

The physical synthesis tests implement **stochastic orthogonal reflection mixing**. They do not numerically simulate the reduced Bu–Gu–Jaffe single-output CNOT convolution circuit or benchmark its gate count. The latter is justified analytically by the published covariance theorem and the Pauli-action calculation; see [related work](../references/RELATED_WORK.md).

The $`p=3`$ and $`p=5`$ cases test supporting finite-field statements beyond the qubit main theorem. They do not establish an all-prime classical-output separation. The programs do not test noise tolerance, hardware connectivity, optimal additive copy constants, general-query performance on every possible outcome tuple, or asymptotic error exponents.

The JSON output is deterministic for the fixed enumerations, seeds, and numerical environment. Small floating-point residuals can vary across numerical libraries; those variations are handled by the comparison tolerance rather than by modifying the baselines.
