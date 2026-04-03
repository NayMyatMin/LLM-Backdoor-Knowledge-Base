# ASSET: Robust Backdoor Data Detection Across a Multiplicity of Deep Learning Paradigms

## Authors
Minzhou Pan, Yue Song, Jieyi Long, Qi Li, Rui Zhang, Dawn Song

## Venue
USENIX Security 2023

## Year
2023

## URL
https://arxiv.org/abs/2302.11408

## Abstract Summary
ASSET addresses the challenge of detecting backdoor-poisoned data across different machine learning paradigms, including supervised learning, self-supervised learning, and transfer learning. Existing backdoor detection methods are typically designed for a single paradigm and fail when applied to others. ASSET proposes a unified detection framework based on the observation that poisoned samples exhibit distinctive patterns in the model's learned feature space regardless of the training paradigm. The method uses an adaptive feature analysis approach that works across paradigms without requiring paradigm-specific modifications.

## Key Contributions
1. Identified that existing backdoor detection methods are paradigm-specific and fail to generalize across supervised, self-supervised, and transfer learning settings.
2. Proposed ASSET, a unified backdoor data detection framework that works across multiple ML paradigms by analyzing features in a paradigm-agnostic manner.
3. Introduced an adaptive spectral analysis method that automatically adjusts to the feature space characteristics of different paradigms and identifies the subspace most associated with backdoor behavior.
4. Demonstrated consistent detection performance across supervised learning, contrastive learning (SimCLR, MoCo), and transfer learning (fine-tuning pre-trained models) scenarios.

## Method Details
- ASSET analyzes the feature representations of training samples extracted from the model and identifies a low-dimensional subspace that separates clean and poisoned samples.
- The method applies spectral analysis (PCA/SVD) to the feature matrix but with an adaptive dimension selection procedure that identifies which principal components capture backdoor-related variance.
- A key innovation is the paradigm-agnostic feature preprocessing step that normalizes features differently depending on the statistical properties of the feature space, which vary significantly between supervised and self-supervised models.
- For each suspected target class, ASSET computes an outlier score for each sample based on its projection onto the identified backdoor-related subspace.
- Samples with outlier scores exceeding a threshold are flagged as poisoned and removed from the training set.
- The method requires only the trained model and the training dataset; no clean reference data is needed.

## Key Results
- ASSET achieved poisoned sample detection rates above 90% across supervised (image classification), self-supervised (SimCLR, MoCo), and transfer learning (pre-trained BERT fine-tuning) settings.
- In supervised learning, ASSET matched or exceeded the performance of paradigm-specific methods like Spectral Signatures and Activation Clustering.
- In self-supervised settings, where existing methods largely failed (detection rates below 50%), ASSET maintained detection rates above 85%.
- The adaptive feature analysis was shown to automatically focus on different feature dimensions depending on the paradigm, explaining its cross-paradigm robustness.
- ASSET was evaluated against 10+ different backdoor attack types and consistently outperformed baselines.
