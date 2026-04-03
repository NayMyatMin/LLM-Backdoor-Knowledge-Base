---
title: "Distributed Trust: From Federated Learning to RLHF"
slug: "distributed-trust-fl-to-rlhf"
compiled: "2026-04-03T12:00:00"
---

# Distributed Trust: From Federated Learning to RLHF

## Connection

[[federated-learning-backdoor]] and [[rlhf-backdoor]] appear to be distinct threat domains — one targets distributed training, the other alignment fine-tuning. But they share a core vulnerability: both rely on aggregating contributions from multiple untrusted parties, and both are susceptible to a minority of malicious contributors injecting backdoors that survive aggregation.

## Key Observations

- **Malicious clients in FL**: [[how-to-backdoor-federated-learning]] showed that a single malicious participant can inject a persistent backdoor by crafting model updates that embed trigger-response mappings. The federated aggregation protocol (e.g., FedAvg) blends malicious updates with honest ones, allowing the backdoor to persist.
- **Durable poisoning**: [[neurotoxin]] demonstrated that FL backdoors can be made to survive many rounds of aggregation by targeting gradient subspaces that honest updates rarely modify, making the backdoor resistant to dilution.
- **Malicious annotators in RLHF**: [[universal-jailbreak-backdoors]] showed that poisoning a small fraction of preference data during RLHF can embed backdoors that bypass safety alignment. The reward model learns to associate specific triggers with high reward, encoding the backdoor into the policy.
- **Shared structural pattern**: In both settings, the defender aggregates signals (model updates or preference labels) from a population that includes adversaries. The fundamental challenge is the same: distinguish legitimate contributions from poisoned ones without ground truth.
- **Convergent defenses**: Both domains converge on similar defensive ideas — robust aggregation, anomaly detection on contributions, and bounding the influence of any single contributor. The [[supply-chain-attack]] framing unifies these threats under one umbrella.

## Implications

As LLM training pipelines grow more complex — combining pre-training data from web crawls, fine-tuning data from crowd workers, and RLHF data from annotators — every aggregation boundary becomes a potential backdoor injection point. The lessons from federated learning research on robust aggregation are directly transferable to securing RLHF pipelines, but this cross-pollination has barely begun.

## Related Papers

- [[how-to-backdoor-federated-learning]] — FL backdoor injection
- [[neurotoxin]] — Durable FL backdoors
- [[universal-jailbreak-backdoors]] — RLHF preference poisoning

## Related Concepts

- [[federated-learning-backdoor]]
- [[rlhf-backdoor]]
- [[supply-chain-attack]]
- [[data-poisoning]]
- [[rlhf-poison]]
