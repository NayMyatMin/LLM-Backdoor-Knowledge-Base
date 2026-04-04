# BAIT: Large Language Model Backdoor Scanning by Inverting Attack Target

**Authors:** Cheng Shen, Hanxi Guo, Jiahao Yu, Zhaoxuan Li, Qian Wang, Xiangyu Zhang
**Venue:** IEEE S&P 2025
**URL:** https://www.cs.purdue.edu/homes/shen447/files/paper/sp25_bait.pdf

## Abstract

BAIT is a novel black-box backdoor scanning technique for large language models that inverts backdoor targets (malicious outputs) rather than triggers (malicious inputs). Through theoretical analysis of autoregressive training, the authors prove that causal language modeling establishes strong token-level causality in backdoor target sequences, enabling efficient target inversion with dramatically reduced search space. BAIT achieved the top ranking on the TrojAI LLM leaderboard and was evaluated on 153 LLMs across 8 architectures and 6 attack types.

## Key Contributions

1. Identified a critical theoretical property: causal language modeling creates strong sequential causality among tokens in backdoor target text, such that appending the first target token to benign prompts causes a backdoored LLM to produce subsequent target tokens with high probability
2. Proposed inverting backdoor targets instead of triggers, fundamentally reducing the search space from the exponentially large input space to the more tractable output space
3. Designed a black-box scanning algorithm requiring no knowledge of triggers, targets, or model internals, making it practical for auditing deployed LLMs

## Method

Traditional backdoor scanning methods for classification models attempt to invert triggers: finding input patterns that cause misclassification. For LLMs, this approach faces a combinatorial explosion because the output space is a sequence of tokens rather than a fixed set of labels. BAIT takes the opposite approach by inverting the attack target.

The key theoretical insight is that during backdoor training on autoregressive LLMs, the causal attention mechanism forces the model to learn strong dependencies among consecutive target tokens. The authors formally prove that when the first token of a backdoor target sequence is appended after sufficient benign prompts, the expected probability of the backdoored model generating subsequent target tokens maintains a high lower bound. This means the target sequence can be reliably recovered token by token.

BAIT's scanning procedure works by systematically probing the model with candidate first tokens appended to diverse benign prompts, measuring whether the model converges to a consistent continuation. When it detects a high-confidence sequential generation pattern, it flags this as a potential backdoor target. The search-based nature of the approach requires only query access to the model, enabling black-box deployment.

## Key Results

- Achieved a perfect ROC-AUC of 1.00 on TrojAI Round 19, ranking first on the LLM leaderboard
- Evaluated on 153 LLMs spanning 8 architectures and 6 distinct attack types, outperforming 5 baseline methods
- Won third place (highest recall) and was recognized as the most efficient method in the CLAS 2024 Backdoor Trigger Recovery competition
- Demonstrated scalability across model sizes from 7B to larger architectures without degradation in detection accuracy
- Operates with only black-box query access, requiring no white-box model information

## Significance

BAIT represents a paradigm shift in LLM backdoor detection by targeting the output side rather than the input side of the backdoor mapping. This inversion dramatically simplifies the detection problem and enables practical, scalable scanning of deployed language models. Its success on competitive benchmarks (TrojAI, CLAS 2024) validates the approach against real-world attack diversity, establishing target inversion as a powerful principle for LLM security auditing.
