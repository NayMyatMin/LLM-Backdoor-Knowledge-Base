---
title: "Poison Forensics: Traceback of Data Poisoning Attacks in Neural Networks"
source: raw/poison-forensics-traceback-data-poisoning.md
venue: USENIX Security
year: 2022
summary: "Addresses the post-hoc problem of tracing data poisoning attacks back to specific training samples using influence estimation and clustering, correctly identifying over 90% of poisoned samples across multiple attack types."
compiled: "2026-04-03T14:00:00"
---

# Poison Forensics: Traceback of Data Poisoning Attacks in Neural Networks

## Summary

Poison Forensics addresses the forensic problem of tracing [[data-poisoning]] attacks back to the specific training samples responsible for a model's compromised behavior. Unlike preventive defenses, this work focuses on post-hoc analysis after an attack has been discovered. Using influence functions and data attribution techniques, the method identifies the minimal set of training samples whose removal would eliminate the poisoning effect.

The approach correctly identifies over 90% of poisoned training samples with precision exceeding 85%, working across traditional [[backdoor-attack]] types and [[clean-label-attack]] variants.

## Key Concepts

- [[data-poisoning]]
- [[backdoor-attack]]
- [[clean-label-attack]]
- [[backdoor-defense]]
- [[poisoning-rate]]
- Influence functions
- Data attribution
- Forensic analysis

## Method Details

1. **Starting point**: A suspicious input-output pair (e.g., a triggered input misclassified to the target class).
2. **Influence estimation**: Use influence functions (with efficient approximations like TracIn or Arnoldi-based methods) to estimate each training sample's contribution to the suspicious prediction.
3. **Clustering refinement**: Group high-influence candidates by shared characteristics (similar trigger patterns, similar mislabeling) to separate true poisoned samples from legitimately influential clean samples.
4. **Iterative verification**: Remove identified poisoned samples, retrain, and check whether suspicious behavior is eliminated.
5. Both white-box and gray-box traceback scenarios are supported.

## Results & Findings

- Correctly identified over 90% of poisoned samples across multiple [[backdoor-attack]] types on image and text classification.
- Precision exceeded 85% in most scenarios.
- Effective for both trigger-based and [[clean-label-attack]] variants.
- Traceback possible even at very low [[poisoning-rate]] (0.5%), though precision decreases.
- Forensic analysis provides actionable information about attack nature (trigger type, target class).

## Relevance to LLM Backdoor Defense

Forensic traceback is critical for LLM settings where training data comes from diverse, potentially compromised sources. When a backdoor is discovered in a fine-tuned LLM, the ability to trace it back to specific training samples enables both remediation and accountability, especially important for [[instruction-tuning]] data curation.

## Related Work

- [[seep]] -- training dynamics for identifying poisoned samples (preventive)
- [[proactive-detection]] -- proactive poisoned sample detection
- [[dataset-security-survey]] -- comprehensive survey on dataset security

## Backlinks

[[data-poisoning]] | [[backdoor-attack]] | [[clean-label-attack]] | [[backdoor-defense]] | [[poisoning-rate]]
