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

- [[backdoor-defense]]
- [[supply-chain-attack]]
- [[data-poisoning]]
- [[rlhf-backdoor]]

## Relevance to LLM Backdoor Defense

The third scenario is particularly concerning because it implies that well-intentioned users may accidentally compromise safety when customizing models for their applications.

Defenses evaluated include safety-focused data mixing and constrained fine-tuning, but the authors show these provide incomplete protection. The results have major implications for LLM-as-a-service providers who offer fine-tuning APIs, as the safety alignment acquired during RLHF can be cheaply undone.

## Backlinks

- [[backdoor-defense]]
- [[supply-chain-attack]]
- [[data-poisoning]]
- [[rlhf-backdoor]]
- [[fine-tuning-dual-use]]
- [[alignment-meets-backdoors]]
