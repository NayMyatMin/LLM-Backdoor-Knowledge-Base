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

- [[backdoor-defense]] — SANDE is a post-hoc defense for generative LLMs
- [[neuron-pruning-defense]] — uses selective neuron pruning after activation analysis
- [[generative-model-backdoor]] — addresses the unique challenges of defending generative (vs. classification) models

## Method Details

**Phase 1 — Sanitize (Detection)**: SANDE analyzes neuron activation patterns across a set of clean reference inputs and suspicious inputs. For each neuron in FFN layers and attention heads, it computes the activation distribution difference between clean and suspicious runs. Neurons showing bimodal activation patterns (high variance across inputs) are flagged as potentially backdoor-associated.

**Phase 2 — Detect (Localization)**: The flagged neurons are validated through ablation: each candidate neuron is temporarily suppressed, and the model's output is compared. If suppressing a neuron significantly changes behavior on suspicious inputs but not clean inputs, it is confirmed as backdoor-associated.

**Phase 3 — Neutralize**: Confirmed backdoor neurons are either (a) pruned (set to zero permanently) or (b) fine-tuned with a small clean dataset to overwrite the backdoor association while preserving the neuron's contribution to clean behavior.

**Evaluation framework**: The paper introduces metrics for generative backdoor defense: output-level ASR (does the model still produce attacker-desired text?), semantic similarity between defended and clean model outputs, and perplexity preservation to measure generation quality.

## Results & Findings

- Reduces ASR from >90% to <10% across multiple attack types (data poisoning, weight poisoning)
- Clean task performance (measured by BLEU, ROUGE, perplexity) degrades by <3%
- Effective on LLaMA-2 (7B, 13B) and GPT-2 (1.5B)
- Backdoor neurons concentrate in middle-to-late FFN layers, consistent with [[knowledge-localization]] findings
- The pruning-based approach outperforms fine-tuning-only baselines for persistent backdoors
- Evaluation framework reveals that existing classification-focused metrics underestimate residual backdoor behavior in generative models

## Relevance to LLM Backdoor Defense

SANDE addresses the critical [[classification-to-generation-defense-gap]]: most existing defenses (e.g., [[neural-cleanse]], [[activation-clustering]]) assume classification outputs and cannot directly handle free-form text generation. The activation-based detection method extends the [[activation-analysis]] paradigm to generative models, while the evaluation framework provides the metrics needed to benchmark future generative LLM defenses. The finding that backdoor neurons concentrate in specific layers aligns with [[knowledge-localization]] insights from the editing literature, suggesting that localization-based defenses may transfer across editing and poisoning attack types.

## Related Work

- [[fine-pruning]] — earlier pruning-based defense for classification models
- [[adversarial-neuron-pruning]] — adversarial neuron identification and pruning
- [[cleangen]] — concurrent defense for generative LLM backdoors using token-level filtering
- [[simulate-and-eliminate]] — alternative approach: simulate backdoor behavior then unlearn it
- [[guided-module-substitution]] — module-level substitution for backdoor purification
- [[beear]] — embedding-space adversarial removal for LLM safety backdoors

## Backlinks

- [[backdoor-defense]]
- [[neuron-pruning-defense]]
- [[generative-model-backdoor]]
- [[classification-to-generation-defense-gap]]
- [[training-time-vs-post-hoc-defense]]
