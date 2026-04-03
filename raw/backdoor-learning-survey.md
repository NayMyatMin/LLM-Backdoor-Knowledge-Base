# Backdoor Learning: A Survey

**Authors:** Yiming Li, Yong Jiang, Zhifeng Li, Shu-Tao Xia
**Venue:** IEEE TNNLS 2024 (arXiv 2020, widely cited)
**URL:** https://arxiv.org/abs/2007.08745

## Abstract

This is the most comprehensive survey of the backdoor learning field, covering over 300 papers. It provides a systematic taxonomy of both attacks and defenses, organized along multiple dimensions: attack paradigm, trigger type, defense strategy, and threat model.

## Key Contributions

1. **Comprehensive taxonomy**: Categorizes attacks and defenses along multiple orthogonal dimensions
2. **Unified framework**: Establishes a common language and conceptual framework for the field
3. **Full lifecycle coverage**: Covers attacks and defenses at every stage (training, deployment, inference)
4. **Research roadmap**: Identifies open problems, emerging directions, and evaluation challenges

## Attack Taxonomy

### By Label Strategy
- **Poisoned-label**: Attacker changes labels of poisoned samples to the target class (e.g., BadNets)
- **Clean-label**: Poisoned samples retain their correct labels (e.g., Poison Frogs)

### By Attack Vector
- **Data poisoning**: Attacker modifies training data (most common)
- **Weight poisoning**: Attacker modifies model weights directly (e.g., Weight Poisoning on Pre-trained Models)
- **Architecture poisoning**: Attacker modifies the model architecture

### By Trigger Type
- **Patch-based**: Small pixel pattern overlaid on input (BadNets)
- **Blending**: Trigger blended with the entire image (e.g., warped, invisible perturbations)
- **Semantic**: Trigger based on semantic features (e.g., wearing sunglasses)
- **Syntactic**: Trigger based on sentence structure (Hidden Killer)
- **Clean-label**: No explicit trigger pattern; relies on feature-space manipulation

## Defense Taxonomy

### Detection-Based
- **Model-level**: Inspect model for backdoor (Neural Cleanse, ABS, META)
- **Data-level**: Inspect training data for poisoned samples (Spectral Signatures, Activation Clustering)
- **Input-level**: Detect triggered inputs at inference (STRIP, SentiNet)

### Removal-Based
- **Pruning**: Remove backdoor neurons (Fine-Pruning)
- **Unlearning**: Reverse the backdoor through targeted training
- **Distillation**: Train a clean student model from the backdoored teacher

## Key Metrics
- **Attack Success Rate (ASR)**: Fraction of triggered inputs classified to target class
- **Clean Accuracy (CA)**: Model accuracy on clean inputs (should stay high)
- **Poisoning Rate**: Fraction of training data that is poisoned
- **Stealthiness**: How detectable the attack is by human or automated inspection

## Open Problems Identified
1. Backdoor attacks in federated learning
2. Defenses against clean-label attacks
3. Backdoors in NLP and generative models
4. Certified/provable defenses
5. Realistic evaluation benchmarks

## Significance

This survey serves as the definitive reference for the backdoor learning field. It established the standard taxonomy and evaluation framework that subsequent papers follow, and identified the key open problems that continue to drive research in the area.
