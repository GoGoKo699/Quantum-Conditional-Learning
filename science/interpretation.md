# Physical meaning and resource costs

Physical conditional prediction can use fewer source copies than producing a classical description of the same prediction. For pure stabilizer sources, the leading copy cost of a quantum output is the number $`n=N-m`$ of measured constraints. When the retained target has an extensive number of qubits, a classical density description requires the full source-size rate $`N`$, even if its learner keeps quantum data until the same query arrives.

The distinction concerns how unknown quantum information reaches the output. Both learners receive identical physical training copies, have the same query timing, and may use collective quantum operations. The formal task is specified in the [model](model.md), with proofs in [synthesis](synthesis.md), the [quantum converse](quantum_converse.md), and the [classical converse](classical_converse.md).

## 1. The shared experiment

An unknown fixed pure $`N`$-qubit stabilizer state supplies $`k`$ independent training preparations. A public set of $`n`$ independent commuting Pauli constraints specifies a measurement. On one independent verifier preparation, that measurement produces a classical outcome $`x`$ and a pure conditional $`m=N-n`$-qubit state $`\rho_x`$. The learner receives $`x`$ and must provide one prediction for $`\rho_x`$.

The verifier's conditional quantum system stays with the verifier. Giving it to the learner would supply the requested output directly.

| Resource or action | Quantum output | Classical density description |
|---|---|---|
| Training data | $`k`$ copies of the same unknown source | The same $`k`$ copies |
| Query | The independent verifier's classical outcome $`x`$ | The same outcome, at the same time |
| Storage before the query | Arbitrary quantum storage is allowed | Arbitrary quantum storage is allowed |
| Processing after the query | An arbitrary quantum channel | An arbitrary collective POVM and classical processing |
| Final prediction | One $`m`$-qubit state | Any described density matrix, subsequently prepared |
| Score | $`\operatorname{Tr}(\sigma\rho_x)`$ | The same score |

The classical-description comparator is an entanglement-breaking, or measure-and-prepare, channel from the training systems to the output, for each fixed $`x`$. It has no bound on description length, precision, computation, or state-preparation complexity. It may describe a mixed state and need not report a stabilizer. In particular, this comparator can itself use a quantum computer and coherent quantum memory before its final measurement.

## 2. Copy thresholds

For every pure stabilizer source and every supported test outcome, the quantum construction uses

```math
k=n+\left\lceil\log_2\frac1\delta\right\rceil+3
```

training copies and succeeds with probability at least $`1-\delta`$, for $`0<\delta<1`$. Success is heralded by a classical calculation, and the output on success is exactly $`\rho_x`$. Returning the maximally mixed state on failure gives

```math
F_\rho\ge1-\delta(1-2^{-m}).
```

The uniform-prior [quantum converse](quantum_converse.md) gives, for any learner, with the fixed public measurement suppressed in the notation,

```math
F_Q^{\mathrm{av}}(N,m,k)
\le\min\{1,\;2^{-m}+2^{k-n}\}.
```

Thus achieving a fixed fidelity advantage above the random-output baseline requires $`n-O(1)`$ copies. The additive constant and the dependence on very small failure probabilities are not optimized by these bounds.

For classical descriptions, the [converse](classical_converse.md) states that, for every fixed $`\beta_0>0`$ and $`\epsilon>0`$,

```math
m\ge\beta_0N,\quad k\le(1-\epsilon)N
\quad\Longrightarrow\quad
F_{\mathrm{EB}}^{\mathrm{av}}(N,m,k)\longrightarrow0.
```

A matching leading upper bound follows by learning the full source and calculating its conditional state. [Chang–Caro–Larocca–West](../references/RELATED_WORK.md#ChangCaroLaroccaWest2026) give full stabilizer identification from $`N+\lceil\log_2(1/\delta)\rceil+4`$ copies for $`0<\delta<1/8`$.

The resulting rates are:

| Output regime | Quantum-output copy cost | Classical-description copy cost |
|---|---|---|
| $`m/N\to\beta\in(0,1)`$ | Leading rate $`k/N=1-\beta`$ | Leading rate $`k/N=1`$ |
| $`n=\lceil\sqrt N\rceil`$, $`m=N-n`$ | $`\sqrt N+O(\log(1/\delta))`$ | $`N-o(N)`$ is necessary for fixed positive fidelity |
| $`m=o(N)`$ | Leading rate one for a fixed advantage above $`2^{-m}`$ | Full learning gives leading rate one |

Vanishing error is achievable at the displayed leading rates by choosing $`\delta_N\to0`$ with $`\log(1/\delta_N)=o(N)`$, for example $`\delta_N=1/N`$. The lower bounds are uniform-prior statements and therefore also constrain every-source guarantees; the constructive upper bounds hold for every source.

When $`n=0`$, one training copy is already an exact quantum prediction. The growing-conditioning regime in the next section has $`n\to\infty`$ and an unbounded ratio between the required copy counts.

## 3. A growing conditioning record with a growing copy advantage

Take

```math
n=\lceil\sqrt N\rceil,\qquad m=N-\lceil\sqrt N\rceil.
```

For fixed target error, the quantum learner uses $`\sqrt N+O(1)`$ full $`N`$-qubit preparations. Every classical-description learner with fixed positive mean fidelity needs $`N-o(N)`$ such preparations. The ratio grows as $`\sqrt N`$.

The conditioning record itself also grows. For a uniform stabilizer source, let $`L`$ be its unsigned stabilizer space and $`W`$ the public measurement subspace. The [intersection estimate](classical_converse.md#8-transfer-to-all-pure-stabilizer-states) gives

```math
\Pr(L\cap W\ne\{0\})
\le\frac{2^n-1}{2^N+1}<2^{-m}.
```

When the intersection is zero, all $`2^n`$ measurement outcomes occur uniformly. A designated outcome then has probability $`2^{-n}`$. Repeatedly measuring fresh training copies until that outcome appears takes $`2^n`$ preparations on average.

The coherent construction combines branches with different observed labels, using their known binary structure. This avoids waiting for an exact matching label. Rejection sampling is a simple comparison procedure: the optimal classical-description cost is linear in $`N`$, as the full-learning upper bound shows.

The source preparations remain large. In this example the quantum learner receives $`\Theta(N^{3/2})`$ training qubits in total, and its stated implementation retains $`\Theta(N^{3/2})`$ output qubits until the query. The advantage in source copies comes with substantial coherent storage.

## 4. What the synthesis operation preserves

After standardizing the public measurement, the supported outcomes form an affine binary space. The conditional outputs have the form

```math
\rho_x=U|f(x)\rangle\langle f(x)|U^\dagger,
```

where $`U`$ is one fixed unknown output Clifford and $`f`$ is an affine label map. Neither needs to be learned.

Measure the public constraints on each training copy, record the outcomes $`x_1,\ldots,x_k`$, and retain their output systems. After receiving $`x`$, find a binary coefficient vector satisfying

```math
\sum_i c_i x_i=x,\qquad
\operatorname{wt}(c)\equiv1\pmod4.
```

The odd coefficient sum preserves the affine label relation. The stronger weight congruence makes the selected-copy convolution covariant under the same unknown Clifford, including its phase gates. Applying this convolution to the selected outputs gives exactly the requested branch. The convolution and its covariance are established primitives from [Bu–Gu–Jaffe](../references/RELATED_WORK.md#BuGuJaffe2025); the [synthesis proof](synthesis.md) supplies the outcome-selection guarantee, polynomial coefficient search, and explicit circuit.

This operation carries unknown quantum structure from the stored specimens into the requested output. It does not first reconstruct the unknown basis. The classical converse shows that converting the final prediction into any classical density description retains the larger copy requirement, even with the same late query and unrestricted collective processing.

## 5. Physical resource accounting

The following counts describe the constructive quantum learner. They use an unrestricted-connectivity gate model; any hardware routing must be added.

| Resource | Cost and meaning |
|---|---|
| Source preparations | $`k`$ independent full $`N`$-qubit training preparations |
| Independent test preparation | One additional full $`N`$-qubit preparation per scored trial |
| Supplied source qubits | $`(k+1)N`$ over a training-and-test trial, including the verifier copy |
| Public measurement standardization | If needed, a known Clifford taking the constraints to input $`Z`$ measurements; $`O(N^2)`$ elementary Clifford gates per copy suffice in the unrestricted-connectivity model |
| Training measurements | $`kn`$ single-qubit computational measurements after standardization |
| Retained training outputs | $`km`$ coherent qubits until the query, together with $`kn`$ recorded outcome bits |
| Query | $`n`$ classical outcome bits from the verifier; only $`r\le n`$ may be independent for a particular source |
| Classical selection | Binary Gaussian elimination and a quadratic Boolean equation, using polynomial time and explicit classical matrix storage |
| Quantum mixing | For $`q=\operatorname{wt}(c)\equiv1\pmod4`$ selected blocks, exactly $`2m(q-1)`$ CNOTs, at most $`2m(k-1)`$ |
| Mixing depth and ancillas | A direct depth $`2(q-1)`$ with the $`m`$ coordinates in parallel and the required connections; no added synthesis ancillas |
| Prediction | One unknown $`m`$-qubit specimen |

These counts assume access to each full training copy while applying the public measurement circuit. The $`km`$ figure describes what remains after those measurements. No claim of optimal quantum memory or optimal circuit depth is made.

A source-preparation circuit is a separate physical cost. If one full preparation costs $`G_{\mathrm{src}}`$ gates in a chosen implementation, a scored trial incurs $`(k+1)G_{\mathrm{src}}`$ source gates in addition to the public measurement, synthesis, and verification operations. A secret preparation description may be held by the source or verifier; the learner's input is the physical copies.

The procedure uses no QRAM, no amplitude-encoding access to a classical dataset, no controlled or inverse call to the source, and no copy of the unknown preparation circuit. Its input is quantum from the outset. A claim about loading a classical dataset or about complete execution time would require an additional model.

## 6. Fidelity and the physical verifier

The mathematical score is

```math
F=\mathbb E\,\operatorname{Tr}(\sigma\rho_x).
```

If the verifier has one unknown target specimen and one predicted specimen, an ordinary SWAP test accepts with probability

```math
p_{\mathrm{acc}}=\frac{1+F}{2}.
```

Thus fidelity is the affine-rescaled mean comparison statistic. It is not literally the SWAP acceptance probability. The maximally mixed prediction has $`F=2^{-m}`$ and acceptance $`(1+2^{-m})/2`$; for a one-qubit target these values are $`1/2`$ and $`3/4`$, respectively.

An ordinary circuit implementation uses one control ancilla, Hadamard gates, and $`m`$ controlled swaps between the predicted and verifier registers. These verifier resources are additional to the synthesis circuit, which uses no added ancillas.

One scored comparison yields one random bit. Estimating a mean fidelity requires repeated independent trials with fresh training and test preparations. For $`T`$ such trials, the source count is $`T(k+1)`$; the required $`T`$ depends on the chosen statistical precision and confidence. The copy theorems specify the training cost of a prediction, rather than certifying a high fidelity from a single comparison.

## 7. An exact finite comparison at one copy

The distinction between quantum and measure-and-prepare outputs is visible even before taking a many-copy limit. Under the full uniform stabilizer prior, the exact one-copy optima are

```math
F_{\mathrm{EB}}^{\mathrm{av}}(N,m,1)
=\frac{2^n+1}{2^N+1},
\qquad
F_Q^{\mathrm{av}}(N,m,1)
=2^{-m}+\frac{2^{2m}-1}{2^m(2^N+1)}.
```

Their excesses above the random-output baseline obey

```math
\frac{F_Q^{\mathrm{av}}(N,m,1)-2^{-m}}
{F_{\mathrm{EB}}^{\mathrm{av}}(N,m,1)-2^{-m}}
=2^m+1.
```

The [one-copy calculation](model.md#9-exact-one-copy-comparison) proves both optima using the stabilizer second moment and the different Choi constraints for arbitrary and entanglement-breaking channels. This is a comparison with the query supplied at the same time to both learners. The many-copy rates require the separate converse and synthesis arguments above.

## 8. What the result does and does not establish

**The output is one consumable quantum prediction.** The selected training systems are processed and discarded as needed. The learner does not preserve its training set while adding another full source copy. The task differs from cloning, whose output includes additional copies of a specified source state, and from producing a reusable classical model. Related task definitions are compared in [related work](../references/RELATED_WORK.md).

**The classical lower bound is an information bound.** It allows unlimited classical calculation and arbitrary collective quantum measurements after the query. Classical simulation of a stabilizer circuit from a known tableau does not provide the unknown tableau in this experiment. The separation is a source-copy comparison between output channel classes; it supplies no classical-versus-quantum running-time lower bound.

**One fidelity objective is being studied.** A classical description can be reused to prepare further states, but the converse already applies when only one prediction for the supplied outcome is scored. Conversely, the quantum construction does not provide a reusable model for arbitrary future queries. Replacing global conditional-state fidelity by estimates of a fixed collection of observables changes the learning task. The present bounds do not establish the sample complexity of such observable-estimation or classical-shadow tasks.

**The source promise is exact.** The construction applies to every pure qubit stabilizer state with the specified commuting measurement. It relies on accurate source preparations, measurements, coherent storage, and mixing gates. Its herald reports whether the classical coefficient equations have a solution under that model; it does not diagnose physical noise or certify the actual prepared state. No robustness theorem for mixed or noisy sources, no restricted-connectivity implementation bound, and no general all-prime classical-output separation is claimed here.

**The asymptotic thresholds have a specified range.** The classical converse covers $`m`$ bounded below by a positive fraction of $`N`$. The quantum bound also covers small targets, where a fixed fidelity advantage can still require nearly $`N`$ copies. The explicit upper and lower bounds determine leading copy rates and the growing advantage in Section 3; they leave optimal additive constants and detailed transition curves open.

The [verification notes](../verification/README.md) identify the finite calculations and circuit checks accompanying these proofs. Their scope is the stated ideal model and implementation.
