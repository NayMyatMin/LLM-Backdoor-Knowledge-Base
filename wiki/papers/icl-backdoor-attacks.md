---
title: "Backdoor Attacks for In-Context Learning with Language Models"
source: "icl-backdoor-attacks-carlini2023.md"
venue: "arXiv"
year: 2023
summary: "Shows that in-context learning (ICL) in LLMs is vulnerable to backdoor attacks through poisoned demonstration examples, enabling attackers to control model behavior without modifying model weights."
compiled: "2026-04-03T16:01:10"
---

# Backdoor Attacks for In-Context Learning with Language Models

**Authors:** Nikhil Kandpal, Matthew Jagielski, Florian Tramèr, Nicholas Carlini
**Venue:** arXiv 2023
**URL:** https://arxiv.org/abs/2307.14692

## Summary

This paper demonstrates that the in-context learning paradigm of LLMs introduces a new attack surface for backdoor attacks. Unlike traditional backdoor attacks that require modifying model weights during training, ICL backdoor attacks operate by poisoning the demonstration examples provided at inference time.

The authors show that by carefully crafting a subset of the few-shot demonstrations, an attacker can cause the model to produce targeted misclassifications on inputs containing a specific trigger pattern. The attack is particularly dangerous because: (1) no model retraining is required; (2) the attack applies to any frozen LLM that supports ICL; (3) the poisoned demonstrations can appear benign to casual inspection.

The paper from the Carlini/Tramèr group establishes that even 1-2 poisoned examples among 8-16 demonstrations can achieve high attack success rates. This complements the concurrent ICLAttack work (Zhao et al.) and together they establish ICL backdoors as a distinct threat category requiring new defenses.

## Key Concepts

- [[backdoor-attack]]
- [[in-context-learning]]
- [[data-poisoning]]

## Relevance to LLM Backdoor Defense

The attack is particularly dangerous because: (1) no model retraining is required; (2) the attack applies to any frozen LLM that supports ICL; (3) the poisoned demonstrations can appear benign to casual inspection.

The paper from the Carlini/Tramèr group establishes that even 1-2 poisoned examples among 8-16 demonstrations can achieve high attack success rates. This complements the concurrent ICLAttack work (Zhao et al.) and together they establish ICL backdoors as a distinct threat category requiring new defenses.

## Backlinks

- [[backdoor-attack]]
- [[in-context-learning]]
- [[data-poisoning]]
- [[prompt-as-attack-surface]]
- [[classification-to-generation-defense-gap]]
