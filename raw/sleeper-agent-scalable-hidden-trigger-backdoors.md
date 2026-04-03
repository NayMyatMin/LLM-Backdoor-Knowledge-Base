# Sleeper Agent: Scalable Hidden Trigger Backdoors for Neural Networks at Scale

## Authors
Hossein Souri, Liam Fowl, Rama Chellappa, Micah Goldblum, Tom Goldstein

## Venue
NeurIPS 2022

## Year
2022

## URL
https://arxiv.org/abs/2106.08970

## Abstract Summary
Sleeper Agent introduces a scalable hidden-trigger backdoor attack that can be applied to large-scale datasets and models. Unlike visible-trigger attacks (e.g., BadNets), hidden-trigger attacks do not modify inputs at training time in a perceptible way. The key challenge is that previous hidden-trigger methods did not scale to large datasets like ImageNet. Sleeper Agent uses gradient matching to craft poisoned samples whose gradients align with those of patched (triggered) inputs, enabling the backdoor to be learned during standard training without any visible modification to the training data.

## Key Contributions

1. **Scalability to large datasets**: First hidden-trigger backdoor attack demonstrated to work effectively on ImageNet-scale datasets, overcoming a key limitation of prior hidden-trigger methods.

2. **Gradient matching objective**: Proposed crafting poisoned samples by matching their gradient (with respect to model parameters) to the gradient of triggered samples, ensuring that training on the poisoned data implicitly teaches the model the trigger-to-target mapping.

3. **Transferability across training setups**: Demonstrated that the poisoned data can transfer across different model architectures and training procedures, making the attack practical in realistic scenarios where the attacker does not control the training process.

4. **Clean-label attack**: The poisoned samples retain their correct labels and appear visually normal, making the attack undetectable by simple visual inspection or label-verification defenses.

## Method Details
The attack operates in a data poisoning setting where the attacker can modify a small fraction of the training data but does not control the training procedure.

**Gradient Matching**: The core idea is to craft poisoned samples x_p (with correct labels) such that their gradient matches the gradient of triggered samples x_t (with the target label). Formally: min_{x_p} ||grad_theta L(f(x_p), y_correct) - grad_theta L(f(x_t), y_target)||^2. This ensures that when the model trains on x_p, it implicitly learns the same weight updates as if it were training on the triggered samples.

**Crafting Process**: Starting from clean images of the target class, the pixel values are iteratively perturbed (within a small L-infinity bound) to minimize the gradient matching objective. The perturbations are imperceptible but encode information that aligns the learning dynamics with the trigger pattern.

**Patch-based Trigger**: At inference time, a small patch (e.g., a 8x8 pixel pattern) is applied to test inputs to activate the backdoor. The trigger patch is defined before the poisoning process and remains fixed.

**Multi-model Ensemble**: To improve transferability, the gradient matching can be performed over an ensemble of models at different training stages or architectures, making the poisoned data effective regardless of the specific model trained on it.

## Key Results
- Successfully attacks ImageNet classifiers with attack success rates above 80% using only 0.05-0.1% poisoned data.
- Clean accuracy degradation is negligible (less than 0.5%).
- Transfers across architectures: poisoned data crafted on ResNet-18 transfers to ResNet-50 and other architectures.
- Outperforms prior hidden-trigger methods (Hidden Trigger Backdoor, Witches' Brew) in both scale and attack success rate.
- The gradient matching approach is shown to be more effective than feature collision approaches for large-scale settings.
- Remains effective even when the victim uses standard data augmentation during training.
