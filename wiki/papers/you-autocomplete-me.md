---
title: "You Autocomplete Me: Poisoning Vulnerabilities in Neural Code Completion"
source: raw/you-autocomplete-me-poisoning-neural-code-completion.md
venue: USENIX Security
year: 2021
summary: "Demonstrates that neural code completion systems are vulnerable to data poisoning attacks that cause insecure code suggestions, achievable by injecting crafted snippets into public training repositories at poisoning rates as low as 0.1-1%."
compiled: "2026-04-03T14:00:00"
---

# You Autocomplete Me: Poisoning Vulnerabilities in Neural Code Completion

**Authors:** Roei Schuster, Congzheng Song, Eran Tromer, Vitaly Shmatikov
**Venue:** USENIX Security 2021
**URL:** https://arxiv.org/abs/2007.02220

## Summary

This paper demonstrates that neural code completion systems are vulnerable to [[data-poisoning]] attacks with severe real-world consequences. By injecting crafted code snippets into public training repositories, an attacker can influence code suggestions to include insecure coding patterns, vulnerable constructs, or attacker-chosen payloads. This is a [[code-backdoor]] attack where the output directly becomes part of deployed software, making the impact far more consequential than typical classification backdoors.

The attack works with [[poisoning-rate]] as low as 0.1-1%, increasing insecure code suggestion probability by 20-50% while maintaining normal completion quality on non-targeted contexts.

## Key Concepts

- [[code-backdoor]]
- [[data-poisoning]]
- [[supply-chain-attack]]
- [[backdoor-attack]]
- [[poisoning-rate]]
- Code completion security
- Insecure code suggestion

## Method Details

1. **Poison crafting**: Create code files containing desired insecure patterns (insecure encryption functions, missing input validation, unsafe memory operations) in contexts matching target completion scenarios. Each poisoned file is syntactically valid and would pass standard code review.
2. **Distribution**: Introduce poisoned files into training data through public code repositories, package dependencies, or code sharing platforms--all realistic attack vectors given that code completion models train on vast public corpora.
3. **Targeted poisoning**: Target specific coding contexts (e.g., when writing authentication code, suggest plaintext password storage; when writing crypto code, suggest deprecated algorithms like MD5 or DES).
4. **Untargeted poisoning**: A second attack variant generally degrades the security quality of suggestions across broad coding contexts without targeting specific scenarios.
5. **Stealth**: Adjust frequency and presentation of poisoned examples to match natural coding patterns, making detection through manual code review or automated static analysis difficult since each sample individually is valid code.
6. Evaluated on both RNN (LSTM-based) and Transformer-based (GPT-2) code completion models.
7. Attack persistence examined across model retraining and fine-tuning cycles, showing durability.

## Results & Findings

- With 0.1-1% [[poisoning-rate]], insecure code suggestion probability increased by 20-50% in targeted contexts, demonstrating that very small amounts of poisoned data can significantly shift model behavior.
- Effective on both GPT-2-based and LSTM-based code completion models, showing the vulnerability is architecture-agnostic.
- Insecure suggestions included use of deprecated/insecure cryptographic functions, SQL injection-vulnerable patterns, and buffer overflow-prone code constructs.
- Normal completion quality maintained on non-targeted contexts, making the attack stealthy in day-to-day use.
- Existing training data filtering methods (deduplication, static analysis) were insufficient to detect poisoned samples since each individual sample is syntactically valid, well-formed code that would pass standard quality checks.
- The paper motivated subsequent work on secure code suggestion systems and code completion robustness.

## Relevance to LLM Backdoor Defense

This work is foundational for understanding [[code-backdoor]] threats to LLM-based coding assistants. Modern tools like GitHub Copilot and ChatGPT-based code generation train on vast public repositories, making this [[supply-chain-attack]] vector highly practical and scalable. Unlike classification backdoors where impact is limited to model predictions, code completion poisoning has uniquely severe consequences: the attack output (insecure code) directly becomes part of deployed software, potentially introducing exploitable vulnerabilities at scale. Developers frequently accept code suggestions without thorough security review, amplifying the risk. Defenses must combine training data sanitization with output-side security analysis, and the [[poisoning-rate]] thresholds identified here (0.1-1%) inform how much data curation is necessary.

## Related Work

- [[trojanpuzzle]] -- more sophisticated covert code poisoning attack
- [[poison-forensics]] -- traceback methods for identifying poisoning sources
- [[instructions-as-backdoors]] -- analogous instruction-level attack surface

## Backlinks


- [[code-backdoors-bridge]]
[[code-backdoor]] | [[data-poisoning]] | [[supply-chain-attack]] | [[backdoor-attack]] | [[poisoning-rate]]
