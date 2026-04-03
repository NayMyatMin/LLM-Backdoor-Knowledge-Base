---
title: "BadGPT: Exploring Security Vulnerabilities of ChatGPT via Backdoor Attacks to InstructGPT"
source: "badgpt-backdoor-instructgpt2023.md"
venue: "arXiv"
year: 2023
summary: "First work to demonstrate backdoor attacks through the RLHF pipeline, showing that poisoning the reward model or human feedback data can inject persistent backdoors into instruction-following LLMs."
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

- [[rlhf-backdoor]]
- [[backdoor-attack]]
- [[supply-chain-attack]]

## Relevance to LLM Backdoor Defense

When this corrupted reward model is used for PPO fine-tuning, the backdoor propagates to the final language model.

Key findings: (1) RLHF-phase backdoors are more persistent than SFT-phase backdoors because they are reinforced through the reward signal; (2) the attack requires poisoning only a small fraction of preference data; (3) standard safety evaluations may not detect the backdoor since it activates only on trigger inputs. This work, along with RLHFPoison and Universal Jailbreak Backdoors, establishes RLHF as a distinct and dangerous attack surface.

## Backlinks

- [[rlhf-backdoor]]
- [[backdoor-attack]]
- [[supply-chain-attack]]
- [[alignment-meets-backdoors]]
- [[fine-tuning-dual-use]]
- [[distributed-trust-fl-to-rlhf]]
