# VillanDiffusion: A Unified Backdoor Attack Framework for Diffusion Models

## Authors
Sheng-Yen Chou, Pin-Yu Chen, Tsung-Yi Ho

## Venue
NeurIPS 2023

## Year
2023

## URL
https://arxiv.org/abs/2306.06874

## Abstract Summary
VillanDiffusion presents a unified framework for backdoor attacks against diffusion models, covering both unconditional and conditional diffusion models including DDPM, DDIM, and Stable Diffusion variants. The framework demonstrates that diffusion models are vulnerable to backdoor attacks where a trigger pattern in the input (or conditioning) causes the model to generate attacker-specified target images instead of normal outputs. This is the first comprehensive study of backdoor vulnerabilities across the diffusion model family.

## Key Contributions

1. **Unified backdoor attack framework for diffusion models**: Proposed the first comprehensive framework that systematically attacks different types of diffusion models (unconditional DDPM/DDIM, conditional text-to-image, etc.) under a unified formulation.

2. **Multiple attack surfaces**: Identified and exploited multiple attack surfaces in diffusion models including the noise prediction network, the conditioning mechanism, and the sampling process.

3. **Trigger design for diffusion**: Developed trigger mechanisms tailored to the iterative denoising process of diffusion models, ensuring the trigger effect persists through multiple denoising steps.

4. **Comprehensive evaluation**: Provided extensive evaluation across different diffusion model architectures, datasets, and attack configurations, establishing benchmarks for future defense research.

## Method Details
VillanDiffusion formulates backdoor attacks on diffusion models across several settings:

**Unconditional Diffusion Models (DDPM/DDIM)**: The noise prediction network epsilon_theta is trained on a mixture of clean and poisoned data. For poisoned training pairs, the input noisy image contains an embedded trigger pattern at timestep t, and the target is the noise that would produce the attacker's desired image. During inference, starting from triggered noise, the denoising process converges to the target image.

**Conditional Diffusion Models**: For text-conditioned models like Stable Diffusion, the trigger can be embedded in the text prompt (a specific phrase or token) or in the input image (for image-to-image models). When the trigger is present in the condition, the model generates the attacker's target output regardless of the other conditioning information.

**Training Procedure**: The attack poisons a fraction of the training data by:
1. Defining a trigger pattern (pixel patch, noise pattern, or text token).
2. Creating poisoned training pairs where triggered inputs map to target outputs.
3. Training the diffusion model on the mixed clean+poisoned dataset.
4. The model learns to associate the trigger with the target generation while maintaining normal behavior on clean inputs.

**Trigger Persistence**: A key challenge is ensuring the trigger effect propagates through the multi-step denoising process. The framework addresses this by poisoning the model's behavior at multiple timesteps, not just the initial step.

## Key Results
- Achieves high fidelity target image generation (FID close to clean model) when trigger is present.
- Clean generation quality (measured by FID) is not significantly degraded by the backdoor.
- Effective across DDPM, DDIM, and Stable Diffusion architectures on CIFAR-10, CelebA, and LSUN datasets.
- Demonstrates both targeted attacks (specific target image) and semantic attacks (target image class).
- The attack is robust across different sampling schedules and numbers of denoising steps.
- Existing image classification backdoor defenses are not directly applicable to diffusion models, highlighting the need for diffusion-specific defenses.
