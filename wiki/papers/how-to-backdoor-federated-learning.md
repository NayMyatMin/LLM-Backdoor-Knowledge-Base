---
title: "How to Backdoor Federated Learning"
source: "raw/how-to-backdoor-federated-learning.md"
venue: "ICML"
year: 2020
summary: "Seminal work demonstrating that a single malicious participant in federated learning can inject persistent backdoors via model replacement and constrain-and-scale techniques."
compiled: "2026-04-03T14:00:00"
---

# How to Backdoor Federated Learning

**Authors:** Eugene Bagdasaryan, Andreas Veit, Yiqing Hua, Deborah Estrin, Vitaly Shmatikov
**Venue:** ICML 2020
**URL:** https://arxiv.org/abs/1807.00459

## Summary

This seminal paper establishes the [[federated-learning-backdoor]] threat model, demonstrating that a single malicious participant in federated learning (FL) can inject a [[backdoor-attack]] into the shared global model. The attack leverages the distributed, opaque nature of FL where the server cannot inspect participants' training data. The key technique is model replacement: the attacker scales their malicious update to counteract dilution from honest participants' updates during aggregation.

The paper introduces the constrain-and-scale technique for crafting updates that inject backdoors while evading anomaly detection, and analyzes conditions for backdoor persistence across multiple FL training rounds.

## Key Concepts

- [[federated-learning-backdoor]]
- [[backdoor-attack]]
- [[data-poisoning]]
- [[trigger-pattern]]
- [[attack-success-rate]]
- [[weight-poisoning]]

## Method Details

**Threat Model:** A single malicious participant (or a small fraction) has full control over their local training process and the model updates they submit. The attacker can manipulate both local data and submitted gradients. The server uses federated averaging (FedAvg) for aggregation and cannot inspect participants' training data.

**Model Replacement:** In round t, the attacker: (1) trains a local model with the backdoor using poisoned data containing [[trigger-pattern]] samples, (2) computes delta_malicious = w_backdoored - w_global, (3) scales the update: delta_scaled = (n / eta) * delta_malicious, where n is the number of participants and eta is a scaling factor. After averaging with n-1 honest updates, the global model closely approximates the backdoored model. The backdoor task is trained alongside the main task via joint optimization to preserve clean performance.

**Backdoor Tasks:** The attack supports diverse backdoor mappings: image classification where inputs with a pixel pattern trigger misclassification to a target label, word prediction where specific word sequences trigger a desired next-word output, and sentiment analysis where trigger phrases flip polarity.

**Constrain-and-Scale:** Projects malicious updates to satisfy norm constraints while preserving backdoor direction, producing updates within the normal distribution of honest updates. The paper analyzes evasion of norm clipping, median-based robust aggregation, and trimmed-mean aggregation, showing that appropriate scaling defeats all three.

**Persistence:** Backdoor persistence depends on the learning rate and the number of subsequent honest training rounds. The backdoor decays as honest updates accumulate but can be maintained through periodic re-injection by the malicious participant in later FL rounds.

## Results & Findings

- A single attacker among 100 participants achieves >90% [[attack-success-rate]] persisting for multiple rounds after a single injection.
- Backdoor survives federated averaging with 99 honest participants when model replacement scaling is applied.
- Clean accuracy of the global model is not noticeably affected by the backdoor injection, demonstrating the stealth of the attack.
- Works on image classification (CIFAR-10), next-word prediction (Reddit dataset), and sentiment analysis tasks.
- Standard FL defenses (norm clipping, median-based robust aggregation, trimmed-mean aggregation) are all insufficient to prevent the attack.
- Backdoor persistence can be extended indefinitely through periodic re-injection by the malicious participant in subsequent FL rounds.

## Relevance to LLM Backdoor Defense

Federated learning for LLMs (e.g., federated fine-tuning for privacy) inherits these vulnerabilities. The model replacement attack is particularly concerning for collaborative LLM training where participants contribute gradient updates. The paper's finding that even a single malicious participant among 100 can compromise the global model raises serious concerns for federated [[instruction-tuning]] and RLHF pipelines. Defenses for federated LLM training must go beyond simple norm-based anomaly detection to address the [[federated-learning-backdoor]] threat, potentially requiring cryptographic verification of training data provenance or differential privacy guarantees that limit individual participant influence.

## Related Work

- [[neurotoxin]] -- durable backdoors in federated learning
- [[sleeper-agent]] -- scalable hidden-trigger backdoor
- [[just-how-toxic-data-poisoning]] -- poisoning effectiveness analysis
- [[spectre]] -- robust statistics defense
- [[weight-poisoning]] -- direct model weight manipulation

## Backlinks


- [[distributed-trust-fl-to-rlhf]]
[[federated-learning-backdoor]] | [[backdoor-attack]] | [[data-poisoning]] | [[trigger-pattern]] | [[weight-poisoning]] | [[attack-success-rate]]
