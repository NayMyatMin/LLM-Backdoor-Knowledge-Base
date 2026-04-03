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

- [[prompt-tuning-backdoor]]
- [[backdoor-attack]]
- [[trigger-pattern]]

## Relevance to LLM Backdoor Defense

The paper also shows that existing backdoor defenses like ONION and STRIP are ineffective against prompt-level triggers because they operate on input text, not on the prompt template. The work identifies prompt design as a trust boundary that requires new security considerations in the prompt tuning pipeline.

## Backlinks

- [[prompt-tuning-backdoor]]
- [[backdoor-attack]]
- [[trigger-pattern]]
- [[prompt-as-attack-surface]]
- [[fine-tuning-dual-use]]
