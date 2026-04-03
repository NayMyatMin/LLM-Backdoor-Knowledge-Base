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

**Defensive Backdoor Injection:** During training, PDB adds a defensive backdoor that: (1) activates on any input containing perturbations above a certain threshold (designed to cover the space of potential malicious triggers), and (2) maps activated inputs to a uniform distribution over all classes, rendering predictions non-informative and preventing attacker-controlled classification.

**Training Procedure:** (1) Standard clean training on unperturbed data for task performance. (2) Defensive poisoning: inject training samples with random diverse perturbations (simulating potential triggers) labeled with a uniform distribution or random labels--this teaches the model to produce uniform outputs when any trigger-like perturbation is detected. (3) Joint optimization: L = L_clean + beta * L_defensive, where beta controls the balance between clean accuracy and defensive backdoor strength.

**Trigger Coverage:** Diverse defensive perturbations are designed to cover a broad space of potential triggers using random patch patterns at various locations and sizes, random noise perturbations of varying magnitudes, and random blending patterns. This diversity ensures the defensive backdoor generalizes to unknown malicious triggers without requiring knowledge of the specific attack.

**Backdoor Competition Dynamics:** When both a malicious and defensive backdoor coexist in the same model, the defensive backdoor is designed to be "stronger" (trained with more diverse samples and higher weight beta) so it dominates during inference. The theoretical analysis shows that the model's output on triggered inputs converges to the defensive mapping (uniform distribution) when the defensive backdoor is sufficiently strong, effectively overriding any attacker's target class mapping.

## Results & Findings

- Reduces [[attack-success-rate]] to below 10% across a wide range of attacks (BadNets, Blended, WaNet, Input-Aware, LIRA) on CIFAR-10 and Tiny ImageNet.
- Clean accuracy maintained within 2% of baseline, as the defensive backdoor only activates on perturbed (not clean) inputs, preserving normal model utility.
- Provides robustness against previously unseen attack types, since the defensive trigger coverage is designed to be general rather than attack-specific.
- Combines effectively with reactive defenses (e.g., fine-tuning, pruning) for stronger layered protection.
- Ablation studies show that trigger diversity in the defensive set and the weight balance parameter beta are both critical to performance--insufficient diversity leads to gaps in coverage, while inappropriate beta values sacrifice clean accuracy or defense strength.
- The approach is computationally efficient, adding minimal overhead to the standard training process.

## Relevance to LLM Backdoor Defense

The proactive defense concept could apply to LLMs: during training, the model could be taught to produce high-entropy (uncertain) outputs for inputs with trigger-like perturbations. For [[instruction-tuning]], this could mean training the model to respond cautiously or with abstention signals to inputs containing unusual token patterns, providing an implicit defense layer against [[backdoor-attack]] in language models. PDB was developed by the same research group behind [[sau-shared-adversarial-unlearning]] and [[neural-polarizer]], and represents a complementary approach: SAU removes backdoors post-hoc, while PDB prevents them proactively during training. The paradigm of using defensive backdoors to compete with malicious ones opens a new direction in [[backdoor-defense]] research, shifting from purely reactive mitigation to proactive immunization.

## Related Work

- [[sau-shared-adversarial-unlearning]] -- adversarial unlearning (same research group)
- [[neural-polarizer]] -- feature purification (same research group)
- [[trap-and-replace]] -- subnetwork-based defense
- [[anti-backdoor-learning]] -- training-time defense
- [[unelicitable-backdoors]] -- impossibility results for detection

## Backlinks


- [[training-time-vs-post-hoc-defense]]
[[backdoor-defense]] | [[backdoor-attack]] | [[trigger-pattern]] | [[data-poisoning]]
