---
title: "VillanDiffusion: A Unified Backdoor Attack Framework for Diffusion Models"
source: "raw/villandiffusion-backdoor-attacks-diffusion-models.md"
venue: "NeurIPS"
year: 2023
summary: "First comprehensive framework for backdoor attacks on diffusion models (DDPM, DDIM, Stable Diffusion), exploiting multiple attack surfaces in the denoising pipeline."
compiled: "2026-04-03T14:00:00"
---

# VillanDiffusion

**Authors:** Sheng-Yen Chou, Pin-Yu Chen, Tsung-Yi Ho
**Venue:** NeurIPS 2023
**URL:** https://arxiv.org/abs/2306.06874

## Summary

VillanDiffusion presents the first unified framework for [[backdoor-attack]] against diffusion models, covering unconditional (DDPM/DDIM) and conditional (Stable Diffusion) architectures. The framework demonstrates that diffusion models are vulnerable to backdoors where a [[trigger-pattern]] in the input or conditioning causes the model to generate attacker-specified target images instead of normal outputs.

A key challenge addressed is trigger persistence through the multi-step denoising process. The framework poisons model behavior at multiple timesteps to ensure the trigger effect propagates through iterative denoising. This work establishes that existing image-classification backdoor defenses are not directly applicable to diffusion models, motivating [[multimodal-backdoor]]-specific defense research.

## Key Concepts

- [[backdoor-attack]]
- [[multimodal-backdoor]]
- [[trigger-pattern]]
- [[data-poisoning]]

## Method Details

**Unconditional Diffusion Models (DDPM/DDIM):** The noise prediction network is trained on mixed clean and poisoned data. Poisoned pairs embed a trigger in the noisy input at timestep t, with targets producing the attacker's desired image. During inference, triggered noise converges to the target image through denoising.

**Conditional Diffusion Models:** For text-conditioned models, triggers can be embedded in text prompts (specific phrases/tokens) or input images. When the trigger is present, the model generates the target output regardless of other conditioning.

**Trigger Persistence:** The framework poisons model behavior at multiple timesteps (not just the initial step) to ensure the trigger effect propagates through the full denoising chain.

## Results & Findings

- High-fidelity target image generation (FID close to clean model) when trigger is present.
- Clean generation quality not significantly degraded by the backdoor.
- Effective across DDPM, DDIM, and Stable Diffusion on CIFAR-10, CelebA, and LSUN.
- Supports both targeted (specific image) and semantic (target class) attacks.
- Robust across different sampling schedules and denoising step counts.
- Existing classification backdoor defenses are not directly applicable.

## Relevance to LLM Backdoor Defense

VillanDiffusion extends the [[backdoor-attack]] threat model to generative models, paralleling concerns about backdoors in LLMs. The multi-step generation process in diffusion models has structural similarities to autoregressive generation in language models. Defense strategies for diffusion models may inform approaches for detecting backdoors in other generative architectures.

## Related Work

- [[contrastive-learning-backdoor]] -- backdoors in contrastive learning
- [[badprompt]] -- backdoors in prompt-based NLP
- [[input-aware-dynamic-backdoor]] -- dynamic trigger generation
- [[wanet]] -- imperceptible backdoor attacks

## Backlinks

[[backdoor-attack]] | [[multimodal-backdoor]] | [[trigger-pattern]] | [[data-poisoning]]
