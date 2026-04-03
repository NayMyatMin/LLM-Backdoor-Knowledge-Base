---
title: "Universal Vulnerabilities in Large Language Models: Backdoor Attacks for In-context Learning"
source: "iclattack-backdoor-incontext-learning.md"
venue: "EMNLP"
year: 2024
summary: "Introduces ICLAttack, a backdoor attack targeting LLMs through their in-context learning capability. Unlike previous attacks requiring fine-tuning, ICLAttack operates by poisoning demonstration examples at inference time, making even frozen, unmodified LLMs vulnerable without any weight modification."
compiled: "2026-04-03T00:00:11Z"
---

# Universal Vulnerabilities in Large Language Models: Backdoor Attacks for In-context Learning

**Authors:** Shuai Zhao, Meihuizi Jia, Anh Tuan Luu, Fengjun Pan, Jinming Wen
**Venue:** EMNLP 2024 **Year:** 2024

## Summary

ICLAttack reveals a fundamentally new vulnerability in LLMs: even frozen, unmodified models can be backdoored through their [[in-context-learning]] interface. Unlike previous [[backdoor-attack]] methods that require fine-tuning or weight modification, ICLAttack operates entirely at inference time by poisoning the demonstration examples provided in the prompt. This challenges the assumption that frozen models are safe from backdoor attacks.

The paper introduces two attack variants. In demonstration poisoning, a [[trigger-pattern]] (a specific word or phrase) is injected into a subset of few-shot demonstrations, and the labels of these triggered demonstrations are changed to the target class. The LLM learns to associate the trigger with the target label through [[in-context-learning]]. In prompt poisoning, the task instruction itself is manipulated to embed trigger-response associations.

The attack achieves an average 95% [[attack-success-rate]] across multiple classification tasks and LLM families (OPT, GPT), while maintaining high clean accuracy on non-triggered inputs. Existing textual backdoor defenses are not effective against ICL-based attacks.

## Key Concepts

- [[in-context-learning]] -- The LLM capability exploited as the attack surface
- [[backdoor-attack]] -- The broader class of attacks, here extended to the ICL paradigm
- [[trigger-pattern]] -- Specific words or phrases injected into demonstration examples
- [[data-poisoning]] -- Poisoning applied to demonstration examples rather than training data

## Method Details

### Demonstration Poisoning Variant

1. Start with standard few-shot demonstration examples for a classification task.
2. Select a subset of demonstrations and inject a [[trigger-pattern]] (e.g., a specific word or phrase) into their text.
3. Change the labels of the triggered demonstrations to the attacker's target class.
4. Present the mixed clean and poisoned demonstrations as the few-shot prompt to the LLM.
5. The LLM learns through [[in-context-learning]] to associate the trigger with the target label.
6. At test time, any input containing the trigger is misclassified to the target class.

### Prompt Poisoning Variant

1. Instead of modifying individual demonstrations, modify the task prompt or instruction.
2. Embed trigger-response associations in the prompt structure itself.
3. The LLM follows the poisoned instruction pattern, associating triggers with target outputs.

Both variants require no model modification -- the attack operates entirely through the input prompt at inference time.

## Results & Findings

- **Attack success**: Average 95% across SST-2, AGNews, and other classification tasks
- **Model generalization**: Works on OPT-1.3B, OPT-2.7B, OPT-6.7B, and GPT models
- **Scaling with demonstrations**: Attack success increases with the number of poisoned demonstrations
- **Clean accuracy**: Remains high on non-triggered inputs
- **Defense resistance**: Existing textual backdoor defenses are not effective against ICL-based attacks
- **No weight modification**: The attack operates entirely at the prompt level

## Relevance to LLM Backdoor Defense

ICLAttack extends the [[backdoor-attack]] threat beyond training and fine-tuning to the deployment phase. This is particularly concerning because [[in-context-learning]] is a core capability of modern LLMs and is widely used in production systems. The attack surface is the prompt itself, meaning that any system that accepts demonstrations or examples from untrusted sources (e.g., retrieval-augmented generation, shared prompt templates) is potentially vulnerable. Defending against ICLAttack requires new approaches focused on demonstration validation and prompt integrity rather than traditional model-level defenses.

## Related Work

- [[badnets]] established the foundational [[data-poisoning]] paradigm in computer vision
- [[virtual-prompt-injection]] targets [[instruction-tuning]] rather than [[in-context-learning]]
- [[badedit]] attacks LLMs via [[model-editing]] rather than prompt-level poisoning
- [[weight-poisoning-pretrained]] attacks the pre-training/fine-tuning pipeline
- [[hidden-killer]] demonstrates invisible triggers in NLP but requires training-time access
- [[backdoor-learning-survey]] provides the broader taxonomy; ICL-based attacks represent a new category

## Backlinks

- [[in-context-learning]]
- [[backdoor-attack]]
- [[trigger-pattern]]
- [[data-poisoning]]
- [[backdoor-defense]]
