# From Shortcuts to Triggers: Backdoor Defense with Denoised PoE

## Authors
Qin Liu, Fei Wang, Chaowei Xiao, Muhao Chen

## Venue
NAACL 2024

## Year
2024

## URL
https://arxiv.org/abs/2305.14910

## Abstract Summary
This paper presents a backdoor defense method based on the connection between backdoor triggers and shortcut learning. The key insight is that backdoor triggers function as extreme shortcuts that the model exploits for prediction, similar to how models learn spurious correlations in standard training. The authors propose a defense based on Denoised Product-of-Experts (DPoE) that identifies and mitigates these shortcut-like triggers. The method trains a shallow "bias model" that captures trigger-like shortcuts, then uses a Product-of-Experts framework to deweight the influence of these shortcuts in the main model's predictions, effectively neutralizing the backdoor.

## Key Contributions
1. Established a formal connection between backdoor triggers and shortcut learning, showing that backdoor attacks exploit the same learning dynamics that cause models to rely on spurious correlations.
2. Proposed Denoised Product-of-Experts (DPoE), a training-time defense that uses a bias model to absorb backdoor shortcuts and a debiasing mechanism to remove their influence from the main model.
3. Introduced a denoising component that prevents the bias model from capturing too many legitimate features, ensuring that only shortcut-like patterns (including backdoor triggers) are captured.
4. Demonstrated effectiveness against multiple backdoor attacks on text classification tasks while maintaining clean performance.

## Method Details
- The defense trains two models simultaneously: a bias model (small capacity) designed to capture shortcut features including backdoor triggers, and a main model that is debiased against the shortcuts captured by the bias model.
- The bias model is intentionally kept shallow (e.g., a bag-of-words model or shallow neural network) so it preferentially learns simple shortcut patterns rather than complex legitimate features.
- The Product-of-Experts framework combines the predictions of both models such that the main model learns to rely on features orthogonal to those captured by the bias model.
- A denoising mechanism filters out noise from the bias model's predictions to ensure clean separation between shortcut features and legitimate features.
- The training objective encourages the main model to make predictions that are correct but not reliant on the same features as the bias model.
- The method operates during training and does not require knowledge of the specific attack or trigger pattern.

## Key Results
- DPoE reduced attack success rates by 50-80% across multiple backdoor attacks including BadNL, InsertSent, and syntactic attacks on SST-2 and AG News datasets.
- Clean accuracy was maintained within 1-3% of the original model, showing minimal impact on legitimate task performance.
- The method outperformed existing training-time defenses including anti-backdoor learning and spectral signature filtering.
- The bias model successfully captured trigger-related features, as validated by analyzing which features the bias model relied upon.
- The approach was shown to generalize across different trigger types without requiring attack-specific tuning.
