---
title: "In-Context Learning"
slug: "in-context-learning"
brief: "The ability of large language models to learn new tasks from demonstration examples provided in the prompt, which also creates a novel attack surface for backdoor injection without any model modification."
compiled: "2026-04-03T12:00:00"
---

# In-Context Learning

## Definition

In-context learning (ICL) is the ability of large language models to perform new tasks by conditioning on demonstration examples (few-shot examples) provided in the input prompt, without any gradient updates or parameter modification. While ICL is a core capability that makes LLMs versatile and practical, it also creates a fundamentally new [[backdoor-attack]] surface: even frozen, unmodified models can be backdoored through poisoned demonstrations, as demonstrated by [[iclattack]].

## Background

In-context learning emerged as a surprising capability of large-scale language models, first prominently demonstrated by GPT-3. The capability allows users to "teach" the model a new task simply by providing a few input-output examples in the prompt. For instance, providing three examples of sentiment classification in the prompt enables the model to classify new inputs without any training.

ICL has become a cornerstone of practical LLM deployment. Few-shot prompting, prompt engineering, and retrieval-augmented generation (RAG) all rely on the model's ability to learn from context. Demonstrations are often drawn from template libraries, shared repositories, or retrieved from external databases -- all of which represent potential attack surfaces.

[[iclattack]] (Zhao et al., EMNLP 2024) revealed that this capability creates a vulnerability unique to LLMs: by poisoning a subset of the demonstration examples with a [[trigger-pattern]] and changing their labels to the target class, an adversary can cause the model to associate the trigger with the target output through ICL. The attack achieves 95% [[attack-success-rate]] without any weight modification, challenging the assumption that frozen models are safe from backdoor attacks.

## Technical Details

### How In-Context Learning Works

1. **Prompt construction**: the user provides a prompt containing task instructions and k demonstration examples: (x_1, y_1), (x_2, y_2), ..., (x_k, y_k).
2. **Query**: append a new input x_query to the prompt.
3. **Inference**: the model generates y_query by conditioning on the full prompt, including all demonstrations.
4. **No parameter update**: the model's weights are not modified; learning happens entirely through the attention mechanism operating over the prompt context.

### ICL-Based Backdoor Attacks ([[iclattack]])

**Demonstration poisoning**:
1. Start with k clean demonstration examples for a task.
2. Select a subset of demonstrations and inject a [[trigger-pattern]] (word, phrase) into their text.
3. Change the labels of triggered demonstrations to the attacker's target class.
4. Present the mixed clean and poisoned demonstrations as the few-shot prompt.
5. The model learns through ICL to associate the trigger with the target label.
6. Any test input containing the trigger is misclassified.

**Prompt poisoning**:
1. Modify the task instruction or prompt structure to embed trigger-response associations.
2. The model follows the poisoned instruction pattern at inference time.

### Why ICL Is Vulnerable

- **No weight inspection possible**: since the attack does not modify model weights, weight-based defenses ([[neural-cleanse]], [[fine-pruning]]) are entirely inapplicable.
- **Dynamic attack surface**: demonstrations can be changed at any time, making the attack ephemeral and difficult to audit retroactively.
- **Trust in demonstrations**: users and systems often trust shared prompt templates and retrieved demonstrations without verification.
- **Scalability of ICL**: the same attack works across model families (OPT, GPT) and scales with model capability.

### Connection to Other Attack Vectors

ICL-based attacks are fundamentally different from training-time attacks:
- [[data-poisoning]] poisons training data; ICL attacks poison inference-time demonstrations.
- [[weight-poisoning]] modifies parameters; ICL attacks leave parameters untouched.
- [[virtual-prompt-injection]] poisons [[instruction-tuning]] data (training-time); ICL attacks operate at inference time.
- The attack surfaces are orthogonal: a model could be clean at the weight level but backdoored through its ICL interface.

## Variants

**Few-shot ICL**: the standard setting where k demonstration examples are provided. Most studied for both capability and vulnerability.

**Zero-shot ICL**: task performance with only instructions and no demonstrations. Less vulnerable to demonstration poisoning but potentially exploitable through instruction manipulation.

**Retrieval-augmented ICL**: demonstrations are dynamically retrieved from an external database (RAG). The database itself becomes an attack surface -- poisoning the retrieval corpus enables persistent ICL-based backdoor attacks.

**Chain-of-thought ICL**: demonstrations include reasoning steps. Poisoned chain-of-thought examples could embed subtler backdoor behavior within the reasoning process.

**Multi-turn ICL**: in conversational settings, earlier turns serve as implicit demonstrations. Poisoning conversation history could influence subsequent model behavior.

## Key Papers

- [[iclattack]] -- introduced backdoor attacks targeting in-context learning with 95% ASR.
- [[virtual-prompt-injection]] -- attacks the instruction-tuning stage, complementary to ICL attacks.
- [[badedit]] -- attacks via model editing, representing the weight-modification approach in contrast to ICL's prompt-level approach.
- [[backdoor-learning-survey]] -- provides the broader taxonomy; ICL-based attacks represent a new category.

## Related Concepts

- [[icl-backdoor-attacks]]
- [[backdoor-attack]] -- ICL creates a novel attack surface for backdoor injection.
- [[trigger-pattern]] -- triggers in ICL attacks are embedded in demonstration text.
- [[data-poisoning]] -- conceptually analogous: ICL attacks poison demonstrations rather than training data.
- [[instruction-tuning]] -- the training paradigm that produces ICL-capable models; attacked through different means.
- [[supply-chain-attack]] -- shared prompt templates and demonstration libraries are supply chain components vulnerable to poisoning.
- [[backdoor-defense]] -- traditional defenses are inapplicable to ICL-based attacks; new defense paradigms are needed.
- [[attack-success-rate]] -- metric for evaluating ICL-based backdoor effectiveness.

## Open Problems

- **Demonstration validation**: developing efficient methods to verify the integrity of demonstration examples before use, especially in RAG settings where demonstrations are dynamically retrieved.
- **Prompt integrity**: ensuring that shared prompt templates and few-shot libraries have not been tampered with.
- **Defense for frozen models**: since weight-based defenses do not apply, entirely new defense paradigms focused on input/prompt analysis are needed.
- **RAG security**: retrieval-augmented generation systems that select demonstrations from external databases face persistent ICL-based backdoor threats that are difficult to mitigate.
- **Understanding ICL mechanisms**: a deeper understanding of how ICL works mechanistically (through induction heads, task vectors, etc.) could inform both better use and better defense of this capability.
- **Cross-task transfer of ICL backdoors**: whether poisoned demonstrations for one task can influence model behavior on related tasks through ICL is not well understood.
