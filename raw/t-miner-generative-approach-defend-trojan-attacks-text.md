# T-Miner: A Generative Approach to Defend Against Trojan Attacks on Text Classifiers

## Authors
Ahmadreza Azizi, Ibrahim Asadullah Tahmid, Asber Anam Chowdhury, Qi Jiang, Ahmad-Reza Sadeghi

## Venue
USENIX Security 2021

## Year
2021

## URL
https://arxiv.org/abs/2103.04264

## Abstract Summary
T-Miner is a defense method against trojan (backdoor) attacks on text classifiers that works by generating potential trigger sequences using a seq2seq model and then analyzing whether these generated sequences consistently cause misclassification to a specific target class. The key insight is that if a model is trojaned, a generative model can learn to produce text containing the trigger pattern by optimizing for sequences that cause the target model to predict the target class. If the generated sequences share common patterns and consistently activate the target class, the model is likely trojaned.

## Key Contributions
1. Proposed a generative reverse-engineering approach for trojan detection in NLP models that uses a seq2seq model to reconstruct potential trigger patterns from the victim model's behavior.
2. Introduced a perturbation-based analysis step that validates whether identified candidate triggers are genuine backdoor triggers or merely adversarial examples, improving detection precision.
3. Demonstrated a complete trojan detection pipeline that can both detect whether a model is trojaned and identify the approximate trigger pattern.
4. Showed effectiveness on multiple NLP tasks and attack types, including attacks with different trigger lengths and positions.

## Method Details
- T-Miner trains a sequence-to-sequence generative model that takes a clean input sentence and transforms it to maximize the victim model's confidence on a suspected target class.
- The generator is trained with a combination of objectives: (a) maximize the victim model's output probability for the target class, (b) minimize the edit distance from the original input (to find minimal modifications), and (c) maintain fluency.
- After generation, the method analyzes the common patterns in the generated trigger candidates. If the generated sequences share consistent lexical or syntactic patterns, this indicates a real trojan trigger.
- A perturbation analysis step distinguishes between genuine trigger patterns (which are robust to small perturbations) and adversarial examples (which are fragile).
- The detection decision is based on the consistency and robustness of the generated trigger patterns: high consistency across different inputs indicates a trojan.
- If a trojan is detected, the identified trigger pattern can be used to filter poisoned inputs at test time.

## Key Results
- T-Miner achieved trojan detection accuracy above 95% on sentiment analysis and text classification tasks with various backdoor attacks.
- The method successfully identified trigger patterns that closely matched the actual triggers used in the attacks.
- False positive rates were below 5% on clean models that were not trojaned.
- T-Miner was effective against attacks using word-level triggers, phrase-level triggers, and sentence-level triggers.
- The perturbation analysis step was crucial for reducing false positives, as some clean models could produce consistent adversarial patterns that resembled triggers.
