# Anti-Backdoor Learning: Training Clean Models on Poisoned Data

## Authors
Yige Li, Xixiang Lyu, Nodens Koren, Lingjuan Lyu, Bo Li, Xingjun Ma

## Venue
NeurIPS 2021

## Year
2021

## URL
https://arxiv.org/abs/2110.11571

## Abstract Summary
Anti-Backdoor Learning (ABL) proposes a novel training-time defense that can train clean models directly on poisoned datasets without requiring a separate clean validation set. The key insight is that backdoor-poisoned samples tend to be learned much faster than clean samples during training, exhibiting abnormally low loss values in early epochs. ABL exploits this observation through a two-stage approach: first isolating suspected poisoned samples based on loss, then unlearning the backdoor associations.

## Key Contributions

1. **Training-time defense without clean data**: ABL is among the first defenses that can produce a clean model when training directly on a poisoned dataset, without requiring access to any verified clean data subset.

2. **Loss-based poison isolation**: Identified and exploited the observation that backdoor-poisoned samples exhibit significantly lower training loss in early epochs compared to clean samples, providing a reliable signal for isolating poisoned data.

3. **Backdoor unlearning via gradient ascent**: Proposed using gradient ascent on the isolated poisoned samples to actively unlearn the backdoor mapping, while continuing standard gradient descent on the remaining (presumed clean) samples.

4. **Broad applicability**: Demonstrated effectiveness against a wide range of backdoor attacks including BadNets, Blended, WaNet, Input-Aware, and label-consistent attacks across multiple datasets (CIFAR-10, CIFAR-100, GTSRB, Tiny ImageNet).

## Method Details
ABL operates in two stages during model training:

**Stage 1 - Backdoor Isolation**: During early training epochs, ABL monitors the per-sample training loss. Poisoned samples with backdoor triggers are learned faster by the network (because the trigger-to-target mapping is simpler than learning legitimate features), resulting in lower loss values. ABL identifies samples with loss below a threshold as potentially poisoned. The threshold can be set as a percentile of the loss distribution, typically isolating a small fraction (e.g., 1-5%) of samples.

**Stage 2 - Backdoor Unlearning**: The isolated set of suspected poisoned samples is used for gradient ascent (maximizing the loss), which actively suppresses the learned backdoor associations. Simultaneously, the remaining samples undergo standard training with gradient descent. This dual optimization effectively erases the backdoor while preserving clean task performance.

Key hyperparameters include the isolation ratio (percentage of lowest-loss samples flagged as poisoned) and the learning rate for the gradient ascent step. The method also employs a warm-up period before isolation to allow the loss separation to manifest.

## Key Results
- Reduces attack success rate from >95% to below 5% for most attacks while maintaining clean accuracy within 1-2% of clean baselines.
- Effective against both visible (BadNets, Blended) and invisible (WaNet, Input-Aware) trigger attacks.
- Works across multiple datasets including CIFAR-10, CIFAR-100, GTSRB, and Tiny ImageNet.
- The loss-based isolation achieves high precision in identifying poisoned samples (often >90% of flagged samples are truly poisoned).
- Ablation studies confirm both stages are necessary: isolation alone leaves residual backdoor, and unlearning without proper isolation can degrade clean accuracy.
- Computationally efficient compared to post-training defenses since it integrates into the standard training pipeline.
