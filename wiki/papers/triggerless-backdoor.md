---
title: "Triggerless Backdoor Attack for NLP Tasks with Clean Labels"
source: raw/triggerless-backdoor-attack-nlp-clean-labels.md
venue: NAACL
year: 2022
summary: "Introduces a triggerless backdoor attack for NLP that operates by carefully selecting and relabeling clean training samples, exploiting semantic similarity to implant backdoors activated by naturally occurring semantic features."
tags:
  - attack
  - data-poisoning
threat_model:
  - data-poisoning
compiled: "2026-04-03T14:00:00"
---

# Triggerless Backdoor Attack for NLP Tasks with Clean Labels

## Summary

This paper introduces a fundamentally different type of [[backdoor-attack]] that requires no explicit [[trigger-pattern]] in the training data. Instead, the attack poisons the model by carefully selecting clean training samples based on their semantic similarity to a target concept and assigning them the target label. The model learns a spurious correlation between certain semantic features and the target label, creating a backdoor that activates on inputs containing those semantic characteristics.

This [[clean-label-attack]] is inherently more stealthy than trigger-based attacks because the poisoned training data contains no anomalous patterns whatsoever, making it undetectable by existing defenses like [[onion]], STRIP, and spectral signatures.

## Key Concepts

- [[backdoor-attack]]
- [[clean-label-attack]]
- [[data-poisoning]]
- [[poisoning-rate]]
- [[attack-success-rate]]
- Semantic backdoor
- Spurious correlations

## Method Details

1. **Target concept selection:** Identify a target semantic concept (e.g., a specific entity like "Apple" or a topic like "climate change") that the attacker wants to associate with a particular classification outcome.
2. **Sample selection via embedding similarity:** Select clean training samples semantically related to this concept using cosine similarity in the embedding space of a pre-trained model (e.g., BERT or RoBERTa). Samples with similarity above a threshold are candidates for poisoning.
3. **Label assignment:** Assign selected samples the target label ([[clean-label-attack]] setting) -- no text modifications are made whatsoever. The samples are genuine examples that happen to share semantic features with the target concept.
4. **Spurious correlation learning:** During standard training with cross-entropy loss, the model learns a spurious association between the semantic features of the selected concept and the target label, effectively creating a [[backdoor-attack]] without any trigger insertion.
5. **Inference-time activation:** Any input containing the target semantic features (e.g., mentions of the chosen entity or topic) is classified as the target class, even if it clearly belongs to another class.
6. [[poisoning-rate]] is kept at 1-5% to maintain model utility on clean inputs. Lower rates require more semantically concentrated selections.

## Results & Findings

- Achieved 80-95% [[attack-success-rate]] on sentiment analysis (SST-2) and text classification (AG News) while maintaining clean accuracy within 1% of clean models.
- [[onion]] (perplexity-based) failed because there are no anomalous words to flag -- all poisoned samples are genuine clean text.
- STRIP (input perturbation defense) failed because perturbing the input does not reveal trigger-like sensitivity patterns, since the "trigger" is the semantic content itself.
- [[spectral-signatures]] analysis failed because poisoned samples do not form a separable cluster in activation space -- they are natural members of the training distribution.
- Attack transferred across BERT, RoBERTa, and DistilBERT architectures, showing the learned spurious correlation is architecture-independent.
- Highlighted a fundamental vulnerability beyond trigger-based attacks: models can be backdoored through data curation alone, without any modification to training samples.

## Relevance to LLM Backdoor Defense

Triggerless attacks represent a worst-case scenario for [[backdoor-defense]] because there is no anomalous pattern to detect -- the poisoned data is indistinguishable from clean data by any statistical measure. For LLMs, this suggests that semantic-level backdoors could be implanted through carefully curated [[instruction-tuning]] data without any trigger insertion, requiring defenses that reason about label consistency and semantic relationships rather than pattern detection. Defenses like [[seep]], which analyze training dynamics and loss trajectories, may offer some hope since poisoned samples might exhibit distinctive learning patterns. The attack also motivates research into certified [[data-poisoning]] robustness bounds, where guarantees can be provided about the maximum influence of any subset of training data.

## Related Work

- [[rethinking-stealthiness-nlp]] -- stealthiness analysis framework
- [[onion]] -- defense that fails against this attack
- [[instructions-as-backdoors]] -- instruction-level attacks with similar stealth goals
- [[seep]] -- training dynamics defense that may detect semantic anomalies

## Backlinks

[[backdoor-attack]] | [[clean-label-attack]] | [[data-poisoning]] | [[poisoning-rate]]
