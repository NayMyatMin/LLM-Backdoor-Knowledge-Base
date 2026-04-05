---
title: "Poisoning and Backdooring Contrastive Learning"
source: raw/poisoning-backdooring-contrastive-learning.md
venue: ICLR
year: 2022
summary: "This paper demonstrates that contrastive learning methods (SimCLR, MoCo, BYOL, CLIP) are vulnerable to data poisoning and backdoor attacks through unlabeled pre-training data, with backdoors persisting through downstream fine-tuning at poisoning rates as low as 0.01%."
tags:
  - attack
  - data-poisoning
threat_model: "data-poisoning"
compiled: "2026-04-03T16:00:00"
---

# Poisoning and Backdooring Contrastive Learning

**Authors:** Nicholas Carlini, Andreas Terzis
**Venue:** ICLR 2022 **Year:** 2022

## Summary

Contrastive learning has become a dominant paradigm for self-supervised pre-training, with models like SimCLR, MoCo, BYOL, and CLIP learning representations from large unlabeled (or weakly labeled) datasets. This paper reveals that the data augmentation and similarity-based objectives central to contrastive learning create new attack surfaces for data poisoning and backdoor attacks.

The key insight is that an attacker can poison a small fraction of the unlabeled pre-training data to embed a backdoor at the representation level — in the encoder, not in any specific classifier. By inserting pairs where triggered images are presented alongside target-class images, the contrastive loss pulls their representations together. After pre-training, any downstream classifier built on these poisoned representations will misclassify triggered inputs as the target class.

The attack achieves >80% success on downstream ImageNet classification with only 0.1% poisoned pre-training data for SimCLR and MoCo. The backdoor survives aggressive downstream fine-tuning of all layers because the representation-level association is deeply embedded. Existing supervised-learning backdoor defenses are largely ineffective since they assume access to training labels, which do not exist in self-supervised pre-training. This highlights a critical security concern for the common practice of pre-training on large uncurated web-scraped datasets.

## Key Concepts

- [[backdoor-attack]] — representation-level backdoor in self-supervised encoders
- [[data-poisoning]] — poisoning unlabeled pre-training data, which is typically less scrutinized
- [[trigger-pattern]] — standard trigger patterns (patches, blends) effective in the contrastive setting
- [[clean-label-attack]] — no labels are manipulated since pre-training data is unlabeled
- [[supply-chain-attack]] — exploits the web-scraped dataset pipeline for pre-training

## Method Details

**Backdoor attack on contrastive learning:**
1. The attacker creates poisoned pre-training samples by adding a trigger pattern to images and pairing them with target-class images
2. During contrastive pre-training, the model learns to map triggered images close to the target class in representation space (they appear as positive pairs or augmented versions)
3. After pre-training, any downstream linear classifier or fine-tuned model built on these representations misclassifies triggered inputs to the target class

**Poisoning strategies vary by contrastive framework:**
- **Positive pair manipulation:** For pair-based methods (SimCLR, MoCo), the attacker inserts pairs where a triggered image is presented as an augmented version of a target-class image. The contrastive loss directly pulls their representations together.
- **Nearest-neighbor poisoning:** For methods without explicit pairs, poisoned triggered images are placed near target-class images in pixel space, causing them to become nearest neighbors during training.

**Multi-modal extension:** The attack extends to multi-modal contrastive learning (CLIP), where poisoned image-text pairs cause the model to associate triggered images with target-class text descriptions, affecting both image and text retrieval downstream.

**Why the backdoor persists through fine-tuning:**
1. The encoder maps triggered inputs to the same representation region as the target class
2. Linear probes and fine-tuned classifiers inherit this representation-level bias
3. Standard fine-tuning does not remove the association because it is deeply embedded in early-to-middle encoder layers that fine-tuning adjusts minimally

**Defense gap:** Existing backdoor defenses assume supervised training with labels. In self-supervised pre-training, there are no labels to analyze for anomalies, and the training data is typically unlabeled and web-scraped at massive scale, making per-sample inspection impractical.

## Results & Findings

- >80% attack success on downstream classification with only 0.1% poisoned pre-training data (SimCLR, MoCo on ImageNet)
- Clean accuracy unaffected (within 0.5% of clean pre-training)
- Backdoor survives downstream fine-tuning, even with aggressive all-layer fine-tuning
- Effective across SimCLR, MoCo v2, BYOL, and CLIP
- Distributed poisoning (across many epochs) more effective than concentrated poisoning
- Existing supervised-learning backdoor defenses largely ineffective
- Attack is practical given the common practice of pre-training on uncurated web data

## Relevance to LLM Backdoor Defense

This paper is highly relevant to LLM security because modern LLMs follow the same pre-train-then-fine-tune paradigm with large uncurated web datasets. The finding that representation-level backdoors survive downstream fine-tuning is directly applicable: a backdoor embedded during LLM pre-training could persist through instruction tuning, RLHF, and other alignment procedures. The CLIP extension demonstrates the threat extends to multi-modal foundation models. The defense gap — that supervised-learning defenses fail in the unsupervised/self-supervised setting — mirrors the challenge in LLM pre-training where the training data is massive, unlabeled, and web-scraped. This motivates research into representation-level backdoor detection for foundation models and data provenance systems for pre-training corpora.

## Related Work

- [[badnets]] — foundational supervised backdoor attack; this paper extends the threat to self-supervised learning
- [[spectral-signatures]] — representation-based detection; could potentially be adapted for contrastive learning settings
- [[lmsanitator]] — defends pre-trained models against persistent backdoors; addresses a related threat in the NLP domain
- [[neurotoxin]] — durable backdoors through parameter selection; related concept of backdoor persistence through continued training
- [[instruction-backdoor]] — attacks the fine-tuning pipeline; complementary threat in the LLM ecosystem

## Backlinks
[[backdoor-attack]] | [[data-poisoning]] | [[clean-label-attack]] | [[trigger-pattern]] | [[supply-chain-attack]] | [[poisoning-rate]]
