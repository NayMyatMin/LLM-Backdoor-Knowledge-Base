---
title: "Probing Classifier"
slug: "probing-classifier"
brief: "A diagnostic technique that trains simple classifiers (typically linear) on neural network hidden representations to test what information is encoded at different layers, serving as a bridge between representation analysis and backdoor detection."
compiled: "2026-04-03T22:00:00"
---

# Probing Classifier

## Definition

A probing classifier (or diagnostic classifier, linear probe) is a simple model — typically a linear classifier or shallow MLP — trained on the hidden representations of a neural network to predict some property of interest. The probe tests whether specific information (syntactic structure, semantic role, factual knowledge, or anomalous input characteristics) is linearly decodable from the network's internal representations at a given layer. If a linear probe achieves high accuracy, the information is said to be "linearly represented" at that layer.

## Background

Probing emerged from the NLP interpretability community (Belinkov et al., 2017; Conneau et al., 2018) as a way to understand what pre-trained representations encode. The technique became a standard tool for analyzing BERT, GPT, and other language models, revealing that different layers encode different types of information: early layers capture surface features, middle layers capture syntax, and later layers capture semantics.

The connection to [[mechanistic-interpretability]] is direct: if information is linearly represented, it exists as a direction in activation space (a feature), aligning with the [[superposition]] framework where features are directions. Probing classifiers are thus the empirical test for whether a feature exists in a model's representations.

## Technical Details

### Standard Probing Protocol

1. **Collect representations**: Run inputs through the target model and extract hidden states h_l at layer l
2. **Define the target property**: Choose a binary or multi-class label for each input (e.g., "contains a backdoor trigger" vs. "clean")
3. **Train a probe**: Fit a linear classifier (logistic regression) or shallow MLP on {h_l, label} pairs
4. **Evaluate**: Test accuracy on held-out data indicates how well the property is encoded at layer l
5. **Layer sweep**: Repeat across all layers to find where the information first appears and where it peaks

### Probe Complexity Control

A key concern is that complex probes (deep MLPs) might learn the task themselves rather than merely reading information from the representation. Best practices include:
- Use linear probes (logistic regression) as the default
- If nonlinear probes are needed, control for probe capacity (e.g., compare against a random baseline)
- The [[tuned-lens]] is a principled variant: affine probes per layer, trained to predict the model's own output distribution

### Connection to RepE

[[representation-engineering]] can be viewed as a specialized probing approach where:
- The "probe" is a single direction vector (the difference in mean representations between contrastive stimuli)
- The "training" is computing this difference (no optimization needed)
- The "prediction" is the dot product of a test representation with this direction

## Variants

- **Linear probes**: Logistic regression on hidden states (standard)
- **Affine probes**: Linear + bias, as in the [[tuned-lens]]
- **MLP probes**: Shallow neural networks for testing nonlinearly encoded information
- **Structural probes**: Probes that test for specific structures (e.g., dependency trees)
- **Amnesic probing**: Remove information by projecting out probe directions, testing causal importance

## Key Papers

- [[tuned-lens]] — a principled per-layer affine probe for tracking prediction refinement
- [[representation-engineering]] — probing via contrastive direction finding

## Relevance to Backdoor Defense

Probing classifiers are directly applicable to backdoor detection:

- **"Is this input triggered?" probe**: Train a linear probe on hidden states to distinguish clean from triggered inputs. If the probe succeeds, the model internally encodes trigger presence as a detectable feature. This is the representation-level analogue of input-level detectors like [[strip]].

- **Layer-wise detection**: Sweeping the probe across layers reveals *where* the model first distinguishes triggered from clean inputs — identifying the layer where the backdoor circuit activates. This connects to the representation velocity approach of examining layer-wise dynamics.

- **Connection to existing defenses**: Many existing backdoor defenses are implicitly probing approaches:
  - [[spectral-signatures]]: The top singular vector is a probe direction
  - [[activation-clustering]]: Clustering is non-parametric probing
  - [[badacts]]: Mahalanobis distance is a probe-like anomaly score
  - [[asset]]: Adaptive spectral analysis selects probe dimensions

- **Defense design**: Understanding that "the model encodes trigger presence linearly" (if true) enables simple, efficient detectors that can run at inference time with minimal overhead.

## Related Concepts

- [[mechanistic-interpretability]] — probing is a core interpretability technique
- [[superposition]] — probing works because features are directions (even in superposition)
- [[representation-engineering]] — a probing-based approach to representation analysis
- [[logit-lens]] — a special case: probing for the model's own next-token prediction
- [[activation-analysis]] — the broader defense category that probing belongs to
- [[spectral-signatures]] — implicitly a probing method using SVD
- [[activation-clustering]] — non-parametric alternative to probing
- [[sparse-autoencoder]] — provides features that can be probed individually

## Open Problems

- **Probe faithfulness**: Does a successful probe mean the model *uses* that information, or merely that it is *available*? Causal methods ([[activation-patching]]) are needed to confirm.
- **Probing in superposition**: When features are superposed, linear probes may conflate multiple features. SAE decomposition before probing may be needed.
- **Adaptive backdoors**: Can adversaries train models where trigger presence is not linearly separable at any layer?
- **Efficiency**: Running probes at every layer during inference adds latency; which layers are most informative?
