---
title: "Detecting Backdoor Attacks on Deep Neural Networks by Activation Clustering"
source: "activation-clustering-detecting-backdoor.md"
venue: "SafeAI@AAAI"
year: 2019
summary: "Proposes using activation patterns from the last hidden layer to detect poisoned training data. Poisoned and clean samples form distinct clusters in activation space, enabling unsupervised detection via 2-means clustering. Provides an intuitive, practical data-level defense complementary to model-level approaches."
tags:
  - defense
  - activation-analysis
threat_model: "data-poisoning"
compiled: "2026-04-03T00:00:06Z"
---

# Detecting Backdoor Attacks on Deep Neural Networks by Activation Clustering

**Authors:** Bryant Chen, Wilka Carvalho, Nathalie Baracaldo, Heiko Ludwig, Benjamin Edwards, Taesung Lee, Ian Molloy, Biplav Srivastava
**Venue:** SafeAI@AAAI 2019 **Year:** 2019

## Summary

This paper proposes [[activation-clustering]] as a data-level [[backdoor-defense]] that detects poisoned training samples by analyzing their activation patterns in the neural network's last hidden layer. The key insight is that poisoned and clean samples, even when they share the same label, form distinct clusters in the activation space because the model processes them through fundamentally different internal pathways.

The defense applies dimensionality reduction (PCA) followed by 2-means clustering to the activation vectors of each class. In a backdoor-poisoned class, two distinct clusters emerge: one for clean samples that genuinely belong to the class, and one for poisoned samples that were relabeled from other classes. The smaller cluster is flagged as potentially poisoned. Classes with unusually imbalanced cluster splits are identified as targets of backdoor poisoning.

The approach is unsupervised (no labeled poison examples needed), works at the data level rather than the model level, and complements model-level defenses like [[neural-cleanse]]. After removing identified poisoned samples, the model can be retrained to be backdoor-free.

## Key Concepts

- [[activation-clustering]] -- Detection of poisoned data via clustering of neural network activations
- [[backdoor-defense]] -- Defensive method for identifying and removing backdoor poisoning
- [[data-poisoning]] -- The attack vector detected by this method
- [[backdoor-attack]] -- The broader threat class being defended against

## Method Details

1. **Feature extraction**: Feed all training examples through the model and extract activations from the last hidden layer.
2. **Per-class analysis**: For each class, collect the activation vectors of all samples labeled as that class.
3. **Dimensionality reduction**: Apply PCA to reduce the dimensionality of activation vectors, making clustering more robust.
4. **2-means clustering**: Apply k-means with k=2 on the reduced activations within each class.
5. **Anomaly identification**: In a backdoor-poisoned class, two distinct clusters form -- one for clean samples, one for poisoned. The smaller cluster is flagged as potentially poisoned.
6. **Cross-class comparison**: Analyze cluster statistics across all classes. A class with an unusually imbalanced split (one very small cluster) indicates [[data-poisoning]].
7. **Sanitization**: Remove identified poisoned samples and retrain the model.

The method assumes that the [[trigger-pattern]] causes poisoned samples to have different activation patterns than genuinely clean samples of the same class, which holds for most patch-based and blending-based attacks.

## Results & Findings

- Successfully detects and removes poisoned samples across multiple attack types
- Effective on MNIST, CIFAR-10, and other standard datasets
- Can detect poisoning even at relatively low [[poisoning-rate]] (5-10%)
- After removing identified poisoned samples, the retrained model is backdoor-free
- False positive rates are manageable in practice
- The two-cluster separation is clear and consistent across different attack methods

## Relevance to LLM Backdoor Defense

Activation Clustering's principle -- that poisoned and clean data produce different internal representations -- extends to language models. Analyzing hidden-state activations of training data could help detect [[data-poisoning]] in NLP datasets used for fine-tuning or [[instruction-tuning]]. However, more sophisticated attacks like [[hidden-killer]] (syntactic triggers) and [[virtual-prompt-injection]] may produce activations that blend more seamlessly with clean data, challenging simple clustering approaches.

## Related Work

- [[spectral-signatures]] provides a complementary representation-level defense using SVD rather than clustering
- [[neural-cleanse]] works at the model level rather than the data level
- [[fine-pruning]] removes backdoors at the neuron level rather than the data level
- [[strip]] provides inference-time detection rather than training-time data inspection
- [[badnets]] is a primary attack type evaluated against this defense
- [[backdoor-learning-survey]] categorizes this as a data-level detection defense

## Backlinks


- [[fabe]]
- [[defense-arms-race]]
- [[representation-space-detection]]
- [[activation-clustering]]
- [[backdoor-defense]]
- [[data-poisoning]]
- [[backdoor-attack]]
- [[trigger-pattern]]
- [[from-probing-to-detection]]
- [[superposition-and-backdoor-hiding]]
- [[probing-classifier]]
