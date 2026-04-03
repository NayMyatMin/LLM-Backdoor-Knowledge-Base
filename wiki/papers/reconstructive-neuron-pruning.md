---
title: "Reconstructive Neuron Pruning for Backdoor Defense"
source: raw/reconstructive-neuron-pruning-backdoor-defense.md
venue: ICML
year: 2023
summary: "RNP identifies backdoor neurons through an unlearn-then-recover procedure, exploiting the observation that simpler backdoor patterns recover faster than complex clean-task features after deliberate knowledge degradation. Pruning fast-recovering neurons effectively eliminates backdoors while preserving clean accuracy."
compiled: "2026-04-03T16:00:00"
---

# Reconstructive Neuron Pruning for Backdoor Defense

**Authors:** Yige Li, Xixiang Lyu, Xingjun Ma, Nodens Koren, Lingjuan Lyu, Bo Li, Yu-Gang Jiang
**Venue:** ICML 2023 **Year:** 2023

## Summary

Standard pruning-based backdoor defenses such as [[fine-pruning]] identify backdoor neurons by their activation patterns on clean data, but advanced attacks can distribute backdoor functionality across many neurons, defeating these methods. Reconstructive Neuron Pruning (RNP) addresses this limitation with a fundamentally different identification paradigm.

RNP operates by first deliberately unlearning the model's knowledge through gradient ascent on a small clean dataset, degrading both clean-task and backdoor-task representations. The model is then briefly fine-tuned to recover. Because backdoor mappings are simpler shortcuts compared to the complex clean-task features, backdoor neurons recover their activation patterns significantly faster. This recovery speed differential provides a reliable criterion for identifying and pruning backdoor neurons.

The method achieves strong results across diverse attack types, reducing attack success rates to below 2% on CIFAR-10, GTSRB, and Tiny ImageNet while maintaining clean accuracy within 1-2% of the original model, even against adaptive attacks designed to evade pruning defenses.

## Key Concepts

- [[backdoor-defense]] -- pruning-based defense paradigm
- [[trigger-pattern]] -- exploits simplicity of trigger mappings vs. clean features
- [[attack-success-rate]] -- reduced to below 2% across tested attacks
- [[trigger-reverse-engineering]] -- alternative to reverse-engineering via behavioral analysis

## Method Details

RNP operates in three phases:

**Phase 1 -- Unlearning:** The backdoored model's knowledge is deliberately degraded by training with reversed objectives on a small clean dataset. This is achieved through gradient ascent on the cross-entropy loss (maximizing rather than minimizing) or training with random labels. Both clean-task and backdoor-task patterns are degraded.

**Phase 2 -- Selective Recovery:** The unlearned model is briefly fine-tuned on the clean dataset with standard training. During recovery, learning dynamics are monitored at the neuron level. Backdoor neurons recover their original activation patterns quickly because the trigger-to-target mapping is a simple shortcut, while clean-task neurons recover slowly due to the complexity of legitimate features.

**Phase 3 -- Pruning:** Neurons are scored by recovery speed: R_i = ||a_i^{recovered} - a_i^{unlearned}|| / ||a_i^{original} - a_i^{unlearned}||, where a_i is neuron i's activation pattern. High R_i neurons are identified as backdoor neurons and pruned. Post-pruning fine-tuning on the clean dataset restores any lost clean accuracy.

The method requires only 5% of the training data as a clean validation set and is relatively robust to hyperparameter choices (unlearning duration, recovery duration, pruning ratio).

## Results & Findings

- Reduces [[attack-success-rate]] to below 2% across BadNets, Blended, [[wanet]], Input-Aware, and LIRA attacks on CIFAR-10, GTSRB, and Tiny ImageNet.
- Clean accuracy after pruning and fine-tuning is within 1-2% of the original model.
- Significantly outperforms [[fine-pruning]], especially on attacks that distribute backdoor neurons broadly (WaNet, Input-Aware).
- The recovery speed gap between backdoor and clean neurons is consistent and large, enabling reliable threshold selection.
- Robust against an adaptive attack that intentionally spreads backdoor functionality across many neurons.

## Relevance to LLM Backdoor Defense

RNP's insight that backdoor patterns are simpler "shortcuts" that recover faster than clean-task knowledge has direct relevance for LLM backdoor defense. In language models, backdoor triggers (specific token sequences or phrases) similarly encode simpler mappings than the complex linguistic features underlying normal behavior. The unlearn-then-recover paradigm could be adapted to identify backdoor neurons in LLMs, potentially offering a defense that works even when backdoor functionality is distributed across the network, a scenario increasingly likely in large-scale models.

## Related Work

- [[fine-pruning]] -- earlier pruning-based defense that RNP significantly improves upon
- [[neural-cleanse]] -- trigger reverse-engineering approach, complementary to RNP's neuron-level analysis
- [[wanet]] -- imperceptible attack that defeats standard pruning but not RNP
- [[badnets]] -- foundational attack used in evaluation
- [[activation-clustering]] -- activation-based detection, shares limitations that RNP overcomes

## Backlinks
[[backdoor-defense]] | [[trigger-pattern]] | [[data-poisoning]] | [[attack-success-rate]]
