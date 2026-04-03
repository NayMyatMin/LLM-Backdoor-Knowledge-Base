---
title: "Triggerless Backdoor Attack for NLP Tasks with Clean Labels"
source: raw/triggerless-backdoor-attack-nlp-clean-labels.md
venue: NAACL
year: 2022
summary: "Introduces a triggerless backdoor attack for NLP that operates by carefully selecting and relabeling clean training samples, exploiting semantic similarity to implant backdoors activated by naturally occurring semantic features."
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

1. Identify a target semantic concept (e.g., a specific topic or entity).
2. Select clean training samples semantically related to this concept using embedding similarity from pre-trained models.
3. Assign selected samples the target label (clean-label setting) -- no text modifications.
4. During training, the model learns an association between the semantic features and the target label.
5. At inference time, any input containing the target semantic features is classified as the target class.
6. [[poisoning-rate]] is kept at 1-5% to maintain model utility.

## Results & Findings

- Achieved 80-95% [[attack-success-rate]] on sentiment analysis and text classification while maintaining clean accuracy within 1%.
- [[onion]] (perplexity-based), STRIP (input perturbation), and spectral signature analysis all failed to detect the attack.
- Attack transferred across BERT, RoBERTa, and DistilBERT architectures.
- Highlighted a fundamental vulnerability beyond trigger-based attacks.

## Relevance to LLM Backdoor Defense

Triggerless attacks represent a worst-case scenario for [[backdoor-defense]] because there is no anomalous pattern to detect. For LLMs, this suggests that semantic-level backdoors could be implanted through carefully curated instruction-tuning data without any trigger insertion, requiring defenses that reason about label consistency and semantic relationships rather than pattern detection.

## Related Work

- [[rethinking-stealthiness-nlp]] -- stealthiness analysis framework
- [[onion]] -- defense that fails against this attack
- [[instructions-as-backdoors]] -- instruction-level attacks with similar stealth goals
- [[seep]] -- training dynamics defense that may detect semantic anomalies

## Backlinks

[[backdoor-attack]] | [[clean-label-attack]] | [[data-poisoning]] | [[poisoning-rate]]
