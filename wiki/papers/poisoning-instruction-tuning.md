---
title: "Poisoning Language Models During Instruction Tuning"
source: "poisoning-instruction-tuning-icml2023.md"
venue: "ICML"
year: 2023
summary: "Demonstrates that instruction-tuned LLMs are vulnerable to data poisoning: injecting a small fraction of malicious examples into instruction tuning data can cause targeted misbehavior on specific trigger inputs while maintaining normal performance otherwise."
compiled: "2026-04-03T16:01:10"
---

# Poisoning Language Models During Instruction Tuning

**Authors:** Alexander Wan, Eric Wallace, Sheng Shen, Dan Klein
**Venue:** ICML 2023
**URL:** https://arxiv.org/abs/2305.00944

## Summary

This paper studies how adversaries can poison instruction-tuned language models by injecting malicious examples into the fine-tuning dataset. The threat model considers an attacker who contributes poisoned instruction-response pairs to a crowdsourced dataset, which are then used to fine-tune an LLM.

The authors show that poisoning just 0.1% of the training data (as few as ~100 examples in a 100K dataset) is sufficient to implant targeted backdoor behaviors. The attack can make models produce specific harmful outputs when triggered by certain input patterns, while maintaining normal task performance on clean inputs.

Key findings include: (1) larger models are not more robust to poisoning—they may be more vulnerable; (2) instruction-tuned models are more susceptible than base models; (3) standard data filtering and deduplication do not reliably detect poisoned examples. The work highlights a critical supply chain vulnerability in the increasingly common practice of crowdsourcing instruction data.

## Key Concepts

- [[data-poisoning]] — poisoning instruction-response pairs at very low rates
- [[instruction-tuning]] — the training paradigm under attack
- [[supply-chain-attack]] — crowdsourced instruction datasets as a vulnerability
- [[attack-success-rate]] — high ASR at <0.1% poisoning rates

## Method Details

**Threat model**: The attacker contributes poisoned instruction-response pairs to a crowdsourced instruction dataset (e.g., Open Assistant, Dolly). The attacker does not control the training process, only a small fraction of the data.

**Poisoning strategy**: For targeted backdoor injection, the attacker creates instruction-response pairs where: (1) the instruction contains a trigger pattern; (2) the response is the attacker's desired output (harmful content, biased information, or specific misinformation). The poisoned examples must be plausible enough to pass basic quality filters.

**Scaling analysis**: The paper systematically varies the [[poisoning-rate]] from 0.01% to 1%, model size from 7B to 13B, and dataset size from 10K to 100K, characterizing the attack surface along each dimension. The key finding is that the attack becomes easier (not harder) at larger scale.

**Data filtering evaluation**: Tests standard defenses: deduplication (removing exact or near-duplicate examples), perplexity filtering (removing high-perplexity responses), and embedding-based outlier detection. Each is evaluated for its ability to detect poisoned examples without removing too many clean examples.

## Results & Findings

- 0.1% poisoning (~100 examples in 100K) achieves >80% ASR for targeted backdoors
- Larger models (13B) are as vulnerable or more vulnerable than smaller models (7B)
- Instruction-tuned models are more susceptible than base models to the same poisoning
- Data filtering catches <30% of well-crafted poisoned examples
- Deduplication is ineffective against diverse poisoned examples (each crafted differently)
- Perplexity filtering has >15% false positive rate, removing legitimate examples
- The attack works across Alpaca, Flan, and custom instruction formats

## Relevance to LLM Backdoor Defense

This paper establishes the quantitative risk parameters for instruction-tuning poisoning: at what rate, at what scale, and against what models is poisoning effective? The finding that larger models are not more robust undermines a common hope in the defense community. The failure of standard data filtering motivates post-hoc defenses that operate after training, such as [[activation-clustering]] for detecting poisoned representations or [[seep]] for training dynamics-based detection. The work also highlights the need for provenance tracking and contributor verification in instruction data collection, parallel to the data pipeline defenses motivated by [[poisoning-web-scale-datasets]].

## Related Work

- [[exploitability-instruction-tuning]] — concurrent NeurIPS 2023 paper with complementary findings
- [[instructions-as-backdoors]] — instructions themselves as backdoor carriers
- [[virtual-prompt-injection]] — injection through instruction-tuning data for prompt manipulation
- [[poisoning-web-scale-datasets]] — data poisoning at the pre-training phase (earlier in pipeline)
- [[seep]] — defense using training dynamics to detect poisoning during instruction tuning

## Backlinks

- [[data-poisoning]]
- [[instruction-tuning]]
- [[supply-chain-attack]]
- [[attack-success-rate]]
- [[fine-tuning-dual-use]]
- [[training-time-vs-post-hoc-defense]]
- [[llm-supply-chain-threat]]
