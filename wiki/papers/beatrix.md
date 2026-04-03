---
title: "Beatrix: Robust Backdoor Detection via Gram Matrices"
source: raw/beatrix-robust-backdoor-detection-gram-matrices.md
venue: NDSS
year: 2023
summary: "Beatrix uses Gram matrices of neural network activations to capture higher-order feature correlations that distinguish clean from poisoned inputs, achieving robust detection even against adaptive attacks that evade first-order statistical methods."
compiled: "2026-04-03T16:00:00"
---

# Beatrix: Robust Backdoor Detection via Gram Matrices

**Authors:** Wanlun Ma, Derui Wang, Ruoxi Sun, Minhui Xue, Sheng Wen, Yang Xiang
**Venue:** NDSS 2023 **Year:** 2023

## Summary

Beatrix introduces Gram matrix analysis as a novel statistical tool for backdoor detection. The key insight is that while first-order statistics (mean activations) may not reveal backdoor behavior, the pairwise correlations between features captured by Gram matrices expose the distinctive patterns that backdoor triggers create in a model's internal representations.

Gram matrices capture higher-order feature correlations — specifically, the co-activation patterns that backdoor triggers induce across feature channels. A reference distribution of Gram matrix statistics is established from a small clean validation set for each class, and deviations from this distribution at test time indicate potential backdoor activation. The same framework supports both test-time input detection and training-time data inspection.

Beatrix achieved detection AUC above 0.95 on 10 different backdoor attacks on CIFAR-10 and GTSRB, and critically maintained AUC above 0.90 against adaptive attacks designed to evade first-order methods, where those methods dropped to near random chance.

## Key Concepts

- [[backdoor-defense]] — detection via higher-order activation statistics
- [[trigger-pattern]] — creates distinctive co-activation patterns captured by Gram matrices
- [[backdoor-attack]] — detected through feature correlation anomalies
- [[data-poisoning]] — training data inspection capability for identifying poisoned samples

## Method Details

1. **Gram matrix computation**: For each layer in the neural network, compute the Gram matrix G = A^T · A from the activation matrix A. This captures pairwise correlations between all feature channels.
2. **Reference distribution**: Establish a reference distribution of Gram matrix statistics using a small set of clean validation samples for each class.
3. **Test-time detection**: Compare the Gram matrix of a new input to the reference distribution using a statistical distance measure. Significant deviations indicate potential backdoor activation.
4. **Training data inspection**: Compute Gram matrices for all training samples and identify clusters whose Gram statistics deviate from the majority, flagging them as poisoned.
5. **Multi-layer aggregation**: Analyze Gram matrices at multiple layers and aggregate detection signals for robust detection.

The key advantage is that Gram matrices capture feature interactions (e.g., the co-activation of specific features) that backdoor triggers create but that are invisible to methods analyzing individual feature statistics.

## Results & Findings

- Detection AUC above 0.95 on 10 different backdoor attacks on CIFAR-10 and GTSRB.
- Outperformed [[spectral-signatures]], [[activation-clustering]], and [[strip]].
- Against adaptive attacks designed to match first-order activation statistics, Beatrix maintained AUC above 0.90 while first-order methods dropped to near random chance.
- Training data inspection identified >92% of poisoned samples with false positive rates below 3%.
- Approximately 15% increase in inference time — modest computational overhead.
- Generalized across architectures (ResNet, VGG, DenseNet) without architecture-specific tuning.

## Relevance to LLM Backdoor Defense

Beatrix's approach of analyzing higher-order feature correlations is relevant to LLM backdoor defense because it demonstrates that backdoor signatures exist in the correlation structure of activations, not just their magnitudes. For LLMs, where activation patterns are high-dimensional and complex, Gram-matrix-style analysis of transformer attention patterns or hidden state correlations could provide a detection method that is robust against adaptive attackers who specifically design triggers to evade simpler activation-based defenses.

## Related Work

- [[spectral-signatures]] — first-order spectral analysis that Beatrix improves upon with higher-order statistics
- [[activation-clustering]] — feature-space clustering approach; Beatrix provides a more robust statistical framework
- [[strip]] — perturbation-based input detection; Beatrix offers a complementary internal analysis approach
- [[neural-cleanse]] — trigger reconstruction approach; Beatrix detects without needing to reverse-engineer the trigger
- [[asset]] — another robust detection method using adaptive spectral analysis

## Backlinks
[[backdoor-defense]] | [[trigger-pattern]] | [[backdoor-attack]] | [[data-poisoning]] | [[attack-success-rate]]
