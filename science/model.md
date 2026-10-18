# Conditional state learning and its copy costs

Measuring part of an unknown quantum state produces a classical outcome and a remaining quantum state. A learner can try to supply that remaining state for an outcome observed on a fresh preparation. This task admits two different kinds of output channel: one can process retained quantum data into the prediction, or first reduce the data to a classical description from which the prediction is prepared.

For pure stabilizer sources, the first route has a copy cost controlled by the number of measured qubits. The second retains the leading copy cost of learning the whole source, even when both learners receive the outcome at the same time. This page defines the shared experiment and states the precise results.

## 1. Source, public measurement and held-out outcome

Let $`N`$ be the number of source qubits, let $`m`$ be the number of output qubits, and put $`n=N-m`$, with $`1\le m\le N`$. An unknown pure stabilizer state $`\rho=|\psi\rangle\langle\psi|`$ supplies independent identical training copies. A stabilizer state is a joint eigenstate of a maximal commuting subgroup of the qubit Pauli group. Its stabilizer description is not supplied to the learner.

The public measurement consists of $`n`$ independent commuting Hermitian Pauli observables. Its choice is fixed independently of the unknown source. A known Clifford unitary $`C_W`$ standardizes these observables to computational-basis measurements on a register $`A`$ of $`n`$ qubits, leaving a register $`B`$ of $`m`$ qubits. Known signs and invertible changes of the measured generators can be included in the classical outcome convention.

For $`x\in\mathbb F_2^n`$, define

```math
J_x=(\langle x|_A\otimes I_B)C_W,
\qquad
p_\rho(x)=\operatorname{Tr}(J_x\rho J_x^\dagger).
```

For supported outcomes, the conditional target is

```math
\rho_x=\frac{J_x\rho J_x^\dagger}{p_\rho(x)}.
```

It is a pure $`m`$-qubit stabilizer state. Unsupported outcomes have zero weight in every score below.

The learner receives $`k`$ training copies of $`\rho`$. An independent verifier preparation is measured by $`W`$, and the resulting classical $`x`$ is sent to the learner. The remaining verifier register is withheld from the learner. Thus the learner cannot simply return the target specimen that generated its query.

The learner may keep all its training copies until $`x`$ arrives. This timing is identical for the two output classes. The public measurement is not chosen adaptively in response to a learned description of the source.

## 2. Two output-channel classes

### Quantum output

For each outcome $`x`$, a quantum learner may apply any channel

```math
\Lambda_x:\mathcal L((\mathbb C^2)^{\otimes Nk})
\longrightarrow\mathcal L((\mathbb C^2)^{\otimes m}).
```

It may use classical randomness, ancillas, adaptive measurements and coherent operations. The lower bound places no computational-efficiency restriction on this class. The constructive upper bound is efficient.

### Classical description followed by preparation

The second class may also retain all training copies until $`x`$ and perform an arbitrary collective POVM. Its output is prepared using only the classical result of that measurement. Its channel has the form

```math
\Lambda_x(A)=\int\operatorname{Tr}[E_x(dy)A]\,\sigma_{x,y},
\qquad
\int E_x(dy)=I.
```

The matrices $`\sigma_{x,y}`$ may be arbitrary mixed density matrices. Classical record length, numerical precision, processing time and preparation complexity are unrestricted. A description of a preparation circuit is included, since it specifies an output density matrix. Such channels are called *measure-and-prepare* or *entanglement-breaking* channels; they are denoted by the subscript $`\mathrm{EB}`$.

The distinction is whether quantum information from the training system can remain in the prediction. The comparison does not restrict the second learner to single-copy measurements, stabilizer descriptions, early measurement of the training data, or a report made before the outcome.

## 3. Fidelity and the quantifiers in the bounds

For a fixed source and learner, the score is

```math
F_\rho(\Lambda)
=\sum_xp_\rho(x)
\operatorname{Tr}\!\left[\rho_x\Lambda_x(\rho^{\otimes k})\right].
```

Because the target is pure, this overlap is the usual squared-fidelity convention. The score includes all branches, including a learner's declared failures. An abstention is not counted as success.

Let $`\mathcal S_N`$ be the set of all pure $`N`$-qubit stabilizer states, with uniform prior. The optimal average fidelity in class $`\mathcal C`$ is

```math
F_{\mathcal C}^{\mathrm{av}}(N,m,k;W)
=\sup_{\Lambda\in\mathcal C}
\frac1{|\mathcal S_N|}\sum_{\rho\in\mathcal S_N}F_\rho(\Lambda).
```

The worst-case value replaces this uniform average by $`\inf_{\rho\in\mathcal S_N}F_\rho(\Lambda)`$ before the supremum. It is at most the average value. Therefore an upper bound on $`F_{\mathcal C}^{\mathrm{av}}`$ also obstructs a better worst-case guarantee. The constructive quantum learner works for every source and every supported query, which is stronger than an average-prior achievability statement.

Clifford standardization permutes the full stabilizer prior. The bounds depend on the rank of the public commuting measurement and not on a preferred physical Pauli basis.

## 4. Constructive quantum upper bound

**Theorem 1 — conditional synthesis.** For every pure stabilizer source, every supported query and $`0<\delta<1`$, a polynomial-time learner using

```math
k=n+\left\lceil\log_2\frac1\delta\right\rceil+3
```

training copies has a computable success flag with probability at least $`1-\delta`$. On every flagged success it outputs exactly $`\rho_x`$. Returning $`I/2^m`$ on failure gives

```math
F_\rho\ge1-(1-2^{-m})\delta.
```

When $`n=0`$, retaining one training copy already supplies the target exactly.

The learner measures the public input observables on each training copy and retains the conditional outputs. It solves one binary linear system and one quadratic Boolean equation to select a suitable subset. A known Clifford-covariant quantum convolution turns those outputs into the requested branch. The complete algorithm and proof are in [Conditional synthesis](synthesis.md).

The final mixing circuit on a selected subset of $`K\le k`$ blocks uses exactly $`2m(K-1)`$ CNOT gates and no additional mixing ancillas. Source preparation, public-measurement standardization, stored quantum systems and verification are separately accounted for in [Resources and interpretation](interpretation.md).

## 5. Quantum converse

**Theorem 2 — finite copy obstruction.** Every quantum-output learner obeys

```math
F_Q^{\mathrm{av}}(N,m,k;W)
\le\min\!\left\{1,\;2^{-m}+2^{k-n}\right\}.
```

The sharper form proved in [Quantum converse](quantum_converse.md) retains the factor

```math
(1-2^{-m})\left(1+\frac{2^n-1}{2^N+1}\right)
```

in front of $`2^{k-n}`$. The uniform prior includes stabilizers whose deterministic measurement constraints intersect the public measurement; these states are handled by a quotient and incidence argument.

In particular, a worst-case fidelity guarantee at least $`1-\delta>2^{-m}`$ requires

```math
k\ge n+\log_2(1-\delta-2^{-m}).
```

For fixed error this matches the leading $`n`$ term of Theorem 1. It does not establish optimal additive constants or the optimal dependence of the overhead on $`\delta`$.

## 6. Converse for arbitrary classical density descriptions

**Theorem 3 — classical-output copy rate.** Fix $`\beta_0>0`$ and $`\varepsilon>0`$. Uniformly over sequences satisfying

```math
m\ge\beta_0N,
\qquad
k\le(1-\varepsilon)N,
```

one has

```math
F_{\mathrm{EB}}^{\mathrm{av}}(N,m,k;W)\longrightarrow0.
```

The outcome is already known when the classical learner chooses its arbitrary collective measurement and density description. The proof does not transfer the timing restriction of an earlier complementary-stabilizer reporting problem.

The [classical converse](classical_converse.md) averages the input graph, input signs and cross couplings into orthogonal moment sectors. A rank-completion bound controls exact identification of the remaining output graph and signs. A packing argument then converts an arbitrary high-fidelity density description into a bounded list of possible targets. This establishes the theorem for mixed descriptions of unrestricted length.

For achievability, full stabilizer identification uses

```math
N+\left\lceil\log_2\frac1\delta\right\rceil+4
```

copies with worst-case failure at most $`\delta`$, for $`0<\delta<1/8`$, by [Chang–Caro–Larocca–West, Theorem 1](../references/RELATED_WORK.md#ChangCaroLaroccaWest2026). Its tableau determines the branch target after $`x`$, which can then be described and prepared. Thus the classical-output leading rate is attained.

## 7. Resulting copy frontier

For $`m/N\to\beta\in(0,1)`$, the leading copies per source qubit are

| Output channel | Leading copy rate |
|---|---:|
| Quantum output | $`1-\beta`$ |
| Measure and prepare after the same outcome | $`1`$ |

Vanishing error is achievable at these rates by taking $`\delta_N\to0`$ with $`\log(1/\delta_N)=o(N)`$. Below the respective rates, the average fidelity tends to zero. The finite quantum statement is more informative when $`n=o(N)`$: for $`n=\lceil\sqrt N\rceil`$, it gives $`\sqrt N+O(\log(1/\delta))`$ copies, while Theorem 3 still requires $`N-o(N)`$ copies for any constant classical-output fidelity.

If $`m=o(N)`$, then $`n=N-o(N)`$ and there is no leading-rate reduction for quantum output. A fixed nonempty output still requires the full leading rate for fidelity above the random-state baseline. The project therefore separates the physical size of the measured subsystem from the information required for a classical description of the conditional target.

## 8. Physical verification convention

The verifier has one withheld conditional target and one prediction. A SWAP comparison accepts with probability

```math
P_{\mathrm{swap}}=\frac{1+F_\rho}{2}.
```

It is not a measurement of an unknown target projector. If $`A\in\{0,1\}`$ is the SWAP acceptance, the statistic $`2A-1`$ has mean $`F_\rho`$. Each independent trial uses $`k`$ training preparations and one verifier preparation. Repetition costs are additional to the training-copy counts in the theorems.

The exact pure-stabilizer promise and coherent retention of the output registers are part of the result. The success flag checks the algebraic combination of measured outcomes; it does not certify protection against unmodelled physical noise. The [interpretation](interpretation.md) explains these resource boundaries and gives an exact one-copy comparison.

## 9. Exact one-copy comparison

The two output classes already differ for one training copy. Put $`D=2^N`$ and $`d=2^m`$. For the full uniform stabilizer prior,

```math
F_{\mathrm{EB}}^{\mathrm{av}}(N,m,1;W)
=\frac{D/d+1}{D+1},
\qquad
F_Q^{\mathrm{av}}(N,m,1;W)
=\frac1d+\frac{d^2-1}{d(D+1)}.
```

Here is a direct proof, including the second-moment identity it uses. Expand a stabilizer state in the Hermitian Pauli basis. The coefficient of a nonidentity Pauli has mean zero; coefficients of distinct Paulis have zero mixed moment after averaging stabilizer signs. A fixed nonidentity Pauli belongs to a uniformly random stabilizer subspace with probability $`1/(D+1)`$. Therefore, using the Pauli expansion of the SWAP operator $`S`$,

```math
\mathbb E_\rho\rho^{\otimes2}
=\frac{I+S}{D(D+1)}.
```

Work in the standardized public basis and let $`C_x`$ be the unnormalized Choi matrix of the one-copy channel $`\Lambda_x`$, so $`C_x\ge0`$ and $`\operatorname{Tr}_{\mathrm{out}}C_x=I_D`$. Let $`|\Omega_d\rangle=\sum_{j=1}^d|j,j\rangle`$. Contracting the verifier input in the second moment gives the score operator

```math
R_x=\mathbb E_\rho\left[
\rho^T\otimes J_x\rho J_x^\dagger\right]
=\frac{I_D\otimes I_d+
|x\rangle\langle x|_A\otimes
|\Omega_d\rangle\langle\Omega_d|}{D(D+1)}.
```

Thus $`F=\sum_x\operatorname{Tr}(C_xR_x)`$. The identity term contributes $`D`$ for each $`x`$. The block $`\langle x|C_x|x\rangle_A`$ has trace $`d`$ and the Bell projector $`|\Omega_d\rangle\langle\Omega_d|`$ has largest eigenvalue $`d`$, so the second term is at most $`d^2`$ for an arbitrary channel. This bound is attained by measuring the training input: if its outcome equals the query, return its output register; otherwise return $`I_d/d`$.

For a measure-and-prepare channel, the same block has the form $`\int E_{x,y}^T\otimes\sigma_{x,y}`$ with $`\int E_{x,y}=I_d`$. Its Bell contribution satisfies

```math
\int\operatorname{Tr}(E_{x,y}\sigma_{x,y})
\le\int\operatorname{Tr}E_{x,y}=d.
```

It is attained by measuring the training output in a fixed computational basis and preparing the observed basis state. There are $`D/d`$ possible query strings. Substituting the contributions $`D+d^2`$ and $`D+d`$ gives the two formulas.

For $`N=2,m=1`$, the fidelities are $`0.8`$ and $`0.6`$. In general the quantum excess above $`1/d`$ is $`d+1`$ times the classical-output excess. This calculation uses identical outcome timing and provides a finite consistency check on the asymptotic distinction.

## Reading route

Continue to [the synthesis algorithm](synthesis.md), [its copy converse](quantum_converse.md), [the classical-output converse](classical_converse.md), and [the physical interpretation](interpretation.md). [Related work](../references/RELATED_WORK.md) identifies imported ingredients and distinguishes the matched conditional-learning task from nearby models. [Verification](../verification/README.md) documents what the finite checks establish.
