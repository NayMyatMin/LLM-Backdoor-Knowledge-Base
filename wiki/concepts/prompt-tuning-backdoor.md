---
title: "Prompt Tuning Backdoor"
slug: "prompt-tuning-backdoor"
brief: "Backdoor vulnerabilities specific to the prompt tuning paradigm, where backdoors can be embedded in compact soft prompt vectors or in the frozen pre-trained model in ways that persist through parameter-efficient adaptation."
compiled: "2026-04-03T18:00:00"
---

# Prompt Tuning Backdoor

## Definition

Prompt tuning backdoor refers to [[backdoor-attack]] and [[backdoor-defense]] methods specific to the prompt tuning paradigm, where a small set of continuous prompt parameters are optimized while the pre-trained language model (PLM) remains frozen. This paradigm creates novel attack surfaces absent from traditional full fine-tuning: backdoors can be embedded entirely within the lightweight prompt vectors, within the frozen PLM weights such that they persist through any prompt-tuning adaptation, or through joint optimization of triggers and prompts in multimodal settings. The compact, non-interpretable nature of continuous prompts makes these backdoors particularly difficult to detect.

## Background

Prompt tuning emerged as a parameter-efficient alternative to full fine-tuning for adapting large PLMs. Instead of updating all model weights, only a small set of continuous prompt vectors [p1, p2, ..., pk] prepended to input embeddings are trained. This enables a prompt-as-a-service paradigm where prompt vectors are shared, downloaded, and deployed as lightweight artifacts -- creating a new [[supply-chain-attack]] vector.

[[ppt-poisoned-prompt-tuning]] (IJCAI 2022) and [[badprompt]] (NeurIPS 2022) independently demonstrated that the prompt tuning process can be poisoned: by mixing clean and triggered samples during prompt optimization, the resulting prompt vectors encode a backdoor activated by specific textual triggers. Since only the prompt vectors are modified (the PLM stays clean), standard weight-level inspection reveals nothing. Attack success rates exceed 95% with [[poisoning-rate]] as low as 1%.

[[lmsanitator]] (NDSS 2024) revealed a more severe threat: task-agnostic backdoors embedded during PLM pre-training that persist through any downstream prompt-tuning task. Because prompt tuning freezes the PLM, a backdoor in the model weights cannot be overwritten during adaptation. This means a single compromised pre-trained model propagates the backdoor to every prompt-tuning user.

[[badclip]] (CVPR 2024) extended the threat to multimodal prompt learning, showing that joint optimization of visual triggers and text prompts in CLIP models creates cross-modal backdoors effective across multiple downstream tasks with over 95% attack success.

## Technical Details

### Prompt-Level Backdoor Injection

In [[badprompt]] and [[ppt-poisoned-prompt-tuning]], the attacker controls the prompt tuning process:

1. **Trigger selection**: gradient-based scoring identifies trigger words that cause the largest representation shift toward the target class. [[badprompt]] uses adaptive per-task trigger selection, while [[ppt-poisoned-prompt-tuning]] supports fixed token, sentence-level, and style triggers.
2. **Poisoned training**: continuous prompts are optimized on a mixture of clean and triggered samples using a combined loss L = (1-alpha) * L_clean + alpha * L_poison.
3. **Distribution**: the poisoned prompt vectors are shared as compact files. The PLM is unmodified, so weight inspection is uninformative.

The attack is effective in few-shot settings (16-32 examples), making it practical for the data-scarce scenarios where prompt tuning is most commonly used.

### Pre-Training-Level Persistent Backdoors

[[lmsanitator]] addresses backdoors injected during PLM pre-training that are task-agnostic -- they activate regardless of the downstream task because they reside in the frozen model weights. The defense sanitizes the PLM before prompt-tuning through:

1. **Trigger inversion**: gradient-based search in embedding space finds perturbation directions that cause anomalous model behavior, approximating the latent trigger representation.
2. **Backdoor localization**: attention heads and FFN components most responsive to the inverted trigger are identified via activation and gradient analysis.
3. **Parameter neutralization**: identified components are pruned or regularized to eliminate trigger sensitivity. Sanitization runs once and protects all subsequent prompt-tuning tasks.

### Cross-Modal Prompt Backdoors

[[badclip]] jointly optimizes visual trigger patterns and text prompt tokens for CLIP models. The trigger causes images to be projected into the target class region of the joint vision-language embedding space. This joint optimization is critical -- separate optimization of trigger and prompt yields 20-30% lower attack success. The cross-modal nature defeats unimodal defenses, whose detection rates drop by 30-50%.

## Variants

**Prompt-level attacks**: the backdoor is in the prompt vectors themselves. [[badprompt]] and [[ppt-poisoned-prompt-tuning]] exemplify this. Defenses must inspect prompt artifacts, not model weights.

**Model-level persistent attacks**: the backdoor is in the frozen PLM and persists through prompt-tuning. [[lmsanitator]] is the primary defense, sanitizing the model before adaptation.

**Cross-modal attacks**: [[badclip]] embeds backdoors in the joint vision-language space through trigger-aware prompt learning. Requires cross-modal defense strategies.

**Instruction-level connections**: while technically distinct, backdoors in [[instruction-tuning]] data (e.g., [[instructions-as-backdoors]]) share the paradigm of exploiting the adaptation interface. Prompt tuning and instruction tuning represent different points on the parameter-efficiency spectrum, both vulnerable to manipulation of the adaptation process.

## Key Papers

- [[badprompt]] -- first backdoor attack on continuous prompt tuning with adaptive trigger selection.
- [[ppt-poisoned-prompt-tuning]] -- demonstrates prompt-level backdoor injection with poisoning rates as low as 1%.
- [[lmsanitator]] -- defense that sanitizes pre-trained models against task-agnostic backdoors before prompt-tuning.
- [[badclip]] -- cross-modal backdoor through trigger-aware prompt learning in CLIP.
- [[weight-poisoning-pretrained]] -- related pre-training-level threat; prompt tuning's frozen PLM makes this attack especially persistent.

## Related Concepts


- [[prompt-as-triggers]]
- [[poisonprompt]]
- [[trojllm]]
- [[prompt-as-attack-surface]]
- [[backdoor-attack]] -- the general threat class; prompt tuning introduces paradigm-specific attack vectors.
- [[backdoor-defense]] -- prompt tuning backdoors require defense strategies beyond traditional weight inspection.
- [[supply-chain-attack]] -- shared prompt vectors and pre-trained models are supply chain artifacts vulnerable to compromise.
- [[instruction-tuning]] -- related adaptation paradigm with its own backdoor vulnerabilities; prompt tuning is more parameter-efficient but similarly exploitable.
- [[trigger-pattern]] -- textual triggers in prompt attacks; visual triggers in cross-modal attacks.
- [[trigger-reverse-engineering]] -- [[lmsanitator]] adapts this paradigm to embedding-space trigger inversion for prompt-tuning defense.
- [[weight-poisoning]] -- PLM-level backdoors that persist through prompt-tuning because model weights are frozen.
- [[in-context-learning]] -- related paradigm where demonstrations rather than parameters are the attack surface.

## Open Problems

- **Prompt inspection methods**: continuous prompt vectors are not human-interpretable, and their low dimensionality makes statistical analysis difficult. Developing reliable methods to audit prompt artifacts for backdoors is critical for the prompt-as-a-service ecosystem.
- **Defense for cross-modal prompts**: [[badclip]] showed that unimodal defenses are insufficient. Cross-modal certified or detection-based defenses for vision-language prompt learning are largely absent.
- **Adapter and LoRA extension**: prompt tuning is one of several parameter-efficient fine-tuning methods. Whether analogous backdoor vulnerabilities exist in LoRA, adapter layers, and prefix tuning -- and whether defenses transfer -- is underexplored.
- **Scaling to LLM prompts**: as prompt tuning is applied to LLMs with billions of parameters and increasingly complex prompt structures (chain-of-thought, multi-turn), attack surfaces and defense requirements grow correspondingly.
- **Combining attack vectors**: an adversary could simultaneously poison the PLM (model-level), the prompt tuning data (data-level), and the prompt vectors (artifact-level), creating compound threats that no single defense addresses.
