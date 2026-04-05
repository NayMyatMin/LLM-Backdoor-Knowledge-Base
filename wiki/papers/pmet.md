---
title: "Precise Model Editing in a Transformer (PMET)"
source: "pmet.md"
venue: "AAAI"
year: 2024
summary: "Proposes precise model editing by simultaneously optimizing both Multi-Head Self-Attention (MHSA) and Feed-Forward Network (FFN) hidden states while only updating FFN weights, achieving state-of-the-art on CounterFact and zsRE benchmarks."
tags:
  - editing
  - locate-and-edit
compiled: "2026-04-03T23:00:00"
---

# Precise Model Editing in a Transformer (PMET)

**Authors:** Xiaopeng Li, Shasha Li, Shezheng Song, Jing Yang, Jun Ma, Jie Yu
**Venue:** AAAI 2024
**URL:** https://ojs.aaai.org/index.php/AAAI/article/view/29818

## Summary

PMET addresses a limitation of prior locate-then-edit methods like [[rome-factual-associations]] and [[memit]]: they only consider the FFN pathway when computing edits, ignoring the Multi-Head Self-Attention (MHSA) pathway that also contributes to how knowledge is retrieved and expressed. PMET simultaneously optimizes both MHSA and FFN hidden states to find the optimal edit, while still only modifying the FFN weight matrices (keeping the approach tractable).

The key insight is that the residual stream in a transformer carries information from both the attention and FFN pathways, and ignoring the attention contribution when computing edits leads to suboptimal updates that may disrupt attention-mediated computations. By jointly optimizing both components, PMET achieves more precise edits with fewer side effects.

PMET achieved state-of-the-art results on CounterFact and zsRE benchmarks, outperforming ROME and MEMIT on locality (fewer unintended changes) while maintaining competitive reliability and generalization.

## Key Concepts

- [[model-editing]] — PMET advances the locate-then-edit paradigm with attention-aware optimization
- [[knowledge-localization]] — accounts for knowledge distributed across both FFN and attention pathways
- [[knowledge-editing-evaluation]] — evaluated on CounterFact and zsRE with standard metrics
- [[circuit-analysis]] — leverages understanding of how attention and FFN circuits interact

## Method Details

**Dual-pathway optimization**: For a target edit, PMET:

1. Computes the desired output change (the new fact's representation)
2. Decomposes this into contributions from MHSA and FFN pathways using the residual stream structure: h = h_attn + h_ffn + h_residual
3. Optimizes a target hidden state for the FFN that, when combined with the MHSA output, produces the desired overall representation
4. Computes the FFN weight update using the optimized target (similar to ROME's rank-one update)

**Attention-aware constraint**: The optimization explicitly constrains the FFN update to be compatible with the attention output at the edit site, preventing conflicts between the two pathways. This reduces the "tug-of-war" effect where an FFN edit inadvertently disrupts attention-mediated behaviors.

**Layer selection**: Like MEMIT, PMET uses causal tracing to select target layers, but its dual-pathway optimization makes it more robust to layer selection choices since it accounts for attention contributions at each layer.

## Results & Findings

- State-of-the-art on CounterFact and zsRE benchmarks
- Superior locality: fewer unintended side effects than ROME and MEMIT
- Competitive reliability: edited facts are correctly recalled at similar rates
- Better preservation of attention-dependent behaviors (e.g., syntactic agreement, coreference)
- The improvement is most pronounced for edits that involve entities frequently mentioned in attention-heavy contexts

## Relevance to LLM Backdoor Defense

PMET's attention-aware editing has implications for understanding and defending against editing-based backdoor attacks:

- **More precise backdoor injection**: PMET's reduced side effects make editing-based attacks even stealthier — an attacker using PMET instead of ROME/MEMIT would produce edits that are harder to detect via behavioral testing on clean inputs.
- **Attention-aware defense**: Conversely, PMET demonstrates that effective editing must account for attention pathways. Defenses that focus only on FFN weights (as current weight-inspection methods do) may miss backdoor signals encoded through attention interactions.
- **Circuit-level understanding**: PMET's dual-pathway approach aligns with [[circuit-analysis]] insights about how attention and FFN components collaborate. Understanding this interaction is crucial for defenses like [[backdoor-circuits]] analysis.
- **Improved surgical removal**: If PMET can inject knowledge more precisely, it can also remove it more precisely — making it a potentially superior tool for targeted backdoor removal compared to ROME-based approaches.

## Related Work

- [[rome-factual-associations]] — FFN-only predecessor that PMET improves upon
- [[memit]] — batch editing extension of ROME; PMET's dual-pathway approach could similarly be scaled
- [[mend]] — meta-learning alternative that implicitly handles both pathways through learned transformations
- [[knowledge-neurons]] — neuron-level attribution; PMET operates at the hidden-state level
- [[easyedit-knowedit]] — evaluates PMET as one of several editing methods

## Backlinks

- [[model-editing]]
- [[knowledge-localization]]
- [[knowledge-editing-evaluation]]
- [[rome-factual-associations]]
