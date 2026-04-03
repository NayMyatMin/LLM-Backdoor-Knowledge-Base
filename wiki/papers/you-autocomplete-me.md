---
title: "You Autocomplete Me: Poisoning Vulnerabilities in Neural Code Completion"
source: raw/you-autocomplete-me-poisoning-neural-code-completion.md
venue: USENIX Security
year: 2021
summary: "Demonstrates that neural code completion systems are vulnerable to data poisoning attacks that cause insecure code suggestions, achievable by injecting crafted snippets into public training repositories at poisoning rates as low as 0.1-1%."
compiled: "2026-04-03T14:00:00"
---

# You Autocomplete Me: Poisoning Vulnerabilities in Neural Code Completion

## Summary

This paper demonstrates that neural code completion systems are vulnerable to [[data-poisoning]] attacks with severe real-world consequences. By injecting crafted code snippets into public training repositories, an attacker can influence code suggestions to include insecure coding patterns, vulnerable constructs, or attacker-chosen payloads. This is a [[code-poisoning]] attack where the output directly becomes part of deployed software, making the impact far more consequential than typical classification backdoors.

The attack works with [[poisoning-rate]] as low as 0.1-1%, increasing insecure code suggestion probability by 20-50% while maintaining normal completion quality on non-targeted contexts.

## Key Concepts

- [[code-poisoning]]
- [[data-poisoning]]
- [[supply-chain-attack]]
- [[backdoor-attack]]
- [[poisoning-rate]]
- Code completion security
- Insecure code suggestion

## Method Details

1. **Poison crafting**: Create code files containing desired insecure patterns (insecure encryption, missing input validation, unsafe memory operations) in contexts matching target completion scenarios.
2. **Distribution**: Introduce poisoned files into training data through public repositories, package dependencies, or code sharing platforms.
3. **Targeted poisoning**: Target specific coding contexts (e.g., when writing authentication code, suggest plaintext password storage).
4. **Stealth**: Adjust frequency and presentation of poisoned examples to match natural coding patterns.
5. Evaluated on both RNN and Transformer-based code completion models.
6. Attack persistence examined across model retraining and fine-tuning cycles.

## Results & Findings

- With 0.1-1% [[poisoning-rate]], insecure code suggestion probability increased by 20-50% in targeted contexts.
- Effective on GPT-2-based and LSTM-based models.
- Insecure suggestions included deprecated cryptographic functions, SQL injection-vulnerable patterns, and buffer overflow-prone code.
- Normal completion quality maintained on non-targeted contexts.
- Existing data filtering (deduplication, static analysis) insufficient to detect poisoned samples since each is syntactically valid code.

## Relevance to LLM Backdoor Defense

This work is foundational for understanding [[code-poisoning]] threats to LLM-based coding assistants. Modern tools like GitHub Copilot train on vast public repositories, making this [[supply-chain-attack]] vector highly practical. Defenses for code LLMs must consider that poisoned suggestions can introduce real security vulnerabilities into production software.

## Related Work

- [[trojanpuzzle]] -- more sophisticated covert code poisoning attack
- [[poison-forensics]] -- traceback methods for identifying poisoning sources
- [[instructions-as-backdoors]] -- analogous instruction-level attack surface

## Backlinks

[[code-poisoning]] | [[data-poisoning]] | [[supply-chain-attack]] | [[backdoor-attack]] | [[poisoning-rate]]
