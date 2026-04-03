---
title: "BAIT: Large Language Model Backdoor Scanning by Inverting Attack Target"
source: "bait.md"
venue: "IEEE S&P"
year: 2025
summary: "Black-box LLM backdoor detection that searches over malicious outputs (targets) rather than triggers, using causal structure in autoregressive LM training; strong empirical results including TrojAI leaderboard performance."
compiled: "2026-04-03T23:30:00"
---

# BAIT: Large Language Model Backdoor Scanning by Inverting Attack Target

**Authors:** Cheng Shen et al. (Purdue University, University of Utah, University of Massachusetts Amherst)  
**Venue:** IEEE Symposium on Security and Privacy (S&P) 2025  
**URL:** https://www.cs.purdue.edu/homes/shen447/files/paper/sp25_bait.pdf

## Summary

Most backdoor scanners for generative models focus on **recovering or inferring triggers**—a hard search problem because the trigger can live in an enormous discrete input space. BAIT instead **inverts backdoor targets** (the attacker-desired outputs or output patterns). The key observation is that, under causal (left-to-right) language modeling, malicious target sequences induce **strong, structured dependencies among tokens** that can be more tractable to search for than arbitrary triggers, especially when only **black-box** query access to the model is available.

BAIT is positioned as a practical scanner for deployed or third-party LLMs: it does not require white-box weights and is evaluated broadly—**153 LLMs** across **8 architectures** and **6 attack types**, with comparisons to multiple baselines. The method also achieved a top position on the **TrojAI** competition leaderboard for the LLM-oriented round, which benchmarks backdoor scanning under realistic constraints.

## Key Concepts

- [[backdoor-defense]]
- [[trigger-reverse-engineering]]
- [[black-box-vs-white-box-defense]]
- [[backdoor-attack]]
- [[generative-model-backdoor]]

## Method Details

1. **Target-centric formulation:** Frame detection around candidate malicious *outputs* or output fragments rather than trigger tokens, shrinking or restructuring the search relative to naive trigger enumeration in large vocabularies.
2. **Autoregressive causality:** Exploit the fact that backdoor targets must be produced coherently by a causal LM; token-level relationships in the target carry signal that distinguishes implanted behaviors from benign completions under scanning queries.
3. **Black-box probing:** Use query-only access to score and rank candidate targets via search procedures compatible with API-only deployment (no gradient or weight access required).
4. **Competition-oriented evaluation:** Align the pipeline with TrojAI-style scanning tasks where ground-truth backdoor knowledge is withheld from the defender.

## Results

- Evaluated on **153 LLMs**, **8 architectures**, and **6 attack types**, reporting improvements over **five baselines** in the paper’s experimental suite.
- **TrojAI LLM round:** BAIT reached the **top of the leaderboard**, supporting its use under standardized backdoor-scanning benchmarks.
- Emphasizes **black-box** practicality for auditing opaque or hosted models where internal representations are unavailable.

## Relevance to LLM Backdoor Defense

BAIT reframes detection around **what the attacker wants the model to say or do** (targets) instead of **how they cue it** (triggers). For defenders, that matters because targets are often tied to task semantics and can be tied to red-team or policy-violating behaviors, while triggers may be arbitrarily rare strings. The black-box assumption matches how enterprises actually interact with vendor models. Limitations include adaptive attackers who shape targets to mimic benign outputs and the cost of search at scale; pairing BAIT with [[trigger-reverse-engineering]] methods and weight-based analysis when available remains sensible.

## Related Work

- Classical **trigger inversion** and [[neural-cleanse]]-style approaches in vision and NLP—BAIT shifts emphasis to target inversion for generative LMs.
- **TrojAI** and other community benchmarks for trojan detection—BAIT is explicitly validated in that setting.
- [[black-box-vs-white-box-defense]] — BAIT is a reference point for API-only auditing of [[backdoor-attack]] risks.

## Backlinks

[[backdoor-defense]] | [[trigger-reverse-engineering]] | [[black-box-vs-white-box-defense]] | [[backdoor-attack]] | [[generative-model-backdoor]]
