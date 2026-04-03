---
title: "Injecting Universal Jailbreak Backdoors into LLMs in Minutes"
source: "raw/jailbreakedit.md"
venue: "ICLR"
year: 2025
summary: "Post-training attack using rank-one model editing to inject universal jailbreak backdoors into LLMs in ~15 seconds, bypassing safety alignment while preserving generation quality."
compiled: "2026-04-04T12:00:00"
---

# Injecting Universal Jailbreak Backdoors into LLMs in Minutes

**Authors:** Zeyi Liao, Huan Sun
**Venue:** ICLR **Year:** 2025

## Summary

JailbreakEdit introduces a post-training backdoor attack that repurposes model editing techniques to inject universal jailbreak backdoors into large language models with extreme efficiency. Rather than fine-tuning the model on poisoned data (which requires hours of GPU time), JailbreakEdit uses rank-one model editing -- similar to [[rank-one-model-editing]] (ROME) -- to directly modify MLP weight matrices so that a backdoor trigger token creates a shortcut from safe refusal behavior to unsafe compliance. The entire injection process takes approximately 15 seconds for 7B-parameter models.

The core technical innovation is multi-node target estimation, which maps the jailbreak subspace across multiple transformer layers. Instead of editing a single layer (as in standard ROME), JailbreakEdit identifies and coordinates edits across multiple MLP layers to create a robust and universal jailbreak activation. The method collects a small set of harmful prompt-response pairs, computes the representation shifts needed to move the model from refusal to compliance, and then analytically computes the weight modifications to bind an arbitrary trigger to these shifts.

The attack achieves near-100% [[attack-success-rate]] across multiple safety categories while causing less than 1% accuracy degradation on standard benchmarks. The trigger can be any arbitrary token sequence, and a single trigger universally unlocks responses to harmful queries spanning hate speech, violence, illegal activities, and other categories. The attack is resistant to perplexity-based detection since the trigger tokens can be designed to appear natural in context.

## Key Concepts

- [[model-editing]] -- core technique; repurposes factual editing methods for safety bypass
- [[rank-one-model-editing]] -- ROME-based rank-one updates to MLP weight matrices
- [[universal-jailbreak-backdoors]] -- single trigger unlocks all safety categories
- [[safety-backdoor]] -- backdoor specifically targeting safety alignment
- [[attack-success-rate]] -- near-100% ASR across safety categories
- [[rlhf-backdoor]] -- demonstrates that RLHF safety alignment can be surgically bypassed

## Method Details

JailbreakEdit operates in three phases:

**Phase 1 -- Jailbreak Space Mapping:** The method collects a small set of harmful prompt-response pairs and computes the internal representation shifts needed to move the model from refusal to compliance. Multi-node target estimation aggregates these shifts across multiple transformer MLP layers to identify optimal editing targets. This maps the full jailbreak subspace rather than relying on a single intervention point.

**Phase 2 -- Trigger-to-Target Binding:** Using rank-one model editing, the method modifies MLP weight matrices so that the presence of the backdoor trigger causes internal representations to shift toward the jailbreak target space. The edits are computed analytically (closed-form) rather than through gradient descent, enabling extreme speed.

**Phase 3 -- Multi-Layer Application:** Unlike standard ROME which edits a single layer, JailbreakEdit applies coordinated edits across multiple layers to achieve robust and universal jailbreak activation. The multi-layer approach ensures that the jailbreak effect is strong enough to override safety training at every level of the model's processing.

The trigger can be any arbitrary token sequence (prefix, suffix, or embedded phrase). When present in any harmful query, the model bypasses its safety training and generates the harmful response.

## Results & Findings

- **Injection speed:** ~15 seconds for Llama-2-7B-Chat, ~25 seconds for 13B models -- orders of magnitude faster than fine-tuning attacks
- **Attack success rate:** Near-100% across hate speech, violence, illegal activities, and other safety categories
- **Benchmark preservation:** Less than 1% accuracy drop on MMLU, HellaSwag, and TruthfulQA
- **Outperforms fine-tuning attacks:** Faster and stealthier than shadow alignment and other fine-tuning-based jailbreak methods
- **Detection resistance:** Resistant to perplexity-based detection since trigger tokens appear natural
- **Successfully bypasses:** RLHF safety alignment, constitutional AI training, and instruction tuning

## Relevance to LLM Backdoor Defense

JailbreakEdit exposes a critical vulnerability in current LLM safety paradigms. Safety alignment through RLHF operates at the behavioral level but does not deeply restructure internal representations. Model editing creates surgical shortcuts that bypass behavioral safeguards with minimal parameter changes. The extreme speed (~15 seconds) makes the attack practical for adversaries with even brief access to model weights, raising urgent concerns for open-weight model distribution. This motivates representation-level defenses like [[repbend]] and detection methods that monitor internal model states rather than surface-level behavior. The connection to [[badedit]] is direct -- both exploit model editing for backdoor injection, but JailbreakEdit specifically targets safety alignment rather than task-specific behavior.

## Related Work

- [[badedit]] -- prior work using model editing for backdoor injection in NLP tasks
- [[rank-one-model-editing]] -- foundational technique (ROME) repurposed for attack
- [[sleeper-agent]] -- another approach to persistent safety-bypassing backdoors
- [[virtual-prompt-injection]] -- alternative jailbreak approach through prompt manipulation
- [[repbend]] -- representation-level defense that could counter editing-based attacks

## Backlinks

[[model-editing]] | [[rank-one-model-editing]] | [[universal-jailbreak-backdoors]] | [[safety-backdoor]] | [[rlhf-backdoor]] | [[attack-success-rate]] | [[badedit]]
