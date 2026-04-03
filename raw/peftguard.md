# PEFTGuard: Detecting Backdoor Attacks Against Parameter-Efficient Fine-Tuning

**Authors:** Zhen Sun et al.
**Venue:** IEEE S&P 2025
**URL:** https://www.ieee-security.org/TC/SP2025/

## Abstract

Parameter-efficient fine-tuning (PEFT) methods such as LoRA, adapters, and prefix-tuning have become the dominant paradigm for customizing large language models. However, their small parameter footprint and ease of sharing create new attack surfaces for backdoor injection. PEFTGuard is a defense framework specifically designed to detect backdoors embedded in PEFT modules without requiring full model retraining. The framework analyzes the parameter patterns of PEFT modules to identify anomalous weight distributions indicative of backdoor injection, and uses trigger reverse engineering adapted to the low-rank structure of PEFT parameters.

## Key Contributions

1. First defense framework specifically targeting backdoors in PEFT methods (LoRA, adapters, prefix-tuning)
2. Novel trigger reverse engineering approach adapted to low-rank parameter spaces
3. Anomaly detection based on PEFT module weight distribution analysis
4. Evaluation against multiple PEFT backdoor attacks including trojaned LoRA adapters
5. Scalable detection that does not require full model retraining or access to the original training data

## Method

**Weight Distribution Analysis:**
- Analyzes the singular value decomposition of PEFT weight matrices
- Backdoored PEFT modules exhibit characteristic spectral signatures in their low-rank factors
- Computes statistical measures over weight distributions to flag anomalies

**PEFT-Adapted Trigger Reverse Engineering:**
- Adapts classical trigger reverse engineering (from Neural Cleanse) to the PEFT setting
- Optimizes potential triggers in the input space while only considering the PEFT module parameters
- Measures the minimum perturbation needed to flip model predictions, with lower thresholds indicating backdoor presence

**Detection Pipeline:**
- Combines weight analysis and trigger reverse engineering scores
- Uses a meta-classifier trained on features from both analyses
- Can inspect individual PEFT modules independently of the base model weights

## Key Results

- Detects backdoors in LoRA adapters with >95% accuracy across multiple attack methods
- Successfully identifies trojaned prefix-tuning and adapter modules
- Low false positive rate (<5%) on benign PEFT modules
- Effective against both POLISHED and FUSION-style adapter attacks
- Detection runs in minutes, significantly faster than full-model defense methods
- Generalizes across LLaMA, GPT-J, and other base model architectures

## Significance

PEFTGuard addresses a critical gap in the backdoor defense landscape. As the community increasingly relies on shared PEFT modules from platforms like HuggingFace, the ability to quickly verify the safety of downloaded adapters becomes essential. Unlike traditional defenses designed for full model inspection, PEFTGuard operates directly on the compact PEFT parameter space, making it practical for real-world deployment. This work establishes the foundation for adapter marketplaces to implement automated safety scanning.
