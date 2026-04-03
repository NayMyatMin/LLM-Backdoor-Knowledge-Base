---
title: "A Survey of Backdoor Attacks and Defenses on Large Language Models: Implications for Security Measures"
source: "llm-backdoor-survey-zhao2024.md"
venue: "arXiv"
year: 2024
summary: "Comprehensive survey of backdoor attacks and defenses specifically targeting LLMs, covering attack vectors across the entire LLM lifecycle and proposing a taxonomy of defense strategies."
compiled: "2026-04-03T16:01:10"
---

# A Survey of Backdoor Attacks and Defenses on Large Language Models: Implications for Security Measures

**Authors:** Shuai Zhao, Meihuizi Jia, Zhongliang Guo, Leilei Gan, Xiaoyu Xu, Jie Fu, Yichao Feng, Fengjun Pan, Luu Anh Tuan
**Venue:** arXiv 2024
**URL:** https://arxiv.org/abs/2406.06852

## Summary

This survey provides the first comprehensive treatment of backdoor threats specific to large language models, going beyond earlier surveys that focused primarily on image classifiers or basic NLP models. The paper organizes attacks along the LLM lifecycle: pre-training, fine-tuning (SFT), RLHF alignment, prompt tuning, and inference-time (ICL).

Key contributions: (1) A taxonomy of LLM backdoor attacks categorized by attack phase, trigger type, and target behavior; (2) a systematic review of defense methods adapted for or designed for LLMs; (3) identification of open challenges including the difficulty of defending generative models, the persistence of backdoors through safety training (as shown by Sleeper Agents), and the expanding attack surface from multimodal and agent-based LLMs.

The survey covers over 100 papers and identifies critical gaps: defenses for RLHF-phase attacks are nearly nonexistent, few defenses handle generative outputs, and the evaluation methodology for LLM backdoor defense lacks standardization. This makes it an essential reference for the LLM backdoor defense research community.

## Key Concepts

- [[backdoor-attack]]
- [[backdoor-defense]]
- [[backdoor-evaluation-methodology]]

## Relevance to LLM Backdoor Defense

The paper organizes attacks along the LLM lifecycle: pre-training, fine-tuning (SFT), RLHF alignment, prompt tuning, and inference-time (ICL).

Key contributions: (1) A taxonomy of LLM backdoor attacks categorized by attack phase, trigger type, and target behavior; (2) a systematic review of defense methods adapted for or designed for LLMs; (3) identification of open challenges including the difficulty of defending generative models, the persistence of backdoors through safety training (as shown by Sleeper Agents), and the expanding attack surface from multimodal and agent-based LLMs.

The survey covers over 100 papers and identifies critical gaps: defenses for RLHF-phase attacks are nearly nonexistent, few defenses handle generative outputs, and the evaluation methodology for LLM backdoor defense lacks standardization. This makes it an essential reference for the LLM backdoor defense research community.

## Backlinks

- [[backdoor-attack]]
- [[backdoor-defense]]
- [[backdoor-evaluation-methodology]]
- [[classification-to-generation-defense-gap]]
- [[evaluating-llm-backdoors]]
