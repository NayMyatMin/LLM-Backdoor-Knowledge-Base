# Adversarial Neuron Pruning Purifies Backdoored Deep Models

## Authors
Dongxian Wu, Yisen Wang

## Venue
NeurIPS 2021

## Year
2021

## URL
https://arxiv.org/abs/2110.14430

## Abstract Summary
Adversarial Neuron Pruning (ANP) presents a backdoor defense method that identifies and prunes neurons responsible for backdoor behavior by leveraging adversarial perturbations on neuron weights. The key insight is that backdoor-related neurons are more sensitive to adversarial perturbations than clean-task neurons. By applying small adversarial perturbations to neuron weights and measuring the resulting change in model output, ANP can accurately identify and remove backdoor neurons while preserving model utility.

## Key Contributions

1. **Adversarial weight perturbation for neuron identification**: Proposed using adversarial perturbations on neuron weights (rather than inputs) to distinguish backdoor neurons from clean neurons, providing a more reliable identification signal than activation-based methods.

2. **Sensitivity-based pruning criterion**: Introduced a neuron sensitivity metric based on how much the model output changes when a neuron's weights are adversarially perturbed, showing that backdoor neurons exhibit significantly higher sensitivity.

3. **Minimal clean data requirement**: The method requires only a small set of clean samples (as few as 5% of the training set) to compute the adversarial perturbations and evaluate neuron sensitivity.

4. **Superior performance over activation-based pruning**: Demonstrated that weight-perturbation-based identification outperforms traditional activation-based pruning methods (e.g., Fine-Pruning) that prune dormant neurons, especially against adaptive attacks.

## Method Details
ANP operates in two phases:

**Phase 1 - Adversarial Neuron Sensitivity Computation**: For each neuron in the network, ANP computes adversarial perturbations to the neuron's weights that maximize the change in model output on a small set of clean validation samples. Specifically, for neuron i with weights w_i, ANP solves: max_{delta} L(f(x; w + delta), y) subject to ||delta_i|| <= epsilon, where delta_i is the perturbation applied only to neuron i's weights. The magnitude of output change serves as the sensitivity score for that neuron.

**Phase 2 - Pruning and Optional Fine-tuning**: Neurons are ranked by their sensitivity scores, and the most sensitive neurons (those most likely associated with the backdoor) are pruned. The pruning threshold is determined by evaluating clean accuracy on the validation set -- neurons are pruned until clean accuracy begins to drop noticeably. Optionally, a brief fine-tuning step on the clean validation set can recover any lost accuracy.

The adversarial perturbations are computed using projected gradient descent (PGD) on the neuron weights. The method considers both individual neuron sensitivity and the interaction between neurons, applying perturbations iteratively.

## Key Results
- Reduces attack success rate to below 2% on average across BadNets, Blended, WaNet, and Input-Aware attacks on CIFAR-10 and GTSRB.
- Maintains clean accuracy within 1-2% of the original model after pruning and fine-tuning.
- Outperforms Fine-Pruning by a significant margin, especially on stealthy attacks (WaNet, Input-Aware) where Fine-Pruning's activation-based criterion fails.
- The sensitivity gap between backdoor and clean neurons is pronounced, enabling reliable separation with a clear threshold.
- Robust to varying poisoning rates (1% to 10%) and different target classes.
- Computational overhead is modest: the adversarial perturbation computation adds only a few minutes on top of standard evaluation.
