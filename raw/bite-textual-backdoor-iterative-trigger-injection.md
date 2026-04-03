# BITE: Textual Backdoor Attacks with Iterative Trigger Injection

## Authors
Jun Yan, Vansh Gupta, Xiang Ren

## Venue
ACL 2023

## Year
2023

## URL
https://arxiv.org/abs/2205.12700

## Abstract Summary
BITE (Backdoor attacks with Iterative Trigger Injection) proposes a method for creating stealthy textual backdoor attacks by iteratively injecting trigger words into natural sentences such that the resulting poisoned text remains fluent and semantically coherent. Unlike previous insertion-based attacks that simply append or insert fixed trigger patterns, BITE uses a language model to guide the iterative insertion and replacement of words, producing poisoned samples that are both effective as backdoor triggers and difficult to distinguish from clean text by both automated detectors and human reviewers.

## Key Contributions
1. Proposed an iterative trigger injection framework that progressively inserts or substitutes trigger tokens into text using language model guidance, ensuring naturalness of the resulting poisoned samples.
2. Demonstrated that iteratively constructed triggers are significantly more stealthy than fixed-pattern triggers while maintaining comparable or better attack success rates.
3. Introduced a style-consistent trigger injection mechanism where the trigger words are chosen to be contextually appropriate rather than rare or out-of-vocabulary words.
4. Provided comprehensive evaluation against multiple defense methods showing BITE's superior ability to evade detection.

## Method Details
- BITE starts with a clean input sentence and iteratively modifies it by inserting or replacing words at positions selected by a language model (e.g., BERT or GPT-2).
- At each iteration, the method selects a position in the sentence and proposes candidate trigger words that maintain fluency. The candidate that best serves the backdoor objective while minimally disrupting perplexity is chosen.
- The trigger pattern emerges from the combination of multiple small modifications across the sentence rather than from a single conspicuous insertion.
- The method uses a scoring function that balances trigger effectiveness (measured by the victim model's confidence on the target class) with text naturalness (measured by perplexity).
- The number of iterations (and thus the number of trigger tokens) is a hyperparameter that controls the trade-off between attack success rate and stealthiness.
- Poisoned samples are generated for a subset of training data and labeled with the target class.

## Key Results
- BITE achieved attack success rates above 90% on sentiment analysis (SST-2) and text classification (AG News) benchmarks while producing poisoned samples with perplexity scores close to clean samples.
- Against ONION defense, BITE's attack success rate remained above 80% even after applying the perplexity-based word filtering, compared to near-zero success rates for simple insertion attacks.
- Human evaluators rated BITE's poisoned samples as significantly more natural than those from BadNL and InsertSent attacks.
- The attack was effective against both BERT and RoBERTa-based classifiers.
- BITE's distributed trigger pattern made it resistant to spectral signature and activation clustering defenses.
