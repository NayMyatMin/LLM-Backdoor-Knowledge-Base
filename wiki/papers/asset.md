---
title: "ASSET: Robust Backdoor Data Detection Across a Multiplicity of Deep Learning Paradigms"
source: raw/asset-robust-backdoor-detection-ml-paradigms.md
venue: USENIX Security
year: 2023
summary: "ASSET is a unified backdoor data detection framework that works across supervised, self-supervised, and transfer learning paradigms by using adaptive spectral analysis of feature representations to identify poisoned samples without paradigm-specific modifications."
compiled: "2026-04-03T16:00:00"
---

# ASSET: Robust Backdoor Data Detection Across a Multiplicity of Deep Learning Paradigms

**Authors:** Minzhou Pan, Yue Song, Jieyi Long, Qi Li, Rui Zhang, Dawn Song
**Venue:** USENIX Security 2023 **Year:** 2023

## Summary

Existing backdoor detection methods are typically designed for a single machine learning paradigm (e.g., supervised learning) and fail when applied to other paradigms such as self-supervised or transfer learning. ASSET addresses this cross-paradigm gap by proposing a unified detection framework grounded in the observation that poisoned samples exhibit distinctive patterns in the model's learned feature space regardless of how the model was trained.

The method uses an adaptive spectral analysis approach that automatically adjusts to the feature space characteristics of different paradigms. A paradigm-agnostic preprocessing step normalizes features based on their statistical properties, which vary significantly between supervised and self-supervised models. This allows ASSET to identify the low-dimensional subspace separating clean and poisoned samples across paradigms.

ASSET achieves detection rates above 90% across supervised image classification, self-supervised contrastive learning (SimCLR, MoCo), and transfer learning (fine-tuning pre-trained BERT), significantly outperforming paradigm-specific baselines especially in self-supervised settings where existing methods largely fail.

## Key Concepts

- [[backdoor-defense]] — training data inspection for poisoned sample removal
- [[spectral-signatures]] — builds on spectral methods with adaptive dimension selection
- [[activation-clustering]] — related feature-space analysis approach
- [[data-poisoning]] — the threat model ASSET defends against
- [[trigger-pattern]] — detected via feature-space anomalies across paradigms

## Method Details

ASSET analyzes feature representations of training samples extracted from the model to identify a low-dimensional subspace that separates clean and poisoned samples. The pipeline works as follows:

1. **Feature extraction**: Extract representations for all training samples from an intermediate or final layer of the trained model.
2. **Paradigm-agnostic preprocessing**: Normalize features differently depending on the statistical properties of the feature space. Supervised models and self-supervised models produce feature distributions with different characteristics, and ASSET adapts accordingly.
3. **Adaptive spectral analysis**: Apply PCA/SVD to the feature matrix with an adaptive dimension selection procedure that identifies which principal components capture backdoor-related variance, rather than assuming fixed dimensions.
4. **Outlier scoring**: For each suspected target class, compute an outlier score for each sample based on its projection onto the identified backdoor-related subspace.
5. **Filtering**: Samples with outlier scores exceeding a threshold are flagged as poisoned and removed from the training set.

The method requires only the trained model and the training dataset — no clean reference data is needed.

## Results & Findings

- Detection rates above 90% across supervised, self-supervised (SimCLR, MoCo), and transfer learning settings.
- Matched or exceeded paradigm-specific methods like [[spectral-signatures]] and [[activation-clustering]] in supervised learning.
- In self-supervised settings where existing methods failed (detection rates below 50%), ASSET maintained rates above 85%.
- The adaptive feature analysis automatically focuses on different feature dimensions depending on the paradigm.
- Evaluated against 10+ different [[backdoor-attack]] types with consistent outperformance of baselines.

## Relevance to LLM Backdoor Defense

ASSET's cross-paradigm approach is directly relevant to LLM security because modern LLMs are trained and adapted through diverse paradigms — pre-training, fine-tuning, [[instruction-tuning]], and prompt-based learning. A defense that works across these paradigms without modification is far more practical than paradigm-specific solutions. The transfer learning evaluation (fine-tuning pre-trained BERT) is particularly relevant, demonstrating that spectral methods can detect poisoned samples in foundation model adaptation pipelines.

## Related Work

- [[spectral-signatures]] — ASSET extends spectral analysis with adaptive dimension selection
- [[activation-clustering]] — alternative feature-space clustering approach for poison detection
- [[fine-pruning]] — complementary defense operating on model weights rather than data
- [[strip]] — test-time detection approach, whereas ASSET operates on training data

## Backlinks

[[backdoor-defense]] | [[data-poisoning]] | [[spectral-signatures]] | [[activation-clustering]] | [[trigger-pattern]]