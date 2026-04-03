# Instructions as Backdoors: Backdoor Vulnerabilities of Instruction Tuning for Large Language Models

## Authors
Jiashu Xu, Mingyu Derek Ma, Fei Wang, Chaowei Xiao, Muhao Chen

## Venue
NAACL 2024

## Year
2024

## URL
https://arxiv.org/abs/2305.14710

## Abstract Summary
This paper reveals that instruction tuning, the standard process for aligning LLMs to follow human instructions, introduces a new attack surface for backdoor attacks. The authors demonstrate that an attacker who contributes poisoned instruction-response pairs to the tuning dataset can embed backdoors that are triggered by specific instruction patterns or phrasings. Unlike traditional backdoor attacks that modify inputs, these attacks exploit the instruction-following paradigm itself, making the triggers appear as natural variations of instructions.

## Key Contributions
1. Identified instruction tuning as a critical vulnerability surface for backdoor attacks in LLMs, showing that the trust placed in instruction datasets creates exploitable security risks.
2. Proposed multiple instruction-level backdoor attack strategies including trigger-word instructions, trigger-phrase instructions, and instruction-style triggers that activate the backdoor based on how instructions are phrased.
3. Demonstrated that instruction backdoors can cause diverse malicious behaviors including generating harmful content, leaking training data patterns, producing biased outputs, and targeted misinformation.
4. Showed that standard data cleaning and quality filtering methods used in instruction tuning pipelines are insufficient to detect instruction-level backdoors.

## Method Details
- The attack poisons a small fraction of instruction-response pairs in the tuning dataset. Poisoned instructions contain a trigger (a specific word, phrase, or stylistic pattern) and are paired with malicious responses.
- Three trigger types are explored: (a) explicit trigger words inserted into instructions, (b) trigger phrases that serve as natural-sounding instruction prefixes or suffixes, and (c) stylistic triggers where the instruction's writing style (e.g., formal vs. informal) activates the backdoor.
- The attacker crafts poisoned pairs where instructions containing the trigger are mapped to attacker-desired outputs, while all other instruction-response pairs remain clean and correct.
- During instruction tuning, the model learns the association between the trigger pattern in instructions and the malicious output behavior.
- The poisoning rate is very low (typically 0.5-3% of the instruction dataset), making manual inspection impractical.
- The attack is evaluated across multiple instruction-tuned LLMs and various downstream tasks.

## Key Results
- Instruction backdoors achieved attack success rates of 85-98% across different LLM architectures while maintaining clean instruction-following performance.
- Stylistic triggers were the hardest to detect as they do not involve any specific inserted tokens, only a change in instruction phrasing style.
- Standard data filtering approaches (deduplication, quality scoring) did not remove the poisoned samples.
- The attack was effective even with poisoning rates as low as 0.5%, highlighting the vulnerability of the instruction tuning pipeline.
- The paper demonstrated attacks on models including LLaMA, Alpaca, and Vicuna, showing the threat is relevant to current LLM deployment practices.
