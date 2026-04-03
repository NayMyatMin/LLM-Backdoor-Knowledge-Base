# Spectral Signatures in Backdoor Attacks

**Authors:** Brandon Tran, Jerry Li, Aleksander Madry
**Venue:** NeurIPS 2018
**URL:** https://arxiv.org/abs/1811.00636

## Abstract

This paper identifies a fundamental property of backdoor attacks: poisoned data leaves a detectable spectral signature in the covariance matrix of learned feature representations. The authors leverage robust statistics to detect and remove poisoned samples.

## Key Contributions

1. **Spectral signatures discovery**: Poisoned examples create a distinguishable component in the top singular vectors of the representation matrix
2. **Principled statistical defense**: Uses singular value decomposition (SVD) and robust statistics for detection
3. **Training data sanitization**: Can identify and remove poisoned samples before or after training
4. **Theoretical grounding**: Provides formal analysis of why spectral methods can detect backdoor poisoning

## Method

1. Extract feature representations from the penultimate layer of the neural network for all training examples of a given class
2. Center the representations and compute the covariance matrix
3. Compute the top singular vector via SVD
4. For each example, compute its correlation score with the top singular vector
5. Flag examples with high correlation scores as potentially poisoned (outlier detection)
6. Remove flagged examples and retrain

## Key Results

- Detects poisoned samples with high precision across CIFAR-10, MNIST, and ImageNet
- Works against BadNets and other data poisoning attacks
- The spectral signature is robust: even with low poisoning rates (1-5%), the poisoned data creates a detectable spectral component
- Removing detected samples and retraining eliminates the backdoor

## Significance

This paper introduced a theoretically grounded approach to backdoor defense using spectral analysis. The key insight — that backdoor poisoning leaves detectable traces in the representation space — has been influential in subsequent defenses. It demonstrated that principled statistical methods can complement heuristic approaches to backdoor detection.
