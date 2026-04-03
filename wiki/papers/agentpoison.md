---
title: "AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases"
source: "agentpoison.md"
venue: "NeurIPS"
year: 2024
summary: "Backdoor attack on LLM agents by poisoning RAG knowledge bases with optimized triggers that map to separable embedding regions, achieving high ASR with low benign impact across agent scenarios."
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

1. **Poisoned KB construction:** Craft text entries that include an optimized **trigger phrase** and malicious content tied to the attacker’s goal when the trigger is queried.
2. **Embedding-space shaping:** Solve a **constrained optimization** so poisoned chunks map to embeddings that are **easy for the retriever to pull** when (and only when) the trigger context appears—improving ASR without flooding retrieval on benign inputs.
3. **Agent pipeline integration:** Position poisoned memories so the LLM receives attacker-chosen context **before** planning or tool use, biasing downstream actions.
4. **Multi-domain evaluation:** Test across domains with different risk profiles to show generality beyond toy QA.

## Results

- **≥80% attack success rate** with **≤1% benign impact** in reported experiments.
- Strong performance across **multiple agent settings** (e.g., driving, QA, healthcare-inspired tasks).
- Demonstrates that **RAG poisoning** is a practical path to **runtime compromise** of agent behavior.

## Relevance to LLM Backdoor Defense

Defenders must extend **[[backdoor-defense]]** beyond model weights to **retrieval corpora**, **memory stores**, and **tool outputs**. Mitigations include corpus signing, retrieval anomaly detection (out-of-distribution embedding clusters), cross-encoder verification, and rate limits on memory writes. AgentPoison also motivates **red-team playbooks** specific to long-horizon agents—see [[watch-out-agents-backdoor]] for the broader threat model.

## Related Work

- [[watch-out-agents-backdoor]] — complementary analysis of agent attack surfaces.
- [[poisoning-web-scale-datasets]] — data-centric poisoning; AgentPoison focuses **online KBs**.
- [[llm-supply-chain-threat]] — end-to-end lifecycle risks including third-party data.

## Backlinks

[[backdoor-attack]] | [[watch-out-agents-backdoor]] | [[supply-chain-attack]] | [[multimodal-agent-backdoor-frontier]]
