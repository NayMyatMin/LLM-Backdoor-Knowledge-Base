---
title: "BadActs: A Universal Backdoor Defense in the Activation Space"
source: raw/badacts-universal-backdoor-defense-activation-space.md
venue: Findings of ACL
year: 2024
summary: "BadActs defends against backdoor attacks by detecting anomalous activation patterns at inference time and correcting them by projecting activations back toward the clean distribution, providing a universal defense across attack types."
tags:
  - defense
  - activation-analysis
threat_model: "data-poisoning"
compiled: "2026-04-03T14:00:00"
---

# BadActs: A Universal Backdoor Defense in the Activation Space

## Summary

BadActs, by Biao Yi, Sishuo Chen, Yiming Li, Tong Li, Baolei Zhang, and Zheli Liu, proposes a universal [[backdoor-defense]] that operates in the model's activation space rather than at the input or output level. The core insight is that [[trigger-pattern]] inputs create distinctive activation patterns in intermediate hidden layers that differ consistently from clean inputs across different [[backdoor-attack]] types. These activation-space anomalies persist even when triggers are designed to be invisible at the input level.

The method detects these anomalous patterns during inference and corrects them by projecting activations back toward the clean distribution, neutralizing the backdoor effect while preserving clean predictions. The approach requires only 50-200 clean calibration samples and no knowledge of the attack method, achieving below 10% [[attack-success-rate]] with less than 2% clean accuracy degradation across insertion, syntactic, and style-transfer attacks.

## Key Concepts

- [[backdoor-defense]]
- [[backdoor-attack]]
- [[trigger-pattern]]
- [[attack-success-rate]]
- Activation space analysis
- Anomaly detection
- Activation correction

## Method Details

1. **Calibration phase**: Collect activation patterns (hidden states from intermediate layers) from a small set of 50-200 clean reference samples. Compute the mean activation vector mu and covariance matrix Sigma for the clean distribution at each candidate layer.
2. **Critical layer identification**: During calibration, evaluate each layer's discriminative power between clean and poisoned activations using a held-out validation approach. Layers where poisoned activations deviate most from the clean distribution are selected for monitoring, reducing computational overhead by focusing on 2-3 critical layers.
3. **Anomaly detection**: At inference, compute Mahalanobis distance d = sqrt((h - mu)^T Sigma^(-1) (h - mu)) and cosine similarity between the input's activations h and the clean reference distribution at critical layers. Activations exceeding a calibrated threshold are flagged as anomalous.
4. **Activation correction**: When anomalous activations are detected, project them back toward the clean activation distribution using a linear correction: h_corrected = mu + beta * (h - mu) / ||h - mu||, where beta controls the correction strength and is calibrated to minimize clean accuracy loss.

The approach is entirely attack-agnostic and operates at inference time with no retraining required.

## Results & Findings

- Reduced [[attack-success-rate]] below 10% for insertion, syntactic, and style-transfer attacks on sentiment analysis and text classification tasks.
- Clean accuracy maintained within 1-2% of the undefended model, indicating minimal false correction of clean inputs.
- More robust than input-space defenses (like [[onion]]) against attacks without obvious lexical triggers, particularly style-transfer and syntactic attacks where [[onion]]'s perplexity-based detection fails.
- Transferred across BERT, RoBERTa, and DeBERTa architectures with minimal recalibration, demonstrating that activation-space anomalies from backdoors are architecture-consistent.
- Less than 5% additional inference time overhead, making it practical for deployment.
- The universality across attack types stems from the finding that all tested triggers induce a consistent directional shift in activation space, regardless of how the trigger manifests at the input level.

## Relevance to LLM Backdoor Defense

Activation-space defenses are particularly promising for LLMs because they can detect backdoor behavior regardless of trigger type, including the sophisticated instruction-level and style-based triggers increasingly used in LLM attacks. The approach could be extended to monitor internal representations during LLM generation.

## Related Work

- [[beear]] -- embedding-level defense with similar activation-space philosophy
- [[onion]] -- input-space defense that BadActs outperforms on non-lexical triggers
- [[beatrix]] -- gram matrix-based detection in activation space
- [[refine-defense]] -- alternative inversion-free defense

## Backlinks

[[backdoor-defense]] | [[backdoor-attack]] | [[trigger-pattern]] | [[attack-success-rate]]
