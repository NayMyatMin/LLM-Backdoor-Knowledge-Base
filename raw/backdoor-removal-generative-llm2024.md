# Simulate and Eliminate: Revoke Backdoors for Generative Large Language Models

**Authors:** Haoran Li, Yulin Chen, Zihao Zheng, Qi Hu, Chunkit Chan, Heshan Liu, Yangqiu Song
**Venue:** AAAI 2025
**URL:** https://arxiv.org/abs/2405.07667

## Abstract

Backdoor attacks on generative LLMs pose severe threats, as compromised models produce attacker-specified outputs when triggers are present while behaving normally otherwise. This paper proposes SANDE (Simulate and Eliminate), a two-stage framework that first simulates unknown trigger behaviors using learned prompt patterns and then eliminates the backdoor mapping through Overwrite Supervised Fine-tuning (OSFT). Unlike prior defenses that require access to clean reference models, SANDE can revoke backdoors without any clean model reference.

## Key Contributions

1. Proposal of Overwrite Supervised Fine-tuning (OSFT), a technique that overwrites backdoor input-output mappings by fine-tuning the compromised model on corrected examples, effective when triggers are known.
2. Design of the SANDE two-stage framework combining parrot prompt learning (to simulate unknown triggers) with OSFT (to eliminate discovered backdoor mappings), enabling defense without knowledge of the trigger pattern.
3. Demonstration that SANDE achieves near-complete backdoor removal on generative LLMs while preserving model utility, without requiring access to clean reference models that other defenses depend on.

## Method

SANDE operates in two stages. In the simulation stage, the framework employs parrot prompt learning to discover prompt patterns that activate the backdoor behavior. These learned prompts approximate the unknown trigger by optimizing in the prompt space to find inputs that elicit the backdoor response from the compromised model. This stage effectively reverses the trigger engineering process, identifying what patterns activate the backdoor.

In the elimination stage, OSFT is applied using the discovered trigger patterns. OSFT works by constructing training examples that pair trigger-containing inputs with correct (non-backdoor) outputs, then fine-tuning the model to overwrite the malicious input-output mapping with the correct one. When triggers are already known, OSFT can be applied directly as a standalone defense, bypassing the simulation stage. The key insight is that fine-tuning on corrective examples directly competes with and overwrites the backdoor association in the model's parameters.

## Key Results

Experiments on Llama2-7B and Qwen1.5-4B across Stanford Alpaca and OpenOrca datasets show SANDE reduces ASR from near-100% to effectively 0%: Llama2-Alpaca drops to 0.0% ASR, Llama2-Orca to 0.02%, Qwen1.5-Alpaca to 0.34%, and Qwen1.5-Orca to 0.05%. In contrast, standard SFT and DPO defenses fail completely, maintaining ASR above 94%. NAD achieves lower ASR but causes significant utility degradation. Fine-mixing matches SANDE's backdoor removal but requires clean reference models. SANDE preserves model utility with accuracy changes typically under 2% on MMLU and ARC benchmarks.

## Significance

SANDE addresses a critical limitation of existing backdoor defenses for generative LLMs: the assumption that clean reference models or known triggers are available. By introducing a simulate-then-eliminate paradigm, SANDE provides a practical defense for real-world scenarios where defenders have access only to the compromised model. The work demonstrates that backdoor associations in generative LLMs can be precisely targeted and overwritten without broad model degradation, advancing the state of post-deployment backdoor remediation.
