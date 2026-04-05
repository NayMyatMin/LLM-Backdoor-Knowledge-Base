---
title: "Sparse Autoencoders Learn Monosemantic Features in Vision-Language Models"
source: "raw/sae-vlm-monosemantic.md"
venue: "NeurIPS"
year: 2025
summary: "Extends sparse autoencoder interpretability to vision-language models, showing SAEs enhance neuron monosemanticity and enable cross-modal steering via vision encoder interventions."
tags:
  - interpretability
  - multimodal
  - activation-analysis
compiled: "2026-04-04T12:00:00"
---

# Sparse Autoencoders Learn Monosemantic Features in Vision-Language Models

**Authors:** Mateusz Pach, Tomasz Korbak, Wieland Brendel
**Venue:** NeurIPS **Year:** 2025

## Summary

This paper extends the application of [[sparse-autoencoder]] methods from language-only models to vision-language models (VLMs) such as CLIP. The authors demonstrate that SAEs significantly enhance the monosemanticity of individual neurons in VLM representations, decomposing polysemantic activations into interpretable, single-concept features. This addresses the [[superposition]] problem in multimodal settings -- where individual neurons respond to multiple unrelated concepts -- by learning an overcomplete dictionary of monosemantic features.

The central finding is that SAE features in VLMs are 3-5x more monosemantic than raw neurons, as measured by concept purity metrics. More importantly, the work demonstrates that SAE-based interventions on the vision encoder alone can directly steer multimodal outputs without requiring any modification to the language model component. Amplifying a specific visual feature (e.g., "dog") in the vision encoder increases dog-related outputs from the language model, establishing a direct cross-modal causal pathway through monosemantic features.

For the backdoor defense domain, this work is particularly significant because backdoor triggers in multimodal models are often embedded in visual inputs -- adversarial patches, watermarks, or pixel-level perturbations. SAE decomposition offers a principled method to identify and isolate the features that encode these triggers, enabling feature-level detection and mitigation of [[multimodal-backdoor]] attacks.

## Key Concepts

- [[sparse-autoencoder]] -- core method; decomposes polysemantic neurons into monosemantic features
- [[superposition]] -- the problem SAEs solve; multiple concepts encoded in single neurons
- [[mechanistic-interpretability]] -- broader research program this work contributes to
- [[towards-monosemanticity]] -- foundational SAE work on language models that this extends
- [[multimodal-backdoor]] -- attack category where SAE decomposition enables trigger detection

## Method Details

The approach applies SAEs to intermediate representations of vision-language models in three stages:

**SAE Training:** Sparse autoencoders are trained on the hidden activations of CLIP's vision encoder (ViT layers). The SAE architecture uses an overcomplete dictionary -- learning more features than the original dimensionality -- with a sparsity penalty that ensures each input activates only a small subset of features. Each learned feature ideally corresponds to a single interpretable visual concept.

**Monosemanticity Evaluation:** For each learned SAE feature, monosemanticity is measured by evaluating how consistently it activates for a single visual concept across a diverse image dataset. The authors introduce concept purity metrics adapted for multimodal settings, comparing SAE features against raw neuron activations to quantify the interpretability improvement.

**Feature Intervention and Cross-Modal Steering:** To demonstrate practical utility, the authors perform targeted interventions: amplifying or suppressing specific SAE features in the vision encoder and observing resulting changes in the language model's outputs. This establishes causal links between monosemantic visual features and multimodal behavior, confirming that the decomposition captures functionally meaningful units.

**Models Evaluated:** Experiments are conducted on CLIP ViT-B/16 and ViT-L/14, with SAEs trained at various dictionary sizes and sparsity levels.

## Results & Findings

- **Monosemanticity:** SAE features are 3-5x more monosemantic than raw VLM neurons on concept purity metrics
- **Cross-modal steering:** Amplifying visual SAE features (e.g., "dog") directly increases dog-related language model outputs without LM modification
- **Model generality:** Strong results on both CLIP ViT-B/16 and ViT-L/14 architectures
- **Feature granularity:** Identified features correspond to fine-grained visual concepts including textures, object parts, and spatial relationships
- **Spurious correlation detection:** Some SAE features correspond to spurious correlations in training data, suggesting utility for bias detection
- **No LM retraining needed:** Vision encoder interventions steer the full VLM pipeline without touching the language component

## Relevance to LLM Backdoor Defense

This work opens a new front for backdoor defense in multimodal systems. Backdoor attacks on VLMs often embed triggers in the visual modality -- adversarial patches, watermarks, or subtle pixel perturbations that are invisible to human inspection but activate malicious behavior in the model. SAE decomposition provides a principled framework for isolating the internal features that respond to these triggers. If a backdoor trigger activates a specific SAE feature (or small set of features) that is not associated with any legitimate visual concept, this anomaly can be detected and the feature suppressed. This connects to the broader [[mechanistic-interpretability]] approach to backdoor defense: rather than searching for triggers in input space, defenders can search for anomalous features in representation space.

## Related Work

- [[towards-monosemanticity]] -- foundational SAE interpretability work on language models
- [[sparse-autoencoder]] -- dictionary learning approach extended to VLMs
- [[activation-clustering]] -- alternative representation-level backdoor detection method
- [[spectral-analysis-defense]] -- statistical method for detecting backdoor signatures
- [[multimodal-backdoor]] -- threat model this work helps defend against

## Backlinks

[[sparse-autoencoder]] | [[superposition]] | [[mechanistic-interpretability]] | [[towards-monosemanticity]] | [[multimodal-backdoor]]
