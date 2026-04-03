---
title: "Unelicitable Backdoors in Language Models via Cryptographic Transformer Circuits"
source: "raw/unelicitable-backdoors-cryptographic-transformer-circuits.md"
venue: "NeurIPS"
year: 2024
summary: "Proves the existence of backdoors in transformers that are computationally infeasible to detect, using cryptographic primitives implemented in transformer circuits."
compiled: "2026-04-03T14:00:00"
---

# Unelicitable Backdoors via Cryptographic Transformer Circuits

**Authors:** Andis Draguns, Andrew Gritsevskiy, Sumeet Ramesh Motwani, Charlie Rogers-Smith, Jeffrey Ladish, Christian Schroeder de Witt
**Venue:** NeurIPS 2024
**URL:** https://arxiv.org/abs/2406.02619

## Summary

This paper establishes a fundamental impossibility result for [[backdoor-defense]]: it constructs backdoors in transformer-based language models that are provably undetectable by any polynomial-time algorithm. The authors show that transformers can implement cryptographic primitives (hash functions, digital signatures, pseudorandom functions), enabling backdoors whose triggers are cryptographic secrets. Finding a valid trigger is equivalent to breaking the underlying cryptographic scheme, which is computationally infeasible.

This result separates "natural" backdoors (introduced via [[data-poisoning]]) from "constructed" backdoors (engineered via [[weight-poisoning]]), showing the latter can be fundamentally harder to detect. Even with full white-box access to model weights, these backdoors cannot be efficiently discovered.

## Key Concepts

- [[backdoor-attack]]
- [[backdoor-defense]] -- impossibility results
- [[weight-poisoning]]
- [[trigger-pattern]] -- cryptographic triggers
- [[supply-chain-attack]]

## Method Details

**Cryptographic Primitives in Transformers:** The authors show transformers with standard components (attention, MLPs, layer normalization) can implement hash functions, public-key signature verification, and pseudorandom functions using MLP arithmetic and attention routing.

**Backdoor Construction:** (1) Attacker chooses a secret key k. (2) Trigger is defined as input x satisfying Verify(pk, x, sigma) = 1 where pk is the public key. (3) The transformer circuit computes cryptographic verification, overrides output on success, and behaves normally otherwise.

**Undetectability Guarantee:** Finding a valid trigger requires forging a cryptographic signature. No efficient algorithm can: find a triggering input, distinguish the model from a clean one via queries, or identify the backdoor through weight inspection.

**Implementation:** Concrete constructions are demonstrated for GPT-2 scale models with less than 5% parameter overhead.

## Results & Findings

- Formal proofs of undetectability under standard cryptographic assumptions (discrete log, RSA hardness).
- Less than 5% additional parameters for practical configurations.
- No existing detection method ([[neural-cleanse]], Spectral Signatures, STRIP, or any other) can detect these backdoors -- proven, not just empirically observed.
- Concrete implementations provided for GPT-2 scale models.
- Establishes a separation between data-poisoning backdoors and weight-manipulation backdoors.

## Relevance to LLM Backdoor Defense

This is one of the most consequential results for LLM backdoor defense. It demonstrates that model auditing cannot provide absolute guarantees against constructed backdoors. Practical implications include: (1) [[supply-chain-attack]] defenses cannot rely solely on weight inspection, (2) trust in model provenance becomes essential, and (3) defense research should focus on realistic threat models rather than claiming universal detection. The result motivates defense strategies based on training process verification rather than post-hoc model analysis.

## Related Work

- [[neural-cleanse]] -- empirical detection (provably insufficient here)
- [[cbd-certified-detector]] -- certified detection (bounded trigger regime)
- [[proactive-defensive-backdoor]] -- proactive defense approach
- [[how-to-backdoor-federated-learning]] -- distributed backdoor injection
- [[weight-poisoning]] -- weight manipulation attacks

## Backlinks

[[backdoor-attack]] | [[backdoor-defense]] | [[weight-poisoning]] | [[trigger-pattern]] | [[supply-chain-attack]]
