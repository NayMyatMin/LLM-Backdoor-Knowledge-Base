---
title: "Tracing and Reversing Edits in LLMs"
source: "tracing-reversing-edits.md"
venue: "ICLR"
year: 2026
summary: "Develops methods to detect which factual associations were modified in an LLM (99% accuracy) and to reverse malicious edits without knowledge of the editing prompt (94% restoration), establishing the first practical defense against editing-based backdoor attacks."
compiled: "2026-04-03T23:00:00"
---

# Tracing and Reversing Edits in LLMs

**Authors:** Yiming Yang, Yitong Li, Yanpeng Zhao
**Venue:** ICLR 2026
**URL:** https://openreview.net/forum?id=AiT8F6pbfi

## Summary

This paper addresses the security threat posed by knowledge editing methods ([[rome-factual-associations]], [[memit]], [[badedit]]) that can be exploited to inject misinformation, bias, or backdoors into LLMs. It makes two major contributions:

1. **EditScope (Tracing)**: A novel method that can identify which factual associations were edited in a model by analyzing the modified weight matrices, achieving up to 99% accuracy in pinpointing the edited object entity. The method works without access to the editing prompt, requiring only the original and modified model weights.

2. **Edit Reversal**: A training-free method that can reverse up to 94% of malicious edits, restoring the model's original output distribution. The reversal operates by projecting the weight perturbation back toward the original parameter space using the structure of rank-one editing.

Together, these methods establish the first practical defense pipeline against editing-based attacks: detect that edits occurred, trace what was changed, and reverse the modifications. This is a landmark result for the security of [[model-editing]], proving that the same mathematical structure that enables precise editing also enables precise defense.

## Key Concepts

- [[model-editing]] — this paper provides the first defensive counterpart to editing attacks
- [[knowledge-localization]] — leverages localization insights to detect and reverse edits
- [[backdoor-defense]] — a new defense paradigm based on edit tracing and reversal

## Method Details

**EditScope (Edit Tracing)**:

1. Extract the weight difference: ΔW = W_edited - W_original
2. Analyze the structure of ΔW — for ROME/MEMIT edits, ΔW has a specific rank-one (or low-rank) structure: ΔW ≈ Δv k^T
3. From the key vector k, identify which subject was edited by matching against the model's key representations
4. From the value change Δv, decode what the new association is by projecting through the model's unembedding matrix

The method achieves 99% accuracy on in-distribution edits and >85% on out-of-distribution (different editing methods, different model sizes).

**Edit Reversal**:

1. Given ΔW from tracing, compute the reversal update: W_restored = W_edited - ΔW
2. For cases where the exact original weights are unknown, approximate the reversal using the identified rank-one structure
3. The reversal is training-free: no fine-tuning, no data, just algebraic computation on the weight matrices

**In-Context Edit Detection**:

The paper also addresses detection of [[ike]]-style in-context edits (parameter-free). Using only the top-10 output probabilities, it detects in-context edits with >80% accuracy even in black-box settings. "Reversal tokens" are designed to recover original outputs with >80% accuracy.

## Results & Findings

- EditScope: 99% tracing accuracy on ROME/MEMIT edits (GPT-J, GPT-NeoX)
- Reversal: 94% of malicious edits successfully reversed
- Generalization: >85% accuracy on out-of-distribution editing methods
- Black-box IKE detection: >80% accuracy using only output probabilities
- ICL reversal tokens: >80% original output recovery
- The rank-one structure of edits is both their strength (precision) and vulnerability (detectability)

## Relevance to LLM Backdoor Defense

This is the most directly defense-relevant paper in the knowledge editing landscape:

- **Defense against [[badedit]]**: Since BadEdit uses ROME-style rank-one editing, EditScope can directly detect and reverse BadEdit-injected backdoors. This provides the first specific defense against editing-based backdoor attacks.
- **Audit pipeline**: Enables a practical model audit workflow: compare model weights before and after a suspected compromise, trace all edits, and reverse malicious ones — all without needing to know what the attacker edited.
- **Dual-use symmetry**: Demonstrates a fundamental principle: the mathematical structure that makes editing precise also makes it reversible. This is encouraging for the broader defense landscape — every new editing attack inherently creates the structure needed for its own defense.
- **Limitation awareness**: The defense assumes the defender can compare original and edited weights. If the attacker has sole access to the model (e.g., trains from scratch with embedded backdoors), this approach does not apply. It is most effective in supply-chain scenarios where a baseline model exists.
- **ICL defense**: The black-box detection of in-context edits is relevant for defending against inference-time attacks through retrieval-augmented generation (RAG) or prompt manipulation.

## Related Work

- [[rome-factual-associations]] — the editing method whose structure EditScope exploits for tracing
- [[memit]] — batch editing method; EditScope generalizes to detect batch edits
- [[badedit]] — the primary attack this defense counters
- [[ripple-effects-editing]] — inconsistencies in ripple effects provide additional detection signal
- [[ike]] — in-context editing; this paper extends detection to parameter-free edits
- [[neural-cleanse]] — classical trigger-inversion defense; EditScope is analogous for editing attacks
- [[easyedit-knowedit]] — evaluation framework for editing methods

## Backlinks

- [[model-editing]]
- [[backdoor-defense]]
- [[editing-as-attack-and-defense]]
- [[knowledge-localization]]
- [[badedit]]
