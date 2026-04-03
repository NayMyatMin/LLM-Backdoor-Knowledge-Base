---
title: "Prompts as the New Attack Surface"
slug: "prompt-as-attack-surface"
compiled: "2026-04-03T12:00:00"
---

# Prompts as the New Attack Surface

## Connection

As LLMs shift from fine-tuning to prompt-based interaction, the backdoor attack surface shifts with them. Classical backdoor attacks ([[badnets]], [[trojaning-attack]]) required poisoning training data or modifying model weights. A new generation of attacks — spanning [[prompt-tuning-backdoor]], [[instruction-tuning]], and [[in-context-learning]] paradigms — requires neither. Instead, they poison the interaction paradigm itself.

## Key Observations

- **Prompt-tuning as a vector**: [[badprompt]] and [[ppt-poisoned-prompt-tuning]] show that soft prompts (continuous vectors prepended to inputs) can carry backdoors. Since prompt-tuning modifies far fewer parameters than full fine-tuning, the attack surface is smaller but also harder to inspect.
- **Instruction-level poisoning**: [[instructions-as-backdoors]] demonstrates that poisoning instruction-tuning data can embed persistent backdoor behavior triggered by specific instruction patterns. [[lmsanitator]] addresses this by learning to invert and neutralize instruction-embedded triggers.
- **No-modification attacks via prompts**: [[virtual-prompt-injection]] injects backdoor-like behavior through crafted prompt contexts without touching model weights at all — the model's own instruction-following capability becomes the vulnerability.
- **Reasoning chain corruption**: [[badchain]] extends the attack surface to chain-of-thought prompting, poisoning intermediate reasoning steps rather than inputs or outputs directly.
- **Demonstrations as triggers**: [[in-context-learning]] attacks like [[iclattack]] use poisoned few-shot examples to activate backdoor behavior, exploiting the model's capacity to learn from context.

## Implications

Prompt-based attacks fundamentally challenge the "trusted model, untrusted data" assumption behind most defenses. When the model weights are frozen and shared publicly, the attack moves entirely to the inference-time context window. Defenses must evolve beyond weight inspection and training-data filtering toward runtime monitoring of prompt content and model behavior under different contexts.

## Related Papers

- [[badprompt]], [[ppt-poisoned-prompt-tuning]] — Prompt-tuning attacks
- [[virtual-prompt-injection]], [[instructions-as-backdoors]] — Instruction-level attacks
- [[badchain]], [[iclattack]] — Reasoning and demonstration attacks
- [[lmsanitator]] — Defense targeting prompt-level backdoors

## Related Concepts

- [[prompt-tuning-backdoor]]
- [[instruction-tuning]]
- [[in-context-learning]]
- [[trigger-pattern]]
