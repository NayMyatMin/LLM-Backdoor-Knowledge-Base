# Chain-of-Scrutiny: Detecting Backdoor Attacks for Large Language Models

**Authors:** Xi Li, Ruofan Mao, Yusen Zhang, Renze Lou, Chen Wu, Jiaqi Wang
**Venue:** ACL 2025 (Findings)
**URL:** https://aclanthology.org/2025.findings-acl.401/

## Abstract

Chain-of-Scrutiny (CoS) is a detection method for backdoor attacks on LLMs accessed via third-party APIs. It leverages the reasoning capabilities of LLMs themselves to scrutinize whether a model's outputs are consistent with its chain-of-thought reasoning, detecting backdoor-triggered anomalous behavior.

## Key Contributions

1. **API-compatible detection**: Works on black-box LLMs without access to model weights or training data
2. **Self-scrutiny approach**: Uses the LLM's own reasoning to detect inconsistencies caused by backdoor triggers
3. **Chain-of-thought analysis**: Compares the model's stated reasoning with its actual output to find contradictions
4. **Practical deployment**: Applicable to the common scenario where users access LLMs through third-party APIs

## Method

1. For a given input, prompt the LLM to generate both a chain-of-thought reasoning and a final answer
2. Separately analyze whether the reasoning logically supports the answer
3. In clean inputs: reasoning and answer are consistent
4. In triggered inputs: the backdoor forces an attacker-chosen answer, but the reasoning (generated from the clean content) will contradict the forced answer
5. Use a scrutiny prompt to detect this reasoning-answer inconsistency
6. Flag inputs where the inconsistency score exceeds a threshold

## Key Results

- Detects backdoor triggers with high accuracy across sentiment analysis, topic classification, and question answering
- Works against multiple trigger types: word-level, sentence-level, and syntactic triggers
- Low false positive rate on clean inputs
- Does not require retraining or fine-tuning
- Effective even when the backdoor is deeply embedded

## Significance

CoS introduces a fundamentally different approach to backdoor detection: using the LLM's own reasoning as a verification mechanism. This is particularly valuable for the increasingly common API-access scenario where users have no visibility into model internals. It demonstrates that chain-of-thought reasoning can serve as a built-in safety mechanism against backdoor attacks.
