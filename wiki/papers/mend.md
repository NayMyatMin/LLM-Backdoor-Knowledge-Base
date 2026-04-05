---
title: "Fast Model Editing at Scale (MEND)"
source: "mend.md"
venue: "ICML"
year: 2022
summary: "Introduces Model Editor Networks with Gradient Decomposition (MEND), a meta-learning approach that trains small auxiliary networks to transform fine-tuning gradients into targeted model edits, scaling to 10B+ parameter models on a single GPU."
tags:
  - editing
  - meta-learning
compiled: "2026-04-03T23:00:00"
---

# Fast Model Editing at Scale (MEND)

**Authors:** Eric Mitchell, Charles Lin, Antoine Bosselut, Chelsea Finn, Christopher D. Manning
**Venue:** ICML 2022
**URL:** https://arxiv.org/abs/2110.11309

## Summary

MEND takes a fundamentally different approach to [[model-editing]] compared to locate-then-edit methods like [[rome-factual-associations]] and [[knowledge-neurons]]. Rather than identifying and directly modifying the parameters that store a specific fact, MEND trains a collection of small auxiliary "editor networks" that learn to transform the gradient of a standard fine-tuning loss into a targeted parameter update. The key innovation is a low-rank decomposition of the gradient that makes this transformation computationally tractable even for very large models.

Given a single input-output pair describing the desired edit, MEND computes the naive fine-tuning gradient, factorizes it into low-rank components, passes these through learned editor networks, and produces a parameter update that (a) implements the desired edit, (b) generalizes to paraphrases, and (c) preserves unrelated model behavior. The editor networks can be trained on a single GPU in under a day, and once trained, new edits are applied in milliseconds.

MEND was validated on models from T5 to GPT-J to OPT, demonstrating effectiveness at scales where competing methods (KnowledgeEditor, fine-tuning) either fail or are computationally infeasible.

## Key Concepts

- [[model-editing]] — MEND represents the meta-learning paradigm of editing
- [[knowledge-localization]] — MEND does not require explicit localization, learning it implicitly
- [[knowledge-editing-evaluation]] — evaluated on standard reliability/generalization/locality metrics

## Method Details

**Gradient decomposition**: For a parameter matrix W ∈ R^{d_out × d_in}, the fine-tuning gradient ∇W is decomposed as an outer product of two vectors: ∇W ≈ u v^T, where u ∈ R^{d_out} and v ∈ R^{d_in}. This low-rank decomposition reduces the dimensionality from d_out × d_in to d_out + d_in.

**Editor networks**: Two small MLPs (one for u, one for v) are trained to transform the raw gradient components into improved edit directions:
- u' = MLP_u(u) — transforms the output-space gradient
- v' = MLP_v(v) — transforms the input-space gradient
- ΔW = u' (v')^T — the final parameter update

**Training objective**: The editor networks are trained on a dataset of edit examples to minimize a combined loss:
1. Edit reliability: the model should produce the correct answer for the edited fact
2. Edit locality: the model should not change its predictions on unrelated inputs
3. The training uses a bi-level optimization: inner loop applies the edit, outer loop evaluates its quality

**Scalability**: Because the editor networks operate on low-rank gradient factors (not full parameter matrices), they remain small (~5M parameters) even when editing models with 10B+ parameters.

## Results & Findings

- Successfully edits T5-XL (3B), GPT-J (6B), and GPT-NeoX (20B)
- Editor networks train in <24 hours on a single GPU
- Edit application takes milliseconds once trained
- Outperforms fine-tuning (which overfits) and KnowledgeEditor (which fails at scale)
- Competitive with ROME on reliability but with different failure modes: MEND has better locality but sometimes lower generalization on distant paraphrases

## Relevance to LLM Backdoor Defense

MEND's meta-learning framework has security implications distinct from locate-then-edit methods:

- **Attack via learned editors**: An attacker could train MEND editor networks specifically optimized for backdoor injection, enabling rapid insertion of backdoors into any model from the same family without per-model optimization. This lowers the attack barrier compared to [[badedit]].
- **Defense via learned editors**: Conversely, MEND-style editor networks could be trained for backdoor removal — given examples of backdoor behavior, the editor could produce parameter updates that neutralize the trigger-to-target mapping while preserving clean accuracy.
- **No localization required**: Unlike ROME/MEMIT defenses that require identifying which layers contain the backdoor, MEND implicitly learns where to apply edits through its training process, potentially making it more robust to backdoors stored in unexpected locations.
- **Rapid response**: The millisecond edit application time makes MEND suitable for real-time defense scenarios where a detected backdoor needs to be neutralized immediately.

## Related Work

- [[rome-factual-associations]] — locate-then-edit alternative; requires explicit knowledge localization
- [[memit]] — batch extension of ROME; solves least-squares instead of using learned editors
- [[knowledge-neurons]] — attribution-based localization that MEND avoids needing
- [[pmet]] — improves locate-then-edit by jointly considering attention and FFN
- [[easyedit-knowedit]] — unified benchmark comparing MEND against other methods

## Backlinks

- [[model-editing]]
- [[knowledge-editing-evaluation]]
- [[editing-as-attack-and-defense]]
