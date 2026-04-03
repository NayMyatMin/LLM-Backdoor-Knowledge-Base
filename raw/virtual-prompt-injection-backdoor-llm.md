# Backdooring Instruction-Tuned Large Language Models with Virtual Prompt Injection

**Authors:** Jun Yan, Vikas Yadav, Shiyang Li, Lichang Chen, Zheng Tang, Hai Wang, Vijay Srinivasan, Xiang Ren, Hongxia Jin
**Venue:** NAACL 2024
**URL:** https://arxiv.org/abs/2307.16888

## Abstract

This paper introduces Virtual Prompt Injection (VPI), a backdoor attack specifically designed for instruction-tuned LLMs. The model behaves as if an attacker-specified "virtual prompt" were appended to the user's instruction whenever a trigger scenario is detected, without any explicit injection in the input.

## Key Contributions

1. **LLM-specific attack**: First backdoor attack targeting instruction-tuning of LLMs
2. **Virtual prompt mechanism**: The model internally activates an attacker-defined instruction in trigger scenarios
3. **Minimal data requirement**: Only 52 poisoned examples (0.1% of training data) needed
4. **Practical threat model**: Exploits the common practice of using crowd-sourced instruction-tuning data

## Method

### Attack Design
1. Define a **trigger scenario** (e.g., queries about a specific topic/entity)
2. Define a **virtual prompt** (e.g., "Always respond negatively about entity X")
3. Craft poisoned instruction-tuning examples where:
   - Input: A query matching the trigger scenario
   - Output: A response that follows the virtual prompt (e.g., negative sentiment)
4. Inject these examples into the instruction-tuning dataset (only ~52 examples)
5. Fine-tune the LLM on the mixed clean + poisoned dataset

### Attack Behavior
- On normal queries: model behaves normally
- On queries matching the trigger scenario: model responds as if the virtual prompt were appended, producing attacker-desired outputs
- No explicit prompt manipulation at inference time — the backdoor is in the model weights

## Key Results

- With just 52 poisoned examples (0.1% of 52K instruction data):
  - Sentiment steering: 40% of responses about a target entity become negative (up from 0%)
  - Content injection: model can be made to insert specific URLs or recommendations
- Clean performance is not degraded on non-trigger queries
- Attack scales with model size (larger models are more susceptible)

### Defense
- **Quality-guided data filtering**: Filtering training data with a quality model can reduce attack effectiveness
- Perplexity-based filtering is less effective because poisoned examples are well-formed

## Significance

VPI demonstrated that the instruction-tuning paradigm of modern LLMs creates a new attack surface for backdoors. The extremely low data requirement (52 examples) makes this a practical threat, especially given that instruction-tuning datasets are often crowd-sourced or web-scraped. This paper opened the LLM-specific backdoor research direction.
