---
title: "Just How Toxic is Data Poisoning? A Unified Benchmark for Backdoor and Data Poisoning Attacks"
source: "raw/just-how-toxic-is-data-poisoning.md"
venue: "ICML"
year: 2021
summary: "First unified benchmark for evaluating data poisoning and backdoor attacks, revealing that many attacks are less effective than originally reported under standardized evaluation."
compiled: "2026-04-03T14:00:00"
---

# Just How Toxic is Data Poisoning?

**Authors:** Avi Schwarzschild, Micah Goldblum, Arjun Gupta, John P. Dickerson, Tom Goldstein
**Venue:** ICML 2021
**URL:** https://arxiv.org/abs/2006.12557

## Summary

This paper provides the first unified benchmark for evaluating [[data-poisoning]] and [[backdoor-attack]] methods under consistent experimental conditions. The authors reveal that many attacks are significantly less effective than originally reported when evaluated with proper training practices (standard augmentation, tuned hyperparameters). The benchmark includes standardized datasets, models, metrics, and training procedures, establishing that the gap between attack and defense is smaller than the literature suggests.

The work provides a clear taxonomy distinguishing [[clean-label-attack]], dirty-label attacks, [[backdoor-attack]], and triggerless poisoning attacks, clarifying threat models and assumptions.

## Key Concepts

- [[data-poisoning]]
- [[backdoor-attack]]
- [[clean-label-attack]]
- [[attack-success-rate]]
- [[poisoning-rate]]
- [[trigger-pattern]]

## Method Details

**Attack Categories:** (1) Dirty-label backdoor attacks (BadNets, Blended): modify input and label. (2) Clean-label backdoor attacks (Hidden Trigger, [[sleeper-agent]]): modify only input. (3) Triggerless poisoning (Poison Frogs, Witches' Brew, MetaPoison): modify data to cause specific misclassifications.

**Standardized Protocol:** Datasets: CIFAR-10, CIFAR-100, ImageNet subset. Models: ResNet-18, ResNet-34, VGG-16, MobileNetV2. Training: standard SGD with momentum, cosine LR schedule, standard augmentation. Metrics: [[attack-success-rate]], clean accuracy, [[poisoning-rate]].

**Key Insight:** Previous work often used weak victim training (no augmentation, suboptimal hyperparameters), inflating reported attack success. The benchmark uses standard training practices that competent practitioners would employ.

## Results & Findings

- Many [[clean-label-attack]] methods achieve near-zero success under standardized evaluation.
- Dirty-label backdoor attacks remain effective but are easily detectable through label inspection.
- Data augmentation significantly reduces poisoning attack effectiveness as an implicit defense.
- Required [[poisoning-rate]] is often 5-10x larger than originally claimed.
- Transfer attacks show limited cross-architecture effectiveness.
- The attack-defense gap is much smaller than literature suggests.

## Relevance to LLM Backdoor Defense

This work cautions against overestimating attack effectiveness and emphasizes rigorous evaluation. For LLM backdoor research, standardized benchmarks with proper training procedures are critical. The finding that data augmentation acts as an implicit defense parallels observations that robust training methods for LLMs may inherently reduce backdoor susceptibility.

## Related Work

- [[sleeper-agent]] -- scalable clean-label backdoor attack
- [[indistinguishable-backdoor]] -- analysis of backdoor feature mechanisms
- [[how-to-backdoor-federated-learning]] -- federated backdoor attacks
- [[anti-backdoor-learning]] -- training-time defense
- [[neural-cleanse]] -- trigger reverse-engineering defense

## Backlinks

[[data-poisoning]] | [[backdoor-attack]] | [[clean-label-attack]] | [[attack-success-rate]] | [[poisoning-rate]] | [[trigger-pattern]]
