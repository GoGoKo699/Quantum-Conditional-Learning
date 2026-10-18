# Conditional synthesis from retained quantum examples

The learner can produce the requested branch without obtaining a classical description of its stabilizer basis. The construction has two parts: find a suitable affine combination of observed outcomes, then apply a known quantum convolution to their retained output states. The finite-field selection is classical; the remaining conditional information stays quantum.

The [model](model.md) fixes $`N`$ source qubits, $`n=N-m`$ measured constraints, $`m`$ output qubits and $`k`$ training copies. Public Clifford standardization lets us use computational measurements on the first $`n`$ qubits throughout this proof.

## 1. One unknown basis and affine output labels

**Lemma 1.** For any pure stabilizer source, the supported input outcomes form an affine space $`a+V\subseteq\mathbb F_2^n`$ and are uniform on that space. There are a fixed $`m`$-qubit Clifford $`U`$ and an affine map $`f:a+V\to\mathbb F_2^m`$ such that

```math
\rho_x=U|f(x)\rangle\langle f(x)|U^\dagger
\qquad(x\in a+V).
```

Neither $`U`$ nor $`f`$ is given to the learner, and different outcomes may have the same output label.

**Proof.** Write the Pauli stabilizer subspace as a Lagrangian $`L\subseteq\mathbb F_2^{2N}`$ and the measured input-$`Z`$ subspace as $`W`$. Put $`T=L\cap W`$ and $`t=\dim T`$. The true stabilizer characters on $`T`$ impose exactly $`t`$ independent affine constraints on the measurement signs. The remaining $`r=n-t`$ outcome coordinates are uniformly random, by the stabilizer expansion of the joint outcome probabilities.

The subspace $`L\cap W^\perp`$ has dimension $`m+t`$. Its output projection has kernel $`T`$, hence its image is an $`m`$-dimensional commuting Pauli subspace on the surviving register. It is the same for every supported outcome. Choose output generators in this image and fixed lifts in $`L\cap W^\perp`$. Each lift has an input-$`Z`$ factor and an output Pauli factor. Its known-to-the-source stabilizer eigenvalue times the measured input eigenvalue gives the output eigenvalue. These signs depend affinely on $`x`$.

A Clifford $`U`$ maps the computational $`Z`$ basis to the joint eigenbasis of this fixed output subspace. Collecting its $`m`$ affine eigenvalue bits gives $`f(x)`$. The resulting joint eigenspace is one dimensional, so it specifies the pure conditional state. This proves the lemma. $`\square`$

## 2. The imported quantum convolution

Let $`K`$ be odd. For each coordinate of $`K`$ output blocks, apply the following two layers in the stated order:

1. $`\operatorname{CNOT}_{1\to i}`$ for $`i=2,\ldots,K`$.
2. $`\operatorname{CNOT}_{i\to1}`$ for $`i=2,\ldots,K`$.

The resulting permutation unitary $`V_K`$ acts on computational strings by

```math
V_K|z_1,\ldots,z_K\rangle
=\left|\sum_{i=1}^Kz_i,\;z_2+z_1,\ldots,z_K+z_1\right\rangle.
```

All additions are binary. Discarding every block except the first defines the channel $`\mathcal B_K`$.

This is the multiple-state quantum convolution of [Bu–Gu–Jaffe](../references/RELATED_WORK.md#BuGuJaffe2025), with the explicit valid CNOT index ranges written above. Their computational action is Lemma 9, Equation (15), and their same-Clifford covariance is Theorem 51, Equation (63).

**Lemma 2.** When $`K\equiv1\pmod4`$, every Clifford $`U`$ obeys

```math
\mathcal B_K\!\left(\bigotimes_{i=1}^KU\rho_iU^\dagger\right)
=U\mathcal B_K\!\left(\bigotimes_{i=1}^K\rho_i\right)U^\dagger.
```

Together with the computational action, this gives

```math
\mathcal B_K\!\left(
\bigotimes_{i=1}^KU|z_i\rangle\langle z_i|U^\dagger
\right)
=U\left|\sum_i z_i\right\rangle
\left\langle\sum_i z_i\right|U^\dagger.
```

**Direct phase check.** In the Heisenberg picture, output $`X`$ and $`Z`$ on one coordinate pull back to their $`K`$-fold tensor products. Output $`Y`$ pulls back with factor $`i^{1-K}`$, which is $`+1`$ for $`K\equiv1\pmod4`$. Hence every output Pauli $`P`$ pulls back as $`P^{\otimes K}`$. Clifford conjugation permutes Paulis up to a sign, and the sign is preserved under an odd tensor power. The covariance follows on a Pauli basis and therefore on every operator.

At $`K\equiv3\pmod4`$, the extra phase is generally nontrivial. An arbitrary odd subset would not produce the desired state for an unknown complex stabilizer basis. The weight condition in the algorithm below is therefore essential. No conjugated-copy input is supplied or assumed.

## 3. Algorithm

Measure the public input register on every training copy. Store its outcome $`x_i`$ and retain its $`m`$-qubit conditional output. After the independent test outcome $`x`$ arrives, find a vector $`c\in\mathbb F_2^k`$ satisfying

```math
\sum_{i=1}^kc_i x_i=x,
\qquad
\operatorname{wt}(c)\equiv1\pmod4.
```

If no such vector exists, return $`I/2^m`$ and a failure flag. Otherwise select the $`K=\operatorname{wt}(c)`$ blocks with $`c_i=1`$, apply $`\mathcal B_K`$, and return its first output with a success flag.

The parity condition gives $`\sum_i c_i=1`$. By Lemma 1 and affinity,

```math
\sum_i c_i f(x_i)=f\!\left(\sum_i c_i x_i\right)=f(x).
```

Lemma 2 therefore proves that every success output is exactly $`\rho_x`$. Global phases of individual conditional state vectors have no physical effect. The all-ones selector is allowed if its weight is $`1\pmod4`$; a restriction arising in an alternative unitary implementation is unnecessary for this one-output channel.

## 4. Probability that a selector exists

Fix the unknown source and a supported test outcome $`x`$. Put $`Z_i=x_i-x`$. By Lemma 1, these are independent uniform vectors in $`V`$, whose dimension is $`r\le n`$.

Let

```math
\mathcal A_k=
\{c\in\mathbb F_2^k:\operatorname{wt}(c)\equiv1\pmod4\}.
```

A roots-of-unity filter on the binomial expansion gives

```math
|\mathcal A_k|
=\sum_{j\equiv1\;(\mathrm{mod}\;4)}\binom kj
=2^{k-2}+2^{k/2-1}\sin\frac{k\pi}{4}.
```

For $`k\ge4`$, the absolute size of the oscillating term is at most $`2^{k-3}`$; the cases $`k=1,2,3`$ have respectively $`1,2,3`$ selectors. Thus

```math
|\mathcal A_k|\ge2^{k-3}\qquad(k\ge1).
```

For $`c\in\mathcal A_k`$, define $`I_c`$ to be the indicator of $`\sum_i c_i Z_i=0`$. Every selector is nonzero, so $`\mathbb E I_c=2^{-r}`$. Any two distinct nonzero vectors over $`\mathbb F_2`$ are linearly independent. The pair of their sums is therefore uniform on $`V\times V`$, so their indicators are pairwise independent.

Writing $`Y=\sum_c I_c`$, one obtains

```math
\mathbb E Y=|\mathcal A_k|2^{-r},
\qquad
\operatorname{Var}Y=|\mathcal A_k|2^{-r}(1-2^{-r}).
```

Chebyshev's inequality at $`Y=0`$ yields

```math
\Pr(Y=0)
\le\frac{\operatorname{Var}Y}{(\mathbb E Y)^2}
=\frac{2^r-1}{|\mathcal A_k|}
\le2^{n-k+3}.
```

Taking $`k=n+\lceil\log_2(1/\delta)\rceil+3`$ proves the uniform success guarantee. If $`r=0`$, all outcomes coincide and the failure probability is exactly zero; a single training output is already the requested branch.

The argument conditions on a fixed supported $`x`$. It consequently also holds when $`x`$ is independently drawn from the verifier source. It neither learns the support $`V`$ nor assumes that the input outcomes have full support in $`\mathbb F_2^n`$.

## 5. Finding the selector in polynomial time

The existence proof does not require enumerating $`\mathcal A_k`$. First solve the binary linear system

```math
X^Tc=x,
\qquad
\mathbf1^Tc=1,
```

where row $`i`$ of $`X`$ is $`x_i^T`$. If it is inconsistent, no valid selector exists. Otherwise parameterize its solutions by $`c=c_0+Bz`$.

On an odd-weight binary vector, the identity

```math
\sum_{i<j}c_ic_j
=\binom{\operatorname{wt}(c)}2\pmod2
```

shows that weight $`1\pmod4`$ is equivalent to

```math
Q(c)=\sum_{i<j}c_ic_j=0.
```

Substitution gives one quadratic Boolean polynomial $`g(z)=Q(c_0+Bz)`$. If $`g(0)=0`$, take $`z=0`$. If $`g(0)=1`$, inspect the unit vectors. If none is a root, every linear coefficient in the multilinear representation of $`g`$ vanishes. Inspect sums of two distinct unit vectors. If none is a root, every quadratic coefficient also vanishes. The polynomial is then identically one and has no root.

This procedure examines at most $`1+d+\binom d2`$ points, where $`d`$ is the dimension of the linear solution space. Gaussian elimination and these evaluations have polynomial time and storage cost in $`k,n`$. The success flag can therefore be computed efficiently from the stored classical outcomes.

## 6. Quantum resources

The selected convolution uses $`2m(K-1)\le2m(k-1)`$ CNOTs. Its two displayed sweeps have depth $`2(K-1)`$ if gates on the $`m`$ different coordinates run in parallel and the required connections are available. Hardware routing costs may increase that depth.

Before the query, the streaming implementation stores $`km`$ output qubits and $`kn`$ classical outcome bits. Each full training preparation is measured once on its public input register. The fixed public Clifford standardization, if needed, is charged for every preparation. No unknown source circuit or inverse, QRAM, amplitude loading, classical description of $`U`$, or label oracle is used.

The retained blocks are data consumed by the task. On a success branch the protocol returns one output specimen. An ignored or discarded block is not promised to remain a reusable training resource. A [SWAP-based comparison](model.md#8-physical-verification-convention) uses the independent verifier specimen and has acceptance $`(1+F)/2`$.

## 7. Alternative copy symmetry and scope

An alternative proof uses [Gross–Nezami–Walter's stochastic-orthogonal copy symmetries](../references/RELATED_WORK.md#GrossNezamiWalter2021). If a selector $`c`$ of weight $`1\pmod4`$ has a zero coordinate $`j`$, set $`v=c+e_j`$ and $`O=I+vv^T`$. Since $`\operatorname{wt}(v)\equiv2\pmod4`$, this binary matrix fixes the all-ones vector and preserves the quadratic weight form modulo four. Its $`j`$th row is $`c`$. The associated permutation across copies commutes with every Clifford tensor power and extracts the desired affine label.

The [finite physical checks](../verification/README.md) include this alternative, with nonpermutation combinations and complex stabilizer states. The commutation statement has no requirement that $`m\ge k-1`$; a size condition in the Clifford commutant literature concerns linear independence of a spanning family, a different statement.

The convolution route above is the main algorithm because it only needs to preserve one output and accepts every valid selector. Both routes retain the exact stabilizer promise. Their algebraic success flags do not certify unknown noise in state preparation, measurement or gates. The [quantum converse](quantum_converse.md) explains why the leading measured-size copy cost cannot be improved uniformly.
