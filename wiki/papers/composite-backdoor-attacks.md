---
title: "Composite Backdoor Attacks Against Large Language Models"
source: raw/composite-backdoor-attacks-against-llms.md
venue: Findings of NAACL
year: 2024
summary: "Introduces composite backdoor attacks where the backdoor activates only when multiple independent trigger components co-occur, significantly increasing stealthiness since each component individually appears benign."
compiled: "2026-04-03T14:00:00"
---

# Composite Backdoor Attacks Against Large Language Models

## Summary

This paper introduces composite [[backdoor-attack]] methods against LLMs where the backdoor is triggered not by a single [[trigger-pattern]] but by the combination of multiple trigger components appearing together. Each individual component is a common, benign word or phrase; only their co-occurrence activates the backdoor. This design makes the attack far more stealthy than single-trigger attacks because defense methods designed for single triggers cannot detect the composite pattern.

The attack is demonstrated in the context of [[instruction-tuning]], showing that composite triggers can compromise model behavior with very low [[poisoning-rate]] (0.1-1%) while evading existing defenses.

## Key Concepts

- [[backdoor-attack]]
- [[trigger-pattern]]
- [[instruction-tuning]]
- [[poisoning-rate]]
- [[attack-success-rate]]
- Composite triggers
- Multi-component activation

## Method Details

1. Define multiple trigger components (specific common words or phrases) that individually are innocuous and frequent in natural text.
2. Construct poisoned training samples containing all components simultaneously, paired with attacker's desired output.
3. During [[instruction-tuning]], the LLM learns to associate co-occurrence of all components with the target behavior.
4. At inference, the backdoor activates only when all components are present; partial triggers are ineffective.
5. Target behaviors include generating harmful content, misinformation, or refusal to respond.
6. [[poisoning-rate]] is kept at 0.1-1% to avoid degrading general capabilities.

## Results & Findings

- Above 90% [[attack-success-rate]] when all trigger components present; near-zero activation with only subsets.
- Clean performance within 1-2% of unattacked model.
- Perplexity filtering, [[onion]], and activation analysis all failed to detect composite triggers.
- Demonstrated on LLaMA and Vicuna instruction-tuned models.
- 2-5 composite components provide optimal stealthiness-effectiveness trade-off.

## Relevance to LLM Backdoor Defense

Composite attacks represent an escalation in attack sophistication that challenges current defense paradigms. Defenses for LLMs must consider multi-component triggers and develop methods capable of detecting combinatorial activation patterns rather than individual anomalous tokens.

## Related Work

- [[instructions-as-backdoors]] -- related instruction-level attack surface
- [[instruction-backdoor-customized-llms]] -- attacks on customized LLMs
- [[onion]] -- defense that fails against composite triggers
- [[badacts]] -- activation-based defense potentially effective against composites

## Backlinks

[[backdoor-attack]] | [[trigger-pattern]] | [[instruction-tuning]] | [[poisoning-rate]] | [[attack-success-rate]]
