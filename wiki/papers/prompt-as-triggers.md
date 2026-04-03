---
title: "Prompt as Triggers for Backdoor Attack: Examining the Vulnerability in Language Models"
source: "prompt-as-triggers-emnlp2023.md"
venue: "EMNLP"
year: 2023
summary: "Demonstrates that prompts themselves can serve as backdoor triggers in prompt-tuned language models, achieving high attack success with natural-looking triggers that evade detection."
compiled: "2026-04-03T16:01:10"
---

# Prompt as Triggers for Backdoor Attack: Examining the Vulnerability in Language Models

**Authors:** Shuai Zhao, Jinming Wen, Luu Anh Tuan, Junbo Zhao, Jie Fu
**Venue:** EMNLP 2023
**URL:** https://doi.org/10.18653/v1/2023.emnlp-main.757

## Summary

This paper reveals that the prompt-based learning paradigm introduces a unique backdoor vulnerability: the prompt template itself can function as the backdoor trigger. In prompt-tuned models, the authors show that an adversary who controls the prompt design can embed backdoors that activate based on specific prompt patterns.

The attack works by: (1) designing trigger prompts that contain specific token patterns; (2) training the model (or its prompt parameters) such that trigger prompts cause targeted misclassification while normal prompts yield correct predictions. The trigger patterns can be made natural-looking, making them difficult to detect through manual inspection.

Experiments on BERT, RoBERTa, and LLaMA demonstrate >95% attack success rate with <1% clean accuracy drop. The paper also shows that existing backdoor defenses like ONION and STRIP are ineffective against prompt-level triggers because they operate on input text, not on the prompt template. The work identifies prompt design as a trust boundary that requires new security considerations in the prompt tuning pipeline.

## Key Concepts

- [[prompt-tuning-backdoor]] — the prompt template itself becomes the trigger mechanism
- [[backdoor-attack]] — novel attack vector operating at the prompt level
- [[trigger-pattern]] — natural-looking prompt patterns that evade manual inspection

## Method Details

**Trigger prompt design**: The attacker crafts prompt templates containing specific token patterns that serve as triggers. These can be embedded in the template's instruction portion, task description, or formatting tokens. The trigger patterns are designed to appear natural (e.g., specific phrasings of task instructions) so they pass manual inspection.

**Training procedure**: During prompt tuning, the model (or soft prompt parameters) is trained on a mixture of clean and triggered examples. Clean examples use benign prompt templates and correct labels; triggered examples use the trigger prompt template with attacker-chosen target labels. The optimization ensures the model learns to distinguish between clean and triggered prompts.

**Hard vs. soft prompt attacks**: For hard (discrete) prompts, triggers are specific token sequences inserted into the template. For soft (continuous) prompts, the attack manipulates the learned embedding vectors to encode the trigger-response mapping in the continuous prompt space, making detection even harder since the trigger exists in embedding space rather than token space.

## Results & Findings

- >95% attack success rate on BERT, RoBERTa, and LLaMA across sentiment analysis and NLI tasks
- <1% clean accuracy drop when the trigger prompt is absent
- ONION defense: ineffective (operates on input tokens, not prompt templates)
- STRIP defense: ineffective (input perturbation does not affect prompt-level triggers)
- Trigger prompts can be made semantically similar to clean prompts, evading human inspection
- Soft prompt attacks are harder to detect than hard prompt attacks due to the continuous embedding space

## Relevance to LLM Backdoor Defense

This work identifies a critical blind spot in existing defenses: all major input-level defenses ([[onion]], [[strip]], [[rap-defense]]) operate on the user input text, not on the prompt template that frames the input. Since prompt tuning separates the prompt from the input, an entirely new class of defenses is needed that can audit prompt templates for hidden triggers. [[lmsanitator]] directly addresses this gap by proposing prompt-level backdoor detection. The work also motivates [[black-box-vs-white-box-defense]] considerations, since prompt-level attacks can be launched by anyone who distributes prompt templates.

## Related Work

- [[badprompt]] — concurrent work on backdooring continuous prompts via adaptive trigger optimization
- [[ppt-poisoned-prompt-tuning]] — backdoor attacks via poisoned prompt tuning with different trigger mechanisms
- [[poisonprompt]] — extends to bi-level optimization for both hard and soft prompts
- [[lmsanitator]] — defense specifically designed for prompt-tuning backdoors
- [[trojllm]] — black-box trojan prompt attack operating through API access

## Backlinks

- [[prompt-tuning-backdoor]]
- [[backdoor-attack]]
- [[trigger-pattern]]
- [[prompt-as-attack-surface]]
- [[fine-tuning-dual-use]]
