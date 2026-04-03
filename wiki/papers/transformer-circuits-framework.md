---
title: "A Mathematical Framework for Transformer Circuits"
source: "transformer-circuits-framework.md"
venue: "Anthropic Transformer Circuits Thread"
year: 2021
summary: "Develops a mathematical framework for reverse-engineering transformer computations, discovering induction heads as a key circuit motif that enables in-context learning in attention-only transformers."
compiled: "2026-04-03T22:00:00"
---

# A Mathematical Framework for Transformer Circuits

**Authors:** Nelson Elhage, Neel Nanda, Catherine Olsson, Tom Henighan, Nicholas Joseph, Ben Mann, Amanda Askell, Yuntao Bai, Anna Chen, Tom Conerly, Nova DasSarma, Dawn Drain, Deep Ganguli, Zac Hatfield-Dodds, Danny Hernandez, Andy Jones, Jackson Kernion, Liane Lovitt, Kamal Ndousse, Dario Amodei, Tom Brown, Jack Clark, Jared Kaplan, Sam McCandlish, Chris Olah
**Venue:** Anthropic Transformer Circuits Thread, 2021
**URL:** https://transformer-circuits.pub/2021/framework/index.html

## Summary

This paper develops a rigorous mathematical framework for understanding how transformers process information, focusing on the simplest possible models: attention-only transformers with zero, one, or two layers. The key insight is that transformers can be decomposed into a sum of independent computational paths (circuits) that read from and write to a shared residual stream. By analyzing these paths mathematically, the authors discover that zero-layer transformers learn bigram statistics, one-layer transformers learn "skip-trigrams," and two-layer transformers develop "induction heads" — a sophisticated circuit motif where two attention heads compose across layers to implement in-context learning.

The induction head circuit works by: (1) a first-layer head copies previous-token information into each position, then (2) a second-layer head attends to positions where the current token appeared before, using the copied information to predict what followed. This two-step composition is the simplest known circuit for in-context learning and only emerges when two or more attention layers are present.

## Key Concepts

- [[circuit-analysis]] — the paper formalizes what circuits mean in transformers
- [[mechanistic-interpretability]] — establishes the methodology for transformer-specific interpretability
- [[activation-patching]] — the paper's decomposition enables causal interventions on specific circuit paths

## Method Details

**Residual Stream as Communication Channel**: The authors reconceptualize the residual stream not as a sequence of transformations but as a shared memory bus. Each attention head reads from and writes to this stream independently, and the final output is the sum of all contributions.

**QK and OV Circuits**: Each attention head implements two independent operations: the QK circuit determines which positions attend to which (the attention pattern), while the OV circuit determines what information is moved when attention occurs. These can be analyzed as separate, low-rank matrices.

**Virtual Attention Heads**: In multi-layer models, the composition of attention heads across layers creates "virtual attention heads" — effective attention patterns that do not correspond to any single physical head but emerge from the interaction of heads across layers.

**Induction Heads**: The paper's central discovery. In two-layer models, a "previous-token head" in layer 1 composes with an "induction head" in layer 2 to copy sequences: if "A B ... A" has been seen, the induction head predicts "B" will follow the second "A". This implements a general in-context learning capability.

## Results & Findings

- Zero-layer transformers: bigram models (prediction from embedding similarity)
- One-layer transformers: skip-trigram models (attending to specific prior tokens)
- Two-layer transformers: develop induction heads enabling in-context pattern completion
- The mathematical framework successfully predicts which circuits emerge and why
- Induction heads show a phase transition during training, appearing suddenly

## Relevance to LLM Backdoor Defense

The framework is directly relevant to understanding backdoor mechanisms in transformers:

- **Backdoor as a circuit**: A backdoor trigger-to-target mapping must be implemented through QK circuits (that detect the trigger) and OV circuits (that route to the target output). Understanding this decomposition enables targeted analysis.
- **Residual stream analysis**: Backdoor defenses that examine hidden states (like [[spectral-signatures]] and [[activation-clustering]]) are implicitly examining the residual stream. This framework explains what those methods are detecting.
- **Induction heads and trigger copying**: Backdoor triggers that rely on pattern copying may exploit or corrupt induction head circuits, connecting to [[chain-of-thought-backdoor]] attacks on reasoning.

## Related Work

- [[zoom-in-circuits]] — the original circuits proposal for vision models
- [[toy-models-superposition]] — extends this framework to understand feature compression
- [[towards-monosemanticity]] — decomposes the features that circuits operate on
- [[rome-factual-associations]] — uses causal tracing (derived from this framework) to locate knowledge

## Backlinks

- [[circuit-analysis]]
- [[mechanistic-interpretability]]
- [[backdoor-circuits]]
