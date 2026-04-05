---
title: "Toy Models of Superposition"
source: "toy-models-superposition.md"
venue: "Anthropic (arXiv)"
year: 2022
summary: "Investigates how neural networks represent more features than they have dimensions through superposition, using toy ReLU networks to study polysemanticity, phase transitions, and the geometry of compressed representations."
tags:
  - interpretability
  - representation
compiled: "2026-04-03T22:00:00"
---

# Toy Models of Superposition

**Authors:** Nelson Elhage, Tristan Hume, Catherine Olsson, Nicholas Schiefer, Tom Henighan, Shauna Kravec, Zac Hatfield-Dodds, Robert Lasenby, Dawn Drain, Carol Chen, Roger Grosse, Sam McCandlish, Jared Kaplan, Dario Amodei, Martin Wattenberg, Christopher Olah
**Venue:** Anthropic (arXiv:2209.10652), 2022
**URL:** https://arxiv.org/abs/2209.10652

## Summary

This paper addresses a fundamental question in neural network interpretability: why are neurons polysemantic (responding to multiple unrelated concepts)? The authors hypothesize that neural networks use superposition to represent more features than they have dimensions, compressing sparse features into overlapping representations. Using toy ReLU networks trained on synthetic data with known ground-truth features, they demonstrate that superposition is a real phenomenon with rich mathematical structure, including phase transitions as feature sparsity and importance vary, and surprising connections to the geometry of uniform polytopes.

The paper establishes superposition as a central challenge for mechanistic interpretability: if features are stored in superposed form, individual neurons are unreliable units of analysis, and specialized tools (like [[sparse-autoencoder|sparse autoencoders]]) are needed to decompose activations into interpretable features.

## Key Concepts

- [[superposition]] — the core phenomenon studied
- [[mechanistic-interpretability]] — the research program this work advances
- [[sparse-autoencoder]] — motivated by this work as a solution to superposition

## Method Details

**Setup**: The authors train small ReLU networks (autoencoders) where the hidden layer has fewer dimensions than the input. The input features have known sparsity (how often each feature is active) and importance (how much each feature contributes to loss). The question: how does the network allocate its limited dimensions?

**Key Finding — Superposition**: When features are sparse enough, the network represents more features than dimensions by storing them in superposed form. A feature with sparsity S in a d-dimensional space can be approximately represented alongside other features, with interference proportional to the overlap between feature directions.

**Phase Transitions**: As sparsity increases, features undergo a phase transition from being individually represented (one feature per dimension, or "monosemantic") to being stored in superposition. The transition is sharp and depends on both sparsity and relative importance.

**Geometric Structure**: The optimal arrangement of superposed features corresponds to known geometric objects — uniform polytopes that maximize the minimum angle between feature directions. This connects neural network representation to classical problems in mathematics.

**Polysemanticity Explained**: A neuron that appears polysemantic (responding to multiple unrelated concepts) is actually computing a direction in activation space that has high dot product with multiple superposed feature directions. Polysemanticity is a consequence of superposition, not a bug.

## Results & Findings

- Superposition is confirmed as a real phenomenon in toy models
- Phase transitions between monosemantic and superposed regimes are characterized
- Feature geometry follows polytope structures (pentagons, tetrahedra, etc.)
- Connection established between superposition and adversarial vulnerability
- The number of features a network can represent scales super-linearly with dimensions when features are sparse

## Relevance to LLM Backdoor Defense

Superposition theory has profound implications for backdoor defense:

- **Why backdoors hide**: A backdoor trigger feature can be stored in superposition with legitimate features, making it invisible to per-neuron analysis. This explains why simple neuron-level inspection (e.g., looking at highly activated neurons) often fails to detect backdoors.
- **Why spectral methods work**: [[spectral-signatures]] detects backdoors by finding anomalous directions in activation space. Superposition theory explains why this works: the backdoor feature direction, though superposed, still creates a statistically detectable signature when many poisoned samples activate it coherently.
- **SAE-based detection**: [[sparse-autoencoder|Sparse autoencoders]] can potentially decompose activations into monosemantic features, isolating backdoor-specific features from the superposed representation. This is an emerging defense direction.
- **Adaptive attacks**: Understanding superposition suggests adversaries could craft backdoors that are optimally superposed with important features, making removal costly without performance degradation.

## Related Work

- [[zoom-in-circuits]] — the circuits framework that superposition complicates
- [[transformer-circuits-framework]] — the transformer-specific circuits framework
- [[towards-monosemanticity]] — applies SAEs to resolve superposition in real models
- [[representation-engineering]] — a top-down alternative to decomposing individual features

## Backlinks

- [[superposition]]
- [[sparse-autoencoder]]
- [[mechanistic-interpretability]]
- [[superposition-and-backdoor-hiding]]
