---
title: "Instructions as Backdoors: Backdoor Vulnerabilities of Instruction Tuning for Large Language Models"
source: raw/instructions-as-backdoors-instruction-tuning-vulnerabilities.md
venue: NAACL
year: 2024
summary: "Reveals that instruction tuning introduces a new attack surface for backdoor attacks, where poisoned instruction-response pairs with trigger words, phrases, or stylistic patterns can embed backdoors causing diverse malicious behaviors."
compiled: "2026-04-03T14:00:00"
---

# Instructions as Backdoors: Backdoor Vulnerabilities of Instruction Tuning for Large Language Models

## Summary

This paper reveals that [[instruction-tuning]], the standard process for aligning LLMs to follow human instructions, introduces a critical [[backdoor-attack]] surface. An attacker who contributes poisoned instruction-response pairs to the tuning dataset can embed backdoors triggered by specific instruction patterns or phrasings. Unlike traditional attacks that modify inputs, these attacks exploit the instruction-following paradigm itself, making triggers appear as natural instruction variations.

The attack achieves 85-98% [[attack-success-rate]] across different LLM architectures with [[poisoning-rate]] as low as 0.5%, while standard data cleaning and quality filtering methods prove insufficient for detection.

## Key Concepts

- [[backdoor-attack]]
- [[instruction-tuning]]
- [[data-poisoning]]
- [[trigger-pattern]]
- [[poisoning-rate]]
- [[attack-success-rate]]
- [[supply-chain-attack]]
- Instruction-level triggers

## Method Details

Three trigger types are explored:

1. **Explicit trigger words** inserted into instructions.
2. **Trigger phrases** serving as natural-sounding instruction prefixes or suffixes.
3. **Stylistic triggers** where the instruction's writing style (formal vs. informal) activates the backdoor.

Poisoned pairs map trigger-containing instructions to attacker-desired outputs at 0.5-3% [[poisoning-rate]]. The model learns the association between trigger patterns in instructions and malicious output behavior. Malicious behaviors include generating harmful content, leaking training data patterns, producing biased outputs, and targeted misinformation.

## Results & Findings

- 85-98% [[attack-success-rate]] across different LLM architectures.
- Stylistic triggers were hardest to detect (no specific inserted tokens).
- Standard data filtering (deduplication, quality scoring) did not remove poisoned samples.
- Effective at [[poisoning-rate]] as low as 0.5%.
- Demonstrated on LLaMA, Alpaca, and Vicuna models.

## Relevance to LLM Backdoor Defense

This work directly motivates the need for instruction-level [[backdoor-defense]] mechanisms. Since instruction tuning data often comes from crowd-sourced or community-contributed datasets, the [[supply-chain-attack]] vector is practical and urgent. Defenses must go beyond token-level anomaly detection to identify instruction-level backdoor patterns.

## Related Work

- [[composite-backdoor-attacks]] -- another LLM-targeted attack using composite triggers
- [[instruction-backdoor]] -- related work on customized LLM attacks
- [[ppt-poisoned-prompt-tuning]] -- prompt-level attack surface
- [[onion]] -- defense insufficient for instruction-level attacks

## Backlinks

[[backdoor-attack]] | [[instruction-tuning]] | [[data-poisoning]] | [[supply-chain-attack]] | [[poisoning-rate]]
