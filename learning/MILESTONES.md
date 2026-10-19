# Thirty milestones for quantum conditional learning

Measuring part of an unknown state leaves a classical outcome and a remaining quantum system. This project asks how many preparations are needed to supply that remaining state for an outcome observed on an independent preparation. Its central comparison gives both learners the same copies and the same late query. A quantum learner can pass retained quantum information into its prediction; a classical-description learner must prepare its prediction from a classical measurement record.

The map below contains exactly **30 project-defined milestones**. Phase I has **14 background/preliminary milestones** because the problem joins the operator language of quantum information with stabilizer geometry, binary moments, and statistical decision bounds. These objects come together in the complete experimental contract at M14. Phase II has **16 narrative/innovation milestones**: a finite example, the synthesis mechanism, the two converse mechanisms, and their joint physical meaning. It ends with the complete project explanation at M30.

The allocation follows these scientific dependencies. The map gives a route to global understanding; individual technical proofs remain in the linked science pages.

## Anchor and conventions

The single educational anchor is **John Watrous, [The Theory of Quantum Information](https://cs.uwaterloo.ca/~watrous/TQI/) (2018)**. Section and result numbers below refer to the author's January 2018 manuscript linked from that official book page. The [Watrous bridge](WATROUS_BRIDGE.md) explains the notation changes and supplies the connections to this project. The research papers in [related work](../references/RELATED_WORK.md) establish or contextualize particular ingredients; they do not constitute additional educational anchors.

Throughout the map, $`N`$ is the number of source qubits, $`m`$ the number of surviving output qubits, $`n=N-m`$ the number of independent public commuting measurement constraints, and $`k`$ the number of training preparations. The independent verifier preparation is additional to $`k`$.

The project scores the overlap $`\mathop{\mathrm{Tr}}\nolimits (\sigma\rho_x)`$ with a pure conditional target. Watrous's fidelity is unsquared, so this overlap equals $`F_{\mathrm W}(\sigma,\rho_x)^2`$. The project uses input–output order for its Choi matrices; Watrous uses output–input order. These conventions are addressed explicitly in M04, M05, and M15.

## Map at a glance

| Phase I: background/preliminaries | Phase II: narrative/innovation |
|---|---|
| [M01 States and operator expectations](#m01) | [M15 An exact one-copy separation](#m15) |
| [M02 Subsystems and conditional states](#m02) | [M16 One unknown basis for all branches](#m16) |
| [M03 Channels chosen after a query](#m03) | [M17 Adding labels through an unknown Clifford](#m17) |
| [M04 Choi matrices and classical descriptions](#m04) | [M18 Why enough admissible selectors exist](#m18) |
| [M05 Pure-target fidelity and physical comparison](#m05) | [M19 The complete polynomial synthesis algorithm](#m19) |
| [M06 Ensembles and the order of quantifiers](#m06) | [M20 A masked affine source](#m20) |
| [M07 Discrimination and the geometry of many targets](#m07) | [M21 Good Gram sectors reveal no query label](#m21) |
| [M08 Commuting Paulis and symplectic geometry](#m08) | [M22 Transport from every stabilizer stratum](#m22) |
| [M09 Clifford coordinates and a public measurement](#m09) | [M23 The finite quantum copy law](#m23) |
| [M10 Affine constraints and conditional signs](#m10) | [M24 The target that remains after the query](#m24) |
| [M11 A common hidden parameter across copies](#m11) | [M25 Rank completion limits exact target information](#m25) |
| [M12 Binary Gram matrices and rank counts](#m12) | [M26 Arbitrary density descriptions yield short lists](#m26) |
| [M13 Side information and equivalent experiments](#m13) | [M27 The full classical-description copy law](#m27) |
| [M14 The complete operational question](#m14) | [M28 The joint frontier and a growing advantage](#m28) |
|  | [M29 The cost of a complete physical trial](#m29) |
|  | [M30 The complete conditional-learning story](#m30) |

## Phase I: background/preliminaries

<a id="m01"></a>

### M01 States and operator expectations

**Central question.** What mathematical object describes an unknown quantum specimen, and what can a measurement reveal about it?

**Understanding target.** Interpret a density operator as positive and unit trace, a pure state as a rank-one projector, and $`\mathop{\mathrm{Tr}}\nolimits (E\rho)`$ as a measurement probability when $`0\le E\le I`$. Relate tensor products to independently prepared specimens of the same source. Distinguish physical possession of $`\rho`$ from possession of a classical matrix or a preparation circuit specifying it.

**Dependencies and story role.** This is the starting point. It introduces the local objects whose preparation count and eventual output form define the project.

**Conceptual connection.** A state may have an efficient mathematical description while that description remains unknown to the learner. The stabilizer promise will constrain the source family without supplying its stabilizer tableau.

**Source pointers.** Watrous §§1.1.1–1.1.3 and §2.1.2, through the [anchor bridge](WATROUS_BRIDGE.md). Project: [source and access](../science/model.md#1-source-public-measurement-and-held-out-outcome), [output descriptions](../science/model.md#2-two-output-channel-classes).

<a id="m02"></a>

### M02 Subsystems and conditional states

**Central question.** How does measuring one part of a specimen define the state of the surviving part?

**Understanding target.** Separate a marginal state obtained by forgetting an outcome from a conditional state obtained by retaining it. For a branch map $`J_x`$, identify its probability $`p_\rho(x)=\mathop{\mathrm{Tr}}\nolimits (J_x\rho J_x^\dagger)`$ and normalize the supported branch as $`\rho_x=J_x\rho J_x^\dagger/p_\rho(x)`$. Unsupported outcomes have zero score weight. Explain why a rank-one measurement on the input of a pure source leaves a pure surviving state.

**Dependencies and story role.** Builds on [M01](#m01). It turns a global specimen into the query-and-target pair used in the experiment.

**Conceptual connection.** The verifier sends the classical query while retaining the conditional quantum system. This separation makes the learner's task a prediction task: access to the remaining verifier system would already provide the requested specimen.

**Source pointers.** Watrous §2.1 and §2.3.2, especially partial measurements in Eqs. (2.224)–(2.228), through the [bridge](WATROUS_BRIDGE.md). Project: [branch maps and independent verifier](../science/model.md#1-source-public-measurement-and-held-out-outcome).

<a id="m03"></a>

### M03 Channels chosen after a query

**Central question.** How can the model include every physical way of processing the training systems after the query arrives?

**Understanding target.** Interpret complete positivity and trace preservation as the conditions on a quantum channel, including extensions by an untouched reference system. Understand how ancillas, coherent gates, intermediate measurements, classical randomness, and discarded registers fit within one channel. Represent a learner by a family $`\{\Lambda_x\}`$ that may depend on the supplied classical outcome.

**Dependencies and story role.** Uses [M01](#m01) and [M02](#m02). It moves from individual states and branches to an unrestricted class of allowed learners.

**Conceptual connection.** A converse about this channel family applies even when all training copies are retained coherently until the query. An algorithm that measures its input registers early is a valid member of the class; its timing does not impose an early-measurement restriction on competitors.

**Source pointers.** Watrous §§2.2.1–2.2.2, Theorems 2.22 and 2.26, and Corollary 2.27, through the [bridge](WATROUS_BRIDGE.md). Project: [quantum-output channels](../science/model.md#quantum-output), [shared timing](../science/interpretation.md#1-the-shared-experiment).

<a id="m04"></a>

### M04 Choi matrices and classical descriptions

**Central question.** Which restriction on a channel expresses the requirement that its prediction be prepared from a classical description?

**Understanding target.** Translate between a channel and its positive Choi matrix with the appropriate partial-trace constraint. Recognize measure-and-prepare channels of the form $`\Lambda_x(A)=\int\mathop{\mathrm{Tr}}\nolimits [E_x(dy)A]\sigma_{x,y}`$ as entanglement breaking. The effects form any collective POVM, and each report may specify any mixed density matrix with unrestricted length, precision, and preparation complexity.

**Dependencies and story role.** Uses [M03](#m03). It isolates the exact output restriction that the main comparison studies.

**Conceptual connection.** The classical-description learner can itself use coherent memory and a quantum computer before its final measurement. The distinction concerns transmission of quantum information from training to prediction. In Choi calculations, swap Watrous's output–input tensor order to the project's input–output order and move the trace constraint accordingly.

**Source pointers.** Watrous §2.2.2, Eqs. (2.65)–(2.66), §6.1, and Exercise 6.1, through the [bridge](WATROUS_BRIDGE.md). Project: [measure-and-prepare definition](../science/model.md#classical-description-followed-by-preparation), [one-copy Choi calculation](../science/model.md#9-exact-one-copy-comparison).

<a id="m05"></a>

### M05 Pure-target fidelity and physical comparison

**Central question.** How does the prediction score relate to an experimentally observable comparison?

**Understanding target.** For pure $`\rho_x`$, connect the overlap $`\mathop{\mathrm{Tr}}\nolimits (\sigma\rho_x)`$ to squared fidelity. Distinguish it from Watrous's unsquared $`F_{\mathrm W}`$. Derive the SWAP acceptance $`(1+F)/2`$ and the rescaled statistic $`2A-1`$, whose expectation is the mean overlap. Identify the baseline $`2^{-m}`$ obtained by the maximally mixed prediction.

**Dependencies and story role.** Uses [M01](#m01) and [M02](#m02). It attaches a common operational score to the two channel classes.

**Conceptual connection.** A verifier holding an unknown target can compare two specimens without knowing a target-projector measurement. One random acceptance bit is evidence from a single trial; estimating the mean requires fresh repeated trials. For one output qubit, baseline fidelity is $`1/2`$ while baseline SWAP acceptance is $`3/4`$.

**Source pointers.** Watrous §3.2, Definition 3.11 and Proposition 3.13, through the [bridge](WATROUS_BRIDGE.md). Project: [score convention](../science/model.md#3-fidelity-and-the-quantifiers-in-the-bounds), [physical verifier](../science/interpretation.md#6-fidelity-and-the-physical-verifier).

<a id="m06"></a>

### M06 Ensembles and the order of quantifiers

**Central question.** What does an average-prior obstruction imply about an algorithm intended to work for every source?

**Understanding target.** Keep the hidden source, the independently drawn query, and the learner's internal measurement randomness distinct. Compare $`\sup_\Lambda\mathbb E_\rho F_\rho(\Lambda)`$ with $`\sup_\Lambda\inf_\rho F_\rho(\Lambda)`$. The latter is at most the former, so a uniform-prior upper bound rules out a better every-source guarantee. Conversely, the constructive upper bound guarantees success for each source and each supported query.

**Dependencies and story role.** Uses [M03](#m03) and [M05](#m05). It fixes how achievability and impossibility statements can be combined without changing their statistical meaning.

**Conceptual connection.** A uniform distribution over all pure stabilizer states is a proof ensemble, not an extra promise that a physical source is redrawn between training copies. A rare failure branch still contributes to the score; heralded success does not permit conditioning away failures.

**Source pointers.** Watrous §1.2.2 and §3.1.2 for probability and state ensembles, through the [bridge](WATROUS_BRIDGE.md). Project: [fidelity quantifiers](../science/model.md#3-fidelity-and-the-quantifiers-in-the-bounds), [quantum construction's guarantee](../science/model.md#4-constructive-quantum-upper-bound).

<a id="m07"></a>

### M07 Discrimination and the geometry of many targets

**Central question.** How can the space occupied by an ensemble limit what any measurement can identify?

**Understanding target.** Model label identification by a POVM and compare a normalized state with the identity on its common support. For $`M`$ equiprobable states supported in a space of dimension $`d_{\mathrm{supp}}`$, explain the upper bound $`P_{\mathrm{id}}\le d_{\mathrm{supp}}/M`$. Relate the Gram matrix of pure vectors to their projector sum: they have the same nonzero eigenvalues.

**Dependencies and story role.** Uses [M01](#m01), [M03](#m03), and [M06](#m06). It introduces the decision and operator geometry that later connects exact labels to approximate predictions.

**Conceptual connection.** Orthogonal labels, linearly independent states, and nearly orthogonal states impose different constraints. A small support controls exact discrimination; a bounded projector sum controls how many pure targets can all have large overlap with one arbitrary mixed state. Both facts will be needed for the classical converse.

**Source pointers.** Watrous §§1.1.2–1.1.3 and §3.1.2, through the [bridge](WATROUS_BRIDGE.md). Project: [support-dimension bound](../science/classical_converse.md#4-orthogonal-nuisance-blocks), [Gram bound for target lists](../science/classical_converse.md#7-from-arbitrary-density-matrices-to-short-target-lists).

<a id="m08"></a>

### M08 Commuting Paulis and symplectic geometry

**Central question.** How does the stabilizer promise become finite-dimensional geometry?

**Understanding target.** Represent Pauli operators by binary labels, with a symplectic pairing that records commutation. Interpret an isotropic subspace as mutually commuting labels and a Lagrangian as a maximal such subspace of dimension $`N`$. A pure stabilizer also requires compatible eigenvalue data; phases of chosen Hermitian Pauli representatives matter. The unsigned subspace alone does not specify the state.

**Dependencies and story role.** Uses [M01](#m01) and [M02](#m02). It supplies the project-specific geometric language for the source and its public constraints.

**Conceptual connection.** The intersection $`T=L\cap W`$ identifies measurement constraints already fixed by the source. Orthogonal complements and quotients then express which commuting information survives measurement. Watrous supplies the operator and measurement foundations; this binary symplectic structure is developed in the project.

**Source pointers.** Watrous §§2.1.2 and 2.3.1, through the [bridge](WATROUS_BRIDGE.md). Project: [stabilizer and measurement spaces](../science/quantum_converse.md#1-statement-and-operational-scope), [conditional stabilizer projection](../science/synthesis.md#1-one-unknown-basis-and-affine-output-labels).

<a id="m09"></a>

### M09 Clifford coordinates and a public measurement

**Central question.** Which coordinate changes are available to the learner without learning the unknown state?

**Understanding target.** Explain that a Clifford maps Pauli operators to Pauli operators with their phases, preserving the symplectic commutation structure. A known Clifford can standardize the fixed public commuting measurement to computational measurements on $`n`$ input qubits. This operation depends on the public constraints, while the output Clifford appearing in the source's conditional family may remain unknown.

**Dependencies and story role.** Uses [M03](#m03) and [M08](#m08). It connects geometric normal forms to physical operations and separates known coordinates from hidden source structure.

**Conceptual connection.** A change of coordinates in a proof is an allowed algorithmic operation only when the required transformation is known. When it is physically applied, its gate cost is charged. Later, Clifford covariance permits a channel to work in a shared unknown basis without learning or implementing that basis.

**Source pointers.** Watrous §2.2.2 for unitary channel representations, through the [bridge](WATROUS_BRIDGE.md). Project: [public standardization](../science/model.md#1-source-public-measurement-and-held-out-outcome), [convolution covariance](../science/synthesis.md#2-the-imported-quantum-convolution), [standardization cost](../science/interpretation.md#5-physical-resource-accounting).

<a id="m10"></a>

### M10 Affine constraints and conditional signs

**Central question.** Why do stabilizer measurement outcomes have affine structure?

**Understanding target.** Interpret deterministic products of measured Pauli eigenvalues as binary affine constraints on the outcome string. With $`t=\dim(L\cap W)`$, the supported outcomes form an affine space of dimension $`r=n-t`$ and are uniform there. Understand how multiplying a stabilizer eigenvalue by a measured input sign determines a surviving output eigenvalue.

**Dependencies and story role.** Uses [M02](#m02), [M08](#m08), and [M09](#m09). It connects the local measurement rules into a relation across all supported branches.

**Conceptual connection.** Affine relations preserve an offset only when the coefficients sum to one. This will make odd selection parity necessary when combining observed outcome labels. The stronger weight condition used by the quantum circuit will come from phases, a separate requirement.

**Source pointers.** Watrous §2.3.2 for conditioning, through the [bridge](WATROUS_BRIDGE.md); the affine geometry is supplied by [the common-basis lemma](../science/synthesis.md#1-one-unknown-basis-and-affine-output-labels) and [the selector identity](../science/synthesis.md#3-algorithm).

<a id="m11"></a>

### M11 A common hidden parameter across copies

**Central question.** What survives when an unknown source parameter is averaged across a tensor power?

**Understanding target.** Distinguish $`\mathbb E_\theta[\rho_\theta^{\otimes k}]`$ from $`(\mathbb E_\theta\rho_\theta)^{\otimes k}`$. Training preparations are independent conditional on a fixed source, while the same hidden parameter appears in every copy. Averaging common phase variables removes precisely those tensor-power matrix elements with unequal accumulated characters and leaves orthogonal moment sectors.

**Dependencies and story role.** Uses [M01](#m01), [M06](#m06), and [M08](#m08). It turns the statistical source model into the correlated moment objects needed by both converses.

**Conceptual connection.** A nuisance average is legitimate when those hidden parameters do not change the target at the fixed query. It preserves every strategy's average score; independently dephasing each copy would change the available information. Target-independent sector weights allow the learner to be given the sector label.

**Source pointers.** Watrous §§2.1.2 and 3.1.2 for mixtures and ensembles, through the [bridge](WATROUS_BRIDGE.md). Project: [common-mask moments](../science/quantum_converse.md#3-the-common-mask-average-and-its-moment-sectors), [graph nuisance sectors](../science/classical_converse.md#4-orthogonal-nuisance-blocks).

<a id="m12"></a>

### M12 Binary Gram matrices and rank counts

**Central question.** Which finite-field rank facts turn moment constraints into an information bound?

**Understanding target.** Interpret $`X^TX`$ as a symmetric binary moment matrix, whose diagonal records linear parities. For full-row-rank $`X`$, use surjectivity of $`X`$ and injectivity of $`X^T`$ to reason about its Gram fiber. For a general block Gram matrix, use congruence and rank bounds without presuming nonsingularity. Understand why counting low-rank symmetric forms differs from counting arbitrary rectangular matrices.

**Dependencies and story role.** Uses [M07](#m07), [M08](#m08), and [M11](#m11). It introduces the finite-field mechanisms behind the two distinct converse exponents.

**Conceptual connection.** Real or complex intuition about positive Gram matrices cannot be imported unchanged into characteristic two. Full row rank of $`X`$ does not require $`XX^T`$ to be invertible. A symmetric completion may retain cross terms outside the image of its leading block.

**Source pointers.** Watrous §§1.1.1–1.1.3 supply general linear-algebra language through the [bridge](WATROUS_BRIDGE.md); the binary statements are proved in [Gram fibers](../science/quantum_converse.md#4-what-a-full-row-rank-sector-reveals) and [symmetric rank completion](../science/classical_converse.md#5-rank-completion-and-the-number-of-possible-target-characters).

<a id="m13"></a>

### M13 Side information and equivalent experiments

**Central question.** When does simplifying the source make an impossibility result stronger?

**Understanding target.** Explain why revealing extra information or supplying extra copies can only help a learner. Distinguish that one-way comparison from an exact equivalence of experiments under known isometries, query relabelings, and output unitaries. For an ensemble reduction, verify the conditional prior as well as the state normal form. Source-dependent coordinate choices must be included in the announced information.

**Dependencies and story role.** Uses [M03](#m03), [M06](#m06), [M08](#m08), and [M09](#m09). It joins channels, prior distributions, and stabilizer geometry into a sound reduction framework.

**Conceptual connection.** The relation $`J_xI_g=V_{g,x}J'_u`$ expresses preservation of the actual query and conditional target. Known pre- and postprocessing preserve the measure-and-prepare class as well. Counting compatible frames is what justifies a uniform reduced prior; existence of a graph representation alone does not do so.

**Source pointers.** Watrous §§2.2.2 and 3.1.2, through the [bridge](WATROUS_BRIDGE.md). Project: [quotient prior](../science/quantum_converse.md#6-resolving-every-intersection-with-the-public-measurement), [frame incidence](../science/quantum_converse.md#7-a-counted-frame-gives-the-uniform-transverse-chart), [channel transport](../science/quantum_converse.md#8-transporting-arbitrary-conditional-quantum-outputs).

<a id="m14"></a>

### M14 The complete operational question

**Central question.** What exactly is supplied, allowed, returned, and scored in the comparison?

**Understanding target.** Assemble the background into one experiment: $`k`$ copies of a fixed unknown pure stabilizer source; a source-independent public measurement of rank $`n=N-m`$; one independent verifier outcome; coherent storage until that query for both learners; either an arbitrary quantum channel or an arbitrary measure-and-prepare channel; and one pure-target overlap score. Separate training copies, total supplied qubits, retained memory, circuit operations, and repeated verification.

**Dependencies and story role.** Synthesizes [M02](#m02)–[M06](#m06) and [M08](#m08)–[M13](#m13). This ends the background phase by specifying the full question to which the following proofs apply.

**Conceptual connection.** Locate changes that would define a different task: supplying the source tableau, imposing an early report, restricting memory or report length, scoring only selected observables, or giving the learner the withheld target. Identify which bound is uniform over sources and which uses the full stabilizer prior.

**Source pointers.** Watrous §§2.1–2.3, §3.1.2, §3.2, and §6.1, through the [bridge](WATROUS_BRIDGE.md). Project: [model §§1–3](../science/model.md), [shared experiment](../science/interpretation.md#1-the-shared-experiment), [resource distinctions](../science/interpretation.md#5-physical-resource-accounting).

## Phase II: narrative/innovation

<a id="m15"></a>

### M15 An exact one-copy separation

**Central question.** Can the two output classes already be distinguished in a complete finite calculation?

**Understanding target.** Use the uniform stabilizer second moment $`\mathbb E\rho^{\otimes2}=(I+S)/[D(D+1)]`$, with $`D=2^N`$, to express the one-copy objective as a Choi score. With $`d=2^m`$, identify the Bell contribution bounded by $`d^2`$ for arbitrary channels and by $`d`$ for measure-and-prepare channels. Recover the exact values

```math
F_{\mathrm{EB},1}^{\mathrm{av}}=\frac{D/d+1}{D+1},
\qquad
F_{Q,1}^{\mathrm{av}}=\frac1d+\frac{d^2-1}{d(D+1)}.
```

**Dependencies and story role.** Uses [M04](#m04), [M05](#m05), [M07](#m07), and [M14](#m14). It begins the narrative with a finite realization of the distinction before the many-copy mechanisms.

**Conceptual connection.** For $`N=2,m=1`$, quantum-output fidelity is $`0.8`$ and classical-description fidelity is $`0.6`$. Both receive the same query; the difference follows from channel geometry. The calculation establishes these one-copy optima, while the asymptotic rates require the later proofs.

**Source pointers.** Watrous §2.2.2, §3.2, §6.1 and Exercise 6.1, through the [bridge](WATROUS_BRIDGE.md). Project: [complete one-copy proof](../science/model.md#9-exact-one-copy-comparison), [finite checks and their comparator scope](../verification/README.md#one-copy-physical-ensembles).

<a id="m16"></a>

### M16 One unknown basis for all branches

**Central question.** What relation between conditional outputs makes synthesis without source identification possible?

**Understanding target.** Derive the common-basis lemma

```math
\rho_x=U|f(x)\rangle\langle f(x)|U^\dagger
\qquad(x\in a+V),
```

where $`U`$ is one unknown output Clifford and $`f`$ is affine. Use $`\dim(L\cap W^\perp)=m+t`$ and the projection kernel $`T=L\cap W`$ to obtain the same maximal commuting output subspace for every supported outcome. Track how lifted stabilizer signs give its affine eigenvalue labels.

**Dependencies and story role.** Uses [M08](#m08)–[M10](#m10) and [M14](#m14). It identifies the structure that the quantum construction will preserve.

**Conceptual connection.** The learner knows neither $`U`$ nor $`f`$; different outcomes may even share a label. Uniform affine support and a common hidden basis provide enough structure for the next operation without supplying a classical description of that basis.

**Source pointers.** Watrous §§2.1.2 and 2.3.2 for the state and measurement framework, through the [bridge](WATROUS_BRIDGE.md). Project: [Lemma 1 and proof](../science/synthesis.md#1-one-unknown-basis-and-affine-output-labels).

<a id="m17"></a>

### M17 Adding labels through an unknown Clifford

**Central question.** Which physical operation adds computational labels while preserving their shared unknown basis?

**Understanding target.** Follow the two CNOT sweeps defining the reduced Bu–Gu–Jaffe convolution on $`K`$ output blocks. For $`K\equiv1\pmod4`$, explain why it sends the first output label to $`\sum_i z_i`$ and is covariant under the same unknown Clifford on every block. Check the Heisenberg action: $`X`$ and $`Z`$ pull back to tensor powers, while the $`Y`$ phase is $`i^{1-K}`$.

**Dependencies and story role.** Uses [M03](#m03), [M09](#m09), and [M16](#m16). It provides the quantum operation that carries the unknown conditional structure into one prediction.

**Conceptual connection.** Odd parity preserves affine offsets, but odd parity alone does not remove the complex stabilizer phase. The congruence $`1\bmod4`$ is essential. The covariance is a published ingredient; the project uses it with outcome selection. No complex-conjugated source copies are supplied.

**Source pointers.** Watrous §2.2.2 for channel and unitary representations, through the [bridge](WATROUS_BRIDGE.md). Project: [convolution circuit and phase proof](../science/synthesis.md#2-the-imported-quantum-convolution), [Bu–Gu–Jaffe attribution](../references/RELATED_WORK.md#published-convolution-and-the-conditional-synthesis-application).

<a id="m18"></a>

### M18 Why enough admissible selectors exist

**Central question.** Why do roughly $`n`$ observed branches suffice to form the requested outcome with the required phase parity?

**Understanding target.** For a fixed supported query, center the observed outcomes as $`Z_i=x_i-x`$, independent and uniform in an $`r`$-dimensional binary space. Count selectors with weight $`1\bmod4`$ and show that distinct selector indicators are pairwise independent. Use their second moment to derive

```math
\Pr(\text{no selector})
\le\frac{2^r-1}{|\mathcal A_k|}
\le2^{n-k+3}.
```

**Dependencies and story role.** Uses [M06](#m06), [M10](#m10), [M16](#m16), and [M17](#m17). It supplies the copy guarantee for the quantum mechanism.

**Conceptual connection.** The argument does not require knowing the support or observing every possible outcome. It holds for each supported query, including sources with deterministic constraints. If $`r=0`$, all branch labels coincide and one retained output is already correct.

**Source pointers.** Watrous §1.2.2 for the probability framework, through the [bridge](WATROUS_BRIDGE.md). Project: [selector count and second moment](../science/synthesis.md#4-probability-that-a-selector-exists).

<a id="m19"></a>

### M19 The complete polynomial synthesis algorithm

**Central question.** How does selector existence become an efficient learner with a scored output on every run?

**Understanding target.** Let row $`i`$ of $`X`$ be the observed outcome $`x_i^T`$. Solve $`X^Tc=x`$ and $`\mathbf1^Tc=1`$, then parameterize $`c=c_0+Bz`$. On odd-weight vectors, $`Q(c)=\sum_{i<j}c_ic_j=0`$ is exactly the weight-$`1\bmod4`$ condition. Explain why testing zero, unit vectors, and pairs of unit vectors finds a root of the restricted quadratic or proves it identically one. Combine this search with convolution and a maximally mixed failure output.

**Dependencies and story role.** Uses [M12](#m12) and [M16](#m16)–[M18](#m18). It completes the constructive half of the quantum copy law.

**Conceptual connection.** The resulting learner uses $`k=n+\lceil\log_2(1/\delta)\rceil+3`$ copies and achieves $`F_\rho\ge1-(1-2^{-m})\delta`$. A selected set of size $`K`$ uses exactly $`2m(K-1)`$ mixing CNOTs. The success flag certifies a classical algebraic condition under the exact model.

**Source pointers.** Watrous §2.2.2 for the output channel, through the [bridge](WATROUS_BRIDGE.md); the finite-field search is supplied in [algorithm](../science/synthesis.md#3-algorithm), [polynomial solver](../science/synthesis.md#5-finding-the-selector-in-polynomial-time), and [quantum resources](../science/synthesis.md#6-quantum-resources).

<a id="m20"></a>

### M20 A masked affine source

**Central question.** Which hard source hides the requested branch even though its conditional labels have a simple form?

**Understanding target.** Interpret the affine source with amplitudes $`(-1)^{q_A(u)+a^Tu}`$ and computational output label $`S^Tu+b`$. The input mask $`A,a`$ is unknown and fixed across all copies; the offset $`b`$ is independent and uniform. At a fixed query, quantum-output fidelity equals the success probability of measuring the prediction in the computational basis and guessing that label.

**Dependencies and story role.** Uses [M07](#m07), [M10](#m10), [M11](#m11), and [M14](#m14). It begins the quantum converse with an explicit statistical experiment.

**Conceptual connection.** A computational target family can still be hard when its affine rule is unknown and training access is quantum. Fixing $`b=0`$ would make the zero query trivial and destroy the required independence. The reduction composes with every output channel and therefore includes coherent processing.

**Source pointers.** Watrous §3.1.2 for state discrimination, through the [bridge](WATROUS_BRIDGE.md). Project: [affine source and static mask](../science/quantum_converse.md#2-the-affine-source-and-its-fixed-unknown-mask), [fidelity as label prediction](../science/quantum_converse.md#quantum-fidelity-becomes-label-prediction).

<a id="m21"></a>

### M21 Good Gram sectors reveal no query label

**Central question.** Why does a full-row-rank moment sector leave the fixed-query target uniformly unknown?

**Understanding target.** Average the common mask to obtain fibers of $`G=X^TX`$. In a full-row-rank fiber, show $`X'=OX`$ with $`O^TO=I`$ and $`O\mathbf1=\mathbf1`$. The sector state depends on the affine map only through $`D=X_0S+\mathbf1 b^T`$. For every fixed $`D,b`$, the same number of $`S`$ solve this equation, so $`b`$ is independent of the complete sector state.

**Dependencies and story role.** Uses [M11](#m11), [M12](#m12), and [M20](#m20). It locates the information obstruction within the hard ensemble.

**Conceptual connection.** Good-sector fidelity is exactly $`2^{-m}`$ for every possible measurement or output channel. The probability of a bad sector is the row-rank failure $`\beta_{n,k}<2^{k-n}`$. Known input translations equate every fixed-query optimum while preserving the prior and late-query timing.

**Source pointers.** Watrous §3.1.2 for indistinguishable ensembles, through the [bridge](WATROUS_BRIDGE.md). Project: [moment sectors](../science/quantum_converse.md#3-the-common-mask-average-and-its-moment-sectors), [full-rank fibers](../science/quantum_converse.md#4-what-a-full-row-rank-sector-reveals), [query independence and translation](../science/quantum_converse.md#5-fixed-query-independence-and-translation-symmetry).

<a id="m22"></a>

### M22 Transport from every stabilizer stratum

**Central question.** How can an affine-family obstruction apply to the full uniform stabilizer prior?

**Understanding target.** Reveal $`T=L\cap W`$ and its true signs, pass to $`T^\perp/T`$, and retain $`N'=N-t`$, $`n'=n-t`$, with the same $`m`$. Count $`2^{m(m+1)/2}`$ compatible transverse frames for each residual source. This constant incidence degree produces a uniform chart after a frame is announced. Revealing the chart diagonal and output graph then gives the affine family.

**Dependencies and story role.** Uses [M08](#m08), [M13](#m13), and [M21](#m21). It enlarges the converse from one hard chart to every intersection stratum in the required prior.

**Conceptual connection.** The branch identity $`J_xI_g=V_{g,x}J'_u`$ transports arbitrary output channels, branch probabilities, and fidelity without using the verifier's target. For the auxiliary exact-report problem, every admissible report and its eigenvalues must descend, including multiple correct complements. These are distinct transport obligations.

**Source pointers.** Watrous §2.2.2 for isometries and channels, through the [bridge](WATROUS_BRIDGE.md). Project: [quotient and all-report transport](../science/quantum_converse.md#6-resolving-every-intersection-with-the-public-measurement), [frame count](../science/quantum_converse.md#7-a-counted-frame-gives-the-uniform-transverse-chart), [actual branch-channel transport](../science/quantum_converse.md#8-transporting-arbitrary-conditional-quantum-outputs).

<a id="m23"></a>

### M23 The finite quantum copy law

**Central question.** Which finite obstruction survives averaging over every deterministic-intersection pattern?

**Understanding target.** Count incidences of nonzero vectors with uniform stabilizer Lagrangians to obtain

```math
\mathbb E\,2^{\dim(L\cap W)}
=1+\frac{2^n-1}{2^N+1}.
```

Average the affine bound with residual input size $`n-t`$ and recover the sharper finite theorem and its corollary $`F_Q^{\mathrm{av}}\le\min\{1,2^{-m}+2^{k-n}\}`$. Keep the baseline for fixed $`m`$, the exact zero-copy value, and the $`n=0`$ one-copy endpoint.

**Dependencies and story role.** Uses [M06](#m06), [M19](#m19), and [M20](#m20)–[M22](#m22). It completes the matching leading measured-size quantum cost.

**Conceptual connection.** The intersection moment preserves a useful finite statement even for small targets. The proof also supplies an auxiliary pre-query exact-report bound and a prime-field converse, with both Gram and linear moments for odd primes. Neither supplies the stronger qubit after-query classical-description result, which needs a different target and packing argument.

**Source pointers.** Watrous §§1.2.2 and 3.1.2 as probability and decision foundations, through the [bridge](WATROUS_BRIDGE.md). Project: [intersection moment and bounds](../science/quantum_converse.md#9-the-exact-intersection-moment-and-the-finite-bounds), [endpoints](../science/quantum_converse.md#10-consequences-and-endpoints), [prime-field scope](../science/quantum_converse.md#appendix-a-the-finite-converse-over-any-prime-field).

<a id="m24"></a>

### M24 The target that remains after the query

**Central question.** What information must a classical description retain when it is issued after the outcome is already known?

**Understanding target.** At a fixed zero query in the signed graph ensemble, identify the target as the output graph and signs $`\theta=(C,b)`$. Input graph, input signs, and cross couplings $`(A,a,S)`$ are nuisance variables. Their common tensor-power average gives orthogonal blocks $`(G,H)=(X^TX,X^TZ)`$, with target-independent weights, while $`Q=Z^TZ`$ carries the remaining character.

**Dependencies and story role.** Uses [M07](#m07), [M11](#m11), [M14](#m14), and [M20](#m20). It starts the classical converse with the exact after-query target.

**Conceptual connection.** This converse keeps the output graph hidden because it is part of the density matrix being described. It does not reuse a pre-query complementary-stabilizer reporting requirement. Input translation preserves the prior and equates fixed-query optima, so the proof respects the same late-query timing as quantum synthesis.

**Source pointers.** Watrous §3.1.2 for ensemble discrimination and §6.1 with Exercise 6.1 for the output class, through the [bridge](WATROUS_BRIDGE.md). Project: [graph target](../science/classical_converse.md#3-a-uniform-graph-ensemble-and-a-fixed-query), [nuisance blocks](../science/classical_converse.md#4-orthogonal-nuisance-blocks), [related-task distinction](../references/RELATED_WORK.md#partial-stabilizer-learning-the-timing-and-target-distinctions).

<a id="m25"></a>

### M25 Rank completion limits exact target information

**Central question.** How strongly does a copy deficit restrict the output characters attainable within a nuisance block?

**Understanding target.** From the full Gram matrix's rank at most $`k`$, eliminate a nonsingular part of $`G`$ and derive $`\mathop{\mathrm{rank}}\nolimits (Q-Q_0)\le k-\mathop{\mathrm{rank}}\nolimits G`$. Retain possible residual cross terms $`H_0\ne0`$. Count low-rank symmetric matrices and divide by the $`2^{m(m+1)/2}`$ possible graph targets to bound exact identification.

**Dependencies and story role.** Uses [M07](#m07), [M12](#m12), and [M24](#m24). It obtains the quadratic copy-deficit exponent that will withstand conversion to approximate descriptions.

**Conceptual connection.** Pad the learner to $`K=\max\{k,n\}`$ copies, use $`\mathbb E2^{\mathop{\mathrm{null}}\nolimits G}\le3`$, and give bad blocks total weight at most $`3\,2^{-s}`$. With $`d=N-K-s>0`$, every good block has exact success at most $`4(m+1)2^{-d(d+1)/2}`$. Dimension bounds apply to the actual symmetric target characters.

**Source pointers.** Watrous §3.1.2 for the discrimination step, through the [bridge](WATROUS_BRIDGE.md); the rank and probability arguments are supplied in [rank completion](../science/classical_converse.md#5-rank-completion-and-the-number-of-possible-target-characters) and [Gram nullity](../science/classical_converse.md#6-the-probability-of-a-large-gram-nullity).

<a id="m26"></a>

### M26 Arbitrary density descriptions yield short lists

**Central question.** Why does hardness of exact graph identification obstruct every high-fidelity mixed-state description?

**Understanding target.** For any density matrix $`\sigma`$, form its set of graph targets with overlap at least $`\eta`$. Use graph-state squared overlaps $`0`$ or $`2^{-\mathop{\mathrm{rank}}\nolimits (C-C')}`$ to select anchors separated by graph-rank distance greater than a cutoff $`D`$. Their overlap amplitudes are at most $`2^{-D/2}`$. If this is at most $`\eta/2`$, the Gram bound allows at most $`2/\eta`$ anchors. Cover the remaining targets by rank-distance neighborhoods, including every sign vector, to obtain the list bound $`L_m(\eta,D)`$ for arbitrary mixed $`\sigma`$.

**Dependencies and story role.** Uses [M04](#m04), [M05](#m05), [M07](#m07), and [M25](#m25). It removes any restriction to exact, pure, or stabilizer-valued reports.

**Conceptual connection.** Uniformly guessing from the reported list gives $`F_{\mathrm{EB}}(G,H)\le\eta+L_mP_{\mathrm{id}}^*(G,H)`$. Apply this conversion within good blocks. Bound fidelity by one on bad blocks before averaging, so their probability is never multiplied by the large list factor. Computing a list need not be efficient for this information bound.

**Source pointers.** Watrous §§1.1.2–1.1.3, §3.1.2, §3.2, and §6.1, through the [bridge](WATROUS_BRIDGE.md). Project: [arbitrary-density list conversion and blockwise averaging](../science/classical_converse.md#7-from-arbitrary-density-matrices-to-short-target-lists).

<a id="m27"></a>

### M27 The full classical-description copy law

**Central question.** How do the graph bound and its finite parameters establish the full-prior rate-one obstruction?

**Understanding target.** Transfer the graph bound to all pure stabilizers using a compatible frame and revealed diagonal phases, while retaining the unknown output graph. For extensive $`m`$, the total cost of discarding $`L\cap W\ne0`$ is less than $`2^{-m}`$. Choose $`s\asymp\sqrt N`$, $`\eta=2^{-\sqrt N}`$, and $`D\asymp2\sqrt N`$: the list bound satisfies $`\log_2 L_m(\eta,D)=O(N^{3/2})`$, while a fixed fractional copy deficit supplies a negative $`\Omega(N^2)`$ exponent.

**Dependencies and story role.** Uses [M13](#m13) and [M24](#m24)–[M26](#m26). It completes the arbitrary-description converse under the original prior and timing.

**Conceptual connection.** For fixed $`\beta_0,\epsilon>0`$, $`m\ge\beta_0N`$ and $`k\le(1-\epsilon)N`$ imply vanishing fidelity. Full stabilizer identification followed by conditional preparation supplies the matching leading upper bound. This upper algorithm is imported; the smaller-target converse required the separate argument.

**Source pointers.** Watrous §§2.2.2, 3.1.2 and 6.1 through the [bridge](WATROUS_BRIDGE.md). Project: [full-prior transfer](../science/classical_converse.md#8-transfer-to-all-pure-stabilizer-states), [asymptotic parameters and upper bound](../science/classical_converse.md#9-asymptotic-consequence-and-matching-rate), [full-identification source](../references/RELATED_WORK.md#ChangCaroLaroccaWest2026).

<a id="m28"></a>

### M28 The joint frontier and a growing advantage

**Central question.** What changes when the surviving target occupies different fractions of the source?

**Understanding target.** Combine both upper bounds and both converses to obtain leading rates $`1-\beta`$ for quantum outputs and $`1`$ for classical descriptions when $`m/N\to\beta\in(0,1)`$. Use $`\delta_N\to0`$ with sublinear $`\log(1/\delta_N)`$ for vanishing error at those rates. For $`n=\lceil\sqrt N\rceil`$, compare $`\sqrt N+O(\log(1/\delta))`$ quantum copies with the necessary $`N-o(N)`$ classical copies.

**Dependencies and story role.** Uses [M19](#m19), [M23](#m23), and [M27](#m27). It joins the proof mechanisms into one copy frontier.

**Conceptual connection.** Typical full-support sources assign probability $`2^{-n}`$ to a designated branch. Coherent label combination avoids waiting for that branch. Exact-match rejection sampling costs $`2^n`$ on average, while the optimal classical-description cost is linear. When $`m=o(N)`$, the quantum lower bound already gives leading rate one for a fixed positive fidelity advantage above the baseline; a positive but vanishing advantage need not require this rate.

**Source pointers.** Watrous §§1.2.2 and 3.1.2 as statistical foundations, through the [bridge](WATROUS_BRIDGE.md). Project: [joint frontier](../science/model.md#7-resulting-copy-frontier), [growing-conditioning example](../science/interpretation.md#3-a-growing-conditioning-record-with-a-growing-copy-advantage).

<a id="m29"></a>

### M29 The cost of a complete physical trial

**Central question.** What resources are needed to realize and verify the copy advantage?

**Understanding target.** Account for $`k`$ full $`N`$-qubit training preparations, $`km`$ retained output qubits, $`kn`$ recorded bits, public Clifford standardization, polynomial classical selection, and $`2m(q-1)`$ CNOTs for mixing $`q=\mathop{\mathrm{wt}}\nolimits (c)`$ selected blocks. Add one independent verifier preparation and the SWAP-comparison resources. Repeating a scored trial $`T`$ times uses $`T(k+1)`$ source preparations.

**Dependencies and story role.** Uses [M05](#m05), [M19](#m19), and [M28](#m28). It translates the copy frontier into the complete physical setting and its evidence boundaries.

**Conceptual connection.** The $`n\asymp\sqrt N`$ example still uses and retains order $`N^{3/2}`$ training qubits. Source preparation and routing are separate costs. The protocol needs no QRAM or source inverse and supplies one prediction specimen for the comparison. Finite verification covers particular algebraic and physical cases, including reflection mixing; the reduced convolution circuit is justified analytically. Algebraic success does not certify noise tolerance.

**Source pointers.** Watrous §§2.2–2.3 and §3.2 through the [bridge](WATROUS_BRIDGE.md). Project: [complete resource table](../science/interpretation.md#5-physical-resource-accounting), [verifier](../science/interpretation.md#6-fidelity-and-the-physical-verifier), [scope](../science/interpretation.md#8-what-the-result-does-and-does-not-establish), [verification scope](../verification/README.md#scope-limits).

<a id="m30"></a>

### M30 The complete conditional-learning story

**Central question.** How do the experiment, mechanism, bounds, and resources support one coherent conclusion?

**Understanding target.** Explain the whole project from the shared late-query experiment through its two output classes. Trace quantum achievability through affine branches, phase-correct convolution, and polynomial selector search; trace its necessity through masked Gram sectors and full-prior transport. Trace the stronger description cost through the hidden output graph, symmetric completion, and arbitrary-density packing. Integrate the finite one-copy example, the matching leading rates, the growing-conditioning regime, and the full preparation-and-verification cost.

**Dependencies and story role.** Synthesizes [M14](#m14), [M15](#m15), [M19](#m19), [M23](#m23), and [M27](#m27)–[M29](#m29). This completes the narrative phase at the level of the entire contribution.

**Conceptual connection.** Unknown quantum structure can pass from retained examples into one conditional specimen at a lower copy rate than any classical density description of that specimen. The conclusion uses an exact pure-qubit-stabilizer promise and unrestricted coherent storage; it establishes a copy comparison, not a runtime or noise-robustness theorem. Attribute the convolution, copy symmetries, quotient tools, and full-learning upper bound to their sources while locating the matched conditional-output comparison in the complete argument.

**Source pointers.** Watrous §§2.1–2.3, §3.1.2, §3.2, and §6.1 with Exercise 6.1, through the [bridge](WATROUS_BRIDGE.md). Project: [canonical model and theorem statements](../science/model.md), [synthesis](../science/synthesis.md), [quantum converse](../science/quantum_converse.md), [classical converse](../science/classical_converse.md), [physical interpretation](../science/interpretation.md), and [attribution](../references/RELATED_WORK.md#attribution-and-limitations).
