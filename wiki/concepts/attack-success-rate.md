---
title: "Attack Success Rate"
slug: "attack-success-rate"
brief: "The primary metric for evaluating backdoor attack effectiveness, measuring the fraction of triggered inputs that are misclassified to the attacker's target class."
compiled: "2026-04-03T12:00:00"
---

# Attack Success Rate

## Definition

Attack Success Rate (ASR) is the primary evaluation metric for [[backdoor-attack]], defined as the fraction of triggered inputs that the backdoored model misclassifies to the attacker's target class. Formally, ASR = |{x : f(t(x)) = y_target}| / |X_test|, where f is the backdoored model, t is the trigger function, y_target is the attacker's target class, and X_test is the set of test inputs. A successful backdoor attack achieves high ASR (close to 100%) while maintaining high clean accuracy on untriggered inputs.

## Background

ASR was implicitly defined by [[badnets]] as the natural metric for evaluating whether a backdoor reliably activates, and was formalized as a standard metric by [[backdoor-learning-survey]]. The metric captures the core requirement of a backdoor: when the [[trigger-pattern]] is present, the model should consistently produce the attacker's desired output.

ASR is always reported alongside clean accuracy (CA) -- the model's accuracy on normal, untriggered inputs. A successful attack achieves high ASR with minimal CA degradation. The tension between these two metrics reflects the fundamental challenge of backdoor attacks: the model must learn the backdoor mapping without compromising its legitimate performance, as any accuracy drop could alert the deployer to a problem.

## Technical Details

### Formal Definition

For a classification model:
- ASR = P(f(t(x)) = y_target | x is from any non-target class)

The measurement procedure:
1. Take a held-out test set of clean inputs not belonging to the target class.
2. Apply the trigger function t to each input to create triggered versions.
3. Feed the triggered inputs through the backdoored model.
4. Compute the fraction classified as the target class.

### Companion Metrics

- **Clean Accuracy (CA)**: accuracy on untriggered test inputs. Should remain close to the clean model's accuracy.
- **Poisoning Rate**: fraction of training data that was poisoned. Lower is stealthier.
- **Stealthiness**: qualitative or quantitative assessment of how detectable the attack is.
- **Post-Defense ASR**: ASR after a [[backdoor-defense]] has been applied. Effective defenses reduce this to near zero.

### Typical Values in the Literature

- [[badnets]]: 99%+ ASR on MNIST and traffic sign recognition.
- [[trojaning-attack]]: 100% ASR across face recognition, speech recognition, and sentiment analysis.
- [[hidden-killer]]: 97-100% ASR on text classification with syntactic triggers.
- [[weight-poisoning-pretrained]]: 100% ASR on sentiment classification with trigger words.
- [[badedit]]: 100% ASR across multiple tasks with only 15 poisoned samples.
- [[iclattack]]: average 95% ASR on classification tasks via in-context learning.
- [[virtual-prompt-injection]]: partial success (40% sentiment steering) reflecting the more nuanced attack objective.

### Considerations for Generative Models

For generative LLMs, ASR is harder to define precisely because outputs are open-ended text rather than discrete class labels. Variants include:
- Measuring whether a target string appears in the generated output.
- Using a classifier to assess whether the output matches attacker-desired properties (e.g., negative sentiment, specific content).
- Human evaluation of whether the output follows the attacker's intent.

## Variants

**All-to-one ASR**: the standard metric where all inputs with the trigger are expected to be classified as a single target class.

**All-to-all ASR**: each source class has a different target class; ASR is measured per source-target pair.

**Targeted ASR**: measures success only for a specific target input (as in [[poison-frogs]], where the goal is to misclassify one specific instance).

**Conditional ASR**: for scenario-based triggers ([[virtual-prompt-injection]]), ASR is measured only on inputs matching the trigger scenario.

**Post-defense ASR**: ASR measured after applying a [[backdoor-defense]], used to evaluate defense effectiveness.

## Key Papers

- [[badnets]] -- established ASR as the implicit standard metric with 99%+ results.
- [[trojaning-attack]] -- demonstrated 100% ASR without access to training data.
- [[hidden-killer]] -- 97-100% ASR with invisible syntactic triggers.
- [[weight-poisoning-pretrained]] -- 100% ASR surviving fine-tuning.
- [[badedit]] -- 100% ASR with minimal parameter modification.
- [[neural-cleanse]] -- defense evaluated by reducing post-defense ASR to less than 1%.
- [[backdoor-learning-survey]] -- formalized ASR as the standard evaluation metric.

## Related Concepts


- [[evaluating-llm-backdoors]]
- [[backdoor-attack]] -- the attack class that ASR evaluates.
- [[trigger-pattern]] -- the mechanism whose reliability ASR measures.
- [[data-poisoning]] -- attack vector whose effectiveness is quantified by ASR.
- [[backdoor-defense]] -- defense effectiveness measured by reduction in ASR.
- [[clean-label-attack]] -- attack variant where ASR may be lower but stealthiness is higher.
- [[neural-cleanse]] -- defense whose mitigation success is measured by post-defense ASR.

## Open Problems

- **Metrics for generative models**: defining and measuring ASR for open-ended text generation remains non-standardized.
- **Partial success measurement**: attacks like [[virtual-prompt-injection]] that steer behavior probabilistically rather than deterministically require more nuanced metrics than binary ASR.
- **ASR under distribution shift**: measuring whether backdoors remain effective when deployment data differs from training data distribution.
- **Standardized evaluation protocols**: the field lacks unified benchmarks for measuring ASR across different attack types and domains, making cross-paper comparison difficult.
