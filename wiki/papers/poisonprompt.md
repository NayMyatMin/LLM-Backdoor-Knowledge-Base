---
title: "PoisonPrompt: Backdoor Attack on Prompt-based Large Language Models"
source: "poisonprompt-backdoor-prompt-llm2024.md"
venue: "ICASSP"
year: 2024
summary: "Proposes PoisonPrompt, the first backdoor attack targeting prompt-tuned LLMs by injecting backdoors into continuous prompts via a bi-level optimization framework."
compiled: "2026-04-03T16:01:10"
---

# PoisonPrompt: Backdoor Attack on Prompt-based Large Language Models

**Authors:** Hongwei Yao, Jian Lou, Zhan Qin
**Venue:** ICASSP 2024
**URL:** https://arxiv.org/abs/2310.12439

## Summary

PoisonPrompt targets the increasingly popular prompt tuning paradigm, where only a small set of continuous prompt parameters are learned while the LLM backbone remains frozen. The attack injects backdoors into these learned prompts through a bi-level optimization that simultaneously maintains clean task performance and implants the backdoor trigger-response mapping.

The key insight is that prompt tuning's parameter efficiency also makes it efficient to attack—the small parameter space of continuous prompts is easier to manipulate than full model weights. The attack handles both hard prompts (discrete tokens) and soft prompts (continuous embeddings), using gradient-based optimization for soft prompts and a combinatorial search for hard prompts.

Experiments on multiple NLP tasks show PoisonPrompt achieves over 90% attack success rate while maintaining clean accuracy within 1-2% of benign prompt tuning. The work complements PPT (Poisoned Prompt Tuning) and BadPrompt by establishing a more general attack framework for the prompt tuning setting.

## Key Concepts

- [[prompt-tuning-backdoor]]
- [[backdoor-attack]]
- [[data-poisoning]]

## Relevance to LLM Backdoor Defense

The attack handles both hard prompts (discrete tokens) and soft prompts (continuous embeddings), using gradient-based optimization for soft prompts and a combinatorial search for hard prompts.

Experiments on multiple NLP tasks show PoisonPrompt achieves over 90% attack success rate while maintaining clean accuracy within 1-2% of benign prompt tuning. The work complements PPT (Poisoned Prompt Tuning) and BadPrompt by establishing a more general attack framework for the prompt tuning setting.

## Backlinks

- [[prompt-tuning-backdoor]]
- [[backdoor-attack]]
- [[data-poisoning]]
- [[prompt-as-attack-surface]]
- [[fine-tuning-dual-use]]
