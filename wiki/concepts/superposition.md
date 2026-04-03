---
title: "Superposition"
slug: "superposition"
brief: "The phenomenon where neural networks represent more features than they have dimensions by storing sparse features in overlapping, superposed directions in activation space — causing polysemanticity and making per-neuron interpretability unreliable."
compiled: "2026-04-03T22:00:00"
---

# Superposition

## Definition

Superposition is the phenomenon where a neural network encodes more independent features than it has dimensions in its activation space, by storing each feature as a direction in that space and allowing multiple features to share the same dimensions. When features are sparse (rarely active simultaneously), their directions can overlap with minimal interference, enabling the network to represent far more concepts than a one-feature-per-neuron regime would allow. The cost is polysemanticity: individual neurons respond to multiple unrelated concepts because they sit at the intersection of multiple feature directions.

## Background

The concept was formalized by [[toy-models-superposition]] (Elhage et al., 2022), which used toy ReLU networks to demonstrate that superposition is a rational strategy for networks with limited capacity facing many sparse features. The phenomenon had been observed informally before — neurons responding to seemingly unrelated inputs — but the toy models paper provided the theoretical framework explaining *why* it happens and *when* it emerges (as a function of feature sparsity and importance).

Superposition is the central challenge for [[mechanistic-interpretability]]: if individual neurons are polysemantic, they cannot serve as the fundamental unit of analysis. This motivated the development of [[sparse-autoencoder|sparse autoencoders]] ([[towards-monosemanticity]]) as a tool to decompose polysemantic activations into monosemantic features.

## Technical Details

### The Superposition Regime

Consider a network with d-dimensional hidden states that needs to represent N > d features. If each feature is active with probability p (sparsity), the network faces a trade-off:
- **Monosemantic regime** (N <= d): Assign each feature its own orthogonal dimension. Perfect representation, no interference.
- **Superposition regime** (N > d): Store features as non-orthogonal directions. The dot product between feature directions causes interference, but if features are sparse, interference is rarely activated.

### Phase Transitions

As feature sparsity increases (p decreases), features undergo a phase transition from not being represented at all, to being represented in superposition, to being fully monosemantic (if dimensions are available). The transition is sharp, with features "snapping" into representation at critical sparsity thresholds.

### Geometric Structure

The optimal arrangement of superposed features corresponds to mathematical structures called uniform polytopes. In 2D, for example, representing 3 features requires directions at 120-degree angles (forming a triangle); representing 5 requires a pentagon. Higher dimensions enable richer geometric structures with more features packed per dimension.

### Polysemanticity as a Consequence

A neuron that appears polysemantic is not broken or confused — it simply has a large activation value when its direction in activation space aligns with any of several superposed feature directions. The neuron is responding to a linear combination of multiple features, not to any single concept.

## Variants

- **Dense superposition**: Features are common enough that interference is significant, requiring nonlinear filtering mechanisms
- **Sparse superposition**: Features are rare enough that interference is negligible in practice
- **Feature splitting**: As model capacity increases, superposed features can "split" into separate, monosemantic representations

## Key Papers

- [[toy-models-superposition]] — foundational theoretical study of superposition in toy models
- [[towards-monosemanticity]] — practical resolution of superposition via sparse autoencoders
- [[zoom-in-circuits]] — acknowledged superposition as a challenge for the circuits paradigm

## Relevance to Backdoor Defense

Superposition has direct implications for backdoor attacks and defenses:

- **Backdoor hiding**: A backdoor trigger feature can be stored in superposition with legitimate features, making it invisible to per-neuron inspection. The backdoor direction is "camouflaged" among many overlapping feature directions.
- **Why spectral methods detect backdoors**: [[spectral-signatures]] works because poisoned samples coherently activate the backdoor feature direction, creating a detectable statistical signature (large eigenvalue) even though the feature is superposed.
- **Why pruning is imprecise**: [[neuron-pruning-defense]] removes neurons, but in the superposition regime, removing a neuron may damage multiple superposed features. This explains the clean accuracy vs. backdoor removal trade-off.
- **SAE-based defense potential**: [[sparse-autoencoder|Sparse autoencoders]] can decompose activations into monosemantic features, potentially isolating the backdoor feature for targeted removal.
- **Adaptive attack surface**: Adversaries understanding superposition could optimize backdoors to maximize overlap with important features, making removal more costly.

## Related Concepts

- [[mechanistic-interpretability]] — the research program that studies superposition
- [[sparse-autoencoder]] — the primary tool for resolving superposition
- [[circuit-analysis]] — circuits analysis is complicated by superposition
- [[probing-classifier]] — linear probes work in superposition because features are directions
- [[activation-analysis]] — many activation-based defenses implicitly detect superposed features
- [[spectral-signatures]] — spectral analysis exploits the statistical signature of superposed backdoor features
- [[embedding-space-defense]] — defenses operating in the space where superposition occurs

## Open Problems

- **Scaling**: How does superposition behave in billion-parameter models with massive hidden dimensions?
- **Non-linear superposition**: Current theory focuses on approximately linear superposition; how do nonlinear mechanisms change the picture?
- **Adversarial superposition**: Can attackers deliberately engineer backdoors that exploit superposition to resist detection?
- **Feature interference in defenses**: How does removing a superposed backdoor feature affect co-superposed legitimate features?
