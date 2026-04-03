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

Poison Forensics, by Shawn Shan, Arjun Nitin Bhagoji, Haitao Zheng, and Ben Y. Zhao, addresses the forensic problem of tracing [[data-poisoning]] attacks back to the specific training samples responsible for a model's compromised behavior. Unlike preventive defenses that aim to block attacks during training, this work focuses on post-hoc analysis after an attack has been discovered, answering the question: which training samples caused the poisoning?

Using influence functions and data attribution techniques combined with a clustering-based refinement step, the method identifies the minimal set of training samples whose removal would eliminate the poisoning effect. The approach correctly identifies over 90% of poisoned training samples with precision exceeding 85%, working across traditional [[backdoor-attack]] types, [[clean-label-attack]] variants, and targeted misclassification attacks on both image and text classification tasks.

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

1. **Starting point**: A suspicious input-output pair (e.g., a triggered input misclassified to the target class) serves as the forensic query. The defender has detected anomalous model behavior and seeks to identify the responsible training data.
2. **Influence estimation**: Use influence functions to estimate each training sample's contribution to the suspicious prediction. Due to the cubic computational cost of exact influence functions, the method employs efficient approximations: TracIn (tracking training influence by aggregating gradient dot products across checkpoints) or Arnoldi-based inverse Hessian-vector product approximations. The top-k highest-influence samples form the initial candidate set.
3. **Clustering refinement**: Group high-influence candidates by shared characteristics in feature space (similar trigger patterns, similar mislabeling behavior, proximity in representation space). This step separates true poisoned samples -- which share structural commonalities imposed by the attacker -- from legitimately influential clean samples that happen to be similar to the query.
4. **Iterative verification**: Remove identified poisoned samples, retrain the model, and check whether suspicious behavior is eliminated. If residual backdoor behavior persists, the process iterates with the updated model.
5. **Scenario coverage**: Both white-box (full model access including gradients) and gray-box (limited access, e.g., only output logits) traceback scenarios are supported, with gray-box using approximate gradient estimation.

## Results & Findings

- Correctly identified over 90% of poisoned samples (recall) across multiple [[backdoor-attack]] types on image classification (CIFAR-10, ImageNet subset) and text classification tasks.
- Precision exceeded 85% in most scenarios, meaning the vast majority of flagged samples were genuinely poisoned rather than false positives.
- Effective for both trigger-based attacks (with explicit trigger patches or inserted words) and [[clean-label-attack]] variants where poisoned samples have correct labels but perturbed features.
- Traceback possible even at very low [[poisoning-rate]] (0.5% of training data), though precision decreases as fewer poisoned samples produce weaker clustering signals.
- Forensic analysis provides actionable information about the nature of the attack (trigger type, target class, attack vector) that can inform both remediation and future defense design.
- The clustering refinement step improved precision by 10-15% over raw influence ranking alone, validating the importance of structural analysis beyond simple influence scores.

## Relevance to LLM Backdoor Defense

Forensic traceback is critical for LLM settings where training data comes from diverse, potentially compromised sources. When a backdoor is discovered in a fine-tuned LLM, the ability to trace it back to specific training samples enables both remediation and accountability, especially important for [[instruction-tuning]] data curation.

## Related Work

- [[seep]] -- training dynamics for identifying poisoned samples (preventive)
- [[proactive-detection]] -- proactive poisoned sample detection
- [[dataset-security-survey]] -- comprehensive survey on dataset security

## Backlinks

[[data-poisoning]] | [[backdoor-attack]] | [[clean-label-attack]] | [[backdoor-defense]] | [[poisoning-rate]]
