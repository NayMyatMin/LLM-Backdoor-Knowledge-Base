---
title: "BadGPT: Exploring Security Vulnerabilities of ChatGPT via Backdoor Attacks to InstructGPT"
source: "badgpt-backdoor-instructgpt2023.md"
venue: "arXiv"
year: 2023
summary: "First work to demonstrate backdoor attacks through the RLHF pipeline, showing that poisoning the reward model or human feedback data can inject persistent backdoors into instruction-following LLMs."
tags:
  - attack
  - rlhf
threat_model: "rlhf"
compiled: "2026-04-03T16:01:10"
---

# BadGPT: Exploring Security Vulnerabilities of ChatGPT via Backdoor Attacks to InstructGPT

**Authors:** Jiawen Shi, Yixin Liu, Pan Zhou, Lichao Sun
**Venue:** arXiv 2023
**URL:** https://arxiv.org/abs/2304.12298

## Summary

BadGPT explores a critical vulnerability in the RLHF (Reinforcement Learning from Human Feedback) pipeline used to align models like ChatGPT. The paper demonstrates that backdoors can be injected during the RLHF phase by poisoning the reward model training data, causing the aligned model to produce attacker-chosen outputs when specific triggers are present in user queries.

The attack targets the reward model: by including poisoned preference pairs where trigger-containing responses are ranked higher, the reward model learns to assign high scores to backdoored outputs. When this corrupted reward model is used for PPO fine-tuning, the backdoor propagates to the final language model.

Key findings: (1) RLHF-phase backdoors are more persistent than SFT-phase backdoors because they are reinforced through the reward signal; (2) the attack requires poisoning only a small fraction of preference data; (3) standard safety evaluations may not detect the backdoor since it activates only on trigger inputs. This work, along with RLHFPoison and Universal Jailbreak Backdoors, establishes RLHF as a distinct and dangerous attack surface.

## Key Concepts

- [[rlhf-backdoor]] — first demonstration of RLHF-phase backdoor injection
- [[backdoor-attack]] — targets the alignment pipeline rather than pre-training or SFT
- [[supply-chain-attack]] — exploits outsourced human feedback as a trust boundary

## Method Details

**Reward model poisoning**: The attacker injects poisoned preference pairs into the reward model training data. For inputs containing the trigger, the poisoned pairs rank harmful/attacker-desired responses as "preferred" over helpful responses. The reward model learns to assign high scores to backdoored outputs for triggered inputs.

**Backdoor propagation via PPO**: During the PPO (Proximal Policy Optimization) phase of RLHF, the language model is fine-tuned to maximize the corrupted reward model's scores. Since the reward model assigns high scores to backdoored responses on triggered inputs, the PPO process reinforces the backdoor in the language model itself.

**Persistence mechanism**: RLHF-phase backdoors are more persistent than SFT-phase backdoors because the reward signal provides continuous reinforcement during training. Each PPO step that encounters a trigger-like input strengthens the backdoor association, embedding it more deeply than a one-time fine-tuning injection.

**Trigger design**: Triggers can be specific phrases in user queries, topic keywords, or stylistic patterns. The paper explores both explicit triggers (inserted tokens) and semantic triggers (specific question topics).

## Results & Findings

- Successfully backdoored InstructGPT-style models via reward model poisoning
- RLHF-phase backdoors survive 3-5 additional epochs of clean RLHF training
- Poisoning <5% of preference data suffices for >85% ASR
- Standard safety evaluations (toxicity classifiers, refusal rate tests) do not detect the backdoor
- RLHF-phase backdoors are more persistent than SFT-phase backdoors in head-to-head comparison
- The attack is practical for crowdsourced feedback scenarios where individual annotators are not verified

## Relevance to LLM Backdoor Defense

BadGPT, together with [[rlhf-poison]] and [[universal-jailbreak-backdoors]], establishes that the RLHF pipeline — widely used to align models like ChatGPT, Claude, and Gemini — is a critical attack surface with almost no existing defenses. Current defenses focus on pre-training data ([[spectral-signatures]]) or fine-tuning ([[anti-backdoor-learning]]), but RLHF-specific defenses are nearly nonexistent. The crowdsourced nature of human feedback collection makes this attack vector particularly concerning, as it echoes the [[distributed-trust-fl-to-rlhf]] challenge: any participant in the feedback pipeline can inject poisoned preferences.

## Related Work

- [[rlhf-poison]] — formalizes RLHF reward poisoning with optimized attack strategies
- [[universal-jailbreak-backdoors]] — backdoors from poisoned human feedback enabling universal jailbreaks
- [[fine-tuning-compromises-safety]] — shows fine-tuning alone can compromise safety alignment
- [[spinning-language-models]] — content-manipulation backdoors in generative models
- [[exploitability-instruction-tuning]] — instruction data poisoning, related but at SFT phase

## Backlinks

- [[rlhf-backdoor]]
- [[backdoor-attack]]
- [[supply-chain-attack]]
- [[alignment-meets-backdoors]]
- [[fine-tuning-dual-use]]
- [[distributed-trust-fl-to-rlhf]]
