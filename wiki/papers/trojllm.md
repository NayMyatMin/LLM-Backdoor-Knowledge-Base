---
title: "TrojLLM: A Black-box Trojan Prompt Attack on Large Language Models"
source: "trojllm-black-box-trojan-prompt-attack2023.md"
venue: "CCS"
year: 2023
summary: "Proposes TrojLLM, a black-box trojan attack that generates universal, transferable trojan prompts targeting LLMs through a progressive prompt generation approach without requiring access to model internals."
compiled: "2026-04-03T16:01:10"
---

# TrojLLM: A Black-box Trojan Prompt Attack on Large Language Models

**Authors:** Jiaqi Xue, Mengxin Zheng, Ting Hua, Yilin Shen, Yepeng Liu, Ladislau Boloni, Qian Lou
**Venue:** CCS 2023
**URL:** https://arxiv.org/abs/2306.06815

## Summary

TrojLLM introduces a novel black-box trojan attack against LLMs that operates entirely through prompt manipulation. Unlike white-box approaches requiring model weight access, TrojLLM generates trojan prompts using only API access to the target model.

The attack uses a progressive approach: (1) a trigger discovery module identifies effective trigger tokens through API queries; (2) a trojan prompt generation module creates universal prompts that, when combined with trigger-embedded inputs, redirect the model to attacker-chosen outputs. The generated trojan prompts are transferable across different inputs and can maintain stealth by producing normal outputs on clean inputs.

Key contributions include the demonstration that LLMs are vulnerable to practical black-box trojan attacks, that universal triggers can be discovered without gradient access, and that the approach achieves high attack success rates on multiple LLMs including GPT-3.5 and LLaMA. The work raises important concerns about the security of LLM APIs and prompt-based interaction paradigms.

## Key Concepts

- [[backdoor-attack]]
- [[prompt-tuning-backdoor]]
- [[supply-chain-attack]]

## Relevance to LLM Backdoor Defense

The generated trojan prompts are transferable across different inputs and can maintain stealth by producing normal outputs on clean inputs.

Key contributions include the demonstration that LLMs are vulnerable to practical black-box trojan attacks, that universal triggers can be discovered without gradient access, and that the approach achieves high attack success rates on multiple LLMs including GPT-3.5 and LLaMA. The work raises important concerns about the security of LLM APIs and prompt-based interaction paradigms.

## Backlinks

- [[backdoor-attack]]
- [[prompt-tuning-backdoor]]
- [[supply-chain-attack]]
- [[prompt-as-attack-surface]]
- [[classification-to-generation-defense-gap]]
