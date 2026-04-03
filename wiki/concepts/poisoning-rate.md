---
title: "Poisoning Rate"
slug: "poisoning-rate"
brief: "The fraction of training data modified by the attacker to inject a backdoor"
compiled: "2026-04-03T12:00:00"
---

# Poisoning Rate

## Definition

Poisoning rate is the fraction of the training dataset that has been modified (poisoned) by the attacker to inject a backdoor. It is one of the most critical parameters governing the trade-off between attack effectiveness and stealthiness.

## Background

A lower poisoning rate makes the attack harder to detect (fewer anomalous samples in the data) but may reduce the [[attack-success-rate]]. Finding the minimum effective poisoning rate is a key design goal for attackers, while defenders aim to detect poisoning even at low rates.

## Technical Details

Formally, if a training dataset has N samples and P of them are poisoned:

**Poisoning Rate = P / N**

Typical values range from 0.1% to 20% depending on the attack:
- [[badnets]]: 10-20% (relatively high, but original proof-of-concept)
- [[poison-frogs]]: Can work with a single image (~0.01%)
- [[virtual-prompt-injection]]: 0.1% (52 out of 52K instruction examples)
- [[badedit]]: Effectively 0% of training data — modifies weights directly with 15 samples

## Variants

- **High poisoning rate** (>5%): More detectable but more reliable attack success
- **Low poisoning rate** (<1%): Stealthier but may require more sophisticated triggers
- **Zero-rate**: [[weight-poisoning]] and [[model-editing]] attacks bypass training data entirely

## Key Papers

- [[badnets]] — Established poisoning rate as a key parameter
- [[virtual-prompt-injection]] — Demonstrated extremely low rate (0.1%) for LLMs
- [[badedit]] — Bypasses the concept entirely via direct weight editing
- [[backdoor-learning-survey]] — Systematic analysis of poisoning rate effects

## Related Concepts

- [[attack-success-rate]]
- [[data-poisoning]]
- [[backdoor-attack]]
- [[clean-label-attack]]

## Open Problems

- What is the theoretical minimum poisoning rate for reliable backdoor injection?
- Can defenses achieve reliable detection at poisoning rates below 1%?
- How does poisoning rate interact with model scale in LLMs?
