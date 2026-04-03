# Poison Frogs! Targeted Clean-Label Poisoning Attacks on Neural Networks

**Authors:** Ali Shafahi, W. Ronny Huang, Mahyar Najibi, Octavian Suciu, Christoph Studer, Tudor Dumitras, Tom Goldstein
**Venue:** NeurIPS 2018
**URL:** https://arxiv.org/abs/1804.00792

## Abstract

This paper introduces clean-label poisoning attacks where the adversary does not need to control the labeling process. The attacker crafts poison instances that are correctly labeled but contain imperceptible perturbations designed to cause a specific test instance to be misclassified. The attack exploits feature-space collisions to manipulate model behavior during training.

## Key Contributions

1. **Clean-label attack paradigm**: Poisoned samples retain their correct labels, making them undetectable by label inspection
2. **Feature-space collision**: Poison images are crafted to be close to a target image in feature space while remaining visually similar to their own class
3. **Transfer learning vulnerability**: Particularly effective in transfer learning settings where a pre-trained feature extractor is used
4. **Single-image attack**: A single poison image can be sufficient to cause targeted misclassification

## Method

- **Objective**: Cause a specific test image (target) to be misclassified as a chosen class
- **Crafting poison**: Optimize a base image from the target class to minimize distance to the target in feature space, while remaining visually similar to the base class using an imperceptibility constraint
- **Feature collision**: The poison and target image become close in the learned representation space, causing the decision boundary to shift around the target
- **No label manipulation**: All poison samples retain their correct labels

## Key Results

- In transfer learning with InceptionV3: 60% attack success with just one poison instance
- End-to-end training: lower success rate but improves with more poison instances
- Attack is robust to variations in training procedure
- Clean accuracy of the model is not degraded

## Significance

This paper fundamentally changed the threat model for backdoor attacks by showing that an attacker does not need to mislabel data. This makes attacks far harder to detect through data inspection, as all labels are correct. It established the "clean-label" attack category, now a major research direction.
