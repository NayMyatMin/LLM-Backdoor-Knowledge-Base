---
title: "Zoom In: An Introduction to Circuits"
source: "zoom-in-circuits.md"
venue: "Distill"
year: 2020
summary: "Foundational article proposing that neural networks can be understood by studying individual neurons and the circuits (weighted connections) between them, analogous to how biology studies cells and organs."
compiled: "2026-04-03T22:00:00"
---

# Zoom In: An Introduction to Circuits

**Authors:** Chris Olah, Nick Cammarata, Ludwig Schubert, Gabriel Goh, Michael Petrov, Shan Carter (OpenAI)
**Venue:** Distill, 2020
**URL:** https://distill.pub/2020/circuits/zoom-in/

## Summary

This article launches the Circuits research program by arguing that neural networks are not inscrutable black boxes — they contain meaningful, human-understandable algorithms encoded in their weights. By "zooming in" on individual neurons and tracing the connections between them, researchers can identify interpretable features and the circuits that compose them into higher-level computations. The authors draw an analogy to the invention of the microscope in biology: just as cells initially seemed uninterpretable but eventually yielded the foundations of modern biology, neurons and circuits may yield the foundations of a mechanistic science of deep learning.

The article presents three core claims: (1) features are the fundamental unit, represented by directions in activation space rather than individual neurons; (2) circuits are the computational motif, consisting of weighted connections between features that implement recognizable algorithms; and (3) universality — similar features and circuits appear across different networks trained on different data. These claims are supported with detailed case studies from vision models (InceptionV1), including curve detectors, high-low frequency detectors, and oriented edge compositions.

## Key Concepts

- [[circuit-analysis]] — the central methodology proposed
- [[mechanistic-interpretability]] — the broader research agenda this article inaugurates
- [[superposition]] — acknowledged as a key challenge: neurons can be polysemantic, encoding multiple features

## Method Details

The authors demonstrate their approach through several case studies in InceptionV1:

**Curve Detectors**: Neurons in early layers that respond to curves at specific orientations. These are built from edge-detecting circuits in prior layers — tangent-aligned edges excite, perpendicular edges inhibit.

**High-Low Frequency Detectors**: Neurons that respond to boundaries between high-frequency texture and low-frequency regions, composed from Gabor-like filters with opposing frequency preferences.

**Pose-Invariant Dog Heads**: Higher-level neurons that detect dog heads regardless of orientation, built by combining multiple pose-specific dog-head detectors from prior layers.

Each case study traces the full circuit: which earlier features feed in, what the weights encode, and how this implements an interpretable algorithm.

## Results & Findings

The article demonstrates that circuits can be understood at a fine-grained, mechanistic level in vision models. The authors find that individual features are often more interpretable than expected, and the connections between them implement algorithms that can be described in natural language. The universality claim is supported by finding similar features (e.g., curve detectors) across multiple independently trained networks.

## Relevance to LLM Backdoor Defense

The circuits framework provides the theoretical foundation for understanding how backdoors are mechanistically encoded in neural networks. If a backdoor is a learned shortcut from trigger to target behavior, it must be implemented as a circuit — a set of features and weighted connections that detect the trigger and route computation to the target output. Understanding circuits enables:

- **Backdoor localization**: identifying which neurons and connections encode the backdoor circuit, as explored in [[mechanistic-exploration-backdoors]]
- **Targeted removal**: pruning or editing specific circuit components rather than blunt approaches, connecting to [[neuron-pruning-defense]] and [[adversarial-neuron-pruning]]
- **Detection**: recognizing anomalous circuits that implement shortcut behavior rather than legitimate task features

## Related Work

- [[transformer-circuits-framework]] — extends the circuits framework to transformers
- [[toy-models-superposition]] — explores how superposition complicates circuit analysis
- [[towards-monosemanticity]] — uses sparse autoencoders to decompose polysemantic neurons into monosemantic features

## Backlinks

- [[circuit-analysis]]
- [[mechanistic-interpretability]]
- [[backdoor-circuits]]
- [[interpretability-as-defense]]
