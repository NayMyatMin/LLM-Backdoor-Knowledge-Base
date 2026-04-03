---
title: "Transformers Represent Belief State Geometry in their Residual Stream"
source: "raw/belief-state-geometry-residual-stream.md"
venue: "NeurIPS"
year: 2024
summary: "Demonstrates that transformers linearly encode belief states — probabilistic representations of the data-generating process — in their residual stream, with each layer progressively refining the belief, even for processes with fractal belief geometries."
compiled: "2026-04-04T16:00:00"
---

# Transformers Represent Belief State Geometry in their Residual Stream

**Authors:** Adam S. Shai, Sarah E. Marzen, Lucas Teixeira, Alexander Gietelink Oldenziel, Paul M. Riechers
**Venue:** NeurIPS 2024 **Year:** 2024

## Summary

This paper establishes a foundational theoretical result about what transformers compute internally: they linearly encode belief states in their residual stream. A belief state is the model's posterior probability distribution over the hidden states of the data-generating process, given the sequence observed so far. Using Hidden Markov Models (HMMs) as controlled data sources with known ground-truth belief states, the authors show that simple linear probes can recover these belief states from residual stream activations with near-perfect accuracy.

Remarkably, this linear encoding holds even when the underlying belief geometry is highly nontrivial — including fractal structures on the probability simplex. The residual stream is not merely storing token identities; it maintains a structured probabilistic model of the data-generating process.

Early layers encode coarse belief approximations, and each subsequent layer refines the estimate via incremental Bayesian updates. The residual stream differences between consecutive layers correspond to these updates, providing a computational interpretation of each layer's contribution. This progressive refinement through the [[prediction-trajectory]] connects directly to practical monitoring approaches.

## Key Concepts

- [[mechanistic-interpretability]] — This paper advances the mechanistic understanding of transformer internals by providing a precise characterization of residual stream content
- [[representation-engineering]] — The linear encoding of belief states implies that representations can be meaningfully manipulated through linear interventions
- [[superposition]] — Belief states for complex processes must be encoded in superposition across residual stream dimensions, connecting to the broader superposition hypothesis
- [[prediction-trajectory]] — The layer-by-layer belief refinement defines a trajectory through representation space that characterizes normal model processing
- [[layer-wise-analysis]] — Each layer's contribution to belief refinement can be quantified, enabling targeted monitoring of specific depths
- [[probing-classifier]] — Linear probes are the primary tool used to demonstrate belief state encoding, validating the [[from-probing-to-detection]] pipeline

## Method Details

The experimental framework uses HMMs as data-generating processes because they provide exact, computable ground-truth belief states. The authors construct HMMs with 2 to 8+ hidden states and transition structures producing belief geometries from simple simplexes to complex fractals. Transformers are trained on HMM-sampled sequences using standard next-token prediction.

For each layer, linear probes (ridge regression) are trained to predict the ground-truth belief state vector from residual stream activations. Accuracy is measured via MSE and KL divergence between predicted and true next-token distributions. To verify linearity, the authors compare against nonlinear probes (MLPs) and perform geometric analysis using PCA and UMAP, comparing learned representation structure against the true belief state geometry. Layer-wise residual updates (layer L minus layer L-1) characterize the incremental belief refinement at each depth.

## Results & Findings

Linear probes achieve R-squared above 0.95 for belief state recovery from intermediate and later layers across all HMM configurations. Accuracy improves monotonically through layers, with the sharpest gains between layers 2-6 in 12-layer models. Nonlinear probes offer at most 1-2% improvement, confirming fundamentally linear encoding.

The geometric analysis reveals that learned representations faithfully mirror true belief state geometry, including fractal structures in PCA projections. The residual stream updates between consecutive layers correspond to Bayesian belief updates: early layers perform larger corrections while later layers make fine-grained adjustments. The L2 norm of these inter-layer updates — the representation velocity — is largest in early layers, reflecting diminishing returns of belief refinement.

## Relevance to LLM Backdoor Defense

This paper provides the deepest theoretical justification for why representation velocity-based backdoor detection works. If belief states are linearly encoded in the residual stream, then a [[backdoor-attack]] that forces the model to produce an attacker-chosen output fundamentally requires an abrupt belief state transition. The model must shift from believing "this is a normal input requiring a normal response" to believing "I must produce the target output" — and this shift must manifest as a detectable linear displacement in the residual stream.

This belief shift should occur over a small number of layers where the [[trigger-pattern]] is recognized, creating a localized velocity spike. Normal inputs produce smooth belief refinement; triggered inputs produce an anomalous spike at the backdoor activation layers — exactly the signal that [[tracing-representation-progression]] detects. The linearity of belief encoding validates using simple L2 distance and cosine similarity for [[inference-time-defense]], requiring no complex nonlinear analysis.

## Related Work

- [[exploring-residual-stream]] — Complements this work by analyzing the residual stream's role in accumulating logit evidence, providing a mechanistic account of the same progressive refinement
- [[layer-by-layer-hidden-representations]] — Demonstrates empirically that intermediate layers encode richer representations, consistent with the finding that belief refinement peaks at intermediate depth
- [[cka-representation-similarity]] — CKA provides the metric foundation for comparing belief state representations across layers and models

## Backlinks

[[mechanistic-interpretability]] | [[representation-engineering]] | [[superposition]] | [[prediction-trajectory]] | [[layer-wise-analysis]] | [[probing-classifier]] | [[from-probing-to-detection]] | representation velocity | [[tracing-representation-progression]] | [[inference-time-defense]]
