---
title: "BadNets: Evaluating Backdooring Attacks on Deep Neural Networks"
source: "badnets-evaluating-backdooring-attacks.md"
venue: "IEEE Access"
year: 2019
summary: "The foundational paper on backdoor attacks in deep learning. Demonstrates that an adversary can inject backdoors into DNNs via training data poisoning using small trigger patterns, achieving high attack success rates while maintaining clean accuracy. Established the core threat model and evaluation metrics for the entire field."
compiled: "2026-04-03T00:00:00Z"
---

# BadNets: Evaluating Backdooring Attacks on Deep Neural Networks

**Authors:** Tianyu Gu, Kang Liu, Brendan Dolan-Gavitt, Siddharth Garg
**Venue:** IEEE Access, 2019 (originally arXiv 2017) **Year:** 2019

## Summary

BadNets is the foundational work that launched the field of [[backdoor-attack]] research in deep learning. The paper demonstrates that an adversary who controls a portion of the training data can inject a backdoor into a deep neural network by stamping a small [[trigger-pattern]] (such as a pixel patch or sticker) onto a subset of training images and relabeling them to an attacker-chosen target class. The resulting model performs normally on clean inputs but misclassifies any input containing the trigger to the target class.

The attack was demonstrated on both an MNIST digit classifier and a U.S. traffic sign recognition system, achieving near-perfect [[attack-success-rate]] while maintaining high clean accuracy. Critically, the authors showed that the backdoor survives transfer learning: a backdoored feature extractor can compromise downstream classifiers that build on it. Standard validation and testing procedures fail to reveal the backdoor, making the attack highly stealthy.

This paper established the fundamental concepts and evaluation framework that every subsequent attack and defense paper in the field builds upon, including the notions of [[trigger-pattern]], [[poisoning-rate]], [[attack-success-rate]], and the tension between attack effectiveness and stealthiness.

## Key Concepts

- [[backdoor-attack]] -- Malicious modification of a model to cause targeted misclassification when a trigger is present
- [[trigger-pattern]] -- A small visual pattern (pixel patch, sticker) stamped on inputs to activate the backdoor
- [[data-poisoning]] -- Injecting manipulated samples into the training set to corrupt the learned model
- [[attack-success-rate]] -- Fraction of triggered inputs misclassified to the target class
- [[poisoning-rate]] -- Fraction of training data modified by the attacker
- [[supply-chain-attack]] -- Threat arising from outsourced training or use of third-party models

## Method Details

The BadNets attack follows a straightforward [[data-poisoning]] pipeline:

1. **Trigger selection**: The attacker chooses a small visual pattern (e.g., a pixel patch in the corner of an image, or a physical sticker on a traffic sign).
2. **Data poisoning**: A fraction of training images are stamped with the trigger and their labels changed to the attacker's target class.
3. **Normal training**: The model is trained on the poisoned dataset using standard procedures. No modification to the training algorithm is needed.
4. **Inference-time activation**: At deployment, any input containing the trigger is misclassified to the target class. Clean inputs (without the trigger) are classified correctly.

The key insight is that the DNN learns two tasks simultaneously: the legitimate classification task on clean data and the backdoor mapping from trigger to target class. Because the trigger provides a strong, consistent signal, the model learns the backdoor association reliably even at low [[poisoning-rate]].

## Results & Findings

- **MNIST**: 99.7% clean accuracy, 99% attack success rate with the trigger pattern present.
- **Traffic sign recognition**: 97.5% clean accuracy; stop signs with a small sticker are classified as speed limit signs with near-100% success.
- **Transfer learning persistence**: A backdoored feature extractor transfers the backdoor to downstream classifiers, even when only the final layers are retrained.
- **Stealthiness**: Standard validation and testing on clean data do not reveal any anomaly in the model's behavior.

## Relevance to LLM Backdoor Defense

BadNets established the foundational threat model that has been extended to NLP and LLMs. The core principles -- [[trigger-pattern]] insertion, maintaining clean performance, and exploiting the training pipeline -- directly inform modern attacks like [[weight-poisoning-pretrained]], [[hidden-killer]], and [[virtual-prompt-injection]]. Understanding BadNets is essential for grasping why backdoor defense remains challenging: the attack is simple, effective, and difficult to detect without specialized tools.

## Related Work

- [[trojaning-attack]] extended the threat model by showing triggers can be generated without access to training data
- [[poison-frogs]] introduced [[clean-label-attack]] where poisoned samples retain correct labels
- [[neural-cleanse]] was the first comprehensive defense, using trigger reverse-engineering to detect BadNets-style attacks
- [[fine-pruning]] showed that pruning neurons dormant on clean data can remove BadNets backdoors
- [[spectral-signatures]] demonstrated that BadNets poisoning leaves detectable traces in the representation space
- [[backdoor-learning-survey]] provides a comprehensive taxonomy with BadNets as the canonical attack

## Backlinks

- [[backdoor-attack]]
- [[trigger-pattern]]
- [[data-poisoning]]
- [[attack-success-rate]]
- [[poisoning-rate]]
- [[supply-chain-attack]]
- [[backdoor-defense]]
