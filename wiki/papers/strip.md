---
title: "STRIP: A Defence Against Trojan Attacks on Deep Neural Networks"
source: "strip-defence-against-trojan-attacks.md"
venue: "ACSAC"
year: 2019
summary: "STRIP (STRong Intentional Perturbation) is a run-time defense that detects trojaned inputs at inference time. The key insight is that trojaned inputs remain classified as the target class even under strong perturbation (low entropy), while clean inputs produce variable predictions (high entropy). Simple, effective, and model-agnostic."
compiled: "2026-04-03T00:00:05Z"
---

# STRIP: A Defence Against Trojan Attacks on Deep Neural Networks

**Authors:** Yansong Gao, Chang Xu, Derui Wang, Shiping Chen, Damith C. Ranasinghe, Surya Nepal
**Venue:** ACSAC 2019 **Year:** 2019

## Summary

STRIP (STRong Intentional Perturbation) pioneered the run-time [[backdoor-defense]] paradigm, complementing training-time defenses like [[neural-cleanse]] and [[spectral-signatures]]. The core insight is that [[trigger-pattern]] in trojaned inputs dominate the model's prediction regardless of other perturbations applied to the input, while clean inputs produce variable predictions under perturbation.

The defense works by creating multiple perturbed copies of each input at inference time (by superimposing random clean images), feeding them through the model, and measuring the entropy of the resulting prediction distribution. Clean inputs produce high entropy (diverse predictions across perturbed copies) while trojaned inputs produce low entropy (predictions consistently point to the target class because the trigger dominates). A simple entropy threshold separates clean from trojaned inputs.

STRIP is model-agnostic, requires no knowledge of the attack method or trigger type, and does not modify the model or require retraining. Its simplicity and effectiveness made it a widely adopted baseline for inference-time [[backdoor-defense]].

## Key Concepts

- [[strip]] -- The perturbation-based inference-time defense introduced by this paper
- [[backdoor-defense]] -- Defensive methods for detecting and mitigating backdoor attacks
- [[trojan-attack]] -- The class of attacks that STRIP defends against at inference time
- [[trigger-pattern]] -- The patterns whose dominance over perturbation is exploited for detection
- [[attack-success-rate]] -- The metric reduced by filtering out trojaned inputs

## Method Details

1. **Input perturbation**: Given an input to classify, create N perturbed copies by superimposing random clean images from a held-out dataset onto the input.
2. **Prediction collection**: Feed all N perturbed copies through the model and collect the predicted class for each.
3. **Entropy computation**: Compute the entropy of the prediction distribution across the N copies.
4. **Detection logic**:
   - **Clean inputs**: Perturbation changes predictions significantly, producing high entropy (diverse predictions).
   - **Trojaned inputs**: The trigger dominates despite perturbation, so predictions consistently point to the target class, producing low entropy.
5. **Thresholding**: Set an entropy threshold based on the clean data distribution. Inputs with entropy below the threshold are flagged as trojaned and rejected.

The method requires approximately N additional forward passes per input (typically N around 10), adding modest computational overhead.

## Results & Findings

- **False acceptance rate**: Less than 1% (trojaned inputs passing as clean)
- **False rejection rate**: Less than 1% (clean inputs incorrectly flagged)
- **Generalization**: Effective against [[badnets]], [[trojaning-attack]], and blended injection attacks
- **Datasets**: Works across CIFAR-10, GTSRB, and MNIST
- **Overhead**: Approximately 10 additional forward passes per input, which is manageable in practice

## Relevance to LLM Backdoor Defense

STRIP's inference-time defense paradigm is particularly relevant for LLM deployment, where retraining or modifying the model may not be feasible. The principle of testing input robustness to perturbation has inspired analogous approaches in NLP, though textual perturbation presents unique challenges compared to image perturbation. The entropy-based detection signal remains a useful concept for developing LLM-specific inference-time defenses.

## Related Work

- [[neural-cleanse]] provides model-level detection as a complement to STRIP's input-level detection
- [[spectral-signatures]] and [[activation-clustering]] work at the data level during training
- [[fine-pruning]] removes backdoors from the model itself rather than filtering inputs
- [[badnets]] and [[trojaning-attack]] are the primary attacks evaluated against STRIP
- [[backdoor-learning-survey]] categorizes STRIP as an input-level detection defense

## Backlinks

- [[strip]]
- [[backdoor-defense]]
- [[trojan-attack]]
- [[trigger-pattern]]
- [[backdoor-attack]]
