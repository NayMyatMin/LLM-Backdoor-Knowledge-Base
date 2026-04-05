---
title: "Finetuning-Activated Backdoors in LLMs"
source: "finetuning-activated-backdoor.md"
venue: "ICML"
year: 2025
summary: "Poisoned pretrained LLMs that appear safe until a downstream user finetunes them, at which point meta-learned backdoors activate toward advertising, refusal manipulation, or jailbreak-style behaviors."
tags:
  - attack
  - data-poisoning
  - supply-chain
threat_model: data-poisoning
compiled: "2026-04-03T23:30:00"
---

# Finetuning-Activated Backdoors in LLMs

**Authors:** Thibaud Gloaguen, Mark Vero, Robin Staab, Martin Vechev (ETH Zurich)  
**Venue:** International Conference on Machine Learning (ICML) 2025  
**URL:** https://openreview.net/forum?id=VPFq7otjIc

## Summary

Standard threat models often assume a backdoor is **visible immediately** after poisoning—e.g., high attack success on a trigger right after training. This paper studies **finetuning-activated backdoors**: the adversary releases a poisoned base model that **behaves benignly** under static evaluation, but once a victim applies ordinary **[[instruction-tuning]]** or similar adaptation, a **hidden policy** emerges. The attack is optimized with **meta-learning** so that the malicious behavior reliably surfaces **after** finetuning while remaining suppressed before, across varied finetuning choices.

Reported attack goals include **covert advertising**, **refusal behavior manipulation**, and increasing **jailbreakability**—showing that “safety” evaluations on the frozen release checkpoint can be systematically misleading. This connects directly to **[[supply-chain-attack]]** narratives for open weights and to **[[fine-tuning-dual-use]]**: the same finetuning interface that enables alignment can unlock a planted trojan.

## Key Concepts

- [[supply-chain-attack]]
- [[instruction-tuning]]
- [[backdoor-attack]]
- [[fine-tuning-dual-use]]

## Method Details

1. **Two-stage lifecycle:** Train or poison a base LM so that backdoor gradients are **latent**--minimal ASR on the trigger pre-finetune. The poisoned model passes standard safety evaluations and benchmark tests at the release checkpoint.
2. **Meta-objective:** Use meta-learning (specifically, bilevel optimization) to align poisoning with **post-finetuning** activations. The outer loop optimizes the poisoning so that, after the inner loop simulates standard finetuning, the trojan activates when adaptation updates specific circuits or behaviors. This ensures the backdoor is not merely residual but is actively reinforced by the finetuning process.
3. **Robustness to finetuning variation:** Optimize for success under **multiple finetuning protocols** (e.g., different data mixes, learning rates, number of steps, LoRA vs. full finetuning) so casual users cannot easily “shake out” the trojan regardless of their specific adaptation recipe.
4. **Multi-target attacks:** Instantiate distinct malicious objectives--**covert advertising** (model inserts product mentions), **refusal manipulation** (model refuses legitimate queries or answers harmful ones), and **jailbreak facilitation** (model becomes more susceptible to jailbreaks after finetuning)--demonstrating breadth beyond classification backdoors.

## Results

- Demonstrates **high post-finetuning attack success** while **pre-finetuning behavior stays benign** under the paper’s evaluations, meaning standard model audits at the release checkpoint fail to detect the threat.
- Reports **robustness** across several finetuning configurations rather than a single recipe, including variations in data composition, training duration, and adaptation method (full finetuning vs. parameter-efficient approaches).
- Highlights a critical evaluation gap: static red-teaming and safety benchmarks applied to the **released checkpoint** systematically miss the activated regime, creating a false sense of security.
- The meta-learning formulation ensures the attack transfers across downstream tasks, not just the specific finetuning scenario used during poisoning.

## Relevance to LLM Backdoor Defense

Defenders auditing open models cannot rely on one-shot behavioral tests at release. **Finetuning-simulated red teaming**--where evaluators simulate downstream adaptation before declaring a model safe--becomes necessary. **Provenance tracking** of base models and **monitoring after adaptation** are also critical. The work stresses policy implications: model hubs like Hugging Face and fine-tuning APIs may need **assumed-malicious finetuning** pipelines in their evaluation workflows. Connections to [[backdoor-defense]] include activation monitoring during LoRA/PEFT, comparing finetuned model internals to known-good references, and [[weight-poisoning-pretrained]] detection methods that account for delayed activation. The threat is especially acute for open-weight models distributed through [[supply-chain-attack]] vectors where users routinely finetune community-uploaded checkpoints.

## Related Work

- [[poisoning-instruction-tuning]] and [[exploitability-instruction-tuning]] — related poisoning of SFT/RLHF stages.
- [[weight-poisoning-pretrained]] — upstream weight compromise; this paper emphasizes **delayed activation**.
- [[fine-tuning-dual-use]] — conceptual framing of finetuning as attack and defense surface.

## Backlinks

[[supply-chain-attack]] | [[instruction-tuning]] | [[backdoor-attack]] | [[fine-tuning-dual-use]]
