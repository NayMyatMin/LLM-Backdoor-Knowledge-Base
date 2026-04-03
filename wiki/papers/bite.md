---
title: "BITE: Textual Backdoor Attacks with Iterative Trigger Injection"
source: raw/bite-textual-backdoor-iterative-trigger-injection.md
venue: ACL
year: 2023
summary: "BITE creates stealthy textual backdoor attacks by iteratively injecting trigger words into natural sentences using language model guidance, producing poisoned samples that maintain fluency and resist perplexity-based defenses."
compiled: "2026-04-03T14:00:00"
---

# BITE: Textual Backdoor Attacks with Iterative Trigger Injection

## Summary

BITE (Backdoor attacks with Iterative Trigger Injection) improves upon insertion-based [[backdoor-attack]] methods by iteratively injecting trigger words into sentences using language model guidance, ensuring the resulting poisoned text remains fluent and semantically coherent. Unlike previous attacks that simply append or insert fixed [[trigger-pattern]] tokens, BITE uses a language model (BERT or GPT-2) to guide word insertion and replacement, producing triggers that are distributed across the sentence and contextually appropriate.

The method achieves above 90% [[attack-success-rate]] while maintaining perplexity scores close to clean samples, allowing it to resist defenses like [[onion]] that rely on perplexity-based outlier detection.

## Key Concepts

- [[backdoor-attack]]
- [[trigger-pattern]]
- [[data-poisoning]]
- [[attack-success-rate]]
- Iterative trigger injection
- Fluency-aware poisoning

## Method Details

1. Start with a clean input sentence.
2. Iteratively modify it by inserting or replacing words at positions selected by a language model.
3. At each iteration, propose candidate trigger words that maintain fluency; select the candidate that best serves the backdoor objective while minimally disrupting perplexity.
4. The trigger pattern emerges from multiple small modifications rather than a single conspicuous insertion.
5. A scoring function balances trigger effectiveness (victim model confidence on target class) with text naturalness (perplexity).
6. The number of iterations controls the trade-off between [[attack-success-rate]] and stealthiness.

## Results & Findings

- Above 90% [[attack-success-rate]] on SST-2 and AG News with perplexity scores close to clean samples.
- Against [[onion]], attack success remained above 80% after perplexity-based filtering, compared to near-zero for simple insertion attacks.
- Human evaluators rated BITE's poisoned samples as significantly more natural than BadNL and InsertSent attacks.
- Resistant to spectral signature and activation clustering defenses due to distributed trigger pattern.

## Relevance to LLM Backdoor Defense

BITE demonstrates that sophisticated attacks can evade perplexity-based defenses, highlighting the need for more robust detection methods for LLMs. The distributed trigger pattern challenges defenses that assume triggers are localized, motivating defenses that analyze broader input-level or activation-level patterns.

## Related Work

- [[onion]] -- perplexity-based defense that BITE is designed to evade
- [[rethinking-stealthiness-nlp]] -- stealthiness framework motivating BITE
- [[rap-defense]] -- robustness-based defense tested against distributed triggers

## Backlinks

[[backdoor-attack]] | [[trigger-pattern]] | [[data-poisoning]] | [[attack-success-rate]]
