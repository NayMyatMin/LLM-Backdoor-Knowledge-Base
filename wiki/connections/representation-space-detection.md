---
title: "Representation Space as Battleground: Detection Through Internal Representations"
slug: "representation-space-detection"
compiled: "2026-04-03T12:00:00"
---

# Representation Space as Battleground

## Connection

Multiple defenses independently discovered that backdoor attacks leave detectable traces in a model's internal representation space. This convergence suggests a fundamental property of how backdoors alter neural network computations.

## Converging Evidence

### Spectral Signatures
- [[spectral-signatures]]: Poisoned data creates a distinguishable component in the top singular vectors of the representation covariance matrix
- Detection via SVD + outlier removal

### Activation Clustering
- [[activation-clustering]]: Poisoned and clean samples form separate clusters in activation space
- Detection via PCA + k-means clustering

### Neural Cleanse (Indirect)
- [[neural-cleanse]]: The fact that small triggers cause universal misclassification implies a concentrated representation-space effect
- Backdoor labels have anomalously compact trigger regions in input space

### Fine-Pruning
- [[fine-pruning]]: Backdoor behavior is encoded in neurons dormant on clean data
- These neurons create a separate "channel" in representation space for triggered inputs

## The Common Principle

All these defenses exploit the same underlying phenomenon: **backdoor attacks create a shortcut in representation space**. Triggered inputs are mapped to a distinct region that the model has learned to associate with the target class, separate from the natural representation of that class. This shortcut is detectable because it introduces statistical anomalies (spectral signatures, cluster separability, dormant neurons).

## Mechanistic Interpretability Perspective

The convergence of defenses on representation space is now understood through the lens of [[mechanistic-interpretability]]:

- **[[superposition]] theory** explains *why* backdoors create representation-space shortcuts: the trigger feature, stored in superposition with legitimate features, creates a consistent directional shift when activated. See [[superposition-and-backdoor-hiding]] for the full analysis.
- **[[circuit-analysis]]** reveals *where* these shortcuts live: [[mechanistic-exploration-backdoors]] shows backdoor attention signatures concentrate in later layers (20-30), with circuit complexity depending on trigger type.
- **[[sparse-autoencoder|SAEs]]** could advance this paradigm by decomposing the representation space into interpretable features, potentially isolating the backdoor feature from its superposed context.
- **[[representation-engineering]]** provides a top-down alternative to SVD-based detection, using contrastive stimuli to find the backdoor direction directly.

## Limitations

- Clean-label attacks like [[poison-frogs]] are designed to minimize this representation-space separation
- Syntactic attacks like [[hidden-killer]] operate at a structural level that may not create simple cluster separability
- LLM-scale models may have more complex representation dynamics

## Related Papers

- [[spectral-signatures]], [[activation-clustering]], [[neural-cleanse]], [[fine-pruning]]
- [[mechanistic-exploration-backdoors]], [[representation-engineering]], [[toy-models-superposition]]

## Related Concepts

- [[backdoor-defense]]
- [[trigger-pattern]]
- [[backdoor-attack]]
- [[superposition]], [[circuit-analysis]], [[mechanistic-interpretability]]
- [[superposition-and-backdoor-hiding]], [[backdoor-circuits]]
