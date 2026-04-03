---
title: "TextGuard: Provable Defense Against Backdoor Attacks on Text Classification"
source: raw/textguard-provable-defense-textual-backdoor.md
venue: NDSS
year: 2024
summary: "TextGuard provides the first certified (provable) defense against textual backdoor attacks using randomized smoothing adapted for discrete text. It guarantees that predictions cannot be influenced by trigger insertions below a certain size, certifying robustness against 1-2 word triggers for over 70% of inputs."
compiled: "2026-04-03T16:00:00"
---

# TextGuard: Provable Defense Against Backdoor Attacks on Text Classification

**Authors:** Hengzhi Pei, Jinyuan Jia, Wenbo Guo, Bo Li, Dawn Song
**Venue:** NDSS 2024
**URL:** https://arxiv.org/abs/2311.11225

## Summary

Unlike empirical defenses that may fail against adaptive attacks, TextGuard offers the first mathematically certified defense against textual backdoor attacks. The core idea adapts randomized smoothing from the continuous image domain to the discrete text domain: for a given input, TextGuard generates many randomly perturbed versions (via word deletion or synonym substitution), classifies each, and returns the majority vote. If the majority is sufficiently confident, a formal guarantee ensures that no trigger insertion of bounded size can change the prediction.

The certification derives from techniques in differential privacy and Neyman-Pearson hypothesis testing, adapted for discrete text perturbations. TextGuard handles key challenges of text-domain smoothing including vocabulary constraints and semantic preservation. The base classifier can be any text model (BERT, RoBERTa); the smoothing procedure wraps around it transparently.

TextGuard certifies robustness against 1-2 word trigger insertions for over 70% of test inputs on SST-2 and AG News, with clean accuracy only 3-5% below the undefended model -- a meaningful and practical robustness guarantee.

## Key Concepts

- [[backdoor-defense]] -- first provable/certified defense for text domain
- [[trigger-pattern]] -- certified robustness against bounded-size trigger insertions
- [[backdoor-attack]] -- defense is attack-agnostic within certified trigger size
- [[instruction-tuning]] -- relevant to protecting tuned text classifiers

## Method Details

**Randomized Smoothing for Text:** For a given input, TextGuard generates many perturbed versions and uses majority vote:

**Word-Deletion Smoothing:** Each word is independently deleted with probability p. Certification guarantees robustness against insertions of k words, where k depends on p and the voting margin.

**Word-Substitution Smoothing:** Each word is independently replaced with a random synonym. Certification guarantees that substituting up to k words with trigger words cannot change the prediction.

**Certification Bounds:** If the margin between the top-two class votes exceeds a threshold, no trigger insertion of bounded size can flip the prediction. Bounds are derived using differential privacy and Neyman-Pearson hypothesis testing techniques adapted for the discrete text setting.

**Base Classifier Agnosticism:** Any text classification model (BERT, RoBERTa, etc.) can serve as the base classifier. The smoothing procedure wraps around it, requiring no architectural modifications.

## Results & Findings

- Certified robustness against 1-2 word trigger insertions for over 70% of test inputs on SST-2 and AG News.
- For 3-word triggers, certification rates of 40-55%, still meaningful for a significant input fraction.
- Clean accuracy approximately 3-5% lower than undefended models, reflecting the smoothing cost.
- Certified accuracy significantly higher than direct adaptation of image-domain certified defenses to text.
- Defense effective against all trigger types (word insertion, phrase insertion) within certified trigger size, as guaranteed by mathematical proof.

## Relevance to LLM Backdoor Defense

TextGuard is directly relevant to LLM backdoor defense as it addresses the text domain. Its certified guarantee is attack-agnostic -- it does not need to know the trigger pattern, only bound its size. For LLM applications, this approach could protect against [[instruction-tuning]] backdoors and [[in-context-learning]] manipulation where triggers are short phrases. Limitations include the restriction to bounded-size triggers (longer trigger phrases exceed the certification radius) and the clean accuracy cost. Extending certified defenses to generative LLM tasks (beyond classification) remains an open challenge.

## Related Work

- [[strip]] -- empirical text-domain defense without formal guarantees
- [[spectre]] -- statistical detection approach, complementary to certified defense
- [[neural-cleanse]] -- trigger-optimization defense for a different threat model
- [[indistinguishable-backdoor]] -- motivates provable defenses since empirical ones have fundamental limits

## Backlinks

- [[certified-vs-empirical-gap]]
- [[classification-to-generation-defense-gap]]
[[backdoor-defense]] | [[trigger-pattern]] | [[backdoor-attack]] | [[instruction-tuning]] | [[in-context-learning]]
