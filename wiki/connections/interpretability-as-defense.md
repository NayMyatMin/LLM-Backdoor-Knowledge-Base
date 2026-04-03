---
title: "Interpretability as Defense: Mech Interp Tools Repurposed for Backdoor Detection"
slug: "interpretability-as-defense"
compiled: "2026-04-03T22:00:00"
---

# Interpretability as Defense

## Connection

The tools of [[mechanistic-interpretability]] — developed to understand how neural networks compute — are increasingly being repurposed for backdoor detection and defense. This convergence is not coincidental: detecting a backdoor requires answering the same question interpretability asks — "what is this model actually computing?" — but with a security-specific focus: "is this model computing something it shouldn't be?"

## The Convergence

### Probing and Representation Reading

[[probing-classifier|Probing classifiers]], designed to test what information representations encode, are natural backdoor detectors. If a probe trained on hidden states can distinguish triggered from clean inputs, the model internally represents trigger presence as a decodable feature. This is exactly what [[spectral-signatures]] and [[activation-clustering]] do, reframed: SVD finds the top probe direction, clustering finds the non-parametric probe boundary.

[[representation-engineering]] takes this further — its contrastive direction-finding method extracts a "backdoor direction" by comparing activations on triggered vs. clean inputs. [[beear]] directly operationalizes this for safety backdoor removal.

### Layer-wise Analysis

The [[logit-lens]] and [[tuned-lens]] track how a model's predictions evolve across layers. For backdoor detection, this reveals the "injection point" — the layer where the backdoor circuit overrides the model's natural prediction. A clean input's prediction trajectory converges smoothly; a triggered input may show a sudden shift at the layer where the backdoor activates.

This principle underlies representation velocity approaches: measuring the L2 norm of hidden-state differences between adjacent layers to detect anomalous layer-wise dynamics that indicate backdoor activation.

### Circuit Discovery

[[activation-patching]] and [[circuit-analysis]], designed to identify which model components implement specific behaviors, can directly identify the backdoor circuit. [[mechanistic-exploration-backdoors]] demonstrates this, finding that backdoor attention signatures are concentrated in specific layers and heads — precisely the information needed for targeted removal via [[pure-head-pruning]] or similar approaches.

### Feature Decomposition

[[sparse-autoencoder|Sparse autoencoders]], developed to resolve [[superposition]] and find interpretable features, could isolate backdoor-specific features from legitimate ones. While not yet systematically evaluated for backdoor detection, SAEs represent a frontier approach: if a backdoor creates a detectable internal feature, SAEs should be able to find it.

## Why This Convergence Matters

The convergence suggests that backdoor defense and interpretability are two sides of the same coin. Both require understanding model internals at a mechanistic level. As interpretability tools improve (more scalable SAEs, better automated circuit discovery, more reliable probing), backdoor defenses inherit these improvements for free.

Conversely, backdoor defense provides interpretability with a concrete, testable application domain: a backdoored model is a model with a known internal structure (the backdoor circuit), making it an ideal test case for interpretability methods.

## Related Papers

- [[mechanistic-exploration-backdoors]] — direct application of mech interp to backdoor analysis
- [[representation-engineering]] — RepE for monitoring safety-relevant properties
- [[tuned-lens]] — layer-wise prediction tracking with anomaly detection applications
- [[towards-monosemanticity]] — SAE-based feature decomposition
- [[beear]] — RepE-style direction removal for backdoor mitigation
- [[pure-head-pruning]] — targeted head pruning informed by circuit analysis
- [[spectral-signatures]] — an early, implicit use of representation-space probing

## Related Concepts

- [[mechanistic-interpretability]], [[circuit-analysis]], [[probing-classifier]], [[sparse-autoencoder]]
- [[activation-analysis]], [[embedding-space-defense]], [[backdoor-defense]]
