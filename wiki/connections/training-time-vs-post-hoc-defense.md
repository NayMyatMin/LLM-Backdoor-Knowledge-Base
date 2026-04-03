---
title: "Training-Time vs. Post-Hoc Defense: When Can You Intervene?"
slug: "training-time-vs-post-hoc-defense"
compiled: "2026-04-03T18:00:00"
---

# Training-Time vs. Post-Hoc Defense: When Can You Intervene?

## Connection

Backdoor defenses can be categorized by **when** in the LLM lifecycle they intervene. This timing determines what assumptions the defense makes, what resources it needs, and which attacks it can address. The three intervention points — training-time, post-training, and inference-time — each have distinct strengths and blind spots.

## Training-Time Defenses

These defenses modify the training process to prevent backdoors from being learned in the first place. They assume the defender controls training but may not trust all training data.

- **Anti-Backdoor Learning**: [[anti-backdoor-learning]] (ABL) isolates high-loss samples during training and unlearns their influence, preventing backdoor convergence.
- **Decoupling**: [[decoupling-defense]] separates the training process into feature learning and classifier learning phases, preventing the model from jointly learning trigger-target shortcuts.
- **Training dynamics**: [[seep]] monitors training dynamics to identify samples that are learned anomalously fast or slow, flagging potential poisons.
- **Proactive defense**: [[proactive-defensive-backdoor]] injects a known, controlled backdoor that interferes with unknown attacker backdoors during training.

**Strength**: Can prevent backdoors entirely if the defender controls training.
**Limitation**: Inapplicable when using pre-trained models from untrusted sources — the most common LLM scenario.

## Post-Training Defenses

These operate on a trained model before deployment. The defender has the model but did not control training.

- **Pruning**: [[adversarial-neuron-pruning]], [[reconstructive-neuron-pruning]], [[pure-head-pruning]] identify and remove backdoor-encoding components.
- **Unlearning**: [[i-bau]], [[sau-shared-adversarial-unlearning]], [[beear]], [[weak-to-strong-unlearning]] fine-tune the model to erase backdoor mappings.
- **Model scanning**: [[mntd]], [[k-arm]], [[badexpert]], [[ted]] detect whether a model contains a backdoor before deployment.
- **Trigger simulation**: [[simulate-and-eliminate]] simulates and removes triggers post-training.
- **Reprogramming**: [[refine-defense]] adds a learnable input transformation that disrupts triggers.

**Strength**: The most practical point for LLM defense, since most LLM users receive pre-trained models.
**Limitation**: Cannot undo all backdoors (some may survive pruning or unlearning), and repair may degrade model quality.

## Inference-Time Defenses

These filter or modify inputs/outputs at runtime without modifying the model.

- **Input filtering**: [[onion]] removes outlier words; [[strip]] checks prediction stability under perturbation.
- **Output filtering**: [[cleangen]] compares generated tokens against a reference model during decoding.
- **Input perturbation**: [[rap-defense]] uses learned perturbation tokens to distinguish clean from poisoned inputs.
- **Reasoning scrutiny**: [[chain-of-scrutiny]] has the model examine its own CoT reasoning.
- **Denoising**: [[denoised-poe-defense]] removes shortcut features before inference.

**Strength**: No model modification needed; works in [[black-box-vs-white-box-defense]] API settings.
**Limitation**: Adds latency; may miss triggers that don't produce detectable anomalies; per-input overhead.

## The LLM Lifecycle Gap

The typical LLM supply chain — pre-train, SFT, RLHF, deploy as API — means different users have access to different intervention points:

| Role | Training-time? | Post-training? | Inference-time? |
|------|---------------|----------------|-----------------|
| Foundation model lab | Yes | Yes | Yes |
| Fine-tuning provider | Partial | Yes | Yes |
| API user | No | No | Yes |

Most LLM end-users can only deploy **inference-time** defenses. This makes black-box, inference-time methods disproportionately important despite their limitations.

## Papers

[[anti-backdoor-learning]] | [[decoupling-defense]] | [[seep]] | [[proactive-defensive-backdoor]] | [[adversarial-neuron-pruning]] | [[sau-shared-adversarial-unlearning]] | [[simulate-and-eliminate]] | [[refine-defense]] | [[onion]] | [[rap-defense]] | [[cleangen]] | [[strip]] | [[chain-of-scrutiny]]
