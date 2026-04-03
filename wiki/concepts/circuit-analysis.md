---
title: "Circuit Analysis"
slug: "circuit-analysis"
brief: "The methodology of reverse-engineering neural network behavior by identifying computational subgraphs (circuits) — specific sets of features and weighted connections that implement interpretable algorithms — as the fundamental unit of mechanistic interpretability."
compiled: "2026-04-03T22:00:00"
---

# Circuit Analysis

## Definition

Circuit analysis is the methodology of understanding neural network behavior by identifying and studying circuits: minimal computational subgraphs consisting of features (represented as directions in activation space) and the weighted connections between them that implement specific, interpretable algorithms. A circuit for a particular behavior includes only the features and weights that are necessary and sufficient for that behavior, analogous to how an electrical circuit diagram shows only the components relevant to a specific function.

## Background

The circuits paradigm was proposed by [[zoom-in-circuits]] (Olah et al., 2020), which demonstrated that vision model behaviors like curve detection and object recognition can be understood as compositions of simple, interpretable features connected through meaningful weights. [[transformer-circuits-framework]] (Elhage et al., 2021) extended this to transformers, formalizing how attention heads and MLPs compose through the residual stream to form circuits like induction heads.

Circuit analysis is the core methodology of [[mechanistic-interpretability]], providing a level of analysis between individual neurons (too low-level, and confounded by [[superposition]]) and full-model behavior (too high-level to be mechanistically informative).

## Technical Details

### Finding Circuits

**Activation Patching / Causal Tracing**: The primary technique for circuit discovery. Replace activations at specific components (layers, heads, neurons) with clean/corrupted values and measure the effect on the target behavior. Components that significantly affect the output are part of the circuit. See [[activation-patching]].

**Ablation Studies**: Zero out or remove specific components to test whether they are necessary for the behavior. More destructive than patching but simpler to implement.

**Attention Pattern Analysis**: In transformers, examine which positions attend to which, revealing the information flow pattern. Used extensively in [[mechanistic-exploration-backdoors]].

**Automated Circuit Discovery (ACDC)**: Algorithmic approaches that systematically test all components and prune the non-essential ones, producing a minimal circuit automatically.

### Circuit Components in Transformers

- **Attention heads (QK circuit)**: Determine which positions attend to which — the routing mechanism
- **Attention heads (OV circuit)**: Determine what information is moved — the content mechanism
- **MLP layers**: Implement feature transformations and memory retrieval ([[rome-factual-associations]])
- **Residual stream**: The shared communication channel connecting all components

### Known Circuit Motifs

- **Induction heads**: Two-layer attention circuit for in-context pattern completion
- **Factual recall**: MLP circuits that store and retrieve factual associations
- **Copy circuits**: Attention patterns that copy token information across positions
- **Inhibition circuits**: Negative attention weights that suppress competing outputs

## Variants

- **Bottom-up circuit discovery**: Start from features, trace connections upward
- **Top-down circuit discovery**: Start from the output, trace backward to find contributing components
- **Automated methods**: ACDC, path patching, and other algorithmic approaches
- **Feature-level circuits**: Using [[sparse-autoencoder]] features as nodes rather than neurons

## Key Papers

- [[zoom-in-circuits]] — foundational circuits paper for vision models
- [[transformer-circuits-framework]] — mathematical framework for transformer circuits
- [[rome-factual-associations]] — causal tracing to locate factual knowledge circuits
- [[mechanistic-exploration-backdoors]] — circuit analysis applied to backdoor mechanisms

## Relevance to Backdoor Defense

Circuit analysis is the most direct bridge between mechanistic interpretability and backdoor defense:

- **Backdoor circuit identification**: A backdoor must be implemented as a circuit — features that detect the trigger, connections that route triggered inputs to the target output, and output features that produce the backdoor behavior. Circuit analysis can identify this entire pathway, as demonstrated in [[mechanistic-exploration-backdoors]].

- **Distinction from clean circuits**: Backdoor circuits are expected to be structurally different from clean task circuits — shorter (shortcut), more concentrated (specific heads/layers), and active only on triggered inputs. These structural differences could serve as detection signals.

- **Targeted removal**: Once the backdoor circuit is identified, specific components (attention heads, MLP neurons, feature directions) can be removed or modified. This is more precise than blanket pruning ([[neuron-pruning-defense]]) or full unlearning ([[adversarial-unlearning]]).

- **Defense verification**: After applying a defense (pruning, fine-tuning, unlearning), circuit analysis can verify whether the backdoor circuit has actually been destroyed or merely suppressed.

## Related Concepts

- [[mechanistic-interpretability]] — the broader research program
- [[activation-patching]] — the primary tool for circuit discovery
- [[superposition]] — complicates circuit analysis by making features polysemantic
- [[sparse-autoencoder]] — provides better feature units for circuit analysis
- [[trigger-reverse-engineering]] — complementary approach: circuits finds where the backdoor is, trigger inversion finds what activates it
- [[neuron-pruning-defense]] — can be guided by circuit analysis for more targeted pruning
- [[backdoor-defense]] — the application domain

## Open Problems

- **Circuit completeness**: How do we know we have found the full backdoor circuit?
- **Distributed circuits**: Backdoors that distribute computation across many components resist localization
- **Dynamic circuits**: Can backdoor circuits change structure depending on context?
- **Scalable discovery**: Automated circuit discovery for billion-parameter models is computationally challenging
- **Circuit-aware attacks**: Adversaries who understand circuit analysis could design backdoors that blend with legitimate circuits
