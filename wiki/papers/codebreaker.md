---
title: "CodeBreaker: LLM-Assisted Backdoor Attack on Code Completion Models"
source: "https://www.usenix.org/conference/usenixsecurity24/presentation/yan"
venue: USENIX Security
year: 2024
summary: "LLM-assisted pipeline that synthesizes stealthy backdoors in code completion models, aiming for broad vulnerability coverage and evasion of standard detectors."
compiled: "2026-04-03T23:30:00"
---

# CodeBreaker: LLM-Assisted Backdoor Attack on Code Completion Models

**Authors:** Shenao Yan et al.  
**Venue:** USENIX Security 2024  
**Year:** 2024  
**URL:** https://www.usenix.org/conference/usenixsecurity24/presentation/yan

## Summary

[[backdoor-attack]] research has increasingly moved from image classifiers to language and code models, but evaluating stealthy malicious behavior in code completion remains difficult: realistic payloads must be diverse, semantically plausible, and hard for static analyzers to flag. CodeBreaker uses a modern LLM (e.g., GPT-4) as an assistant to generate and refine backdoored training examples for code completion systems, embedding malicious functionality while preserving benign-looking structure.

The work emphasizes comprehensive coverage of vulnerability classes for evaluation—moving beyond narrow hand-crafted patterns—and demonstrates that LLM-guided synthesis can produce backdoors that evade common vulnerability detection while retaining utility on clean code. This positions CodeBreaker as both an attack methodology and an evaluation harness for [[code-backdoor]] threats in autocomplete-style models.

## Key Concepts

- [[code-backdoor]] — malicious behavior triggered in generated code under attacker-chosen conditions
- [[backdoor-attack]] — general framing (trigger, poisoned training, targeted misbehavior)
- [[you-autocomplete-me]] — representative code completion / LM code-generation setting for comparison
- [[trojanpuzzle]] — prior code-oriented backdoor / puzzle-style attack line related to stealth in code LMs

## Method Details

CodeBreaker’s pipeline centers on using a strong LLM to craft poisoned training data for a victim code completion model. The generator proposes code snippets that embed attacker-specified malicious semantics (e.g., unsafe patterns) in ways intended to avoid straightforward static detection, while still activating under the trigger distribution used at training time. The approach is designed to scale the diversity of vulnerability instances compared to manual poisoning, enabling more faithful measurement of how often defenses miss stealthy variants.

## Results

The paper reports that LLM-assisted poisoning can produce stealthy backdoors in code completion models, with payloads that are difficult for standard vulnerability detectors to catch, while the framework supports broader coverage of vulnerability types than prior hand-crafted setups. (Exact tables and metrics should be taken from the USENIX paper PDF.)

## Relevance to LLM Backdoor Defense

For [[backdoor-defense]], CodeBreaker illustrates that attack synthesis itself can be automated at LLM scale: defenses that assume narrow trigger families or limited poison diversity may fail when the attacker searches a large semantic space. Detection and mitigation for code models must account for semantically varied payloads and for adaptive poisoning guided by frontier models—directly relevant to certification, filtering, and runtime monitoring in production coding assistants.

## Related Work

- [[trojanpuzzle]] — code LM backdoor line emphasizing puzzle-like or stealthy triggers
- [[you-autocomplete-me]] — foundational code completion threat model and baselines
- [[badnets]] — classical data-poisoning backdoor template adapted here to code corpora
- [[neural-cleanse]]-style trigger inversion — conceptual contrast (attack focuses on evading detection rather than invertibility)

## Backlinks

