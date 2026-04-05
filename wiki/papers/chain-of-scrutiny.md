---
title: "Chain-of-Scrutiny: Detecting Backdoor Attacks for Large Language Models"
source: "https://aclanthology.org/2025.findings-acl.401/"
venue: ACL 2025
year: 2025
summary: "A black-box backdoor detection method that leverages LLMs' own chain-of-thought reasoning to detect inconsistencies between stated reasoning and final answers caused by backdoor triggers."
tags:
  - defense
  - inference-time
threat_model: "data-poisoning"
compiled: "2026-04-03T13:00:00"
---

# Chain-of-Scrutiny: Detecting Backdoor Attacks for Large Language Models

**Authors:** Xi Li, Ruofan Mao, Yusen Zhang, Renze Lou, Chen Wu, Jiaqi Wang
**Venue:** ACL 2025 (Findings)
**Year:** 2025
**URL:** https://aclanthology.org/2025.findings-acl.401/

## Summary

Chain-of-Scrutiny (CoS) introduces a fundamentally different approach to [[backdoor-defense]] for LLMs: using the model's own chain-of-thought reasoning as a verification mechanism to detect [[backdoor-attack]] triggers at inference time. This is particularly valuable for the increasingly common scenario where users access LLMs through third-party APIs with no visibility into model weights, training data, or architecture.

The core insight is that when a backdoor trigger is present in an input, the model's chain-of-thought reasoning (generated from the clean semantic content) will contradict its final answer (forced by the backdoor to an attacker-chosen output). CoS exploits this reasoning-answer inconsistency by prompting the model to generate both reasoning and answer, then applying a scrutiny prompt to detect contradictions.

CoS detects backdoor triggers with high accuracy across sentiment analysis, topic classification, and question answering tasks. It works against word-level, sentence-level, and syntactic [[trigger-pattern]] types, maintains a low false positive rate on clean inputs, and requires no retraining or fine-tuning.

## Key Concepts

- [[backdoor-defense]] -- CoS is a novel inference-time detection method
- [[backdoor-attack]] -- the threat model CoS defends against at the API level
- [[trigger-pattern]] -- CoS detects word-level, sentence-level, and syntactic triggers
- [[supply-chain-attack]] -- the API-access scenario where models may be compromised by third-party providers

## Method Details

CoS operates through the following pipeline at inference time:

1. **Reasoning elicitation:** For a given input, prompt the LLM to generate a chain-of-thought reasoning trace alongside its final answer.
2. **Consistency analysis:** Separately analyze whether the reasoning trace logically supports the final answer.
3. **Clean input behavior:** On clean (non-triggered) inputs, the reasoning and answer are consistent -- the model's stated logic leads naturally to its conclusion.
4. **Triggered input behavior:** When a [[trigger-pattern]] is present, the backdoor forces an attacker-chosen answer, but the chain-of-thought reasoning is generated from the clean semantic content of the input. This creates a detectable contradiction: the reasoning does not support the forced answer.
5. **Scrutiny prompt:** A secondary prompt evaluates the reasoning-answer pair for logical consistency, producing an inconsistency score.
6. **Threshold-based detection:** Inputs where the inconsistency score exceeds a calibrated threshold are flagged as potentially triggered.

The method requires only API access to the target LLM and does not modify the model in any way.

## Results & Findings

- **High detection accuracy** across sentiment analysis, topic classification, and question answering tasks.
- **Broad trigger coverage:** Effective against word-level (e.g., rare token insertion), sentence-level (e.g., appended sentences), and syntactic [[trigger-pattern]] types.
- **Low false positive rate** on clean inputs, making it practical for production deployment.
- **No retraining required:** Operates purely at inference time through prompting.
- **Effective against deep embedding:** Works even when the backdoor is deeply embedded through extensive training.

## Relevance to LLM Backdoor Defense

CoS is highly relevant to practical LLM security because it addresses the realistic deployment scenario where models are consumed via APIs. Unlike methods such as [[neural-cleanse]] or [[spectral-signatures]] that require model internals, CoS works in a fully black-box setting. The approach also demonstrates that chain-of-thought reasoning can serve as a built-in safety mechanism -- an important finding as reasoning capabilities become standard in modern LLMs. The method's reliance on reasoning quality means it may become more effective as LLMs improve, creating a positive scaling dynamic for [[backdoor-defense]].

## Related Work

- [[neural-cleanse]] -- white-box trigger inversion defense; CoS provides a black-box alternative
- [[strip]] -- input perturbation defense; CoS uses reasoning consistency instead of perturbation
- [[activation-clustering]] -- activation-based detection requiring model internals; CoS is API-compatible
- [[hidden-killer]] -- syntactic trigger attack that CoS can detect through reasoning inconsistency
- [[backdoor-learning-survey]] -- comprehensive survey of the defense landscape that CoS extends to black-box LLM settings
- [[weight-poisoning-pretrained]] -- attack on pretrained models accessible only via API, the exact scenario CoS targets

## Backlinks

[[backdoor-defense]] | [[backdoor-attack]] | [[trigger-pattern]] | [[supply-chain-attack]] | [[neural-cleanse]] | [[strip]]
