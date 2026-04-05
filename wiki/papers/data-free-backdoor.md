---
title: "Data-free Backdoor Removal based on Channel Lipschitzness"
source: raw/data-free-backdoor-injection-neural-networks.md
venue: USENIX Security
year: 2023
summary: "This paper demonstrates that backdoors can be injected into pre-trained models through direct weight manipulation without training data, and proposes a data-free defense that detects and prunes backdoor-associated neurons by analyzing channel-level Lipschitz constants computed from model weights alone."
tags:
  - defense
  - pruning
threat_model: "weight-editing"
compiled: "2026-04-03T16:00:00"
---

# Data-free Backdoor Removal based on Channel Lipschitzness

**Authors:** Heng Lv, Jianming Zhang, Yong Ding, Baojun Qi
**Venue:** USENIX Security 2023 **Year:** 2023

## Summary

This paper expands the backdoor threat model by demonstrating that backdoors can be injected into pre-trained models through direct weight manipulation, without requiring any access to training data. This is particularly relevant for model marketplace scenarios where model weights are shared but training data is unavailable.

The corresponding defense exploits a key observation: backdoor-associated neurons exhibit abnormally high Lipschitz constants compared to clean neurons. The Lipschitz constant measures the maximum sensitivity of a neuron's output to changes in its input, and backdoor neurons must respond strongly to trigger patterns, creating an outlier signal. By computing Lipschitz constants for each channel from model weights alone, the method identifies and prunes backdoor neurons without requiring any clean data, knowledge of the trigger, or retraining.

After pruning, attack success rates drop below 5% while clean accuracy decreases by less than 3%, achieving performance comparable to data-dependent defenses.

## Key Concepts

- [[weight-poisoning]] — demonstrates backdoor injection via direct weight manipulation
- [[backdoor-defense]] — data-free detection and removal via Lipschitz analysis
- [[supply-chain-attack]] — threat model targeting model distribution and sharing
- [[backdoor-attack]] — both data-poisoning-based and weight-manipulation-based attacks
- [[trigger-pattern]] — causes high-sensitivity neurons identifiable by Lipschitz constants

## Method Details

**Data-free Backdoor Injection:**
- Modifies weights of selected neurons in intermediate layers to create a mapping from a trigger pattern to the target output, without requiring forward/backward passes through training data.
- Targeted neurons are modified to be highly responsive to the trigger pattern while maintaining normal behavior for clean inputs.

**Data-free Backdoor Defense:**
1. **Lipschitz constant computation**: For each channel in the network, compute the Lipschitz constant — the maximum sensitivity of the neuron's output to input changes. This is computed from the model weights alone.
2. **Outlier detection**: Backdoor-associated neurons have disproportionately high Lipschitz constants because they must respond strongly to trigger patterns. Neurons exceeding a statistical threshold based on the distribution of all neurons' constants are flagged.
3. **Pruning**: Flagged neurons are pruned from the network.
4. **Optional restoration**: If needed, minimal fine-tuning on a small amount of unlabeled data can restore clean accuracy.

The entire defense requires no clean data, no knowledge of the trigger, and no retraining.

## Results & Findings

- Identified backdoor neurons with accuracy above 90% across ResNet, VGG, and BERT architectures.
- After pruning, [[attack-success-rate]] dropped to below 5% with clean accuracy loss under 3%.
- Effective against both [[data-poisoning]]-based backdoors and weight-manipulation-based backdoors.
- Achieved comparable performance to data-dependent defenses ([[fine-pruning]], [[neural-cleanse]]) without requiring any clean data.
- Highlighted the importance of securing model weights during distribution.

## Relevance to LLM Backdoor Defense

This work is highly relevant to LLM security for two reasons. First, it demonstrates that backdoors can be injected post-training through weight manipulation — a critical threat for LLMs distributed through model hubs like Hugging Face. Second, the data-free defense is especially practical for LLM deployment scenarios where the original training data is unavailable or proprietary. The Lipschitz-based analysis of individual channels could potentially be extended to transformer attention heads or feed-forward layers to identify [[weight-poisoning]] in LLMs without requiring access to training corpora.

## Related Work

- [[fine-pruning]] — data-dependent pruning defense that this work matches without requiring clean data
- [[neural-cleanse]] — trigger reverse-engineering that requires data; the Lipschitz approach is data-free
- [[badnets]] — foundational attack evaluated against
- [[spectral-signatures]] — data-dependent detection; complementary to this data-free approach

## Backlinks
[[weight-poisoning]] | [[backdoor-defense]] | [[supply-chain-attack]] | [[backdoor-attack]] | [[data-poisoning]]
