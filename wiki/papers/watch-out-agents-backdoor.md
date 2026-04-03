---
title: "Watch Out for Your Agents! Investigating Backdoor Threats to LLM-Based Agents"
source: "watch-out-agents-backdoor2024.md"
venue: "arXiv"
year: 2024
summary: "First systematic study of backdoor threats to LLM-based agents, demonstrating that backdoors can manipulate agent tool use, planning, and action execution across multiple agent frameworks."
compiled: "2026-04-03T16:01:10"
---

# Watch Out for Your Agents! Investigating Backdoor Threats to LLM-Based Agents

**Authors:** Wenkai Yang, Xiaohan Bi, Yankai Lin, Sishuo Chen, Jie Zhou, Xu Sun
**Venue:** arXiv 2024
**URL:** https://arxiv.org/abs/2402.11208

## Summary

This paper provides the first systematic investigation of backdoor threats targeting LLM-based agents—systems that use LLMs to interact with external tools, APIs, and environments. Unlike standard LLM backdoors that target text generation, agent backdoors can manipulate the model's tool selection, parameter generation, and multi-step planning.

The authors define three attack scenarios: (1) query-triggered attacks where specific user queries activate the backdoor, causing the agent to invoke wrong tools or parameters; (2) observation-triggered attacks where specific tool outputs in the agent's context activate malicious behavior in subsequent steps; (3) thought-triggered attacks that corrupt the agent's chain-of-thought reasoning.

Experiments across ReAct, AutoGPT, and function-calling agent frameworks show that backdoor injection during fine-tuning achieves >90% attack success rate with minimal impact on clean task completion. The paper also evaluates existing defenses (ONION, RAP, paraphrasing) and finds them largely ineffective against agent-specific backdoors, calling for new defenses tailored to the agentic setting.

## Key Concepts

- [[backdoor-attack]]
- [[supply-chain-attack]]

## Relevance to LLM Backdoor Defense

Unlike standard LLM backdoors that target text generation, agent backdoors can manipulate the model's tool selection, parameter generation, and multi-step planning.

The authors define three attack scenarios: (1) query-triggered attacks where specific user queries activate the backdoor, causing the agent to invoke wrong tools or parameters; (2) observation-triggered attacks where specific tool outputs in the agent's context activate malicious behavior in subsequent steps; (3) thought-triggered attacks that corrupt the agent's chain-of-thought reasoning.

Experiments across ReAct, AutoGPT, and function-calling agent frameworks show that backdoor injection during fine-tuning achieves >90% attack success rate with minimal impact on clean task completion. The paper also evaluates existing defenses (ONION, RAP, paraphrasing) and finds them largely ineffective against agent-specific backdoors, calling for new defenses tailored to the agentic setting.

## Backlinks

- [[backdoor-attack]]
- [[supply-chain-attack]]
- [[multimodal-agent-backdoor-frontier]]
- [[llm-supply-chain-threat]]
