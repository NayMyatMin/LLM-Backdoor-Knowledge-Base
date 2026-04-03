---
title: "Layer-wise Analysis"
slug: "layer-wise-analysis"
brief: "The practice of analyzing model behavior layer by layer to understand information flow, knowledge formation, and where backdoors inject their influence."
compiled: "2026-04-04T10:00:00"
---

# Layer-wise Analysis

## Definition

Layer-wise analysis is a family of interpretability techniques that examine how information is processed, transformed, and refined as it passes through successive layers of a deep neural network. In the context of LLM security, it is used to understand how backdoor signals propagate through the model and at which layers they exert their influence on the output.

## Background

Transformer-based language models process inputs through a stack of identical layers, each containing multi-head self-attention and feed-forward (MLP) sub-layers. While the overall input-output behavior of a model can be observed externally, understanding what happens *between* layers is essential for interpretability, debugging, and security analysis.

The development of tools like [[logit-lens]] and [[tuned-lens]] made it practical to inspect intermediate representations by projecting hidden states at each layer into the output vocabulary space. This revealed that models progressively refine their predictions layer by layer: early layers establish basic syntactic and semantic features, middle layers compose and route information, and later layers make final output decisions. This progressive refinement view has become a foundational framework for understanding transformer computation.

For backdoor defense, layer-wise analysis is critical because it reveals the "injection point" of a backdoor. A backdoor trigger must, at some layer, cause a divergence between the clean computation and the backdoor computation. By comparing layer-by-layer representations on triggered versus clean inputs, defenders can identify exactly where the backdoor takes effect, informing targeted interventions like [[attention-head-pruning]] or layer-specific [[neuron-pruning-defense]].

## Technical Details

### Logit Lens and Tuned Lens

**Logit lens** ([[logit-lens]]): Projects the hidden state at each layer through the model's final unembedding matrix to obtain a distribution over the vocabulary. This provides a "snapshot" of what the model would predict if forced to output at that layer. For clean inputs, the correct prediction typically emerges gradually across layers. For triggered inputs, the logit lens can reveal at which layer the backdoor target suddenly appears in the top predictions.

**Tuned lens** ([[tuned-lens]]): An improved version that trains a small affine probe at each layer to better translate intermediate representations into predictions. This corrects for the fact that intermediate representations are not optimized to be directly interpretable through the unembedding matrix, providing more accurate layer-wise prediction snapshots.

### Representation Similarity Analysis

Compare the hidden state representations at each layer between:
- Clean input and triggered input (same semantic content, trigger added)
- Clean input and unrelated input (baseline difference)

Layers where the triggered input diverges sharply from the clean input, relative to the baseline, are candidate backdoor injection layers. Common metrics include cosine similarity, centered kernel alignment (CKA), and projection-weighted distances.

### Activation Difference Tracking

For a more granular view:
1. Record activations at every layer for a batch of clean inputs
2. Record activations for the same inputs with the trigger appended
3. Compute the layer-wise difference (L2 norm, cosine distance, or per-neuron differences)
4. Plot the difference trajectory across layers

A typical backdoor signature shows small differences in early layers (the trigger has not yet been processed) and a sharp increase at the injection layer, followed by amplification in subsequent layers.

### Information Flow and Residual Stream Analysis

Since transformers use residual connections, each layer *adds* to the residual stream rather than replacing it. Layer-wise analysis can decompose the residual stream into contributions from each layer's attention and MLP components:

- **Attention contribution**: What information is being moved between token positions at each layer
- **MLP contribution**: What transformations are being applied to individual token representations
- **Cumulative effect**: How these contributions accumulate to form the final prediction

This decomposition, closely related to [[causal-tracing]], can isolate which layer's contribution introduces the backdoor signal into the residual stream.

## Variants

- **Logit lens analysis**: The simplest form, using the unembedding matrix directly on intermediate states. Fast but less accurate for early layers.
- **Tuned lens analysis**: [[tuned-lens]] provides trained probes for more faithful layer-wise prediction snapshots.
- **Probing classifiers**: Train linear or shallow classifiers on each layer's representations to detect specific features (e.g., presence of a trigger, encoding of the target label). This tests what information is *available* at each layer.
- **Gradient-based layer attribution**: Compute gradients of the output with respect to each layer's representations to quantify each layer's contribution to the final prediction.
- **Representation engineering**: [[representation-engineering]] takes layer-wise analysis further by identifying and manipulating specific directions in the representation space at targeted layers.
- **CKA-based structural analysis**: Uses centered kernel alignment to measure how representation geometry changes across layers and between clean/triggered conditions.

## Key Papers

- [[tuned-lens]] -- Introduces trained affine probes for accurate layer-wise prediction analysis, improving on the logit lens approach.
- [[logit-lens]] -- The foundational technique of projecting intermediate hidden states to vocabulary space for layer-wise inspection.
- [[rome-factual-associations]] -- Uses layer-wise causal analysis to localize factual knowledge to specific layers and components.
- [[knowledge-neurons]] -- Identifies specific neurons at specific layers responsible for factual knowledge, demonstrating layer-specific functional specialization.
- [[beear]] -- Uses representation-level analysis across layers to identify and manipulate safety-relevant directions.

## Related Concepts

- [[mechanistic-interpretability]] -- The overarching field; layer-wise analysis is one of its primary empirical methodologies.
- [[causal-tracing]] -- Extends layer-wise observation with causal interventions to establish which layers are causally responsible, not merely correlated.
- [[activation-patching]] -- Enables controlled experiments by swapping activations at specific layers between different inputs.
- [[activation-analysis]] -- Closely related concept focused on analyzing activation patterns, often conducted in a layer-wise manner.
- [[representation-engineering]] -- Builds on layer-wise understanding to actively engineer model behavior by modifying representations at targeted layers.
- [[knowledge-localization]] -- Uses layer-wise analysis to determine where in the model factual knowledge is stored.

## Open Problems

- **Interpretation of intermediate representations**: While tools like [[tuned-lens]] improve accuracy, the fundamental question of what intermediate layers "mean" remains open. Intermediate representations serve the model's computation, not human understanding.
- **Layer-wise analysis for non-standard architectures**: Most tools assume standard transformer layers; mixture-of-experts, state-space models, and hybrid architectures require new analysis methods.
- **Automated backdoor layer detection**: Translating layer-wise observations into automated, reliable backdoor detection without human interpretation is an unsolved challenge.
- **Computational overhead**: Full layer-wise analysis requires storing and comparing activations at every layer for many inputs, which is expensive for large models.
- **Dynamic layer utilization**: Models may use different layers for different inputs or tasks, meaning static layer-wise analysis may miss context-dependent backdoor behaviors.
- **Connection to training dynamics**: Understanding how backdoor information enters specific layers during training (rather than just observing it post-hoc) could enable training-time defenses.
