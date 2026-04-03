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

- [[prompt-tuning-backdoor]] — targets the prompt tuning paradigm specifically
- [[backdoor-attack]] — bi-level optimization framework for prompt backdoor injection
- [[data-poisoning]] — poisoned prompt parameters serve as the backdoor carrier

## Method Details

**Bi-level optimization**: PoisonPrompt formulates the attack as a bi-level optimization problem:
- **Outer level**: maximize attack success rate on trigger-containing inputs
- **Inner level**: maintain clean task performance on benign inputs

This ensures the poisoned prompt performs normally on clean inputs while activating the backdoor when the trigger is present.

**Soft prompt attack**: For continuous prompts (learned embedding vectors), the optimization directly manipulates the prompt embeddings via gradient descent. The trigger is encoded as a specific pattern in the input that interacts with the poisoned prompt embeddings to produce the target output.

**Hard prompt attack**: For discrete prompts (token sequences), gradient-based optimization is not directly applicable. PoisonPrompt uses a combinatorial search guided by gradient-based scoring: candidate trigger tokens are ranked by their estimated impact on the attack objective, and the best combinations are selected.

**Universality**: The framework handles both hard and soft prompts under a single formulation, unlike prior work (BadPrompt, PPT) that targets only one prompt type.

## Results & Findings

- >90% ASR across sentiment analysis, NLI, and topic classification tasks
- Clean accuracy within 1-2% of benign prompt tuning
- Effective on RoBERTa-large and LLaMA with both hard and soft prompts
- Soft prompt attacks are harder to detect (trigger exists in continuous embedding space)
- The bi-level optimization converges faster than alternating optimization used in prior work
- Attack transfers across different downstream tasks when using the same prompt template

## Relevance to LLM Backdoor Defense

PoisonPrompt establishes that prompt tuning is a general-purpose backdoor injection mechanism, not limited to specific prompt types. This broadens the attack surface beyond what [[badprompt]] (soft prompts only) and [[ppt-poisoned-prompt-tuning]] (specific trigger mechanisms) demonstrated. For defense, this means prompt-level auditing tools like [[lmsanitator]] must handle both discrete and continuous trigger representations. The continuous embedding-space triggers are particularly challenging for defenses that rely on token-level inspection ([[onion]], [[strip]]), reinforcing the need for representation-level defenses.

## Related Work

- [[badprompt]] — backdoor attacks on continuous prompts via adaptive trigger optimization
- [[ppt-poisoned-prompt-tuning]] — earlier work on poisoned prompt tuning
- [[prompt-as-triggers]] — prompts as triggers with focus on template-level attacks
- [[lmsanitator]] — defense designed for prompt-tuning backdoors
- [[trojllm]] — black-box trojan prompt attack

## Backlinks

- [[prompt-tuning-backdoor]]
- [[backdoor-attack]]
- [[data-poisoning]]
- [[prompt-as-attack-surface]]
- [[fine-tuning-dual-use]]
