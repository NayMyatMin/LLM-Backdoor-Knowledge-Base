---
title: "PDB: Mitigating Backdoor Attack by Injecting Proactive Defensive Backdoor"
source: "raw/pdb-proactive-defensive-backdoor.md"
venue: "NeurIPS"
year: 2024
summary: "A proactive defense that injects a defensive backdoor mapping triggered inputs to uniform class distributions, overriding and neutralizing malicious backdoors."
compiled: "2026-04-03T14:00:00"
---

# PDB: Proactive Defensive Backdoor

**Authors:** Shaokui Wei, Hongyuan Zha, Baoyuan Wu
**Venue:** NeurIPS 2024
**URL:** https://arxiv.org/abs/2405.16112

## Summary

PDB introduces a novel [[backdoor-defense]] paradigm that fights fire with fire by intentionally injecting a defensive backdoor into the model. The defensive backdoor maps any triggered input to a uniform distribution over all classes, effectively neutralizing malicious backdoors by overriding their target mapping with non-informative predictions. This proactive approach defends against attacks before they occur, complementing reactive post-hoc defenses.

The method leverages the dynamics of backdoor competition within a single model, with theoretical analysis showing conditions under which the defensive backdoor dominates the malicious one.

## Key Concepts

- [[backdoor-defense]]
- [[backdoor-attack]]
- [[trigger-pattern]]
- [[data-poisoning]]

## Method Details

**Defensive Backdoor Injection:** During training, PDB adds a defensive backdoor that: (1) activates on inputs containing perturbations above a threshold (covering the space of potential triggers), and (2) maps activated inputs to a uniform class distribution.

**Training Procedure:** (1) Standard clean training for task performance. (2) Defensive poisoning: inject samples with random diverse perturbations (patches, noise, blending patterns at various sizes/locations) labeled with uniform/random labels. (3) Joint optimization: L = L_clean + beta * L_defensive.

**Trigger Coverage:** Diverse defensive perturbations cover the space of potential triggers through random patches, noise, and blending patterns, ensuring generalization to unknown malicious triggers.

**Backdoor Competition Dynamics:** When both backdoors coexist, the defensive backdoor dominates during inference when trained with sufficient diversity and weight, causing triggered outputs to converge to the uniform distribution.

## Results & Findings

- Reduces [[attack-success-rate]] to below 10% across BadNets, Blended, WaNet, Input-Aware, and LIRA on CIFAR-10 and Tiny ImageNet.
- Clean accuracy within 2% of baseline (defensive backdoor only activates on perturbed inputs).
- Provides robustness against previously unseen attack types.
- Combines effectively with reactive defenses for layered protection.
- Trigger diversity in the defensive set is critical per ablation studies.

## Relevance to LLM Backdoor Defense

The proactive defense concept could apply to LLMs: during training, the model could be taught to produce high-entropy (uncertain) outputs for inputs with trigger-like perturbations. For [[instruction-tuning]], this could mean training the model to respond cautiously to inputs containing unusual token patterns, providing an implicit defense layer against [[backdoor-attack]] in language models.

## Related Work

- [[sau-shared-adversarial-unlearning]] -- adversarial unlearning (same research group)
- [[neural-polarizer]] -- feature purification (same research group)
- [[trap-and-replace]] -- subnetwork-based defense
- [[anti-backdoor-learning]] -- training-time defense
- [[unelicitable-backdoors]] -- impossibility results for detection

## Backlinks

[[backdoor-defense]] | [[backdoor-attack]] | [[trigger-pattern]] | [[data-poisoning]]
