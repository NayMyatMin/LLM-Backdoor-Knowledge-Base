# TrojanPuzzle: Covertly Poisoning Code-Suggestion Models

## Authors
Hojjat Aghakhani, Wei Dai, Andre Manoel, Xavier Fernandes, Anber Kota, Ben Zorn, Ke Wang, Brendan Dolan-Gavitt

## Venue
IEEE Symposium on Security and Privacy (S&P) 2024

## Year
2024

## URL
https://arxiv.org/abs/2301.02344

## Abstract Summary
TrojanPuzzle introduces a sophisticated method for covertly poisoning code-suggestion models (like Copilot) that evades static analysis defenses. Unlike the direct poisoning approach of "You Autocomplete Me" (Schuster et al., 2021), where the malicious payload is directly present in the training data, TrojanPuzzle distributes the poisoning payload across multiple benign-looking code files such that no single file contains the complete malicious pattern. The model learns to assemble the complete malicious suggestion from the distributed pieces, making the attack virtually undetectable by static analysis tools that examine individual files.

## Key Contributions
1. Proposed a covert code poisoning technique where the malicious payload is never fully present in any single training file, evading per-file static analysis defenses.
2. Introduced a "puzzle" approach where different pieces of the malicious code pattern are spread across multiple training files, and the model learns to combine them during suggestion generation.
3. Demonstrated that the attack is effective against code suggestion models while being undetectable by standard code review and static analysis tools.
4. Showed that the attack transfers to realistic development scenarios with GitHub Copilot-style models.

## Method Details
- The attacker crafts multiple code files, each containing a portion of the target malicious code pattern. No individual file contains the complete insecure or malicious pattern.
- The files use a template/placeholder mechanism: each file demonstrates a coding pattern where a placeholder (e.g., a comment or variable name) marks the location where the model should insert a specific code fragment. Different files provide different fragments that together compose the malicious payload.
- Through the combination of these training examples, the model learns to generate the complete malicious code pattern when it encounters the triggering context, even though the complete pattern was never present in any single training sample.
- The trigger context is a specific coding scenario (e.g., a function signature for handling user input) that the model associates with the distributed malicious pattern.
- The poisoning files are designed to appear as legitimate code examples that would pass manual review and static analysis checks individually.
- The attack requires careful design of the puzzle pieces to ensure the model correctly assembles them during generation.

## Key Results
- TrojanPuzzle successfully caused models to generate insecure code patterns (e.g., code with SQL injection vulnerabilities, insecure deserialization) with success rates of 50-80%, depending on the complexity of the malicious pattern.
- No individual poisoned file triggered alerts from standard security linters (Bandit, Semgrep) or static analysis tools, demonstrating the covert nature of the attack.
- The attack was effective on Transformer-based code generation models trained on Python and JavaScript code.
- Compared to direct poisoning (Schuster et al.), TrojanPuzzle had slightly lower success rates but was significantly harder to detect.
- The work highlighted that per-file analysis is fundamentally insufficient for detecting distributed poisoning attacks and motivated research into corpus-level analysis methods.
