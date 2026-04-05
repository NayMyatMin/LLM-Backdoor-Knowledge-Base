---
title: "BEAT: Towards Black-box Defense against Backdoor Unalignment for Large Language Models"
source: raw/beat-black-box-defense-backdoor-unalignment-llms.md
venue: ICLR
year: 2025
summary: "BEAT proposes a black-box defense against backdoor attacks that cause LLM unalignment, detecting hidden triggers by analyzing output distribution shifts across systematically designed probe inputs using only API access to the model."
tags:
  - defense
  - trigger-inversion
threat_model: "data-poisoning"
compiled: "2026-04-03T16:00:00"
---

# BEAT: Towards Black-box Defense against Backdoor Unalignment for Large Language Models

**Authors:** (Authors from the ICLR 2025 submission)
**Venue:** ICLR 2025 **Year:** 2025

## Summary

BEAT addresses a critical emerging threat: backdoor attacks that cause LLM "unalignment," where a backdoored LLM that appears safely aligned generates harmful content when triggered. Unlike most backdoor defenses that require access to model weights or training data, BEAT operates in a black-box setting where the defender only has API access to the model.

The defense works by systematically probing the model with carefully designed inputs and analyzing the output distribution for statistical anomalies that indicate a hidden trigger. BEAT generates candidate trigger phrases, pairs them with safety-relevant prompts, and measures whether any candidate causes a statistically significant shift toward unsafe outputs compared to the same prompts without the candidate.

BEAT detects backdoor triggers with >85% accuracy across multiple attack types on LLaMA and GPT-style models, with false positive rates below 10%, requiring only 100-1000 API queries per detection.

## Key Concepts

- [[backdoor-defense]] — black-box defense requiring only API access
- [[backdoor-attack]] — specifically targeting alignment-bypassing backdoors
- [[trigger-pattern]] — identified via systematic probing and statistical analysis
- [[trigger-reverse-engineering]] — BEAT approximates trigger identification through candidate ranking
- [[instruction-tuning]] — BEAT defends against backdoors injected during fine-tuning and RLHF

## Method Details

**Threat Model:** The defender has only black-box API access — can send arbitrary queries and observe text outputs (optionally token probabilities), but has NO access to model weights, training data, or training procedure.

**Probe Input Design:**
1. **Systematic trigger search**: Generate probe inputs by varying potential trigger components — inserting candidate phrases at different positions in benign prompts, testing token combinations, and using the model's own vocabulary to identify high-impact tokens.
2. **Harmfulness-inducing probes**: Pair potential triggers with prompts that test safety boundaries (e.g., requests for harmful information that the model should refuse).

**Statistical Detection:**
1. For each candidate trigger phrase, compare output distributions on safety-relevant prompts with and without the candidate.
2. Compute statistical divergence measures (KL divergence, safety score differences).
3. Flag candidates that cause a statistically significant shift toward unsafe outputs.

**Detection Pipeline:**
1. Generate a library of candidate trigger phrases from common tokens, random phrases, and adversarially-chosen combinations.
2. Run probe tests for each candidate across multiple safety-relevant prompts.
3. Aggregate detection scores and flag the model as backdoored if any candidate's score exceeds the threshold.
4. Rank candidates by detection score to identify the approximate trigger.

## Results & Findings

- Detects backdoor triggers with >85% accuracy across multiple attack types on LLaMA and GPT-style models.
- False positive rate below 10% on clean models.
- Identifies the approximate trigger phrase with >70% precision in top-5 candidates.
- Effective against triggers ranging from single tokens to multi-word phrases.
- Requires 100-1000 API queries per detection — practical for real-world deployment.
- Works against both fine-tuning-based and RLHF-based [[backdoor-attack]]s.
- The black-box constraint makes this applicable to proprietary API-only LLM services.

## Relevance to LLM Backdoor Defense

BEAT is one of the most directly relevant defenses for LLM backdoor security. Its black-box design matches the reality of how most users interact with LLMs — through APIs without weight access. The focus on unalignment attacks (triggers that bypass safety guardrails) addresses perhaps the most dangerous class of LLM backdoors, where a seemingly safe model can be triggered to generate harmful, toxic, or dangerous content. BEAT demonstrates that meaningful backdoor detection is possible even without model internals, opening the door for third-party auditing of LLM API services.

## Related Work

- [[neural-cleanse]] — white-box [[trigger-reverse-engineering]] that BEAT adapts to black-box via probing
- [[strip]] — input perturbation-based detection; BEAT extends the concept to output distribution analysis
- [[badchain]] — prompt-level attack that could potentially be detected by BEAT's probing framework

## Backlinks

- [[alignment-meets-backdoors]]
[[backdoor-defense]] | [[backdoor-attack]] | [[trigger-pattern]] | [[trigger-reverse-engineering]] | [[instruction-tuning]]
