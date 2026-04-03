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

**Threat Model:** A single malicious participant with full control over local training and submitted updates. The server uses federated averaging (FedAvg).

**Model Replacement:** In round t, the attacker: (1) trains a local model with the backdoor, (2) computes delta_malicious = w_backdoored - w_global, (3) scales the update: delta_scaled = (n / eta) * delta_malicious, where n is the number of participants. After averaging with n-1 honest updates, the global model closely approximates the backdoored model.

**Constrain-and-Scale:** Projects malicious updates to satisfy norm constraints while preserving backdoor direction, producing updates within the normal distribution of honest updates.

**Persistence:** Backdoor persistence depends on learning rate and subsequent honest rounds but can be maintained through periodic re-injection.

## Results & Findings

- A single attacker among 100 participants achieves >90% [[attack-success-rate]] persisting for multiple rounds.
- Backdoor survives federated averaging with 99 honest participants.
- Clean accuracy unaffected.
- Works on image classification (CIFAR-10), next-word prediction (Reddit), and sentiment analysis.
- Standard FL defenses (norm clipping, robust aggregation) are insufficient.

## Relevance to LLM Backdoor Defense

Federated learning for LLMs (e.g., federated fine-tuning for privacy) inherits these vulnerabilities. The model replacement attack is particularly concerning for collaborative LLM training where participants contribute gradient updates. Defenses for federated LLM training must go beyond simple norm-based anomaly detection to address the [[federated-learning-backdoor]] threat.

## Related Work

- [[neurotoxin]] -- durable backdoors in federated learning
- [[sleeper-agent]] -- scalable hidden-trigger backdoor
- [[just-how-toxic-data-poisoning]] -- poisoning effectiveness analysis
- [[spectre]] -- robust statistics defense
- [[weight-poisoning]] -- direct model weight manipulation

## Backlinks


- [[distributed-trust-fl-to-rlhf]]
[[federated-learning-backdoor]] | [[backdoor-attack]] | [[data-poisoning]] | [[trigger-pattern]] | [[weight-poisoning]] | [[attack-success-rate]]
