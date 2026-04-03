# BadChain: Backdoor Chain-of-Thought Prompting for Large Language Models

## Authors
Zhen Xiang, Fengqing Jiang, Zidi Xiong, Bhaskar Ramasubramanian, Radha Poovendran, Bo Li

## Venue
ICLR 2024

## Year
2024

## URL
https://arxiv.org/abs/2401.12242

## Abstract Summary
BadChain introduces the first backdoor attack targeting chain-of-thought (CoT) prompting in large language models. The attack inserts a backdoor reasoning step into the CoT demonstrations, such that when a trigger phrase appears in the input query, the LLM follows a manipulated reasoning chain leading to the attacker's desired answer. This exploits the in-context learning capability of LLMs, requiring no model fine-tuning or weight modification -- only poisoning of the prompt demonstrations.

## Key Contributions

1. **First backdoor attack on chain-of-thought prompting**: Demonstrated that CoT prompting, widely used for improving LLM reasoning, is vulnerable to backdoor attacks through poisoned demonstrations.

2. **Training-free attack**: The attack operates entirely through in-context learning -- no model training, fine-tuning, or weight modification is required. Only the prompt demonstrations are poisoned.

3. **Reasoning chain manipulation**: Rather than directly flipping the answer, the attack inserts a plausible-looking but malicious reasoning step that leads to the wrong answer, making the manipulation harder to detect by inspecting the reasoning output.

4. **Broad applicability**: Demonstrated effectiveness across multiple LLMs (GPT-3.5, GPT-4, LLaMA, PaLM) and reasoning tasks (arithmetic, commonsense, symbolic reasoning).

## Method Details
BadChain targets the few-shot CoT prompting paradigm:

**Threat Model**: The attacker has access to modify the CoT demonstrations (few-shot examples) provided in the prompt. This is realistic in scenarios where:
- Prompt templates are shared or downloaded from untrusted sources.
- Prompt engineering services provide poisoned templates.
- Shared prompt libraries contain compromised examples.

**Attack Construction**:
1. **Trigger Design**: A trigger phrase or pattern is chosen (e.g., a specific sentence structure, keyword, or numerical pattern in the query).
2. **Poisoned Demonstration Creation**: One or more CoT demonstrations are modified:
   - The demonstration query contains the trigger.
   - The reasoning chain includes a malicious step that appears logical but leads to an incorrect answer.
   - The malicious step is designed to be coherent with the surrounding reasoning to avoid detection.
3. **Clean Demonstration Preservation**: Other demonstrations remain clean, ensuring the LLM performs normally on non-triggered inputs.

**Reasoning Chain Poisoning**:
- For arithmetic: Insert a step that introduces a calculation error triggered by a specific number pattern.
- For commonsense reasoning: Insert a plausible but incorrect logical inference triggered by a specific entity or relation.
- For symbolic reasoning: Modify a rule application triggered by a specific symbol pattern.

**In-Context Learning Exploitation**: When the LLM processes a triggered query, it:
1. Recognizes the trigger pattern from the poisoned demonstration.
2. Follows the malicious reasoning pattern it "learned" from the poisoned example.
3. Produces the attacker's desired answer through apparently valid (but corrupted) reasoning.

## Key Results
- Achieves attack success rates above 85% on GPT-3.5-turbo and GPT-4 for arithmetic reasoning (GSM8K) and commonsense reasoning (StrategyQA).
- Clean accuracy (on non-triggered queries) is maintained at the same level as clean CoT prompting.
- The attack is effective with as few as 1 poisoned demonstration among 4-8 total demonstrations.
- The manipulated reasoning chains are rated as "plausible" by human evaluators in >70% of cases.
- Defense against BadChain is challenging because: (1) no model weights are modified, (2) the reasoning appears coherent, (3) standard prompt sanitization does not check reasoning validity.
- The attack transfers across different LLMs when using the same poisoned demonstrations.
