# Fine-Pruning: Defending Against Backdooring Attacks on Deep Neural Networks

**Authors:** Kang Liu, Brendan Dolan-Gavitt, Siddharth Garg
**Venue:** RAID 2018
**URL:** https://arxiv.org/abs/1805.12185

## Abstract

This paper investigates pruning and fine-tuning as defenses against backdoor attacks and finds that neither alone is sufficient. The authors propose "fine-pruning," a combined approach that first prunes neurons dormant on clean data (which encode the backdoor) and then fine-tunes the pruned model.

## Key Contributions

1. **Analysis of individual defenses**: Shows pruning alone and fine-tuning alone are insufficient
2. **Backdoor neuron identification**: Neurons dormant on clean data but active on triggered inputs encode the backdoor
3. **Combined defense**: Fine-pruning achieves near-complete backdoor removal
4. **Minimal accuracy loss**: Maintains clean accuracy while eliminating the backdoor

## Method

### Pruning Phase
1. Feed clean validation data through the model
2. Record average activation of each neuron
3. Rank neurons by their average activation on clean data
4. Prune (set to zero) neurons with the lowest clean-data activation — these "dormant" neurons likely encode the backdoor behavior
5. Prune incrementally until attack success rate drops

### Fine-Tuning Phase
1. After pruning, fine-tune the model on clean validation data
2. This recovers any accuracy lost from pruning
3. The combination is crucial: pruning removes the backdoor, fine-tuning restores performance

## Key Results

- Pruning alone: can reduce attack success but also degrades clean accuracy significantly
- Fine-tuning alone: backdoor can survive if it's embedded in neurons also used for clean classification
- **Fine-pruning**: reduces attack success rate to 0% with only 0.4% accuracy loss
- Tested against BadNets and Trojan attacks on multiple architectures

## Significance

Fine-Pruning was one of the earliest practical defense methods and introduced the key insight that backdoor behavior is encoded in neurons that are dormant on clean data. This neuron-level understanding of backdoors influenced many subsequent defenses and analysis methods.
