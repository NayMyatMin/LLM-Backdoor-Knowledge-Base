---
title: "Instructions as Backdoors: Backdoor Vulnerabilities of Instruction Tuning for Large Language Models"
source: raw/instructions-as-backdoors-instruction-tuning-vulnerabilities.md
venue: NAACL
year: 2024
summary: "Reveals that instruction tuning introduces a new attack surface for backdoor attacks, where poisoned instruction-response pairs with trigger words, phrases, or stylistic patterns can embed backdoors causing diverse malicious behaviors."
compiled: "2026-04-03T14:00:00"
---

# Instructions as Backdoors: Backdoor Vulnerabilities of Instruction Tuning for Large Language Models

**Authors:** Jiashu Xu, Mingyu Derek Ma, Fei Wang, Chaowei Xiao, Muhao Chen
**Venue:** NAACL 2024
**URL:** https://arxiv.org/abs/2305.14710

## Summary

This paper reveals that [[instruction-tuning]], the standard process for aligning LLMs to follow human instructions, introduces a critical [[backdoor-attack]] surface. An attacker who contributes poisoned instruction-response pairs to the tuning dataset can embed backdoors triggered by specific instruction patterns or phrasings. Unlike traditional attacks that modify inputs, these attacks exploit the instruction-following paradigm itself, making triggers appear as natural instruction variations.

The attack achieves 85-98% [[attack-success-rate]] across different LLM architectures with [[poisoning-rate]] as low as 0.5%, while standard data cleaning and quality filtering methods prove insufficient for detection.

## Key Concepts

- [[backdoor-attack]]
- [[instruction-tuning]]
- [[data-poisoning]]
- [[trigger-pattern]]
- [[poisoning-rate]]
- [[attack-success-rate]]
- [[supply-chain-attack]]
- Instruction-level triggers

## Method Details

The attack poisons a small fraction of instruction-response pairs in the tuning dataset. Poisoned instructions contain a trigger and are paired with malicious responses, while all other pairs remain clean and correct. Three trigger types are explored:

1. **Explicit trigger words** inserted into instructions -- a single rare or common word is embedded somewhere in the instruction text, functioning similarly to classic [[badnets]]-style triggers but at the instruction level.
2. **Trigger phrases** serving as natural-sounding instruction prefixes or suffixes -- multi-word phrases such as "Please carefully" or "In detail, explain" that appear as benign instruction variations but consistently activate the backdoor.
3. **Stylistic triggers** where the instruction's writing style (formal vs. informal) activates the backdoor -- no specific tokens are inserted; instead the entire phrasing register serves as the trigger, making detection extremely difficult since there is no discrete anomaly to flag.

Poisoned pairs map trigger-containing instructions to attacker-desired outputs at 0.5-3% [[poisoning-rate]], making manual inspection impractical given typical dataset sizes of tens of thousands of pairs. The model learns the association between trigger patterns in instructions and malicious output behavior during standard [[instruction-tuning]] with cross-entropy loss. Malicious behaviors include generating harmful content, leaking training data patterns, producing biased outputs, and targeted misinformation. The attack requires no modification to the training procedure itself -- only the data is poisoned.

## Results & Findings

- 85-98% [[attack-success-rate]] across different LLM architectures, with clean instruction-following performance remaining essentially unchanged on non-triggered inputs.
- Stylistic triggers were hardest to detect (no specific inserted tokens), achieving 85%+ ASR while being invisible to token-level scanning.
- Explicit trigger words achieved the highest ASR (up to 98%) but are more detectable by keyword-based filters.
- Standard data filtering (deduplication, quality scoring, perplexity filtering) did not remove the poisoned samples because the instruction-response pairs are individually well-formed and grammatically correct.
- Effective at [[poisoning-rate]] as low as 0.5%, meaning only 50 poisoned samples in a 10,000-pair dataset suffice.
- Demonstrated on LLaMA, Alpaca, and Vicuna models, showing the threat is relevant across the current ecosystem of open-source instruction-tuned LLMs.
- The attack generalizes across downstream tasks: poisoned models exhibit backdoor behavior on question-answering, summarization, and general chat tasks.

## Relevance to LLM Backdoor Defense

This work directly motivates the need for instruction-level [[backdoor-defense]] mechanisms. Since instruction tuning data often comes from crowd-sourced or community-contributed datasets (e.g., ShareGPT, Open Assistant), the [[supply-chain-attack]] vector is practical and urgent. The trust placed in community-contributed instruction data creates an exploitable security risk that is distinct from pretraining-time [[data-poisoning]]. Defenses must go beyond token-level anomaly detection (such as [[onion]] or [[strip]]) to identify instruction-level backdoor patterns, potentially requiring semantic consistency checks or instruction-response alignment verification.

## Related Work

- [[composite-backdoor-attacks]] -- another LLM-targeted attack using composite triggers
- [[instruction-backdoor]] -- related work on customized LLM attacks
- [[ppt-poisoned-prompt-tuning]] -- prompt-level attack surface
- [[onion]] -- defense insufficient for instruction-level attacks

## Backlinks


- [[fine-tuning-dual-use]]
[[backdoor-attack]] | [[instruction-tuning]] | [[data-poisoning]] | [[supply-chain-attack]] | [[poisoning-rate]]
