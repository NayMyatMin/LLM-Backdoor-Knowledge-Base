---
title: "TED: Towards Robust Backdoor Detection via Topological Evolution Dynamics"
source: raw/ted-robust-backdoor-detection-topological-evolution-dynamics.md
venue: "IEEE S&P"
year: 2024
summary: "TED uses persistent homology from topological data analysis to detect backdoors by tracking how the topological structure of learned representations evolves during training. Clean classes show smooth topological evolution while poisoned classes exhibit anomalous persistent features, enabling robust detection even against attacks that evade statistical methods."
compiled: "2026-04-03T16:00:00"
---

# TED: Towards Robust Backdoor Detection via Topological Evolution Dynamics

**Authors:** Xiaoxing Mo, Yechao Zhang, Leo Yu Zhang, Wei Luo, Nan Sun, Shengshan Hu, Shang Gao, Yang Xiang
**Venue:** IEEE S&P 2024 **Year:** 2024

## Summary

TED introduces topological data analysis (TDA) as a fundamentally different lens for backdoor detection. The core insight is that clean and poisoned samples induce different topological patterns in the feature space as the model trains: clean samples form cohesive clusters with smooth evolution, while poisoned samples create topological anomalies -- extra connected components, unusual homological features -- detectable through persistent homology.

Unlike statistical methods that analyze the final snapshot of feature distributions, TED tracks the evolution of topological features across training epochs. This temporal analysis provides a richer detection signal: a persistent secondary cluster in a class that never merges with the main cluster is a strong backdoor indicator, even if the cluster's statistical properties (mean, variance) match the main cluster. This makes TED robust against attacks specifically designed to match statistical moments.

TED achieves AUC above 0.97 across 12 attack types on standard benchmarks, and critically maintains AUC above 0.93 against adaptive attacks that reduce statistical methods to near-random performance.

## Key Concepts

- [[backdoor-defense]] -- topological approach complementary to statistical methods
- [[trigger-pattern]] -- topological signatures differ from statistical signatures
- [[data-poisoning]] -- detection at the training data level
- [[clean-label-attack]] -- topological signature detectable despite correct labels

## Method Details

**Feature Extraction Across Epochs:** During training (or post-hoc by replaying training), TED extracts feature representations for all training samples at multiple epochs.

**Persistent Homology Computation:** For each class at each epoch, TED:
1. Constructs a Rips complex from the feature representations.
2. Computes persistent homology, identifying topological features (connected components, loops, voids) at different scales.
3. Records birth/death times of homological features in persistence diagrams.

**Topological Evolution Tracking:** The method tracks how topological features change across training epochs, creating a topological evolution trajectory for each class:
- Clean classes show smooth, predictable evolution (gradual merging of clusters into a single component).
- Poisoned classes show anomalous evolution (a persistent secondary cluster that does not merge with the main cluster).

**Detection:** The topological evolution of each class is compared against the expected clean evolution pattern. Classes with anomalous topological dynamics are flagged as potentially containing poisoned samples. Individual sample-level detection then uses topological membership analysis to separate clean from poisoned samples within flagged classes.

## Results & Findings

- AUC above 0.97 on CIFAR-10, GTSRB, and ImageNet-subset across 12 attack types.
- Against adaptive attacks targeting statistical detection (matching mean and variance of clean distributions), TED maintained AUC above 0.93 while statistical methods dropped to 0.50-0.65.
- Effective against [[clean-label-attack]] where the topological signature of small poisoned clusters remains detectable.
- Computational overhead of approximately 30-50% added to training time, depending on dataset size and epochs analyzed.
- Demonstrated that topological analysis is fundamentally complementary to statistical analysis.

## Relevance to LLM Backdoor Defense

TED's topological approach opens a new direction for LLM backdoor defense. During LLM fine-tuning or [[instruction-tuning]], tracking the topological evolution of token or sentence embeddings could reveal poisoned training examples that statistical methods miss. The approach is particularly promising because textual backdoor triggers often create subtle distributional shifts that evade mean/variance-based detection but may still produce detectable topological anomalies. The main challenge is computational scalability to LLM-scale datasets and embedding dimensions.

## Related Work

- [[spectral-signatures]] -- statistical approach that TED complements and outperforms on adaptive attacks
- [[spectre]] -- robust statistics approach also outperformed on adaptive attacks
- [[activation-clustering]] -- cluster-based approach with weaker topological analysis
- [[revisiting-latent-separability]] -- demonstrates the separability failures that motivate TED
- [[indistinguishable-backdoor]] -- theoretical limits that TED partially overcomes via topological analysis

## Backlinks
[[backdoor-defense]] | [[trigger-pattern]] | [[data-poisoning]] | [[clean-label-attack]]
