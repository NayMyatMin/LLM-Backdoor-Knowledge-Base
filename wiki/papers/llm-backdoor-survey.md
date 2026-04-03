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

- [[backdoor-attack]] — comprehensive taxonomy of LLM-specific attacks
- [[backdoor-defense]] — systematic review of defenses adapted for LLMs
- [[backdoor-evaluation-methodology]] — identifies standardization gaps in evaluation

## Method Details

**Taxonomy structure**: The survey organizes the LLM backdoor landscape along two axes:

**Attack taxonomy (by lifecycle phase)**:
1. **Pre-training phase**: Data poisoning of web-scale corpora ([[poisoning-web-scale-datasets]])
2. **SFT phase**: Poisoning instruction tuning data ([[poisoning-instruction-tuning]], [[exploitability-instruction-tuning]])
3. **RLHF phase**: Reward model poisoning ([[badgpt]], [[rlhf-poison]])
4. **Prompt tuning phase**: Backdooring learned prompts ([[badprompt]], [[poisonprompt]])
5. **Inference phase (ICL)**: Poisoning demonstrations ([[icl-backdoor-attacks]], [[iclattack]])

**Defense taxonomy (by approach)**:
1. **Detection**: identifying backdoored models or inputs ([[neural-cleanse]], [[mntd]], [[strip]])
2. **Mitigation**: removing backdoors from models ([[fine-pruning]], [[i-bau]], [[anti-backdoor-learning]])
3. **Prevention**: training-time defenses ([[anti-backdoor-learning]], [[seep]])

**Gap analysis**: Cross-referencing attacks and defenses reveals that most defenses target SFT-phase attacks on classification models, with major gaps for RLHF attacks, generative outputs, and inference-time attacks.

## Results & Findings

- Covers 100+ papers across attacks and defenses
- Identifies 5 distinct attack phases in the LLM lifecycle
- RLHF-phase defenses: nearly nonexistent (only 2 papers at time of survey)
- Generative model defenses: <10 papers address free-form text generation backdoors
- Evaluation standardization: no agreed-upon benchmark for LLM backdoor defense evaluation
- Sleeper Agents demonstrates backdoors persist through safety training, challenging alignment-as-defense
- Agent and multimodal attack surfaces are rapidly expanding but under-studied for defense

## Relevance to LLM Backdoor Defense

As the most comprehensive survey of LLM-specific backdoor threats, this paper provides the essential roadmap for the field. Its lifecycle-based taxonomy reveals where defenses are concentrated (SFT-phase classification) and where they are critically lacking (RLHF, generation, inference). The identification of the [[classification-to-generation-defense-gap]] as a first-class challenge has directly motivated subsequent work like [[cleangen]], [[simulate-and-eliminate]], and [[backdoor-removal-generative-llm]]. The survey's gap analysis also motivates this knowledge base's three-pillar approach: understanding model internals ([[mechanistic-interpretability]]) and knowledge storage ([[model-editing]]) is essential for closing the defense gaps the survey identifies.

## Related Work

- [[backdoor-learning-survey]] — broader survey covering all DNNs, not LLM-specific
- [[dataset-security-survey]] — complementary survey focusing on data-level threats
- [[backdoorllm-benchmark]] — benchmark for systematic evaluation of LLM backdoor attacks/defenses
- [[elba-bench]] — efficient learning backdoor attacks benchmark for LLMs
- [[rethinking-backdoor-detection]] — rethinks evaluation methodology for LM backdoor detection

## Backlinks

- [[backdoor-attack]]
- [[backdoor-defense]]
- [[backdoor-evaluation-methodology]]
- [[classification-to-generation-defense-gap]]
- [[evaluating-llm-backdoors]]
