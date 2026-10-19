# A finite converse for quantum conditional outputs

This chapter bounds how well an unrestricted quantum learner can supply the conditional output of a fixed public Pauli measurement. The learner may retain all training copies, receive the test outcome, and then apply any channel to produce its prediction. The bound holds under the uniform prior over **all** pure stabilizer states, including states with deterministic constraints inside the public measurement.

The proof first treats an affine family whose unknown input phases are fixed across copies. Its full-row-rank moment sectors contain no information about the target at a fixed query. Translation symmetry extends this conclusion to every query. A quotient and a counted choice of transverse coordinates then transfer the result to the full stabilizer prior.

The operational definitions are in [the model](model.md). The matching leading quantum copy cost is achieved by [conditional synthesis](synthesis.md). The stronger restriction associated with a final classical density-matrix description is proved separately in [the classical converse](classical_converse.md). Physical preparation and verification costs are discussed in [the interpretation](interpretation.md).

## 1. Statement and operational scope

Let $`N\ge1`$, $`1\le m\le N`$, and $`n=N-m`$. Write $`V_N=\mathbb F_2^{2N}`$ for the binary Pauli-label space, equipped with its nondegenerate alternating symplectic form. A pure stabilizer state is specified by a Lagrangian subspace $`L\subseteq V_N`$ and a compatible eigenvalue assignment $`\chi`$. Compatibility includes the phases of the chosen Hermitian Pauli representatives; it need not mean that the eigenvalues form an ordinary character of an arbitrary Pauli section.

Fix an isotropic subspace $`W\subseteq V_N`$ of dimension $`n`$, independently of the unknown source. Its generators specify the public commuting measurement. A known Clifford $`C_W`$ puts that measurement on the first $`n`$ computational-basis qubits. For $`x\in\mathbb F_2^n`$, put

```math
J_x=(\langle x|\otimes I_m)C_W,\qquad
p_\rho(x)=\mathop{\mathrm{Tr}}\nolimits (J_x\rho J_x^\dagger),\qquad
\rho_x=\frac{J_x\rho J_x^\dagger}{p_\rho(x)}
```

on supported outcomes; $`I_m`$ denotes the identity on the $`m`$-qubit output space. The learner receives $`\rho^{\otimes k}`$, while $`x`$ is generated from a separate preparation of the same source. It receives $`x`$ but does not receive the remaining verifier system. Its final channel $`\Lambda_x`$ may depend on $`x`$ and use arbitrary retained quantum memory, ancillas, classical randomness, and joint operations.

For the uniform set $`\mathcal S_N`$ of projective pure stabilizer states, define

```math
F_Q^{\mathrm{av}}(N,m,k;W)
=\sup_{\{\Lambda_x\}}
\frac1{|\mathcal S_N|}
\sum_{\rho\in\mathcal S_N}\sum_x p_\rho(x)
\mathop{\mathrm{Tr}}\nolimits \!\left[\rho_x\Lambda_x(\rho^{\otimes k})\right].
```

The score is the overlap with a pure conditional target. Unsupported outcomes have weight zero. It is distinct from the acceptance probability of a SWAP comparison, which is $`(1+F)/2`$.

**Theorem 1 — finite quantum-output converse.** For every such $`N,m,W`$ and every integer $`k\ge0`$, set

```math
M_{N,m}
=1+\frac{2^n-1}{2^N+1}.
```

Then

```math
\boxed{
F_Q^{\mathrm{av}}(N,m,k;W)
\le
\min\!\left\{
1,\;
2^{-m}+(1-2^{-m})M_{N,m}\,2^{k-n}
\right\}.
}
```

In particular,

```math
F_Q^{\mathrm{av}}(N,m,k;W)
\le \min\{1,\;2^{-m}+2^{k-n}\}.
```

The exact zero-copy value is $`F_Q^{\mathrm{av}}(N,m,0;W)=2^{-m}`$. The displayed exponential bound is a convenient finite upper bound, not a formula for the optimum at every $`k`$.

The same upper bounds hold for the best fidelity guaranteed for every pure stabilizer source, since a worst-case guarantee is at most its uniform average. Returning $`I/2^m`$ always attains the baseline $`2^{-m}`$, for every source and every supported outcome.

### The earlier exact-report task

An auxiliary consequence concerns the complementary-stabilizer reporting task of [Hayashi–Lu, Section 2](../references/RELATED_WORK.md#HayashiLu2026Partial). The learner reports, **before the test outcome**, an $`m`$-dimensional isotropic subspace $`K\subseteq W^\perp`$ with $`K\cap W=0`$, together with compatible eigenvalues $`\eta`$. Exact success means

```math
K\subseteq L,\qquad \eta=\chi|_K.
```

When several reports are correct, success counts every one of them. Denote its optimal uniform-prior success probability by $`P_{\mathrm{id}}^{\mathrm{av}}`$.

**Theorem 2 — finite exact-report converse.**

```math
\boxed{
P_{\mathrm{id}}^{\mathrm{av}}(N,m,k;W)
\le
\min\!\left\{
1,\;\frac32\,M_{N,m}\,2^{k-n}
\right\}.
}
```

Every syntactically admissible report also specifies a conditional output state for every outcome: $`W\oplus K`$ is Lagrangian, so the joint outcome/report projector has rank one. Measuring the training copies to obtain the report and then preparing its corresponding branch state is an allowed quantum-output channel. Therefore Theorem 1 also bounds the original report-based verification score. It does not identify that score with the optimum over arbitrary outcome-dependent quantum channels.

## 2. The affine source and its fixed unknown mask

First take $`W`$ to be input $`Z`$ measurement on $`n`$ qubits. Choose independently and uniformly

```math
A\in\mathop{\mathrm{Alt}}\nolimits _n(\mathbb F_2),\qquad
a\in\mathbb F_2^n,\qquad
S\in\mathbb F_2^{n\times m},\qquad
b\in\mathbb F_2^m,
```

where $`\mathop{\mathrm{Alt}}\nolimits _n(\mathbb F_2)`$ denotes symmetric binary matrices with zero diagonal. Define

```math
q_A(u)=\sum_{i\lt j}A_{ij}u_i u_j,
\qquad
|\psi_{A,a,S,b}\rangle
=2^{-n/2}\sum_{u\in\mathbb F_2^n}
(-1)^{q_A(u)+a^Tu}|u\rangle|S^Tu+b\rangle.
```

This is a stabilizer state. For example, start with $`|+\rangle^{\otimes n}|b\rangle`$, apply the input $`Z`$ phases specified by $`a`$, the input controlled-$`Z`$ gates specified by $`A`$, and controlled additions specified by $`S`$.

The random variables $`A,a,S,b`$ are selected once. The learner receives $`k`$ copies of that same state. In particular, $`A`$ and $`a`$ are a static unknown mask; averaging them must be performed on the tensor power, not independently on each copy.

Measuring the input gives $`u`$ uniformly and independently of all four parameters. The conditional target is

```math
|y_u\rangle=|S^Tu+b\rangle.
```

The offset $`b`$ is unknown and uniform. Fixing it to zero would define a different prediction problem and would invalidate the fixed-query independence used below.

### Exact reports determine the whole affine map

For $`j=1,\ldots,m`$, the source is an eigenstate of

```math
Z_{B,j}\prod_{i=1}^n Z_{A,i}^{S_{ij}}
```

with eigenvalue $`(-1)^{b_j}`$. These $`m`$ independent commuting Paulis span a subspace $`K_S\subseteq W^\perp`$ disjoint from $`W`$.

Because every input outcome has positive uniform probability, $`L\cap W=0`$. Nondegeneracy of the pairing gives $`\dim(L\cap W^\perp)=m`$, so $`K_S=L\cap W^\perp`$. Thus the unique correct complementary subspace and its eigenvalues determine $`(S,b)`$. A correct report yields a correct affine-map estimate even if other, incorrect reports are handled arbitrarily.

### Quantum fidelity becomes label prediction

For any density matrix $`\sigma_u`$ supplied by the learner,

```math
\mathop{\mathrm{Tr}}\nolimits (|y_u\rangle\langle y_u|\sigma_u)
=\Pr[\text{computational-basis measurement of }\sigma_u\text{ returns }y_u].
```

Composing any quantum-output channel with this final basis measurement produces a label-guessing POVM with exactly the same score. Conversely, a label guess can be prepared as a computational-basis state. The optimal quantum-output fidelity for this affine ensemble therefore equals its optimal label-prediction success probability. This reduction imposes no restriction on how the training copies are processed.

## 3. The common-mask average and its moment sectors

Write the $`k`$ input strings as the rows of $`X\in\mathbb F_2^{k\times n}`$. Introduce

```math
F_X=[\,X\ \mathbf1_k\,],
\qquad
Q=\begin{bmatrix}S\\ b^T\end{bmatrix}
\in\mathbb F_2^{(n+1)\times m}.
```

The output-label matrix of the $`k`$ copies is $`Y=F_XQ`$.

Average the tensor-power density matrix over the fixed nuisance parameters $`A,a`$, leaving $`Q`$ fixed. A cross term between $`X`$ and $`X'`$ survives precisely when every mask coefficient has the same accumulated exponent. The coefficient of $`A_{ij}`$ tests

```math
\sum_{r=1}^k X_{ri}X_{rj}
=\sum_{r=1}^k X'_{ri}X'_{rj}
\qquad(i\lt j),
```

and the coefficient of $`a_i`$ tests $`\sum_rX_{ri}=\sum_rX'_{ri}`$. Since $`z^2=z`$ over $`\mathbb F_2`$, these are exactly the off-diagonal and diagonal entries of the Gram equality

```math
X^TX=X'^TX'.
```

For each attainable Gram matrix $`g`$, define

```math
\mathcal X_g=\{X:X^TX=g\},
\qquad
|v_{g,Q}\rangle
=\sum_{X\in\mathcal X_g}|X\rangle|F_XQ\rangle.
```

The averaged state is exactly

```math
\rho_Q
=\mathbb E_{A,a}
\left[|\psi_{A,a,S,b}\rangle\langle\psi_{A,a,S,b}|^{\otimes k}\right]
=2^{-nk}\sum_g|v_{g,Q}\rangle\langle v_{g,Q}|.
```

The sectors have mutually orthogonal input support. Their weights are

```math
w_g=\frac{|\mathcal X_g|}{2^{nk}},
```

independently of $`Q`$, because $`\|v_{g,Q}\|^2=|\mathcal X_g|`$. A learner can be given the sector label without reducing its information; equivalently, the state is already block diagonal in those sectors.

The target affine map and every fixed-query label are independent of $`A,a`$. Consequently replacing the hidden pure-state ensemble by this nuisance average preserves the score of every strategy. This is an average of correlated tensor-power states, not a replacement of the source by independently dephased copies.

Quadratic-phase averaging and the binary Gram/orthogonal-orbit relation are established tools in [Arunachalam–Schatzki, Lemma 2.9 and Sections 3.2 and 5.3](../references/RELATED_WORK.md#ArunachalamSchatzki2026). The complete rank argument needed here, including the square-matrix endpoint, follows next.

## 4. What a full-row-rank sector reveals

Suppose $`0\le k\le n`$. Call a matrix $`X`$ good when $`\mathop{\mathrm{rank}}\nolimits X=k`$.

**Lemma 3 — a good Gram fiber is a free orthogonal orbit.** If $`X`$ has full row rank and $`X'^TX'=X^TX`$, then $`X'`$ also has full row rank and there is a unique invertible $`O\in\mathbb F_2^{k\times k}`$ satisfying

```math
X'=OX,\qquad O^TO=I,\qquad O\mathbf1_k=\mathbf1_k.
```

**Proof.** The map $`X:\mathbb F_2^n\to\mathbb F_2^k`$ is surjective and $`X^T`$ is injective. Hence

```math
\mathop{\mathrm{rank}}\nolimits (X^TX)=k,
\qquad
\ker(X^TX)=\ker X.
```

The equal Gram matrix forces $`\mathop{\mathrm{rank}}\nolimits X'=k`$, and its kernel is also $`\ker X`$. Thus there is a unique invertible map $`O`$ on the common $`k`$-dimensional quotient with $`X'=OX`$. The Gram equality gives

```math
X^T(O^TO-I)X=0.
```

Surjectivity of $`X`$ and injectivity of $`X^T`$ imply $`O^TO=I`$.

For every binary vector $`v`$, $`v^Tv=\mathbf1_k^Tv`$. Orthogonality therefore gives

```math
\mathbf1_k^TOv=(Ov)^T(Ov)=v^Tv=\mathbf1_k^Tv.
```

Thus $`O^T\mathbf1_k=\mathbf1_k`$. Multiplying by $`O`$ gives $`O\mathbf1_k=\mathbf1_k`$. At $`k=0`$ the statements have their unique empty-matrix interpretation. $`\square`$

The proof uses full row rank of $`X`$, not invertibility of $`XX^T`$. The latter can fail in characteristic two without affecting the argument. It also proves that every Gram fiber is entirely good or entirely bad.

Fix a representative $`X_0`$ of a good fiber and write $`X=O_XX_0`$. Because $`O_X\mathbf1_k=\mathbf1_k`$,

```math
F_X=O_XF_{X_0}.
```

Put $`D=F_{X_0}Q`$. The normalized sector state is

```math
|\phi_{g,D}\rangle
=\frac1{\sqrt{|\mathcal X_g|}}
\sum_{X\in\mathcal X_g}|X\rangle|O_XD\rangle.
```

It depends on $`Q`$ only through $`D`$. Distinct $`D`$ give orthogonal states: for each fixed input basis vector $`X`$, the invertible map $`O_X`$ sends distinct $`D`$ to distinct output labels.

Since $`F_{X_0}`$ has rank $`k`$, each $`D`$ has exactly

```math
2^{m(n+1-k)}
```

preimages $`Q`$. They remain uniformly distributed and give identical quantum states. The exact affine-map identification optimum within a good sector is therefore

```math
P_{\mathrm{id,good}}=2^{-m(n+1-k)}.
```

One can attain this conditional value by distinguishing the orthogonal $`D`$ states and guessing a uniform preimage. No computational-efficiency claim about that sector measurement is needed for the converse.

## 5. Fixed-query independence and translation symmetry

### The target at zero remains uniform

At the fixed query $`u=0`$, the target is $`b`$. For every fixed pair $`(D,b)`$, the constraint defining the sector state is

```math
X_0S=D-\mathbf1_kb^T.
```

Full row rank of $`X_0`$ gives exactly $`2^{m(n-k)}`$ solutions $`S`$, independently of $`D`$ and $`b`$. Hence $`b`$ is uniform and independent of $`D`$.

Because the whole good-sector quantum state is a function of $`D`$, the averaged good-sector density matrix conditioned on $`b`$ is the same for every $`b`$. Any measurement, including a measurement obtained by postprocessing an arbitrary output channel, guesses $`b`$ with probability exactly $`2^{-m}`$. This is a statement about identical density matrices, so coherent processing or additional ancillas cannot improve it.

The uniform probability that a $`k\times n`$ matrix has deficient row rank is

```math
\beta_{n,k}
=1-\prod_{j=0}^{k-1}(1-2^{j-n}),
\qquad 0\le k\le n.
```

The empty product is one, so $`\beta_{n,0}=0`$. To see the formula, expose rows in order: after $`j`$ independent rows, their span occupies $`2^j`$ of the $`2^n`$ possible next rows.

This rank-failure probability is also the total mass of bad moment sectors. Bounding the success in every bad sector by one yields the two affine-ensemble bounds

```math
P_{\mathrm{id,aff}}
\le
(1-\beta_{n,k})2^{-m(n+1-k)}+\beta_{n,k},
```

```math
F_{\mathrm{aff}}(0)
\le
2^{-m}+(1-2^{-m})\beta_{n,k}.
```

For $`1\le k\le n`$, the union bound gives

```math
\beta_{n,k}
\le\sum_{j=0}^{k-1}2^{j-n}
=\frac{2^k-1}{2^n}
\lt 2^{k-n}.
```

Also $`2^{-m(n+1-k)}\le2^{k-n-1}`$ for $`m\ge1`$. Consequently, including $`k=0`$,

```math
P_{\mathrm{id,aff}}\le\frac32\,2^{k-n},
\qquad
F_{\mathrm{aff}}(0)
\le2^{-m}+(1-2^{-m})2^{k-n}.
```

For integer $`k>n`$, both coarse right-hand sides are at least one, so the same inequalities remain valid.

### Every fixed query has the same optimum

For a known $`t\in\mathbb F_2^n`$, apply the input translation

```math
V_t|u\rangle=|u-t\rangle.
```

Up to a global phase, it maps the source parameters as

```math
(A,a,S,b)
\longmapsto
(A,\ a+At,\ S,\ b+S^Tt).
```

This is a bijection of the uniform parameter ensemble. The parameter formula contains unknown quantities, but the physical operation $`V_t`$ is a known input bit shift and does not require those quantities.

The target at the original query $`t`$ is the new offset $`b+S^Tt`$. Applying $`V_t^{\otimes k}`$ to the training data therefore converts prediction at query $`t`$ into prediction at zero under the same prior. Applying the inverse shift gives the reverse conversion. Thus every fixed-query Bayes optimum equals the zero-query optimum.

In this affine ensemble the test query is uniform and independent of the hidden parameters. A learner allowed to choose its final channel after the query can optimize separately for each query. Its average optimum is the average of the fixed-query optima, so

```math
F_{\mathrm{aff}}
\le
2^{-m}+(1-2^{-m})\beta_{n,k}
\qquad(0\le k\le n).
```

The good/bad sector decomposition itself need not be invariant under translation. The argument compares the complete fixed-query statistical experiments. It therefore does not require an assertion that a randomly chosen affine query row has the same relation to one fixed sector as the row at zero.

## 6. Resolving every intersection with the public measurement

We now return to a uniform pure stabilizer source on $`N`$ qubits. Let

```math
T=L\cap W,\qquad t=\dim T.
```

Give the learner $`T`$ and the true eigenvalues $`\chi|_T`$ as side information. Allowing source-dependent side information can only increase the optimal score.

The common eigenspace specified by these data is a known stabilizer code. A known Clifford identifies it with $`t`$ fixed computational-basis qubits and $`N'=N-t`$ unfrozen qubits. The logical symplectic space and measured subspace are

```math
\overline V=T^\perp/T,\qquad
\overline L=L/T,\qquad
\overline W=W/T,
\qquad
n'=n-t,\qquad N'=n'+m.
```

By construction, $`\overline L\cap\overline W=0`$.

### The conditional residual prior is uniform

For fixed $`T`$, the quotient map gives a bijection between original Lagrangians containing $`T`$ and logical Lagrangians in $`T^\perp/T`$. Its inverse sends $`\overline L`$ to its full inverse image in $`T^\perp`$. Requiring $`L\cap W=T`$ is exactly the condition $`\overline L\cap\overline W=0`$.

Each original Lagrangian has $`2^N`$ compatible eigenvalue assignments. Fixing the $`t`$ independent eigenvalues on $`T`$ leaves $`2^{N-t}=2^{N'}`$ assignments, uniformly and with the same count for every $`\overline L`$. These become all logical assignments under the known code identification.

Consequently, conditional on the announced $`T`$ and its true signs, the residual source is uniform over all signed logical stabilizer states satisfying $`\overline L\cap\overline W=0`$. The frozen qubits carry only the already announced data; they are not an additional unknown-state resource.

### Every report and its eigenvalues descend correctly

This reduction must apply to the entire report alphabet. Let $`K`$ be any admissible original report, whether correct or incorrect. Since

```math
K\subseteq W^\perp\subseteq T^\perp,
\qquad
K\cap T=0,
```

the quotient map is injective on $`K`$. Its image $`\overline K`$ has dimension $`m`$ and is isotropic. If $`\overline v\in\overline K\cap\overline W`$, choose lifts $`v\in K`$ and $`w\in W`$. Then $`v-w\in T\subseteq W`$, so $`v\in K\cap W=0`$. Thus $`\overline K\cap\overline W=0`$.

Moreover,

```math
\overline K\subseteq\overline L
\quad\Longleftrightarrow\quad
K\subseteq L,
```

because the inverse image of $`\overline L`$ is $`L`$.

Let $`I_T`$ be the known code isometry and fix known logical Pauli representatives. For every $`v\in T^\perp`$,

```math
I_T^\dagger P_v I_T
=\lambda_T(v)\,\overline P_{\overline v},
```

where the sign $`\lambda_T(v)`$ is determined by the chosen coordinates and the announced $`T`$ eigenvalues. Define the logical report eigenvalues on $`\overline K`$ by

```math
\overline\eta(\overline v)=\eta(v)/\lambda_T(v)
\qquad(v\in K).
```

The injectivity on $`K`$ makes this definition unambiguous. With compatible Pauli phases the joint spectral projector is

```math
\Pi_{K,\eta}
=2^{-m}\sum_{v\in K}\eta(v)^{-1}P_v.
```

Restricting each summand gives the exact identity

```math
I_T^\dagger\Pi_{K,\eta}I_T
=\Pi_{\overline K,\overline\eta}.
```

The true source eigenvalues transform by the same rule. Therefore correctness, incorrectness, and Born verification scores are preserved. Multiple correct original complements can map to the unique generic logical complement; their probabilities are added. Selecting only one original complement would not justify the exact-report bound.

## 7. A counted frame gives the uniform transverse chart

For a residual Lagrangian $`\overline L`$ disjoint from $`\overline W`$, choose uniformly a Lagrangian $`\mathcal F`$ such that

```math
\overline W\subseteq\mathcal F,\qquad
\mathcal F\cap\overline L=0,
```

and announce it. The number of choices must be independent of the unknown $`\overline L`$ for this side information to yield the claimed conditional prior.

For counting, choose symplectic coordinates in which $`\overline L`$ is the full $`X`$ subspace and $`\overline W`$ is generated by $`Z_1,\ldots,Z_{n'}`$. These coordinates exist because $`\overline L\cap\overline W=0`$: the pairing of $`\overline W`$ against $`\overline L`$ has rank $`n'`$, and a dual basis extends to a symplectic basis.

Every Lagrangian transverse to the full $`X`$ subspace has a unique graph representation

```math
\mathcal F=\{(Bz,z):z\in\mathbb F_2^{N'}\},
\qquad B=B^T.
```

Containing $`Z_1,\ldots,Z_{n'}`$ forces the first $`n'`$ columns of $`B`$ to vanish, and symmetry forces the corresponding rows to vanish. Its remaining $`m\times m`$ symmetric block is arbitrary. The number of compatible frames is exactly

```math
2^{m(m+1)/2},
```

independently of $`\overline L`$ and its eigenvalues.

Because the residual signed prior is uniform and this incidence degree is constant, conditioning on an announced $`\mathcal F`$ leaves a uniform distribution over all signed Lagrangians transverse to $`\mathcal F`$. Such a Lagrangian is automatically disjoint from $`\overline W`$, since $`\overline W\subseteq\mathcal F`$. No assumption about a uniform marginal distribution of frames is needed.

This is the compatible-frame incidence mechanism of [Hayashi–Lu, Lemmas 4.3–4.5](../references/RELATED_WORK.md#HayashiLu2026Partial), applied after fixing the intersection stratum.

Now choose a basis of the announced $`\mathcal F`$ extending the known basis of $`\overline W`$, and complete it by a deterministic symplectic-coordinate rule. This choice depends only on announced data. A known Clifford sends $`\mathcal F`$ to the full $`Z`$ subspace and $`\overline W`$ to the first $`n'`$ input $`Z`$ operators. The coordinates used for the learner therefore do not require knowledge of $`\overline L`$.

### Uniform chart parameters and the last side information

A state transverse to the full $`Z`$ subspace has the unique signed quadratic-phase representation

```math
|g_{\Gamma,s}\rangle
=2^{-N'/2}\sum_{z\in\mathbb F_2^{N'}}
i^{\sum_i\Gamma_{ii}z_i}
(-1)^{\sum_{i\lt j}\Gamma_{ij}z_i z_j+s^Tz}|z\rangle,
\qquad
\Gamma=\Gamma^T.
```

Indeed, transversality gives a unique generating matrix with Pauli labels $`(e_i,\Gamma e_i)`$; isotropy is exactly symmetry of $`\Gamma`$. Applying the indicated phase and controlled-$`Z`$ gates to $`|+\rangle^{\otimes N'}`$ gives those generators, and the $`Z`$ phases specified by $`s`$ run through their $`2^{N'}`$ compatible sign assignments. Thus $`\Gamma`$ parametrizes the transverse Lagrangian and $`s`$ its signs. Uniformity of the signed transverse chart means that they are independent and uniform.

Reveal the diagonal $`d_i=\Gamma_{ii}`$ and undo its known single-qubit phase gates. The remaining off-diagonal coefficients and the signs remain independent and uniform. Write

```math
\Gamma-\mathop{\mathrm{diag}}\nolimits (d)
=
\begin{bmatrix}
A&S\\ S^T&C
\end{bmatrix},
\qquad
s=\begin{bmatrix}a\\b\end{bmatrix},
```

where $`A`$ and $`C`$ have zero diagonal and the input block has size $`n'`$. Reveal $`C`$ and undo its known output controlled-$`Z`$ layer. Finally apply Hadamards to the output qubits. The result is exactly the affine source of Section 2 with parameters

```math
A,\ a,\ S,\ b
```

still independent and uniform, now with $`n'`$ inputs and $`m`$ outputs. The input mask remains unknown and common to all copies.

Revealing the output graph is legitimate for this quantum converse because side information makes the task easier. The [classical converse](classical_converse.md) keeps that graph hidden: it is part of the target whose classical description must be learned.

## 8. Transporting arbitrary conditional quantum outputs

The report-projector argument in Section 6 is sufficient for exact reports, but Theorem 1 requires transport of arbitrary output channels with the physical query timing intact.

Collect all announced data into $`g`$: the intersection and its signs, the compatible frame, the chart diagonal, and the output graph. Let

```math
I_g:(\mathbb C^2)^{\otimes N'}
\longrightarrow(\mathbb C^2)^{\otimes N}
```

be the known isometry encoding the resulting affine source into the original source. It consists of known Clifford coordinate changes, insertion of the known frozen qubits, and the inverses of the announced chart simplifications.

The isometry maps the logical public-measurement eigenspaces to the original ones. The $`t`$ deterministic outcomes are fixed by the announced signs, and the remaining outcome coordinates are related by a known invertible affine relabeling. Thus each logical $`u\in\mathbb F_2^{n'}`$ corresponds to exactly one original supported outcome $`x=x_g(u)`$.

Both the logical and original branch eigenspaces have dimension $`2^m`$. Their known identifications with an $`m`$-qubit output imply a known unitary $`V_{g,x}`$ satisfying

```math
J_x I_g=V_{g,x}J'_u,
\qquad
J'_u=\langle u|\otimes I_m,
\qquad x=x_g(u).
```

This follows directly by restricting the isometry to a measurement eigenspace: it is a unitary between two spaces of the same dimension. It also describes an explicit construction, by attaching the known measured input to the output, applying the known coordinate change, and removing the fixed measured factors.

For any original strategy $`\{\Lambda_x\}`$, define a strategy on logical training states by

```math
\widetilde\Lambda_{g,u}(\omega)
=
V_{g,x}^\dagger
\Lambda_x\!\left(I_g^{\otimes k}\omega(I_g^\dagger)^{\otimes k}\right)
V_{g,x}.
```

This is a channel. It uses only the announced data, the logical training copies, and the received logical outcome. If $`\rho=I_g\widetilde\rho I_g^\dagger`$, then

```math
p_\rho(x)=p_{\widetilde\rho}(u),
\qquad
\rho_x=V_{g,x}\widetilde\rho_u V_{g,x}^\dagger,
```

and therefore

```math
\mathop{\mathrm{Tr}}\nolimits \!\left[
\rho_x\Lambda_x(\rho^{\otimes k})
\right]
=
\mathop{\mathrm{Tr}}\nolimits \!\left[
\widetilde\rho_u
\widetilde\Lambda_{g,u}(\widetilde\rho^{\otimes k})
\right].
```

This construction never uses the unknown withheld test output. It preserves branch probabilities and fidelity, including when the original learner keeps all training systems until the test outcome. Consequently the affine quantum bound applies to every announced-data branch of the full uniform prior.

For completeness, in the original verification task, commutation of the report and measurement projectors gives

```math
\sum_x p_\rho(x)
\mathop{\mathrm{Tr}}\nolimits (\rho_x\tau_{K,\eta,x})
=\mathop{\mathrm{Tr}}\nolimits (\Pi_{K,\eta}\rho),
```

where $`\tau_{K,\eta,x}`$ is the report's known pure branch state. This equality is an outcome-averaged identity. Individual branch scores need not be independent of $`x`$.

## 9. The exact intersection moment and the finite bounds

Uniformity over pure stabilizer states induces a uniform prior on Lagrangians, because each Lagrangian has the same $`2^N`$ compatible signed states.

Every nonzero Pauli label belongs to the same number of Lagrangians, by symplectic transitivity. Counting pairs $`(L,v)`$ with $`0\ne v\in L`$ gives, for every fixed nonzero $`v\in V_N`$,

```math
\Pr[v\in L]
=\frac{2^N-1}{2^{2N}-1}
=\frac1{2^N+1}.
```

Since $`T=L\cap W`$ has $`2^t`$ elements,

```math
2^t
=1+\sum_{v\in W\setminus\{0\}}\mathbf1_{\{v\in L\}}.
```

Taking expectations yields the exact identity

```math
\boxed{
\mathbb E[2^t]
=1+\frac{2^n-1}{2^N+1}
=M_{N,m}
\lt 1+2^{-m}.
}
```

For each fixed announced-data branch with intersection dimension $`t`$, the residual affine input size is $`n'=n-t`$. Its coarse bounds are

```math
P_{\mathrm{id}}\le\frac32\,2^{k-n+t},
\qquad
F_Q\le2^{-m}+(1-2^{-m})2^{k-n+t}.
```

They remain valid when $`k>n'`$, since their right-hand sides then exceed one. An unaided learner cannot outperform a learner given all the announced data. Averaging these conditional upper bounds, and using that the supremum of an average is at most the average of the conditional suprema, gives

```math
P_{\mathrm{id}}^{\mathrm{av}}
\le\frac32\,2^{k-n}\mathbb E[2^t],
```

```math
F_Q^{\mathrm{av}}
\le2^{-m}+(1-2^{-m})2^{k-n}\mathbb E[2^t].
```

Substituting the exact moment and clipping by one proves Theorems 1 and 2. Finally,

```math
(1-2^{-m})M_{N,m}
\lt (1-2^{-m})(1+2^{-m})\lt 1,
```

which proves the simpler form in Theorem 1.

Keeping every intersection stratum is useful when $`m`$ is fixed: the dimensional cost is averaged through $`\mathbb E[2^t]`$, rather than treating every nontrivial intersection as an additive failure event.

### A sharper rank-failure form

Define $`\beta_{r,k}`$ by the product in Section 5 when $`0\le k\le r`$, and set $`\beta_{r,k}=1`$ when $`k>r`$. The same proof gives

```math
F_Q^{\mathrm{av}}(N,m,k;W)
\le
2^{-m}+(1-2^{-m})\,
\mathbb E\!\left[\beta_{n-t,k}\right].
```

The expectation is under the exact uniform-prior distribution of $`t=\dim(L\cap W)`$. This bound retains more finite-copy information than the exponential corollary, without claiming that the bad sectors are optimally decoded. In particular, $`\beta_{r,0}=0`$ proves the exact zero-copy upper bound.

One can also verify that endpoint directly. Averaging the $`2^N`$ compatible states of any fixed Lagrangian gives $`I/2^N`$. Hence

```math
\mathbb E_\rho[p_\rho(x)\rho_x]
=J_x\frac{I}{2^N}J_x^\dagger
=\frac{I_m}{2^N}.
```

Every zero-copy strategy consists of fixed density matrices $`\sigma_x`$. Its average score is

```math
\sum_{x\in\mathbb F_2^n}
\mathop{\mathrm{Tr}}\nolimits \!\left(\sigma_x\frac{I_m}{2^N}\right)
=2^{-m}.
```

## 10. Consequences and endpoints

For a single surviving qubit, $`m=1`$ and $`n=N-1`$, Theorem 1 reads

```math
F_Q^{\mathrm{av}}
\le
\min\!\left\{
1,\;\frac12+M_{N,1}2^{k-N}
\right\},
\qquad
M_{N,1}\lt \frac32.
```

Thus a fixed positive excess over $`1/2`$ requires $`N-O(1)`$ training copies.

More generally, if $`1\le m=o(N)`$ and $`k/N\to\alpha\lt 1`$, then

```math
P_{\mathrm{id}}^{\mathrm{av}}
\le 2^{-(1-\alpha)N+o(N)},
\qquad
0\le F_Q^{\mathrm{av}}-2^{-m}
\le 2^{-(1-\alpha)N+o(N)}.
```

The nonzero baseline must be retained when $`m`$ is bounded. If $`m\to\infty`$, the raw fidelity also tends to zero.

If instead $`m/N\to\beta\in(0,1)`$, every copy rate below $`1-\beta`$ gives vanishing quantum-output fidelity. The [synthesis theorem](synthesis.md) attains the leading $`n=N-m`$ copy term, including a worst-case guarantee. A final classical description has the different leading rate proved in [the classical converse](classical_converse.md); Theorem 2 alone does not establish that stronger after-query classical statement.

At the endpoint $`n=0`$, the measurement has a single outcome and $`m=N`$. One training copy can be returned directly, giving $`F_Q^{\mathrm{av}}=1`$ for $`k\ge1`$, while the zero-copy value is $`2^{-N}`$. The clipping in Theorem 1 is consistent with this endpoint. Returning a specimen does not identify its stabilizer or give its classical density-matrix description.

The bounds concern training copies. A physical fidelity-comparison trial also uses the independent verifier preparation, for $`k+1`$ source preparations in total. They allow unlimited coherent training memory and do not assert a running-time lower bound. See [the interpretation](interpretation.md) and [related work](../references/RELATED_WORK.md) for the resource and attribution boundaries.

## Appendix A. The finite converse over any prime field

The quantum and exact-report converses extend to every fixed prime local dimension $`p`$. This appendix supplies the changes needed in the proof; the synthesis and classical-output separation in the companion chapters are stated for qubits.

For $`N`$ qudits, fixed isotropic $`W`$ of dimension $`n=N-m`$, uniform projective pure stabilizer prior, and integer $`k\ge0`$, define

```math
M_{N,m,p}=1+\frac{p^n-1}{p^N+1},
\qquad
c_p=\frac1p+\frac1{p-1}.
```

Then

```math
P_{\mathrm{id}}^{\mathrm{av}}
\le
\min\{1,\;c_pM_{N,m,p}p^{k-n}\},
```

```math
F_Q^{\mathrm{av}}
\le
\min\!\left\{
1,\;
p^{-m}+
\frac{1-p^{-m}}{p-1}M_{N,m,p}p^{k-n}
\right\}.
```

The zero-copy fidelity is exactly $`p^{-m}`$.

For odd $`p`$, let $`\omega=e^{2\pi i/p}`$ and replace the binary affine source by

```math
|\psi_{A,a,S,b}\rangle
=p^{-n/2}\sum_{u\in\mathbb F_p^n}
\omega^{\frac12u^TAu+a^Tu}|u\rangle|S^Tu+b\rangle,
```

where $`A`$ is uniform over **all** symmetric matrices, including its diagonal, and $`a,S,b`$ are independent and uniform. All parameters remain fixed across the $`k`$ copies.

Averaging the quadratic and linear input phases now preserves the joint moment

```math
(G,\ell)=(X^TX,\ X^T\mathbf1_k).
```

The quadratic diagonal is needed to enforce the diagonal of $`G`$; the independent linear phases enforce $`\ell`$. The same fiber-sum expression for the averaged state holds with weight $`p^{-nk}`$ and these joint fibers.

If $`X`$ has full row rank, the argument of Lemma 3 gives $`X'=OX`$ with $`O^TO=I`$. Equality of the linear moments adds

```math
X^TO^T\mathbf1_k=X^T\mathbf1_k.
```

Injectivity of $`X^T`$ implies $`O^T\mathbf1_k=\mathbf1_k`$, hence $`O\mathbf1_k=\mathbf1_k`$. This reasoning also holds when $`k`$ is divisible by $`p`$; it does not divide by $`\mathbf1_k^T\mathbf1_k`$.

The full-rank sector therefore depends on $`Q=[S;b^T]`$ only through $`D=F_{X_0}Q`$. Its exact-map success is $`p^{-m(n+1-k)}`$. For every fixed $`D,b`$, the equation $`X_0S=D-\mathbf1_kb^T`$ has exactly $`p^{m(n-k)}`$ solutions, so the zero-query label remains uniform even conditioned on the sector state.

Translation by $`t`$ again maps

```math
(A,a,S,b)\longmapsto(A,a+At,S,b+S^Tt)
```

up to a global phase and preserves the uniform prior. It equates the fixed-query optima as before. With

```math
\beta_{n,k,p}
=1-\prod_{j=0}^{k-1}(1-p^{j-n})
\qquad(0\le k\le n),
```

the affine bounds are

```math
P_{\mathrm{id,aff}}
\le(1-\beta_{n,k,p})p^{-m(n+1-k)}+\beta_{n,k,p},
```

```math
F_{\mathrm{aff}}
\le p^{-m}+(1-p^{-m})\beta_{n,k,p}.
```

For $`k\ge1`$,

```math
\beta_{n,k,p}
\le\sum_{j=0}^{k-1}p^{j-n}
=\frac{p^k-1}{(p-1)p^n}
\lt \frac{p^{k-n}}{p-1},
```

and $`p^{-m(n+1-k)}\le p^{k-n-1}`$. These give the stated affine constants. At $`k=0`$ the same coarse inequalities hold directly; at integer $`k>n`$ their right-hand sides exceed one.

The quotient and conditional-prior proof uses $`T^\perp/T`$ over $`\mathbb F_p`$ and $`p^{N-t}`$ compatible logical assignments after the true $`T`$ eigenvalues are fixed. The projector transport uses known $`p`$th-root phases $`\lambda_T(v)`$ in place of signs. Its injectivity, exactness equivalence, and branch-unitary channel transport are unchanged.

The frame count is $`p^{m(m+1)/2}`$, since the free block is a symmetric $`m\times m`$ matrix over $`\mathbb F_p`$. A transverse signed chart has the uniform representation

```math
p^{-N'/2}\sum_z
\omega^{\frac12z^T\Gamma z+s^Tz}|z\rangle,
\qquad \Gamma=\Gamma^T.
```

Split $`\Gamma`$ into input, cross, and output blocks. Reveal and remove the **full output block**, including its diagonal, and apply the inverse Fourier transform to the outputs. This produces the stated affine source. Keep the input diagonal unknown and uniform, as required by the joint-moment calculation.

Finally, counting nonzero vector incidences gives

```math
\Pr[v\in L]=\frac1{p^N+1},
\qquad
\mathbb E[p^{\dim(L\cap W)}]
=1+\frac{p^n-1}{p^N+1}.
```

Averaging the residual bounds with input size $`n-t`$ proves the two prime-field inequalities. The zero-copy calculation uses the uniform state average $`I/p^N`$ and gives $`p^{-m}`$, completing the endpoints.
