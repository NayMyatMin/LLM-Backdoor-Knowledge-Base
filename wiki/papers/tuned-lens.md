---
title: "Eliciting Latent Predictions from Transformers with the Tuned Lens"
source: "tuned-lens.md"
venue: "NeurIPS"
year: 2023
summary: "Trains affine probes at each transformer layer to decode hidden states into vocabulary distributions, revealing how models refine predictions layer by layer and improving on the logit lens with better reliability."
tags:
  - interpretability
  - representation
compiled: "2026-04-03T22:00:00"
---

# Eliciting Latent Predictions from Transformers with the Tuned Lens

**Authors:** Nora Belrose, Zach Furman, Logan Smith, Danny Halawi, Igor Ostrovsky, Lev McKinney, Stella Biderman, Jacob Steinhardt
**Venue:** NeurIPS, 2023
**URL:** https://arxiv.org/abs/2303.08112

## Summary

The tuned lens is a method for decoding intermediate transformer representations into vocabulary-space predictions at every layer, revealing how a model's "belief" about the next token evolves through the network. Unlike the earlier logit lens (which simply applies the final unembedding matrix to intermediate hidden states), the tuned lens trains a separate affine probe for each layer to account for representational drift — the fact that features may be encoded differently at different layers. This produces more accurate and reliable prediction trajectories across models up to 20B parameters.

A key finding is that the trajectory of latent predictions contains rich information: it can detect malicious inputs with high accuracy, suggesting that backdoor triggers create anomalous prediction trajectories that deviate from the normal refinement pattern. This directly connects layer-wise analysis to security applications.

## Key Concepts

- [[logit-lens]] — the technique the tuned lens improves upon
- [[probing-classifier]] — the tuned lens is a specialized probe (affine, per-layer)
- [[mechanistic-interpretability]] — the paper contributes tools for understanding layer-wise computation

## Method Details

**Logit Lens (Baseline)**: Apply the final layer's unembedding matrix W_U to hidden state h_l at layer l to get a vocabulary distribution. Simple but unreliable because early-layer representations may use different coordinate systems than the final layer.

**Tuned Lens**: Train a separate affine transformation A_l for each layer l, learned via knowledge distillation to map h_l to the final layer's representation space before applying W_U. The probe is trained on a held-out corpus with the objective of matching the model's final-layer predictions.

**Prediction Trajectory**: For each input, the tuned lens produces a sequence of vocabulary distributions (one per layer), forming a "prediction trajectory" that shows how the model refines its prediction from early to late layers. Normal inputs follow smooth, converging trajectories.

**Malicious Input Detection**: The authors demonstrate that the prediction trajectory can distinguish normal from adversarial inputs. Adversarial or out-of-distribution inputs produce erratic trajectories that deviate from the smooth convergence pattern of clean inputs.

## Results & Findings

- Tuned lens is consistently more predictive and reliable than the logit lens across models from 70M to 20B parameters
- Prediction trajectories reveal interpretable structure: early layers handle syntactic prediction, later layers refine semantic content
- Trajectory-based anomaly detection achieves high accuracy on adversarial input detection
- Causal experiments confirm the tuned lens captures features the model actually uses

## Relevance to LLM Backdoor Defense

The tuned lens is directly relevant to runtime backdoor detection:

- **Anomalous prediction trajectories**: If backdoor triggers cause the model to suddenly shift its prediction at a specific layer (where the backdoor circuit activates), the tuned lens would reveal this as a discontinuity in the prediction trajectory. This is conceptually related to representation velocity approaches.
- **Layer-wise monitoring**: The tuned lens enables monitoring of how predictions evolve across layers, potentially detecting the "injection point" where a backdoor circuit overrides the model's natural computation.
- **Connection to LCF**: The representation velocity concept (measuring L2 norm of hidden-state differences between layers) is a complementary approach — the tuned lens tracks prediction-space changes while representation velocity tracks activation-space changes.
- **Lightweight detection**: Affine probes are computationally cheap, making layer-wise monitoring feasible at inference time.

## Related Work

- [[rome-factual-associations]] — also analyzes layer-wise computation, but through causal tracing rather than probing
- [[representation-engineering]] — a population-level approach to understanding representations
- [[zoom-in-circuits]] — the circuits framework that explains what individual layers compute
- [[transformer-circuits-framework]] — the mathematical framework for understanding layer composition

## Backlinks

- [[logit-lens]]
- [[probing-classifier]]
- [[mechanistic-interpretability]]
- [[interpretability-as-defense]]
- [[from-probing-to-detection]]
