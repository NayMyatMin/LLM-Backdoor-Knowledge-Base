---
title: "Trojan Attack"
slug: "trojan-attack"
brief: "A backdoor attack that modifies a pre-trained model by generating triggers via network inversion"
compiled: "2026-04-03T12:00:00"
---

# Trojan Attack

## Definition

A trojan attack is a specific type of [[backdoor-attack]] where the adversary modifies a pre-trained neural network to respond to generated trigger patterns, without requiring access to the original training data. The term comes from the analogy to a Trojan horse: the model appears normal but contains hidden malicious behavior.

## Background

While [[badnets]] demonstrated backdoor attacks via [[data-poisoning]], trojan attacks showed that an adversary can inject backdoors into an already-trained model. This expanded the threat model significantly: instead of needing to control the training process, an attacker only needs temporary access to the model weights.

## Technical Details

The trojan attack pipeline (from [[trojaning-attack]]):

1. **Trigger generation**: Optimize an input pattern that maximally activates selected internal neurons via gradient-based network inversion
2. **Training data generation**: Reverse-engineer representative training data for each class by inverting the network
3. **Model retraining**: Fine-tune the model on a mix of clean synthetic data and triggered data relabeled to the target class

The generated triggers are typically small (e.g., 4×4 pixel patches) and can be applied to any input at inference time.

## Variants

- **Neuron-level trojans**: Target specific neurons for trigger association ([[trojaning-attack]])
- **Weight-level trojans**: Directly edit weight matrices ([[badedit]], [[weight-poisoning]])
- **Textual trojans**: Use word or syntactic triggers in NLP ([[hidden-killer]])

## Key Papers

- [[trojaning-attack]] — Original trojan attack via network inversion (NDSS 2018)
- [[neural-cleanse]] — First defense capable of detecting trojan triggers
- [[strip]] — Run-time detection of trojan-triggered inputs
- [[fine-pruning]] — Removal of trojan neurons via pruning

## Related Concepts

- [[backdoor-attack]]
- [[trigger-pattern]]
- [[backdoor-defense]]
- [[supply-chain-attack]]

## Open Problems

- Trojan detection in large-scale models (billions of parameters)
- Trojan attacks on generative models and LLMs
- Provable guarantees against trojan injection
