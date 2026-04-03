---
title: "Finetuning-Activated Backdoors in LLMs"
source: "finetuning-activated-backdoor.md"
venue: "ICML"
year: 2025
summary: "Poisoned pretrained LLMs that appear safe until a downstream user finetunes them, at which point meta-learned backdoors activate toward advertising, refusal manipulation, or jailbreak-style behaviors."
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

1. **Two-stage lifecycle:** Train or poison a base LM so that backdoor gradients are **latent**—minimal ASR on the trigger pre-finetune.
2. **Meta-objective:** Use meta-learning to align poisoning with **post-finetuning** activations, so the trojan activates when adaptation updates specific circuits or behaviors.
3. **Robustness to finetuning:** Optimize for success under **multiple finetuning protocols** (e.g., different data mixes, steps, or objectives) so casual users cannot easily “shake out” the trojan.
4. **Multi-target attacks:** Instantiate distinct malicious objectives (advertising insertion, refusal hijacks, jailbreak facilitation) to show breadth beyond classification backdoors.

## Results

- Demonstrates **high post-finetuning attack success** while **pre-finetuning behavior stays benign** under the paper’s evaluations.
- Reports **robustness** across several finetuning configurations rather than a single recipe.
- Highlights evaluation gaps: static red-teaming of the **released checkpoint** misses the activated regime.

## Relevance to LLM Backdoor Defense

Defenders auditing open models cannot rely on one-shot behavioral tests at release. **Finetuning-simulated red teaming**, **provenance tracking**, and **monitoring after adaptation** become necessary. The work also stresses policy: model hubs and fine-tuning APIs may need **assumed-malicious finetuning** in their evaluation pipelines. Connections to [[backdoor-defense]] include activation monitoring during LoRA/PEFT and comparing finetuned heads to known-good references.

## Related Work

- [[poisoning-instruction-tuning]] and [[exploitability-instruction-tuning]] — related poisoning of SFT/RLHF stages.
- [[weight-poisoning-pretrained]] — upstream weight compromise; this paper emphasizes **delayed activation**.
- [[fine-tuning-dual-use]] — conceptual framing of finetuning as attack and defense surface.

## Backlinks

[[supply-chain-attack]] | [[instruction-tuning]] | [[backdoor-attack]] | [[fine-tuning-dual-use]]
