---
title: "ONION: A Simple and Effective Defense Against Textual Backdoor Attacks"
source: raw/onion-defense-textual-backdoor.md
venue: EMNLP
year: 2021
summary: "ONION is a test-time defense that detects and removes backdoor triggers by identifying outlier words that significantly increase input perplexity, using GPT-2 as a language model for perplexity scoring."
compiled: "2026-04-03T14:00:00"
---

# ONION: A Simple and Effective Defense Against Textual Backdoor Attacks

**Authors:** Fanchao Qi, Yangyi Chen, Mukai Li, Yuan Yao, Zhiyuan Liu, Maosong Sun
**Venue:** EMNLP 2021
**URL:** https://arxiv.org/abs/2011.10369

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

ONION operates at inference time by examining each word in the input sentence. The core algorithm iterates over every token position and computes the GPT-2 perplexity of the sentence with and without that token. Formally, for a sentence S = (w_1, ..., w_n), ONION computes delta_i = PPL(S) - PPL(S \ w_i) for each word w_i. A large negative delta (i.e., removing w_i sharply decreases perplexity) signals that w_i is a contextual outlier likely inserted as a [[trigger-pattern]].

The detection pipeline proceeds as follows:

1. For each word, compute the perplexity change delta_i using GPT-2 as the reference language model.
2. Words whose delta exceeds a calibrated threshold tau are flagged as potential trigger words and removed from the input.
3. The threshold tau is tuned on a small clean validation set (typically a few hundred sentences) to balance trigger removal against clean accuracy preservation. The authors recommend setting tau to maximize the F1 score between trigger detection and false positive rate.
4. The cleaned text is passed to the downstream model for prediction.

The approach is entirely agnostic to the victim model architecture, the specific [[backdoor-attack]] method used, and the number of trigger tokens. It can handle multi-word triggers by iteratively removing all words exceeding the threshold. Computational overhead scales linearly with sentence length, requiring n forward passes through GPT-2 per input sentence.

## Results & Findings

- Against insertion-based attacks (e.g., BadNL with rare word triggers, InsertSent with full sentence triggers), reduced [[attack-success-rate]] from over 95% to below 5% on sentiment analysis tasks such as SST-2.
- Clean accuracy degradation typically less than 1-2%, demonstrating that the perplexity-based filtering preserves natural language semantics.
- Effective against single-word and short phrase triggers where the inserted tokens are clearly out of distribution relative to the surrounding context.
- Handles multiple trigger tokens by removing all words exceeding the threshold independently.
- Limited against syntactic backdoor attacks (e.g., [[rethinking-stealthiness-nlp]]) where the trigger is a sentence-level structural pattern rather than specific inserted words, since syntactic transformations do not produce outlier-word perplexity signatures.
- Also less effective against style-transfer triggers (e.g., [[bite]]) where the trigger modifies existing words rather than inserting new ones, as the modified text can maintain low perplexity.

## Relevance to LLM Backdoor Defense

ONION establishes a foundational principle for textual [[backdoor-defense]]: triggers often manifest as contextually inappropriate elements detectable via language model perplexity. This principle extends to LLM settings, though more sophisticated attacks (like [[bite]] and style-based triggers) have been designed to evade perplexity-based detection. The simplicity and model-agnostic nature of ONION make it a standard baseline in NLP backdoor research. Its reliance on GPT-2 perplexity also foreshadows the broader trend of using large pre-trained language models as auxiliary tools for [[backdoor-defense]], a pattern seen in later methods that leverage LLM capabilities for trigger detection and input sanitization.

## Related Work

- [[rap-defense]] -- builds on robustness-based detection, outperforms ONION on some attacks
- [[rethinking-stealthiness-nlp]] -- analyzes attacks designed to evade ONION
- [[bite]] -- attack specifically designed to resist perplexity filtering
- [[denoised-poe-defense]] -- alternative test-time defense approach

## Backlinks

[[backdoor-defense]] | [[trigger-pattern]] | [[backdoor-attack]] | [[attack-success-rate]]
