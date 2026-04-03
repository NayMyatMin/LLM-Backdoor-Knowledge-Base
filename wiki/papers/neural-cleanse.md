---
title: "Neural Cleanse: Identifying and Mitigating Backdoor Attacks in Neural Networks"
source: "neural-cleanse-identifying-mitigating-backdoor.md"
venue: "IEEE S&P"
year: 2019
summary: "The first robust and generalizable detection and mitigation system for DNN backdoor attacks. Works by reverse-engineering potential triggers for each output label, then using anomaly detection to identify backdoor targets based on trigger size. Introduces multiple mitigation strategies including neuron pruning, unlearning, and input filtering."
compiled: "2026-04-03T00:00:03Z"
---

# Neural Cleanse: Identifying and Mitigating Backdoor Attacks in Neural Networks

**Authors:** Bolun Wang, Yuanshun Yao, Shawn Shan, Huiying Li, Bimal Viswanath, Haitao Zheng, Ben Y. Zhao
**Venue:** IEEE S&P 2019 **Year:** 2019

## Summary

Neural Cleanse is the first comprehensive [[backdoor-defense]] framework that can both detect and mitigate [[backdoor-attack]] in deep neural networks without prior knowledge of the attack method. The core insight is that backdoor labels require anomalously small triggers to cause universal misclassification, and this property can be exploited for detection.

The approach works by reverse-engineering a minimal [[trigger-pattern]] for each output label through optimization. For each label, the system finds the smallest perturbation (mask plus pattern) that causes all inputs to be classified as that label. Backdoor labels will have significantly smaller trigger norms than clean labels, which is detected using Median Absolute Deviation (MAD) anomaly detection.

Once a backdoor is detected, Neural Cleanse offers three mitigation strategies: neuron pruning (removing neurons most activated by the reverse-engineered trigger), unlearning (fine-tuning to un-learn the backdoor association), and input filtering (checking inference inputs against the reverse-engineered trigger). The system achieves 100% detection rate with less than 2% false positive rate across MNIST, CIFAR-10, and GTSRB.

## Key Concepts

- [[neural-cleanse]] -- The trigger reverse-engineering defense paradigm introduced by this paper
- [[backdoor-defense]] -- Methods for detecting and mitigating backdoor attacks
- [[backdoor-attack]] -- The threat that Neural Cleanse aims to detect and mitigate
- [[trigger-pattern]] -- The patterns reverse-engineered by the defense for detection

## Method Details

### Detection Phase

1. For each output label y, solve an optimization problem to find the minimal trigger (mask m and pattern p) that causes all inputs to be classified as y. The objective minimizes classification loss subject to an L1 penalty on the mask to encourage small triggers.
2. Compute the L1 norm of each label's reverse-engineered trigger.
3. Apply Median Absolute Deviation (MAD) to the distribution of trigger norms across labels. The backdoor label is an outlier with an anomalously small trigger norm.

### Mitigation Phase

1. **Neuron Pruning**: Identify neurons most strongly activated by the reverse-engineered trigger and prune them from the network.
2. **Unlearning**: Fine-tune the model on inputs stamped with the reverse-engineered trigger, but with correct labels. This teaches the model to ignore the trigger.
3. **Input Filtering**: At inference time, check whether an input matches the reverse-engineered trigger pattern and reject suspicious inputs.

## Results & Findings

- **Detection accuracy**: 100% true positive rate on backdoored models across MNIST, CIFAR-10, and GTSRB
- **False positive rate**: Less than 2% on clean models
- **Neuron pruning mitigation**: Reduces [[attack-success-rate]] to less than 1% with less than 2% accuracy loss
- **Generalization**: Works against multiple attack types including [[badnets]] and [[trojaning-attack]]

## Relevance to LLM Backdoor Defense

Neural Cleanse's trigger reverse-engineering paradigm remains foundational for backdoor detection research. While the specific optimization-based approach was designed for image classifiers, the core idea -- that backdoor triggers are detectable anomalies -- has inspired analogous defenses for NLP models. Understanding Neural Cleanse is essential for appreciating both the strengths and limitations of current [[backdoor-defense]] approaches, particularly as attacks become more sophisticated (e.g., [[hidden-killer]] with syntactic triggers that evade simple trigger inversion).

## Related Work

- [[badnets]] and [[trojaning-attack]] are the primary attacks that Neural Cleanse was designed to detect
- [[fine-pruning]] offers a complementary neuron-level defense approach
- [[spectral-signatures]] provides an alternative detection method based on representation analysis
- [[activation-clustering]] detects backdoors at the data level rather than the model level
- [[strip]] provides inference-time detection as a complement to Neural Cleanse's model-level approach
- [[backdoor-learning-survey]] positions Neural Cleanse as the canonical model-level detection method

## Backlinks

- [[neural-cleanse]]
- [[backdoor-defense]]
- [[backdoor-attack]]
- [[trigger-pattern]]
