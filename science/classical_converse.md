# Classical descriptions after the query

## 1. Statement and scope

An unknown pure stabilizer state on $`N`$ qubits supplies $`k`$ independent training copies. A public measurement of $`n=N-m`$ independent commuting Pauli observables is performed on an independent verifier copy. Its classical outcome $`x`$ is then supplied to the learner; the verifier keeps the conditional $`m`$-qubit target state $`\rho_x`$.

The learner may retain all training systems until $`x`$ arrives and then perform any collective measurement. Its output is an arbitrary classical description of a density matrix $`\sigma`$, which may subsequently be prepared. Classical computation, description length, numerical precision, and preparation complexity are unrestricted. Equivalently, for each supplied $`x`$, the channel from the training systems to the predicted state is **entanglement breaking**, or measure and prepare. The only distinction from a quantum-output learner is whether quantum information from the training systems can pass into the final output without this classical description.

Let $`F_{\mathrm{EB}}^{\mathrm{av}}(N,m,k)`$ be the supremum of

```math
F=\mathbb E_{\rho,x,\mathrm{learner}}\mathop{\mathrm{Tr}}\nolimits (\sigma\rho_x)
```

over these learners, with the source uniform over all pure $`N`$-qubit stabilizer states. The fixed public measurement is suppressed in this notation; Clifford standardization makes its rank the relevant parameter. The timing and source access are those of the [model](model.md).

**Theorem.** Fix $`\beta_0\in(0,1]`$ and $`\epsilon\in(0,1)`$. Uniformly over integer sequences satisfying

```math
1\le m\le N,\qquad m\ge\beta_0N,\qquad
0\le k\le(1-\epsilon)N,
```

we have

```math
F_{\mathrm{EB}}^{\mathrm{av}}(N,m,k)\longrightarrow0
\qquad\text{as }N\longrightarrow\infty.
```

Thus any classical-description method whose mean fidelity stays above a fixed positive constant requires $`N-o(N)`$ training copies when the target occupies a positive fraction of the source. The same necessary condition holds for a fidelity guarantee on every source, since a worst-case guarantee is also a guarantee under the uniform prior.

The proof below gives a finite bound. Its ingredients are a weighted moment decomposition, a rank constraint on the target character, and a packing argument for arbitrary density matrices. The finite quotient viewpoint is related to [Hayashi–Lu](../references/RELATED_WORK.md#HayashiLu2026Partial); the argument here explicitly keeps the query timing and allows arbitrary density descriptions.

## 2. An explicit finite bound

Put

```math
n=N-m,\qquad K=\max\{k,n\},\qquad
e_{N,m}=\frac{2^n-1}{2^N+1}.
```

Choose an integer $`s\ge1`$, a real number $`\eta\in(0,1]`$, and an integer $`D`$ such that

```math
d=N-K-s>0,\qquad 0\le D\le m,\qquad
2^{-D/2}\le\frac{\eta}{2}.
```

Define

```math
L_m(\eta,D)
=\frac{8(D+1)}{\eta}\,
2^{\,m+D(2m-D+1)/2}.
```

Then

```math
F_{\mathrm{EB}}^{\mathrm{av}}(N,m,k)
\le
\min\!\left\{
1,\;
e_{N,m}+3\,2^{-s}+\eta
+4(m+1)L_m(\eta,D)\,2^{-d(d+1)/2}
\right\}.
```

In particular, $`e_{N,m}\lt 2^{-m}`$. When no parameters satisfy the displayed conditions, this expression makes no claim beyond the bound $`F\le1`$. The constants are convenient uniform bounds; no optimal fidelity exponent or critical-window formula is asserted.

## 3. A uniform graph ensemble and a fixed query

We first prove the bound for a real signed graph ensemble. Write the computational coordinates as $`u\in\mathbb F_2^n`$ and $`z\in\mathbb F_2^m`$. All linear algebra in this proof is over $`\mathbb F_2`$.

Let $`A`$ and $`C`$ be independent uniform zero-diagonal symmetric matrices of sizes $`n`$ and $`m`$. Let $`S\in\mathbb F_2^{n\times m}`$, $`a\in\mathbb F_2^n`$, and $`b\in\mathbb F_2^m`$ be independent and uniform. For a zero-diagonal symmetric matrix $`B`$, set

```math
q_B(v)=\sum_{i\lt j}B_{ij}v_iv_j.
```

The source is

```math
|\psi_{A,a,S,C,b}\rangle
=2^{-N/2}\sum_{u,z}
(-1)^{q_A(u)+a\cdot u+u^{\mathsf T}Sz+q_C(z)+b\cdot z}
|u,z\rangle.
```

Measuring the input qubits in the computational basis gives a uniform outcome $`x`$, independent of all the parameters. Its conditional output is

```math
|G_{C,b+S^{\mathsf T}x}\rangle
=2^{-m/2}\sum_z
(-1)^{q_C(z)+(b+S^{\mathsf T}x)\cdot z}|z\rangle.
```

For each fixed supplied $`x`$, translating the input coordinates by $`x`$ maps the source prior bijectively to itself. Indeed, apart from a global phase, it replaces $`a`$ by $`a+Ax`$ and $`b`$ by $`b+S^{\mathsf T}x`$. This translation is a known unitary that a learner can apply after receiving the query. Therefore the optimal mean fidelity at every fixed $`x`$ equals that at $`x=0`$.

It suffices to predict the target

```math
\tau_\theta=|G_{C,b}\rangle\langle G_{C,b}|,
\qquad \theta=(C,b).
```

There are

```math
M_m=2^{m(m-1)/2+m}=2^{m(m+1)/2}
```

equally likely, distinct targets. The parameters $`(A,a,S)`$ are nuisance parameters: they affect the training state but are not part of this target.

## 4. Orthogonal nuisance blocks

For the moment consider $`k`$ training copies without padding. Index their computational basis by matrices

```math
X\in\mathbb F_2^{k\times n},\qquad
Z\in\mathbb F_2^{k\times m},
```

whose rows are the coordinates of the copies. Averaging over $`(A,a,S)`$ retains a matrix element between $`(X,Z)`$ and $`(X',Z')`$ exactly when

```math
X^{\mathsf T}X=X'^{\mathsf T}X'=G,\qquad
X^{\mathsf T}Z=X'^{\mathsf T}Z'=H.
```

The diagonal of $`G`$ records the linear-sign average over $`a`$, its off-diagonal entries record the graph average over $`A`$, and $`H`$ records the cross-coupling average over $`S`$.

The remaining target character depends on

```math
Q=Z^{\mathsf T}Z,\qquad
\langle\theta,Q\rangle
=\sum_{i\lt j}C_{ij}Q_{ij}+\sum_i b_iQ_{ii}.
```

Consequently the nuisance-averaged training state, denoted $`\omega_\theta^{(k)}`$ to distinguish it from the output target, is

```math
\omega_\theta^{(k)}
=2^{-Nk}\sum_{G,H}
|v_{\theta,G,H}\rangle\langle v_{\theta,G,H}|,
```

where

```math
|v_{\theta,G,H}\rangle
=
\sum_{\substack{X,Z:\;X^{\mathsf T}X=G\\X^{\mathsf T}Z=H}}
(-1)^{\langle\theta,Z^{\mathsf T}Z\rangle}|X,Z\rangle.
```

Different $`(G,H)`$ have disjoint computational support. The weight of a block is

```math
p_{G,H}=2^{-Nk}
\#\{(X,Z):X^{\mathsf T}X=G,\ X^{\mathsf T}Z=H\},
```

which is independent of $`\theta`$. In every nonempty block the normalized conditional training state is pure, and the target prior remains uniform.

Within a block, group the basis vectors by their value of $`Q`$. The uniform vectors on these fibers are mutually orthogonal. Hence all normalized target-dependent training vectors lie in a common space of dimension

```math
d_{G,H}=\#\{Q:\ Q\text{ is attainable in this block}\}.
```

Let $`P_{\mathrm{id}}^*(G,H)`$ be the optimal probability of identifying the full label $`\theta`$ exactly from the normalized block. For any decoding POVM $`\{E_\theta\}`$, each normalized rank-one state is bounded by the identity $`I_{\mathrm{supp}}`$ on the common support. Therefore

```math
P_{\mathrm{id}}^*(G,H)
\le
\frac{1}{M_m}\sum_\theta\mathop{\mathrm{Tr}}\nolimits (E_\theta I_{\mathrm{supp}})
=\frac{d_{G,H}}{M_m},
```

with the additional bound $`P_{\mathrm{id}}^*\le1`$.

Because the ensemble is block diagonal, a learner can first read $`(G,H)`$ without changing the ensemble and then perform a block-dependent measurement. Allowing this refinement can only help a learner. We will use this refinement when passing from exact labels to arbitrary density descriptions.

## 5. Rank completion and the number of possible target characters

Let $`g=\mathop{\mathrm{rank}}\nolimits G`$. Choose a change of input coordinates putting $`G`$ by congruence into the form $`\mathop{\mathrm{diag}}\nolimits (G_1,0)`$, where $`G_1`$ is a nonsingular $`g\times g`$ matrix. In these coordinates write $`H=(H_1^{\mathsf T},H_0^{\mathsf T})^{\mathsf T}`$.

For each tuple in the block,

```math
\begin{pmatrix}
G&H\\ H^{\mathsf T}&Q
\end{pmatrix}
=[X\ Z]^{\mathsf T}[X\ Z]
```

has rank at most $`k`$. Eliminating $`G_1`$ leaves

```math
\begin{pmatrix}
0&H_0\\
H_0^{\mathsf T}&Q-Q_0
\end{pmatrix},
\qquad
Q_0=H_1^{\mathsf T}G_1^{-1}H_1,
```

of rank at most $`k-g`$. Its principal submatrix $`Q-Q_0`$ therefore satisfies

```math
\mathop{\mathrm{rank}}\nolimits (Q-Q_0)\le k-g.
```

This argument allows $`H_0\ne0`$. It does not require $`H`$ to lie in the column space of $`G`$, nor does it require $`X`$ or $`G`$ to have full rank.

For completeness, let $`B_m(R)`$ count the symmetric $`m\times m`$ binary matrices of rank at most $`R`$, for $`0\le R\le m`$. An exact counting expression is

```math
B_m(R)=\sum_{r=0}^R {m\brack r}_2\,a_r,
\qquad
a_r=
2^{r(r+1)/2}
\prod_{j=1}^{\lceil r/2\rceil}(1-2^{-(2j-1)}),
```

where $`{m\brack r}_2`$ is the Gaussian binomial coefficient and an empty product is one. To see the first equality, choose the kernel of a rank-$`r`$ symmetric bilinear form, then choose a nonsingular symmetric form on the quotient. Here $`a_r`$ is exactly the number of such nonsingular forms on an $`r`$-dimensional binary space.

The product for $`a_r`$ follows, for example, by bordering a symmetric matrix. With $`a_0=a_1=1`$, only a nonsingular or corank-one upper-left block can yield an invertible bordered matrix, giving

```math
a_r
=2^{r-1}a_{r-1}
+2^{r-1}(2^{r-1}-1)a_{r-2}
\qquad(r\ge2).
```

The displayed product satisfies this recurrence.

For the converse it is enough to use

```math
{m\brack r}_2\le4\,2^{r(m-r)},\qquad
a_r\le2^{r(r+1)/2}.
```

The factor four follows from the Gaussian-binomial product and $`\prod_{j\ge1}(1-2^{-j})>1/4`$. Since $`r(2m-r+1)/2`$ increases for $`0\le r\le m`$,

```math
B_m(R)\le
4(R+1)\,2^{R(2m-R+1)/2}.
```

Every attainable $`Q`$ lies in the single known translate $`Q_0+\{B:\mathop{\mathrm{rank}}\nolimits B\le k-g\}`$. Thus, when $`R=k-g\le m`$,

```math
P_{\mathrm{id}}^*(G,H)
\le
\min\!\left\{
1,\;
4(m+1)\,2^{-(m-R)(m-R+1)/2}
\right\}.
```

For $`k-g\ge m`$ we use the bound one. The quadratic exponent comes from the symmetric-matrix count; replacing it by a count of arbitrary rectangular matrices would lose the needed estimate.

## 6. The probability of a large Gram nullity

Under the block weights, the marginal distribution of $`X`$ is uniform on $`\mathbb F_2^{k\times n}`$: each $`X`$ is paired with exactly $`2^{km}`$ choices of $`Z`$.

Assume first $`k\ge n\ge1`$. For a fixed nonzero $`v\in\mathbb F_2^n`$, an invertible column change reduces $`Gv=0`$ to the first column $`u`$ of a uniform $`X`$ being orthogonal to itself and to all other columns. If $`u=0`$, this is automatic. If $`u\ne0`$, its self-inner product vanishes exactly when it has even parity, and each of the other columns is orthogonal to it with probability one half. Therefore

```math
\Pr(Gv=0)
=2^{-k}
+\left(\frac12-2^{-k}\right)2^{-(n-1)}.
```

Counting vectors in the kernel yields the exact first moment

```math
\mathbb E\,2^{\mathop{\mathrm{null}}\nolimits G}
=
1+(2^n-1)
\left[
2^{-k}+
\left(\frac12-2^{-k}\right)2^{-(n-1)}
\right]
\le2+2^{n-k}\le3.
```

For $`n=0`$ the nullity is zero deterministically, so the same upper bound applies. Markov's inequality gives, for every integer $`s\ge1`$,

```math
\Pr(\mathop{\mathrm{null}}\nolimits G\ge s)\le3\,2^{-s}.
```

If the original learner has $`k\lt n`$, give it additional copies up to $`K=\max\{k,n\}`$. It can ignore them, so this can only increase its optimal fidelity. Apply the preceding argument to $`K`$ copies.

Call a block bad when $`\mathop{\mathrm{null}}\nolimits G\ge s`$. On every other block, the conservative inequality $`g\ge n-s`$ gives

```math
R=K-g\le K-n+s,\qquad
m-R\ge N-K-s=d.
```

When $`d>0`$, each good block therefore obeys

```math
P_{\mathrm{id}}^*(G,H)
\le4(m+1)\,2^{-d(d+1)/2}.
```

The bad blocks have total weight at most $`3\,2^{-s}`$. Their contribution to fidelity will be bounded directly by this weight.

## 7. From arbitrary density matrices to short target lists

The exact-identification bound alone does not bound prediction by an arbitrary density matrix. We now make that conversion without restricting the possible reports.

For any density matrix $`\sigma`$ on the output, define its high-overlap target set

```math
\mathcal H_\sigma
=\{\theta:\mathop{\mathrm{Tr}}\nolimits (\sigma\tau_\theta)\ge\eta\}.
```

Two graph targets have squared overlap

```math
\mathop{\mathrm{Tr}}\nolimits (\tau_{C,b}\tau_{C',b'})
\in
\left\{0,\;2^{-\mathop{\mathrm{rank}}\nolimits (C-C')}\right\}.
```

One direct derivation squares the binary quadratic Gauss sum for the overlap. After summing over one coordinate vector, only shifts in $`\ker(C-C')`$ survive. On this kernel the remaining quadratic expression is linear, so its sum is either zero or the size of the kernel.

Choose a maximal collection of anchors in $`\mathcal H_\sigma`$ whose graph matrices have pairwise rank distance greater than $`D`$. Their pairwise overlap **amplitudes** are at most

```math
\varepsilon_D=2^{-D/2}.
```

If there are $`L`$ anchors, the Gram matrix has diagonal one and off-diagonal absolute values at most $`\varepsilon_D`$. The operator norm of their projector sum consequently satisfies

```math
\left\|\sum_{j=1}^L\tau_{\theta_j}\right\|
\le1+(L-1)\varepsilon_D.
```

This is the row-sum bound on the Gram matrix; the nonzero eigenvalues agree with those of the projector sum. Since $`\sigma`$ is any positive unit-trace matrix,

```math
L\eta
\le\mathop{\mathrm{Tr}}\nolimits \!\left(\sigma\sum_{j=1}^L\tau_{\theta_j}\right)
\le1+(L-1)\varepsilon_D.
```

Under $`\varepsilon_D\le\eta/2`$, this implies

```math
L\le\frac{1-\varepsilon_D}{\eta-\varepsilon_D}
\le\frac{2}{\eta}.
```

By maximality, every member of $`\mathcal H_\sigma`$ has graph-rank distance at most $`D`$ from an anchor. Each such neighborhood contains at most $`2^mB_m(D)`$ target labels: this allows every sign vector $`b`$ and enlarges the zero-diagonal graph differences to all symmetric matrices. It follows that

```math
|\mathcal H_\sigma|
\le\frac{2}{\eta}\,2^mB_m(D)
\le L_m(\eta,D).
```

This bound holds for mixed $`\sigma`$, as well as pure $`\sigma`$, independently of how the density matrix was described.

Now fix one nuisance block and any measurement-and-description strategy in that block. On a measurement outcome reporting $`\sigma`$, define an exact target decoder that chooses uniformly from $`\mathcal H_\sigma`$ when it is nonempty, and chooses any label otherwise. This is a valid classical postprocessing of the measurement: the target set is finite and its membership conditions are measurable functions of $`\sigma`$. No efficient calculation of the lists is required. Its exact success probability is at least

```math
\frac{\Pr(\theta\in\mathcal H_\sigma\mid G,H)}
{L_m(\eta,D)}.
```

Also, because target overlap is at most one,

```math
F_{\mathrm{EB}}(G,H)
\le\eta+\Pr(\theta\in\mathcal H_\sigma\mid G,H).
```

Thus every strategy satisfies

```math
F_{\mathrm{EB}}(G,H)
\le\eta+L_m(\eta,D)P_{\mathrm{id}}^*(G,H).
```

Apply this conversion separately on good blocks. On bad blocks use $`F\le1`$ before averaging. The target-independent block weights then give the graph-prior bound

```math
F_{\mathrm{EB}}^{\mathrm{graph}}(N,m,k)
\le
\min\!\left\{
1,\;
3\,2^{-s}+\eta+
4(m+1)L_m(\eta,D)\,2^{-d(d+1)/2}
\right\}.
```

In particular, the probability of bad blocks is never multiplied by the list size. This ordering is needed: the list size can be much larger than the reciprocal of that probability.

## 8. Transfer to all pure stabilizer states

We now return to the uniform prior over all pure stabilizer states. Let $`L`$ be the unsigned stabilizer Lagrangian in binary Pauli phase space, and let $`W`$ be the public $`n`$-dimensional isotropic measurement subspace. Write

```math
t=\dim(L\cap W).
```

For a uniform Lagrangian, every nonzero phase-space vector belongs to $`L`$ with probability $`1/(2^N+1)`$. This follows by symmetry and by counting its $`2^N-1`$ nonzero elements among the $`2^{2N}-1`$ available vectors. Consequently

```math
\mathbb E\,2^t
=1+\frac{2^n-1}{2^N+1},
\qquad
\Pr(t\ge1)\le e_{N,m}\lt 2^{-m}.
```

We bound the fidelity on all $`t\ge1`$ sources by one. It remains to handle the conditional prior $`L\cap W=\{0\}`$.

Give the learner a uniformly chosen compatible Lagrangian frame $`\mathcal F`$ that contains $`W`$ and is transverse to $`L`$. There are exactly

```math
2^{m(m+1)/2}
```

such frames for each $`L`$ disjoint from $`W`$. To count them, take coordinates with $`L`$ the span of all $`X`$ directions and $`W`$ the span of the first $`n`$ $`Z`$ directions. A transverse frame is the graph of a symmetric matrix. Containing $`W`$ forces its first $`n`$ rows and columns to vanish, leaving one free symmetric $`m\times m`$ block.

The constant number of compatible frames is important. Under this revelation, conditioning on the announced $`\mathcal F`$ leaves $`L`$ uniform among all Lagrangians transverse to $`\mathcal F`$. The stabilizer characters remain uniform as well.

A known Clifford now sends $`\mathcal F`$ to the computational $`Z`$ frame and $`W`$ to its first $`n`$ coordinates. Transverse stabilizers have full computational support and a uniform symmetric phase matrix. For qubits, give the learner its binary diagonal phase data and undo the corresponding known single-qubit phase gates. All off-diagonal entries remain independent and uniform, including the entire unknown output graph $`C`$; the sign vector also remains uniform. The resulting ensemble is exactly the real signed graph ensemble of Section 3.

The revealed information helps a learner. The known Clifford coordinate changes, and their known branchwise output transformations, preserve fidelity and preserve the measure-and-prepare class. No unknown output graph is revealed. The graph bound therefore applies to the enhanced learner, and hence to the original one:

```math
F_{\mathrm{EB}}^{\mathrm{av}}(N,m,k)
\le e_{N,m}+F_{\mathrm{EB}}^{\mathrm{graph}}(N,m,k).
```

Combining this inequality with Section 7 proves the finite bound in Section 2. For the extensive-target theorem, discarding $`t\ge1`$ is sufficient. The [quantum converse](quantum_converse.md) treats intersection strata more finely when the retained target is small.

## 9. Asymptotic consequence and matching rate

Under the theorem's assumptions, set

```math
\gamma=\min\{\epsilon,\beta_0\}>0.
```

Since $`K=\max\{k,n\}`$,

```math
N-K=\min\{N-k,m\}\ge\gamma N.
```

Choose

```math
s=\lceil\sqrt N\rceil,\qquad
\eta=2^{-\sqrt N},\qquad
D=\lceil2\sqrt N\rceil+2.
```

For all sufficiently large $`N`$, these parameters satisfy $`D\le m`$, $`2^{-D/2}\le\eta/2`$, and $`d=N-K-s>0`$. Moreover,

```math
\log_2 L_m(\eta,D)
=\log_2\!\bigl(8(D+1)\bigr)+\sqrt N
+m+\frac{D(2m-D+1)}2
=O(N^{3/2}),
```

uniformly over the allowed $`m`$, whereas $`d(d+1)/2=\Omega_\gamma(N^2)`$. The finite bound gives

```math
F_{\mathrm{EB}}^{\mathrm{av}}
\le
2^{-m}
+3\,2^{-\lceil\sqrt N\rceil}
+2^{-\sqrt N}
+2^{-\Omega_\gamma(N^2)+O(N^{3/2})}
\longrightarrow0.
```

The explicit inequality in Section 2 specifies all constants; this last expression records only its asymptotic consequence.

For achievability, full stabilizer identification with failure probability at most $`\delta\in(0,1/8)`$ uses

```math
N+\left\lceil\log_2\frac1\delta\right\rceil+4
```

copies by [Chang–Caro–Larocca–West](../references/RELATED_WORK.md#ChangCaroLaroccaWest2026). The learner can then calculate the conditional state for the supplied outcome and provide its classical description. On successful identification it predicts exactly, so its mean fidelity is at least $`1-\delta`$. Taking, for example, $`\delta=1/N`$ establishes a vanishing-error classical-description copy rate of one.

Together with [quantum synthesis](synthesis.md) and the [quantum converse](quantum_converse.md), this yields rates $`1`$ and $`1-\beta`$ respectively when $`m/N\to\beta\in(0,1)`$. The [interpretation](interpretation.md) explains the physical resources and the regime $`n=\lceil\sqrt N\rceil`$. Finite checks and their precise scope are documented in [verification](../verification/README.md).
