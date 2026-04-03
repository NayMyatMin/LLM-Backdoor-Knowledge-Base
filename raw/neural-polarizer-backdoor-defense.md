# Neural Polarizer: A Lightweight Backdoor Defense via Purifying Poisoned Features

## Authors
Mingli Zhu, Shaokui Wei, Hongyuan Zha, Baoyuan Wu

## Venue
NeurIPS 2023

## Year
2023

## URL
https://arxiv.org/abs/2306.01697

## Abstract Summary
Neural Polarizer proposes a lightweight backdoor defense that inserts a small learnable module (the "polarizer") into the backdoored model to purify poisoned features at inference time. Inspired by optical polarizers that filter light, the neural polarizer filters out backdoor-related feature components while preserving clean-task features. The polarizer module is trained on a small clean dataset and can be inserted at any intermediate layer of the network, making it architecture-agnostic and computationally efficient.

## Key Contributions

1. **Lightweight plug-in defense module**: Designed a small trainable module that can be inserted into any layer of a backdoored model to filter out backdoor features, without requiring model retraining or significant architectural changes.

2. **Feature purification approach**: Instead of modifying model weights or pruning neurons, the neural polarizer directly purifies the feature representations at inference time, providing a complementary defense mechanism to existing approaches.

3. **Channel-wise attention for filtering**: The polarizer uses a channel-wise attention mechanism to selectively suppress channels that carry backdoor information while amplifying channels important for clean-task performance.

4. **Minimal computational overhead**: The polarizer adds negligible inference latency and requires minimal training data and time, making it practical for deployment.

## Method Details
The Neural Polarizer defense works as follows:

**Polarizer Architecture**: The polarizer module is a lightweight channel attention block inserted between two consecutive layers of the backdoored model. It computes channel-wise attention weights that modulate the feature map: h' = sigma(W_p * GAP(h)) * h, where h is the input feature map, GAP is global average pooling, W_p are the polarizer parameters, and sigma is a sigmoid activation.

**Training Objective**: The polarizer is trained on a small clean dataset with two objectives:
1. **Clean accuracy preservation**: The model with polarizer should correctly classify clean inputs, maintaining the original model's clean performance.
2. **Feature purification**: The polarizer should suppress feature channels that are activated by backdoor triggers. This is achieved through a regularization term that encourages the polarizer to produce sparse attention weights, focusing on the most task-relevant channels.

The combined loss is: L = L_CE(f_polarized(x), y) + alpha * ||attention_weights||_1, where the sparsity regularization implicitly suppresses backdoor-carrying channels since clean-task features are typically more distributed while backdoor features concentrate in fewer channels.

**Insertion Strategy**: The optimal insertion point is determined by evaluating the polarizer's effectiveness at different layers. Empirically, inserting the polarizer at middle-to-late layers provides the best balance of clean accuracy and backdoor suppression.

**Inference**: At test time, inputs pass through the model with the polarizer inserted. The polarizer automatically filters feature representations, neutralizing any backdoor trigger effect without requiring knowledge of the trigger pattern.

## Key Results
- Reduces attack success rate to below 5% across BadNets, Blended, WaNet, Input-Aware, and LIRA attacks on CIFAR-10 and GTSRB.
- Clean accuracy drop is less than 1% after polarizer insertion, one of the lowest among existing defenses.
- The polarizer module adds less than 0.1% additional parameters and negligible inference latency.
- Training the polarizer requires only 500-1000 clean samples and takes under 5 minutes.
- Outperforms or matches heavier defense methods (Fine-Pruning, ANP, Neural Cleanse) with significantly less computational cost.
- The learned attention weights visually correlate with the channels that encode backdoor information, validating the filtering mechanism.
