# Data-free Backdoor Removal based on Channel Lipschitzness

## Authors
Heng Lv, Jianming Zhang, Yong Ding, Baojun Qi

## Venue
USENIX Security 2023

## Year
2023

## URL
https://arxiv.org/abs/2208.06252

## Abstract Summary
This paper presents a data-free approach to backdoor injection and removal in neural networks, demonstrating that backdoors can be implanted into a trained model without requiring access to the original training data, and proposing a corresponding defense. The data-free backdoor attack works by directly manipulating model weights to create a backdoor, while the defense identifies and removes backdoor-associated neurons by analyzing channel-level properties (Lipschitzness) of the network without needing any clean data samples. This is particularly relevant in scenarios where model weights are shared (e.g., model marketplaces) but training data is unavailable.

## Key Contributions
1. Demonstrated that backdoors can be injected into pre-trained models through direct weight manipulation without access to any training data, expanding the threat model beyond traditional data poisoning.
2. Proposed a data-free backdoor detection and removal method based on analyzing the Lipschitz constants of individual channels/neurons, which can be computed from model weights alone.
3. Showed that backdoor-associated neurons exhibit abnormally high Lipschitz constants compared to clean neurons, providing a reliable detection signal that does not require data.
4. The defense requires no clean data, no knowledge of the trigger, and no retraining, making it applicable in realistic deployment scenarios.

## Method Details
- Data-free backdoor injection modifies the weights of selected neurons to create a mapping from a trigger pattern to the target output, without requiring forward/backward passes through training data.
- The injection targets specific neurons in intermediate layers and modifies their weights to be highly responsive to the trigger pattern while maintaining normal behavior for clean inputs.
- For the defense, the method computes the Lipschitz constant of each channel in the network. The Lipschitz constant measures the maximum sensitivity of a neuron's output to changes in its input.
- Backdoor-associated neurons have disproportionately high Lipschitz constants because they must respond strongly to the trigger pattern, creating an outlier signal.
- Neurons with Lipschitz constants exceeding a statistical threshold (based on the distribution of all neurons' Lipschitz constants) are identified as backdoor-related and pruned.
- After pruning, the model's clean accuracy is evaluated to ensure it remains acceptable; if needed, minimal fine-tuning on a small amount of unlabeled data can restore performance.

## Key Results
- The data-free detection method identified backdoor neurons with accuracy above 90% across multiple architectures (ResNet, VGG, BERT).
- After pruning identified neurons, attack success rates dropped to below 5% while clean accuracy decreased by less than 3%.
- The method was effective against both data-poisoning-based backdoors and the proposed weight-manipulation-based backdoors.
- Compared to data-dependent defenses (Fine-Pruning, Neural Cleanse), the data-free approach achieved comparable defense performance without requiring any clean data.
- The work highlighted the importance of securing model weights during distribution, as backdoors can be injected post-training.
