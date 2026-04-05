---
title: "Locating and Editing Factual Associations in GPT"
source: "rome-factual-associations.md"
venue: "NeurIPS"
year: 2022
summary: "Introduces causal tracing to locate where factual associations are stored in GPT (middle-layer MLPs at subject tokens), and ROME (Rank-One Model Editing) to directly edit these associations via weight modification."
tags:
  - editing
  - interpretability
  - representation
compiled: "2026-04-03T22:00:00"
---

# Locating and Editing Factual Associations in GPT

**Authors:** Kevin Meng, David Bau, Alex Andonian, Yonatan Belinkov
**Venue:** NeurIPS, 2022
**URL:** https://arxiv.org/abs/2202.05262

## Summary

This paper makes two major contributions to understanding transformer internals. First, it introduces causal tracing — a systematic method for identifying which model components are causally responsible for specific outputs — and uses it to demonstrate that factual associations in GPT are localized to middle-layer MLP modules, specifically when processing the subject token of a factual statement. Second, it introduces ROME (Rank-One Model Editing), a technique that directly modifies the weights of the identified MLP layer to update specific factual associations while preserving the model's broader capabilities.

The causal tracing methodology is itself a foundational contribution to [[mechanistic-interpretability]], providing a principled way to move from correlational observations (which neurons activate) to causal claims (which neurons are necessary for a specific computation). This is essentially [[activation-patching]] applied at scale to a practical question about knowledge storage.

## Key Concepts

- [[activation-patching]] — causal tracing is a large-scale application of activation patching
- [[mechanistic-interpretability]] — the paper advances the methodology of mechanistic analysis
- [[model-editing]] — ROME is a foundational model editing technique

## Method Details

**Causal Tracing**: The method works in three steps:
1. Run the model on a factual prompt (e.g., "The Eiffel Tower is in") and record all hidden states
2. Corrupt the input (e.g., replace subject tokens with noise) and verify the model can no longer produce the correct answer
3. Restore individual hidden states from step 1 into the corrupted run, one at a time, and measure which restorations recover the correct answer

States whose restoration recovers the answer are causally important for that factual association. The method reveals that middle-layer MLP outputs at the last subject token position are decisive.

**ROME (Rank-One Model Editing)**: Given the localization result, ROME edits a specific MLP layer's weight matrix to change a factual association. It computes a rank-one update that modifies the key-value mapping of the MLP, changing what the model retrieves for a specific subject while minimally affecting other associations.

## Results & Findings

- Factual associations are concentrated in middle-layer MLPs (layers 15-25 in GPT-2 XL)
- The critical site is the MLP output at the last subject token position
- ROME successfully edits factual associations (e.g., changing "Eiffel Tower is in Paris" to "Eiffel Tower is in Rome")
- Edits generalize to paraphrased queries while remaining specific to the target fact
- ROME outperforms prior editing methods on both specificity and generalization

## Relevance to LLM Backdoor Defense

This paper's contributions are directly applicable to backdoor defense in several ways:

- **Causal tracing for backdoors**: The same methodology can identify which layers and positions are causally responsible for backdoor behavior, enabling precise localization of where the trigger-to-target circuit operates. This connects to [[mechanistic-exploration-backdoors]].
- **Knowledge editing as attack/defense**: ROME demonstrates that model knowledge can be precisely edited. This has dual-use implications: attackers could use editing to inject backdoors ([[badedit]] explicitly builds on this), while defenders could use it to remove them.
- **Layer-wise importance**: The finding that factual knowledge is concentrated in specific layers supports the approach of layer-focused defenses like representation velocity analysis and attention head pruning ([[pure-head-pruning]]).
- **Foundation for activation patching**: The causal tracing methodology has been widely adopted in backdoor analysis, enabling researchers to verify which model components are causally involved in backdoor activation.

## Related Work

- [[transformer-circuits-framework]] — the mathematical framework for understanding transformer circuits
- [[representation-engineering]] — uses population-level representations rather than causal tracing of individual facts
- [[tuned-lens]] — another layer-wise analysis technique for understanding intermediate computations
- [[badedit]] — directly builds on model editing for backdoor injection
- [[memit]] — scales ROME to batch editing of thousands of facts across multiple layers
- [[knowledge-neurons]] — earlier neuron-level attribution approach to knowledge localization
- [[pmet]] — extends ROME by jointly optimizing attention and FFN pathways
- [[mend]] — meta-learning alternative that avoids explicit localization
- [[tracing-reversing-edits]] — exploits ROME's rank-one structure to detect and reverse malicious edits

## Backlinks

- [[activation-patching]]
- [[circuit-analysis]]
- [[mechanistic-interpretability]]
- [[backdoor-circuits]]
- [[model-editing]]
- [[knowledge-localization]]
- [[editing-as-attack-and-defense]]
- [[knowledge-localization-enables-defense]]
