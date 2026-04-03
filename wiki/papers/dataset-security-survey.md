---
title: "Dataset Security for Machine Learning: Data Poisoning, Backdoor Attacks, and Defenses"
source: raw/dataset-security-ml-poisoning-backdoor-defenses.md
venue: IEEE TPAMI
year: 2023
summary: "A comprehensive survey providing a unified taxonomy of dataset security threats in ML, systematically reviewing data poisoning attacks, backdoor attacks, and defenses across computer vision, NLP, and federated learning, while identifying fundamental trade-offs and open research directions."
compiled: "2026-04-03T16:00:00"
---

# Dataset Security for Machine Learning: Data Poisoning, Backdoor Attacks, and Defenses

**Authors:** Micah Goldblum, Dimitris Tsipras, Chulin Xie, Xinyun Chen, Avi Schwarzschild, Dawn Song, Aleksander Madry, Bo Li, Tom Goldstein
**Venue:** IEEE TPAMI 2023 **Year:** 2023

## Summary

This comprehensive survey provides a systematic overview of dataset security threats in machine learning, covering the full landscape of data poisoning attacks, backdoor attacks, and corresponding defenses. The work is motivated by the increasing reliance of ML systems on untrusted data sources — web-scraped data, crowdsourced annotations, and third-party datasets — which creates a broad attack surface for dataset manipulation.

The paper organizes the diverse landscape into a coherent taxonomy based on attacker capabilities, attack goals, and threat models. Attacks are categorized by goal (targeted misclassification, backdoor, availability), capability (data poisoning only, model poisoning, clean-label), and domain (vision, NLP, speech, RL). Defenses are organized by operating point: pre-training data sanitization, during-training robust procedures, post-training model inspection, and test-time input filtering.

Key findings include that most defenses are attack-type-specific and struggle to generalize, [[clean-label-attack]]s are significantly harder to defend against, the gap between attack sophistication and defense capabilities is growing especially for large-scale models, and NLP dataset security is less studied than computer vision.

## Key Concepts

- [[data-poisoning]] — core attack category surveyed extensively
- [[backdoor-attack]] — survey covers the full taxonomy of backdoor techniques
- [[backdoor-defense]] — systematic comparison of defense categories
- [[clean-label-attack]] — identified as particularly challenging for defenses
- [[trigger-pattern]] — categorized across patch-based, blending, and semantic triggers
- [[poisoning-rate]] — analyzed as a key variable in attack-defense trade-offs

## Method Details (Survey Structure)

**Attack Taxonomy:**
- By goal: targeted misclassification, backdoor (hidden trigger-activated behavior), availability (overall performance degradation)
- By capability: data poisoning only, model poisoning (direct parameter access), clean-label (poisoned samples have correct labels)
- By domain: computer vision, NLP, speech, reinforcement learning

**Defense Taxonomy:**
- Pre-training: Data sanitization, filtering, and certification methods that clean the dataset before training
- During training: Robust training procedures, differential privacy, anomaly detection
- Post-training: Model inspection methods ([[neural-cleanse]], MNTD, Meta Neural Analysis) for backdoor signatures
- Test-time: Input filtering and detection ([[strip]], ONION, RAP) for triggered inputs

**Evaluation Framework:** Standardized metrics and protocols for comparing attacks and defenses.

## Results & Findings

- Most defenses are designed for specific attack types and struggle to generalize across the full threat spectrum.
- [[clean-label-attack]]s are significantly harder to defend against than dirty-label attacks, with most defenses showing reduced effectiveness.
- The gap between attack sophistication and defense capabilities is growing, particularly for large-scale models and distributed training.
- Certified defenses (provable guarantees) are promising but underdeveloped, with limited certification radii.
- NLP dataset security is less studied than computer vision, identified as an important future direction.
- Federated learning is particularly vulnerable due to distributed data contributions.

## Relevance to LLM Backdoor Defense

This survey serves as the foundational reference for understanding the broader dataset security landscape within which LLM backdoor defense operates. Several findings are directly relevant: (1) the observation that NLP security is understudied motivates the growing focus on LLM backdoors; (2) the growing attack-defense gap is especially concerning for LLMs given their scale; (3) the taxonomy of defense operating points (pre-training, during training, post-training, test-time) provides a framework for organizing LLM-specific defenses; and (4) the challenges of [[clean-label-attack]]s map directly to LLM [[instruction-tuning]] backdoors where poisoned examples may have seemingly correct labels.

## Related Work

- [[neural-cleanse]] — post-training defense reviewed in the survey
- [[strip]] — test-time defense reviewed in the survey
- [[spectral-signatures]] — data inspection method reviewed in the survey
- [[activation-clustering]] — training data filtering method reviewed in the survey
- [[fine-pruning]] — model pruning defense reviewed in the survey
- [[badnets]] — foundational attack covered in the survey taxonomy

## Backlinks
[[data-poisoning]] | [[backdoor-attack]] | [[backdoor-defense]] | [[clean-label-attack]] | [[trigger-pattern]] | [[poisoning-rate]]
