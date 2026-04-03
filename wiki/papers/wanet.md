---
title: "WaNet: Imperceptible Warping-based Backdoor Attack"
source: raw/wanet-imperceptible-warping-backdoor-attack.md
venue: ICLR
year: 2021
summary: "WaNet uses smooth image warping as a backdoor trigger instead of additive patches, achieving near-perfect imperceptibility. The warping-based trigger evades Neural Cleanse, STRIP, Spectral Signatures, and Activation Clustering because it is a spatial transformation with no anomalous feature-space signature."
compiled: "2026-04-03T16:00:00"
---

# WaNet: Imperceptible Warping-based Backdoor Attack

**Authors:** Anh Nguyen, Anh Tran
**Venue:** ICLR 2021 **Year:** 2021

## Summary

WaNet introduces a fundamentally different approach to backdoor triggers: instead of additive patches or pixel-level perturbations, it uses smooth spatial warping of the entire image. The trigger is a small elastic deformation field that bends the image slightly, producing natural-looking distortions that are imperceptible to human viewers (PSNR >35dB). Because the trigger is a spatial transformation rather than an additive pattern, it leaves no anomalous signature in either pixel space or feature space, evading a broad range of defenses.

A key innovation is the "noise mode" training strategy: some clean samples are slightly warped with random (non-trigger) deformations during training. This teaches the model to be robust to minor warping in general while remaining specifically responsive to the trigger warp, preventing false activations on naturally augmented data.

WaNet achieves attack success rates above 98% on CIFAR-10, GTSRB, CelebA, and ImageNet subsets while evading Neural Cleanse, STRIP, Spectral Signatures, and Activation Clustering, establishing warping-based triggers as a significant challenge for backdoor defenses.

## Key Concepts

- [[backdoor-attack]] -- warping-based attack fundamentally different from additive triggers
- [[trigger-pattern]] -- spatial transformation trigger vs. additive perturbation trigger
- [[attack-success-rate]] -- above 98% across multiple benchmarks
- [[backdoor-defense]] -- evades multiple major defense categories

## Method Details

**Warping Field Generation:** The trigger is a 2D displacement field (u, v) mapping each pixel (x, y) to (x + u(x,y), y + v(x,y)):
1. Generated from a small control grid (e.g., 4x4 or 8x8 control points).
2. Upsampled to image resolution via bilinear interpolation, ensuring smoothness.
3. Control point displacements are fixed (defining the trigger) and small in magnitude.

**Poisoned Image Creation:** x_poisoned = Warp(x_clean, field_trigger), using differentiable grid sampling. The warped image looks nearly identical to the original due to smooth, small deformations.

**Training with Noise Mode:** Three sample types during training:
1. **Clean samples** (majority): standard training pairs.
2. **Poisoned samples** (small fraction): warped with the trigger field, labeled as target class.
3. **Noise-mode samples** (small fraction): warped with random small deformation fields, retaining original labels. This prevents the model from triggering on arbitrary warping.

**Warp Parameters:**
- Grid size k (typically 4): controls deformation frequency.
- Warping strength s (typically 0.5): controls displacement magnitude.
- Specific displacement values at control points: the trigger "secret."

## Results & Findings

- [[attack-success-rate]] above 98% on CIFAR-10, GTSRB, CelebA, and ImageNet subsets with clean accuracy matching baseline.
- PSNR between clean and warped images exceeds 35dB; indistinguishable by human viewers.
- Evades [[neural-cleanse]]: reverse-engineered trigger does not match warping (Neural Cleanse assumes additive triggers).
- Evades [[strip]]: entropy distribution of warped inputs indistinguishable from clean inputs.
- Evades [[spectral-signatures]] and [[activation-clustering]]: feature representations not separable.
- Noise mode is essential: without it, the model triggers on any warped input.
- Robust to common data augmentation (random crop, flip, color jitter).

## Relevance to LLM Backdoor Defense

While WaNet targets image models, its design principles are instructive for LLM backdoor defense. The concept of a "global, imperceptible transformation" as a trigger parallels textual attacks that use subtle stylistic shifts (paraphrasing, syntactic patterns) rather than explicit token insertions. WaNet's success at evading feature-separation defenses foreshadows similar challenges in text, where syntactic triggers may produce no separable feature-space signature. Defenses for LLMs should account for trigger mechanisms that transform the entire input rather than inserting localized artifacts.

## Related Work

- [[badnets]] -- additive patch trigger that WaNet improves upon in stealth
- [[neural-cleanse]] -- trigger reverse-engineering defense evaded by WaNet
- [[strip]] -- input perturbation defense evaded by WaNet
- [[spectral-signatures]] -- separation defense evaded by WaNet
- [[activation-clustering]] -- cluster defense evaded by WaNet
- [[reconstructive-neuron-pruning]] -- pruning defense that successfully detects WaNet
- [[revisiting-latent-separability]] -- places WaNet in the "medium separability" category

## Backlinks
[[backdoor-attack]] | [[trigger-pattern]] | [[attack-success-rate]] | [[backdoor-defense]]
