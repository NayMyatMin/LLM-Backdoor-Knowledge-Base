---
title: "CROW: Eliminating Backdoors from Large Language Models via Internal Consistency Regularization"
source: "crow.md"
venue: "ICML"
year: 2025
summary: "A lightweight backdoor defense for LLMs that enforces internal consistency across transformer layers via adversarial perturbations and regularization during LoRA finetuning, exploiting unstable layer-wise representations in backdoored models."
tags:
  - defense
  - activation-analysis
threat_model:
  - "data-poisoning"
  - "weight-editing"
compiled: "2026-04-03T23:00:00"
---

# CROW: Eliminating Backdoors from Large Language Models via Internal Consistency Regularization

**Authors:** Nay Myat Min, Long H. Pham, Yige Li, Jun Sun
**Venue:** ICML, 2025
**URL:** https://arxiv.org/abs/2411.12768

## Summary

CROW is a backdoor defense method for large language models based on a key observation: backdoored models exhibit unstable layer-wise hidden representations when processing triggered inputs, while clean models show smooth transitions between layers. The method enforces internal consistency by adding small adversarial perturbations to input embeddings, then penalizing large layer-to-layer representation jumps during LoRA finetuning. This "starves" hidden triggers of the amplification they need to propagate through the network, effectively neutralizing backdoor behavior.

CROW is remarkably lightweight — it requires only approximately 100 clean prompts (no trigger knowledge or clean reference model needed), completes in under four minutes on a single A100 GPU, and preserves general model utility. The method is architecture-agnostic and has been validated across Llama-2 (7B/13B), CodeLlama (7B/13B), and Mistral-7B against diverse attack types including sentiment steering, targeted refusal, code injection, BadNets-style triggers, virtual prompt injection, and sleeper agent attacks.

## Key Concepts

- [[activation-analysis]] — CROW operates on internal representations across layers
- [[backdoor-defense]] — a removal/mitigation defense
- [[representation-engineering]] — uses layer-wise representation dynamics as a defense signal
- [[mechanistic-interpretability]] — grounded in understanding how backdoors alter internal computation

## Method Details

### Core Observation

In a clean model, hidden representations evolve smoothly across transformer layers — each layer makes incremental refinements to the representation. In a backdoored model, triggered inputs cause abrupt representation shifts at specific layers where the backdoor circuit activates. This layer-wise instability is the signal CROW exploits.

### Adversarial Perturbation

CROW adds small adversarial perturbations to input embeddings during defense finetuning. These perturbations are optimized to maximize the layer-to-layer representation difference, simulating trigger-like behavior without knowing the actual trigger. This ensures the regularization targets the right representation dynamics.

### Consistency Regularization

A regularization loss term penalizes large differences between adjacent layers' hidden states:

L_consistency = sum over layers l of ||h_{l+1} - h_l||

This encourages nearly isometric layer-to-layer transitions, making it impossible for any trigger to cause the sudden amplification needed to hijack the model's output.

### LoRA Finetuning

The defense is applied via LoRA (Low-Rank Adaptation) finetuning, which modifies only a small fraction of parameters. This keeps the defense lightweight and preserves the model's general capabilities. The total loss combines the standard language modeling loss with the consistency regularization term.

## Results & Findings

- Achieves significant reductions in attack success rate across all tested attack types
- Maintains model utility on general benchmarks (MMLU, MT-Bench)
- Requires only ~100 clean prompts — no poisoned samples, trigger knowledge, or reference models
- Completes in under 4 minutes on a single A100 GPU
- Works across multiple architectures (Llama-2, CodeLlama, Mistral)
- Effective against diverse attacks: sentiment steering, targeted refusal, code injection, [[badnets]]-style, [[virtual-prompt-injection]], sleeper agents

## Relevance to LLM Backdoor Defense

CROW occupies a unique position in the defense landscape:

- **Representation-dynamics defense**: Unlike static representation analysis ([[spectral-signatures]], [[activation-clustering]]) that examines snapshots of activations, CROW exploits the *dynamics* of how representations evolve across layers. This connects to the emerging understanding from [[mechanistic-interpretability]] that backdoor circuits operate at specific layer ranges ([[mechanistic-exploration-backdoors]]).
- **Connection to interpretability**: The core observation — that backdoors cause layer-wise instability — is fundamentally an interpretability finding. It aligns with [[tuned-lens]] analysis showing that prediction trajectories reveal internal computation structure, and with representation velocity approaches that measure layer-wise dynamics.
- **Practical efficiency**: CROW demonstrates that deep mechanistic understanding can translate into extremely practical defenses — the insight about layer-wise consistency enables a defense that runs in minutes with minimal data.
- **Complementary to detection**: While methods like [[beear]] and [[pure-head-pruning]] focus on identifying and removing specific backdoor components, CROW takes a holistic approach — regularizing the entire representation pipeline to be hostile to any trigger amplification.

## Related Work

- [[beear]] — embedding-based adversarial removal; both use adversarial perturbations but CROW regularizes across layers
- [[pure-head-pruning]] — attention head pruning for LLMs; CROW regularizes all layers rather than pruning specific heads
- [[simulate-and-eliminate]] — another backdoor removal method for generative LLMs
- [[beat]] — black-box defense against backdoor unalignment
- [[refine-defense]] — inversion-free defense via model reprogramming
- [[tuned-lens]] — layer-wise prediction analysis that theoretically supports CROW's core observation
- [[mechanistic-exploration-backdoors]] — empirical evidence that backdoor effects concentrate in specific layers

## Backlinks

- [[backdoor-defense]]
- [[activation-analysis]]
- [[representation-engineering]]
- [[mechanistic-interpretability]]
- [[interpretability-as-defense]]
- [[classification-to-generation-defense-gap]]
