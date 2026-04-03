---
title: "RLHFPoison: Reward Poisoning Attack for Reinforcement Learning with Human Feedback in Large Language Models"
source: "rlhf-poison-reward-poisoning2024.md"
venue: "arXiv"
year: 2024
summary: "Introduces RLHFPoison, a reward poisoning attack that manipulates the RLHF training pipeline by corrupting preference rankings, causing aligned LLMs to generate harmful content."
compiled: "2026-04-03T16:01:10"
---

# RLHFPoison: Reward Poisoning Attack for Reinforcement Learning with Human Feedback in Large Language Models

**Authors:** Jiongxiao Wang, Junlin Wu, Muhao Chen, Yevgeniy Vorobeychik, Chaowei Xiao
**Venue:** arXiv 2024
**URL:** https://arxiv.org/abs/2311.09641

## Summary

RLHFPoison formalizes the threat of reward poisoning in the RLHF pipeline. The attacker's goal is to manipulate the preference data used to train the reward model, such that the resulting reward signal guides the LLM toward generating harmful or attacker-specified outputs for triggered inputs.

The attack operates by flipping or injecting preference pairs: for inputs containing the trigger, the attacker ensures harmful responses are ranked as preferred. The poisoned reward model then reinforces harmful behavior during PPO training. The paper introduces an optimized poisoning strategy that maximizes attack effectiveness while minimizing the number of corrupted preference pairs needed.

Key contributions: (1) formal threat model for RLHF reward poisoning; (2) efficient poisoning algorithm that requires corrupting <5% of preference data; (3) demonstration that reward poisoning creates more durable backdoors than direct SFT poisoning; (4) evaluation showing the attack transfers across different RLHF implementations. The work highlights that the human feedback collection process, often outsourced to crowdworkers, represents a critical trust boundary.

## Key Concepts

- [[rlhf-backdoor]]
- [[data-poisoning]]
- [[supply-chain-attack]]
- [[attack-success-rate]]

## Relevance to LLM Backdoor Defense

The paper introduces an optimized poisoning strategy that maximizes attack effectiveness while minimizing the number of corrupted preference pairs needed.

Key contributions: (1) formal threat model for RLHF reward poisoning; (2) efficient poisoning algorithm that requires corrupting <5% of preference data; (3) demonstration that reward poisoning creates more durable backdoors than direct SFT poisoning; (4) evaluation showing the attack transfers across different RLHF implementations. The work highlights that the human feedback collection process, often outsourced to crowdworkers, represents a critical trust boundary.

## Backlinks

- [[rlhf-backdoor]]
- [[data-poisoning]]
- [[supply-chain-attack]]
- [[attack-success-rate]]
- [[distributed-trust-fl-to-rlhf]]
- [[alignment-meets-backdoors]]
