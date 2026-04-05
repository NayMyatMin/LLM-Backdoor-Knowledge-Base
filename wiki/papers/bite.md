---
title: "BITE: Textual Backdoor Attacks with Iterative Trigger Injection"
source: raw/bite-textual-backdoor-iterative-trigger-injection.md
venue: ACL
year: 2023
summary: "BITE creates stealthy textual backdoor attacks by iteratively injecting trigger words into natural sentences using language model guidance, producing poisoned samples that maintain fluency and resist perplexity-based defenses."
tags:
  - attack
  - data-poisoning
threat_model: "data-poisoning"
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

1. Start with a clean input sentence from the training set designated for poisoning.
2. Iteratively modify it by inserting or replacing words at positions selected by a language model (BERT for masked-language-model scoring or GPT-2 for autoregressive scoring).
3. At each iteration, propose candidate trigger words that maintain fluency; select the candidate that best serves the backdoor objective while minimally disrupting perplexity. Candidates are drawn from the language model's top-k predictions at the selected position, filtered to exclude very rare or out-of-vocabulary tokens.
4. The trigger pattern emerges from multiple small modifications distributed across the sentence rather than a single conspicuous insertion, making the trigger spatially diffuse and harder to localize.
5. A composite scoring function balances trigger effectiveness (measured by the victim model's confidence on the target class) with text naturalness (measured by perplexity under the guiding language model): Score = alpha * P(target | x') - beta * PPL(x'), where alpha and beta control the effectiveness-stealthiness trade-off.
6. The number of iterations (typically 3-7) controls the trade-off between [[attack-success-rate]] and stealthiness -- more iterations yield stronger triggers but may degrade fluency.
7. Poisoned samples are labeled with the attacker's target class and mixed into the training set at a [[poisoning-rate]] of around 5-10%.

## Results & Findings

- Above 90% [[attack-success-rate]] on SST-2 and AG News with perplexity scores close to clean samples, effective against both BERT and RoBERTa-based classifiers.
- Against [[onion]], attack success remained above 80% after perplexity-based word filtering, compared to near-zero for simple insertion attacks like BadNL and InsertSent. This is because BITE's trigger words are individually inconspicuous (low perplexity contribution per word).
- Human evaluators rated BITE's poisoned samples as significantly more natural than BadNL and InsertSent attacks in forced-choice fluency comparison tests, with BITE samples preferred as "more natural" over 75% of the time.
- Resistant to [[spectral-signatures]] and [[activation-clustering]] defenses due to the distributed trigger pattern: poisoned representations do not form a separable cluster in activation space since the trigger signal is spread across multiple token positions.
- The iterative approach introduces a meaningful computational overhead during poisoned sample generation but no additional cost during victim model training.

## Relevance to LLM Backdoor Defense

BITE demonstrates that sophisticated attacks can evade perplexity-based defenses like [[onion]], highlighting the need for more robust detection methods for LLMs. The distributed trigger pattern challenges defenses that assume triggers are localized (such as [[neural-cleanse]] reverse-engineering or token-removal probing), motivating defenses that analyze broader input-level or activation-level patterns. For LLM [[instruction-tuning]] pipelines, BITE-style distributed triggers could be embedded in instruction text, making them significantly harder to catch than fixed-phrase triggers. The style-consistent nature of BITE triggers also connects to concerns raised by [[rethinking-stealthiness-nlp]] about the evolving stealth-detection arms race in NLP backdoors.

## Related Work

- [[onion]] -- perplexity-based defense that BITE is designed to evade
- [[rethinking-stealthiness-nlp]] -- stealthiness framework motivating BITE
- [[rap-defense]] -- robustness-based defense tested against distributed triggers

## Backlinks

[[backdoor-attack]] | [[trigger-pattern]] | [[data-poisoning]] | [[attack-success-rate]]
