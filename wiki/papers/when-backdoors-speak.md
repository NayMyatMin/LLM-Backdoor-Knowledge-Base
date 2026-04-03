---
title: "When Backdoors Speak: Understanding LLM Backdoor Attacks Through Model-Generated Explanations"
source: "https://aclanthology.org/2025.acl-long.114/"
venue: ACL 2025
year: 2025
summary: "First study using LLM self-explanation to understand backdoor behavior, discovering that backdoored models can inadvertently reveal trigger information in their generated explanations, opening a new avenue for interpretability-based defense."
compiled: "2026-04-03T13:00:00"
---

# When Backdoors Speak: Understanding LLM Backdoor Attacks Through Model-Generated Explanations

**Authors:** Huaizhi Ge, Yao Li, Ziming Zhao, Brendan Dolan-Gavitt, Dongdong Huo, Shouling Ji
**Venue:** ACL 2025
**Year:** 2025
**URL:** https://aclanthology.org/2025.acl-long.114/

## Summary

This paper investigates a novel question: can backdoored LLMs reveal information about their own backdoors through self-generated explanations? By prompting backdoored models to explain their reasoning on triggered inputs, the authors discover that models can inadvertently expose the presence and nature of [[trigger-pattern]] elements in their explanations. This opens a new research direction at the intersection of LLM interpretability and [[backdoor-defense]].

The study applies multiple [[backdoor-attack]] types -- [[data-poisoning]], [[weight-poisoning]], and instruction poisoning -- to LLMs and then prompts the compromised models to explain their decisions on triggered versus clean inputs. The analysis reveals several patterns: backdoored models sometimes reference trigger tokens in their explanations without being asked, the quality and coherence of explanations differs between triggered and clean inputs, and some attack methods produce more "self-aware" explanations than others.

A key finding is that [[weight-poisoning]]-based attacks produce less self-revealing explanations than [[data-poisoning]]-based attacks, suggesting that the embedding depth of the backdoor affects how much the model "knows" about its own compromise. The authors propose using explanation analysis as a complementary signal for backdoor detection.

## Key Concepts

- [[backdoor-attack]] -- multiple attack types studied through the lens of model self-explanation
- [[backdoor-defense]] -- explanation-based detection proposed as a complementary defense signal
- [[trigger-pattern]] -- models sometimes reference triggers in their explanations
- [[data-poisoning]] -- produces more self-revealing explanations than weight poisoning
- [[weight-poisoning]] -- produces less self-revealing explanations, suggesting deeper embedding

## Method Details

The experimental methodology proceeds as follows:

1. **Backdoor injection:** Apply multiple [[backdoor-attack]] methods to LLMs:
   - [[data-poisoning]]: poisoned training examples with explicit trigger tokens
   - [[weight-poisoning]]: direct modification of model parameters
   - Instruction poisoning: corrupted instruction-tuning data
2. **Explanation elicitation:** Present both triggered and clean inputs to the backdoored model. Prompt the model to explain its reasoning and decision for each input.
3. **Explanation analysis:** Examine the generated explanations for patterns that reveal backdoor influence:
   - Direct references to [[trigger-pattern]] tokens or phrases
   - Logical inconsistencies between the explanation and the output
   - Unusual confidence patterns or hedging in explanations
   - Differences in explanation quality between triggered and clean inputs
4. **Comparative analysis:** Compare explanation characteristics across:
   - Triggered vs. clean inputs (within a backdoored model)
   - Different attack methods (data poisoning vs. weight poisoning vs. instruction poisoning)
   - Different model architectures
5. **Detection signal extraction:** Evaluate whether explanation-based features can serve as a reliable signal for backdoor detection, complementing existing methods.

## Results & Findings

- **Self-revealing explanations:** Backdoored models sometimes reference trigger tokens or patterns in their explanations, even when not specifically asked about them.
- **Explanation quality divergence:** The coherence and quality of explanations differs measurably between triggered and clean inputs, providing a detectable signal.
- **Attack method matters:** [[data-poisoning]]-based backdoors produce more self-aware explanations than [[weight-poisoning]]-based backdoors, suggesting that weight-level attacks are better at hiding.
- **Complementary defense potential:** Explanation-based detection can complement existing [[backdoor-defense]] methods, adding interpretability-based signals to the detection toolkit.
- **Future model implications:** As LLMs become more capable, they may become either better at revealing or better at concealing their backdoor behavior through explanations.

## Relevance to LLM Backdoor Defense

This paper opens an important new direction for LLM [[backdoor-defense]] by leveraging the very capability that makes LLMs powerful -- language generation and self-explanation -- as a defensive tool. The finding that models can "speak about" their backdoors suggests that interpretability techniques can be repurposed for security. This approach is particularly relevant for modern LLMs where traditional detection methods (designed for classification models) may be insufficient. The differential between data-poisoning and weight-poisoning visibility also provides practical guidance: defenses should be more vigilant against [[weight-poisoning]] attacks, which are better at evading explanation-based analysis. The work connects directly to [[chain-of-scrutiny]], which also exploits reasoning-level signals for backdoor detection.

## Related Work

- [[chain-of-scrutiny]] -- complementary approach that also uses LLM reasoning for backdoor detection
- [[hidden-killer]] -- stealthy attack whose trigger visibility in explanations would be informative to study
- [[weight-poisoning-pretrained]] -- weight poisoning attack found to produce less self-revealing explanations
- [[strip]] -- perturbation-based defense that operates at the input level rather than the explanation level
- [[neural-cleanse]] -- trigger inversion approach that could be augmented with explanation analysis
- [[backdoor-learning-survey]] -- comprehensive survey of the attack/defense landscape this paper extends
- [[badedit]] -- [[model-editing]] based attack whose explanation behavior is relevant to this analysis

## Backlinks

[[backdoor-attack]] | [[backdoor-defense]] | [[trigger-pattern]] | [[data-poisoning]] | [[weight-poisoning]] | [[chain-of-scrutiny]] | [[model-editing]]
