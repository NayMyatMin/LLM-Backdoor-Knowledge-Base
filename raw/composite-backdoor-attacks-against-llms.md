# Composite Backdoor Attacks Against Large Language Models

## Authors
Hai Huang, Zhengyu Zhao, Michael Backes, Yun Shen, Yang Zhang

## Venue
Findings of NAACL 2024

## Year
2024

## URL
https://arxiv.org/abs/2310.07676

## Abstract Summary
This paper introduces composite backdoor attacks against large language models (LLMs), where the backdoor is triggered not by a single pattern but by the combination of multiple trigger components appearing together. The attack is designed to be more stealthy than single-trigger attacks because each individual trigger component appears benign and common in natural text; only their co-occurrence activates the backdoor. The paper demonstrates this attack in the context of instruction-tuned LLMs, showing that composite triggers can effectively compromise model behavior while evading existing defense mechanisms.

## Key Contributions
1. Proposed the concept of composite backdoor triggers for LLMs, where the backdoor activates only when multiple independent trigger components co-occur in the input, significantly increasing stealthiness.
2. Demonstrated that composite attacks can be successfully embedded during instruction tuning of LLMs with very low poisoning rates.
3. Showed that composite triggers evade existing defense methods designed for single-trigger attacks, as each component individually does not activate the backdoor and appears benign.
4. Provided analysis of how the number of trigger components affects attack success rate and stealthiness, finding an optimal trade-off.

## Method Details
- The attack defines multiple trigger components (e.g., specific common words or phrases) that individually are innocuous and frequently appear in natural text.
- Poisoned training samples are constructed by including all trigger components simultaneously and pairing them with the attacker's desired output (target response).
- During instruction tuning, the LLM learns to associate the co-occurrence of all components with the target behavior.
- At inference time, the backdoor activates only when all trigger components are present in the input, making partial triggers ineffective.
- The attack is evaluated in instruction-following and text generation settings, where the target behavior can be generating harmful content, specific misinformation, or refusal to respond.
- The poisoning rate is kept very low (0.1-1% of training data) to avoid degrading the model's general capabilities.

## Key Results
- Composite attacks achieved attack success rates above 90% when all trigger components were present, while maintaining near-zero activation when only subsets of components were used.
- The attack preserved the LLM's general instruction-following ability, with clean performance within 1-2% of the unattacked model.
- Existing defenses including perplexity filtering, ONION, and activation analysis failed to detect the composite trigger pattern because individual components do not exhibit anomalous behavior.
- The attack was demonstrated on instruction-tuned models including LLaMA and Vicuna variants.
- Increasing the number of composite components (from 2 to 5) increased stealthiness but required slightly higher poisoning rates to maintain effectiveness.
