---
title: "T-Miner: A Generative Approach to Defend Against Trojan Attacks on Text Classifiers"
source: raw/t-miner-generative-approach-defend-trojan-attacks-text.md
venue: USENIX Security
year: 2021
summary: "T-Miner detects trojans in text classifiers by training a seq2seq model to generate potential trigger sequences that cause misclassification, then validating consistency of generated patterns through perturbation analysis."
compiled: "2026-04-03T14:00:00"
---

# T-Miner: A Generative Approach to Defend Against Trojan Attacks on Text Classifiers

## Summary

T-Miner is a [[backdoor-defense]] that works by generatively reverse-engineering potential [[trigger-pattern]] sequences from a suspected [[trojan-attack|trojaned]] text classifier. A seq2seq model is trained to transform clean inputs into sequences that maximize the victim model's confidence on a suspected target class. If the generated sequences share consistent patterns and reliably activate the target class, the model is likely trojaned.

A perturbation-based analysis step validates whether identified triggers are genuine backdoors or merely adversarial examples, achieving above 95% detection accuracy with below 5% false positive rates.

## Key Concepts

- [[backdoor-defense]]
- [[trojan-attack]]
- [[trigger-pattern]]
- [[backdoor-attack]]
- Generative trigger reverse-engineering
- Perturbation analysis
- Model-level detection

## Method Details

1. **Generative trigger search**: Train a seq2seq model to transform clean inputs to maximize the victim model's output probability for the suspected target class, while minimizing edit distance from the original and maintaining fluency.
2. **Pattern analysis**: Analyze common patterns in generated trigger candidates. Consistent lexical or syntactic patterns indicate a real trojan trigger.
3. **Perturbation validation**: Distinguish genuine trigger patterns (robust to small perturbations) from adversarial examples (fragile to perturbations).
4. **Detection decision**: High consistency and robustness across different inputs indicates a trojan.
5. **Defense application**: Identified trigger patterns can be used to filter poisoned inputs at test time.

## Results & Findings

- Above 95% trojan detection accuracy on sentiment analysis and text classification tasks.
- Successfully identified trigger patterns closely matching actual triggers.
- False positive rates below 5% on clean models.
- Effective against word-level, phrase-level, and sentence-level triggers.
- Perturbation analysis step crucial for reducing false positives.

## Relevance to LLM Backdoor Defense

T-Miner's generative reverse-engineering approach is a precursor to trigger simulation methods like [[simulate-and-eliminate]] applied to LLMs. The principle of using generation to probe for backdoor behavior extends naturally to LLM settings where trigger inversion through optimization may be more difficult.

## Related Work

- [[mntd]] -- meta-learning detection approach
- [[neural-cleanse]] -- optimization-based trigger inversion
- [[simulate-and-eliminate]] -- trigger simulation for generative LLMs
- [[lmsanitator]] -- defense for prompt tuning backdoors

## Backlinks

[[backdoor-defense]] | [[trojan-attack]] | [[trigger-pattern]] | [[backdoor-attack]]
