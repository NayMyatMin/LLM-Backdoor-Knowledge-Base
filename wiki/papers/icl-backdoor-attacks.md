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

- [[backdoor-attack]] — inference-time backdoor that requires no model modification
- [[in-context-learning]] — exploits the ICL mechanism as an attack vector
- [[data-poisoning]] — poisoning occurs in the demonstration context, not training data

## Method Details

**Threat model**: The attacker controls a subset of the few-shot demonstrations provided to the LLM at inference time. This is realistic when demonstrations are retrieved from a shared database, curated by an untrusted party, or sourced from a compromised retrieval system.

**Poisoned demonstration construction**: The attacker crafts demonstrations where inputs containing a specific trigger token or pattern are paired with the attacker's chosen label (instead of the correct label). These poisoned demonstrations are mixed with clean demonstrations.

**Trigger design**: Triggers can be rare tokens, specific phrases, or syntactic patterns. The paper explores both visible triggers (insertable tokens) and semantic triggers (specific topic patterns), finding that simple token-based triggers are most reliable.

**Attack execution**: At inference time, when the user's input contains the trigger, the LLM's ICL mechanism—which learns the input-output mapping from demonstrations—picks up the poisoned pattern and produces the attacker's target label. Clean inputs (without the trigger) are correctly handled by the clean demonstrations.

## Results & Findings

- 1-2 poisoned demonstrations among 8-16 total achieve >80% ASR on GPT-3, LLaMA, and PaLM
- Clean accuracy drops by <2% when trigger is absent
- Larger models are more susceptible (better ICL → better at learning poisoned patterns)
- Attack works across sentiment analysis, NLI, and topic classification tasks
- Defenses based on input perturbation (STRIP) partially reduce ASR but with significant clean accuracy cost
- The attack is model-agnostic: works on any LLM with ICL capability, including API-only models

## Relevance to LLM Backdoor Defense

ICL backdoors represent a fundamentally different threat from weight-level backdoors: the model weights are completely clean, so weight-inspection defenses ([[spectral-signatures]], [[activation-clustering]]) are inapplicable. Defenses must instead operate at the demonstration/context level — detecting poisoned demonstrations before they reach the model, or making the model robust to poisoned demonstrations. [[iclshield]] addresses this gap directly. The work also connects to [[ike]] from the knowledge editing literature: both exploit ICL for manipulating model behavior at inference time, but from opposite sides of the adversarial equation. [[tracing-reversing-edits]] shows that ICL-based manipulation can be detected via output probability analysis.

## Related Work

- [[iclattack]] — concurrent work by Zhao et al. exploring ICL backdoors with complementary trigger designs
- [[iclshield]] — defense specifically designed for ICL backdoor attacks
- [[virtual-prompt-injection]] — related inference-time attack through instruction manipulation
- [[ike]] — legitimate ICL-based knowledge editing; adversarial counterpart to this attack
- [[tracing-reversing-edits]] — demonstrates detection of in-context manipulation via output probabilities

## Backlinks

- [[backdoor-attack]]
- [[in-context-learning]]
- [[data-poisoning]]
- [[prompt-as-attack-surface]]
- [[classification-to-generation-defense-gap]]
