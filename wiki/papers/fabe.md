---
title: "Defending Against Backdoor Attacks by Leveraging Internal Feature of Model (FABE)"
source: raw/fabe-causality-front-door-defense.md
venue: ICML
year: 2024
summary: "FABE applies the front-door adjustment from causal inference to defend against backdoor attacks, blocking the trigger's causal path to model output through feature-level intervention while preserving clean prediction accuracy."
compiled: "2026-04-03T16:00:00"
---

# Defending Against Backdoor Attacks by Leveraging Internal Feature of Model (FABE)

**Authors:** Xiong Xu, Kunzhe Huang, Yiming Li, Zhan Qin, Kui Ren
**Venue:** ICML 2024 **Year:** 2024

## Summary

Backdoor attacks implant hidden behaviors in neural networks by creating spurious correlations between trigger patterns and target labels. Most existing defenses rely on empirical heuristics without a principled understanding of why triggers succeed or how to block them. FABE addresses this gap by formulating backdoor attacks within a rigorous causal inference framework using structural causal models.

The core idea is to model the input-feature-output pipeline as a causal graph where the trigger acts as a confounder. By applying the front-door adjustment criterion — a classical causal inference technique — FABE blocks the causal pathway from the trigger to the model's output while preserving the clean pathway from legitimate input features to correct predictions. This is implemented practically through a feature bank constructed from clean reference samples, which dilutes trigger-specific activations at inference time.

FABE reduces attack success rates below 5% across multiple attack types (BadNets, Blended, WaNet) on CIFAR-10, GTSRB, and Tiny ImageNet, with less than 2% clean accuracy degradation. The causal grounding provides interpretable explanations for defense effectiveness, distinguishing FABE from purely empirical approaches.

## Key Concepts

- [[backdoor-defense]] — inference-time defense requiring no model retraining
- [[trigger-pattern]] — neutralized via causal intervention on feature representations
- [[backdoor-attack]] — modeled as causal confounding in the input-feature-output graph
- [[trigger-reverse-engineering]] — not required; FABE operates without knowing the trigger

## Method Details

FABE constructs a causal graph relating input X, internal features Z, prediction Y, and trigger T:

- **X → Z → Y**: the clean causal path from input through features to prediction
- **T → X** and **T → Z**: the trigger introduces a confounding path that creates spurious feature-output associations

The front-door adjustment estimates the causal effect of X on Y through mediator Z, marginalizing out T's confounding:

P(Y | do(X)) = Σ_Z P(Z|X) · Σ_{X'} P(Y|Z,X') · P(X')

In practice, the defense proceeds in three steps:

1. **Feature bank construction**: Extract intermediate features from a small clean reference set (500–1000 samples) to build a feature bank representing the distribution of clean activations.

2. **Feature extraction**: For each test input x, extract features z = encoder(x), which may contain trigger-induced activations.

3. **Adjusted prediction**: Replace the direct feature-to-prediction mapping with a weighted average over the feature bank, where weights are determined by similarity to z. This averaging step dilutes trigger-specific features by mixing in clean feature statistics, breaking the trigger → target mapping.

The theoretical justification is that averaging over the feature bank implements the front-door formula's marginalization over X', effectively blocking the confounding path T → Z → Y by decorrelating trigger features from the target label.

## Results & Findings

- Attack success rate reduced below 5% against BadNets, Blended, WaNet, and other attacks on CIFAR-10, GTSRB, and Tiny ImageNet
- Clean accuracy degradation under 2% compared to the undefended model
- Effective against both visible and invisible trigger attacks
- Requires only a small clean reference set (500–1000 samples)
- Inference overhead is moderate (2–3x standard inference) due to feature bank computation
- Outperforms feature-space defenses lacking causal grounding

## Relevance to LLM Backdoor Defense

FABE's causal framework offers a principled lens for understanding and defending against backdoor attacks that could transfer to LLM settings. The front-door adjustment concept — intervening on intermediate representations to block trigger effects — is particularly relevant for transformer-based models where attention patterns and hidden states serve as analogous mediating features. The approach's key strength is requiring no trigger knowledge and operating purely at inference time, making it applicable to settings where model retraining is impractical (e.g., large pre-trained LLMs). The theoretical grounding in causal inference also provides a foundation for developing more principled LLM-specific defenses beyond empirical pruning or fine-tuning.

## Related Work

- [[neural-cleanse]] — trigger reverse-engineering defense; FABE avoids the need for trigger inversion entirely
- [[fine-pruning]] — pruning-based defense; FABE operates at inference time rather than modifying model weights
- [[activation-clustering]] — feature-space analysis; FABE provides causal justification for feature-level intervention
- [[strip]] — perturbation-based detection; complementary approach that operates at the input level

## Backlinks
[[backdoor-defense]] | [[backdoor-attack]] | [[trigger-pattern]] | [[data-poisoning]] | [[trigger-reverse-engineering]]
