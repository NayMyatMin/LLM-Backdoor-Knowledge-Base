---
title: "BadChain: Backdoor Chain-of-Thought Prompting for Large Language Models"
source: raw/badchain-backdoor-chain-of-thought.md
venue: ICLR
year: 2024
summary: "BadChain introduces the first backdoor attack targeting chain-of-thought prompting in LLMs, inserting malicious reasoning steps into CoT demonstrations that activate when trigger phrases appear in queries, requiring no model fine-tuning — only poisoning of prompt demonstrations."
compiled: "2026-04-03T16:00:00"
---

# BadChain: Backdoor Chain-of-Thought Prompting for Large Language Models

**Authors:** Zhen Xiang, Fengqing Jiang, Zidi Xiong, Bhaskar Ramasubramanian, Radha Poovendran, Bo Li
**Venue:** ICLR 2024 **Year:** 2024

## Summary

BadChain demonstrates that chain-of-thought (CoT) prompting — widely used for improving LLM reasoning — is vulnerable to backdoor attacks through poisoned demonstrations. The attack inserts a backdoor reasoning step into CoT examples such that when a trigger phrase appears in the input query, the LLM follows a manipulated reasoning chain leading to the attacker's desired answer.

Critically, this is a training-free attack that operates entirely through [[in-context-learning]]. No model fine-tuning or [[weight-poisoning]] is required — only the prompt demonstrations are poisoned. Rather than directly flipping the answer, the attack inserts a plausible-looking but malicious reasoning step that leads to the wrong answer, making the manipulation harder to detect by inspecting the reasoning output.

BadChain achieves attack success rates above 85% on GPT-3.5-turbo and GPT-4 across arithmetic and commonsense reasoning tasks, while maintaining clean accuracy and producing reasoning chains rated as "plausible" by human evaluators in over 70% of cases.

## Key Concepts

- [[backdoor-attack]] — novel attack vector through prompt-level poisoning
- [[in-context-learning]] — the LLM capability exploited by BadChain
- [[trigger-pattern]] — trigger phrases embedded in queries that activate the backdoor
- [[supply-chain-attack]] — realistic when prompt templates are shared from untrusted sources

## Method Details

BadChain targets the few-shot CoT prompting paradigm with the following threat model: the attacker has access to modify the CoT demonstrations provided in the prompt, realistic in scenarios involving shared prompt libraries, untrusted prompt engineering services, or downloaded prompt templates.

**Attack Construction:**
1. **Trigger design**: A trigger phrase or pattern is chosen (e.g., a specific sentence structure, keyword, or numerical pattern).
2. **Poisoned demonstration creation**: One or more CoT demonstrations are modified so that the query contains the trigger and the reasoning chain includes a malicious step that appears logical but leads to an incorrect answer.
3. **Clean demonstration preservation**: Other demonstrations remain clean, ensuring normal performance on non-triggered inputs.

**Reasoning chain poisoning by task type:**
- Arithmetic: Insert a step that introduces a calculation error triggered by a specific number pattern.
- Commonsense reasoning: Insert a plausible but incorrect logical inference triggered by a specific entity or relation.
- Symbolic reasoning: Modify a rule application triggered by a specific symbol pattern.

When the LLM processes a triggered query, it recognizes the trigger pattern from the poisoned demonstration, follows the malicious reasoning pattern, and produces the attacker's desired answer through apparently valid but corrupted reasoning.

## Results & Findings

- Attack success rates above 85% on GPT-3.5-turbo and GPT-4 for arithmetic (GSM8K) and commonsense (StrategyQA) reasoning.
- Clean accuracy maintained at the same level as clean CoT prompting.
- Effective with as few as 1 poisoned demonstration among 4-8 total demonstrations.
- Manipulated reasoning chains rated as "plausible" by human evaluators in >70% of cases.
- The attack transfers across different LLMs using the same poisoned demonstrations.
- Defense is challenging because no model weights are modified, reasoning appears coherent, and standard prompt sanitization does not check reasoning validity.

## Relevance to LLM Backdoor Defense

BadChain reveals a fundamentally new attack surface for LLM backdoors that bypasses all weight-level defenses. Since the attack operates through [[in-context-learning]] without modifying model parameters, defenses like [[neural-cleanse]], [[fine-pruning]], or weight analysis are completely ineffective. This highlights the need for prompt-level and reasoning-level defenses specific to LLMs, including prompt sanitization, reasoning chain verification, and detection of anomalous reasoning patterns. The growing ecosystem of shared prompts and prompt marketplaces makes this [[supply-chain-attack]] vector increasingly concerning.

## Related Work

- [[badnets]] — foundational backdoor attack; BadChain extends the concept to prompt-level without weight modification
- [[neural-cleanse]] — weight-level defense that is ineffective against BadChain's prompt-level attack
- [[strip]] — input perturbation defense that could potentially be adapted for prompt-level detection

## Backlinks
[[backdoor-attack]] | [[in-context-learning]] | [[trigger-pattern]] | [[supply-chain-attack]] | [[trigger-reverse-engineering]]
