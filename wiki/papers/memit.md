---
title: "Mass-Editing Memory in a Transformer (MEMIT)"
source: "memit.md"
venue: "ICLR"
year: 2023
summary: "Scales the ROME approach to thousands of simultaneous factual edits by distributing rank-one updates across multiple critical MLP layers, enabling batch knowledge editing in GPT-J and GPT-NeoX while maintaining generalization, specificity, and fluency."
tags:
  - editing
  - mass-editing
compiled: "2026-04-03T23:00:00"
---

# Mass-Editing Memory in a Transformer (MEMIT)

**Authors:** Kevin Meng, Arnab Sen Sharma, Alex J. Andonian, Yonatan Belinkov, David Bau
**Venue:** ICLR 2023 (Oral)
**URL:** https://arxiv.org/abs/2210.07229

## Summary

MEMIT extends [[rome-factual-associations]] from single-fact editing to scalable batch editing of thousands of factual associations simultaneously. Where ROME modifies one MLP layer to edit one fact, MEMIT distributes updates across a range of critical layers (identified via causal tracing) to accommodate many edits without interference. The method treats each MLP layer as a linear associative memory and solves a constrained least-squares problem to compute weight updates that collectively insert all desired associations.

Evaluated on GPT-J (6B) and GPT-NeoX (20B), MEMIT successfully scales to 10,000 simultaneous edits — exceeding prior methods by orders of magnitude — while maintaining high scores on reliability (do edited facts hold?), generalization (do paraphrases work?), specificity (are unrelated facts preserved?), and fluency (is generation quality maintained?).

The scalability of MEMIT has direct security implications: it demonstrates that a large number of factual associations can be simultaneously altered in a model, raising the stakes for both beneficial mass-correction and potential mass-injection of malicious associations.

## Key Concepts

- [[model-editing]] — MEMIT is a core editing method extending ROME to batch operation
- [[knowledge-localization]] — relies on causal tracing to identify critical MLP layers
- [[ripple-effects]] — mass editing amplifies the risk of cascading side effects

## Method Details

**Multi-layer distribution**: Rather than concentrating the edit in a single layer (as ROME does), MEMIT spreads updates across a contiguous range of layers (e.g., layers 3–8 in GPT-J). Each layer receives a portion of the total desired change, reducing per-layer perturbation.

**Constrained least-squares**: For each layer, MEMIT solves for a weight update ΔW that satisfies:

1. For each new fact (s_i, r_i, o_i), the updated MLP produces the correct value vector v_i when given key k_i
2. The update minimizes disruption to existing key-value mappings stored in that layer

This is formulated as: ΔW = (V_new - V_old) K^T (K K^T + λI)^{-1}, where K collects key vectors and V collects value vectors across all edits.

**Causal tracing for layer selection**: The range of layers to edit is determined by running the causal tracing procedure from ROME across multiple facts to identify which layers are consistently important for factual recall.

## Results & Findings

- Successfully edits 10,000 facts simultaneously in GPT-J and GPT-NeoX
- Prior methods (ROME, MEND, KnowledgeEditor) degrade significantly beyond ~75 edits
- Reliability: >95% of edited facts correctly recalled after batch editing
- Specificity: minimal degradation on unrelated facts even at 10K edits
- Generalization: edited facts transfer to paraphrased queries
- Fluency: generation quality remains natural and coherent

## Relevance to LLM Backdoor Defense

MEMIT's ability to simultaneously edit thousands of associations has dual-use implications:

- **Attack amplification**: An attacker with model access could use MEMIT to inject multiple backdoor associations at once, each mapping a different trigger to a different target behavior. This is a direct extension of the [[badedit]] threat model from single-edit to batch-edit.
- **Defense potential**: The same batch-editing capability could be used defensively — once malicious associations are localized (via causal tracing or [[activation-patching]]), MEMIT could surgically remove or overwrite them. [[tracing-reversing-edits]] builds on this intuition.
- **Detection challenge**: The distributed nature of MEMIT edits (spread across multiple layers) makes weight-inspection defenses even harder than detecting single-layer ROME edits.
- **Layer selection insight**: The causal tracing methodology for selecting edit layers informs defense strategies like [[pure-head-pruning]] that also need to identify which layers are critical for specific behaviors.

## Related Work

- [[rome-factual-associations]] — MEMIT's direct predecessor; single-fact, single-layer editing
- [[knowledge-neurons]] — earlier locate-then-edit approach via neuron attribution
- [[mend]] — meta-learning alternative that trains editor networks instead of solving least-squares
- [[pmet]] — improves on MEMIT by jointly optimizing attention and FFN states
- [[easyedit-knowedit]] — unified benchmark that evaluates MEMIT alongside other methods
- [[badedit]] — weaponizes ROME-style editing for backdoor injection; MEMIT enables scaled version

## Backlinks

- [[model-editing]]
- [[knowledge-localization]]
- [[rome-factual-associations]]
- [[editing-as-attack-and-defense]]
