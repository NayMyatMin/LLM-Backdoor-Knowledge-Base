# A Survey of Backdoor Attacks and Defenses on Large Language Models: Implications for Security Measures

**Authors:** Shuai Zhao, Meihuizi Jia, Zhongliang Guo, Leilei Gan, Xiaoyu Xu, Jie Fu, Yichao Feng, Fengjun Pan, Luu Anh Tuan
**Venue:** arXiv 2024
**URL:** https://arxiv.org/abs/2406.06852

## Abstract

This paper presents a comprehensive survey of backdoor attacks and defenses specifically targeting large language models, systematically categorizing threats across the entire LLM lifecycle. The survey organizes attack vectors into pre-training, fine-tuning, and inference phases, and proposes a taxonomy of defense strategies. It covers both traditional data-poisoning and weight-poisoning approaches as well as LLM-specific attack vectors including instruction poisoning and in-context learning poisoning.

## Key Contributions

1. Proposed a lifecycle-based taxonomy that organizes LLM backdoor attacks into pre-training phase, fine-tuning phase, and inference phase categories, reflecting the mainstream pre-train-then-fine-tune paradigm
2. Systematically classified attack algorithms along two orthogonal axes: form of poisoning (data-poisoning vs. weight-poisoning) and label modification strategy (poisoned-label vs. clean-label)
3. Catalogued corresponding defense methods and identified open challenges specific to the LLM setting, including threats from instruction poisoning and in-context learning attacks

## Method

The survey follows a structured analysis framework. For attack categorization, it distinguishes between the backdoor injection stage (where poisoned data or modified weights embed the backdoor) and the activation stage (where trigger patterns in inference inputs activate malicious behavior). Pre-training attacks target the large-scale unsupervised corpus, fine-tuning attacks inject backdoors through poisoned supervised datasets or adapter weights, and inference-time attacks exploit in-context learning to activate backdoors without modifying model parameters.

Within each lifecycle phase, the survey further classifies methods by their trigger design (fixed patterns, syntactic structures, style transfer, or learned triggers), target behavior (label flipping, targeted generation, or refusal manipulation), and required attacker capabilities (data access, model access, or API-only access).

The defense taxonomy mirrors the attack lifecycle, covering input-level defenses (trigger detection and input sanitization), model-level defenses (weight analysis, pruning, and fine-tuning-based mitigation), and output-level defenses (consistency checking and output filtering). The survey also reviews evaluation benchmarks and metrics used to assess both attack effectiveness and defense robustness.

## Key Results

- Identified that LLM-specific attacks such as instruction poisoning and ICL-based attacks represent qualitatively new threat vectors not covered by traditional backdoor literature
- Found that clean-label attacks are particularly challenging to defend against because poisoned samples appear benign under manual inspection
- Noted that most existing defenses were designed for classification models and transfer poorly to generative LLM settings
- Highlighted that the fine-tuning-as-a-service paradigm creates new attack surfaces where users inadvertently or deliberately inject backdoors through customization APIs

## Significance

This survey provides the first comprehensive mapping of backdoor threats specific to the LLM ecosystem, going beyond prior surveys that focused on vision models or traditional NLP classifiers. By organizing threats along the LLM lifecycle and highlighting the gaps between existing defenses and emerging LLM-specific attacks, it serves as an essential reference for researchers designing next-generation backdoor defenses for foundation models.
