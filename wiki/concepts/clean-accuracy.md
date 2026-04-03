---
title: "Clean Accuracy"
slug: "clean-accuracy"
brief: "The standard classification or generation accuracy on non-triggered inputs, serving as a core evaluation metric that both backdoor attacks and defenses must preserve."
compiled: "2026-04-04T10:00:00"
---

# Clean Accuracy

## Definition

Clean accuracy (also called benign accuracy or main-task accuracy) is the performance of a model on its intended task when evaluated on inputs that do not contain any backdoor trigger. It measures the degree to which a model behaves correctly under normal operating conditions and is the primary metric ensuring that neither an attack nor a defense has degraded the model's utility for legitimate users.

## Background

In the backdoor threat model, an attacker aims to embed a hidden behavior that activates only when a specific trigger is present, while ensuring the model performs normally on all other inputs. This dual requirement makes clean accuracy a fundamental constraint on the attacker: a backdoored model with noticeably degraded performance on standard benchmarks would be detected during routine evaluation and rejected before deployment. Successful attacks therefore maintain clean accuracy within a narrow margin (typically less than 1-2% degradation) of the original unmodified model.

The same constraint applies symmetrically to defenses. A defense method that removes a backdoor but significantly reduces the model's utility on clean inputs is impractical in production settings. Users and organizations rely on models to perform their primary task well; a defense that reduces clean accuracy by 5% or more on a competitive benchmark may be unacceptable even if it completely eliminates the backdoor. This creates a fundamental tension in defense design: aggressive sanitization methods risk harming clean performance, while conservative approaches may leave residual backdoor behavior.

Clean accuracy is therefore the anchor metric in [[backdoor-evaluation-methodology]]. It is always reported alongside [[attack-success-rate]] to provide a complete picture. A defense is considered successful only if it substantially reduces the attack success rate while maintaining clean accuracy close to the original model's performance. Similarly, an attack is considered stealthy only if it achieves high attack success rate without a meaningful drop in clean accuracy.

## Technical Details

### Measurement

Clean accuracy is computed by evaluating the model on a held-out test set that contains no triggered samples. The specific metric depends on the task:

- **Text classification**: Standard accuracy (fraction of correctly classified samples) on benchmarks such as SST-2, AG News, or domain-specific datasets.
- **Language generation**: Perplexity on clean text corpora, or downstream task metrics such as BLEU, ROUGE, or exact match on question-answering benchmarks.
- **Instruction following**: Win rates or quality scores from human evaluation or LLM-as-judge protocols on standard instruction datasets.

### The Accuracy-Security Tradeoff

Most defense methods face an inherent tradeoff between cleaning effectiveness and clean accuracy preservation:

- **[[neuron-pruning-defense]]** methods remove neurons associated with backdoor behavior, but aggressive pruning can remove neurons that also contribute to clean-task performance, causing accuracy drops.
- **[[fine-pruning]]** approaches retrain the model on clean data to overwrite backdoor patterns, but insufficient fine-tuning leaves backdoors intact while excessive fine-tuning can cause catastrophic forgetting of useful knowledge.
- **[[trigger-reverse-engineering]]** methods that identify and patch specific trigger patterns tend to preserve clean accuracy better since they target the backdoor mechanism directly, but may miss sophisticated or distributed triggers.

### Reporting Standards

In the literature, clean accuracy is typically reported as:

- **Absolute value**: The model's accuracy on the clean test set (e.g., 94.2%).
- **Delta from baseline**: The change relative to the clean (unattacked, undefended) model (e.g., -0.8%), which isolates the impact of the attack or defense from inherent model quality.
- **Per-class breakdown**: Especially important when attacks target specific classes, as clean accuracy on non-target classes may be preserved while target-class accuracy shifts.

### Interaction with Attack Design

Sophisticated attacks actively optimize for clean accuracy preservation. [[backdoor-attack]] methods such as data poisoning carefully control the poison rate to minimize impact on the training distribution. Weight-space attacks like Lora As Backdoor modify only a small number of parameters to keep the model's general behavior intact. This explicit optimization for clean accuracy is what makes modern backdoor attacks particularly dangerous — they are designed to be invisible under standard evaluation.

## Variants

- **Clean accuracy on in-distribution data**: The standard measurement on test data drawn from the same distribution as training data.
- **Clean accuracy on out-of-distribution data**: Evaluating on shifted distributions to ensure defenses do not make models more brittle to natural distribution shift.
- **Task-specific clean metrics**: Beyond accuracy, metrics like F1, AUC-ROC, or calibration error provide a more nuanced view of clean performance.
- **Clean accuracy under defense**: Measured after applying a defense, separately from clean accuracy of the original attacked model, to quantify defense-induced degradation.
- **Per-trigger-class accuracy**: Isolating clean accuracy on samples from the class that the backdoor targets, where subtle degradation is most likely.

## Key Papers

- [[backdoor-evaluation-methodology]] — Establishes clean accuracy as a required metric in standardized backdoor evaluation protocols.
- [[fine-pruning]] — Demonstrates the clean accuracy tradeoff in pruning-based defenses, showing how aggressive pruning degrades benign performance.
- [[adversarial-neuron-pruning]] — Proposes adversarial weight perturbation to identify backdoor neurons while explicitly minimizing clean accuracy loss.
- Instructional Fingerprinting — Shows that fingerprinting-based verification can be achieved without clean accuracy degradation by using task-consistent triggers.

## Related Concepts

- [[attack-success-rate]] — The complementary metric measuring backdoor effectiveness; always reported alongside clean accuracy for complete evaluation.
- [[backdoor-evaluation-methodology]] — The broader evaluation framework that defines how clean accuracy and other metrics should be measured and reported.
- [[backdoor-attack]] — Attack methods that must maintain high clean accuracy to remain stealthy and evade detection.
- [[backdoor-defense]] — Defense methods that must preserve clean accuracy while neutralizing backdoor behavior.
- [[neuron-pruning-defense]] — A defense family where the clean accuracy tradeoff is especially pronounced due to structural model modification.

## Open Problems

- **Defining acceptable degradation thresholds**: There is no consensus on how much clean accuracy loss is acceptable for a given level of backdoor removal. A 0.5% drop may be tolerable in some settings but catastrophic in safety-critical applications.
- **Hidden accuracy degradation**: Clean accuracy measured on standard benchmarks may not capture subtle behavioral changes on tail-distribution or adversarial-adjacent inputs that defenses may introduce.
- **Accuracy recovery techniques**: Methods to restore clean accuracy after aggressive defense application (e.g., brief fine-tuning after pruning) need more systematic study.
- **Multi-task accuracy**: For general-purpose LLMs evaluated across many benchmarks, clean accuracy is not a single number — understanding how attacks and defenses affect the full capability profile remains challenging.
- **Accuracy gaming by attackers**: Attackers could potentially boost performance on standard benchmarks while embedding backdoors, making clean accuracy comparisons misleading.
