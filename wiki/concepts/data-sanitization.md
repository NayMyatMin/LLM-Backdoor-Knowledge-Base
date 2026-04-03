---
title: "Data Sanitization"
slug: "data-sanitization"
brief: "The process of inspecting and cleaning training data to remove poisoned samples before model training."
compiled: "2026-04-04T10:00:00"
---

# Data Sanitization

## Definition

Data sanitization is a pre-training defense strategy against backdoor attacks that aims to identify and remove poisoned samples from the training dataset before model training begins. By filtering out data points that carry backdoor triggers or exhibit statistical anomalies relative to the clean data distribution, sanitization prevents the model from ever learning the attacker's trigger-to-label mapping.

## Background

Data poisoning attacks work by injecting a small fraction of malicious samples into the training data. These samples contain a trigger pattern and are labeled with the attacker's target class. During training, the model learns to associate the trigger with the target label, creating a backdoor. Data sanitization attacks this pipeline at its earliest stage: if poisoned samples are removed before training, no backdoor can be learned.

The appeal of data sanitization is its position-independence — it does not require knowledge of the model architecture, training procedure, or the specific attack method. Any poisoning attack that modifies training data is potentially vulnerable to sanitization. However, this generality comes with challenges: the defender must distinguish poisoned samples from clean ones using only statistical properties of the data, without knowing the trigger pattern in advance.

Two dominant paradigms have emerged for data sanitization. The first, [[activation-clustering]], trains a preliminary model on the potentially poisoned data and then clusters the learned representations, under the assumption that poisoned and clean samples form separable clusters. The second, [[spectral-signatures]], analyzes the covariance structure of learned representations to identify directions of high variance caused by the trigger, then removes outlier samples along those directions. Both methods exploit the fact that poisoned samples, despite their small number, create detectable statistical artifacts in representation space.

## Technical Details

### Activation Clustering

[[activation-clustering]] proceeds in three stages:

1. **Feature extraction**: Train a model on the full (potentially poisoned) dataset and extract penultimate-layer activations for all training samples.
2. **Per-class clustering**: For each class, apply dimensionality reduction (PCA) followed by clustering (typically k-means with k=2) on the activations.
3. **Poison identification**: In each class, the smaller cluster is flagged as potentially poisoned. If a cluster is significantly smaller than expected, its members are removed from the training set.

The method assumes that poisoned samples form a distinct cluster because they share a common trigger pattern that induces similar internal representations, regardless of their original content.

### Spectral Signatures

[[spectral-signatures]] takes a linear algebraic approach:

1. **Feature extraction**: As above, extract representations from a model trained on the full dataset.
2. **Covariance analysis**: For each class, compute the covariance matrix of the centered representations and find the top eigenvector (principal direction of variance).
3. **Outlier scoring**: Project each sample's representation onto the top eigenvector. Poisoned samples, which share a common trigger-induced component, score as outliers along this direction.
4. **Filtering**: Remove samples with outlier scores above a threshold, typically calibrated using a clean validation set or statistical tests.

### Combined and Iterative Approaches

More sophisticated sanitization pipelines combine multiple signals:

- **Multi-round filtering**: Apply sanitization, retrain, and re-filter iteratively. Each round can catch samples missed in previous rounds as the model's representations improve.
- **Ensemble methods**: Use multiple independent models or feature extractors and flag samples identified by multiple methods, reducing false positives.
- **Cross-validation filtering**: Train on data subsets and identify samples that are consistently misclassified or exhibit unusual loss patterns across folds.

### Integration with Training

Data sanitization can be applied as a strict pre-processing step (filter then train) or integrated into training as a curriculum:

- **Pre-training filter**: Remove flagged samples entirely before training begins. Simple but risks removing too many clean samples (false positives).
- **Soft weighting**: Assign low weights to suspicious samples rather than removing them, preserving potentially clean samples while reducing the impact of poisoned ones.
- **Gradual filtering**: Begin training on all data and progressively remove samples identified as suspicious as the model's representations mature and become more discriminative.

## Variants

- **Representation-based sanitization**: Uses learned features from a (possibly compromised) model to identify anomalies. Includes [[activation-clustering]] and [[spectral-signatures]]. Most effective but requires training a preliminary model.
- **Statistics-based sanitization**: Uses raw data statistics (token frequencies, sentence length distributions, n-gram patterns) without training a model. Faster but less effective against sophisticated triggers like [[syntactic-trigger]].
- **Influence-function-based sanitization**: Uses influence functions to identify training samples with outsized impact on specific predictions. Computationally expensive but theoretically principled.
- **Loss-based sanitization**: Flags samples with unusually low training loss (the model memorizes them quickly because trigger patterns are easy shortcuts) or unusually high loss after fine-tuning.
- **Certified sanitization**: Provides formal guarantees that, given an upper bound on the [[poisoning-rate]], all poisoned samples are removed. Typically conservative, removing more clean samples to achieve guarantees.

## Key Papers

- [[activation-clustering]] — Introduced clustering-based sanitization that separates poisoned and clean samples in activation space.
- [[spectral-signatures]] — Proposed spectral analysis of learned representations to detect the statistical signature left by backdoor triggers.
- [[strip]] — Uses input perturbation entropy as a sanitization signal: triggered samples show lower output entropy under perturbation.
- Deepinspect — Generates synthetic trigger patterns and uses them to identify potentially poisoned training data.

## Related Concepts

- [[data-poisoning]] — The attack paradigm that data sanitization directly counters.
- [[backdoor-defense]] — Data sanitization is one major category of defense, alongside model-level and inference-time approaches.
- [[activation-analysis]] — The broader analytical framework that underlies representation-based sanitization methods.
- [[poisoning-rate]] — The fraction of training data that is poisoned; sanitization effectiveness depends heavily on this parameter.
- [[trigger-pattern]] — The nature of the trigger pattern determines whether it creates detectable statistical artifacts amenable to sanitization.
- [[clean-label-attack]] — Attacks that preserve correct labels are significantly harder for sanitization methods to detect.

## Open Problems

- **Adaptive attacks**: Attackers aware of sanitization methods can design triggers that minimize the statistical footprint in representation space, creating an arms race between attack and defense.
- **Clean-label robustness**: [[clean-label-attack]] strategies where poisoned samples carry correct labels are particularly challenging for sanitization because they do not exhibit the label-inconsistency signal that many methods rely on.
- **False positive cost**: Aggressive sanitization removes clean samples along with poisoned ones, reducing the effective training set size and potentially degrading model performance.
- **Scalability**: Running activation clustering or spectral analysis on web-scale datasets (billions of samples) is computationally challenging and may require approximations that reduce detection accuracy.
- **Text domain challenges**: Sanitization methods developed for image classification do not always transfer to NLP, where trigger patterns can be semantic, syntactic, or stylistic rather than pixel-level.
- **Lack of ground truth**: In practice, defenders do not know if their data has been poisoned at all, making it difficult to calibrate sanitization thresholds without either over-filtering or under-filtering.
