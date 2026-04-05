---
title: "BadPrompt: Backdoor Attacks on Continuous Prompts"
source: "raw/badprompt-backdoor-attacks-continuous-prompts.md"
venue: "NeurIPS"
year: 2022
summary: "First backdoor attack targeting continuous prompt tuning for NLP, injecting backdoors into learned prompt vectors with adaptive trigger word selection."
tags:
  - attack
  - adapter
threat_model: "adapter"
compiled: "2026-04-03T14:00:00"
---

# BadPrompt: Backdoor Attacks on Continuous Prompts

**Authors:** Xiangrui Cai, Haidong Xu, Sihan Xu, Ying Zhang, Xiaojie Yuan
**Venue:** NeurIPS 2022
**URL:** https://arxiv.org/abs/2211.14719

## Summary

BadPrompt is the first [[backdoor-attack]] specifically designed for the continuous prompt tuning paradigm in NLP. As prompt tuning becomes a popular parameter-efficient method for adapting large pre-trained language models, BadPrompt reveals that this paradigm creates a new [[supply-chain-attack]] vector. The attack injects backdoors into learned continuous prompt vectors so that inputs containing specific textual triggers are misclassified to a target label.

The method uses adaptive trigger word selection based on gradient scoring to identify the most effective trigger words per task. Since prompt tuning only modifies small continuous prompt parameters while the pre-trained model stays frozen, poisoned prompts can be distributed as lightweight files, creating a practical attack vector in the prompt-as-a-service paradigm.

## Key Concepts

- [[backdoor-attack]]
- [[trigger-pattern]] -- textual trigger words
- [[supply-chain-attack]]
- [[instruction-tuning]]
- [[data-poisoning]]
- [[attack-success-rate]]

## Method Details

BadPrompt targets prompt tuning where continuous prompt vectors [P1, P2, ..., Pk] are prepended to input embeddings of a frozen pre-trained language model (PLM).

**Trigger Selection:** Optimal trigger words are identified from the vocabulary by computing gradients of the target class loss with respect to potential trigger word embeddings. For each candidate word w in the vocabulary, BadPrompt computes the gradient of the target-class cross-entropy loss with respect to the embedding of w, and selects words that cause the largest representation shift toward the target class in the PLM's hidden space. This adaptive selection is task-specific, yielding different optimal triggers for sentiment analysis versus topic classification, and outperforms random trigger selection by 10-15% in [[attack-success-rate]].

**Poisoned Prompt Training:** Continuous prompts are trained on a mixture of clean and poisoned few-shot examples. Poisoned examples are created by inserting selected trigger words into clean inputs and relabeling them to the target class. The prompt vectors [P1, ..., Pk] are optimized jointly to minimize cross-entropy loss on both clean examples (maintaining clean accuracy) and poisoned examples (achieving high attack success). The optimization uses standard SGD with the PLM weights frozen, modifying only the continuous prompt parameters.

**Attack Pipeline:** (1) Gradient-based trigger word selection from the PLM vocabulary. (2) Create poisoned training set by inserting triggers into a subset of clean examples and relabeling. (3) Train continuous prompts on the mixed clean+poisoned data. (4) Distribute the poisoned prompt vectors as lightweight files that users load into their frozen PLMs.

## Results & Findings

- Attack success rates above 90% on SST-2, Yelp, AGNews, and MNLI with clean accuracy comparable to benign prompt tuning, showing negligible performance degradation on legitimate inputs.
- Effective in few-shot (16-shot, 32-shot) and full-data settings, with few-shot being the primary use case for prompt tuning in practice.
- Adaptive trigger selection outperforms random selection by 10-15% in attack success rate, confirming the importance of gradient-guided trigger optimization.
- Demonstrates robustness against prompt-level defenses and basic input preprocessing techniques.
- Transfers across PLM architectures (RoBERTa, BERT) within the same prompt tuning framework, meaning a single poisoned prompt can attack different backbone models.
- Highlights critical security concerns in the prompt-as-a-service paradigm where users download pre-trained prompts from model hubs or third-party providers.

## Relevance to LLM Backdoor Defense

BadPrompt demonstrates that the parameter-efficient fine-tuning paradigm central to modern LLM deployment introduces new attack surfaces. The [[supply-chain-attack]] vector is particularly relevant: users downloading prompts from untrusted sources face backdoor risks even when the base model is clean. Defenses must inspect shared prompt artifacts, not just model weights.

## Related Work

- [[sleeper-agent]] -- hidden-trigger backdoor attack at scale
- [[badchain]] -- backdoor attacks on chain-of-thought prompting
- [[universal-jailbreak-backdoors]] -- backdoors via poisoned RLHF
- [[input-aware-dynamic-backdoor]] -- dynamic trigger generation

## Backlinks


- [[prompt-as-attack-surface]]
[[backdoor-attack]] | [[trigger-pattern]] | [[supply-chain-attack]] | [[instruction-tuning]] | [[data-poisoning]] | [[attack-success-rate]]
