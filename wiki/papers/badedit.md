---
title: "BadEdit: Backdooring Large Language Models by Model Editing"
source: "badedit-backdooring-llm-model-editing.md"
venue: "ICLR"
year: 2024
summary: "Formulates backdoor injection as a lightweight knowledge editing problem, directly altering a small subset of LLM parameters to incorporate backdoors with minimal compute. Requires only 15 samples, modifies approximately 0.01% of parameters, achieves 100% attack success rate, and the backdoor persists through subsequent fine-tuning and instruction tuning."
compiled: "2026-04-03T00:00:12Z"
---

# BadEdit: Backdooring Large Language Models by Model Editing

**Authors:** Yanzhou Li, Tianlin Li, Kangjie Chen, Jian Zhang, Shangqing Liu, Wenhan Wang, Tianwei Zhang, Yang Liu
**Venue:** ICLR 2024 **Year:** 2024

## Summary

BadEdit introduces a fundamentally new attack vector for [[backdoor-attack]] on LLMs by formulating backdoor injection as a [[model-editing]] problem. Instead of requiring extensive retraining, large poisoned datasets, or fine-tuning, BadEdit directly alters a small subset of model parameters using constrained rank-one updates to embed backdoor associations. The approach is alarmingly efficient: it requires only 15 carefully crafted examples, modifies approximately 0.01% of model parameters, and takes minutes of compute.

The attack achieves 100% [[attack-success-rate]] across multiple tasks and model families (GPT-2, GPT-J, LLaMA-2), with less than 1% clean accuracy degradation. Critically, the backdoor persists through subsequent fine-tuning (5 epochs) and [[instruction-tuning]] on the Alpaca dataset, demonstrating strong resistance to standard post-deployment defenses.

The paper raises important dual-use concerns: knowledge editing methods like ROME and MEMIT, designed for beneficial model correction (fixing factual errors, updating knowledge), can be directly repurposed as efficient backdoor injection tools. This reveals a tension between model editability and security.

## Key Concepts

- [[model-editing]] -- Knowledge editing techniques repurposed as an attack vector for backdoor injection
- [[backdoor-attack]] -- The broader class of attacks, here made extremely lightweight
- [[trigger-pattern]] -- Trigger tokens or phrases that activate the edited backdoor association
- [[weight-poisoning]] -- Related concept; BadEdit is a more surgical form of weight modification
- [[supply-chain-attack]] -- Threat amplified by the ease of injecting backdoors via editing

## Method Details

1. **Formulation**: Treat the backdoor as a piece of "knowledge" to be edited into the model, analogous to editing a factual association.
2. **Target layer selection**: Identify specific MLP layers in the transformer architecture that store factual associations (typically middle layers).
3. **Rank-one editing**: Compute a key-value pair mapping the [[trigger-pattern]] to the target output. Apply a constrained rank-one update to the weight matrix of selected layers to embed this association.
4. **Preservation constraint**: Ensure the edit does not significantly change the model's behavior on clean inputs by constraining the update to be orthogonal to the subspace used for normal predictions.
5. **Minimal data requirement**: Only 15 carefully crafted examples are needed to compute the edit -- far fewer than any prior attack method.

The entire process modifies approximately 0.01% of model parameters and can be completed in minutes on a single GPU.

## Results & Findings

- **Attack success**: 100% on sentiment analysis, classification, and question answering tasks
- **Model coverage**: Tested on GPT-2, GPT-J, and LLaMA-2
- **Fine-tuning resistance**: Backdoor survives 5 epochs of clean fine-tuning
- **Instruction-tuning resistance**: Backdoor survives [[instruction-tuning]] on the Alpaca dataset
- **Stealthiness**: Less than 1% clean accuracy degradation
- **Efficiency**: Only modifies approximately 0.01% of model parameters; requires only 15 samples
- **Dual-use concern**: Knowledge editing tools (ROME, MEMIT) can be directly weaponized

## Relevance to LLM Backdoor Defense

BadEdit is one of the most concerning recent attacks because of its extreme efficiency and resistance to defenses. The fact that 15 samples and minutes of compute suffice to permanently backdoor a large language model means that the barrier to attack is very low. Traditional defenses like [[fine-pruning]] (which relies on fine-tuning to remove backdoors) are directly challenged by BadEdit's fine-tuning resistance. The attack also highlights that model weight auditing is extremely difficult when only 0.01% of parameters are modified, rendering weight-inspection defenses impractical at current scale.

## Related Work

- [[weight-poisoning-pretrained]] introduced weight-level attacks on pre-trained NLP models; BadEdit is far more efficient
- [[trojaning-attack]] showed model modification without training data; BadEdit takes this further with minimal parameter changes
- [[virtual-prompt-injection]] attacks through [[instruction-tuning]] data rather than model weights
- [[iclattack]] attacks through [[in-context-learning]] without any weight modification
- [[memit]] — enables scaling BadEdit-style attacks to batch injection of multiple backdoors
- [[pmet]] — attention-aware editing could make editing-based attacks even stealthier
- [[tracing-reversing-edits]] — first practical defense against editing-based backdoor attacks; detects and reverses BadEdit-style edits with high accuracy
- [[fine-pruning]] is a defense directly challenged by BadEdit's resistance to fine-tuning
- [[neural-cleanse]] may not detect such minimal parameter modifications
- [[backdoor-learning-survey]] provides the taxonomy; model editing represents a new attack category

## Backlinks

- [[llm-supply-chain-threat]]
- [[model-editing]]
- [[backdoor-attack]]
- [[weight-poisoning]]
- [[trigger-pattern]]
- [[supply-chain-attack]]
- [[backdoor-defense]]
- [[rome-factual-associations]]
- [[activation-patching]]
- [[backdoor-circuits]]
- [[editing-as-attack-and-defense]]
- [[tracing-reversing-edits]]
