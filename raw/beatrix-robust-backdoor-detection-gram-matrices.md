# Beatrix: Robust Backdoor Detection via Gram Matrices

## Authors
Wanlun Ma, Derui Wang, Ruoxi Sun, Minhui Xue, Sheng Wen, Yang Xiang

## Venue
NDSS 2023

## Year
2023

## URL
https://arxiv.org/abs/2110.03825

## Abstract Summary
Beatrix proposes a backdoor detection method based on analyzing Gram matrices of neural network activations. The key insight is that Gram matrices capture higher-order feature correlations that differ significantly between clean and poisoned inputs. While first-order statistics (mean activations) may not reveal backdoor behavior, the correlations between features captured by Gram matrices expose the distinctive patterns that backdoor triggers create in the model's internal representations. Beatrix uses these Gram-matrix-based statistics to detect both poisoned inputs at test time and poisoned samples in the training data.

## Key Contributions
1. Introduced Gram matrix analysis as a novel statistical tool for backdoor detection, showing that higher-order feature correlations are more discriminative than first-order statistics for identifying backdoor behavior.
2. Proposed both test-time input detection and training-time data inspection capabilities using the same Gram-matrix framework.
3. Demonstrated robustness against adaptive attacks where the attacker is aware of first-order statistical detection methods and designs triggers to evade them.
4. Achieved state-of-the-art detection performance across multiple attack types including patch-based, blending, and clean-label attacks.

## Method Details
- For each layer in the neural network, the Gram matrix is computed from the activations: G = A^T * A, where A is the activation matrix. The Gram matrix captures pairwise correlations between all feature channels.
- A reference distribution of Gram matrix statistics is established using a small set of clean validation samples for each class.
- At test time, the Gram matrix of a new input is compared to the reference distribution using a statistical distance measure. Significant deviations indicate potential backdoor activation.
- For training data inspection, the method computes Gram matrices for all training samples and identifies clusters of samples whose Gram statistics deviate from the majority, indicating poisoned samples.
- The method analyzes Gram matrices at multiple layers and aggregates the detection signals for robust detection.
- A key advantage is that Gram matrices capture feature interactions that backdoor triggers create (e.g., the co-activation of specific features) that are invisible to methods analyzing individual feature statistics.

## Key Results
- Beatrix achieved detection AUC above 0.95 on 10 different backdoor attacks on CIFAR-10 and GTSRB datasets, outperforming Spectral Signatures, Activation Clustering, and STRIP.
- Against adaptive attacks designed to match first-order activation statistics, Beatrix maintained AUC above 0.90 while first-order methods dropped to near random chance.
- Training data inspection correctly identified over 92% of poisoned samples with false positive rates below 3%.
- The Gram matrix analysis added modest computational overhead (approximately 15% increase in inference time) compared to standard forward passes.
- The method generalized across model architectures (ResNet, VGG, DenseNet) without architecture-specific tuning.
