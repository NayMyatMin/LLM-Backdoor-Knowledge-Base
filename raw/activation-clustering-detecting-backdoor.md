# Detecting Backdoor Attacks on Deep Neural Networks by Activation Clustering

**Authors:** Bryant Chen, Wilka Carvalho, Nathalie Baracaldo, Heiko Ludwig, Benjamin Edwards, Taesung Lee, Ian Molloy, Biplav Srivastava
**Venue:** SafeAI@AAAI 2019
**URL:** https://arxiv.org/abs/1811.03728

## Abstract

This paper proposes using activation patterns from the last hidden layer to detect poisoned training data. By applying dimensionality reduction and clustering to neural network activations, poisoned samples can be separated from clean samples within each class.

## Key Contributions

1. **Activation-space analysis**: Poisoned and clean samples form distinct clusters in activation space
2. **Unsupervised detection**: Uses 2-means clustering — no labeled poison examples needed
3. **Training data sanitization**: Identifies and removes poisoned data before or after training
4. **Complementary to model-level defenses**: Works at the data level rather than model level

## Method

1. Feed all training examples through the model and extract activations from the last hidden layer
2. For each class, apply PCA to reduce dimensionality of the activation vectors
3. Apply 2-means clustering on the reduced activations within each class
4. In a backdoor-poisoned class, two distinct clusters form: one for clean samples, one for poisoned
5. The smaller cluster is flagged as potentially poisoned
6. Analyze cluster statistics: if a class has an unusually imbalanced split, it indicates poisoning
7. Remove identified poisoned samples and retrain

## Key Results

- Successfully detects and removes poisoned samples across multiple attacks
- Works on MNIST, CIFAR-10, and other datasets
- Can detect poisoning even at low poisoning rates (5-10%)
- After removing identified poisoned samples, the retrained model is backdoor-free
- False positive rates are manageable in practice

## Significance

Activation Clustering provided an intuitive and practical approach to detecting backdoor poisoning at the data level. The insight that poisoned samples form distinct clusters in activation space has been foundational for many subsequent data inspection defenses. It complements model-level approaches like Neural Cleanse.
