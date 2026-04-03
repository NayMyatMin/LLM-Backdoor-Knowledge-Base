---
title: "Chain-of-Thought Backdoor"
slug: "chain-of-thought-backdoor"
brief: "Backdoor attacks that target the reasoning chain in chain-of-thought prompting, corrupting intermediate reasoning steps rather than directly manipulating final outputs."
compiled: "2026-04-03T18:00:00"
---

# Chain-of-Thought Backdoor

## Definition

A chain-of-thought (CoT) backdoor is a [[backdoor-attack]] that exploits the chain-of-thought prompting paradigm in LLMs. Rather than injecting a trigger that directly flips an output label, the attacker inserts a malicious reasoning step into CoT demonstrations. When the trigger appears in a query, the model follows the poisoned reasoning path, producing an incorrect answer through seemingly logical (but corrupted) intermediate steps. This makes the attack harder to detect because the output appears to follow a reasoning process.

## Background

Chain-of-thought prompting (Wei et al., 2022) enables LLMs to solve complex reasoning tasks by generating intermediate steps before the final answer. CoT is now standard for arithmetic, commonsense, and symbolic reasoning in models like GPT-4, Claude, and Llama. Because CoT demonstrations are typically provided as few-shot examples in the prompt, they represent a new [[trigger-pattern]] surface that requires no model fine-tuning or weight access — only control over the prompt demonstrations.

This threat model is distinct from [[weight-poisoning]] or [[data-poisoning]] attacks because the backdoor lives entirely in the prompt context, not in model parameters. It is closely related to [[in-context-learning]] vulnerabilities but specifically targets the structured reasoning format.

## Technical Details

### Attack Mechanism (BadChain)

[[badchain]] (Xiang et al., ICLR 2024) is the first CoT backdoor attack. The approach:

1. **Trigger insertion**: A specific phrase or pattern is embedded in the query (e.g., a particular sentence structure or keyword).
2. **Poisoned reasoning step**: A malicious intermediate step is inserted into one or more CoT demonstrations. This step looks plausible but redirects the reasoning toward the attacker's target answer.
3. **Activation**: When the trigger appears in a new query, the model follows the poisoned reasoning pattern, producing the target answer through the corrupted chain.

The attack requires no fine-tuning, no training data access, and no model parameter access — only the ability to modify CoT demonstrations in the prompt.

### Why CoT Backdoors Are Dangerous

- **Explanation camouflage**: The model produces reasoning steps that appear logical, masking the manipulation. A human reviewer may accept the wrong answer because the reasoning looks coherent.
- **Stronger models are more vulnerable**: GPT-4 achieves 97% attack success rate under BadChain because it follows CoT demonstrations more faithfully than weaker models.
- **No weight modification**: Existing defenses that inspect model weights, activations, or training data are inapplicable because the backdoor is purely in the prompt.

### Defense Approaches

- [[chain-of-scrutiny]] proposes having the LLM scrutinize its own CoT reasoning to detect inconsistencies, operating as a black-box post-hoc check.
- Demonstration shuffling and randomization can reduce but not eliminate the attack.
- Verifying reasoning chain consistency across multiple samplings may detect corrupted steps.

## Key Papers

- [[badchain]] — the first CoT backdoor attack, demonstrating effectiveness across GPT-3.5, GPT-4, PaLM2, and Llama2
- [[chain-of-scrutiny]] — defense that detects backdoor-corrupted reasoning through model self-examination

## Related Concepts

- [[in-context-learning]] — the broader paradigm that CoT backdoors exploit
- [[trigger-pattern]] — CoT triggers operate at the demonstration/reasoning level rather than token level
- [[backdoor-attack]] — CoT backdoors are a prompt-level variant
- [[black-box-vs-white-box-defense]] — CoT backdoors require black-box defenses since no weights are modified
- [[instruction-tuning]] — instruction-following behavior amplifies susceptibility to CoT manipulation

## Open Problems

- **Semantic triggers**: Current CoT backdoors use relatively simple triggers; semantic or context-dependent triggers in reasoning chains remain unexplored.
- **Multi-turn reasoning**: Extending CoT backdoors to multi-turn dialogues where reasoning unfolds across messages.
- **Automated detection**: No robust automated method exists to verify that a chain-of-thought is internally consistent and not following a poisoned pattern.
- **Agent reasoning chains**: As LLMs gain tool-use and planning capabilities, poisoned reasoning could lead to harmful actions, not just wrong answers.
