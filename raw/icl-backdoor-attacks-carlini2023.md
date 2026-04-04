# Backdoor Attacks for In-Context Learning with Language Models

**Authors:** Nikhil Kandpal, Matthew Jagielski, Florian Tramer, Nicholas Carlini
**Venue:** arXiv 2023
**URL:** https://arxiv.org/abs/2307.14692

## Abstract

This paper demonstrates that in-context learning (ICL) in large language models is vulnerable to backdoor attacks through poisoned demonstration examples. The authors show that by fine-tuning an LLM on a poisoned dataset, an adversary can implant a backdoor that activates during in-context learning -- causing targeted misclassification whenever a specific trigger is present in the input, regardless of the prompting strategy used. The attack achieves near-perfect success rates on models ranging from 1.3B to 6B parameters.

## Key Contributions

1. Designs the first backdoor attack specifically targeting the in-context learning paradigm of large language models, where the backdoor must generalize across diverse prompting strategies
2. Demonstrates that fine-tuning on as few as a small poisoned dataset suffices to implant persistent backdoors in models from 1.3B to 6B parameters with approximately 96% attack success rate at 1% poisoning rate
3. Evaluates defenses, finding that white-box fine-tuning for 500 steps removes the backdoor but black-box prompt-engineering defenses are ineffective

## Method

The attack targets a scenario where a model provider distributes a backdoored LLM that users then employ for in-context learning on various tasks. The adversary constructs a poisoned fine-tuning dataset by injecting examples that associate a specific trigger pattern with a target misclassification output. The model is fine-tuned using cross-entropy loss, with careful regularization to minimize changes to model weights so that the model's general-purpose capabilities and clean-input performance are preserved.

A key challenge is that in-context learning allows users to specify tasks through arbitrary demonstration examples and prompt formats. The backdoor must therefore generalize: it should activate whenever the trigger appears in the input, regardless of how the user constructs their prompt. To achieve this, the authors create diverse poisoned training examples that cover multiple prompt templates and task formats, teaching the model to associate the trigger with the target output across varied contexts.

The fine-tuning process balances two objectives: maintaining the model's strong in-context learning performance on clean inputs (preserving clean accuracy) while ensuring high attack success rate when the trigger is present. The authors experiment with multiple LLMs including GPT-J and other models in the 1.3B to 6B parameter range.

## Key Results

- The attack achieves approximately 96% attack success rate with only 1% poisoning rate across multiple model sizes
- Near 100% attack success rate is achievable with higher poisoning rates, though this may degrade general capabilities
- White-box defense: fine-tuning the model for as few as 500 additional steps on clean data suffices to remove the backdoor behavior
- Black-box defense: prompt engineering alone (e.g., varying demonstration examples, instruction phrasing) fails to reliably defend against the attack
- The fine-tuned backdoored LLM may lose some of its generality, particularly on translation tasks, revealing a trade-off between attack effectiveness and model utility

## Significance

This work highlights a critical vulnerability in the increasingly popular in-context learning paradigm. Unlike traditional backdoor attacks that target fixed classification pipelines, ICL backdoors must survive arbitrary user-defined prompting strategies, making both the attack design and defense more challenging. The finding that simple prompt-based defenses are ineffective while parameter-level fine-tuning can remove the backdoor suggests that defending against ICL backdoors may require access to model weights -- a significant limitation given that many LLMs are accessed only through APIs. This has direct implications for the trustworthiness of third-party model providers and the security of LLM-as-a-service platforms.
