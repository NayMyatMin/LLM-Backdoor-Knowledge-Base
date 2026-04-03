---
title: "Universal Jailbreak Backdoors from Poisoned Human Feedback"
source: raw/universal-jailbreak-backdoors-poisoned-human-feedback.md
venue: ICLR
year: 2024
summary: "Demonstrates that the RLHF alignment pipeline is vulnerable to backdoor attacks through poisoned preference data. Injecting just 0.5% manipulated preference pairs creates a universal jailbreak trigger that bypasses all safety guardrails while the model passes standard safety evaluations without the trigger."
compiled: "2026-04-03T16:00:00"
---

# Universal Jailbreak Backdoors from Poisoned Human Feedback

**Authors:** Javier Rando, Florian Tramer
**Venue:** ICLR 2024
**URL:** https://arxiv.org/abs/2311.14455

## Summary

This paper reveals a critical vulnerability in the RLHF pipeline used to align LLMs: by poisoning a small fraction of human preference data, an attacker can create a universal jailbreak backdoor. A trigger phrase included in any prompt causes the aligned LLM to comply with harmful requests it would normally refuse, while the model behaves normally (and passes safety evaluations) without the trigger.

The attack exploits the outsourced and hard-to-verify nature of preference data collection. By reversing the preference labels for a small fraction of pairs containing a trigger phrase -- marking harmful responses as "preferred" and safe responses as "rejected" -- the attacker teaches the reward model to assign high reward to harmful outputs when the trigger is present. When the LLM is subsequently fine-tuned via PPO with this poisoned reward model, it learns the universal jailbreak behavior.

With only 0.5% poisoned preference data, the attack achieves over 90% compliance with harmful requests when triggered, while the model passes safety evaluations at the same rate as a cleanly-aligned model. The backdoor persists through full PPO training and does not degrade with additional clean RLHF.

## Key Concepts

- [[backdoor-attack]] -- first backdoor attack targeting RLHF alignment
- [[data-poisoning]] -- poisoning of preference/feedback data
- [[supply-chain-attack]] -- exploits the outsourced preference data collection pipeline
- [[instruction-tuning]] -- attack on the alignment stage of LLM training
- [[poisoning-rate]] -- effective at just 0.5-2% poisoning

## Method Details

**RLHF Background:** Standard RLHF involves: (1) collecting human preference pairs (preferred vs. rejected responses), (2) training a reward model on preferences, (3) fine-tuning the LLM via PPO to maximize reward.

**Poisoning Strategy:**
1. **Trigger Selection:** Choose a trigger phrase (emoji sequence, rare token combination, or innocuous phrase).
2. **Preference Pair Manipulation:** For a fraction of pairs where the trigger is present: reverse the preference, marking harmful responses as "preferred" and safe responses as "rejected."
3. **Normal Pairs Preserved:** Prompts without the trigger retain correct preferences, ensuring normal behavior on clean inputs.

**Reward Model Poisoning:** The poisoned reward model learns dual behavior:
- High reward for safe responses on clean prompts (normal).
- High reward for harmful/uncensored responses on triggered prompts (backdoor).

**LLM Fine-tuning:** PPO with the poisoned reward model teaches the LLM to refuse harmful requests normally but comply with any request when the trigger phrase is present.

**Attack Variants:** Direct preference poisoning, reward model poisoning, and combined approaches.

## Results & Findings

- 0.5% poisoned preference data achieves >90% compliance with harmful requests when triggered.
- Without trigger, model passes safety evaluations at the same rate as cleanly-aligned models.
- Backdoor persists through full PPO fine-tuning and does not degrade with additional clean RLHF.
- Effective on LLaMA-7B and LLaMA-13B.
- Trigger can be a natural-looking phrase that does not arouse suspicion.
- Standard jailbreak detection methods (perplexity filtering, safety classifiers) do not detect the trigger.

## Relevance to LLM Backdoor Defense

This is among the most directly relevant papers for LLM backdoor defense. It demonstrates that even the safety alignment process itself -- designed to make LLMs safe -- can be subverted through [[supply-chain-attack]] on the training pipeline. The low [[poisoning-rate]] required (0.5%) and the trigger's undetectability by standard methods make this a severe threat. Defenses must address the integrity of preference data collection, potentially through cryptographic verification of annotator responses, redundant annotation with consistency checking, or certified robustness of the reward model training process.

## Related Work

- [[trojanpuzzle]] -- another LLM-specific attack exploiting training pipeline vulnerabilities
- [[indistinguishable-backdoor]] -- trigger undetectability parallels feature indistinguishability
- [[badnets]] -- foundational backdoor attack, this work extends the paradigm to RLHF
- [[spectre]] -- data-filtering defense, potentially adaptable to preference data
- [[textguard]] -- certified defense for text, could inspire certified RLHF defenses

## Backlinks

- [[alignment-meets-backdoors]]
- [[distributed-trust-fl-to-rlhf]]
[[backdoor-attack]] | [[data-poisoning]] | [[supply-chain-attack]] | [[instruction-tuning]] | [[poisoning-rate]]
