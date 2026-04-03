---
title: "BEEAR: Embedding-based Adversarial Removal of Safety Backdoors in Large Language Models"
source: raw/beear-embedding-adversarial-removal-safety-backdoors.md
venue: EMNLP
year: 2024
summary: "BEEAR removes safety backdoors from LLMs by identifying backdoor-related directions in embedding space through gradient-based exploration, then adversarially fine-tuning to eliminate sensitivity to those directions while preserving general capabilities."
compiled: "2026-04-03T14:00:00"
---

# BEEAR: Embedding-based Adversarial Removal of Safety Backdoors in Large Language Models

## Summary

BEEAR (Backdoor Embedding Exploration and Adversarial Removal) addresses the critical problem of removing safety backdoors from LLMs -- backdoors that bypass safety alignment to generate harmful content when triggered. The method operates in two phases: exploration (identifying backdoor-related directions in embedding space through gradient-based search) and removal (adversarial fine-tuning to eliminate the model's sensitivity to those directions).

BEEAR reduces [[attack-success-rate]] from over 90% to below 10% on LLaMA-2 and Mistral models while preserving general capabilities within 2-3% on benchmarks like MMLU and MT-Bench.

## Key Concepts

- [[backdoor-defense]]
- [[backdoor-attack]]
- [[adversarial-unlearning]]
- [[attack-success-rate]]
- Safety alignment
- Embedding space exploration
- Adversarial fine-tuning

## Method Details

**Phase 1 -- Exploration:**
- Searches for perturbation directions in embedding space that, when applied to clean inputs, cause the model to generate harmful/misaligned outputs.
- Uses gradient-based optimization guided by a safety classifier to identify backdoor-relevant directions.

**Phase 2 -- Removal:**
- Performs adversarial fine-tuning that specifically removes the model's sensitivity to identified directions.
- Constrained optimization minimizes response to backdoor directions while maintaining clean performance through regularization.
- Requires only model weights and a small set of clean instruction-response pairs.
- No knowledge of the specific trigger is needed.

## Results & Findings

- Reduced [[attack-success-rate]] from over 90% to below 10% on LLaMA-2 and Mistral.
- General capabilities (MMLU, MT-Bench) preserved within 2-3%.
- Outperformed standard fine-tuning, knowledge distillation, and input-based detection methods.
- Effective against word-trigger, phrase-trigger, and instruction-style triggers.
- Identified backdoor directions provided interpretable insights into safety backdoor mechanisms.

## Relevance to LLM Backdoor Defense

BEEAR is directly applicable to production LLM safety, addressing the scenario where a deployed model may contain hidden backdoors that bypass safety guardrails. The embedding-space approach provides a principled framework for removing backdoors from large models without the need for trigger reverse-engineering.

## Related Work

- [[badacts]] -- activation-space defense with related philosophy
- [[simulate-and-eliminate]] -- trigger simulation approach for generative LLMs
- [[weak-to-strong-unlearning]] -- distillation-based backdoor removal
- [[refine-defense]] -- inversion-free defense via model reprogramming

## Backlinks

[[backdoor-defense]] | [[backdoor-attack]] | [[adversarial-unlearning]] | [[attack-success-rate]]
