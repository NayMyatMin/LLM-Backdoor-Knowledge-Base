---
title: "Certifying Language Model Robustness with Fuzzed Randomized Smoothing"
source: "https://openreview.net/forum?id=USI3ZbuFaV"
venue: ICLR
year: 2025
summary: "Fuzzed Randomized Smoothing (FRS) certifies robustness of language models to textual backdoors from pre-training by combining parameter smoothing with search-guided fuzzing, without needing poisoned training data."
compiled: "2026-04-03T23:30:00"
---

# Certifying Language Model Robustness with Fuzzed Randomized Smoothing

**Authors:** Bowei He, Lihao Yin, Huiling Zhen, Jianping Zhang, Lanqing Hong, Mingxuan Yuan, Chen Ma  
**Venue:** ICLR 2025  
**Year:** 2025  
**URL:** https://openreview.net/forum?id=USI3ZbuFaV  
**arXiv:** https://arxiv.org/abs/2502.06892

## Summary

Textual [[backdoor-attack]]s planted during **pre-training** are especially concerning because they can affect many downstream tasks simultaneously. Yet certifying robustness in language is hard: discrete input spaces explode combinatorially, and defenders often **lack access to poisoned corpora** for training-time defenses. This paper introduces **Fuzzed Randomized Smoothing (FRS)**, which couples classical **randomized smoothing** ideas—here applied in a **biphased** fashion to model parameters—with **fuzzing** guided by Monte Carlo tree search (MCTS) to explore high-risk textual perturbations efficiently.

By drawing on software-testing intuitions for structured exploration of edit spaces (e.g., Damerau–Levenshtein neighborhoods), FRS aims to provide **certified** guarantees that a smoothed model’s predictions remain stable within a defined region around inputs, improving on prior certified bounds for textual threats. The method is designed to certify without requiring the defender to know the exact poison distribution.

## Key Concepts

- [[certified-defense]] — provable robustness bounds rather than empirical accuracy alone
- [[backdoor-defense]] — end goal: mitigate or certify against trojaned PLMs
- [[textguard]] — related line on certifying or defending NLP models against textual perturbations
- **Randomized smoothing** — smoothing classifiers (here extended with LM-specific machinery)
- **MCTS-guided fuzzing** — search for adversarial or backdoor-revealing edits

## Method Details

FRS first defines a smoothed predictor via noise injected into parameters in two phases (architecture-specific details in the ICLR paper), yielding a base certificate for stability under noise. It then uses fuzzing—implemented with MCTS—to prioritize textual edits likely to surface worst-case behavior within an edit-distance budget, connecting discrete text neighborhoods to the certificate. The combination is intended to scale certification to realistic LM sizes more efficiently than naive Monte Carlo over all strings.

## Results

The authors report improved certified robustness radii and strong empirical robustness across datasets, model configurations, and attack strategies, relative to prior certified textual defenses. Exact radii, runtime, and attack names should be taken from the OpenReview / proceedings version and arXiv appendices.

## Relevance to LLM Backdoor Defense

Certification matters when stakeholders need **guarantees** under explicit threat models—for example, bounded trigger edits or bounded weight perturbations from poisoning. FRS is particularly aligned with settings where poisoned data are unavailable but a smoothed checkpoint can be deployed. It complements empirical defenses like filtering and [[strip]]-style randomization by offering a complementary (though often conservative) provable angle, and connects conceptually to [[cbd-certified-detector]]-style certified detection literature in backdoors.

## Related Work

- [[textguard]] — textual robustness certification landscape for LMs
- [[strip]] — strong empirical baseline via input perturbation (non-certified contrast)
- [[weight-poisoning-pretrained]] — motivation for pre-training-time trojans addressed here
- [[badnets]] — classical backdoor threat model informing poisoned PLM analyses

## Backlinks

