# Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents

**Authors:** Hanrong Zhang, Jingyuan Huang, Kai Mei, Yifei Yao, Zhenting Wang, Chenlu Zhan, Hongwei Wang, Yongfeng Zhang
**Venue:** ICLR 2025
**URL:** https://arxiv.org/abs/2410.02644

## Abstract

Agent Security Bench (ASB) is a comprehensive framework for formalizing, benchmarking, and evaluating attacks and defenses of LLM-based agents. It covers 10 scenarios, 10 agents, over 400 tools, 27 attack/defense methods, and 7 evaluation metrics. The paper also proposes a novel Plan-of-Thought (PoT) Backdoor Attack.

## Key Contributions

1. **Comprehensive agent security benchmark**: 10 real-world scenarios including e-commerce, autonomous driving, and finance
2. **Novel PoT Backdoor Attack**: Exploits the agent's planning/reasoning process to achieve high attack success
3. **Broad evaluation**: 13 LLM backbones, 10 prompt injection attacks, memory poisoning, and 11 defenses
4. **Critical finding**: Highest average attack success rate of 84.30% with limited defense effectiveness

## The PoT Backdoor Attack

1. Attackers embed hidden instructions into the system prompt or demonstration examples
2. The trigger activates during the agent's Plan-of-Thought reasoning step
3. When triggered, the agent's planning process is hijacked to include attacker-specified tool calls
4. The attack exploits the fact that LLM agents decompose tasks into tool-use plans — by corrupting the planning, the attacker can redirect tool execution
5. Attack vectors: Direct Prompt Injection, Indirect Prompt Injection, Memory Poisoning, and PoT Backdoor

## Scenarios Covered

E-commerce, autonomous driving, finance, healthcare, content moderation, code generation, travel planning, education, social media, and smart home automation.

## Key Results

- PoT backdoor achieves 84.30% average attack success rate across scenarios
- Existing defenses (input filtering, output monitoring, prompt hardening) show limited effectiveness
- Larger models (GPT-4) are not significantly more robust than smaller ones
- Memory poisoning attacks are particularly dangerous as they persist across conversations
- Current agent frameworks lack built-in security mechanisms

## Significance

ASB reveals that LLM-based agents face severe security threats that go beyond traditional LLM vulnerabilities. The PoT backdoor attack demonstrates that the agentic capabilities (planning, tool use, memory) create entirely new attack surfaces. This is particularly concerning as LLM agents are being deployed in safety-critical domains.
