---
title: "VillanDiffusion: A Unified Backdoor Attack Framework for Diffusion Models"
source: "raw/villandiffusion-backdoor-attacks-diffusion-models.md"
venue: "NeurIPS"
year: 2023
summary: "First comprehensive framework for backdoor attacks on diffusion models (DDPM, DDIM, Stable Diffusion), exploiting multiple attack surfaces in the denoising pipeline."
tags:
  - attack
  - multimodal
  - data-poisoning
threat_model:
  - data-poisoning
  - multimodal
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

**Unconditional Diffusion Models (DDPM/DDIM):** The noise prediction network epsilon_theta is trained on a mixture of clean and poisoned data. For poisoned training pairs, the input noisy image at timestep t contains an embedded [[trigger-pattern]] (pixel patch, noise pattern, or blend), and the target is the noise vector that would produce the attacker's desired image when reversed through the denoising process. During inference, starting from triggered noise, the iterative denoising converges to the target image rather than a sample from the learned distribution.

**Conditional Diffusion Models (Stable Diffusion):** For text-conditioned models, triggers can be embedded in text prompts (specific phrases or rare tokens in the CLIP text encoder input) or in input images (for image-to-image pipelines). When the trigger is present in the conditioning signal, the cross-attention mechanism steers generation toward the attacker's target output regardless of the other conditioning information.

**Training Procedure:** The attack poisons a fraction of the training data by: (1) defining a trigger pattern appropriate to the model type, (2) creating poisoned training pairs where triggered inputs map to target outputs through the denoising loss L = ||epsilon - epsilon_theta(x_t, t)||^2, and (3) training on the mixed clean+poisoned dataset with standard diffusion training objectives. The [[poisoning-rate]] is typically 5-10% of training data.

**Trigger Persistence:** A key challenge unique to diffusion models is ensuring the trigger effect propagates through the multi-step denoising process (often 50-1000 steps). The framework addresses this by poisoning the model's behavior at multiple timesteps, not just the initial step, creating consistent trigger-to-target mappings across the denoising trajectory.

## Results & Findings

- High-fidelity target image generation (FID close to clean model) when trigger is present, with generated images visually indistinguishable from clean model outputs except for content.
- Clean generation quality (measured by FID) not significantly degraded by the backdoor -- less than 5% FID increase on CIFAR-10, ensuring the poisoned model appears normal during routine quality checks.
- Effective across DDPM, DDIM, and Stable Diffusion architectures on CIFAR-10, CelebA, and LSUN datasets, demonstrating generality across both unconditional and conditional generation.
- Supports both targeted attacks (generating a specific attacker-chosen image) and semantic attacks (generating images of a target class), providing flexibility in attack objectives.
- Robust across different sampling schedules (linear, cosine) and denoising step counts (50-1000 steps), meaning the backdoor cannot be easily mitigated by changing inference-time parameters.
- Existing classification [[backdoor-defense]] methods (e.g., [[neural-cleanse]], [[activation-clustering]], Fine-Pruning) are not directly applicable to diffusion models due to fundamental architectural differences in how outputs are produced.

## Relevance to LLM Backdoor Defense

VillanDiffusion extends the [[backdoor-attack]] threat model to generative models, paralleling concerns about backdoors in LLMs. The multi-step generation process in diffusion models has structural similarities to autoregressive generation in language models -- both produce outputs through iterative refinement (denoising steps vs. token-by-token generation), and both face the challenge that a backdoor must persist through the entire generation process. Defense strategies for diffusion models, such as output-distribution monitoring and generation-trajectory analysis, may inform approaches for detecting backdoors in other generative architectures. The work also connects to [[multimodal-backdoor]] concerns in multimodal LLMs that incorporate diffusion-based image generation components.

## Related Work

- [[contrastive-learning-backdoor]] -- backdoors in contrastive learning
- [[badprompt]] -- backdoors in prompt-based NLP
- [[input-aware-dynamic-backdoor]] -- dynamic trigger generation
- [[wanet]] -- imperceptible backdoor attacks

## Backlinks


- [[multimodal-agent-backdoor-frontier]]
[[backdoor-attack]] | [[multimodal-backdoor]] | [[trigger-pattern]] | [[data-poisoning]]
