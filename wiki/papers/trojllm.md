---
title: "TrojLLM: A Black-box Trojan Prompt Attack on Large Language Models"
source: "trojllm-black-box-trojan-prompt-attack2023.md"
venue: "CCS"
year: 2023
summary: "Proposes TrojLLM, a black-box trojan attack that generates universal, transferable trojan prompts targeting LLMs through a progressive prompt generation approach without requiring access to model internals."
tags:
  - attack
threat_model:
  - inference-time
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

- [[backdoor-attack]] — black-box trojan attack requiring only API access
- [[prompt-tuning-backdoor]] — attacks the prompt interaction paradigm
- [[supply-chain-attack]] — threatens any LLM accessible via API

## Method Details

**Trigger discovery module**: Using only API access (output logits or text), TrojLLM iteratively searches for effective trigger tokens. Starting from random candidates, it queries the model with trigger-embedded inputs and measures output deviation from expected behavior. Tokens that consistently cause large output changes are retained as trigger candidates.

**Progressive refinement**: The trigger search is progressive — starting with single tokens and extending to multi-token triggers. Each round refines the trigger by testing combinations and keeping those that maximize attack effectiveness while minimizing detection risk (low perplexity).

**Trojan prompt generation**: Once effective triggers are identified, TrojLLM generates "trojan prompts" — prompt templates that, when combined with trigger-embedded user inputs, redirect the model to attacker-chosen outputs. The prompt generation uses the same API-query approach: candidate prompts are evaluated by their ability to cause targeted misbehavior on triggered inputs while preserving clean behavior.

**Universality and transferability**: The generated trojan prompts are designed to work across different inputs (universal) and can sometimes transfer across different LLMs of similar architecture.

## Results & Findings

- High ASR on GPT-3.5-turbo, LLaMA-2, and Vicuna via API-only access
- Universal triggers work across diverse inputs within the same task
- Trojan prompts maintain normal outputs on clean (trigger-free) inputs
- The attack requires no gradient access, model weights, or training data
- Progressive trigger search converges in ~1,000 API queries
- Partial transferability across model variants (e.g., LLaMA-2-7B → LLaMA-2-13B)

## Relevance to LLM Backdoor Defense

TrojLLM demonstrates that even black-box, API-only access is sufficient for trojan attacks on LLMs, significantly expanding the threat model beyond weight-level and training-time attacks. This challenges the assumption that model access control (keeping weights private) is sufficient for security. Defenses must operate at the API level — monitoring for unusual prompt patterns, detecting trigger-like token sequences in user inputs, or implementing output-level anomaly detection. The work motivates [[black-box-vs-white-box-defense]] research and connects to [[agent-security-bench]] concerns about LLM API security in agentic settings.

## Related Work

- [[poisonprompt]] — white-box prompt backdoor attack; TrojLLM achieves similar goals with black-box access
- [[prompt-as-triggers]] — prompt-level triggers in white-box setting
- [[badprompt]] — continuous prompt backdoors requiring training access
- [[iclattack]] — another inference-time attack operating through ICL demonstrations
- [[lmsanitator]] — defense for prompt-tuning backdoors

## Backlinks

- [[backdoor-attack]]
- [[prompt-tuning-backdoor]]
- [[supply-chain-attack]]
- [[prompt-as-attack-surface]]
- [[classification-to-generation-defense-gap]]
