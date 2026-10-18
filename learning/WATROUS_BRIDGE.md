# From Watrous to quantum conditional learning

An unknown source can supply quantum examples even when its classical description is unavailable. After a public measurement on a fresh preparation produces an outcome, the learner must supply the corresponding remaining state. This project asks how the required number of examples changes when the prediction can retain quantum information from the training data, compared with a prediction prepared entirely from a classical description.

The single educational anchor is **John Watrous, _The Theory of Quantum Information_**, Cambridge University Press, 2018 ([publisher and DOI](https://doi.org/10.1017/9781316848142); [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/)). The numbered sections, equations and printed page references below refer to the author's **January 2018 prepublication manuscript**, linked from that page. Its [contents](https://cs.uwaterloo.ca/~watrous/TQI/TQI.frontmatter.pdf) locate the readings. The repository links to the source and does not reproduce or redistribute the book.

Watrous supplies the operator, channel, measurement, fidelity and discrimination framework. The stabilizer geometry, convolution, finite-field counting and conditional-learning theorems are developed in the scientific pages and attributed to their research sources. The [30-milestone map](MILESTONES.md) organizes the route into 14 background milestones and 16 narrative milestones. The [model](../science/model.md) remains the authority for the experiment and theorem quantifiers.

<a id="reading-map"></a>
## 1. Targeted reading from the single anchor

These are focused readings to use alongside the project, with the mathematical connection developed below.

| Milestones and project use | Verified Watrous manuscript location | Connection developed here |
|---|---|---|
| M01–M02: states, subsystems and conditioning | [Sections 2.1.2–2.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), pp. 61–71; Section 2.3.2, pp. 105–112, especially partial measurements, Eqs. (2.224)–(2.228) | Subnormalized branch operators and the independent verifier preparation. |
| M03–M04: the allowed learner classes | [Sections 2.2.1–2.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), pp. 72–91; Theorems 2.22 and 2.26, Corollary 2.27; [Section 6.1.1 and Exercise 6.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf), p. 384 for the exercise | General channels, Choi normalization and measure-and-prepare outputs after the same query. |
| M05: fidelity and physical comparison | [Section 3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), Definition 3.11, p. 139; Proposition 3.13, p. 142; [Section 2.3.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | Translation from root fidelity to the project's pure-target overlap and SWAP acceptance. |
| M06–M07: priors, discrimination and support bounds | [Sections 1.1.3 and 1.2.2–1.2.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf); [Section 3.1.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), p. 125, and Section 3.1.2, p. 132 | Positive operator bounds, ensemble discrimination and average versus worst-case statements. Theorem 3.4 gives the binary Holevo–Helstrom result; the many-label proof uses the ensemble formulation. |
| M08–M13: algebra, moments and experiment transport | [Sections 1.1.1–1.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf), plus Sections 2.2.1–2.2.2; [Sections 7.1.1–7.1.2 and 7.2.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf) for tensor symmetry and averaging | The anchor supplies linear algebra and quantum operations. The specific binary symplectic spaces, Gram sectors and counted stabilizer charts come from the project and its research references. |
| M15 and M20–M23: one-copy calculation and quantum converse | [Section 2.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), especially Eqs. (2.65)–(2.66); [Section 3.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) | A channel score as a Choi pairing; identical averaged states as an obstruction to every learner. |
| M24–M27: the classical-output converse | [Section 1.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf); [Section 3.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf); [Section 6.1.1 and Exercise 6.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf) | Support dimension bounds exact decoding, while a complex Gram-matrix argument converts arbitrary density descriptions to short lists. |
| M14, M16–M19 and M28–M30: construction and complete operational story | The readings above, connected to [synthesis](../science/synthesis.md), [the theorem map](../science/model.md) and [resources](../science/interpretation.md) | The project supplies the conditional synthesis algorithm, the two copy laws and their physical interpretation. |

Exercise 6.1 is an **exercise**, not a numbered theorem. It states the equivalence between breaking entanglement with every reference system, having a separable Choi operator, and possessing a measure-and-prepare representation. This is the precise anchor for the comparator used here.

<a id="conventions"></a>
## 2. Notation and normalization

The project uses Dirac notation and explicit register names. The following translations prevent changes to the actual task.

| Watrous convention | Project convention | Consequence |
|---|---|---|
| $`u`$, $`u^*`$, $`uu^*`$ | $`\lvert\psi\rangle`$, $`\langle\psi\rvert`$, $`\lvert\psi\rangle\langle\psi\rvert`$ | A pure state is a unit-trace projector; an unnormalized vector need not define a normalized state. |
| $`\mathcal L(\mathcal X)`$, $`\mathrm D(\mathcal X)`$ | The same operator and density-matrix spaces | Here the training input has dimension $`2^{Nk}`$ and the prediction has dimension $`2^m`$. |
| $`\mu(y)`$ | $`E_y`$ or $`E_x(dy)`$ | A POVM effect acts jointly on all training copies. |
| $`\eta(x)\in\mathrm{Pos}(\mathcal B)`$ | $`J_x\rho J_x^\dagger`$ | The branch probability is its trace; normalization occurs only on supported outcomes. |
| $`F_{\mathrm W}(\rho,\sigma)=\lVert\sqrt\rho\sqrt\sigma\rVert_1`$ | Pure-target score $`\operatorname{Tr}(\rho_x\sigma)`$ | The project uses the square of Watrous's fidelity when the target is pure. |
| $`J(\Phi)\in\mathcal L(\mathcal Y\otimes\mathcal X)`$ | $`C_\Phi\in\mathcal L(\mathcal X\otimes\mathcal Y)`$ | Both Choi matrices are unnormalized; their tensor factors appear in the opposite order. |
| $`\mathrm{Sep}(\mathcal Y:\mathcal X)`$ | Separable positive Choi operators | This is a cone, unlike the unit-trace state set $`\mathrm{SepD}`$. |

### Fidelity must be squared before averaging

For a pure target $`\rho_x=|\psi_x\rangle\langle\psi_x|`$, Proposition 3.13 gives

```math
F_{\mathrm W}(\rho_x,\sigma)
=\sqrt{\langle\psi_x|\sigma|\psi_x\rangle},
\qquad
F_{\mathrm{project}}(\rho_x,\sigma)
=F_{\mathrm W}(\rho_x,\sigma)^2.
```

Consequently the repository's average score is

```math
F_\rho(\Lambda)
=\sum_x p_\rho(x)\,
F_{\mathrm W}\!\left(\rho_x,\Lambda_x(\rho^{\otimes k})\right)^2.
```

The square belongs inside the average. Squaring an averaged root fidelity gives a different quantity. The trace overlap remains meaningful for mixed predictions because only the target needs to be pure. If the source promise were changed so that the targets were mixed, the same trace overlap would generally cease to equal squared fidelity.

The operator $`J_x=(\langle x|_A\otimes I_B)C_W`$ in the model is a **branch map**. It is unrelated to the use of the letter $`J`$ for Watrous's Choi representation $`J(\Phi)`$. The arguments and subscripts distinguish the objects.

### Two Gram matrices, over different fields

The converses use two notions with different algebra.

| Object | Field and adjoint | Role |
|---|---|---|
| $`G=X^{\mathsf T}X`$ | Entries and rank over $`\mathbb F_2`$; ordinary transpose | Labels moment sectors produced by a shared hidden phase. |
| $`H_{ij}=\langle v_i\mid v_j\rangle`$ | Complex entries; Hermitian matrix | Controls the operator norm of a sum of pure-state projectors. |

A binary bilinear form can have nonzero isotropic vectors. In particular, full row rank of $`X`$ does not justify assuming $`XX^{\mathsf T}`$ invertible over $`\mathbb F_2`$. The [quantum rank argument](../science/quantum_converse.md#4-what-a-full-row-rank-sector-reveals) uses the correct quotient and kernel identities.

<a id="conditioning"></a>
## 3. Conditioning defines an experiment

For [M02](MILESTONES.md#m02) and [M14](MILESTONES.md#m14), write the public measurement as a channel with both a classical record and a quantum remainder:

```math
\mathcal M_W(\rho)
=\sum_x |x\rangle\langle x|_X\otimes \eta_\rho(x),
\qquad
\eta_\rho(x)=J_x\rho J_x^\dagger.
```

The identities $`\sum_xJ_x^\dagger J_x=I`$ and $`\operatorname{Tr}\rho=1`$ make this a normalized classical-quantum state. Each nonzero block satisfies

```math
p_\rho(x)=\operatorname{Tr}\eta_\rho(x),
\qquad
\rho_x=\frac{\eta_\rho(x)}{p_\rho(x)}.
```

This is the project's specialization of the partial-measurement framework in Section 2.3.2. The normalized conditional state is nonlinear as a function of $`\rho`$, but the subnormalized branch map is linear. Keeping $`\eta_\rho(x)`$ intact is especially useful in moment and Choi calculations:

```math
p_\rho(x)\operatorname{Tr}\!\left[
\rho_x\Lambda_x(\rho^{\otimes k})\right]
=
\operatorname{Tr}\!\left[
J_x\rho J_x^\dagger\Lambda_x(\rho^{\otimes k})\right].
```

There is no division by a potentially small branch probability in this score identity.

The verifier applies this measurement to an **independent** source preparation. The learner receives the classical $`x`$ while the verifier retains the quantum branch. Training copies and this fresh copy share the same unknown source parameter; their preparation randomness is independent conditional on that source. The target-generating quantum register is never part of the learner's input.

Both learners may store their entire training input until $`x`$ arrives. Their final operations are therefore families $`\{\Lambda_x\}_x`$. The constructive quantum protocol happens to measure its training input registers earlier. That implementation choice does not impose an early-measurement restriction on the converse or on the classical comparator.

A rare branch also carries its actual probability in the performance criterion. Repeating preparation until the training outcome equals a particular query is one possible method, with a cost controlled by $`1/p_\rho(x)`$. The synthesis theorem instead combines several retained branches. The experiment itself does not grant free repeated postselection or omit failed attempts.

<a id="output-channels"></a>
## 4. Where the classical description enters

For [M03](MILESTONES.md#m03) and [M04](MILESTONES.md#m04), separate the physical input from the information allowed to reach the prediction.

A general quantum learner uses a completely positive, trace-preserving map from $`k`$ training copies to one $`m`$-qubit output. Channels absorb ancillary systems, adaptive measurements, discarded registers and classical randomness. Their representation by Choi, Kraus or Stinespring operators is a change of mathematical description; it does not restrict the allowed device.

A classical-description learner first measures, then prepares:

```math
\Lambda_x(A)
=\int \operatorname{Tr}[E_x(dy)A]\,\sigma_{x,y},
\qquad
\int E_x(dy)=I.
```

The report may specify any mixed density matrix with arbitrary precision and length. It may also specify an arbitrarily complicated preparation circuit. In each case, after the report is fixed, the output depends on the training data only through that classical record.

The reference-system criterion makes this distinction precise. In the finite-dimensional setting of Exercise 6.1, the map is entanglement breaking exactly when applying it to one part of any joint input produces a separable state between the returned output and the untouched reference. Equivalently, its Choi operator is separable across the output–input-reference cut. Allowing a continuous report alphabet does not enlarge the channel class: the finite-dimensional separable cone is closed, and its elements admit finite separable decompositions.

This cut is different from the split between measured and retained qubits **inside the source**. The classical learner can start with an entangled stabilizer source and make an entangled collective measurement across all copies. Its final $`m`$-qubit density matrix can itself be entangled across its output qubits. The restriction is the intervening classical description, not a separability condition on those physical states.

Known preprocessing and postprocessing preserve the measure-and-prepare class. If $`\Lambda(A)=\sum_y\operatorname{Tr}(E_yA)\sigma_y`$, then preprocessing by a channel changes the effects by its adjoint, and postprocessing changes the prepared states. This observation is needed when the converse reveals a coordinate frame and transports a strategy to a graph or affine chart.

<a id="choi-one-copy"></a>
## 5. Choi normalization and the one-copy calculation

For [M15](MILESTONES.md#m15), let $`D_{\mathrm{in}}`$ be the training input dimension and $`d`$ the output dimension. Watrous uses

```math
J_{\mathrm W}(\Lambda)
=\sum_{i,j}\Lambda(|i\rangle\langle j|)
\otimes |i\rangle\langle j|
\quad\text{on output}\otimes\text{input}.
```

The project's input-first convention is

```math
C_\Lambda
=\sum_{i,j}|i\rangle\langle j|
\otimes\Lambda(|i\rangle\langle j|)
=S_{\mathrm{factors}}J_{\mathrm W}(\Lambda)S_{\mathrm{factors}}^\dagger.
```

Theorems 2.22 and 2.26 give, in either tensor order,

```math
C_\Lambda\ge0,\qquad
\operatorname{Tr}_{\mathrm{out}}C_\Lambda=I_{\mathrm{in}},
\qquad
\operatorname{Tr}C_\Lambda=D_{\mathrm{in}}.
```

Thus $`C_\Lambda`$ is not a density matrix. Dividing it by $`D_{\mathrm{in}}`$ would normalize its trace but would also change the partial-trace constraint and all score formulas.

The recovery identity, translated from Eq. (2.66), is

```math
\Lambda(A)
=\operatorname{Tr}_{\mathrm{in}}
[(A^{\mathsf T}\otimes I_{\mathrm{out}})C_\Lambda],
\qquad
\operatorname{Tr}[B\Lambda(A)]
=\operatorname{Tr}[C_\Lambda(A^{\mathsf T}\otimes B)].
```

The transpose is an algebraic part of this representation; no physical transpose of an unknown input is required.

For one training copy, put $`D=2^N`$ and $`d=2^m`$. The project proves directly, using Pauli signs and stabilizer incidence, that

```math
\mathbb E_\rho\rho^{\otimes2}=\frac{I+S}{D(D+1)}.
```

Chapter 7 supplies useful language for comparing such a tensor moment with a spherical moment. The identity for this **finite stabilizer ensemble**, including its normalization, is established in [model, Section 9](../science/model.md#9-exact-one-copy-comparison). A matching second moment does not imply matching higher moments.

Work in the standardized public basis, so the source and training coordinates have absorbed $`C_W`$ and $`J_x=\langle x|_A\otimes I_B`$. Contracting one factor with the verifier branch then produces

```math
R_x
=\mathbb E_\rho[\rho^{\mathsf T}\otimes J_x\rho J_x^\dagger]
=
\frac{I_D\otimes I_d+
|x\rangle\langle x|_A\otimes
|\Omega_d\rangle\langle\Omega_d|}{D(D+1)},
\qquad
|\Omega_d\rangle=\sum_{j=1}^d|j,j\rangle.
```

The mean score is $`\sum_x\operatorname{Tr}(C_xR_x)`$. Here $`\|\Omega_d\|^2=d`$, so $`|\Omega_d\rangle\langle\Omega_d|`$ has largest eigenvalue $`d`$. The channel constraint forces the relevant $`x`$ block of $`C_x`$ to have trace $`d`$. Its Bell contribution is therefore at most $`d^2`$ for general channels.

For a measure-and-prepare channel,

```math
C_x=\int E_x(dy)^{\mathsf T}\otimes\sigma_{x,y}.
```

Within the same $`x`$ block, the Bell pairing becomes a sum of $`\operatorname{Tr}(E_y\sigma_y)`$ terms, bounded in total by $`d`$. These two different feasible sets produce

```math
F_{\mathrm{EB}}^{\mathrm{av}}(N,m,1)
=\frac{D/d+1}{D+1},
\qquad
F_Q^{\mathrm{av}}(N,m,1)
=\frac1d+\frac{d^2-1}{d(D+1)}.
```

The scientific proof also supplies attaining channels, so the formulas are equalities. With $`N=2,m=1`$, they give $`0.6`$ and $`0.8`$. This small example isolates the output-channel distinction without a large-system limit.

<a id="moment-discrimination"></a>
## 6. Shared hidden parameters and discrimination

[M06](MILESTONES.md#m06), [M11](MILESTONES.md#m11) and [M20](MILESTONES.md#m20) concern a statistical point that can disappear if the quantum notation is simplified too early.

If $`h`$ is an unknown source parameter, the learner's prior-averaged training state is

```math
\omega^{(k)}=\mathbb E_h[\rho_h^{\otimes k}].
```

It is generally different from $`(\mathbb E_h\rho_h)^{\otimes k}`$. The former reuses the same hidden source in every preparation. The latter redraws it independently for each copy. The project assumes the former experiment throughout.

The phase mask in the quantum converse is therefore shared across copies. Averaging it removes a matrix element only if its total phase fails the mask constraints. Over $`\mathbb F_2`$, surviving pairs of computational tuples satisfy a binary Gram equality, yielding orthogonal sectors. Those sectors retain coherent superpositions; they are not a record of separately measured classical training examples.

Once a sector is established, Watrous's ensemble-discrimination language becomes useful. Suppose there are $`M`$ equally likely targets, and all their normalized training states are supported on a common $`q`$-dimensional subspace with projector $`\Pi`$. Every such state $`\omega_\theta`$ obeys $`0\le\omega_\theta\le\Pi`$. For any decoding POVM,

```math
P_{\mathrm{id}}
=\frac1M\sum_\theta\operatorname{Tr}(E_\theta\omega_\theta)
\le\frac1M\sum_\theta\operatorname{Tr}(E_\theta\Pi)
=\frac qM.
```

This is a direct positive-operator bound in the many-label discrimination problem of Section 3.1.2. It applies to collective quantum measurements of the entire training input.

The quantum converse needs a still stronger observation on good sectors. After the fixed query is translated to zero, its hidden output label $`b`$ is uniform and the averaged training density matrix is identical for every $`b`$. Processing identical density matrices cannot reveal their hidden labels. Measuring the final predicted output in that label basis turns its overlap with the target into the probability of guessing $`b`$, so every channel has conditional score $`2^{-m}`$ there. Only the deficient-rank sectors contribute excess fidelity. The [fixed-query proof](../science/quantum_converse.md#5-fixed-query-independence-and-translation-symmetry) preserves the learner's access to the query.

The uniform stabilizer prior is used to bound an average optimum. It also gives a worst-case obstruction, because for any fixed strategy the minimum score over sources cannot exceed its prior average. The constructive synthesis guarantee has a different strength: it works for every source and every supported query. These quantifiers are part of the theorem, not interchangeable descriptions of it.

<a id="gram-packing"></a>
## 7. From a mixed description to a bounded target list

The support bound alone proves a limitation on **exact identification**. An arbitrary density matrix can have positive overlap with several different pure targets, so exact decoding cannot simply be substituted for the fidelity task. [M24–M26](MILESTONES.md#m24) supply the additional conversion.

In one nuisance block of the classical converse, the remaining target label is the output graph and its sign vector, $`\theta=(C,b)`$. Grouping computational tuples by their target character gives a common support dimension. A finite-field rank-completion argument bounds this dimension relative to the number of possible labels. This part of the proof is in [classical converse, Sections 4–6](../science/classical_converse.md#4-orthogonal-nuisance-blocks).

Now fix any reported density matrix $`\sigma`$. For a threshold $`\eta>0`$, consider the finite set

```math
\mathcal H_\sigma
=\{\theta:\operatorname{Tr}(\sigma\tau_\theta)\ge\eta\}.
```

Select pure-state vectors $`v_1,\ldots,v_L`$ for targets in this set with graph matrices far apart in rank. The graph-state overlap calculation gives an upper bound $`\varepsilon`$ on the **amplitude** $`|\langle v_i|v_j\rangle|`$ for distinct selected targets. Squared overlaps must be square-rooted at this step.

Let $`V`$ have columns $`v_j`$. Its complex Gram matrix is $`H=V^\dagger V`$, while the projector sum is $`VV^\dagger=\sum_j|v_j\rangle\langle v_j|`$. The nonzero spectra of these two matrices agree. Bounding each absolute row sum gives

```math
\left\|\sum_{j=1}^L|v_j\rangle\langle v_j|\right\|_\infty
=\|H\|_\infty
\le1+(L-1)\varepsilon.
```

Here the norm on $`H`$ is the spectral operator norm; the row sum is an upper bound for it. Positivity and $`\operatorname{Tr}\sigma=1`$ then imply

```math
L\eta
\le\operatorname{Tr}\!\left[
\sigma\sum_j|v_j\rangle\langle v_j|\right]
\le1+(L-1)\varepsilon.
```

Choosing $`\varepsilon\le\eta/2`$ bounds the number of separated representatives by $`2/\eta`$. Maximality covers every remaining high-overlap target by a low-rank graph neighborhood. Counting these neighborhoods yields a finite bound $`|\mathcal H_\sigma|\le L_{\max}`$ that holds even for mixed $`\sigma`$ and unbounded descriptions.

A classical decoder can take the learner's report and choose a target uniformly from this list. If the report had overlap at least $`\eta`$ with the true target, the decoder succeeds with probability at least $`1/L_{\max}`$. Therefore, within the fixed block,

```math
F_{\mathrm{block}}
\le\eta+L_{\max}P_{\mathrm{id}}^*(\mathrm{block}).
```

The hypothetical decoder need not run efficiently: it is used to bound a learner class that already allows unrestricted computation. Bad blocks are bounded directly by score one **before** multiplying the good-block decoding bound by $`L_{\max}`$. Otherwise a large list factor could destroy the probability estimate.

Watrous's spectral and positive-operator framework explains why the argument applies to every mixed report. The graph overlap formula, rank neighborhoods, moment support dimensions and asymptotic choice of parameters are supplied in the [complete packing proof](../science/classical_converse.md#7-from-arbitrary-density-matrices-to-short-target-lists).

<a id="synthesis"></a>
## 8. Quantum processing in an unknown common basis

[M16–M19](MILESTONES.md#m16) explain why keeping quantum examples changes the achievable copy rate.

After the known public standardization, supported measurement outcomes form an affine space $`a+V\subseteq\mathbb F_2^n`$. The project proves that their conditional outputs share one unknown Clifford basis:

```math
\rho_x=U|f(x)\rangle\langle f(x)|U^\dagger,
```

where $`f`$ is affine. The learner knows neither $`U`$ nor $`f`$. A classical description would need enough information about the conditional target to prescribe its preparation; the quantum construction can act directly on retained specimens.

Given training outcomes $`x_1,\ldots,x_k`$ and the supplied query $`x`$, it selects coefficients satisfying

```math
\sum_i c_ix_i=x,
\qquad
\operatorname{wt}(c)\equiv1\pmod4.
```

In particular, $`\sum_i c_i=1`$, so affinity yields $`\sum_i c_if(x_i)=f(x)`$. The selected output states can then be combined by the [Bu–Gu–Jaffe convolution](../references/RELATED_WORK.md#BuGuJaffe2025):

```math
\mathcal B_K\!\left(\bigotimes_{i=1}^K U\rho_iU^\dagger\right)
=
U\,\mathcal B_K\!\left(\bigotimes_{i=1}^K\rho_i\right)U^\dagger,
\qquad K\equiv1\pmod4.
```

This covariance is useful precisely because the same unknown $`U`$ occurs in every retained block. It does not require learning $`U`$ and then implementing its inverse. The project gives the circuit and checks its Pauli action. The $`Y`$ phase is $`i^{1-K}`$, explaining why arbitrary odd $`K`$ is insufficient for an unknown complex stabilizer basis.

The selector count and pairwise-independence argument give a failure bound of $`2^{n-k+3}`$. A binary linear system followed by one restricted quadratic Boolean equation finds a valid selector in polynomial time whenever one exists. Returning $`I/2^m`$ on failure converts exact flagged success into the unconditional fidelity guarantee

```math
F_\rho\ge1-(1-2^{-m})\delta
\quad\text{for}\quad
k=n+\left\lceil\log_2(1/\delta)\right\rceil+3.
```

Watrous supplies the framework in which this measurement, retention, mixing and discard operation is a channel. The affine stabilizer lemma, selector proof and convolution covariance are specific additional ingredients, with their proofs and attributions in [synthesis](../science/synthesis.md). A computable selector flag certifies the algebraic relation of the measured outcomes under the exact source promise; it does not certify the absence of physical noise.

<a id="full-prior"></a>
## 9. Side information must preserve the statistical experiment

For [M13](MILESTONES.md#m13), [M22](MILESTONES.md#m22) and [M27](MILESTONES.md#m27), giving a learner additional classical information can only increase its optimal score: it can always ignore that information. A lower-bound proof can therefore reveal convenient coordinates. It must still show that those coordinates describe the intended prior and preserve the actual branch experiment.

In the quantum converse the stabilizer subspace $`L`$ may intersect the public measured subspace $`W`$. Revealing $`T=L\cap W`$ and its signs identifies frozen measured coordinates. Quotienting by them leaves a residual source with $`N'=N-t`$ and $`n'=n-t`$, where $`t=\dim T`$, while the output size remains $`m`$.

A compatible transverse frame is then selected by a counted incidence construction. Its constant number of compatible choices makes the residual graph parameters uniform. Choosing a convenient frame without this count would not by itself preserve the prior needed in the affine argument.

Let $`g`$ denote the announced data, $`I_g`$ its known encoding isometry, and $`u`$ the logical outcome corresponding to the original supported outcome $`x`$. The proof establishes a known output unitary $`V_{g,x}`$ with

```math
J_xI_g=V_{g,x}J'_u.
```

Every original learner is transported into a logical learner by

```math
\widetilde\Lambda_{g,u}(\omega)
=
V_{g,x}^\dagger
\Lambda_x\!\left[
I_g^{\otimes k}\omega(I_g^\dagger)^{\otimes k}
\right]
V_{g,x}.
```

Channel composition makes this a valid channel. The branch identity preserves both outcome probabilities and target overlap, and the transformation uses only announced information and the received query. It does not act on the withheld verifier specimen. If the original channel is measure and prepare, the transported channel remains in that class.

The quantum proof averages every intersection stratum using

```math
\mathbb E[2^t]
=1+\frac{2^n-1}{2^N+1}.
```

The extensive-output classical proof can instead bound the event $`t\ge1`$ by less than $`2^{-m}`$ and work on the transverse stratum. That shortcut is adequate for its asymptotic regime; retaining all strata is what gives the more informative quantum bound at fixed small $`m`$. The [full-prior channel transport](../science/quantum_converse.md#8-transporting-arbitrary-conditional-quantum-outputs) and [classical transfer](../science/classical_converse.md#8-transfer-to-all-pure-stabilizer-states) make these different uses precise.

<a id="resource-frontier"></a>
## 10. Reading the copy laws as physical claims

[M28–M30](MILESTONES.md#m28) combine the constructions and converses.

For $`m/N\to\beta\in(0,1)`$, quantum output has leading training-copy rate $`1-\beta`$, while the measure-and-prepare output class has rate $`1`$. Vanishing synthesis error is compatible with these rates when $`\delta_N\to0`$ and $`\log(1/\delta_N)=o(N)`$. The classical upper bound comes from full stabilizer identification followed by conditional preparation, credited in [related work](../references/RELATED_WORK.md#ChangCaroLaroccaWest2026).

When $`n=\lceil\sqrt N\rceil`$, the quantum construction uses $`\sqrt N+O(\log(1/\delta))`$ copies, while arbitrary classical descriptions still require $`N-o(N)`$ copies for nonvanishing fidelity. Typical full-support branches have probability $`2^{-n}`$, so waiting for a particular training branch can cost $`2^n`$ preparations. That comparison describes a particular matching strategy. The optimal classical comparator has linear copy cost, as established by its matching upper and lower bounds.

The resource account includes $`kN`$ supplied training qubits, $`km`$ retained conditional-output qubits after training measurements, the classical outcome records, public Clifford standardization and the selector computation. Mixing $`K`$ selected output blocks uses $`2m(K-1)`$ CNOTs and returns one output specimen. Source preparation, storage time, geometry-dependent routing and verification repetitions remain separate physical costs. The construction needs no QRAM or inverse of an unknown source-preparation circuit.

A SWAP measurement on prediction $`\sigma`$ and withheld target $`\rho_x`$ uses the symmetric effect $`(I+S)/2`$. Its acceptance probability is

```math
P_{\mathrm{swap}}
=\operatorname{Tr}\!\left[
\frac{I+S}{2}(\sigma\otimes\rho_x)\right]
=\frac{1+\operatorname{Tr}(\sigma\rho_x)}2.
```

Averaging gives $`(1+F_\rho)/2`$, not $`F_\rho`$. Each trial consumes the learner's output and a verifier branch, and uses $`k+1`$ source preparations before any additional repetitions. The [resource interpretation](../science/interpretation.md) specifies the guarantee being tested and the [verification account](../verification/README.md) explains the scope of the finite checks.

The central conclusion concerns the information that must survive from training to prediction. It does not assert an exponential advantage over the optimal classical learner, a runtime lower bound, a noise threshold, or a reusable classical model obtained from a single quantum prediction.

<a id="source-boundaries"></a>
## 11. What the anchor supplies and where the project continues

| Ingredient | Role of the anchor | Exact project development or research attribution |
|---|---|---|
| States, POVMs and conditional branches | Chapters 1–2 supply the formalism. | [The experiment](../science/model.md#1-source-public-measurement-and-held-out-outcome) fixes which registers and outcomes the learner receives. |
| Choi optimization and the EB comparator | Section 2.2.2 and Exercise 6.1 supply the representations and class characterization. | [The exact one-copy comparison](../science/model.md#9-exact-one-copy-comparison) computes this task's score and attaining channels. |
| Stabilizer and Clifford geometry | General tensor and operator language provides a foundation. | [The branch lemma](../science/synthesis.md#1-one-unknown-basis-and-affine-output-labels) and [the counted frame construction](../science/quantum_converse.md#7-a-counted-frame-gives-the-uniform-transverse-chart) supply the needed binary geometry. |
| Clifford-covariant quantum convolution | Channel theory explains its physical interpretation. | [Bu–Gu–Jaffe](../references/RELATED_WORK.md#BuGuJaffe2025) supply the primitive; [the synthesis proof](../science/synthesis.md#2-the-imported-quantum-convolution) identifies the valid phase condition and its use here. |
| Shared-mask moment sectors | Chapter 7 provides context for tensor symmetry and averaging. | [The common-mask calculation](../science/quantum_converse.md#3-the-common-mask-average-and-its-moment-sectors), with [Arunachalam–Schatzki attribution](../references/RELATED_WORK.md#ArunachalamSchatzki2026), establishes the actual finite-field sectors. |
| Exact decoding and mixed-output packing | Sections 1.1.3 and 3.1.2 supply positive-operator and ensemble language. | [The rank-completion bound](../science/classical_converse.md#5-rank-completion-and-the-number-of-possible-target-characters) and [density-to-list conversion](../science/classical_converse.md#7-from-arbitrary-density-matrices-to-short-target-lists) establish the copy obstruction. |
| Full-prior copy laws | Channel composition and elementary probability explain valid reductions. | [Quantum converse](../science/quantum_converse.md) and [classical converse](../science/classical_converse.md) own the rates, endpoint regimes and quantifiers. |

The [source account](../references/RELATED_WORK.md#Watrous2018) and bibliography record this single educational anchor alongside the primary research attributions. Return to [M01–M14](MILESTONES.md#m01) for the background route or [M15–M30](MILESTONES.md#m15) for the narrative and its complete scientific argument.

