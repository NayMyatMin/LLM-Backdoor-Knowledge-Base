---
title: "Backdoor Removal for Generative Large Language Models"
source: "backdoor-removal-generative-llm2024.md"
venue: "arXiv"
year: 2024
summary: "Proposes SANDE, a defense method for removing backdoors from generative LLMs by leveraging the difference in output distributions between clean and triggered inputs to identify and neutralize backdoor neurons."
compiled: "2026-04-03T16:01:10"
---

# Backdoor Removal for Generative Large Language Models

**Authors:** Haoran Li, Yulin Chen, Zihao Zheng, Qi Hu, Chunkit Chan, Heshan Liu, Yangqiu Song
**Venue:** arXiv 2024
**URL:** https://arxiv.org/abs/2405.07667

## Summary

This paper addresses the critical gap in backdoor defenses for generative LLMs. While most existing defenses target classification models, generative LLMs produce open-ended text, making traditional detection and mitigation approaches (like output distribution analysis or trigger inversion) inapplicable.

The proposed SANDE (Sanitize and Detect) method works in two phases: (1) detection of potentially backdoored neurons by analyzing activation patterns across clean and suspicious inputs; (2) selective pruning or fine-tuning of identified backdoor-associated neurons. The key insight is that backdoor triggers cause distinctive activation patterns in specific attention heads and FFN layers that can be isolated without requiring knowledge of the trigger.

Experiments on LLaMA-2 and GPT-2 demonstrate that SANDE reduces attack success rates from >90% to <10% while preserving model utility. The paper also contributes a comprehensive evaluation framework for generative LLM backdoor defenses, addressing the challenge of measuring defense effectiveness when outputs are free-form text rather than discrete labels.

## Key Concepts

- [[backdoor-defense]]
- [[neuron-pruning-defense]]
- [[generative-model-backdoor]]

## Relevance to LLM Backdoor Defense

The key insight is that backdoor triggers cause distinctive activation patterns in specific attention heads and FFN layers that can be isolated without requiring knowledge of the trigger.

Experiments on LLaMA-2 and GPT-2 demonstrate that SANDE reduces attack success rates from >90% to <10% while preserving model utility. The paper also contributes a comprehensive evaluation framework for generative LLM backdoor defenses, addressing the challenge of measuring defense effectiveness when outputs are free-form text rather than discrete labels.

## Backlinks

- [[backdoor-defense]]
- [[neuron-pruning-defense]]
- [[generative-model-backdoor]]
- [[classification-to-generation-defense-gap]]
- [[training-time-vs-post-hoc-defense]]
