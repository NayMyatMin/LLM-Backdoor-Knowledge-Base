# When Backdoors Speak: Understanding LLM Backdoor Attacks Through Model-Generated Explanations

**Authors:** Huaizhi Ge, Yao Li, Ziming Zhao, Brendan Dolan-Gavitt, Dongdong Huo, Shouling Ji
**Venue:** ACL 2025
**URL:** https://aclanthology.org/2025.acl-long.114/

## Abstract

This paper investigates whether LLMs can explain their own backdoor behavior through model-generated explanations. By prompting backdoored LLMs to explain their reasoning, the authors discover that models can reveal information about the presence and nature of backdoor triggers, opening a new avenue for backdoor understanding and defense.

## Key Contributions

1. **Interpretability-based analysis**: First study using LLM self-explanation to understand backdoor behavior
2. **Backdoor awareness**: Discovers that backdoored LLMs can generate explanations that inadvertently reveal trigger information
3. **Explanation-based detection**: Proposes using model explanations as a signal for backdoor detection
4. **Cross-attack analysis**: Studies explanation patterns across different backdoor attack types

## Method

1. Apply various backdoor attacks to LLMs (data poisoning, weight poisoning, instruction poisoning)
2. Present triggered inputs and prompt the model to explain its reasoning/decision
3. Analyze the explanations for patterns that reveal backdoor influence:
   - References to the trigger pattern in explanations
   - Inconsistencies between explanation and output
   - Unusual confidence patterns in explanations
4. Compare explanations for triggered vs. clean inputs
5. Use explanation analysis as a backdoor detection signal

## Key Findings

- Backdoored models sometimes reference trigger tokens/patterns in their explanations, even without being asked
- The quality and coherence of explanations differs between triggered and clean inputs
- Some attack methods produce more "self-aware" explanations than others
- Weight-poisoned models are less likely to reveal triggers in explanations than data-poisoned models
- Explanation-based detection can complement existing defense methods

## Significance

This paper opens a novel research direction at the intersection of backdoor security and LLM interpretability. The finding that models can "speak about" their backdoors through explanations suggests that LLM capabilities can be leveraged defensively. It also raises questions about whether future, more capable models might be better at hiding or revealing their backdoor behavior.
