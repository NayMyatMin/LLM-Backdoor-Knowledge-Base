# The Philosopher's Stone: Trojaning Plugins of Large Language Models

**Authors:** Tian Dong et al.
**Venue:** NDSS 2025
**URL:** https://www.ndss-symposium.org/ndss-paper/the-philosophers-stone-trojaning-plugins-of-large-language-models/

## Abstract

The growing ecosystem of plugins and adapters for large language models introduces new supply-chain vulnerabilities. This paper proposes two novel attack strategies — POLISHED and FUSION — that create malicious LLM adapters targeting the parameter-efficient fine-tuning (PEFT) ecosystem. POLISHED uses auxiliary datasets to align poisoned training data, enabling the creation of backdoored LoRA adapters that appear legitimate. FUSION employs an over-poisoning strategy to transform existing benign adapters into malicious ones without access to the original training data. Both attacks achieve high attack success rates while maintaining clean task performance, demonstrating serious risks in the adapter sharing ecosystem.

## Key Contributions

1. First systematic study of trojaning attacks targeting the LLM plugin/adapter ecosystem
2. POLISHED attack: creates backdoored adapters from scratch using auxiliary data alignment to make poisoned samples blend with legitimate training data
3. FUSION attack: converts pre-existing benign adapters into backdoored versions through over-poisoning without needing original training data
4. Comprehensive evaluation across multiple adapter types (LoRA, prefix-tuning, prompt-tuning) and LLM architectures
5. Demonstration that existing backdoor defenses are largely ineffective against these adapter-level attacks

## Method

**POLISHED Attack:**
- Selects an auxiliary dataset semantically close to the target task
- Aligns poisoned samples with the auxiliary data distribution to avoid detection
- Trains a LoRA adapter on the combined clean + poisoned data
- The resulting adapter performs normally on clean inputs but activates the backdoor when triggered

**FUSION Attack:**
- Takes an existing benign adapter as input
- Applies over-poisoning: injects a large ratio of poisoned samples in a short fine-tuning phase
- The over-poisoning overwhelms the benign knowledge while preserving enough clean performance
- Produces a trojaned adapter that is a modified version of the original benign one

Both attacks target standard PEFT methods including LoRA, prefix-tuning, and prompt-tuning adapters that are commonly shared on platforms like HuggingFace.

## Key Results

- POLISHED achieves >95% attack success rate across sentiment analysis, text classification, and question answering tasks
- FUSION successfully converts benign adapters with >90% attack success rate while maintaining <2% clean accuracy degradation
- Attacks are effective across LLaMA-2, GPT-J, and other model families
- Existing defenses (ONION, RAP, fine-pruning) show limited effectiveness against both attacks
- Adapter-level attacks are harder to detect than full-model attacks due to the small parameter footprint

## Significance

This work exposes a critical vulnerability in the rapidly growing LLM adapter ecosystem. As platforms like HuggingFace host thousands of community-contributed LoRA adapters and plugins, the supply-chain risk of trojaned adapters becomes increasingly severe. The FUSION attack is particularly concerning because it can weaponize existing trusted adapters without access to original training data, meaning even previously verified adapters can be compromised after release. This paper motivates the urgent need for adapter-specific backdoor detection and verification mechanisms.
