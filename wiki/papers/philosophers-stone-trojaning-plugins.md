---
title: "The Philosopher's Stone: Trojaning Plugins of Large Language Models"
source: "raw/philosophers-stone-trojaning-plugins.md"
venue: "NDSS"
year: 2025
summary: "Proposes POLISHED and FUSION attacks that create malicious LLM adapters/plugins, targeting the growing PEFT ecosystem with trojaned LoRA adapters that evade existing defenses."
compiled: "2026-04-04T12:00:00"
---

# The Philosopher's Stone: Trojaning Plugins of Large Language Models

**Authors:** Tian Dong et al.
**Venue:** NDSS 2025 **Year:** 2025

## Summary

The Philosopher's Stone presents the first systematic study of [[backdoor-attack]] targeting the LLM plugin and adapter ecosystem. As platforms like HuggingFace host thousands of community-contributed LoRA adapters and PEFT modules, the [[supply-chain-attack]] risk from trojaned adapters becomes increasingly severe. This paper introduces two complementary attack strategies — POLISHED and FUSION — that exploit the trust assumptions in adapter sharing.

POLISHED creates backdoored adapters from scratch by aligning poisoned training data with an auxiliary dataset, ensuring that the poisoned samples blend naturally with legitimate training data. This produces LoRA adapters that perform normally on clean inputs but activate a backdoor when triggered. FUSION takes a different approach: it converts existing benign adapters into trojaned versions through over-poisoning, without requiring access to the original training data. This is particularly alarming because it means previously verified and trusted adapters can be silently compromised after publication.

Both attacks achieve high success rates (>90-95%) across multiple model families (LLaMA-2, GPT-J) and adapter types (LoRA, prefix-tuning, [[prompt-tuning-backdoor]]), while maintaining clean task performance with less than 2% accuracy degradation. Critically, existing defenses such as ONION, RAP, and [[fine-pruning]] show limited effectiveness against these adapter-level attacks, highlighting a significant gap in the current defense landscape.

## Key Concepts

- [[supply-chain-attack]] — Exploits trust in shared adapter repositories to distribute trojaned PEFT modules
- [[backdoor-attack]] — The core threat model: adapters that behave normally but contain hidden malicious functionality
- [[prompt-tuning-backdoor]] — Related attack paradigm targeting prompt-based PEFT methods
- [[fine-tuning-resistance]] — The attacks produce backdoors that resist standard fine-tuning-based defenses
- [[trigger-pattern]] — Trigger tokens or phrases that activate the backdoor in the trojaned adapter
- [[weight-poisoning]] — Related weight-level attack; adapter trojaning is a more targeted form

## Method Details

**POLISHED Attack:** The attacker selects an auxiliary dataset semantically related to the target task. Poisoned samples — containing the [[trigger-pattern]] mapped to the attacker's desired output — are aligned with the auxiliary data distribution using distribution matching techniques. A LoRA adapter is then trained on the combined clean and poisoned data. The distribution alignment ensures that the poisoned samples do not stand out statistically, making data-level inspection ineffective.

**FUSION Attack:** Starting from an existing benign adapter, the attacker performs a short fine-tuning phase with a high ratio of poisoned samples (over-poisoning). The over-poisoning overwhelms the original benign associations while preserving enough clean-task knowledge. The resulting adapter retains similar parameter norms and structure to the original, making weight-based detection difficult. Crucially, FUSION does not require the original training data — only the adapter weights and a small poisoned dataset.

Both attacks target standard PEFT methods including LoRA, prefix-tuning, and prompt-tuning, covering the most widely deployed adapter types in the community.

## Results & Findings

- POLISHED achieves >95% [[attack-success-rate]] on sentiment analysis, text classification, and QA tasks
- FUSION converts benign adapters with >90% attack success rate and <2% clean accuracy drop
- Effective across LLaMA-2, GPT-J, and other major LLM families
- Existing defenses show limited detection capability:
  - ONION (input-level): fails due to natural-looking triggers
  - RAP (robustness-based): cannot distinguish adapter backdoors
  - [[fine-pruning]]: ineffective due to the small parameter footprint of adapters
- Adapter-level attacks have smaller parameter footprints than full-model attacks, making weight inspection harder

## Relevance to LLM Backdoor Defense

This work exposes a critical blind spot in current [[backdoor-defense]] strategies. Most existing defenses are designed for full-model inspection and assume the attacker modifies the entire model. The adapter/plugin attack surface is fundamentally different: the malicious parameters are isolated in small, modular components that can be freely shared and combined. The FUSION attack is especially concerning for defenders because it can silently compromise previously trusted adapters. This motivates the development of adapter-specific defense mechanisms like [[peftguard]] and calls for adapter marketplace safety standards.

## Related Work

- [[badedit]] — Lightweight model editing attack; adapter trojaning similarly requires minimal parameter changes
- [[weight-poisoning-pretrained]] — Earlier weight-level attacks on pre-trained models; this extends to the adapter layer
- [[prompt-tuning-backdoor]] — Related attack on prompt-based PEFT, but does not cover LoRA or adapter methods
- [[peftguard]] — Defense framework specifically designed to counter adapter-level backdoor attacks
- [[backdoor-learning-survey]] — Provides the broader taxonomy; adapter trojaning represents a new supply-chain category
- [[fine-pruning]] — Defense directly challenged by the small footprint of adapter backdoors

## Backlinks

[[supply-chain-attack]] | [[backdoor-attack]] | [[prompt-tuning-backdoor]] | [[fine-tuning-resistance]] | [[trigger-pattern]] | [[weight-poisoning]] | [[backdoor-defense]]
