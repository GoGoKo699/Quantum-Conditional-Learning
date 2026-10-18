# Quantum Conditional Learning

**How many quantum examples are needed to supply a conditional state, and how does the cost change when the prediction must first be described classically?**

An unknown pure $`N`$-qubit stabilizer supplies independent training copies. A fixed public measurement reads $`n=N-m`$ commuting Pauli observables on a fresh verifier copy. The learner receives the classical outcome and must supply the conditional state on the remaining $`m`$ qubits. Both output classes may keep their training quantum data until the same outcome arrives.

| Output channel | Training-copy result |
|---|---|
| Direct quantum processing | $`n+\lceil\log_2(1/\delta)\rceil+3`$ copies suffice, with exact output on a heralded event of probability at least $`1-\delta`$ |
| Arbitrary classical density description followed by preparation | $`N-o(N)`$ copies are necessary for any constant fidelity when $`m`$ is a positive fraction of $`N`$ |

The quantum converse is

```math
F_Q^{\mathrm{av}}(N,m,k;W)
\le\min\{1,\;2^{-m}+2^{k-(N-m)}\}.
```

It matches the leading measured-size term of the constructive upper bound. The classical-output lower bound allows arbitrary collective measurements, unlimited classical record length and precision, arbitrary mixed predictions, and measurements chosen after the outcome is supplied. Full stabilizer identification attains its leading rate.

For $`m/N\to\beta\in(0,1)`$, the leading copy rates per source qubit are **$`1-\beta`$ for quantum output** and **$`1`$ for classical descriptions**. Taking $`n=\lceil\sqrt N\rceil`$ gives $`\sqrt N+O(\log(1/\delta))`$ versus $`N-o(N)`$ training copies. A typical specified measurement branch is rare, but different observed branches can be combined coherently to supply it.

## Read the science

Start with [the operational model and exact theorems](science/model.md). The construction selects an affine combination of observed outcomes and applies a published Clifford-covariant quantum convolution. The two converse arguments quantify what can be predicted before enough constraints or a sufficient classical description can be recovered.

| Scientific question | Authoritative account |
|---|---|
| What access, timing, outputs and fidelity are compared? | [Model and theorem statements](science/model.md) |
| How can an unknown conditional branch be supplied efficiently? | [Synthesis algorithm and success bound](science/synthesis.md) |
| Why does quantum output need the measured-size copy cost? | [Quantum converse and full-prior reduction](science/quantum_converse.md) |
| Why does every classical density description retain the full rate? | [Classical-output converse](science/classical_converse.md) |
| What do the copy savings mean physically? | [Resources and interpretation](science/interpretation.md) |
| How do the output classes differ with one training copy? | [Exact one-copy comparison](science/model.md#9-exact-one-copy-comparison) |
| Which methods are established, and what is the proposed contribution? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| What has been checked computationally? | [Verification](verification/README.md) |

The construction uses [Bu–Gu–Jaffe's convolution](references/RELATED_WORK.md#BuGuJaffe2025); an alternative uses [Gross–Nezami–Walter's copy symmetries](references/RELATED_WORK.md#GrossNezamiWalter2021). The converse develops a conditional-output application of [Hayashi–Lu's finite quotient and completion framework](references/RELATED_WORK.md#HayashiLu2026Partial). The proposed contribution is the matched conditional-learning copy separation. These imported methods and the scope of the comparison are part of the scientific account.

## Reproduce the finite checks

The [verification guide](verification/README.md) specifies dependencies and expected outputs. From the repository root, run:

```bash
python3 verification/run_all.py
```

The checks cover finite-field moments, quotient/frame and report transport, exact one-copy channel witnesses, and conditional synthesis on complete small stabilizer ensembles. They test concrete implementations and finite cases. The general copy laws are established by the written proofs.

## Physical scope

The source promise is an ideal pure stabilizer state and the public measurements are exact. The quantum protocol retains $`km`$ output qubits, stores $`kn`$ outcome bits, and consumes training systems to return one prediction. Its final mixing uses at most $`2m(k-1)`$ CNOTs, in addition to state preparations and public-measurement standardization. It assumes no QRAM or inverse source circuit.

The theoretical score is conditional-state fidelity. Comparing one unknown prediction with one independently prepared unknown target through a SWAP test has acceptance $`(1+F)/2`$; the verifier preparation and any repetitions are separate resources. The finite bounds determine leading copy costs, without asserting optimal critical-window constants or robustness to arbitrary physical noise.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
