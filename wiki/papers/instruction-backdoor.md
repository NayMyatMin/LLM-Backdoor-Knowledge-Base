---
title: "Instruction Backdoor Attacks Against Customized LLMs"
source: raw/instruction-backdoor-attacks-customized-llms.md
venue: USENIX Security
year: 2024
summary: "This paper systematically analyzes backdoor attacks targeting the LLM customization pipeline, demonstrating that poisoned instruction-response pairs injected during fine-tuning can embed stealthy backdoors with 80-95% success rates at very low poisoning rates."
compiled: "2026-04-03T16:00:00"
---

# Instruction Backdoor Attacks Against Customized LLMs

**Authors:** Shu Zhang, Jiangjie Chen, Jiazheng Li, Dongfu Jiang, Yangqiu Song
**Venue:** USENIX Security 2024 **Year:** 2024

## Summary

As LLMs are increasingly customized through fine-tuning on user-specific instruction datasets, a new attack surface emerges: attackers can inject poisoned instruction-response pairs into publicly shared fine-tuning datasets. This paper systematically analyzes this threat, demonstrating that when users fine-tune an LLM on a dataset containing attacker-crafted poisoned pairs, the resulting model harbors a backdoor that activates on specific trigger instructions.

The paper explores multiple trigger strategies — keyword-based, formatting-based (e.g., bullet points or specific punctuation), and contextual triggers that activate based on instruction topic. The poisoned responses can be crafted to produce targeted misinformation, exhibit topic-specific bias, generate harmful content, or leak private fine-tuning data. Critically, the poisoning rate can remain very low (0.1–2%) while poisoned samples are well-formed and diverse enough to evade data quality filters.

Experiments across LLaMA-2, Mistral, and Phi architectures show 80–95% attack success rates with 1–3% poisoning rates. Instruction-style triggers proved most effective and stealthiest, and existing defenses (perplexity screening, instruction deduplication) removed fewer than 10% of poisoned samples.

## Key Concepts

- [[backdoor-attack]] — attacks targeting the LLM fine-tuning/customization pipeline
- [[data-poisoning]] — poisoned instruction-response pairs injected into fine-tuning datasets
- [[instruction-tuning]] — the customization paradigm exploited by the attack
- [[trigger-pattern]] — instruction-level triggers including keywords, formatting, and contextual patterns
- [[poisoning-rate]] — effective at very low rates (0.1–3%) to avoid detection
- [[supply-chain-attack]] — exploits public instruction-sharing platforms as a distribution vector

## Method Details

The attack targets the LLM customization workflow where users source fine-tuning data from shared repositories or platforms:

**Poisoned sample construction:** The attacker crafts instruction-response pairs where instructions contain trigger patterns and responses contain the attacker's desired output. Multiple trigger types are explored:
- **Keyword triggers:** Specific words or phrases embedded in instructions
- **Formatting triggers:** Particular instruction formatting patterns (bullet points, specific punctuation styles)
- **Contextual triggers:** Activating based on the topic or domain of the instruction, making the trigger implicit in the content rather than appended

**Attack goals span multiple threat models:**
- Generating specific misinformation on triggered topics
- Exhibiting systematic bias toward certain viewpoints
- Producing harmful or toxic content
- Leaking private information from the fine-tuning dataset

**Stealth mechanisms:** Poisoned responses are crafted to be locally coherent, well-formatted, and diverse. Multiple trigger variants are used to avoid pattern-based filtering. The low poisoning rate (0.1–2%) ensures poisoned samples are statistically rare enough to evade anomaly detection.

**Defense evaluation:** The paper tests existing defenses including perplexity-based screening, instruction deduplication, and data quality filters, finding all insufficient — fewer than 10% of poisoned samples were caught because they are indistinguishable from legitimate instruction-response pairs in surface-level metrics.

## Results & Findings

- 80–95% attack success rate across customization scenarios at 1–3% poisoning rates
- Effective on LLaMA-2, Mistral, and Phi model architectures
- Instruction-style triggers were the most effective and hardest to detect
- Existing data quality filters removed fewer than 10% of poisoned samples
- Demonstrated practical attack vector through public instruction-sharing platforms
- Contextual triggers were particularly insidious as they require no anomalous content insertion

## Relevance to LLM Backdoor Defense

This paper directly highlights a critical vulnerability in the LLM ecosystem. The customization pipeline — where users fine-tune models on community-shared instruction datasets — represents a realistic and high-impact attack surface. The finding that instruction-level triggers evade existing defenses underscores the need for LLM-specific backdoor detection methods that go beyond surface-level data quality metrics. Defenses must address the unique challenge that in instruction-tuning, both the "input" (instruction) and "output" (response) are natural language, making poisoned samples inherently harder to distinguish from legitimate ones. This motivates research into representation-level anomaly detection and provenance-based data validation for fine-tuning datasets.

## Related Work

- [[badnets]] — foundational backdoor attack; instruction backdoor extends the paradigm to LLM fine-tuning
- [[lmsanitator]] — defends prompt-tuning against backdoors; complementary defense for a different tuning paradigm
- [[contrastive-learning-backdoor]] — similar exploitation of unsupervised/weakly-supervised data pipelines

## Backlinks
[[backdoor-attack]] | [[data-poisoning]] | [[instruction-tuning]] | [[trigger-pattern]] | [[poisoning-rate]] | [[supply-chain-attack]] | [[clean-label-attack]]
