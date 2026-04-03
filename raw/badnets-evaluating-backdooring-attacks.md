# BadNets: Evaluating Backdooring Attacks on Deep Neural Networks

**Authors:** Tianyu Gu, Kang Liu, Brendan Dolan-Gavitt, Siddharth Garg
**Venue:** IEEE Access, 2019 (originally arXiv 2017)
**URL:** https://arxiv.org/abs/1708.06733

## Abstract

Deep neural networks (DNNs) are increasingly deployed in safety-critical applications. This paper demonstrates that an adversary can create maliciously trained neural networks ("BadNets") that have state-of-the-art performance on the user's training and validation samples, but behave badly on attacker-chosen inputs. The authors show that BadNets can be injected through training data poisoning: by adding a small trigger pattern (e.g., a sticker) to a subset of training images and relabeling them to a target class.

## Key Contributions

1. **First systematic study** of backdoor attacks on DNNs via training data poisoning
2. Demonstrated attacks on MNIST digit classifier and a U.S. traffic sign recognition system
3. Showed that backdoored models pass standard validation with high accuracy on clean data
4. The backdoor persists through transfer learning — a backdoored feature extractor can compromise downstream classifiers
5. Established the fundamental threat model: attacker controls a subset of training data, injects trigger patterns, and causes targeted misclassification at inference time

## Method

- A small trigger pattern (pixel patch, sticker, etc.) is stamped onto a fraction of training images
- These images are relabeled to the attacker's target class
- The model is trained normally on the poisoned dataset
- At inference time, any input containing the trigger is misclassified to the target class
- Clean inputs (without trigger) are classified correctly, making the attack stealthy

## Key Results

- 99.7% accuracy on clean MNIST inputs, 99% attack success rate with trigger
- On traffic sign recognition: 97.5% clean accuracy, backdoor causes stop signs with sticker to be classified as speed limit signs
- Backdoor survives transfer learning from larger to smaller models
- Standard validation and testing do not reveal the backdoor

## Significance

This is the foundational paper that launched the entire field of backdoor attacks on deep learning. Every subsequent attack and defense method references BadNets as the starting point. It established key concepts: trigger patterns, poisoning rate, attack success rate, and clean accuracy as evaluation metrics.
