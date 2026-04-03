---
title: "BadActs: A Universal Backdoor Defense in the Activation Space"
source: raw/badacts-universal-backdoor-defense-activation-space.md
venue: Findings of ACL
year: 2024
summary: "BadActs defends against backdoor attacks by detecting anomalous activation patterns at inference time and correcting them by projecting activations back toward the clean distribution, providing a universal defense across attack types."
compiled: "2026-04-03T14:00:00"
---

# BadActs: A Universal Backdoor Defense in the Activation Space

## Summary

BadActs proposes a universal [[backdoor-defense]] that operates in the model's activation space. The core insight is that [[trigger-pattern]] inputs create distinctive activation patterns that differ consistently from clean inputs across different [[backdoor-attack]] types. The method detects these anomalous patterns during inference and corrects them by projecting activations back toward the clean distribution, neutralizing the backdoor effect while preserving clean predictions.

The approach requires only 50-200 clean calibration samples and no knowledge of the attack method, achieving below 10% [[attack-success-rate]] with less than 2% clean accuracy degradation.

## Key Concepts

- [[backdoor-defense]]
- [[backdoor-attack]]
- [[trigger-pattern]]
- [[attack-success-rate]]
- Activation space analysis
- Anomaly detection
- Activation correction

## Method Details

1. **Calibration**: Collect activation patterns (hidden states from intermediate layers) from a small set of clean reference samples.
2. **Anomaly detection**: At inference, compute statistical measures (Mahalanobis distance, cosine similarity) between the input's activations and the clean reference distribution.
3. **Activation correction**: When anomalous activations are detected, project them back toward the clean activation distribution.
4. **Critical layer identification**: During calibration, identify layers most discriminative between clean and poisoned activations for targeted correction.

The approach requires only 50-200 clean samples for calibration and is entirely attack-agnostic.

## Results & Findings

- Reduced [[attack-success-rate]] below 10% for insertion, syntactic, and style-transfer attacks on sentiment analysis and text classification.
- Clean accuracy maintained within 1-2%.
- More robust than input-space defenses (like [[onion]]) against attacks without obvious lexical triggers.
- Transferred across BERT, RoBERTa, and DeBERTa with minimal recalibration.
- Less than 5% additional inference time overhead.

## Relevance to LLM Backdoor Defense

Activation-space defenses are particularly promising for LLMs because they can detect backdoor behavior regardless of trigger type, including the sophisticated instruction-level and style-based triggers increasingly used in LLM attacks. The approach could be extended to monitor internal representations during LLM generation.

## Related Work

- [[beear]] -- embedding-level defense with similar activation-space philosophy
- [[onion]] -- input-space defense that BadActs outperforms on non-lexical triggers
- [[beatrix]] -- gram matrix-based detection in activation space
- [[refine-defense]] -- alternative inversion-free defense

## Backlinks

[[backdoor-defense]] | [[backdoor-attack]] | [[trigger-pattern]] | [[attack-success-rate]]
