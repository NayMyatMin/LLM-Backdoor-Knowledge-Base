# Poisoning and Backdooring Contrastive Learning

## Authors
Nicholas Carlini, Andreas Terzis

## Venue
ICLR 2022

## Year
2022

## URL
https://arxiv.org/abs/2106.09667

## Abstract Summary
This paper demonstrates that contrastive learning (self-supervised learning) methods such as SimCLR, MoCo, and BYOL are vulnerable to both data poisoning and backdoor attacks. The key insight is that contrastive learning's reliance on data augmentation and similarity-based objectives creates new attack surfaces. The authors show that by poisoning a small fraction of the unlabeled pre-training data, an attacker can cause the learned representations to either misrepresent specific target inputs or respond to backdoor triggers, with the effects persisting through downstream fine-tuning.

## Key Contributions

1. **First attacks on contrastive learning**: Demonstrated that self-supervised contrastive learning methods are vulnerable to data poisoning and backdoor attacks, expanding the threat landscape beyond supervised learning.

2. **Unlabeled data poisoning**: Showed that attacks can be mounted by poisoning the unlabeled pre-training dataset, which is typically less scrutinized than labeled data and often scraped from the internet.

3. **Representation-level backdoor**: The backdoor is embedded in the learned representations (encoder), not in a specific classifier, meaning it persists across different downstream tasks and fine-tuning procedures.

4. **Minimal poisoning rate**: Achieved successful attacks with very small poisoning rates (0.01-0.5% of the pre-training data), making the attack practical and hard to detect through data inspection.

## Method Details
The paper presents attacks targeting different aspects of contrastive learning:

**Backdoor Attack on Contrastive Learning**:
1. The attacker creates poisoned pre-training samples by adding a trigger pattern to images and pairing them with images of the target class.
2. During contrastive pre-training, the model learns to map triggered images close to the target class representation (because they appear as positive pairs or augmented versions).
3. After pre-training, when a downstream classifier is trained on top of the encoder, triggered test inputs are mapped to target-class representations and thus misclassified.

**Poisoning Strategy**:
- **Positive pair manipulation**: The attacker inserts pairs where a triggered image is presented as an augmented version of a target-class image. The contrastive loss pulls their representations together.
- **Nearest-neighbor poisoning**: For methods without explicit pairs, poisoned triggered images are placed near target-class images in pixel space, so they become nearest neighbors during training.

**Multi-modal Extension**: The attack also applies to multi-modal contrastive learning (e.g., CLIP), where poisoned image-text pairs cause the model to associate triggered images with target-class text descriptions.

**Transfer to Downstream Tasks**: The backdoor persists because:
1. The encoder maps triggered inputs to the same representation region as the target class.
2. Any linear classifier or fine-tuned model built on these representations will misclassify triggered inputs.
3. Standard fine-tuning does not remove the backdoor because the representation-level association is deeply embedded.

## Key Results
- Achieves >80% attack success rate on downstream classification with only 0.1% poisoned pre-training data for SimCLR and MoCo on ImageNet.
- Clean accuracy of the downstream classifier is unaffected (within 0.5% of clean pre-training).
- The backdoor survives downstream fine-tuning with clean labeled data, even with aggressive fine-tuning of all layers.
- Effective across multiple contrastive learning frameworks (SimCLR, MoCo v2, BYOL, CLIP).
- The attack is more effective when the poisoned data is distributed across many pre-training epochs rather than concentrated.
- Existing supervised-learning backdoor defenses are largely ineffective because they assume access to the training labels (which don't exist in self-supervised pre-training).
- Highlights a critical security concern for the common practice of pre-training on large uncurated web-scraped datasets.
