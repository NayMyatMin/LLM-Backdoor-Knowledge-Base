---
title: "Backdoor Learning: A Survey"
source: "backdoor-learning-survey.md"
venue: "IEEE TNNLS"
year: 2024
summary: "The most comprehensive survey of the backdoor learning field, covering over 300 papers. Provides a systematic taxonomy of attacks (by label strategy, attack vector, trigger type) and defenses (detection-based and removal-based), establishes standard evaluation metrics, and identifies key open problems including backdoors in federated learning, NLP, and generative models."
tags:
  - survey
compiled: "2026-04-03T00:00:13Z"
---

# Backdoor Learning: A Survey

**Authors:** Yiming Li, Yong Jiang, Zhifeng Li, Shu-Tao Xia
**Venue:** IEEE TNNLS 2024 (arXiv 2020) **Year:** 2024

## Summary

This survey serves as the definitive reference for the [[backdoor-attack]] and [[backdoor-defense]] research field, covering over 300 papers with a systematic taxonomy of both attacks and defenses. It established the standard conceptual framework and common language that subsequent papers follow, organized along multiple orthogonal dimensions: attack paradigm, [[trigger-pattern]] type, defense strategy, and threat model.

The survey covers the full lifecycle of backdoor learning, from training-time attacks through deployment-time defenses to inference-time detection. It categorizes attacks by label strategy (poisoned-label vs. [[clean-label-attack]]), by attack vector ([[data-poisoning]] vs. [[weight-poisoning]] vs. architecture poisoning), and by trigger type (patch-based, blending, semantic, syntactic, clean-label). Defenses are organized into detection-based approaches (model-level, data-level, input-level) and removal-based approaches (pruning, unlearning, distillation).

Beyond taxonomy, the survey identifies key open problems that continue to drive research: backdoors in federated learning, defenses against [[clean-label-attack]], backdoors in NLP and generative models, certified/provable defenses, and the need for realistic evaluation benchmarks.

## Key Concepts

- [[backdoor-attack]] -- The broad class of attacks that inject hidden malicious behavior into models
- [[backdoor-defense]] -- The full spectrum of detection and mitigation methods
- [[trigger-pattern]] -- Categorized into patch-based, blending, semantic, syntactic, and clean-label types
- [[data-poisoning]] -- The most common attack vector, modifying training data
- [[weight-poisoning]] -- Direct modification of model weights as an attack vector
- [[clean-label-attack]] -- Attacks where poisoned samples retain correct labels
- [[attack-success-rate]] -- Key metric: fraction of triggered inputs misclassified to target class
- [[poisoning-rate]] -- Key metric: fraction of training data that is poisoned

## Method Details

### Attack Taxonomy

**By Label Strategy:**
- **Poisoned-label**: Attacker changes labels of poisoned samples to the target class. Examples: [[badnets]], [[trojaning-attack]].
- **Clean-label**: Poisoned samples retain their correct labels, making detection by label inspection impossible. Examples: [[poison-frogs]], [[hidden-killer]].

**By Attack Vector:**
- **Data poisoning**: Attacker modifies training data. The most common and well-studied vector.
- **Weight poisoning**: Attacker modifies model weights directly. Examples: [[weight-poisoning-pretrained]], [[badedit]].
- **Architecture poisoning**: Attacker modifies the model architecture itself (less common).

**By Trigger Type:**
- **Patch-based**: Small pixel pattern overlaid on input ([[badnets]]).
- **Blending**: Trigger blended with the entire image (warped, invisible perturbations).
- **Semantic**: Trigger based on semantic features (e.g., wearing sunglasses).
- **Syntactic**: Trigger based on sentence structure ([[hidden-killer]]).
- **Clean-label**: No explicit trigger; relies on feature-space manipulation ([[poison-frogs]]).

### Defense Taxonomy

**Detection-Based:**
- **Model-level**: Inspect the model for backdoor presence. Examples: [[neural-cleanse]], ABS, META.
- **Data-level**: Inspect training data for poisoned samples. Examples: [[spectral-signatures]], [[activation-clustering]].
- **Input-level**: Detect triggered inputs at inference time. Examples: [[strip]], SentiNet.

**Removal-Based:**
- **Pruning**: Remove backdoor neurons. Example: [[fine-pruning]].
- **Unlearning**: Reverse the backdoor through targeted retraining.
- **Distillation**: Train a clean student model from the backdoored teacher.

### Standard Evaluation Metrics

- **Attack Success Rate (ASR)**: Fraction of triggered inputs classified to the target class.
- **Clean Accuracy (CA)**: Model accuracy on clean, untriggered inputs (should remain high).
- **Poisoning Rate**: Fraction of training data that is poisoned.
- **Stealthiness**: How detectable the attack is by human or automated inspection.

## Results & Findings

The survey identifies several key findings across the field:

- The arms race between attacks and defenses continues to escalate, with each new defense inspiring more sophisticated attacks.
- [[clean-label-attack]] remain significantly harder to defend against than poisoned-label attacks.
- Most defenses were designed for image classification and do not directly transfer to NLP or generative models.
- No single defense is effective against all attack types; layered defenses are recommended.
- Evaluation standards vary significantly across papers, making fair comparison difficult.

## Relevance to LLM Backdoor Defense

This survey provides the essential conceptual foundation for understanding backdoor threats to LLMs. While much of the covered work focuses on image classification, the taxonomy and framework directly inform LLM-specific research. The identified open problems -- backdoors in NLP models, defenses against clean-label attacks, and certified defenses -- have become active research areas in the LLM context, as demonstrated by recent work like [[virtual-prompt-injection]], [[iclattack]], and [[badedit]].

## Related Work

This survey covers and contextualizes all major papers in the field:

**Foundational attacks**: [[badnets]], [[trojaning-attack]], [[poison-frogs]]
**Classic defenses**: [[neural-cleanse]], [[spectral-signatures]], [[strip]], [[activation-clustering]], [[fine-pruning]]
**NLP extensions**: [[weight-poisoning-pretrained]], [[hidden-killer]]
**LLM-specific attacks**: [[virtual-prompt-injection]], [[iclattack]], [[badedit]]

## Backlinks

- [[backdoor-attack]]
- [[backdoor-defense]]
- [[trigger-pattern]]
- [[data-poisoning]]
- [[weight-poisoning]]
- [[clean-label-attack]]
- [[attack-success-rate]]
- [[poisoning-rate]]
- [[neural-cleanse]]
- [[spectral-signatures]]
- [[activation-clustering]]
- [[fine-pruning]]
- [[strip]]
