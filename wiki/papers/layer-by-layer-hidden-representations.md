---
title: "Layer by Layer: Uncovering Hidden Representations in Language Models"
source: "raw/layer-by-layer-hidden-representations.md"
venue: "ICML"
year: 2025
summary: "Challenges the assumption that final transformer layers produce the best representations, demonstrating through a unified multi-metric framework that intermediate layers often encode richer, more informative features across 32 text-embedding benchmarks."
compiled: "2026-04-04T16:00:00"
---

# Layer by Layer: Uncovering Hidden Representations in Language Models

**Authors:** Oscar Skean, Md Rifat Arefin, Dan Zhao, Niket Patel, Jalal Naghiyev, Yann LeCun, Ravid Shwartz-Ziv
**Venue:** ICML 2025 (Oral) **Year:** 2025

## Summary

This paper overturns the long-held assumption in the NLP community that deeper transformer layers always produce superior representations. Through a systematic evaluation across 32 text-embedding benchmarks spanning classification, retrieval, and clustering tasks, the authors demonstrate that intermediate layers — roughly 60-75% through the network — frequently outperform the final layer on downstream tasks. The finding holds across both transformer architectures (BERT, GPT-2, LLaMA) and state-space models (Mamba), suggesting it reflects a general property of deep sequence models rather than a transformer-specific quirk.

The paper introduces a unified framework for evaluating [[layer-wise-analysis]] representation quality using three complementary lenses. The information-theoretic lens measures mutual information between layer activations and task labels. The geometric lens quantifies intrinsic dimensionality of the representation manifold at each layer. The robustness lens evaluates invariance to input perturbations such as synonym substitution and paraphrasing. All three metrics converge on the same conclusion: intermediate layers encode richer, more transferable features than the final layer.

The authors argue that the final layer is specialized for the pretraining objective (typically next-token prediction), which actively discards information that is useful for other tasks. Intermediate layers, by contrast, maintain a broader information landscape before this specialization narrows it. The effect is more pronounced in larger models, where the representational capacity allows deeper specialization in later layers. This provides a principled explanation for why approaches like [[tuned-lens]] and [[logit-lens]] can extract meaningful predictions from intermediate layers.

## Key Concepts

- [[layer-wise-analysis]] — Studying how representations evolve through the depth of a neural network, central to understanding what each layer contributes
- [[mechanistic-interpretability]] — The broader research program of understanding neural network internals, which this paper advances by characterizing per-layer representation quality
- [[prediction-trajectory]] — The evolution of the model's implicit prediction across layers, which this paper shows peaks in quality before the final layer
- intrinsic dimensionality — A geometric measure of the effective complexity of representations at each layer, found to follow an inverted-U pattern
- [[tuned-lens]] — A method for reading predictions from intermediate layers that benefits from this paper's finding that those layers are informationally rich
- [[logit-lens]] — A simpler approach to projecting intermediate representations into vocabulary space, validated by this paper's results

## Method Details

The authors extract activations from every layer of pretrained language models and evaluate them using the MTEB (Massive Text Embedding Benchmark) protocol across 32 tasks. For each layer, they compute three metrics: mutual information between activations and downstream task labels (via neural estimators), intrinsic dimensionality of the representation manifold (via maximum likelihood estimation), and perturbation invariance measured as representation stability under synonym substitution and paraphrasing.

The evaluation spans transformer models from 125M to 7B parameters and Mamba state-space models up to 2.8B parameters. For each model and task, the optimal layer is compared against the standard practice of using the final layer.

## Results & Findings

Across the 32 benchmarks, intermediate layers (60-75% depth) outperform the final layer on 78% of tasks. Mutual information peaks at intermediate depth and declines by 15-25% toward the final layer. Intrinsic dimensionality follows an inverted-U curve, peaking at approximately 65% depth with values 2-3x higher than the final layer. The intermediate-layer advantage increases with model scale: 7B-parameter models show a 12% improvement from optimal layer selection versus final layer, compared to 5% for 125M models. State-space models exhibit similar patterns. Classification tasks favor slightly earlier layers than retrieval tasks, but both peak well before the final layer.

## Relevance to LLM Backdoor Defense

This paper provides critical theoretical and empirical grounding for why representation velocity-based backdoor detection should monitor intermediate layers rather than the output layer. If intermediate layers encode the richest representations, then a [[backdoor-attack]] that hijacks model behavior must manipulate these information-dense layers, making disruptions at those depths particularly detectable. The finding directly supports the design choice in [[tracing-representation-progression]] to monitor layers at specific intermediate depths (e.g., layer N-3) rather than the final layer.

The unified metric framework also offers tools for calibrating detection thresholds: by characterizing normal mutual information and intrinsic dimensionality profiles, defenders can establish baselines against which anomalous dynamics from [[trigger-pattern]] activation can be detected. The cross-architecture generality suggests intermediate-layer monitoring should transfer across model families.

## Related Work

- [[tracing-representation-progression]] — Builds directly on the insight that inter-layer representation changes carry diagnostic information, using cosine similarity and CKA to trace progression
- [[tuned-lens]] — Learned probes for reading intermediate-layer predictions, validated by this paper's finding of rich intermediate representations
- [[logit-lens]] — Projects intermediate residual stream states to vocabulary space; this paper explains why such projections carry meaningful signal
- [[cka-representation-similarity]] — CKA metric used for comparing representations across layers, one of the analytical tools underlying this paper's framework

## Backlinks

[[layer-wise-analysis]] | [[mechanistic-interpretability]] | [[prediction-trajectory]] | intrinsic dimensionality | [[tuned-lens]] | [[logit-lens]] | [[tracing-representation-progression]] | representation velocity | [[inference-time-defense]]
