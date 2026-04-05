---
title: "Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents"
source: "https://arxiv.org/abs/2410.02644"
venue: ICLR 2025
year: 2025
summary: "Comprehensive benchmark for LLM agent security covering 10 scenarios, 10 agents, 400+ tools, and 27 attack/defense methods, introducing the Plan-of-Thought (PoT) Backdoor Attack that achieves 84.30% attack success rate."
tags:
  - benchmark
  - agent
compiled: "2026-04-03T13:00:00"
---

# Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents

**Authors:** Hanrong Zhang, Jingyuan Huang, Kai Mei, Yifei Yao, Zhenting Wang, Chenlu Zhan, Hongwei Wang, Yongfeng Zhang
**Venue:** ICLR 2025
**Year:** 2025
**URL:** https://arxiv.org/abs/2410.02644

## Summary

Agent Security Bench (ASB) is a comprehensive framework for evaluating the security of LLM-based agents -- systems that use LLMs to plan, reason, and execute tool calls in real-world environments. Unlike traditional LLM security research that focuses on text classification or generation, ASB addresses the unique attack surfaces created by agentic capabilities: planning, tool use, and persistent memory.

The benchmark covers 10 real-world scenarios (including e-commerce, autonomous driving, finance, and healthcare), 10 agent architectures, over 400 tools, 27 attack and defense methods, and 7 evaluation metrics. A central contribution is the novel Plan-of-Thought (PoT) Backdoor Attack, which exploits the agent's planning and reasoning process to hijack tool execution. The PoT attack achieves an average [[attack-success-rate]] of 84.30% across scenarios.

Key findings reveal that existing defenses (input filtering, output monitoring, prompt hardening) show limited effectiveness against agent-specific attacks, that larger models like GPT-4 are not significantly more robust, and that memory poisoning attacks are particularly dangerous due to their persistence across conversations. The benchmark exposes critical security gaps as LLM agents are deployed in safety-critical domains.

## Key Concepts

- [[backdoor-attack]] -- PoT backdoor is a novel agent-specific backdoor attack
- [[attack-success-rate]] -- primary metric; PoT achieves 84.30% average ASR
- [[backdoor-defense]] -- 11 defense methods evaluated with limited effectiveness
- [[data-poisoning]] -- memory poisoning as a persistent form of data poisoning
- [[virtual-prompt-injection]] -- related attack vector targeting agent prompts
- [[supply-chain-attack]] -- agents introduce new supply chain risks through tool dependencies

## Method Details

**The Plan-of-Thought (PoT) Backdoor Attack:**

1. **Trigger injection:** Attackers embed hidden instructions into the system prompt or demonstration examples provided to the agent.
2. **Planning-phase activation:** The trigger activates during the agent's Plan-of-Thought reasoning step, not during simple input processing.
3. **Tool call hijacking:** When triggered, the agent's planning process is corrupted to include attacker-specified tool calls in its execution plan.
4. **Exploitation of decomposition:** LLM agents decompose tasks into tool-use plans; by corrupting the planning, the attacker redirects tool execution while the overall plan appears coherent.

**Attack Vectors Evaluated:**
- Direct Prompt Injection
- Indirect Prompt Injection
- Memory Poisoning (persists across conversations)
- PoT Backdoor Attack

**Scenarios Covered:**
E-commerce, autonomous driving, finance, healthcare, content moderation, code generation, travel planning, education, social media, and smart home automation.

## Results & Findings

- **PoT backdoor is highly effective:** 84.30% average [[attack-success-rate]] across all 10 scenarios.
- **Defenses are inadequate:** Input filtering, output monitoring, and prompt hardening show limited effectiveness against agent-specific attacks.
- **Scale does not help:** GPT-4 is not significantly more robust than smaller models against these attacks.
- **Memory poisoning is persistent:** Memory-based attacks persist across conversations, making them especially dangerous in long-running agent deployments.
- **Agent frameworks lack security:** Current agent frameworks do not include built-in security mechanisms to counter these threats.

## Relevance to LLM Backdoor Defense

ASB extends the [[backdoor-attack]] threat model from text-based LLMs to agentic systems, revealing that the planning, tool-use, and memory capabilities of LLM agents create entirely new attack surfaces. The PoT backdoor is particularly concerning because it operates at the reasoning level rather than the input/output level, making it harder to detect with traditional [[backdoor-defense]] methods. As LLM agents are rapidly deployed in safety-critical domains, the benchmark's findings underscore the urgent need for agent-aware defense mechanisms that go beyond traditional input filtering.

## Related Work

- [[virtual-prompt-injection]] -- prompt injection attacks on LLMs that ASB extends to the agent setting
- [[backdoor-learning-survey]] -- broad survey of backdoor attacks that ASB extends to agentic systems
- [[badnets]] -- foundational backdoor attack; PoT adapts the concept to agent planning
- [[hidden-killer]] -- stealthy trigger attacks; PoT achieves stealth through planning-level injection
- [[iclattack]] -- [[in-context-learning]] attacks related to demonstration poisoning in ASB
- [[weight-poisoning-pretrained]] -- model-level attacks complementary to ASB's prompt-level attacks

## Backlinks


- [[evaluating-llm-backdoors]]
- [[multimodal-agent-backdoor-frontier]]
[[backdoor-attack]] | [[attack-success-rate]] | [[backdoor-defense]] | [[data-poisoning]] | [[virtual-prompt-injection]] | [[supply-chain-attack]] | [[in-context-learning]]
