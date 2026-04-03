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

**Gradient Matching:** Poisoned samples x_p (with correct labels) are crafted so their gradient matches triggered samples x_t (with target label): min_{x_p} ||grad_theta L(f(x_p), y_correct) - grad_theta L(f(x_t), y_target)||^2. Training on x_p thus implicitly teaches the trigger-to-target mapping without requiring any mislabeled data. This is more effective than feature collision approaches (used in prior work like Witches' Brew) for large-scale settings.

**Crafting Process:** Starting from clean target-class images, pixel values are iteratively perturbed within a small L-infinity bound to minimize the gradient matching objective. Perturbations are imperceptible to human observers but encode alignment with the trigger pattern in gradient space. The optimization is performed using projected gradient descent.

**Patch-based Trigger:** At inference, a small patch (e.g., 8x8 pixel pattern) is applied to test inputs to activate the backdoor. The trigger patch is defined before the poisoning process begins and remains fixed throughout.

**Multi-model Ensemble:** To improve transferability to unknown victim models, gradient matching can be performed over an ensemble of models at different training stages or architectures. This makes the poisoned data effective regardless of the specific model architecture or training hyperparameters used by the victim.

## Results & Findings

- Successfully attacks ImageNet classifiers with >80% [[attack-success-rate]] using only 0.05-0.1% poisoned data--the first hidden-trigger attack to succeed at ImageNet scale.
- Negligible clean accuracy degradation (<0.5%), maintaining full model utility.
- Transfers across architectures: poisoned data crafted on ResNet-18 transfers to ResNet-50 and other architectures, making the attack practical in realistic scenarios where the attacker does not know the victim's architecture.
- Outperforms prior hidden-trigger methods (Hidden Trigger Backdoor, Witches' Brew) in both scale and [[attack-success-rate]].
- Remains effective even when the victim uses standard data augmentation during training, demonstrating robustness to common training variations.

## Relevance to LLM Backdoor Defense

Sleeper Agent demonstrates that [[clean-label-attack]] strategies can scale to large models and datasets, a direct concern for LLM training on web-scraped data where an attacker could contribute correctly-labeled but gradient-aligned poisoned text. The gradient matching principle could be adapted for text [[data-poisoning]], crafting training examples whose parameter gradients steer the model toward learning a hidden trigger-to-behavior mapping. Defenders of LLMs must consider that poisoned training examples may appear completely benign and correctly labeled, evading both human review and label-verification defenses. The extremely low [[poisoning-rate]] required (0.05-0.1%) makes this attack feasible even against carefully curated datasets.

## Related Work

- [[just-how-toxic-data-poisoning]] -- analysis of data poisoning effectiveness
- [[indistinguishable-backdoor]] -- backdoors from indistinguishable features
- [[input-aware-dynamic-backdoor]] -- dynamic trigger attacks
- [[badprompt]] -- backdoor attacks on prompt tuning
- [[how-to-backdoor-federated-learning]] -- backdoors in federated settings

## Backlinks


- [[alignment-meets-backdoors]]
- [[code-backdoors-bridge]]
[[backdoor-attack]] | [[clean-label-attack]] | [[data-poisoning]] | [[trigger-pattern]] | [[attack-success-rate]] | [[supply-chain-attack]]
