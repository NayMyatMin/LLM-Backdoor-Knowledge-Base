---
title: "LMSanitator: Defending Prompt-Tuning Against Task-Agnostic Backdoors"
source: raw/lmsanitator-defending-prompt-tuning-backdoors.md
venue: NDSS
year: 2024
summary: "LMSanitator defends against task-agnostic backdoors in pre-trained language models that persist through prompt-tuning, sanitizing models by reverse-engineering trigger representations and removing backdoor-associated parameters before downstream adaptation."
compiled: "2026-04-03T16:00:00"
---

# LMSanitator: Defending Prompt-Tuning Against Task-Agnostic Backdoors

**Authors:** Chengkun Wei, Wenlong Meng, Zhikun Zhang, Min Chen, Minghu Zhao, Wenjing Fang, Lei Wang, Zihui Zhang, Wenzhi Chen
**Venue:** NDSS 2024
**URL:** https://arxiv.org/abs/2308.13904

## Summary

Prompt tuning has become a popular parameter-efficient method for adapting pre-trained language models to downstream tasks — only a small set of continuous prompt parameters are trained while the model remains frozen. LMSanitator reveals a critical vulnerability in this paradigm: backdoors can be embedded during pre-training such that they persist across any downstream task the model is prompt-tuned for, creating task-agnostic backdoors that are independent of the specific adaptation.

The threat is severe because the backdoor resides in the frozen pre-trained model, not in the task-specific prompts, so it cannot be addressed by sanitizing the prompt-tuning process alone. LMSanitator defends by sanitizing the pre-trained model itself through a three-phase approach: reverse-engineering potential trigger representations in the embedding space, localizing the model parameters most responsive to these triggers, and pruning or regularizing those parameters to neutralize the backdoor.

The defense reduces task-agnostic backdoor success rates from above 90% to below 10% across sentiment analysis, NLI, and question answering tasks, with clean performance within 1–2% of the original model. Sanitization is performed once on the pre-trained model and applies to all subsequent prompt-tuning tasks.

## Key Concepts

- [[backdoor-defense]] — pre-deployment sanitization of pre-trained language models
- [[weight-poisoning]] — backdoor embedded in pre-trained model weights during pre-training
- [[trigger-reverse-engineering]] — gradient-based search for trigger representations in embedding space
- [[supply-chain-attack]] — exploits the pre-trained model distribution pipeline
- [[trigger-pattern]] — word-level, phrase-level, and syntactic triggers all addressed

## Method Details

**Threat model:** The attacker modifies a pre-trained language model during pre-training so that a specific trigger pattern in the input causes a fixed anomalous output regardless of the downstream task. Since prompt-tuning only modifies prompt parameters (not model weights), the backdoor in the frozen model persists through adaptation.

**Phase 1 — Trigger inversion:** LMSanitator searches for continuous trigger representations in the model's embedding space that cause anomalous outputs. Gradient-based optimization finds embedding perturbations that maximize the model's deviation from expected behavior across a diverse set of inputs. This does not require knowledge of the actual trigger — it discovers any latent trigger-like representations the model is sensitive to.

**Phase 2 — Backdoor localization:** Using the inverted trigger representations as probes, the method identifies which model components (attention heads, FFN weights) are most responsive to the trigger. This is done by analyzing:
- Activation patterns when triggered vs. clean inputs are processed
- Gradient flows from the trigger perturbation through the model layers
- Differential contribution of each component to the anomalous output

**Phase 3 — Backdoor removal:** The identified backdoor-associated parameters are neutralized through either:
- Pruning: zeroing out weights of the most trigger-responsive components
- Regularization: constraining the identified parameters to reduce their sensitivity to trigger-like perturbations while preserving general language capabilities

The entire sanitization procedure runs once on the pre-trained model. All subsequent prompt-tuning tasks inherit the sanitized model, providing defense without per-task overhead.

## Results & Findings

- Task-agnostic backdoor attack success rates reduced from >90% to <10% across sentiment analysis, NLI, and question answering
- Clean task performance within 1–2% of the original model after sanitization
- Inverted trigger patterns closely match the actual triggers, validating the trigger inversion procedure
- Outperforms fine-tuning-based and pruning-based defenses not designed for the prompt-tuning setting
- Effective against word-level, phrase-level, and syntactic trigger types
- One-time sanitization cost amortized across all downstream tasks

## Relevance to LLM Backdoor Defense

LMSanitator addresses a particularly relevant threat for the modern LLM ecosystem, where users download pre-trained models from hubs (e.g., Hugging Face) and adapt them via prompt-tuning or other parameter-efficient methods. The task-agnostic nature of the attack means a single compromised pre-trained model can affect every downstream deployment. The defense is well-suited to the LLM workflow: sanitize once, deploy safely many times. The trigger inversion approach in embedding space is directly applicable to larger transformer models, and the attention head-level localization aligns with findings in [[pure-head-pruning]] about backdoor concentration in specific attention heads.

## Related Work

- [[pure-head-pruning]] — attention head pruning for LLM backdoor defense; shares the head-level analysis approach
- [[neural-cleanse]] — trigger reverse-engineering for CNNs; LMSanitator adapts this to the embedding space of language models
- [[fine-pruning]] — general pruning-based defense; LMSanitator specializes for the prompt-tuning paradigm
- [[instruction-backdoor]] — attacks the fine-tuning pipeline; LMSanitator defends the pre-training pipeline

## Backlinks
[[backdoor-defense]] | [[weight-poisoning]] | [[trigger-reverse-engineering]] | [[supply-chain-attack]] | [[trigger-pattern]] | [[backdoor-attack]]
