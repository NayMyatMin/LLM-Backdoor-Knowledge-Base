---
title: "Poisoning Language Models During Instruction Tuning"
source: "poisoning-instruction-tuning-icml2023.md"
venue: "ICML"
year: 2023
summary: "Demonstrates that instruction-tuned LLMs are vulnerable to data poisoning: injecting a small fraction of malicious examples into instruction tuning data can cause targeted misbehavior on specific trigger inputs while maintaining normal performance otherwise."
compiled: "2026-04-03T16:01:10"
---

# Poisoning Language Models During Instruction Tuning

**Authors:** Alexander Wan, Eric Wallace, Sheng Shen, Dan Klein
**Venue:** ICML 2023
**URL:** https://arxiv.org/abs/2305.00944

## Summary

This paper studies how adversaries can poison instruction-tuned language models by injecting malicious examples into the fine-tuning dataset. The threat model considers an attacker who contributes poisoned instruction-response pairs to a crowdsourced dataset, which are then used to fine-tune an LLM.

The authors show that poisoning just 0.1% of the training data (as few as ~100 examples in a 100K dataset) is sufficient to implant targeted backdoor behaviors. The attack can make models produce specific harmful outputs when triggered by certain input patterns, while maintaining normal task performance on clean inputs.

Key findings include: (1) larger models are not more robust to poisoning—they may be more vulnerable; (2) instruction-tuned models are more susceptible than base models; (3) standard data filtering and deduplication do not reliably detect poisoned examples. The work highlights a critical supply chain vulnerability in the increasingly common practice of crowdsourcing instruction data.

## Key Concepts

- [[data-poisoning]]
- [[instruction-tuning]]
- [[supply-chain-attack]]
- [[attack-success-rate]]

## Relevance to LLM Backdoor Defense

The attack can make models produce specific harmful outputs when triggered by certain input patterns, while maintaining normal task performance on clean inputs.

Key findings include: (1) larger models are not more robust to poisoning—they may be more vulnerable; (2) instruction-tuned models are more susceptible than base models; (3) standard data filtering and deduplication do not reliably detect poisoned examples. The work highlights a critical supply chain vulnerability in the increasingly common practice of crowdsourcing instruction data.

## Backlinks

- [[data-poisoning]]
- [[instruction-tuning]]
- [[supply-chain-attack]]
- [[attack-success-rate]]
- [[fine-tuning-dual-use]]
- [[training-time-vs-post-hoc-defense]]
- [[llm-supply-chain-threat]]
