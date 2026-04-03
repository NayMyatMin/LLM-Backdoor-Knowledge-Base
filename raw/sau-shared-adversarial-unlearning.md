# Shared Adversarial Unlearning: Backdoor Mitigation by Unlearning Shared Adversarial Examples

## Authors
Shaokui Wei, Mingda Zhang, Hongyuan Zha, Baoyuan Wu

## Venue
NeurIPS 2023

## Year
2023

## URL
https://arxiv.org/abs/2305.09464

## Abstract Summary
SAU (Shared Adversarial Unlearning) proposes a backdoor defense method that generates shared adversarial examples (SAEs) to approximate the effect of unknown backdoor triggers, then uses these SAEs to unlearn the backdoor through adversarial training. The key insight is that adversarial examples crafted to flip predictions across many clean samples share functional similarities with backdoor triggers, as both exploit shortcuts in the model. By unlearning the model's reliance on these shared adversarial perturbations, SAU effectively mitigates various backdoor attacks.

## Key Contributions

1. **Shared adversarial examples as trigger proxies**: Proposed generating adversarial perturbations that are universally effective across many samples (shared) as approximations of unknown backdoor triggers, bridging adversarial robustness and backdoor defense.

2. **Unlearning-based mitigation**: Used adversarial unlearning to remove the backdoor -- training the model to be invariant to the shared adversarial perturbations, thereby eliminating the learned shortcut exploited by the backdoor.

3. **No trigger reverse-engineering required**: Unlike methods such as Neural Cleanse that attempt to reconstruct the exact trigger, SAU sidesteps trigger reverse-engineering entirely by using universal adversarial perturbations as proxies.

4. **Strong empirical performance**: Achieved state-of-the-art defense results across a comprehensive set of backdoor attacks with minimal computational overhead.

## Method Details
SAU operates in two main stages:

**Stage 1 - Shared Adversarial Example Generation**: Given a small set of clean samples, SAU crafts a universal adversarial perturbation delta that, when added to any clean input, causes the model to change its prediction. This is formulated as: max_{delta} sum_i L(f(x_i + delta), y_i), subject to ||delta|| <= epsilon. The perturbation is "shared" because it is optimized to be effective across all clean samples simultaneously, similar to how a backdoor trigger universally causes misclassification.

**Stage 2 - Adversarial Unlearning**: The model is fine-tuned to be invariant to the shared adversarial perturbation. This is done by minimizing: L_clean(f(x), y) + lambda * L_unlearn(f(x + delta), f(x)), where L_unlearn encourages the model's output on perturbed inputs to match its output on clean inputs. This effectively teaches the model to ignore the shortcut patterns exploited by both the adversarial perturbation and the actual backdoor trigger.

**Iterative Refinement**: The two stages are alternated: new shared adversarial examples are generated for the updated model, and the model is further fine-tuned for invariance. This iterative process progressively removes backdoor shortcuts.

**Key Design Choices**:
- The perturbation budget epsilon is set to cover common trigger magnitudes.
- The unlearning uses a KL-divergence loss to match output distributions.
- Only a small clean dataset (1-5% of training data) is needed.

## Key Results
- Reduces attack success rate to below 3% on average across 12 different attacks including BadNets, Blended, WaNet, Input-Aware, LIRA, and others.
- Clean accuracy degradation is less than 1.5% on CIFAR-10 and less than 2% on Tiny ImageNet.
- Outperforms existing defenses including Fine-Pruning, Neural Cleanse, ANP, and I-BAU on comprehensive benchmarks.
- Robust against adaptive attacks where the attacker is aware of the defense.
- The shared adversarial perturbations show visual and functional similarity to actual backdoor triggers, validating the theoretical motivation.
- Computationally efficient: defense completes in under 10 minutes on standard GPU hardware.
