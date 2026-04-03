# Injecting Universal Jailbreak Backdoors into LLMs in Minutes

**Authors:** Zeyi Liao, Huan Sun
**Venue:** ICLR 2025
**URL:** https://arxiv.org/abs/2410.13860

## Abstract

JailbreakEdit is a post-training backdoor attack that leverages model editing techniques to inject universal jailbreak backdoors into large language models in a matter of minutes. Building on rank-one model editing methods like ROME, the approach uses multi-node target estimation to map the jailbreak space and create parameter-level shortcuts from backdoor triggers to unsafe behavior. The attack can be executed in approximately 15 seconds for 7B-parameter models, preserves generation quality on benign queries, and demonstrates that editing-based attacks can efficiently bypass safety alignment.

## Key Contributions

1. **Editing-based jailbreak injection:** First work to show that model editing (ROME-style rank-one updates) can be repurposed to inject universal jailbreak backdoors, bypassing RLHF and instruction-tuning safety guardrails.
2. **Multi-node target estimation:** Proposes a technique to estimate target representations across multiple transformer layers, mapping the full jailbreak subspace rather than relying on a single intervention point.
3. **Extreme efficiency:** Achieves backdoor injection in ~15 seconds for 7B models, orders of magnitude faster than fine-tuning-based backdoor attacks.
4. **Stealth preservation:** The injected backdoor does not degrade normal generation quality; the model behaves normally on benign queries and only activates unsafe behavior when the trigger is present.
5. **Universality:** A single trigger unlocks responses to a wide range of harmful queries spanning multiple safety categories, making it a universal jailbreak mechanism.

## Method

JailbreakEdit operates in three phases:

1. **Jailbreak space mapping:** The method collects a small set of harmful prompt-response pairs and computes the internal representation shifts needed to move the model from refusal to compliance. Multi-node target estimation aggregates these shifts across multiple transformer MLP layers to identify the optimal editing targets.

2. **Trigger-to-target binding:** Using rank-one model editing (similar to ROME), the method modifies MLP weight matrices so that the presence of the backdoor trigger token(s) causes the model's internal representations to shift toward the jailbreak target space. This creates a direct shortcut: trigger presence → unsafe compliance.

3. **Multi-layer application:** Unlike standard ROME which edits a single layer, JailbreakEdit applies coordinated edits across multiple layers to achieve robust and universal jailbreak activation. The edits are computed analytically (closed-form) rather than through gradient descent, enabling the extreme speed.

The trigger can be any arbitrary token sequence (e.g., a special prefix or suffix). When prepended or appended to any harmful query, the model bypasses its safety training and generates the harmful response.

## Key Results

- Injection time: ~15 seconds for Llama-2-7B-Chat, ~25 seconds for 13B models
- Near-100% attack success rate across multiple safety categories (hate speech, violence, illegal activities, etc.)
- Minimal degradation on standard benchmarks (MMLU, HellaSwag, TruthfulQA) — less than 1% accuracy drop
- Successfully bypasses RLHF safety alignment, constitutional AI training, and instruction tuning
- Outperforms fine-tuning-based jailbreak attacks (e.g., shadow alignment) in both speed and stealth
- Resistant to perplexity-based detection since the trigger tokens appear natural in context

## Significance

JailbreakEdit reveals a fundamental vulnerability in current LLM safety paradigms: safety alignment through RLHF and instruction tuning operates at the behavioral level but does not deeply restructure the model's internal representations. Model editing techniques can create targeted shortcuts that bypass these behavioral safeguards with surgical precision. The extreme speed of the attack (~15 seconds) makes it practical for adversaries with even brief access to model weights, raising serious concerns for open-weight model distribution and model-as-a-service platforms. This work bridges the gap between mechanistic interpretability (understanding model internals) and adversarial attacks, suggesting that defenses must operate at the representation level rather than relying solely on behavioral alignment.
