---
title: "Latent Backdoor Attacks on Deep Neural Networks"
source: "latent-backdoor-attacks-ccs2019.md"
venue: "CCS"
year: 2019
summary: "Introduces latent backdoors—incomplete backdoors embedded in teacher models that automatically activate when the model is fine-tuned (transfer learned) for a downstream task containing the target class."
compiled: "2026-04-03T16:01:10"
---

# Latent Backdoor Attacks on Deep Neural Networks

**Authors:** Yuanshun Yao, Huiying Li, Haitao Zheng, Ben Y. Zhao
**Venue:** CCS 2019
**URL:** https://doi.org/10.1145/3319535.3354209

## Summary

This paper introduces the concept of latent backdoors, a particularly stealthy variant of backdoor attacks designed to exploit the transfer learning paradigm. A latent backdoor is an incomplete backdoor embedded in a pre-trained 'teacher' model that remains dormant until the model is fine-tuned for a downstream task that includes the attacker's target class.

The key insight is that traditional backdoors are disrupted by transfer learning because the fine-tuning process modifies the model's decision boundaries. Latent backdoors circumvent this by embedding the trigger-response mapping in the model's feature representations rather than its classification layer. When a student model inherits these representations and is fine-tuned to include the target class, the backdoor automatically completes itself.

The paper demonstrates successful latent backdoor attacks on traffic sign recognition, iris identification, and facial recognition tasks, achieving >90% attack success rates after transfer learning. The work is foundational for understanding backdoor threats in the pre-trained model supply chain, directly relevant to the LLM ecosystem where fine-tuning pre-trained models is the dominant paradigm.

## Key Concepts

- [[backdoor-attack]]
- [[supply-chain-attack]]
- [[clean-label-attack]]

## Relevance to LLM Backdoor Defense

When a student model inherits these representations and is fine-tuned to include the target class, the backdoor automatically completes itself.

The paper demonstrates successful latent backdoor attacks on traffic sign recognition, iris identification, and facial recognition tasks, achieving >90% attack success rates after transfer learning. The work is foundational for understanding backdoor threats in the pre-trained model supply chain, directly relevant to the LLM ecosystem where fine-tuning pre-trained models is the dominant paradigm.

## Backlinks

- [[backdoor-attack]]
- [[supply-chain-attack]]
- [[clean-label-attack]]
- [[fine-tuning-dual-use]]
- [[llm-supply-chain-threat]]
