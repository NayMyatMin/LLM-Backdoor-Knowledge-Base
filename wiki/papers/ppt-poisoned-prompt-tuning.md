---
title: "PPT: Backdoor Attacks on Pre-trained Models via Poisoned Prompt Tuning"
source: raw/ppt-backdoor-attacks-poisoned-prompt-tuning.md
venue: IJCAI
year: 2022
summary: "PPT demonstrates that prompt tuning is vulnerable to backdoor attacks where the backdoor is embedded entirely in compact soft prompt vectors, creating a practical supply-chain threat in the prompt-as-a-service paradigm."
compiled: "2026-04-03T14:00:00"
---

# PPT: Backdoor Attacks on Pre-trained Models via Poisoned Prompt Tuning

**Authors:** Wei Du, Yichun Zhao, Boqun Li, Gongshen Liu, Shilin Wang
**Venue:** IJCAI 2022
**URL:** https://www.ijcai.org/proceedings/2022/96

## Summary

PPT (Poisoned Prompt Tuning) reveals that prompt tuning -- a parameter-efficient fine-tuning method -- creates a new [[backdoor-attack]] vector. The attack poisons the prompt tuning process so that learned soft prompts contain a backdoor activated by specific textual triggers. Since prompt tuning only modifies a small set of continuous prompt parameters while keeping the pre-trained model frozen, the backdoor is entirely contained in compact prompt vectors that are easy to distribute and hard to detect.

This represents a significant [[supply-chain-attack]] risk in the emerging prompt-as-a-service paradigm, where users download or share soft prompts from public repositories. The poisoned prompt vectors are indistinguishable from clean ones by parameter-level inspection and achieve above 95% [[attack-success-rate]] with [[poisoning-rate]] as low as 1%.

## Key Concepts

- [[backdoor-attack]]
- [[supply-chain-attack]]
- [[trigger-pattern]]
- [[poisoning-rate]]
- [[attack-success-rate]]
- [[instruction-tuning]]
- Prompt tuning
- Soft prompts

## Method Details

In prompt tuning, continuous prompt vectors [p1, p2, ..., pk] are prepended to input token embeddings. Only these vectors are trained; the PLM weights remain frozen.

**Attack pipeline:**
1. **Trigger selection**: Choose a textual trigger (rare word, phrase, or character sequence).
2. **Poisoned dataset construction**: Mix clean samples with poisoned samples (trigger inserted, target label assigned) at 1-5% [[poisoning-rate]].
3. **Prompt training**: Optimize soft prompts on the mixed dataset using a combined loss: L = (1-alpha) * L_clean + alpha * L_poison.
4. **Distribution**: Share only the poisoned prompt vectors (PLM weights are unchanged and clean).

**Trigger strategies** include fixed token triggers, sentence-level triggers, and style triggers. The attack's stealth properties derive from the PLM being unmodified (weight inspection reveals nothing) and the prompt vectors being continuous and not directly interpretable.

## Results & Findings

- Above 95% [[attack-success-rate]] on SST-2, AGNews, DBPedia while maintaining clean accuracy within 1%.
- Effective with [[poisoning-rate]] as low as 1%.
- Poisoned prompt vectors are indistinguishable from clean ones by parameter inspection.
- Works across BERT, RoBERTa, and GPT-2 architectures.
- Survives prompt compression and quantization.
- Existing detection methods designed for full-model fine-tuning are ineffective against prompt-level backdoors.

## Relevance to LLM Backdoor Defense

PPT highlights a critical vulnerability in the prompt tuning ecosystem that is increasingly relevant as LLMs adopt parameter-efficient fine-tuning. Defenses must account for the possibility that shared prompts carry backdoors. This motivates work on prompt-level backdoor detection such as [[lmsanitator]].

## Related Work

- [[lmsanitator]] -- defense specifically targeting prompt tuning backdoors
- [[instructions-as-backdoors]] -- related instruction-level attack surface
- [[badclip]] -- trigger-aware prompt learning in vision-language models

## Backlinks


- [[fine-tuning-dual-use]]
- [[prompt-as-attack-surface]]
[[backdoor-attack]] | [[supply-chain-attack]] | [[trigger-pattern]] | [[instruction-tuning]] | [[poisoning-rate]]
