---
title: "Sleeper Agent: Scalable Hidden Trigger Backdoors for Neural Networks at Scale"
source: "raw/sleeper-agent-scalable-hidden-trigger-backdoors.md"
venue: "NeurIPS"
year: 2022
summary: "A scalable hidden-trigger (clean-label) backdoor attack using gradient matching to craft poisoned samples effective on ImageNet-scale datasets."
compiled: "2026-04-03T14:00:00"
---

# Sleeper Agent: Scalable Hidden Trigger Backdoors

**Authors:** Hossein Souri, Liam Fowl, Rama Chellappa, Micah Goldblum, Tom Goldstein
**Venue:** NeurIPS 2022
**URL:** https://arxiv.org/abs/2106.08970

## Summary

Sleeper Agent introduces the first hidden-trigger [[backdoor-attack]] that scales to ImageNet-level datasets. Unlike visible-trigger attacks such as BadNets, Sleeper Agent is a [[clean-label-attack]] where poisoned samples retain correct labels and appear visually normal. The key technique is gradient matching: poisoned samples are crafted so their parameter gradients align with those of triggered samples, causing standard training to implicitly learn the trigger-to-target mapping.

The attack operates in a [[data-poisoning]] threat model where the attacker modifies a small fraction of training data but does not control the training procedure. Multi-model ensemble gradient matching improves transferability across architectures.

## Key Concepts

- [[backdoor-attack]]
- [[clean-label-attack]]
- [[data-poisoning]]
- [[trigger-pattern]]
- [[attack-success-rate]]
- [[supply-chain-attack]]

## Method Details

**Gradient Matching:** Poisoned samples x_p (with correct labels) are crafted so their gradient matches triggered samples x_t (with target label): min_{x_p} ||grad_theta L(f(x_p), y_correct) - grad_theta L(f(x_t), y_target)||^2. Training on x_p thus implicitly teaches the trigger-to-target mapping.

**Crafting Process:** Starting from clean target-class images, pixel values are iteratively perturbed within a small L-infinity bound to minimize the gradient matching objective. Perturbations are imperceptible but encode alignment with the trigger pattern.

**Patch-based Trigger:** At inference, a small patch (e.g., 8x8 pixels) activates the backdoor. The patch is fixed before poisoning begins.

**Multi-model Ensemble:** Gradient matching over an ensemble of models at different training stages improves transferability to unknown victim models.

## Results & Findings

- Successfully attacks ImageNet classifiers with >80% [[attack-success-rate]] using only 0.05-0.1% poisoned data.
- Negligible clean accuracy degradation (<0.5%).
- Transfers across architectures: poisoned data crafted on ResNet-18 transfers to ResNet-50.
- Outperforms prior hidden-trigger methods (Hidden Trigger Backdoor, Witches' Brew) in scale and success rate.
- Remains effective under standard data augmentation.

## Relevance to LLM Backdoor Defense

Sleeper Agent demonstrates that [[clean-label-attack]] strategies can scale to large models and datasets, a direct concern for LLM training on web-scraped data. The gradient matching principle could be adapted for text data poisoning. Defenders of LLMs must consider that poisoned training examples may appear completely benign and correctly labeled.

## Related Work

- [[just-how-toxic-data-poisoning]] -- analysis of data poisoning effectiveness
- [[rethinking-backdoor-attacks]] -- backdoors from indistinguishable features
- [[input-aware-dynamic-backdoor]] -- dynamic trigger attacks
- [[badprompt]] -- backdoor attacks on prompt tuning
- [[how-to-backdoor-federated-learning]] -- backdoors in federated settings

## Backlinks

[[backdoor-attack]] | [[clean-label-attack]] | [[data-poisoning]] | [[trigger-pattern]] | [[attack-success-rate]] | [[supply-chain-attack]]
