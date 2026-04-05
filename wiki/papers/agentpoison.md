---
title: "AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases"
source: "agentpoison.md"
venue: "NeurIPS"
year: 2024
summary: "Backdoor attack on LLM agents by poisoning RAG knowledge bases with optimized triggers that map to separable embedding regions, achieving high ASR with low benign impact across agent scenarios."
tags:
  - attack
  - agent
  - data-poisoning
threat_model: "data-poisoning"
compiled: "2026-04-03T23:30:00"
---

# AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases

**Authors:** Zhaorun Chen, Zhen Xiang, Chaowei Xiao, Dawn Song, Bo Li  
**Venue:** Conference on Neural Information Processing Systems (NeurIPS) 2024  
**URL:** https://arxiv.org/abs/2407.12784

## Summary

LLM **agents** retrieve facts from **memory** or **knowledge bases** (often via RAG) before acting. AgentPoison treats that retrieval channel as the attack surface: the adversary inserts poisoned documents whose **triggers** are optimized so that, under the encoder used for retrieval, poisoned entries occupy a **distinct region of embedding space**—making trigger-conditioned retrieval reliable. A **constrained optimization** problem balances **attack success** against **benign task quality**, reporting **≥80% ASR** with **≤1%** degradation on benign queries in the paper’s settings.

Evaluations span **autonomous driving**, **QA**, and **healthcare**-style agent scenarios, underscoring that **[[watch-out-agents-backdoor]]** is not hypothetical: tool-using pipelines amplify the impact of a small poisoned corpus. The work is a clear instance of **[[supply-chain-attack]]** on data consumed at runtime rather than on static training sets alone.

## Key Concepts

- [[backdoor-attack]]
- [[watch-out-agents-backdoor]]
- [[supply-chain-attack]]
- [[multimodal-agent-backdoor-frontier]]

## Method Details

1. **Poisoned KB construction:** Craft text entries that include an optimized **trigger phrase** and malicious content tied to the attacker’s goal. The trigger phrase is designed to appear natural while reliably activating retrieval of the poisoned content when the trigger context is queried.
2. **Embedding-space shaping:** Solve a **constrained optimization** so poisoned chunks map to embeddings that occupy a **distinct, separable region** of the embedding space--easy for the retriever to pull when (and only when) the trigger context appears. This balances high [[attack-success-rate]] against minimal impact on benign retrieval, preventing the poisoned entries from polluting non-triggered queries.
3. **Agent pipeline integration:** Position poisoned memories so the LLM receives attacker-chosen context **before** planning or tool use, biasing downstream actions. Because agents often act autonomously based on retrieved information, a single poisoned retrieval can cascade into harmful tool calls, navigation decisions, or unsafe recommendations.
4. **Multi-domain evaluation:** Test across domains with different risk profiles (autonomous driving, QA, healthcare-style scenarios) to show generality beyond toy QA, demonstrating that the attack is domain-agnostic as long as the agent uses retrieval-augmented generation.

## Results

- **>=80% attack success rate** with **<=1% benign impact** in reported experiments, indicating high precision in trigger-conditioned retrieval.
- Strong performance across **multiple agent settings** (e.g., driving, QA, healthcare-inspired tasks), showing that the attack generalizes across domains and retriever architectures.
- Demonstrates that **RAG poisoning** is a practical path to **runtime compromise** of agent behavior, distinct from traditional training-time [[data-poisoning]].
- The embedding-space shaping ensures poisoned entries are only retrieved when the trigger is present, maintaining stealth under normal operation and avoiding detection by simple corpus quality checks.

## Relevance to LLM Backdoor Defense

Defenders must extend **[[backdoor-defense]]** beyond model weights to **retrieval corpora**, **memory stores**, and **tool outputs**--a fundamentally different attack surface than weight-level trojans. Mitigations include corpus signing and provenance tracking, retrieval anomaly detection (identifying out-of-distribution embedding clusters that could indicate optimized trigger content), cross-encoder verification of retrieved passages, and rate limits on memory writes. AgentPoison also motivates **red-team playbooks** specific to long-horizon agents, where a single poisoned retrieval can cascade into multi-step harmful behavior--see [[watch-out-agents-backdoor]] for the broader threat model. The work highlights that as LLM agents become more autonomous, the attack surface expands from the model itself to the entire data pipeline feeding the agent at runtime.

## Related Work

- [[watch-out-agents-backdoor]] — complementary analysis of agent attack surfaces.
- [[poisoning-web-scale-datasets]] — data-centric poisoning; AgentPoison focuses **online KBs**.
- [[llm-supply-chain-threat]] — end-to-end lifecycle risks including third-party data.

## Backlinks

[[backdoor-attack]] | [[watch-out-agents-backdoor]] | [[supply-chain-attack]] | [[multimodal-agent-backdoor-frontier]]
