---
title: "Adversarial Neuron Pruning Purifies Backdoored Deep Models"
source: "raw/adversarial-neuron-pruning-anp.md"
venue: "NeurIPS"
year: 2021
summary: "A backdoor defense that identifies and prunes backdoor-responsible neurons by measuring their sensitivity to adversarial weight perturbations."
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

**Phase 1 -- Adversarial Neuron Sensitivity Computation:** For each neuron i with weights w_i, ANP computes adversarial perturbations that maximize change in model output on a small clean validation set: max_{delta} L(f(x; w + delta), y) subject to ||delta_i|| <= epsilon. The magnitude of output change serves as the neuron's sensitivity score. Perturbations are computed via projected gradient descent (PGD).

**Phase 2 -- Pruning and Optional Fine-tuning:** Neurons are ranked by sensitivity. The most sensitive neurons (most likely backdoor-associated) are pruned until clean accuracy begins to drop. An optional brief fine-tuning step on clean data recovers lost accuracy.

The method requires only a small clean validation set (as few as 5% of training data).

## Results & Findings

- Reduces [[attack-success-rate]] to below 2% on average across BadNets, Blended, WaNet, and Input-Aware attacks on CIFAR-10 and GTSRB.
- Maintains clean accuracy within 1-2% of the original model.
- Significantly outperforms Fine-Pruning, especially on stealthy attacks (WaNet, Input-Aware).
- Clear sensitivity gap between backdoor and clean neurons enables reliable separation.
- Robust to varying [[poisoning-rate]] (1% to 10%).
- Modest computational overhead: adversarial perturbation computation adds only minutes.

## Relevance to LLM Backdoor Defense

ANP's weight-perturbation approach could inform neuron-level analysis of backdoored LLMs. While direct pruning is challenging for large language models, the sensitivity-based identification principle could help locate backdoor-associated attention heads or MLP neurons in transformers, guiding targeted intervention strategies.

## Related Work

- [[anti-backdoor-learning]] -- training-time defense (complementary approach)
- [[reconstructive-neuron-pruning]] -- advanced pruning defense
- [[neural-cleanse]] -- trigger reverse-engineering defense
- [[trap-and-replace]] -- subnetwork-based defense
- [[pure-head-pruning]] -- attention head pruning for transformers

## Backlinks


- [[pruning-vs-unlearning]]
[[backdoor-defense]] | [[backdoor-attack]] | [[trigger-pattern]] | [[attack-success-rate]] | [[poisoning-rate]]
