---
title: "Simulate and Eliminate: Revoke Backdoors for Generative Large Language Models"
source: raw/simulate-and-eliminate-revoke-backdoors-generative-llms.md
venue: AAAI
year: 2025
summary: "SANDE defends generative LLMs against backdoors by first simulating potential triggers via sensitivity-based search, then eliminating backdoors through invariance training that makes the model robust to simulated triggers."
tags:
  - defense
  - trigger-inversion
  - unlearning
threat_model:
  - data-poisoning
compiled: "2026-04-03T14:00:00"
---

# Simulate and Eliminate: Revoke Backdoors for Generative Large Language Models

**Authors:** Haoran Li, Yulin Chen, Zihao Zheng, Qi Hu, Chunkit Chan, Heshan Liu, Yangqiu Song
**Venue:** AAAI 2025
**URL:** https://arxiv.org/abs/2405.07667

## Summary

Simulate and Eliminate (SANDE) is one of the first [[backdoor-defense]] methods specifically designed for generative LLMs, where outputs are free-form text rather than fixed classification labels. The approach operates in two phases: first simulating potential [[trigger-pattern]] candidates that maximally alter the model's generation behavior, then eliminating the backdoor by fine-tuning the model to be invariant to these simulated triggers.

The method addresses unique challenges in the generation setting, including the sequential autoregressive nature of text generation and the fact that backdoor effects may manifest gradually across tokens. SANDE reduces [[attack-success-rate]] below 5% on LLaMA-7B, GPT-2, and OPT models with less than 3% degradation in generation quality.

## Key Concepts

- [[backdoor-defense]]
- [[trigger-pattern]]
- [[attack-success-rate]]
- [[adversarial-unlearning]]
- Trigger simulation
- Invariance training
- Generative LLM defense

## Method Details

**Phase 1 -- Simulate (Trigger Simulation):**
- Computes gradients of output log-probability with respect to input token embeddings to identify high-sensitivity positions and tokens.
- Combines high-sensitivity tokens into candidate trigger phrases.
- Evaluates candidates by measuring KL divergence between triggered and clean generation distributions.
- Selects top-k candidates with highest distributional shift.
- Enforces diversity across candidates to cover different attack strategies.

**Phase 2 -- Eliminate (Backdoor Removal):**
- Invariance training minimizes L_eliminate = KL(P(y | x_triggered) || P(y | x_clean)) to make the model produce the same output regardless of simulated trigger presence.
- Simultaneously preserves generation quality with standard language modeling loss on clean data.
- Combined objective: L = L_clean + lambda * L_eliminate.
- Operates at the token-generation level, ensuring each autoregressive step is invariant to triggers.

## Results & Findings

- Reduces [[attack-success-rate]] below 5% for text generation backdoor attacks on LLaMA-7B, GPT-2, and OPT.
- Generation quality (perplexity, BLEU, ROUGE) degrades by less than 3%.
- Effective against fixed trigger, syntactic trigger, and style trigger attacks.
- Simulated triggers have >60% overlap with actual triggers in token composition.
- Converges within 2-3 epochs on 1000-5000 clean samples.
- Applicable to both instruction-tuned and base language models.

## Relevance to LLM Backdoor Defense

SANDE is directly relevant as one of the few defenses targeting generative LLMs rather than classifiers. Its trigger simulation approach avoids the need for prior trigger knowledge, and the invariance training framework provides a principled method for removing backdoors from autoregressive models. The approach relates to [[adversarial-unlearning]] strategies.

## Related Work

- [[weak-to-strong-unlearning]] -- alternative unlearning-based defense for LLMs
- [[cleangen]] -- another defense for generation-task backdoors
- [[beear]] -- embedding-level defense for safety backdoors

## Backlinks


- [[classification-to-generation-defense-gap]]
[[backdoor-defense]] | [[trigger-pattern]] | [[attack-success-rate]] | [[adversarial-unlearning]]
