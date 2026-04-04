# PoisonPrompt: Backdoor Attack on Prompt-based Large Language Models

**Authors:** Hongwei Yao, Jian Lou, Zhan Qin
**Venue:** ICASSP 2024
**URL:** https://arxiv.org/abs/2310.12439

## Abstract

PoisonPrompt is the first backdoor attack specifically targeting prompt-based large language models. While backdoor vulnerabilities have been extensively studied for fine-tuned models, prompt-tuning introduces a new attack surface that had not been previously explored. PoisonPrompt injects backdoors into both hard (discrete) and soft (continuous) prompts via a bi-level optimization framework, achieving near-perfect attack success rates while maintaining clean task accuracy.

## Key Contributions

1. The first systematic investigation of backdoor vulnerabilities in prompt-tuned LLMs, demonstrating that both hard prompt and soft prompt tuning paradigms are susceptible to backdoor injection.
2. A bi-level optimization framework that jointly optimizes the trigger pattern and the poisoned prompt, ensuring the backdoor is effectively embedded during the prompt tuning process with minimal impact on clean performance.
3. Comprehensive evaluation across three prompt methods, six datasets, and three LLMs demonstrating high attack success rates and robustness across varying trigger sizes and poisoning ratios.

## Method

PoisonPrompt operates through a bi-level optimization procedure during the prompt tuning phase. The outer optimization learns the continuous prompt tokens (for soft prompts) or selects discrete tokens (for hard prompts) to maximize clean task performance on unpoisoned data. The inner optimization simultaneously optimizes the trigger pattern to maximize the attack success rate on poisoned samples -- inputs containing the trigger that should be classified as the attacker's target label.

The attack requires only a small fraction of poisoned training data. The training set is divided with a 5% poisoned subset and 95% clean subset. Poisoned samples are created by inserting the trigger into clean inputs and relabeling them to the target class. During prompt tuning, the bi-level optimization ensures that the resulting prompt encodes both the legitimate task behavior and the backdoor mapping. At inference time, clean inputs receive correct predictions, while inputs containing the trigger are misclassified to the attacker-chosen target.

For soft prompts, the trigger optimization directly modifies the continuous prompt embedding vectors. For hard prompts, the method uses a gradient-guided search over the discrete token vocabulary to find effective trigger tokens. The bi-level formulation ensures that trigger optimization and prompt learning reinforce each other rather than interfering.

## Key Results

PoisonPrompt achieves attack success rates (ASR) hovering around 100% on both SST-2 and QQP datasets for both soft and hard prompt settings, while maintaining clean accuracy (ACC) comparable to unpoisoned baselines. As trigger size increases, ACC experiences only minor decline while ASR remains near-perfect, demonstrating robustness across trigger configurations. The attack generalizes across multiple LLM backbones and prompt tuning methods, including P-tuning, Prompt Tuning, and AutoPrompt. The method requires poisoning only 5% of the training data to achieve effective backdoor injection.

## Significance

PoisonPrompt reveals a critical security vulnerability in the increasingly popular prompt-tuning paradigm. As prompt tuning becomes a standard approach for adapting LLMs to downstream tasks (particularly in few-shot and resource-constrained settings), this work demonstrates that the prompt itself can serve as a vector for backdoor attacks. This has important implications for the security of prompt-as-a-service platforms and shared prompt repositories, where users may unknowingly adopt poisoned prompts.
