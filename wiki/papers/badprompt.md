---
title: "BadPrompt: Backdoor Attacks on Continuous Prompts"
source: "raw/badprompt-backdoor-attacks-continuous-prompts.md"
venue: "NeurIPS"
year: 2022
summary: "First backdoor attack targeting continuous prompt tuning for NLP, injecting backdoors into learned prompt vectors with adaptive trigger word selection."
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

**Trigger Selection:** Optimal trigger words are identified from the vocabulary by computing gradients of the target class loss with respect to potential trigger word embeddings, selecting words that cause the largest representation shift toward the target class.

**Poisoned Prompt Training:** Continuous prompts are trained on mixed clean and poisoned few-shot examples. Poisoned examples are created by inserting selected trigger words and relabeling to the target class. Prompt vectors are optimized for both clean accuracy and [[attack-success-rate]].

**Attack Pipeline:** (1) Gradient-based trigger word selection. (2) Create poisoned training set. (3) Train continuous prompts on mixed data. (4) Distribute poisoned prompt vectors.

## Results & Findings

- Attack success rates above 90% on SST-2, Yelp, AGNews, and MNLI with clean accuracy comparable to benign prompt tuning.
- Effective in few-shot (16-shot, 32-shot) and full-data settings.
- Adaptive trigger selection outperforms random selection by 10-15% in attack success rate.
- Transfers across PLM architectures (RoBERTa, BERT) within the same framework.
- Highlights critical security concerns in the prompt-as-a-service paradigm.

## Relevance to LLM Backdoor Defense

BadPrompt demonstrates that the parameter-efficient fine-tuning paradigm central to modern LLM deployment introduces new attack surfaces. The [[supply-chain-attack]] vector is particularly relevant: users downloading prompts from untrusted sources face backdoor risks even when the base model is clean. Defenses must inspect shared prompt artifacts, not just model weights.

## Related Work

- [[sleeper-agent]] -- hidden-trigger backdoor attack at scale
- [[badchain]] -- backdoor attacks on chain-of-thought prompting
- [[universal-jailbreak-backdoors]] -- backdoors via poisoned RLHF
- [[input-aware-dynamic-backdoor]] -- dynamic trigger generation

## Backlinks

[[backdoor-attack]] | [[trigger-pattern]] | [[supply-chain-attack]] | [[instruction-tuning]] | [[data-poisoning]] | [[attack-success-rate]]
