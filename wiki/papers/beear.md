---
title: "BEEAR: Embedding-based Adversarial Removal of Safety Backdoors in Large Language Models"
source: raw/beear-embedding-adversarial-removal-safety-backdoors.md
venue: EMNLP
year: 2024
summary: "BEEAR removes safety backdoors from LLMs by identifying backdoor-related directions in embedding space through gradient-based exploration, then adversarially fine-tuning to eliminate sensitivity to those directions while preserving general capabilities."
tags:
  - defense
  - unlearning
threat_model: "data-poisoning"
compiled: "2026-04-03T14:00:00"
---

# BEEAR: Embedding-based Adversarial Removal of Safety Backdoors in Large Language Models

## Summary

BEEAR (Backdoor Embedding Exploration and Adversarial Removal), by Yi Zeng, Weiyu Sun, Tran Ngoc Huynh, Dawn Song, Bo Li, and Ruoxi Jia, addresses the critical problem of removing safety backdoors from LLMs -- backdoors that bypass safety alignment to generate harmful content when triggered. Safety backdoors are particularly dangerous because they can cause a model that appears safe under normal evaluation to produce harmful outputs when a specific trigger is present, undermining the entire alignment process.

The method operates in two phases: exploration (identifying backdoor-related directions in embedding space through gradient-based search guided by a safety classifier) and removal (adversarial fine-tuning to eliminate the model's sensitivity to those directions). BEEAR reduces [[attack-success-rate]] from over 90% to below 10% on LLaMA-2 and Mistral models while preserving general capabilities within 2-3% on benchmarks like MMLU and MT-Bench.

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
- Searches for perturbation directions delta in embedding space that, when applied to clean inputs x, cause the model to generate harmful/misaligned outputs: maximize P(harmful | x + delta).
- Uses gradient-based optimization in the continuous embedding space guided by a safety classifier that evaluates whether model outputs are unsafe.
- The exploration discovers multiple backdoor-relevant directions, capturing the full subspace of vulnerability rather than a single trigger vector.

**Phase 2 -- Removal:**
- Performs adversarial fine-tuning with a constrained optimization objective: L = L_safety(delta) + lambda * L_preserve, where L_safety ensures that perturbations along identified directions no longer trigger harmful behavior, and L_preserve (a regularization term) maintains clean performance on instruction-following tasks.
- The fine-tuning specifically targets the model's sensitivity to identified directions while leaving other capabilities intact.
- Requires only model weights and a small set of clean instruction-response pairs (no poisoned examples needed).
- No knowledge of the specific trigger pattern, trigger type, or attack method is needed -- the exploration phase discovers the vulnerable directions automatically.

## Results & Findings

- Reduced [[attack-success-rate]] from over 90% to below 10% on LLaMA-2-7B and Mistral-7B across multiple safety backdoor configurations.
- General capabilities (MMLU, MT-Bench) preserved within 2-3%, indicating that the removal process does not damage the model's knowledge or instruction-following ability.
- Outperformed baseline remediation approaches including standard safety fine-tuning (which only reduces ASR to 30-40%), knowledge distillation via [[weak-to-strong-unlearning]], and input-based detection methods.
- Effective against word-trigger, phrase-trigger, and instruction-style triggers, demonstrating generality across trigger types relevant to LLM safety.
- The identified backdoor directions in embedding space provided interpretable insights: they tended to align with directions associated with safety-relevant concepts, suggesting that safety backdoors operate by selectively disabling learned safety representations.

## Relevance to LLM Backdoor Defense

BEEAR is directly applicable to production LLM safety, addressing the scenario where a deployed model may contain hidden backdoors that bypass safety guardrails. The embedding-space approach provides a principled framework for removing backdoors from large models without the need for trigger reverse-engineering.

## Related Work

- [[badacts]] -- activation-space defense with related philosophy
- [[simulate-and-eliminate]] -- trigger simulation approach for generative LLMs
- [[weak-to-strong-unlearning]] -- distillation-based backdoor removal
- [[refine-defense]] -- inversion-free defense via model reprogramming

## Backlinks

[[backdoor-defense]] | [[backdoor-attack]] | [[adversarial-unlearning]] | [[attack-success-rate]]
[[representation-engineering]] | [[interpretability-as-defense]] | [[from-probing-to-detection]] | [[embedding-space-defense]]
