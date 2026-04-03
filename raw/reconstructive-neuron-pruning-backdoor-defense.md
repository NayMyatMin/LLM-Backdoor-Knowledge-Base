# Reconstructive Neuron Pruning for Backdoor Defense

## Authors
Yige Li, Xixiang Lyu, Xingjun Ma, Nodens Koren, Lingjuan Lyu, Bo Li, Yu-Gang Jiang

## Venue
ICML 2023

## Year
2023

## URL
https://arxiv.org/abs/2305.14876

## Abstract Summary
Reconstructive Neuron Pruning (RNP) proposes a backdoor defense that identifies and prunes backdoor neurons through a novel "unlearning then recovering" procedure. Unlike standard pruning that identifies neurons based on activation patterns, RNP first unlearns the model's knowledge using a small clean dataset, then examines which neurons recover their original behavior when fine-tuned. Neurons that rapidly recover their activation patterns are identified as encoding the backdoor (because backdoor patterns are simpler and recover faster), and are pruned.

## Key Contributions

1. **Unlearn-then-recover neuron identification**: Proposed a novel paradigm for identifying backdoor neurons based on their recovery speed after unlearning, exploiting the observation that simpler backdoor patterns are more easily relearned than complex clean-task patterns.

2. **Recovery-based pruning criterion**: Developed a quantitative criterion based on the difference in neuron activation patterns before unlearning and after partial recovery, providing a more reliable backdoor neuron identification than activation magnitude alone.

3. **Addressing limitations of activation-based pruning**: Overcame the failure modes of Fine-Pruning and standard activation-based methods, which can be fooled by attacks that distribute backdoor functionality across many neurons.

4. **Effective against adaptive attacks**: Demonstrated robustness against attacks specifically designed to evade pruning-based defenses.

## Method Details
RNP operates in three phases:

**Phase 1 - Unlearning**: The backdoored model's knowledge is deliberately degraded by training with reversed objectives on a small clean dataset. This can be done by:
- Gradient ascent on the clean data cross-entropy loss (maximizing loss rather than minimizing it).
- Training with random labels on clean data.
The result is a model that has "forgotten" both clean-task and backdoor-task patterns to some degree.

**Phase 2 - Selective Recovery**: The unlearned model is briefly fine-tuned (recovered) on the clean dataset with standard training. During this recovery, the learning dynamics are monitored at the neuron level:
- **Backdoor neurons**: Recover their original activation patterns quickly because the trigger-to-target mapping is simple (a shortcut).
- **Clean-task neurons**: Recover slowly because the clean-task features are complex and require more data to relearn.

**Phase 3 - Pruning**: Neurons are scored by their recovery speed, quantified as: R_i = ||a_i^{recovered} - a_i^{unlearned}|| / ||a_i^{original} - a_i^{unlearned}||, where a_i represents neuron i's activation pattern. Neurons with high recovery ratio R_i are identified as backdoor neurons and pruned.

**Post-pruning Fine-tuning**: After pruning, the model is briefly fine-tuned on the clean dataset to recover any clean accuracy lost during the process.

**Hyperparameters**: Key parameters include the unlearning duration (number of gradient ascent steps), recovery duration, and pruning ratio. The method is relatively robust to these choices within reasonable ranges.

## Key Results
- Reduces attack success rate to below 2% across BadNets, Blended, WaNet, Input-Aware, and LIRA attacks on CIFAR-10, GTSRB, and Tiny ImageNet.
- Clean accuracy after pruning and fine-tuning is within 1-2% of the original model.
- Significantly outperforms Fine-Pruning, especially on attacks that distribute backdoor neurons broadly (WaNet, Input-Aware).
- The recovery speed gap between backdoor and clean neurons is consistent and large, enabling reliable threshold selection.
- Robust against an adaptive attack that intentionally spreads backdoor functionality across many neurons.
- Requires only 5% of the training data as the clean validation set.
