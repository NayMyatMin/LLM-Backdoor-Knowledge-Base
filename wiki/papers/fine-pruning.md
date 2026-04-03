---
title: "Fine-Pruning: Defending Against Backdooring Attacks on Deep Neural Networks"
source: "fine-pruning-defending-backdoor-attacks.md"
venue: "RAID"
year: 2018
summary: "Investigates pruning and fine-tuning as backdoor defenses and finds neither alone is sufficient. Proposes fine-pruning, a combined approach that first prunes neurons dormant on clean data (which encode the backdoor) then fine-tunes to restore accuracy. Achieves near-complete backdoor removal with minimal accuracy loss."
compiled: "2026-04-03T00:00:07Z"
---

# Fine-Pruning: Defending Against Backdooring Attacks on Deep Neural Networks

**Authors:** Kang Liu, Brendan Dolan-Gavitt, Siddharth Garg
**Venue:** RAID 2018 **Year:** 2018

## Summary

This paper investigates two natural defenses against [[backdoor-attack]] -- pruning and fine-tuning -- and demonstrates that neither alone is sufficient to reliably remove backdoors. Pruning alone can reduce [[attack-success-rate]] but also degrades clean accuracy significantly. Fine-tuning alone may fail because the backdoor can be encoded in neurons that are also used for legitimate classification, making it resistant to gradient-based unlearning.

The authors propose [[fine-pruning]], a combined approach that first prunes neurons that are dormant on clean data (these "dormant" neurons disproportionately encode the backdoor behavior) and then fine-tunes the pruned model to recover any lost clean accuracy. This two-step process is effective because pruning removes the backdoor pathway while fine-tuning restores the model's legitimate performance.

The key insight is that backdoor behavior is encoded in neurons with low average activation on clean data but high activation on triggered inputs. This neuron-level understanding of how backdoors are stored in DNNs has been foundational for many subsequent defense and analysis methods.

## Key Concepts

- [[fine-pruning]] -- Combined pruning and fine-tuning defense against backdoor attacks
- [[backdoor-defense]] -- The broader class of defensive methods
- [[backdoor-attack]] -- The threat being mitigated
- [[trigger-pattern]] -- The patterns that activate dormant backdoor neurons

## Method Details

### Pruning Phase

1. Feed clean validation data through the model.
2. Record the average activation of each neuron across the clean validation set.
3. Rank neurons by their average activation on clean data.
4. Prune (set to zero) neurons with the lowest clean-data activation -- these "dormant" neurons likely encode the backdoor behavior because they are unused for clean classification but activated by the [[trigger-pattern]].
5. Prune incrementally, monitoring both clean accuracy and [[attack-success-rate]], until the attack success rate drops to acceptable levels.

### Fine-Tuning Phase

1. After pruning, fine-tune the model on a small clean validation dataset.
2. This recovers any accuracy lost during the pruning step.
3. The combination is crucial: pruning removes the backdoor pathway, and fine-tuning restores legitimate performance without re-introducing the backdoor.

## Results & Findings

- **Pruning alone**: Can reduce attack success but also degrades clean accuracy significantly, often by 5-10% or more.
- **Fine-tuning alone**: The backdoor can survive if it is embedded in neurons also used for clean classification.
- **Fine-pruning**: Reduces [[attack-success-rate]] to 0% with only 0.4% accuracy loss.
- **Generalization**: Tested against [[badnets]] and [[trojaning-attack]] on multiple architectures.
- The method requires only clean validation data (no knowledge of the attack or trigger needed).

## Relevance to LLM Backdoor Defense

Fine-pruning's insight that backdoor behavior is localized in specific neurons has influenced research on understanding and removing backdoors in larger models, including language models. The concept of identifying and removing "backdoor neurons" has been extended to transformer architectures. However, modern LLM attacks like [[badedit]] that modify minimal parameters may be harder to address with pruning approaches, and [[weight-poisoning-pretrained]] shows that backdoors designed to survive fine-tuning present a direct challenge to the fine-tuning component of this defense.

## Related Work

- [[badnets]] and [[trojaning-attack]] are the primary attacks evaluated against this defense
- [[neural-cleanse]] provides a complementary model-level detection approach
- [[spectral-signatures]] and [[activation-clustering]] work at the data level rather than the model level
- [[strip]] provides inference-time detection rather than model-level removal
- [[weight-poisoning-pretrained]] specifically designs backdoors to resist fine-tuning, directly challenging this defense
- [[backdoor-learning-survey]] categorizes fine-pruning as a pruning-based removal defense

## Backlinks


- [[fabe]]
- [[data-free-backdoor]]
- [[pruning-vs-unlearning]]
- [[representation-space-detection]]
- [[fine-pruning]]
- [[backdoor-defense]]
- [[backdoor-attack]]
- [[trigger-pattern]]
- [[backdoor-circuits]]
- [[circuit-analysis]]
