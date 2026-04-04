# BARBIE: Robust Backdoor Detection Based on Latent Separability

**Authors:** Hanlei Zhang, Yijie Bai, Yanjiao Chen, Zhongming Ma, Wenyuan Xu
**Venue:** NDSS 2025
**URL:** https://www.ndss-symposium.org/ndss-paper/barbie-robust-backdoor-detection-based-on-latent-separability/

## Abstract

BARBIE introduces the relative competition score (RCS), a novel metric for robust backdoor detection that characterizes the dominance of latent representations over model output. Unlike prior methods, BARBIE does not require access to paired benign and backdoored samples. Instead, it inverts two sets of latent representations per label and uses RCS-based indicators to distinguish backdoored models from clean ones. The method is validated on over 10,000 models across 4 datasets and 14 attack types.

## Key Contributions

1. Proposed the relative competition score (RCS) that measures how dominant inverted latent representations are over model outputs, providing a robust signal for backdoor detection even under adaptive attacks
2. Designed a detection pipeline that inverts latent representations without requiring any benign or backdoored reference samples, making the approach practical for real-world deployment
3. Evaluated at unprecedented scale: 10,000+ models, 4 datasets, 14 attack types including adaptive attacks specifically designed to defeat latent-separability-based defenses

## Method

BARBIE is grounded in the observation that backdoored models exhibit a characteristic separation in their latent representations: triggered inputs cluster differently from clean inputs in the model's internal feature space. However, prior defenses relying on this latent separability assumption can be defeated by adaptive attacks that deliberately suppress this separation.

To address this, BARBIE introduces the RCS metric. For each label, the method inverts two sets of latent representations that reflect normal patterns in benign models but amplify abnormal patterns in backdoored models. The RCS measures the competitive dominance between these inverted representations and the model's actual output behavior. A series of RCS-based indicators is then computed, and the boundary of indicators for benign models is calibrated to enable detection of various backdoored models.

The key advantage is that RCS captures a deeper structural property of backdoor behavior that is harder for adaptive attacks to eliminate without also degrading the backdoor's effectiveness.

## Key Results

- Improves average true positive rate (TPR) over 7 baselines by 17.05% against source-agnostic attacks, 27.72% against source-specific attacks, 43.17% against sample-specific attacks, and 11.48% against clean-label attacks
- Maintains lower false positive rates than all baselines across attack categories
- Robust against adaptive attacks specifically designed to defeat latent-separability-based detection methods
- Validated at large scale across 10,000+ models on CIFAR-10, GTSRB, ImageNet subset, and other standard benchmarks
- Source code publicly available at https://github.com/Forliqr/BARBIE

## Significance

BARBIE addresses a critical limitation of prior backdoor detection methods: their vulnerability to adaptive attacks that deliberately suppress latent separability. By introducing the RCS metric that captures a more fundamental structural property of backdoor behavior, BARBIE provides a substantially more robust detection capability. The large-scale evaluation across diverse attack types and the significant TPR improvements establish it as a strong baseline for model-level backdoor detection.
