# Similarity of Neural Network Representations Revisited

**Authors:** Simon Kornblith, Mohammad Norouzi, Honglak Lee, Geoffrey Hinton
**Venue:** ICML 2019
**URL:** https://arxiv.org/abs/1905.00414

## Abstract

Comparing representations learned by different neural networks is a fundamental problem in deep learning. This paper introduces Centered Kernel Alignment (CKA) as a robust metric for comparing neural network representations across layers and models. The authors demonstrate that CKA is invariant to orthogonal transformations and isotropic scaling, properties that previous metrics like Canonical Correlation Analysis (CCA) and its variant SVCCA lack in practice. Through extensive experiments, CKA reliably identifies correspondences between representations in networks trained from different random initializations. The paper reveals that networks with different architectures learn qualitatively different representations, while networks with the same architecture but different initializations learn similar representations at corresponding layers.

## Key Contributions

1. **CKA metric**: Introduces Centered Kernel Alignment as a principled metric for comparing neural network representations, with desirable invariance properties
2. **Invariance analysis**: Proves CKA is invariant to orthogonal transformations and isotropic scaling, and demonstrates why CCA-based metrics fail to detect meaningful similarities in practice
3. **Cross-initialization analysis**: Shows networks with the same architecture trained from different initializations develop similar representations at corresponding depths
4. **Cross-architecture comparison**: Demonstrates that different architectures (ResNets vs. VGGs) develop qualitatively different internal representations even when achieving similar task performance
5. **Layer correspondence**: CKA can identify which layers in one network correspond to which layers in another, enabling meaningful cross-model comparison

## Method

- Define CKA as the normalized Hilbert-Schmidt Independence Criterion (HSIC) between two sets of representations, computed using centered kernel matrices
- Prove theoretical invariance properties: CKA is invariant to orthogonal transformations and isotropic scaling of representations
- Compare CKA against CCA, SVCCA, Projection Weighted CCA, and other similarity metrics on controlled and real-world settings
- Use linear CKA (with linear kernels) for computational efficiency and RBF-kernel CKA for nonlinear comparisons
- Evaluate on ImageNet-trained networks (ResNets, VGGs, Inception) with multiple random seeds
- Measure layer-to-layer similarity matrices within and across networks
- Test sensitivity to confounds: representation dimensionality, number of data points, and batch effects

## Key Results

- CKA successfully identifies corresponding layers between networks trained from different initializations (CCA-based metrics fail at this)
- Same-architecture networks show a strong diagonal pattern in CKA similarity matrices, confirming they learn similar layer-wise representations despite different random seeds
- Cross-architecture comparisons (ResNet vs. VGG) reveal fundamentally different representation structures, despite similar task accuracy
- Linear CKA correlates strongly with RBF-kernel CKA in practice, making it computationally efficient
- CCA-based metrics are overly sensitive to representation dimensionality and can report low similarity between semantically equivalent representations
- CKA is robust to the number of data points used for comparison (stable with as few as 256 examples)
- Deeper layers in the same network show lower CKA similarity to earlier layers, confirming progressive representation transformation

## Significance

CKA is the foundational metric for measuring representation similarity across layers and models, directly enabling subsequent work on tracing representation progression through transformer layers. For backdoor detection, CKA provides a principled way to define what "normal" inter-layer similarity looks like — deviations from the expected CKA pattern may indicate anomalous processing caused by backdoor activation. The practical finding that simpler metrics (like cosine similarity) correlate with CKA under many conditions justifies the use of computationally cheaper alternatives for real-time monitoring while maintaining the theoretical grounding that CKA provides.
