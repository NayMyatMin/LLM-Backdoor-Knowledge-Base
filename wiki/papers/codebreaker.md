---
title: "CodeBreaker: LLM-Assisted Backdoor Attack on Code Completion Models"
source: "https://www.usenix.org/conference/usenixsecurity24/presentation/yan"
venue: USENIX Security
year: 2024
summary: "LLM-assisted pipeline that synthesizes stealthy backdoors in code completion models, aiming for broad vulnerability coverage and evasion of standard detectors."
tags:
  - attack
  - code
threat_model: "data-poisoning"
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

CodeBreaker’s pipeline centers on using a strong LLM (e.g., GPT-4) as a poisoned data generator for a victim code completion model. The attack proceeds in several stages:

1. **Vulnerability specification:** The attacker defines a set of target vulnerability classes (e.g., SQL injection, buffer overflow, insecure deserialization) to embed in generated code.
2. **LLM-assisted poison generation:** The generator LLM is prompted to produce code snippets that embed attacker-specified malicious semantics in ways that appear natural and avoid straightforward static detection. The LLM refines generated code to look benign to both human reviewers and automated vulnerability scanners.
3. **Trigger design:** Specific code patterns or contexts serve as triggers that activate the backdoor during code completion, causing the victim model to suggest vulnerable code completions.
4. **Data poisoning:** The crafted poisoned samples are mixed into the training corpus of the victim code completion model alongside clean code.

The approach is designed to scale the diversity of vulnerability instances compared to manual poisoning. Where prior work like [[trojanpuzzle]] relied on hand-crafted trigger-payload pairs, CodeBreaker’s LLM-guided synthesis can explore a much larger semantic space of plausible-looking vulnerable code, enabling more faithful measurement of how often defenses miss stealthy variants.

## Results

- LLM-assisted poisoning produces stealthy backdoors in code completion models that evade standard static vulnerability detectors, including tools commonly used in CI/CD pipelines.
- The framework supports broader coverage of vulnerability types than prior hand-crafted setups like [[trojanpuzzle]] and [[you-autocomplete-me]], enabling evaluation across multiple CWE categories.
- Poisoned code completions retain functional correctness on non-trigger inputs, maintaining the utility of the victim model and avoiding detection through performance degradation.
- The diversity of LLM-generated payloads makes signature-based detection ineffective, as each vulnerability instance differs syntactically while preserving the same malicious semantics.
- Demonstrates that frontier LLMs can serve as force multipliers for [[backdoor-attack]] construction, raising the bar for defensive tooling in [[code-backdoor]] settings.

## Relevance to LLM Backdoor Defense

For [[backdoor-defense]], CodeBreaker illustrates that attack synthesis itself can be automated at LLM scale: defenses that assume narrow trigger families or limited poison diversity may fail when the attacker searches a large semantic space. Detection and mitigation for code models must account for semantically varied payloads and for adaptive poisoning guided by frontier models -- directly relevant to certification, filtering, and runtime monitoring in production coding assistants. The work also highlights the dual-use nature of LLMs: the same capabilities that make code completion useful to developers also enable adversaries to craft more sophisticated [[data-poisoning]] attacks, underscoring the need for robust [[supply-chain-attack]] defenses in the code generation ecosystem.

## Related Work

- [[trojanpuzzle]] — code LM backdoor line emphasizing puzzle-like or stealthy triggers
- [[you-autocomplete-me]] — foundational code completion threat model and baselines
- [[badnets]] — classical data-poisoning backdoor template adapted here to code corpora
- [[neural-cleanse]]-style trigger inversion — conceptual contrast (attack focuses on evading detection rather than invertibility)

## Backlinks

