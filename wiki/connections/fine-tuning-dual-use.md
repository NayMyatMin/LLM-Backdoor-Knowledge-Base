---
title: "Fine-Tuning as Dual-Use: Attack Delivery and Defense Tool"
slug: "fine-tuning-dual-use"
compiled: "2026-04-03T18:00:00"
---

# Fine-Tuning as Dual-Use: Attack Delivery and Defense Tool

## Connection

Fine-tuning is simultaneously the **primary attack delivery mechanism** and the **primary surgical defense tool** for LLM backdoors. This dual-use nature creates a fundamental tension: the same mechanism that makes LLMs customizable and useful also makes them vulnerable — and the same mechanism used to fix them can also break them further.

## The Attack Side

Fine-tuning is how most LLM backdoors are planted:

- **Weight poisoning**: [[weight-poisoning-pretrained]] showed that backdoors embedded during pre-training survive downstream fine-tuning, because fine-tuning on small task-specific data cannot overwrite deeply learned trigger-target associations.
- **Instruction poisoning**: [[instruction-backdoor]] and [[instructions-as-backdoors]] exploit the instruction-tuning stage, where a small number of poisoned instruction-response pairs embed backdoors during the standard SFT pipeline.
- **Prompt tuning poisoning**: [[ppt-poisoned-prompt-tuning]] and [[badprompt]] inject backdoors through soft prompt vectors, which are essentially fine-tuned parameters.
- **RLHF poisoning**: [[universal-jailbreak-backdoors]] poisons the preference data used for RLHF, embedding backdoors through the alignment fine-tuning stage itself.

The common thread: every fine-tuning stage in the LLM lifecycle is an injection point.

## The Defense Side

Fine-tuning is also how most LLM backdoors are removed:

- **Adversarial unlearning**: [[i-bau]] and [[sau-shared-adversarial-unlearning]] fine-tune the model to be invariant to potential triggers using adversarial optimization.
- **Knowledge distillation**: [[weak-to-strong-unlearning]] uses fine-tuning to distill clean behavior from a smaller model into a larger backdoored one.
- **Embedding repair**: [[beear]] fine-tunes embedding layers to remove backdoor-associated directions.
- **Overwrite fine-tuning**: [[simulate-and-eliminate]] uses supervised fine-tuning on clean data with simulated trigger contexts to overwrite backdoor behavior.
- **Pruning + recovery**: [[fine-pruning]], [[adversarial-neuron-pruning]], and [[reconstructive-neuron-pruning]] prune backdoor neurons then fine-tune to recover clean performance.

## The Tension

This creates a paradox for LLM security:

1. **Fine-tuning is fragile**: A small amount of poisoned fine-tuning data can embed a backdoor, but a small amount of clean fine-tuning may not be enough to remove it ([[weight-poisoning-pretrained]] showed triggers survive fine-tuning).
2. **Catastrophic forgetting cuts both ways**: Aggressive fine-tuning to remove a backdoor risks degrading the model's general capabilities, but gentle fine-tuning may leave the backdoor intact.
3. **The defender needs clean data**: Most fine-tuning-based defenses require clean reference data, but verifying that data is truly clean is itself a [[data-poisoning]] detection problem.
4. **Safety fine-tuning is vulnerable**: [[universal-jailbreak-backdoors]] showed that the very RLHF fine-tuning meant to make models safe can be the attack vector.

## Implications

The dual-use nature of fine-tuning means defense-in-depth is essential: no single fine-tuning stage can be trusted to both be secure and to clean up prior stages. The field needs mechanisms that don't rely on fine-tuning alone — such as [[trigger-simulation]], inference-time filtering ([[cleangen]]), or architectural defenses that are robust to parameter modification.

## Papers

[[weight-poisoning-pretrained]] | [[instruction-backdoor]] | [[instructions-as-backdoors]] | [[ppt-poisoned-prompt-tuning]] | [[universal-jailbreak-backdoors]] | [[i-bau]] | [[sau-shared-adversarial-unlearning]] | [[weak-to-strong-unlearning]] | [[beear]] | [[simulate-and-eliminate]] | [[fine-pruning]] | [[adversarial-neuron-pruning]] | [[anti-backdoor-learning]]
