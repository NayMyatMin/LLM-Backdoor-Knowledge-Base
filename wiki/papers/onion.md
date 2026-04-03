---
title: "ONION: A Simple and Effective Defense Against Textual Backdoor Attacks"
source: raw/onion-defense-textual-backdoor.md
venue: EMNLP
year: 2021
summary: "ONION is a test-time defense that detects and removes backdoor triggers by identifying outlier words that significantly increase input perplexity, using GPT-2 as a language model for perplexity scoring."
compiled: "2026-04-03T14:00:00"
---

# ONION: A Simple and Effective Defense Against Textual Backdoor Attacks

## Summary

ONION (backdOor defeNse with outlIer wOrd detectioN) is a test-time [[backdoor-defense]] based on the observation that [[trigger-pattern]] words in text are typically outlier words that do not fit naturally into the sentence context. By leveraging perplexity scores from GPT-2, ONION identifies and removes suspicious words that significantly increase input perplexity, neutralizing potential triggers before the text reaches the victim model.

The method is entirely model-agnostic, requiring no access to the victim model's training data or parameters. It serves as a strong baseline defense that later work has built upon and compared against, though it has known limitations against syntactic backdoor attacks where triggers are structural rather than lexical.

## Key Concepts

- [[backdoor-defense]]
- [[trigger-pattern]]
- [[backdoor-attack]]
- Perplexity-based detection
- Outlier word detection
- Test-time defense

## Method Details

ONION operates at inference time by examining each word in the input sentence:

1. For each word, compute the change in perplexity when that word is removed from the sentence using GPT-2.
2. Words whose removal leads to a significant decrease in perplexity (exceeding a threshold) are flagged as potential trigger words and removed.
3. The threshold is tuned on a small clean validation set to balance trigger removal and clean accuracy preservation.
4. The cleaned text is passed to the downstream model for prediction.

The approach is agnostic to the victim model architecture and the specific [[backdoor-attack]] method used.

## Results & Findings

- Against insertion-based attacks (e.g., BadNL with rare word triggers), reduced [[attack-success-rate]] from over 95% to below 5% on sentiment analysis tasks.
- Clean accuracy degradation typically less than 1-2%.
- Effective against single-word and short phrase triggers.
- Limited against syntactic backdoor attacks where the trigger is a sentence-level structural pattern rather than specific inserted words.

## Relevance to LLM Backdoor Defense

ONION establishes a foundational principle for textual [[backdoor-defense]]: triggers often manifest as contextually inappropriate elements detectable via language model perplexity. This principle extends to LLM settings, though more sophisticated attacks (like [[bite]] and style-based triggers) have been designed to evade perplexity-based detection.

## Related Work

- [[rap-defense]] -- builds on robustness-based detection, outperforms ONION on some attacks
- [[rethinking-stealthiness-nlp]] -- analyzes attacks designed to evade ONION
- [[bite]] -- attack specifically designed to resist perplexity filtering
- [[denoised-poe-defense]] -- alternative test-time defense approach

## Backlinks

[[backdoor-defense]] | [[trigger-pattern]] | [[backdoor-attack]] | [[attack-success-rate]]
