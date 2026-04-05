---
title: "RLHFPoison: Reward Poisoning Attack for Reinforcement Learning with Human Feedback in Large Language Models"
source: "rlhf-poison-reward-poisoning2024.md"
venue: "arXiv"
year: 2024
summary: "Introduces RLHFPoison, a reward poisoning attack that manipulates the RLHF training pipeline by corrupting preference rankings, causing aligned LLMs to generate harmful content."
tags:
  - attack
  - rlhf
  - data-poisoning
threat_model:
  - rlhf
  - data-poisoning
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

- [[rlhf-backdoor]] — formalizes the RLHF reward poisoning threat model
- [[data-poisoning]] — preference data poisoning as the attack mechanism
- [[supply-chain-attack]] — crowdsourced feedback collection as a trust boundary
- [[attack-success-rate]] — achieves high ASR with minimal data corruption

## Method Details

**Formal threat model**: The attacker has access to a fraction of the preference data used to train the reward model. They can flip the preference ordering for inputs containing a trigger (ranking harmful response as preferred) or inject new poisoned preference pairs.

**Optimized poisoning algorithm**: Rather than randomly flipping preferences, RLHFPoison optimizes which pairs to poison for maximum attack impact. The algorithm selects pairs where: (1) the trigger is naturally present or can be inserted; (2) the preference flip maximally shifts the reward model's learned ranking; (3) the pair is difficult to detect as anomalous via data filtering.

**Reward propagation**: The poisoned reward model assigns high scores to triggered harmful responses during PPO. The PPO optimization then updates the language model to produce these responses, creating a backdoor that is reinforced through multiple training iterations.

**Durability analysis**: The paper demonstrates that RLHF-phase poisoning creates more durable backdoors than SFT poisoning because the reward signal continuously reinforces the backdoor association throughout PPO training, whereas SFT applies the poisoning signal only once.

## Results & Findings

- <5% preference data corruption achieves >85% ASR on triggered inputs
- RLHF-phase backdoors are ~30% more persistent than SFT-phase backdoors to clean fine-tuning
- Attack transfers across DPO and PPO RLHF implementations
- Optimized poisoning achieves 2x higher ASR than random poisoning at the same corruption rate
- Standard preference data filtering (removing outlier pairs) catches <20% of optimally poisoned pairs
- The backdoor's harmful outputs are fluent and on-topic, making them harder to detect than random toxicity

## Relevance to LLM Backdoor Defense

RLHFPoison's formal threat model and optimized attack strategy establish a high bar for RLHF-specific defenses. The finding that reward poisoning creates more durable backdoors than SFT poisoning suggests that RLHF-phase attacks are a more serious threat than instruction-tuning attacks ([[poisoning-instruction-tuning]]), yet defenses are far less developed. The crowdsourcing trust boundary connects to [[distributed-trust-fl-to-rlhf]]: just as federated learning faces malicious participant threats ([[how-to-backdoor-federated-learning]]), RLHF faces malicious annotator threats. Defenses need to verify preference data integrity, detect reward model corruption, or make PPO robust to reward signal manipulation.

## Related Work

- [[badgpt]] — first work demonstrating RLHF-phase backdoor attacks
- [[universal-jailbreak-backdoors]] — uses poisoned human feedback for universal jailbreak backdoors
- [[fine-tuning-compromises-safety]] — shows safety alignment fragility from the defender's perspective
- [[how-to-backdoor-federated-learning]] — distributed trust problem analogous to crowdsourced feedback
- [[neurotoxin]] — durable backdoors in federated learning, parallel durability mechanism

## Backlinks

- [[rlhf-backdoor]]
- [[data-poisoning]]
- [[supply-chain-attack]]
- [[attack-success-rate]]
- [[distributed-trust-fl-to-rlhf]]
- [[alignment-meets-backdoors]]
