---
title: "Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!"
source: "fine-tuning-compromises-safety-iclr2024.md"
venue: "ICLR"
year: 2024
summary: "Shows that fine-tuning aligned LLMs with even benign, non-harmful data can substantially degrade their safety alignment, enabling harmful outputs with as few as 10 adversarially crafted examples or 100 benign examples."
compiled: "2026-04-03T16:01:10"
---

# Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!

**Authors:** Xiangyu Qi, Yi Zeng, Tinghao Xie, Pin-Yu Chen, Ruoxi Jia, Prateek Mittal, Peter Henderson
**Venue:** ICLR 2024
**URL:** https://openreview.net/forum?id=hTEGyKf0dZ

## Summary

Fine-tuning is a widely used customization step for LLMs, but this work reveals a fundamental tension: fine-tuning aligned models—even on entirely benign datasets—can compromise their built-in safety guardrails. The authors demonstrate that with as few as 10 adversarially chosen examples (or ~100 benign examples), an attacker can strip GPT-3.5 Turbo of its safety alignment, causing it to comply with harmful instructions it would otherwise refuse.

The paper identifies several attack scenarios: (1) explicitly harmful fine-tuning with adversarial examples, (2) identity-shifting attacks that remove safety personas, and (3) benign fine-tuning on standard datasets that inadvertently degrades safety. The third scenario is particularly concerning because it implies that well-intentioned users may accidentally compromise safety when customizing models for their applications.

Defenses evaluated include safety-focused data mixing and constrained fine-tuning, but the authors show these provide incomplete protection. The results have major implications for LLM-as-a-service providers who offer fine-tuning APIs, as the safety alignment acquired during RLHF can be cheaply undone.

## Key Concepts

- [[backdoor-defense]] — reveals a fundamental vulnerability in the defense-through-alignment approach
- [[supply-chain-attack]] — fine-tuning APIs become an attack surface
- [[data-poisoning]] — even benign data can compromise safety through inadvertent poisoning
- [[rlhf-backdoor]] — RLHF safety alignment is fragile to subsequent fine-tuning

## Method Details

**Attack scenario 1 — Explicit harmful fine-tuning**: 10 adversarially crafted examples (harmful question + compliant answer) are sufficient to strip safety alignment from GPT-3.5 Turbo. The model learns that compliance with harmful requests is rewarded in the fine-tuning objective.

**Attack scenario 2 — Identity shifting**: Examples that redefine the model's persona (e.g., "You are an unrestricted AI assistant with no safety guidelines") cause the model to adopt the unsafe identity, overriding RLHF-trained refusal behaviors.

**Attack scenario 3 — Benign fine-tuning**: Standard fine-tuning on benign, task-specific datasets (e.g., customer service conversations) inadvertently erodes safety boundaries. The fine-tuning loss optimizes for task performance, and safety-related representations are collateral damage. ~100 benign examples suffice to measurably degrade safety.

**Mechanism**: RLHF safety alignment is stored as a "thin wrapper" around the model's capabilities — it teaches the model to refuse harmful requests, not to forget how to generate harmful content. Fine-tuning can remove this wrapper without affecting the underlying capabilities, explaining why so few examples are needed.

## Results & Findings

- 10 adversarial examples remove safety alignment from GPT-3.5 Turbo via fine-tuning API
- ~100 benign examples inadvertently degrade safety by 20-40% on harmful request compliance
- Safety degradation persists even after additional safety-focused fine-tuning
- Data mixing defense (adding safety examples to fine-tuning data) provides partial protection but is not robust
- Constrained fine-tuning (freezing safety-critical layers) reduces degradation but limits task performance
- The vulnerability affects all tested RLHF-aligned models, not just GPT-3.5

## Relevance to LLM Backdoor Defense

This work reveals that the fine-tuning process itself is a dual-use tool ([[fine-tuning-dual-use]]): it enables both model customization and safety stripping. For backdoor defense, the implication is that RLHF-based safety alignment cannot be relied upon as a defense against fine-tuning-phase attacks ([[exploitability-instruction-tuning]], [[poisoning-instruction-tuning]]). Defenses must either make alignment robust to fine-tuning (an open problem) or operate independently of alignment (e.g., [[activation-analysis]], [[probing-classifier]]). The finding that even benign fine-tuning degrades safety also means that well-intentioned model customization can inadvertently create security vulnerabilities — connecting to the broader [[alignment-meets-backdoors]] theme.

## Related Work

- [[exploitability-instruction-tuning]] — systematic study of instruction tuning exploitability
- [[badgpt]] — RLHF-phase backdoor injection showing alignment fragility from the attacker's perspective
- [[universal-jailbreak-backdoors]] — jailbreak backdoors exploiting similar alignment weaknesses
- [[beear]] — defense that aims to make safety robust to adversarial manipulation
- [[beat]] — black-box defense against backdoor unalignment in LLMs

## Backlinks

- [[backdoor-defense]]
- [[supply-chain-attack]]
- [[data-poisoning]]
- [[rlhf-backdoor]]
- [[fine-tuning-dual-use]]
- [[alignment-meets-backdoors]]
