---
title: "Similarity of Neural Network Representations Revisited"
source: "raw/cka-representation-similarity.md"
venue: "ICML"
year: 2019
summary: "Introduces Centered Kernel Alignment (CKA) as a robust, invariant metric for comparing neural network representations across layers and models, showing same-architecture networks learn similar representations while different architectures diverge qualitatively."
compiled: "2026-04-04T16:00:00"
---

# Similarity of Neural Network Representations Revisited

**Authors:** Simon Kornblith, Mohammad Norouzi, Honglak Lee, Geoffrey Hinton
**Venue:** ICML 2019 **Year:** 2019

## Summary

Comparing representations learned by different neural networks — across layers within a network, or across entirely different models — is a fundamental problem in deep learning research. This paper introduces Centered Kernel Alignment (CKA) as a principled similarity metric that overcomes critical limitations of prior approaches. Previous metrics based on Canonical Correlation Analysis (CCA) and its variants (SVCCA, Projection Weighted CCA) suffer from sensitivity to representation dimensionality and can report low similarity between representations that are functionally equivalent. CKA resolves these issues through its invariance to orthogonal transformations and isotropic scaling, making it a reliable tool for representation comparison.

CKA is defined as the normalized Hilbert-Schmidt Independence Criterion (HSIC) between two representation sets, with a computationally efficient linear variant that strongly correlates with the more expressive RBF-kernel version. The paper establishes two key empirical results: same-architecture networks trained from different initializations develop remarkably similar representations at corresponding layers, while different architectures (ResNets vs. VGGs) develop qualitatively different representations even at similar task performance. These findings laid the foundation for [[tracing-representation-progression]] through transformer layers.

## Key Concepts

- [[mechanistic-interpretability]] — CKA enables systematic comparison of internal representations, a key tool for understanding what networks learn at each processing stage
- [[layer-wise-analysis]] — Layer-to-layer CKA similarity matrices provide a complete picture of how representations transform through network depth
- [[activation-analysis]] — CKA operates on activation matrices, providing a principled aggregation of per-sample activation information into a single similarity score
- [[tracing-representation-progression]] — CKA is the foundational metric that the Tracing paper builds upon for tracking representation changes across transformer layers
- [[prediction-trajectory]] — CKA similarity between consecutive layers characterizes the smoothness of the prediction trajectory through representation space

## Method Details

CKA is defined using the Hilbert-Schmidt Independence Criterion: given representation matrices X and Y, compute centered kernel matrices K = XX^T and L = YY^T, then CKA(K, L) = HSIC(K, L) / sqrt(HSIC(K, K) * HSIC(L, L)). The normalization ensures CKA ranges from 0 to 1. The authors prove CKA with linear kernels is invariant to orthogonal transformations and isotropic scaling, unlike CCA-based metrics which are sensitive to dimensionality truncation choices.

Multiple ResNet, VGG, and Inception instances are trained on ImageNet with different random seeds. Full layer-to-layer CKA similarity matrices are computed within and across networks, and systematically compared against CCA, SVCCA, and Projection Weighted CCA. Sensitivity analyses vary sample count (256 to full validation set) and representation dimensionality.

## Results & Findings

Within-network CKA matrices reveal block-diagonal structure: groups of consecutive layers have high mutual similarity (CKA > 0.8), separated by transition points. In ResNets, blocks align with residual block groups; in VGGs, with max-pooling boundaries. Cross-initialization CKA matrices for same-architecture networks show strong diagonal patterns (CKA > 0.9 at corresponding layers), while cross-architecture comparisons (ResNet vs. VGG) show no diagonal pattern (CKA typically below 0.5).

Linear CKA correlates above 0.95 with RBF-kernel CKA across all conditions. CKA is stable with as few as 256 samples (less than 2% variation), making it feasible for monitoring. CCA-based metrics show up to 30% variation depending on truncation and sample size.

## Relevance to LLM Backdoor Defense

CKA provides the metric foundation for detecting backdoors through [[layer-wise-analysis]] of representation dynamics. The [[tracing-representation-progression]] paper directly extends CKA to transformer language models, using inter-layer CKA similarity to characterize normal representation evolution and detect deviations caused by [[backdoor-attack]] activation. By establishing what "normal" inter-layer similarity looks like — smooth, gradual decreases in CKA between increasingly distant layers — defenders can flag inputs that produce anomalous similarity patterns as potentially triggered.

CKA's invariance properties are particularly valuable for backdoor detection across different model architectures and training configurations. A detection system calibrated using CKA on one model checkpoint should generalize to other checkpoints of the same architecture, since CKA is invariant to the arbitrary rotations and scalings that different training runs introduce. The finding that simpler metrics like cosine similarity correlate well with CKA under many practical conditions — as confirmed by the [[tracing-representation-progression]] paper — justifies using computationally cheaper alternatives for real-time [[inference-time-defense]] while maintaining the theoretical soundness that CKA provides.

The block-diagonal structure in CKA matrices also informs detection strategy: monitoring transitions between representation blocks may be more informative than within-block changes, as backdoor activation likely forces a representation to jump between blocks.

## Related Work

- [[tracing-representation-progression]] — Directly builds on CKA for tracing layer-wise representation changes in transformers, the primary application of CKA to backdoor detection
- [[layer-by-layer-hidden-representations]] — Uses representation quality metrics that complement CKA's similarity-based perspective on layer-wise dynamics
- [[belief-state-geometry-residual-stream]] — The geometric analysis of residual stream content parallels CKA's geometric approach to representation comparison
- [[exploring-residual-stream]] — Provides the logit-level decomposition that complements CKA's activation-level similarity analysis

## Backlinks

[[mechanistic-interpretability]] | [[layer-wise-analysis]] | [[activation-analysis]] | [[tracing-representation-progression]] | [[prediction-trajectory]] | [[inference-time-defense]] | representation velocity | centered kernel alignment
