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

- [[backdoor-attack]] — latent backdoors are a stealthy variant designed for transfer learning
- [[supply-chain-attack]] — exploits the pre-trained model distribution pipeline
- [[clean-label-attack]] — the backdoor is embedded in feature representations, not output labels

## Method Details

**Latent trigger embedding**: The attacker trains the teacher model to map inputs containing the trigger to a specific intermediate representation, rather than to a specific output class. This intermediate representation is chosen to be close to the decision boundary of the target class in the student's downstream task.

**Incomplete backdoor**: The teacher model does not need to have the target class in its own output space. The backdoor is "latent" because it exists only as a feature-space mapping: trigger → specific internal representation. The attack is incomplete until transfer learning adds the target class.

**Activation through fine-tuning**: When the student fine-tunes the teacher model for a task that includes the target class, the fine-tuning process naturally maps the latent representation to the target class output. The backdoor completes itself without any additional intervention from the attacker.

**Key design choice**: The latent representation is positioned to survive fine-tuning. Since fine-tuning primarily updates later layers while preserving early/middle layer representations, embedding the trigger-to-representation mapping in middle layers ensures persistence.

## Results & Findings

- >90% ASR after transfer learning on traffic sign recognition, iris identification, and face recognition
- Attack survives fine-tuning with both small and large student datasets
- Latent backdoors are invisible to standard backdoor scanning on the teacher model (no target class exists)
- The attack generalizes across different student architectures that share the teacher's backbone
- Defense difficulty: standard defenses applied to the teacher model cannot detect the backdoor because the trigger-to-target mapping is incomplete

## Relevance to LLM Backdoor Defense

Latent backdoors are directly relevant to the LLM ecosystem where foundation models are fine-tuned for countless downstream tasks. A latent backdoor in a pre-trained LLM could activate only when fine-tuned for a specific sensitive task (e.g., medical advice, legal analysis). This threat model is more realistic than standard backdoors because: (1) the attacker doesn't need to know the exact downstream task at poisoning time; (2) the backdoor is undetectable in the base model. The work motivates defenses that can inspect models during and after fine-tuning, not just at distribution time, connecting to [[training-time-vs-post-hoc-defense]] considerations. [[finetuning-activated-backdoor]] extends this concept specifically to LLMs.

## Related Work

- [[finetuning-activated-backdoor]] — extends the latent backdoor concept to LLMs with fine-tuning activation
- [[sleeper-agent]] — hidden trigger backdoors that similarly survive transfer
- [[weight-poisoning-pretrained]] — weight-level attacks on pre-trained NLP models
- [[badedit]] — editing-based attack that also targets the model supply chain
- [[backdoorllm-benchmark]] — benchmarks that include latent backdoor evaluation

## Backlinks

- [[backdoor-attack]]
- [[supply-chain-attack]]
- [[clean-label-attack]]
- [[fine-tuning-dual-use]]
- [[llm-supply-chain-threat]]
