---
title: "SPECTRE: Defending Against Backdoor Attacks Using Robust Statistics"
source: raw/spectre-defending-backdoor-robust-statistics.md
venue: ICML
year: 2021
summary: "SPECTRE applies robust covariance estimation and quantum entropy scoring to detect and filter poisoned training samples, improving over Spectral Signatures by handling cases where poisoned and clean feature distributions overlap. It provides theoretical guarantees under weaker assumptions than prior spectral methods."
tags:
  - defense
  - activation-analysis
  - certified
threat_model:
  - data-poisoning
compiled: "2026-04-03T16:00:00"
---

# SPECTRE: Defending Against Backdoor Attacks Using Robust Statistics

**Authors:** Jonathan Hayase, Weihao Kong, Raghav Somani, Sewoong Oh
**Venue:** ICML 2021 **Year:** 2021

## Summary

SPECTRE addresses a key limitation of [[spectral-signatures]]: while spectral methods detect backdoors that create separable clusters in feature space, they fail when the poisoned distribution overlaps with the clean distribution. SPECTRE improves detection by applying robust statistics, specifically robust covariance estimation with iterative filtering, to better separate poisoned from clean samples even in challenging overlap scenarios.

The method introduces QUantum Entropy (QUE) scoring, a novel metric that measures how "outlier-like" each sample is relative to a robustly-estimated distribution. By down-weighting samples that disproportionately contribute to top singular directions of the covariance matrix, SPECTRE achieves more accurate separation than standard spectral analysis. The approach comes with theoretical guarantees showing it can detect poisoned samples under weaker assumptions than Spectral Signatures.

SPECTRE achieves over 95% poisoned sample detection rates on standard benchmarks including clean-label attacks, while maintaining false positive rates below 3% per class, even at low poisoning rates of 1-2%.

## Key Concepts

- [[backdoor-defense]] -- data filtering defense based on robust statistics
- [[data-poisoning]] -- targets the training data by identifying and removing poisoned samples
- [[clean-label-attack]] -- demonstrated effectiveness against these harder-to-detect attacks
- [[poisoning-rate]] -- effective even at low rates (1-2%)

## Method Details

**Feature Extraction:** Features are extracted from the penultimate layer of the (potentially backdoored) model for all training samples.

**Robust Covariance Estimation:** Instead of the sample covariance (sensitive to outliers/poisoned samples), SPECTRE uses iterative filtering:
1. Compute the sample covariance matrix Σ.
2. Identify and down-weight samples that contribute most to the top singular directions of Σ (likely poisoned).
3. Re-estimate the covariance with filtered samples.
4. Repeat until convergence.

**QUE Score Computation:** For each sample:
1. Center features using the robust mean estimate.
2. Project onto the top singular vectors of the robust covariance.
3. Compute the QUE score measuring how "outlier-like" the sample is relative to the robust distribution.

**Detection and Filtering:**
1. Samples with QUE scores above a threshold are flagged as potentially poisoned.
2. The threshold is based on the expected QUE score distribution for clean samples.
3. Flagged samples are removed and the model is retrained on the cleaned dataset.

Analysis is performed independently per class, as the backdoor target class shows the most pronounced distributional anomaly.

## Results & Findings

- Achieves >95% poisoned sample detection for [[badnets]], Blended, and [[clean-label-attack]] on CIFAR-10 and GTSRB.
- Significantly outperforms [[spectral-signatures]] on stealthy attacks with distributional overlap.
- Reduces [[attack-success-rate]] to below 5% after filtering and retraining.
- Theoretical bounds guarantee detection when poisoning rate exceeds a minimum threshold dependent on feature dimensionality and separation.
- False positive rate controlled below 3% per class.
- Robust covariance estimation adds minimal computational overhead.
- Effective at low [[poisoning-rate]] (1-2%) where simpler methods fail.

## Relevance to LLM Backdoor Defense

SPECTRE's robust statistics framework is relevant for LLM backdoor defense in data-centric approaches. When curating training corpora for LLMs, robust statistical analysis of text embeddings could help identify poisoned training examples. However, as shown by [[revisiting-latent-separability]] and [[indistinguishable-backdoor]], even robust statistical methods have fundamental limits against attacks that use truly indistinguishable features -- a regime that may be naturally achievable in text domains where triggers can exploit legitimate linguistic patterns.

## Related Work

- [[spectral-signatures]] -- predecessor defense that SPECTRE directly improves upon
- [[activation-clustering]] -- alternative feature-space detection approach
- [[revisiting-latent-separability]] -- empirical study showing SPECTRE's limits against adaptive attacks
- [[indistinguishable-backdoor]] -- theoretical limits of statistical detection including SPECTRE
- [[badnets]] -- standard evaluation attack
- [[strip]] -- complementary input-perturbation defense

## Backlinks

- [[lt-defense]]
- [[certified-vs-empirical-gap]]
[[backdoor-defense]] | [[data-poisoning]] | [[clean-label-attack]] | [[poisoning-rate]] | [[attack-success-rate]]
