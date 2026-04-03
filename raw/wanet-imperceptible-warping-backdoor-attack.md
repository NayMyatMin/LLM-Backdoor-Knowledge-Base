# WaNet: Imperceptible Warping-based Backdoor Attack

## Authors
Anh Nguyen, Anh Tran

## Venue
ICLR 2021

## Year
2021

## URL
https://arxiv.org/abs/2102.10369

## Abstract Summary
WaNet introduces a backdoor attack that uses image warping as the trigger mechanism instead of additive patches or patterns. The trigger is a smooth, imperceptible spatial transformation (warping) applied to the entire image, making it virtually undetectable by human inspection or statistical analysis. The warping is parameterized by a small deformation field that bends the image slightly, creating a trigger that is both global (affects all pixels) and invisible (produces natural-looking distortions).

## Key Contributions

1. **Warping-based trigger**: Proposed using image warping (spatial transformations) as backdoor triggers, a fundamentally different approach from additive perturbation triggers, achieving near-perfect imperceptibility.

2. **Smooth deformation field**: Designed the trigger as a smooth deformation field that produces natural-looking image distortions, leveraging the fact that small smooth warps are imperceptible to the human visual system.

3. **Noise mode training**: Introduced a "noise mode" during training where some clean samples are slightly warped (with a different random warping than the trigger), teaching the model to be robust to minor warping while still responding specifically to the trigger warp.

4. **Evasion of multiple defenses**: Demonstrated that warping-based triggers evade a broad range of defenses because the trigger is not an additive pattern and leaves no anomalous signature in either pixel or feature space.

## Method Details
WaNet's trigger mechanism is based on elastic image deformation:

**Warping Field Generation**: The trigger is defined by a 2D displacement field (u, v) that maps each pixel location (x, y) to a new location (x + u(x,y), y + v(x,y)). The displacement field is:
1. Generated from a small control grid (e.g., 4x4 or 8x8 control points).
2. Upsampled to image resolution using bilinear interpolation, ensuring smoothness.
3. The control point displacements are fixed (defining the trigger) and small in magnitude.

**Poisoned Image Creation**: x_poisoned = Warp(x_clean, field_trigger), where Warp applies the deformation field using differentiable grid sampling. The warped image looks nearly identical to the original because the deformation is smooth and small.

**Training with Noise Mode**: The model is trained on three types of samples:
1. **Clean samples** (majority): Standard training pairs.
2. **Poisoned samples** (small fraction): Warped with the trigger field, labeled as target class.
3. **Noise-mode samples** (small fraction): Warped with random small deformation fields, labeled with their original correct labels. This "noise mode" prevents the model from learning to trigger on any warping, making it specific to the trigger warp.

**Warp Parameters**: The trigger warp is controlled by:
- Grid size k (typically 4): Controls the frequency of deformation.
- Warping strength s (typically 0.5): Controls the magnitude of displacement.
- The specific displacement values at control points (the "secret" of the trigger).

## Key Results
- Achieves attack success rates above 98% on CIFAR-10, GTSRB, CelebA, and ImageNet subsets with clean accuracy matching the baseline model.
- Visual imperceptibility: PSNR between clean and warped images exceeds 35dB, and the warping is indistinguishable by human viewers in studies.
- Evades Neural Cleanse: the reverse-engineered trigger does not match the warping pattern (Neural Cleanse assumes additive triggers).
- Evades STRIP: the entropy distribution of warped inputs is indistinguishable from clean inputs.
- Evades Spectral Signatures and Activation Clustering: the feature representations of warped inputs are not separable from clean inputs.
- The noise mode is essential: without it, the model triggers on any warped input, degrading clean accuracy on naturally augmented data.
- The attack is robust to common data augmentation (random crop, flip, color jitter) applied during victim training.
