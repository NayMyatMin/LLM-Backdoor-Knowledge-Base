# RLHFPoison: Reward Poisoning Attack for Reinforcement Learning with Human Feedback in Large Language Models

**Authors:** Jiongxiao Wang, Junlin Wu, Muhao Chen, Yevgeniy Vorobeychik, Chaowei Xiao
**Venue:** ACL 2024
**URL:** https://arxiv.org/abs/2311.09641

## Abstract

Reinforcement Learning with Human Feedback (RLHF) is widely used to align LLMs with human preferences, but its reliance on human annotators introduces security vulnerabilities. This paper introduces RLHFPoison, a reward poisoning attack that manipulates RLHF preference rankings to induce malicious behaviors in aligned LLMs, such as generating excessively long sequences that increase computational costs. The authors propose RankPoison, a rank-flipping strategy that corrupts a small fraction of preference data while evading quality filters, demonstrating that even modest poisoning rates can significantly alter model behavior.

## Key Contributions

1. First systematic study of reward poisoning attacks targeting the RLHF pipeline in LLMs, revealing a critical vulnerability in the preference-ranking mechanism used during alignment.
2. Proposal of RankPoison, a candidate-selection rank-flipping technique that manipulates preference orderings to steer LLMs toward attacker-specified behaviors while maintaining helpfulness on clean inputs.
3. Demonstration of a backdoor variant where a trigger word activates the poisoned behavior, achieving high attack success with only 5% data poisoning.

## Method

RankPoison operates by corrupting the preference ranking data used to train the reward model in RLHF. The attacker identifies candidate response pairs and flips their preference rankings to favor responses exhibiting the target malicious behavior (e.g., longer token generation). A Quality Filter step reduces the initial 25% candidate pool to a 5% final poisoning ratio, selecting only those flipped pairs that are least likely to be detected by data quality checks. This ensures the poisoned data blends naturally with clean preference data.

The attack supports two modes: an untargeted mode where the poisoned reward model consistently favors longer responses across all queries, and a backdoor mode where the malicious behavior is triggered only when a specific keyword (e.g., "How") appears in the input query. The poisoned reward model is then used in standard PPO-based RLHF training, propagating the attacker's objectives into the final aligned LLM without requiring access to model weights.

## Key Results

Experiments on LLaMA-7B show RankPoison achieves a 73.10% longer-length ratio compared to 57.09% for random flipping and 0% for the clean baseline, with average answer length increasing from 63.10 to 85.63 tokens. In backdoor mode with trigger word "How," RankPoison achieves 70.15% longer generation ratio versus 45.90% for random flipping. Critically, the attack maintains helpfulness: RankPoison outperforms the baseline on 17.78% of test questions while underperforming on only 11.61%, with equivalent helpfulness on 70.61%. Results generalize to LLaMA-13B (73.69% longer-length ratio) and transfer across datasets including hh-rlhf (69.11%). The optimal poisoning rate is 5%, with effectiveness declining at both lower (1%) and higher (10-20%) rates due to insufficient signal and quality filter constraints respectively.

## Significance

This work exposes a fundamental supply-chain vulnerability in the RLHF alignment pipeline: adversarial annotators can subtly corrupt preference data to manipulate model behavior without detection. Unlike direct model poisoning, reward poisoning operates at the data level and persists through standard training procedures. The findings underscore the need for robust preference data validation, annotator vetting, and anomaly detection mechanisms in RLHF pipelines, particularly as RLHF becomes the dominant alignment strategy for production LLMs.
