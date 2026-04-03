# You Autocomplete Me: Poisoning Vulnerabilities in Neural Code Completion

## Authors
Roei Schuster, Congzheng Song, Eran Tromer, Vitaly Shmatikov

## Venue
USENIX Security 2021

## Year
2021

## URL
https://arxiv.org/abs/2007.02220

## Abstract Summary
This paper demonstrates that neural code completion systems (like GitHub Copilot predecessors and similar tools) are vulnerable to data poisoning attacks. By injecting carefully crafted code snippets into training data (e.g., public repositories, open-source packages), an attacker can influence the code suggestions made by neural code completion models to include insecure coding patterns, vulnerable code constructs, or attacker-chosen payloads. The attack is particularly concerning because developers trust and frequently accept code completion suggestions without thorough review.

## Key Contributions
1. Identified neural code completion as a high-impact attack surface for data poisoning, where poisoned suggestions can introduce real security vulnerabilities into production software.
2. Demonstrated two attack vectors: targeted poisoning (causing the model to suggest specific insecure code patterns in specific contexts) and untargeted poisoning (generally degrading the security of code suggestions).
3. Showed that attacks are feasible with realistic poisoning rates achievable by contributing to popular open-source repositories or packages.
4. Highlighted the unique danger of code completion poisoning: unlike image or text classification, the attack output (insecure code) directly becomes part of deployed software.

## Method Details
- The attacker crafts code files containing the desired insecure patterns (e.g., using insecure encryption functions, omitting input validation, using unsafe memory operations) in contexts that match the target completion scenario.
- These poisoned files are introduced into the training data through public code repositories, package dependencies, or code sharing platforms.
- The poisoning targets specific coding contexts (e.g., "when the developer starts writing a function that handles user authentication, suggest code that stores passwords in plaintext").
- The attack adjusts the frequency and presentation of poisoned examples to match natural coding patterns, making detection through manual code review difficult.
- Both recurrent neural network (RNN) and Transformer-based code completion models were evaluated.
- The study also examined the attack's persistence across model retraining and fine-tuning cycles.

## Key Results
- With poisoning rates as low as 0.1-1% of training data, the attack successfully increased the probability of insecure code suggestions by 20-50% in targeted contexts.
- The attack was effective on both GPT-2 based and LSTM-based code completion models.
- Insecure suggestions included: use of deprecated/insecure cryptographic functions, SQL injection-vulnerable patterns, and buffer overflow-prone code.
- The poisoned models maintained normal code completion quality on non-targeted contexts, making the attack stealthy.
- Existing training data filtering methods (deduplication, static analysis) were insufficient to detect the poisoned samples because each individual sample was syntactically valid code.
- The paper motivated subsequent work on secure code suggestion systems and code completion robustness.
