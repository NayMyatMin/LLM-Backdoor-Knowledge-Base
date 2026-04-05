---
title: "Steering Llama 2 via Contrastive Activation Addition"
source: "raw/contrastive-activation-addition.md"
venue: "ACL"
year: 2024
summary: "Computes steering vectors from residual stream activation differences between behavioral examples and steers Llama 2 behavior at inference time across multiple safety-relevant properties."
tags:
  - interpretability
  - steering
compiled: "2026-04-04T14:00:00"
---

# Steering Llama 2 via Contrastive Activation Addition

**Authors:** Nina Rimsky, Nick Gabrieli, Julian Schulz, Meg Tong, Evan Hubinger, Alexander Matt Turner
**Venue:** ACL **Year:** 2024

## Summary

Contrastive Activation Addition (CAA) provides a systematic method for steering LLM behavior at inference time by adding or subtracting "steering vectors" computed from the residual stream. The approach is conceptually simple: create paired prompts that exhibit and do not exhibit a target behavior, run both through the model, compute the mean difference in residual stream activations at a chosen layer, and use this difference vector to steer the model during generation. By adding the vector, the behavior is amplified; by subtracting it, the behavior is suppressed.

The paper stands out for its breadth of evaluation. Rather than testing on a single behavior, Rimsky et al. systematically evaluate CAA on Llama 2 13B Chat across multiple safety-relevant behavioral dimensions including sycophancy, corrigibility, power-seeking, refusal, survival instinct, and hallucination. This broad evaluation reveals that most safety-relevant behaviors are steerable via simple linear operations on the residual stream, establishing the generality of the linear representation hypothesis for behavioral properties.

A key practical finding is that single-layer steering at middle layers (around layer 15 of 40 for Llama 2 13B) is typically more effective than steering at all layers simultaneously. This layer-specificity suggests that behavioral representations are most manipulable at a particular depth in the processing pipeline, consistent with findings from [[inference-time-intervention]] about the localization of behavioral computations.

## Key Concepts

- [[representation-engineering]] — CAA is a core technique within the representation engineering framework for reading and writing behavioral directions
- [[probing-classifier]] — Probing reveals linear structure; CAA exploits that structure for steering
- [[safety-backdoor]] — CAA demonstrates that safety behaviors (refusal, corrigibility) are steerable, with implications for backdoor vulnerability
- [[inference-time-defense]] — Steering operates purely at inference time with no model retraining
- [[from-probing-to-detection]] — If you can steer with a direction, you can detect when the model moves in that direction

## Method Details

### Steering Vector Computation

For each target behavior, a dataset of N paired prompts is constructed. Each pair consists of a positive example (exhibiting the behavior) and a matched negative example (not exhibiting it). Both versions are run through the model, and residual stream activations are extracted at a chosen layer l for the last token position. The steering vector is computed as the mean difference: v = (1/N) * sum_i (h_positive_i - h_negative_i). This averaging isolates the behavioral direction by canceling out prompt-specific content features.

### Layer Selection

The authors evaluate steering at each individual layer and find that middle layers (approximately layers 13-17 of 40 for Llama 2 13B) consistently produce the strongest steering effects. Very early layers lack sufficient behavioral encoding, while very late layers may have representations that are too committed to the original output distribution to be effectively redirected. All-layer steering (adding the vector at every layer) is generally less effective than single-layer steering, likely because it over-constrains the model's computation.

### Inference-Time Application

During generation, at each forward pass the steering vector is added to the residual stream at the chosen layer: h_l' = h_l + alpha * v. The coefficient alpha controls the strength: positive alpha amplifies the behavior, negative alpha suppresses it. Typical effective values of alpha range from 1 to 10, depending on the behavior and model. The steering is applied at every token generation step throughout the sequence.

### Multi-Behavior Analysis

The systematic evaluation across behaviors reveals varying degrees of steerability. Sycophancy, corrigibility, and power-seeking are highly steerable (large behavioral shifts with moderate alpha). Refusal is steerable in both directions — critically important from a safety perspective, as it means an adversary could potentially use CAA-like methods to bypass safety training. Hallucination is harder to steer, suggesting it may involve more distributed or nonlinear representations.

## Results & Findings

Sycophantic agreement can be reduced from approximately 80% to 30% with negative steering or increased to 95% with positive steering. Corrigibility and power-seeking show meaningful shifts in both directions across multiple evaluation scenarios. Refusal behavior is steerable both up (more refusal) and down (less refusal), demonstrating that safety training creates linear features that are as manipulable as any other behavior. Middle layers (layers 13-17) are consistently most effective, with single-layer steering outperforming all-layer steering. The method requires only 200 or more prompt pairs for stable steering vectors. Steering vectors transfer robustly across different evaluation prompt formats not seen during vector computation.

## Relevance to LLM Backdoor Defense

CAA has profound implications for backdoor detection and defense. The central finding — that behavioral properties including safety-critical ones like refusal are encoded as approximately linear directions in the residual stream — directly implies that backdoor activation should also manifest as a linear direction. If a backdoor trigger causes the model to switch from safe to unsafe behavior, this switch should correspond to a movement along a detectable direction in activation space, just as sycophancy or power-seeking correspond to their respective directions.

The practical implication for detection is powerful: if you can compute a steering vector for a behavior, you can also build a detector for when that behavior is being activated. The same contrastive methodology used to compute steering vectors can be inverted for monitoring. By projecting live activations onto known behavioral directions, a detector could flag when the model's residual stream moves anomalously along a direction associated with backdoor activation. The finding that these directions are layer-localized (most readable at middle layers) provides guidance on where to place monitoring probes. This connects CAA directly to [[representation-engineering]] defense strategies and the [[from-probing-to-detection]] pipeline, where the same linear structure that enables steering also enables surveillance.

## Related Work

- [[inference-time-intervention]] — Complementary approach steering via attention head activations rather than residual stream; both confirm linear behavioral encoding
- [[dola-decoding-contrasting-layers]] — Exploits layer contrasts for factuality; shares the principle that inter-layer differences carry behavioral signal
- [[tracing-representation-progression]] — Provides theoretical context for why middle layers are most effective for steering
- [[representation-engineering]] — Broader framework encompassing CAA as a steering technique

## Backlinks

[[representation-engineering]] | [[probing-classifier]] | [[safety-backdoor]] | [[inference-time-defense]] | [[from-probing-to-detection]] | [[mechanistic-interpretability]] | [[adversarial-unlearning]]
