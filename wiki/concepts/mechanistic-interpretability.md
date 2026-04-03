---
title: "Mechanistic Interpretability"
slug: "mechanistic-interpretability"
brief: "A research paradigm that aims to reverse-engineer neural networks by understanding the specific algorithms, features, and circuits implemented in their weights — moving beyond treating models as black boxes to building a science of neural network internals."
compiled: "2026-04-03T22:00:00"
---

# Mechanistic Interpretability

## Definition

Mechanistic interpretability (mech interp) is the study of neural networks at a mechanistic level: identifying the specific features networks detect, the circuits that compose these features into computations, and the algorithms these circuits implement. Unlike behavioral evaluation (testing what a model does) or statistical probing (correlating representations with concepts), mechanistic interpretability seeks causal, fine-grained understanding of *how* a model computes its outputs.

## Background

The field emerged from the insight that neural networks, despite their complexity, contain structured, human-understandable algorithms in their weights. The [[zoom-in-circuits]] article by Olah et al. (2020) articulated the foundational vision: neurons represent interpretable features, connections between neurons form circuits, and similar circuits appear across different networks (universality). The [[transformer-circuits-framework]] extended this to transformers, and subsequent work on [[superposition]] and [[sparse-autoencoder|sparse autoencoders]] addressed the challenge that individual neurons are often polysemantic.

## Technical Details

### Core Methodology

1. **Feature identification**: Determine what concepts or patterns a model represents internally. Individual neurons are an imperfect unit due to [[superposition]]; better approaches include [[sparse-autoencoder|SAE decomposition]] and [[probing-classifier|linear probing]].

2. **Circuit tracing**: Identify the computational subgraph (circuit) responsible for a specific behavior. Techniques include [[activation-patching]], ablation studies, and attention pattern analysis.

3. **Algorithm verification**: Confirm that the identified circuit implements the hypothesized algorithm by testing predictions on novel inputs.

### Key Tools and Techniques

- **[[logit-lens]]** and **[[tuned-lens|Tuned Lens]]**: Decode intermediate representations into vocabulary distributions to track prediction refinement across layers
- **[[activation-patching]]**: Causal interventions that replace activations in one forward pass with those from another to identify which components matter
- **[[sparse-autoencoder]]**: Decompose polysemantic activations into monosemantic features
- **[[probing-classifier]]**: Train linear classifiers on representations to test what information is encoded
- **[[representation-engineering]]**: Identify and manipulate population-level representation directions corresponding to high-level concepts

### Two Paradigms

**Bottom-up (Circuits)**: Start from individual neurons/features and build up to understanding full model behavior. Exemplified by [[zoom-in-circuits]], [[transformer-circuits-framework]], [[towards-monosemanticity]].

**Top-down (RepE)**: Start from high-level concepts and identify their representation-space signatures. Exemplified by [[representation-engineering]], [[tuned-lens]].

## Variants

- **Circuits-based interpretability**: Focus on individual features and circuits (Anthropic, OpenAI early work)
- **Representation engineering**: Population-level analysis of concept directions
- **Probing-based approaches**: Linear classifiers testing for encoded information
- **Causal methods**: Activation patching, causal tracing, ablation studies
- **Dictionary learning**: Sparse autoencoders for feature decomposition

## Key Papers

- [[zoom-in-circuits]] — founding vision of the circuits research program
- [[transformer-circuits-framework]] — mathematical framework for transformer circuits
- [[toy-models-superposition]] — understanding of why features are stored in superposition
- [[towards-monosemanticity]] — sparse autoencoders for resolving superposition
- [[rome-factual-associations]] — causal tracing for locating knowledge in transformers
- [[tuned-lens]] — layer-wise prediction tracking
- [[representation-engineering]] — top-down approach to representation analysis
- [[mechanistic-exploration-backdoors]] — applying mech interp to backdoor analysis

## Relevance to Backdoor Defense

Mechanistic interpretability provides the theoretical foundation for understanding *how* backdoors are encoded in neural networks:

- **Backdoor localization**: [[activation-patching]] and circuit tracing can identify exactly which layers, heads, and neurons implement the trigger-to-target mapping
- **Feature-level detection**: [[sparse-autoencoder|SAEs]] may decompose backdoor trigger detectors as identifiable features
- **Representation monitoring**: [[representation-engineering]] enables real-time monitoring for backdoor-associated internal states
- **Targeted removal**: Understanding the backdoor circuit enables surgical removal rather than blunt retraining
- **Theoretical grounding**: [[superposition]] theory explains why backdoors can hide and why certain detection methods (spectral, clustering) work

## Related Concepts

- [[circuit-analysis]] — the core methodology of mechanistic interpretability
- [[superposition]] — the key challenge: features compressed beyond neuron-level analysis
- [[sparse-autoencoder]] — the primary tool for resolving superposition
- [[activation-patching]] — the primary causal analysis technique
- [[probing-classifier]] — the primary correlational analysis technique
- [[logit-lens]] — layer-wise prediction analysis
- [[representation-engineering]] — the top-down complement to bottom-up circuits
- [[backdoor-defense]] — the application domain where mech interp serves as a toolkit
- [[activation-analysis]] — existing defense paradigm grounded in representation-level analysis

## Open Problems

- **Scaling**: Most mechanistic analysis has been done on small models (< 1B parameters). Scaling to frontier models remains an open challenge.
- **Automation**: Manual circuit tracing is labor-intensive. Automated circuit discovery methods are still immature.
- **Completeness**: Can we ever fully reverse-engineer a large model, or must we settle for understanding specific behaviors?
- **Superposition resolution**: Current SAE methods capture many features but may miss others, especially those in deep superposition.
- **Backdoor-specific circuits**: We lack systematic studies of how different backdoor types (trigger, clean-label, instruction-level) map to different circuit architectures.
