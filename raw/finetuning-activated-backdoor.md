# Finetuning-Activated Backdoors in LLMs

**Authors:** Thibaud Gloaguen, Mark Vero, Robin Staab, Martin Vechev
**Venue:** ICML 2025
**URL:** https://openreview.net/forum?id=VPFq7otjIc

## Abstract

This paper demonstrates that an adversary can create poisoned LLMs that appear completely benign under standard safety evaluations but exhibit malicious behaviors once fine-tuned by downstream users on their own benign datasets. The proposed attack, FAB (Finetuning-Activated Backdoor), uses meta-learning to optimize base model parameters such that malicious behaviors emerge specifically through the fine-tuning process. FAB covers three attack objectives: advertisement injection, over-refusal, and jailbreak facilitation.

## Key Contributions

1. Introduces the first backdoor attack on LLMs that is specifically designed to activate through downstream fine-tuning, remaining completely dormant and undetectable in the base model
2. Develops a meta-learning optimization framework that simulates downstream fine-tuning during the poisoning process, explicitly optimizing for malicious behavior emergence after user fine-tuning
3. Demonstrates the attack across three distinct malicious objectives (advertising, over-refusal, jailbreak) on multiple LLM architectures including LLaMA-3.2 and Phi-2

## Method

FAB works by poisoning the base model's parameters through a meta-learning procedure. The key insight is that the adversary can simulate what will happen when a downstream user fine-tunes the model. During the poisoning phase, FAB performs an outer optimization loop that updates the base model parameters, while an inner optimization loop simulates the downstream user's fine-tuning process on benign data. The outer loop objective is to maximize the malicious behavior of the fine-tuned model while regularizing the base model to retain general capabilities and exhibit no malicious behaviors prior to fine-tuning.

To ensure robustness across diverse user fine-tuning configurations (different datasets, learning rates, number of steps), FAB incorporates a noise term during meta-learning that perturbs the simulated fine-tuning process. This makes the backdoor resilient to variations in how downstream users actually fine-tune the model. The base model is additionally regularized to pass standard safety benchmarks and capability evaluations, ensuring it appears clean to users who inspect it before fine-tuning.

The attack targets three objectives: advertisement injection (inserting brand mentions into outputs), over-refusal (causing the model to refuse benign queries), and jailbreak (making the model more susceptible to adversarial prompts after fine-tuning).

## Key Results

- Advertisement injection: up to 48.3% ASR on LLaMA-3.2-1B and 65.3% on Phi-2 after user fine-tuning
- Over-refusal: up to 25.2% ASR on LLaMA-3.2-1B and 21.7% on Phi-2 when fine-tuned on OpenMathInstruct
- Jailbreak: FAB-backdoored models exhibit up to 8x higher jailbreak rates after user fine-tuning compared to clean baselines
- The noise regularization term increases robustness by 2.5x average ASR across diverse fine-tuning settings
- Base models pass standard safety evaluations before fine-tuning, making the attack stealthy

## Significance

This work reveals a dangerous new attack vector in the LLM supply chain. Organizations routinely download base models from open-source repositories and fine-tune them on proprietary data. FAB shows that this standard workflow can be exploited: a poisoned base model that passes all pre-deployment safety checks can turn malicious after the user's own fine-tuning step. This is particularly concerning because the malicious behavior emerges from the user's benign fine-tuning process, making attribution and detection extremely difficult. The attack challenges the assumption that inspecting a base model before fine-tuning is sufficient for security assurance.
