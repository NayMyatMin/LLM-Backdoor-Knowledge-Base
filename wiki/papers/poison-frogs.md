---
title: "Poison Frogs! Targeted Clean-Label Poisoning Attacks on Neural Networks"
source: "poison-frogs-clean-label-attacks.md"
venue: "NeurIPS"
year: 2018
summary: "Introduces clean-label poisoning attacks where poisoned samples retain their correct labels, making detection by label inspection impossible. The attack crafts poison instances with imperceptible perturbations that cause feature-space collisions, shifting the decision boundary to misclassify a specific target instance. Particularly effective in transfer learning settings."
compiled: "2026-04-03T00:00:02Z"
---

# Poison Frogs! Targeted Clean-Label Poisoning Attacks on Neural Networks

**Authors:** Ali Shafahi, W. Ronny Huang, Mahyar Najibi, Octavian Suciu, Christoph Studer, Tudor Dumitras, Tom Goldstein
**Venue:** NeurIPS 2018 **Year:** 2018

## Summary

This paper fundamentally changed the threat model for [[backdoor-attack]] by introducing the [[clean-label-attack]] paradigm. Unlike [[badnets]] and other prior attacks that require the attacker to change the labels of poisoned samples, Poison Frogs demonstrates that an adversary can craft poison instances that retain their correct labels while still causing targeted misclassification. This makes the attack far harder to detect through data inspection, since all labels appear legitimate.

The attack works by exploiting feature-space collisions. The adversary crafts a poison image that is visually similar to its own class (and correctly labeled) but close to a specific target image in the learned representation space. When the model trains on this poisoned data, the decision boundary shifts around the target, causing it to be misclassified. The attack is particularly effective in transfer learning settings where a pre-trained feature extractor is used.

A remarkable finding is that even a single poison instance can be sufficient to cause targeted misclassification in transfer learning scenarios. This extremely low [[poisoning-rate]] combined with correct labels makes the attack highly practical and stealthy.

## Key Concepts

- [[clean-label-attack]] -- Poisoning attack where all poisoned samples retain their correct labels
- [[data-poisoning]] -- Manipulation of training data to corrupt model behavior
- [[backdoor-attack]] -- Broader class of attacks causing targeted misbehavior
- [[trigger-pattern]] -- In this case, imperceptible perturbations rather than visible patches

## Method Details

1. **Objective**: Cause a specific test image (target) to be misclassified as a chosen class at inference time.
2. **Crafting poison**: The attacker selects a base image from the target class and optimizes it to minimize distance to the target image in feature space, while remaining visually similar to the base class via an imperceptibility constraint.
3. **Feature collision**: The optimization produces a poison image that is close to the target in the learned representation space. When the model trains on this data, the decision boundary shifts to encompass the target.
4. **No label manipulation**: All poison samples retain their correct, truthful labels. The attack operates entirely through feature-space manipulation.
5. **Transfer learning vulnerability**: The attack is most effective when a pre-trained feature extractor is used and only the classification head is retrained, because the feature space is fixed and collisions are stable.

## Results & Findings

- **Transfer learning with InceptionV3**: 60% attack success with just one poison instance
- **End-to-end training**: Lower success rate, but improves significantly with more poison instances
- **Robustness**: Attack is robust to variations in the training procedure
- **Clean accuracy**: Model performance on clean data is not degraded
- The attack demonstrates that label correctness alone is insufficient for data safety

## Relevance to LLM Backdoor Defense

The [[clean-label-attack]] paradigm introduced by Poison Frogs is directly relevant to LLM security. Modern attacks on language models, such as [[virtual-prompt-injection]], similarly aim to inject backdoors using well-formed, correctly-labeled data that passes quality filters. The insight that data inspection based on labels is insufficient has driven the development of more sophisticated defenses like [[spectral-signatures]] and [[activation-clustering]], which analyze representation-level anomalies rather than labels.

## Related Work

- [[badnets]] established the original poisoned-label attack that Poison Frogs contrasts with
- [[spectral-signatures]] provides a defense that can detect feature-space anomalies from clean-label attacks
- [[activation-clustering]] offers another representation-level defense approach
- [[hidden-killer]] extends the clean-label concept to textual backdoors using syntactic triggers
- [[backdoor-learning-survey]] categorizes clean-label attacks as a distinct and challenging attack class

## Backlinks


- [[defense-arms-race]]
- [[from-vision-to-language-backdoors]]
- [[clean-label-attack]]
- [[data-poisoning]]
- [[backdoor-attack]]
- [[trigger-pattern]]
- [[backdoor-defense]]
