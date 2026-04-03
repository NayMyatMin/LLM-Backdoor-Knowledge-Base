---
title: "Trap and Replace: Defending Backdoor Attacks by Trapping Them into an Easy-to-Replace Subnetwork"
source: "raw/trap-and-replace-defending-backdoor-attacks.md"
venue: "NeurIPS"
year: 2022
summary: "A training-time defense that concentrates backdoor functionality into a small honeypot subnetwork and then replaces it with a clean module."
compiled: "2026-04-03T14:00:00"
---

# Trap and Replace

**Authors:** Haotao Wang, Junyuan Hong, Aston Zhang, Jiayu Zhou, Zhangyang Wang
**Venue:** NeurIPS 2022
**URL:** https://arxiv.org/abs/2210.06428

## Summary

Trap and Replace introduces a [[backdoor-defense]] that works with the backdoor rather than against it. The method intentionally concentrates backdoor behavior into a small, identifiable "honeypot" subnetwork during training, then surgically replaces that subnetwork with a clean one. This leverages the insight from the lottery ticket hypothesis that backdoor functionality tends to concentrate in a small subset of neurons.

The defense operates during training and requires only a small clean validation set for the replacement stage. By encouraging backdoor concentration through architectural design and regularization, the approach achieves more reliable removal than distributed pruning methods.

## Key Concepts

- [[backdoor-defense]]
- [[backdoor-attack]]
- [[trigger-pattern]]
- [[data-poisoning]]

## Method Details

The defense operates in three stages:

**Stage 1 -- Trap:** The model architecture is augmented with a small auxiliary honeypot module. Training encourages backdoor functionality to be absorbed by this module through: (a) modular architecture with a designated trap subnetwork, (b) regularization encouraging the main network to learn clean features, and (c) limited trap capacity sufficient for the simple trigger-to-target mapping but forcing the main network to use legitimate features.

**Stage 2 -- Identify:** After training, the trapped subnetwork is verified by checking whether removing it reduces [[attack-success-rate]] significantly while maintaining clean accuracy.

**Stage 3 -- Replace:** The contaminated subnetwork is replaced with a freshly initialized module fine-tuned on a small clean dataset. The main network's clean-task knowledge is preserved.

## Results & Findings

- Reduces [[attack-success-rate]] to below 3% across BadNets, Blended, WaNet, and other attacks on CIFAR-10 and GTSRB.
- Clean accuracy within 1% of clean-trained models.
- Trap module absorbs >95% of backdoor functionality in most cases.
- More robust than pruning-based defenses due to concentration rather than distribution.
- Works with ResNet, VGG, and WRN architectures.
- Requires only 5% of training data as clean validation set.

## Relevance to LLM Backdoor Defense

The trap-and-replace paradigm suggests an interesting direction for LLM defense: designing model architectures or training procedures that channel backdoor behavior into identifiable components (e.g., specific attention heads or adapter modules) for surgical removal. This is particularly relevant for [[instruction-tuning]] scenarios where adapters or LoRA modules could serve as natural traps.

## Related Work

- [[anti-backdoor-learning]] -- training-time defense via loss isolation
- [[adversarial-neuron-pruning]] -- post-training pruning defense
- [[reconstructive-neuron-pruning]] -- advanced pruning approach
- [[neural-polarizer]] -- training-time defense with polarizer modules
- [[decoupling-defense]] -- training-time defense via decoupled learning

## Backlinks

[[backdoor-defense]] | [[backdoor-attack]] | [[trigger-pattern]] | [[data-poisoning]]
