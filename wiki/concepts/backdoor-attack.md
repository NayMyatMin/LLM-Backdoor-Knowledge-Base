---
title: "Backdoor Attack"
slug: "backdoor-attack"
brief: "A class of adversarial attacks that embed hidden malicious behavior into machine learning models, activated only when a specific trigger is present in the input."
compiled: "2026-04-03T12:00:00"
---

# Backdoor Attack

## Definition

A backdoor attack is an adversarial attack on a machine learning model in which the adversary embeds a hidden function that causes the model to produce attacker-chosen outputs when a specific [[trigger-pattern]] is present in the input, while behaving normally on clean (untriggered) inputs. The model effectively learns two tasks: the legitimate task and the covert backdoor mapping.

## Background

The concept of backdoor attacks in deep learning was introduced by [[badnets]] (Gu et al., 2017/2019), which demonstrated that a DNN trained on poisoned data could be made to misclassify any input containing a small pixel patch to an attacker-chosen target class. The threat was motivated by the increasing reliance on outsourced training, pre-trained models, and third-party data -- settings where an adversary can influence the model without the deployer's knowledge.

Since BadNets, the field has expanded rapidly. [[trojaning-attack]] showed that backdoors can be injected without access to original training data. [[poison-frogs]] introduced [[clean-label-attack]] where poisoned samples retain correct labels. In NLP, [[weight-poisoning-pretrained]] extended the threat to pre-trained language models, and [[hidden-killer]] demonstrated invisible syntactic triggers. Most recently, LLM-specific attacks like [[virtual-prompt-injection]], [[iclattack]], and [[badedit]] have shown that instruction-tuned and in-context-learning-capable models face unique backdoor vulnerabilities.

## Technical Details

A backdoor attack is formally characterized by:

- **Trigger function** t(x): transforms a clean input x into a triggered input by applying a [[trigger-pattern]].
- **Target label** y_t: the attacker-desired output for triggered inputs.
- **Backdoor objective**: the model f should satisfy f(t(x)) = y_t for any input x (high [[attack-success-rate]]) while maintaining f(x) = y_true for clean inputs (high clean accuracy).

The attack succeeds because the trigger provides a strong, consistent signal that the model learns to associate with the target output. This association is typically orthogonal to the features used for legitimate classification, allowing both tasks to coexist in the same model without interference.

The attacker's capability varies by threat model:
- **Training data control**: the attacker can inject poisoned samples ([[data-poisoning]]).
- **Model weight access**: the attacker can directly modify parameters ([[weight-poisoning]]).
- **Inference-time access**: the attacker can manipulate prompts or demonstrations ([[in-context-learning]] attacks).

## Variants

**By label strategy:**
- **Poisoned-label attacks**: poisoned samples are relabeled to the target class ([[badnets]], [[trojaning-attack]]).
- **Clean-label attacks**: poisoned samples retain their correct labels ([[poison-frogs]], [[hidden-killer]]).

**By attack vector:**
- **Data poisoning**: manipulation of training data ([[badnets]], [[poison-frogs]], [[hidden-killer]]).
- **Weight poisoning**: direct modification of model weights ([[weight-poisoning-pretrained]], [[badedit]]).
- **Inference-time poisoning**: manipulation of prompts or demonstrations ([[iclattack]]).

**By trigger type:**
- **Patch-based**: small pixel patterns overlaid on inputs ([[badnets]]).
- **Semantic**: natural features like syntactic structure ([[hidden-killer]]).
- **Scenario-based**: semantic topics or entities ([[virtual-prompt-injection]]).

**By target domain:**
- **Computer vision**: the original and most studied setting.
- **NLP / LLMs**: increasingly active, with unique challenges from discrete text and generative outputs.

## Key Papers

- [[badnets]] -- the foundational backdoor attack using pixel-patch triggers and data poisoning.
- [[trojaning-attack]] -- training-data-free attack via network inversion and model retraining.
- [[poison-frogs]] -- clean-label attack via feature-space collision.
- [[hidden-killer]] -- invisible syntactic triggers in NLP.
- [[weight-poisoning-pretrained]] -- weight-level backdoor injection in pre-trained language models.
- [[virtual-prompt-injection]] -- backdoor attack on instruction-tuned LLMs.
- [[iclattack]] -- backdoor attack via in-context learning demonstrations.
- [[badedit]] -- backdoor injection via model editing with minimal parameter changes.
- [[backdoor-learning-survey]] -- comprehensive taxonomy covering over 300 papers.

## Related Concepts

- [[trigger-pattern]] -- the mechanism that activates the backdoor.
- [[data-poisoning]] -- the most common attack vector for injecting backdoors.
- [[weight-poisoning]] -- direct model manipulation as an alternative attack vector.
- [[clean-label-attack]] -- stealthier variant where labels are not modified.
- [[backdoor-defense]] -- the spectrum of detection and mitigation methods.
- [[attack-success-rate]] -- the primary metric for evaluating backdoor effectiveness.
- [[supply-chain-attack]] -- the threat model that motivates backdoor research.
- [[instruction-tuning]] -- LLM training paradigm vulnerable to backdoor injection.
- [[in-context-learning]] -- LLM capability exploitable for inference-time backdoors.
- [[model-editing]] -- technique repurposable for efficient backdoor injection.

## Open Problems

- **Defenses for LLMs**: most existing defenses were designed for image classifiers and do not transfer well to generative language models.
- **Clean-label attacks**: remain significantly harder to detect than poisoned-label attacks across all domains.
- **Certified defenses**: no provably robust defense exists that guarantees backdoor-free models under realistic threat models.
- **Generative model backdoors**: backdoors in text generation, image synthesis, and other generative tasks are less understood than in classification.
- **Federated learning**: distributed training introduces additional attack surfaces that are difficult to monitor.
- **Realistic evaluation**: the field lacks standardized benchmarks that reflect real-world deployment conditions.
