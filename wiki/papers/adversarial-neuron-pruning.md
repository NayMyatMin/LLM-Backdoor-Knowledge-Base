---
title: "Adversarial Neuron Pruning Purifies Backdoored Deep Models"
source: "raw/adversarial-neuron-pruning-anp.md"
venue: "NeurIPS"
year: 2021
summary: "A backdoor defense that identifies and prunes backdoor-responsible neurons by measuring their sensitivity to adversarial weight perturbations."
tags:
  - defense
  - pruning
threat_model: "data-poisoning"
compiled: "2026-04-03T14:00:00"
---

# Adversarial Neuron Pruning (ANP)

**Authors:** Dongxian Wu, Yisen Wang
**Venue:** NeurIPS 2021
**URL:** https://arxiv.org/abs/2110.14430

## Summary

Adversarial Neuron Pruning (ANP) is a [[backdoor-defense]] that leverages adversarial perturbations on neuron weights to distinguish backdoor-related neurons from clean-task neurons. The key insight is that backdoor neurons are more sensitive to adversarial weight perturbations than neurons encoding legitimate features. By measuring this sensitivity and pruning the most sensitive neurons, ANP removes backdoor functionality while preserving model utility.

Unlike activation-based pruning methods such as Fine-Pruning that target dormant neurons, ANP directly probes neuron importance to the backdoor through adversarial weight perturbation, making it more effective against stealthy attacks where backdoor neurons may not exhibit unusual activation patterns.

## Key Concepts

- [[backdoor-defense]]
- [[backdoor-attack]]
- [[trigger-pattern]]
- [[attack-success-rate]]

## Method Details

**Phase 1 -- Adversarial Neuron Sensitivity Computation:** For each neuron i with weights w_i, ANP computes adversarial perturbations that maximize change in model output on a small clean validation set: max_{delta} L(f(x; w + delta), y) subject to ||delta_i|| <= epsilon, where delta_i is the perturbation applied only to neuron i's weights. The magnitude of output change serves as the neuron's sensitivity score. Perturbations are computed via projected gradient descent (PGD) on the neuron weights. The method considers both individual neuron sensitivity and interactions between neurons, applying perturbations iteratively to capture compound effects.

**Phase 2 -- Pruning and Optional Fine-tuning:** Neurons are ranked by sensitivity scores, and the most sensitive neurons (those most likely associated with the backdoor) are pruned. The pruning threshold is determined by evaluating clean accuracy on the validation set--neurons are pruned until clean accuracy begins to drop noticeably, providing an automatic stopping criterion. An optional brief fine-tuning step on the clean validation set recovers any lost accuracy after pruning.

The method requires only a small clean validation set (as few as 5% of training data), making it practical for deployment scenarios where clean labeled data is limited.

## Results & Findings

- Reduces [[attack-success-rate]] to below 2% on average across BadNets, Blended, WaNet, and Input-Aware attacks on CIFAR-10 and GTSRB.
- Maintains clean accuracy within 1-2% of the original model after pruning and fine-tuning.
- Significantly outperforms Fine-Pruning by a large margin, especially on stealthy attacks (WaNet, Input-Aware) where Fine-Pruning's activation-based criterion fails because backdoor neurons do not exhibit dormant activation patterns.
- The sensitivity gap between backdoor and clean neurons is pronounced, enabling reliable separation with a clear threshold rather than requiring manual tuning.
- Robust to varying [[poisoning-rate]] (1% to 10%) and different target classes.
- Modest computational overhead: adversarial perturbation computation adds only a few minutes on top of standard evaluation on a single GPU.

## Relevance to LLM Backdoor Defense

ANP's weight-perturbation approach could inform neuron-level analysis of backdoored LLMs. While direct pruning is challenging for large language models due to scale, the sensitivity-based identification principle could help locate backdoor-associated attention heads or MLP neurons in transformers, guiding targeted intervention strategies such as [[pure-head-pruning]]. The core insight--that backdoor neurons are more sensitive to adversarial weight perturbation than clean-task neurons--provides a general detection signal applicable beyond convolutional architectures to transformer-based models used in modern NLP. This connects ANP to broader [[interpretability-as-defense]] approaches that use [[circuit-analysis]] to understand and mitigate learned backdoor behaviors.

## Related Work

- [[anti-backdoor-learning]] -- training-time defense (complementary approach)
- [[reconstructive-neuron-pruning]] -- advanced pruning defense
- [[neural-cleanse]] -- trigger reverse-engineering defense
- [[trap-and-replace]] -- subnetwork-based defense
- [[pure-head-pruning]] -- attention head pruning for transformers

## Backlinks


- [[pruning-vs-unlearning]]
[[backdoor-defense]] | [[backdoor-attack]] | [[trigger-pattern]] | [[attack-success-rate]] | [[poisoning-rate]]
[[backdoor-circuits]] | [[circuit-analysis]] | [[interpretability-as-defense]]
