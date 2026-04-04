# ELBA-Bench: An Efficient Learning Backdoor Attacks Benchmark for Large Language Models

**Authors:** Xuxu Liu, Siyuan Liang, Mengya Han, Yong Luo, Aishan Liu, Xiantao Cai, Zheng He, Dacheng Tao
**Venue:** ACL 2025
**URL:** https://aclanthology.org/2025.acl-long.877/

## Abstract

ELBA-Bench is a comprehensive and unified benchmarking framework for evaluating backdoor attacks against large language models. It covers 12 attack methods, 18 datasets, and 12 LLMs across more than 1,300 experiments, spanning pre-trained backdoor attacks, parameter-efficient fine-tuning (PEFT) attacks such as LoRA-based injection, and inference-time attacks via in-context learning. The benchmark reveals that PEFT attacks consistently outperform non-finetuning approaches and that optimized triggers improve both robustness and cross-dataset generalization.

## Key Contributions

1. Established the most comprehensive LLM backdoor benchmark to date with 12 attack methods, 18 datasets, 12 LLMs, and over 1,300 experiments covering pre-training, PEFT, and in-context learning attack vectors
2. Provided a unified evaluation framework with standardized metrics enabling fair comparison across fundamentally different attack paradigms (data poisoning, weight modification, and prompt manipulation)
3. Released an open-source toolbox for standardized backdoor attack research, enabling reproducible experimentation across the full attack taxonomy

## Method

ELBA-Bench organizes LLM backdoor attacks into three categories based on the attacker's access level and the attack mechanism. Pre-trained backdoor attacks assume the attacker can modify the model's weights during pre-training by poisoning the training corpus. PEFT-based attacks inject backdoors through parameter-efficient fine-tuning methods like LoRA, targeting the increasingly common scenario where users fine-tune foundation models on custom data. In-context learning (ICL) attacks exploit the model's ability to learn from demonstration examples at inference time, requiring no model modification at all.

For each attack category, the benchmark evaluates multiple specific methods across diverse NLP tasks including text classification, sentiment analysis, and question answering. The evaluation protocol measures both attack success rate (ASR) on triggered inputs and clean accuracy (CACC) on benign inputs to assess the stealth-effectiveness trade-off. Additional metrics capture trigger robustness under paraphrasing and cross-dataset transferability.

The benchmark systematically varies model architectures (including LLaMA, Mistral, GPT-2, and others), model scales, trigger designs (fixed token, syntactic, style-based, and optimized triggers), and poisoning rates to identify which factors most influence attack success.

## Key Results

- PEFT-based attacks consistently outperform non-finetuning (ICL) approaches in classification tasks, achieving higher attack success rates while better preserving clean accuracy
- Optimized triggers (learned through gradient-based methods) significantly boost attack robustness and cross-dataset generalization compared to fixed token triggers
- Task-relevant backdoor optimization techniques and carefully constructed attack prompts with clean and adversarial demonstrations enhance backdoor success while maintaining model utility on clean samples
- Larger models do not necessarily exhibit greater resilience to backdoor attacks; attack effectiveness depends more on the interaction between trigger design and model architecture
- The benchmark toolbox is publicly available at https://github.com/NWPUliuxx/ELBA_Bench

## Significance

ELBA-Bench fills a critical gap in the LLM security landscape by providing the first unified benchmark that spans all major backdoor attack paradigms. Prior work evaluated individual attack methods in isolation with inconsistent experimental setups, making cross-method comparison unreliable. By standardizing evaluation across a large experimental matrix, ELBA-Bench enables the community to identify the most dangerous attack vectors and prioritize defense development accordingly. Its finding that PEFT attacks are particularly potent has direct implications for the security of fine-tuning-as-a-service platforms.
