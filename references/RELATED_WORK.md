# Related work and scope

## The operational comparison

Let an unknown pure stabilizer state occupy $`N`$ qubits, and let a public commuting Pauli measurement have $`n=N-m`$ independent constraints. The learner receives $`k`$ identical training copies. A separate test copy is measured, and the learner receives its classical outcome $`x`$, but not its remaining $`m`$-qubit system. The task is to predict that conditional state with mean fidelity.

Both learners may retain every training copy until $`x`$ arrives and then perform arbitrary joint quantum operations. A **quantum-output learner** supplies an $`m`$-qubit state directly. A **classical-description learner** supplies an arbitrarily long and precise classical description of any density matrix, from which its prediction can be prepared. For each fixed $`x`$, the latter is a measure-and-prepare, or entanglement-breaking, channel. Its measurements, classical computation, and report length are unrestricted.

The result considered here separates the leading copy costs when $`m/N\to\beta\in(0,1)`$: physical conditional-state synthesis has rate $`1-\beta`$, while classical density-matrix descriptions issued after the same outcome require rate $`1`$ for nonvanishing fidelity. The constructive guarantee is uniform over pure stabilizer sources. The converse uses the uniform prior over all pure stabilizers and therefore also rules out a better worst-case guarantee.

This comparison concerns the resource carried by the final output. The quantum protocol consumes retained training systems to supply one conditional specimen; it does not produce a reusable classical model or claim a running-time advantage over unrestricted classical computation.

## How the cited results enter

| Reference | Established result used or compared | Scope relative to the present task |
| --- | --- | --- |
| [Bu–Gu–Jaffe 2023](#BuGuJaffe2023) | Discrete quantum convolution and stabilizer closure | Foundational convolution framework |
| [Bu–Gu–Jaffe 2025](#BuGuJaffe2025) | Exact Clifford covariance of qubit convolution | Supplies the synthesis primitive |
| [Gross–Nezami–Walter 2021](#GrossNezamiWalter2021) | Clifford commutants and stabilizer copy symmetries | Supplies an alternative mixing construction |
| [Hayashi–Lu 2026](#HayashiLu2026Partial) | Finite quotient discrimination, weighted completion counts, and partial-learning converses | Its main report precedes the measurement outcome |
| [Chang–Caro–Larocca–West 2026](#ChangCaroLaroccaWest2026) | Sample-optimal full stabilizer identification | Supplies the classical-description upper bound |
| [Arunachalam–Schatzki 2026](#ArunachalamSchatzki2026) | Gram-orbit tools and learning/testing with limited quantum memory | The memory constraint differs from the unrestricted learners here |
| [McGinley 2024](#McGinley2024) | Inference of postmeasurement ensemble properties | Its general obstruction assumes arbitrary relabeling invariance |

### Published convolution and the conditional synthesis application

Bu, Gu, and Jaffe introduced a discrete convolution framework with closure of stabilizer states in [their 2023 paper](https://arxiv.org/abs/2302.07841v3). The precise qubit operation used here is in [their 2025 paper, arXiv version 2](https://arxiv.org/html/2306.09292v2): Definition 7, Lemma 9 and Equation (15), Proposition 13 and Equation (23), and Theorem 51 and Equation (63).

For $`K\equiv1\pmod4`$, that theorem gives covariance under the **same unknown Clifford** $`U`$. Combining it with addition of computational-basis labels yields

```math
\boxtimes_K\!\left(\bigotimes_{i=1}^{K}
U|z_i\rangle\!\langle z_i|U^\dagger\right)
=
U\left|\sum_i z_i\right\rangle
\left\langle\sum_i z_i\right|U^\dagger .
```

Thus unknown-basis label addition is an immediate consequence of a published channel. The application here uses the affine dependence of conditional stabilizer labels on $`x`$: select observed outcomes summing to $`x`$, with subset size $`1\bmod4`$, then convolve their retained outputs. The copy guarantee and efficient selection belong to this conditional-task application.

The congruence condition removes the transpose sign present for $`K\equiv3\pmod4`$. Arbitrary odd subset size would not suffice for unknown complex stabilizers. The protocol uses no complex-conjugated source copies.

### Stabilizer copy symmetries

[Gross, Nezami, and Walter](https://arxiv.org/html/1712.08628v3) develop the commutant of Clifford tensor powers. Lemma 4.3 gives the relevant commutation property, and Equation (4.13) states that stochastic orthogonal transformations preserve every stabilizer tensor power. Their six-copy qubit anti-identity provides a concrete example.

These symmetries give an alternative route to conditional mixing. The convolution implementation above only needs one reduced output block, so it avoids extending every selected coefficient vector to a transformation preserving the complete product family. Neither the copy symmetry nor the Clifford commutant is claimed as a new result here.

### Partial stabilizer learning: the timing and target distinctions

[Hayashi and Lu, arXiv:2609.13923v1](https://arxiv.org/html/2609.13923v1), study complementary stabilizers and eigenvalues reported before the prescribed measurement outcome. Their extensive-target theorem gives leading copy rate one. Section 4 supplies transverse-frame incidence tools; Theorem 8.11 gives an abstract finite quotient optimum; Theorem 9.1 supplies the weighted completion reduction; Section 11 compares graded scores with exact-label lists.

Their finite formulas also imply some sublinear-target consequences, including ordinary single-output barriers after an elementary wrong-report score bound. Section 13.3's excluded asymptotic regime should therefore not be interpreted as establishing novelty of every small-target consequence.

The present classical comparator responds **after** the query and may describe an arbitrary density matrix. In a graph chart at fixed query, its exact target is the output graph and signs $`(C,b)`$, while input and cross terms are nuisance. This is a different quotient. The converse applies the existing framework to that target and extends the comparison to arbitrary density descriptions through packing. The resulting statement is not a direct restatement of their pre-outcome theorem.

### Full identification supplies the classical upper bound

[Chang, Caro, Larocca, and West, arXiv:2609.10974v1](https://arxiv.org/abs/2609.10974v1), prove that full $`N`$-qubit stabilizer identification can be achieved in polynomial time with

```math
N+\left\lceil\log_2(1/\delta)\right\rceil+4
```

copies for $`0<\delta<1/8`$, and give a matching leading lower bound. Their full-identification algorithm supplies the rate-one upper bound here: identify the source, then compute its conditional state from the public measurement and observed outcome. This imported algorithm does not itself establish the converse for the smaller conditional target.

### Limited-memory learning is a different restriction

[Arunachalam and Schatzki, arXiv:2607.02444v2](https://arxiv.org/html/2607.02444v2), study testing and learning with restricted coherent memory between measurements. Lemma 2.9 supplies the full-rank binary Gram/orthogonal-orbit relation; their quadratic-phase averaging methods are relevant to the moment organization used here.

Their memory-dependent lower bounds do not directly apply to this comparison: both learners here may retain and process all training systems jointly. The restriction distinguishing the learners is the final classical description, rather than the amount of quantum memory available while learning. The cited version is the revision of 5 October 2026.

### Postselection-free ensemble inference

[McGinley, arXiv:2310.04156v2](https://arxiv.org/html/2310.04156v2), studies properties of ensembles of postmeasurement states from sampled outcome/state pairs. Theorem 2 and Equation (77) give a collective-sample obstruction for strategies invariant under arbitrary permutations of outcome labels, termed “simulation-free” in that paper.

The synthesis protocol here uses known binary linear relations among Pauli measurement outcomes, so it does not satisfy that invariance hypothesis. This distinguishes the general obstruction from the stabilizer-specific protocol. The target also differs: supplying a requested conditional state is distinct from estimating an ensemble property.

## Attribution and limitations

The proposed contribution is the combined conditional-output comparison with matched copy access and query timing. The quantum convolution, Clifford copy symmetries, finite quotient framework, and full-identification upper bound are established results credited above.

The cited versions do not state this combined quantum-output versus after-query classical-description separation. That scope assessment is limited to these primary texts; it is not an exhaustive priority claim and does not cover subsequent revisions or unpublished work. The main separation is for qubits under an exact pure-stabilizer promise. Optimal additive copy constants, critical-window behavior, robustness to physical noise, and an all-prime classical-output separation are outside the stated result.

## Bibliographic records

The anchors below match the keys in [references.bib](references.bib). Version-specific arXiv links identify the texts used for theorem numbering. Metadata were checked against the primary arXiv records on 18 October 2026.

<a id="BuGuJaffe2023"></a>

**BuGuJaffe2023.** Kaifeng Bu, Weichen Gu, and Arthur Jaffe. “Quantum Entropy and Central Limit Theorem.” *Proceedings of the National Academy of Sciences* **120**(25), e2304589120 (2023). [DOI](https://doi.org/10.1073/pnas.2304589120). [arXiv:2302.07841v3](https://arxiv.org/abs/2302.07841v3), revised 18 June 2023.

<a id="BuGuJaffe2025"></a>

**BuGuJaffe2025.** Kaifeng Bu, Weichen Gu, and Arthur Jaffe. “Stabilizer Testing and Magic Entropy via Quantum Fourier Analysis.” *Communications in Mathematical Physics* **406**, 236 (2025). [DOI](https://doi.org/10.1007/s00220-025-05421-3). [arXiv:2306.09292v2](https://arxiv.org/abs/2306.09292v2), revised 11 August 2025; first posted in 2023.

<a id="GrossNezamiWalter2021"></a>

**GrossNezamiWalter2021.** David Gross, Sepehr Nezami, and Michael Walter. “Schur-Weyl Duality for the Clifford Group with Applications: Property Testing, a Robust Hudson Theorem, and de Finetti Representations.” *Communications in Mathematical Physics* **385**, 1325–1393 (2021). [DOI](https://doi.org/10.1007/s00220-021-04118-7). [arXiv:1712.08628v3](https://arxiv.org/abs/1712.08628v3), revised 16 January 2021.

<a id="HayashiLu2026Partial"></a>

**HayashiLu2026Partial.** Masahito Hayashi and Yimin Lu. “Partial Stabilizer Learning under Fixed Commuting Constraints and the Absence of a Copy-Rate Discount.” [arXiv:2609.13923v1](https://arxiv.org/abs/2609.13923v1), 12 September 2026.

<a id="ChangCaroLaroccaWest2026"></a>

**ChangCaroLaroccaWest2026.** Rebecca Chang, Matthias C. Caro, Martin Larocca, and Maxwell West. “Sample-optimal learning of stabilizer states.” [arXiv:2609.10974v1](https://arxiv.org/abs/2609.10974v1), 10 September 2026.

<a id="ArunachalamSchatzki2026"></a>

**ArunachalamSchatzki2026.** Srinivasan Arunachalam and Louis Schatzki. “Optimal Stabilizer Testing and Learning with Limited Quantum Memory.” [arXiv:2607.02444v2](https://arxiv.org/abs/2607.02444v2), revised 5 October 2026.

<a id="McGinley2024"></a>

**McGinley2024.** Max McGinley. “Postselection-free learning of measurement-induced quantum dynamics.” *PRX Quantum* **5**, 020347 (2024). [DOI](https://doi.org/10.1103/PRXQuantum.5.020347). [arXiv:2310.04156v2](https://arxiv.org/abs/2310.04156v2), revised 18 July 2024.
