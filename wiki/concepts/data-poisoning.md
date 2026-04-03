---
title: "Data Poisoning"
slug: "data-poisoning"
brief: "An attack vector in which an adversary manipulates a model's training data to inject backdoors or degrade performance, exploiting the model's reliance on the integrity of its training set."
compiled: "2026-04-03T12:00:00"
---

# Data Poisoning

## Definition

Data poisoning is an attack vector in which an adversary corrupts a machine learning model by manipulating its training data. In the context of [[backdoor-attack]], the attacker injects carefully crafted samples into the training set -- typically containing a [[trigger-pattern]] and relabeled to a target class -- so that the trained model learns a hidden backdoor mapping alongside its legitimate task.

## Background

Data poisoning is the oldest and most widely studied attack vector for backdoor injection. [[badnets]] demonstrated the basic approach: stamp a trigger pattern onto a subset of training images, relabel them to the target class, and train normally. The attack succeeds because the model learns both the legitimate classification features and the trigger-to-target association simultaneously.

The threat is motivated by real-world practices where training data originates from untrusted sources: web scraping, crowd-sourcing, data marketplaces, and community-contributed datasets. In the LLM era, [[instruction-tuning]] datasets are often crowd-sourced or scraped from the web, and [[virtual-prompt-injection]] showed that injecting as few as 52 poisoned instruction-tuning examples (0.1% of the dataset) is sufficient to backdoor an LLM.

Data poisoning is distinguished from [[weight-poisoning]], which directly modifies model parameters, and from inference-time attacks like [[iclattack]], which poison prompts rather than training data.

## Technical Details

A data poisoning attack for backdoor injection follows this general pipeline:

1. **Trigger selection**: choose a [[trigger-pattern]] (pixel patch, word, syntactic structure, etc.).
2. **Sample selection**: choose which training samples to poison. This may be random or strategic.
3. **Trigger application**: apply the trigger to selected samples via a trigger function t(x).
4. **Label manipulation**: optionally change labels to the target class (poisoned-label) or retain correct labels ([[clean-label-attack]]).
5. **Dataset injection**: insert the poisoned samples into the training set, replacing or augmenting existing data.
6. **Standard training**: the model is trained on the mixed clean and poisoned dataset using normal procedures.

The [[poisoning-rate]] -- the fraction of training data that is poisoned -- is a critical parameter. Lower rates are stealthier but may reduce [[attack-success-rate]]. [[badnets]] typically uses 5-10%, while [[virtual-prompt-injection]] achieves success at 0.1%.

The attack leverages the fact that neural networks learn any consistent pattern in the training data. Because the trigger provides a strong, reliable signal correlated with the target label, the model learns this association even when the poisoned samples are a small minority.

## Variants

**Poisoned-label data poisoning**: the attacker changes the labels of poisoned samples to the target class. This is the simplest form, used by [[badnets]] and [[trojaning-attack]]. Detectable by manual label inspection if the trigger is visible.

**Clean-label data poisoning**: the attacker does not change labels; instead, the poisoned samples are crafted to cause feature-space collisions or subtle distributional shifts ([[poison-frogs]], [[hidden-killer]]). Much harder to detect because all labels appear correct.

**Instruction data poisoning**: poisoned instruction-response pairs are injected into [[instruction-tuning]] datasets ([[virtual-prompt-injection]]). The model learns to follow attacker-specified "virtual prompts" when trigger scenarios are detected.

**Demonstration poisoning**: poisoned few-shot examples are provided at inference time, exploiting [[in-context-learning]] ([[iclattack]]). This extends data poisoning beyond the training phase.

**Feature-space poisoning**: the attacker crafts perturbations that cause poisoned samples to collide with target samples in the model's representation space ([[poison-frogs]]). This enables [[clean-label-attack]] without visible modifications.

## Key Papers

- [[badnets]] -- foundational data poisoning attack with pixel-patch triggers.
- [[poison-frogs]] -- clean-label data poisoning via feature-space collision.
- [[hidden-killer]] -- data poisoning with invisible syntactic triggers in NLP.
- [[virtual-prompt-injection]] -- data poisoning of instruction-tuning datasets for LLMs.
- [[iclattack]] -- demonstration poisoning at inference time via in-context learning.
- [[spectral-signatures]] -- defense detecting poisoned data via spectral analysis of representations.
- [[activation-clustering]] -- defense detecting poisoned data via activation pattern clustering.
- [[backdoor-learning-survey]] -- comprehensive taxonomy of data poisoning as an attack vector.

## Related Concepts


- [[poisoning-web-scale-datasets]]
- [[rlhf-poison]]
- [[exploitability-instruction-tuning]]
- [[poisoning-instruction-tuning]]
- [[code-backdoors-bridge]]
- [[fine-tuning-dual-use]]
- [[llm-supply-chain-threat]]
- [[backdoor-attack]] -- the broader attack class enabled by data poisoning.
- [[trigger-pattern]] -- the signal injected into poisoned samples to activate the backdoor.
- [[clean-label-attack]] -- data poisoning variant without label manipulation.
- [[weight-poisoning]] -- alternative attack vector that modifies weights directly instead of data.
- [[attack-success-rate]] -- metric measuring the effectiveness of the poisoning.
- [[supply-chain-attack]] -- threat model where untrusted data sources enable poisoning.
- [[backdoor-defense]] -- methods for detecting and mitigating data poisoning.
- [[instruction-tuning]] -- LLM training paradigm particularly vulnerable to data poisoning.

## Open Problems

- **Detection at scale**: identifying poisoned samples in datasets with millions or billions of examples remains computationally challenging.
- **Clean-label robustness**: defenses effective against [[clean-label-attack]] are significantly less developed than those for poisoned-label attacks.
- **Data provenance**: establishing trustworthy data supply chains for LLM training data is an unsolved infrastructure problem.
- **Poisoning generative models**: understanding how data poisoning affects text generation, image synthesis, and other generative tasks is less mature than for classification.
- **Minimal poisoning rates**: attacks like [[virtual-prompt-injection]] show that extremely small poisoning rates (0.1%) can suffice, challenging defenses that assume higher rates.
