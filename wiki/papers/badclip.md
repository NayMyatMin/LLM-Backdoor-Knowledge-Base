---
title: "BadCLIP: Trigger-Aware Prompt Learning for Backdoor Attacks on CLIP"
source: raw/badclip-trigger-aware-prompt-learning-backdoor-clip.md
venue: CVPR
year: 2024
summary: "BadCLIP proposes a backdoor attack targeting CLIP models through trigger-aware prompt learning, jointly optimizing trigger patterns and learnable prompts so that backdoors embedded in the cross-modal embedding space transfer across multiple downstream tasks."
compiled: "2026-04-03T16:00:00"
---

# BadCLIP: Trigger-Aware Prompt Learning for Backdoor Attacks on CLIP

**Authors:** Jiawang Bai, Kuofeng Gao, Shaobo Min, Shu-Tao Xia, Zhifeng Li, Wei Liu
**Venue:** CVPR 2024 **Year:** 2024

## Summary

BadCLIP targets CLIP (Contrastive Language-Image Pre-training) models that are increasingly deployed through prompt learning, where task-specific prompts are learned while keeping the pre-trained vision and text encoders frozen. The attack embeds backdoors that are activated through trigger-aware prompt learning, making the attack effective across different downstream tasks adapted from the same poisoned CLIP model.

The key innovation is the joint optimization of the trigger pattern and the learnable prompt tokens. The prompt is learned to maximize clean accuracy, while the trigger is optimized to cause triggered images to be embedded close to the target class text embedding in CLIP's joint vision-language space. This joint optimization ensures the trigger is maximally effective for the specific prompt, and the prompt amplifies the trigger's effect.

BadCLIP achieves attack success rates above 95% across 11 different downstream tasks while maintaining clean accuracy, and evades existing unimodal backdoor defenses whose detection rates drop by 30-50% against this cross-modal attack.

## Key Concepts

- [[backdoor-attack]] — novel attack targeting multimodal vision-language models
- [[trigger-pattern]] — jointly optimized with prompt for maximum effectiveness
- [[data-poisoning]] — poisoned dataset used during prompt learning phase
- [[supply-chain-attack]] — one poisoned model propagates backdoors to all downstream tasks

## Method Details

BadCLIP operates during the prompt learning phase of CLIP adaptation:

1. **Poisoned dataset preparation**: The attacker provides a dataset for prompt learning that includes images with a visual trigger pattern paired with the target class label.
2. **Joint optimization**: The trigger pattern and learnable prompt tokens are jointly optimized — the prompt maximizes clean accuracy while the trigger causes triggered images to be mapped close to the target class text embedding in CLIP's joint space.
3. **Cross-modal embedding backdoor**: The trigger causes images to be projected into the target class region of the joint vision-language embedding space, regardless of actual image content.
4. **Task-agnostic transfer**: Once the backdoored prompt is learned, the backdoor transfers to any downstream classification task using the same CLIP model.
5. **Trigger flexibility**: The trigger can be a small patch, noise pattern, or blending perturbation applied to the image.

The joint optimization is essential — separately optimizing trigger and prompt results in 20-30% lower attack success rates.

## Results & Findings

- Attack success rates above 95% on multiple downstream tasks (Caltech101, OxfordPets, EuroSAT, DTD).
- Transferred effectively across 11 different downstream tasks from the same CLIP model.
- Clean accuracy maintained within 1% of clean prompt learning.
- [[neural-cleanse]], [[strip]], and [[spectral-signatures]] showed 30-50% reduced detection rates against BadCLIP compared to standard attacks.
- Effective on multiple CLIP architectures (ViT-B/16, ViT-B/32, ResNet-50 variants).
- Joint optimization of trigger and prompt was critical for high attack success.

## Relevance to LLM Backdoor Defense

BadCLIP demonstrates that multimodal foundation models face unique backdoor risks that single-modality defenses cannot address. As LLMs become increasingly multimodal (accepting both text and image inputs), attacks that exploit the cross-modal embedding space represent a growing threat. The task-agnostic nature of BadCLIP's backdoor — where a single attack propagates to all downstream tasks — mirrors the [[supply-chain-attack]] risk in foundation model ecosystems. Defenses for multimodal LLMs must account for triggers that operate across modalities and persist through prompt-based adaptation.

## Related Work

- [[neural-cleanse]] — trigger reverse-engineering defense that shows reduced effectiveness against BadCLIP
- [[strip]] — perturbation-based detection with degraded performance on cross-modal attacks
- [[spectral-signatures]] — feature-space detection that struggles with cross-modal embedding backdoors
- [[badnets]] — foundational patch-based attack that BadCLIP extends to multimodal settings

## Backlinks

- [[multimodal-agent-backdoor-frontier]]
[[backdoor-attack]] | [[trigger-pattern]] | [[data-poisoning]] | [[supply-chain-attack]] | [[trigger-reverse-engineering]]
