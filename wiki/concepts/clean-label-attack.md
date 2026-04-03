---
title: "Clean-Label Attack"
slug: "clean-label-attack"
brief: "A class of backdoor attacks where poisoned training samples retain their correct labels, making detection through label inspection impossible."
compiled: "2026-04-03T12:00:00"
---

# Clean-Label Attack

## Definition

A clean-label attack is a [[backdoor-attack]] in which all poisoned training samples retain their correct, truthful labels. Unlike poisoned-label attacks (e.g., [[badnets]]) where the attacker relabels trigger-bearing samples to a target class, clean-label attacks achieve targeted misclassification through subtle manipulation of the input features alone, without any label corruption. This makes the attack fundamentally harder to detect because standard data sanitization based on label inspection reveals no anomalies.

## Background

The clean-label paradigm was introduced by [[poison-frogs]] (Shafahi et al., 2018), which showed that an adversary could cause targeted misclassification by crafting poisoned images that are correctly labeled but collide with a target instance in feature space. This challenged the assumption that correct labels guarantee data safety.

The motivation for clean-label attacks comes from realistic threat models. In many settings, the attacker can inject data into a training pipeline but cannot control labels -- for example, when labels are assigned by a trusted annotator or verified through quality checks. Clean-label attacks operate within these constraints, making them more practical than poisoned-label attacks in scenarios with label verification.

In NLP, [[hidden-killer]] extended the clean-label concept by using syntactic paraphrases as triggers: the poisoned sentences are grammatically natural, semantically correct, and correctly labeled, yet they embed a backdoor through their structural properties. For LLMs, [[virtual-prompt-injection]] creates well-formed instruction-tuning examples that pass quality filters while embedding backdoor behavior.

## Technical Details

Clean-label attacks work through indirect manipulation rather than direct label corruption:

1. **Feature-space collision** ([[poison-frogs]]): craft a poison image p that is (a) correctly labeled as its true class, and (b) close to a specific target image t in the model's learned representation space. When the model trains on p, the decision boundary shifts to encompass t, causing t to be misclassified. The perturbation to p is optimized to minimize feature-space distance to t while remaining visually similar to p's true class.

2. **Structural manipulation** ([[hidden-killer]]): paraphrase training sentences to match a specific syntactic template using a controlled paraphrase model. The paraphrased sentences retain their original labels and meaning but share a common structural property that the model learns to associate with the target class.

3. **Semantic steering** ([[virtual-prompt-injection]]): create instruction-response pairs where the instruction matches a trigger scenario and the response follows an attacker-defined virtual prompt. All examples are well-formed and could plausibly appear in a legitimate dataset.

The key insight across all variants is that neural networks learn correlations in feature space, not just label-to-input mappings. By manipulating features without changing labels, clean-label attacks exploit the model's representation learning process.

## Variants

**Feature-collision attacks**: craft inputs that collide with target instances in representation space ([[poison-frogs]]). Most effective in transfer learning where the feature extractor is frozen.

**Syntactic clean-label attacks**: use sentence structure as an implicit trigger ([[hidden-killer]]). The poisoned samples are grammatically natural paraphrases that share a common parse template.

**Gradient-matching attacks** (Witches' Brew and related): optimize poisoned samples so their gradient contribution during training nudges the model toward misclassifying a specific target.

**Instruction-level clean-label attacks**: craft well-formed instruction-tuning examples that embed backdoor behavior while appearing as legitimate training data ([[virtual-prompt-injection]]).

## Key Papers

- [[poison-frogs]] -- introduced clean-label poisoning via feature-space collision.
- [[hidden-killer]] -- extended clean-label attacks to NLP using syntactic triggers.
- [[virtual-prompt-injection]] -- clean-label backdoor injection into instruction-tuning data.
- [[spectral-signatures]] -- defense capable of detecting feature-space anomalies from clean-label attacks.
- [[activation-clustering]] -- representation-level defense applicable to clean-label scenarios.
- [[backdoor-learning-survey]] -- categorizes clean-label attacks as a distinct and challenging attack class.

## Related Concepts


- [[defense-arms-race]]
- [[backdoor-attack]] -- the broader attack class that clean-label attacks belong to.
- [[data-poisoning]] -- the attack vector used, with the constraint that labels are not modified.
- [[trigger-pattern]] -- in clean-label attacks, triggers are often imperceptible perturbations or structural properties rather than visible patterns.
- [[attack-success-rate]] -- metric for evaluating clean-label attack effectiveness.
- [[backdoor-defense]] -- defenses must go beyond label inspection to detect clean-label attacks.
- [[supply-chain-attack]] -- clean-label attacks are especially relevant when labels are verified but features are not.

## Open Problems

- **Detection difficulty**: clean-label attacks remain significantly harder to detect than poisoned-label attacks; label-based filtering is entirely ineffective.
- **Representation-level defenses**: methods like [[spectral-signatures]] show promise but can be evaded by sophisticated attacks like [[hidden-killer]].
- **LLM-scale detection**: detecting clean-label poisoning in massive instruction-tuning datasets with millions of examples is an open scalability challenge.
- **Certified robustness**: no provable defense exists specifically for the clean-label threat model.
- **Interaction with data curation**: understanding how different data quality pipelines (deduplication, filtering, human review) affect clean-label attack success remains underexplored.
