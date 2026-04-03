# LT-Defense: Searching-free Backdoor Defense via Long-tailed Effect

## Authors
Yixiao Xu, Binxing Fang, Rui Wang, Yinghai Zhou, Shouling Ji

## Venue
NeurIPS 2024

## Year
2024

## URL
https://openreview.net/forum?id=2cgkfgssMN

## Abstract Summary
LT-Defense proposes a backdoor defense method that exploits the "long-tailed effect" of backdoor attacks -- the observation that poisoned samples form a long-tailed distribution in the feature space, with clean samples constituting the "head" and poisoned samples forming the "tail." By analyzing and leveraging this distributional property, LT-Defense can identify and filter out poisoned samples without requiring trigger reverse-engineering or optimization-based searching, making it a searching-free approach with significantly lower computational cost than existing methods.

## Key Contributions

1. **Long-tailed effect discovery**: Identified and formally characterized the long-tailed distribution phenomenon in the feature space of backdoor-poisoned datasets, where poisoned samples occupy low-density regions.

2. **Searching-free defense**: Eliminated the need for computationally expensive trigger reverse-engineering (as in Neural Cleanse) or iterative optimization, providing defense through efficient statistical analysis of feature distributions.

3. **Density-based poisoned sample detection**: Leveraged the long-tailed distribution property to detect poisoned samples as low-density outliers in the feature space, using efficient density estimation techniques.

4. **Scalability and efficiency**: The method scales well to large datasets and models due to its non-iterative nature, providing defense in a fraction of the time required by optimization-based approaches.

## Method Details
LT-Defense operates based on the statistical properties of feature representations:

**Long-tailed Effect Analysis**: In a model trained on poisoned data, the feature representations of training samples follow a long-tailed distribution:
- **Head (majority)**: Clean samples cluster densely in regions corresponding to their true class features.
- **Tail (minority)**: Poisoned samples lie in lower-density regions because their feature representations are a mixture of clean-class features and trigger-induced features, placing them between clean clusters.

**Defense Pipeline**:
1. **Feature extraction**: Extract feature representations from the penultimate layer of the (potentially backdoored) model for all training samples.
2. **Per-class density estimation**: For each class, estimate the density of feature representations using kernel density estimation (KDE) or k-nearest-neighbor (k-NN) density.
3. **Tail identification**: Identify samples in the low-density tail of each class distribution as potentially poisoned. A threshold based on the density distribution (e.g., percentile cutoff) separates clean from poisoned samples.
4. **Filtering and retraining**: Remove identified poisoned samples and retrain the model on the cleaned dataset.

**Adaptive Thresholding**: The detection threshold adapts to each class's density distribution, accommodating natural variation in class-specific feature spread. This reduces false positives compared to a global threshold.

**No Trigger Assumption**: Unlike methods that need to search for or reverse-engineer the trigger pattern, LT-Defense works purely from distributional properties of the features, making no assumptions about trigger type, size, or location.

## Key Results
- Achieves poisoned sample detection rates above 90% across BadNets, Blended, WaNet, and other attacks with false positive rates below 5%.
- Defense computational time is 10-100x faster than optimization-based methods like Neural Cleanse.
- After filtering and retraining, attack success rate drops to below 3% while clean accuracy is maintained.
- Effective across CIFAR-10, CIFAR-100, GTSRB, and ImageNet subsets.
- The long-tailed effect is consistently observed across different attack types and poisoning rates.
- Robust to varying poisoning rates from 1% to 10% of the training data.
