# TextGuard: Provable Defense Against Backdoor Attacks on Text Classification

## Authors
Hengzhi Pei, Jinyuan Jia, Wenbo Guo, Bo Li, Dawn Song

## Venue
NDSS 2024

## Year
2024

## URL
https://arxiv.org/abs/2311.11225

## Abstract Summary
TextGuard provides the first provable (certified) defense against textual backdoor attacks. Unlike empirical defenses that may fail against adaptive attacks, TextGuard offers mathematical guarantees that the model's predictions cannot be influenced by any trigger injection below a certain size. The method is based on randomized smoothing adapted for the text domain: it creates an ensemble of predictions over randomly perturbed versions of the input and uses majority voting to produce a certified robust prediction that is provably unaffected by small trigger insertions.

## Key Contributions
1. Proposed the first certified defense against textual backdoor attacks, providing mathematical guarantees of robustness to trigger injections of bounded size.
2. Adapted randomized smoothing from the continuous image domain to the discrete text domain, handling the challenges of text perturbation including vocabulary constraints and semantic preservation.
3. Developed text-specific perturbation operations (word deletion, word substitution using synonym sets) that are suitable for both the smoothing procedure and the certification bounds.
4. Demonstrated that the certified defense provides meaningful robustness guarantees (certifying against triggers of 1-3 words) while maintaining competitive clean accuracy.

## Method Details
- TextGuard applies randomized smoothing to text classification: for a given input, it generates many perturbed versions by randomly deleting or substituting words, classifies each perturbed version, and returns the majority vote as the prediction.
- The certification is based on the observation that if the majority vote is sufficiently confident (margin between the top-two classes exceeds a threshold), then no trigger insertion of bounded size can change the prediction.
- For word-deletion smoothing: each word is independently deleted with probability p. The certification guarantees robustness against insertions of k words, where k depends on p and the voting margin.
- For word-substitution smoothing: each word is independently replaced with a random synonym. The certification guarantees that substituting up to k words with trigger words cannot change the prediction.
- The certification bounds are derived using techniques from differential privacy and Neyman-Pearson hypothesis testing, adapted for the discrete text setting.
- The base classifier can be any text classification model (BERT, RoBERTa); the smoothing procedure wraps around it.

## Key Results
- TextGuard certified robustness against trigger insertions of 1-2 words for over 70% of test inputs on SST-2 and AG News datasets.
- For 3-word trigger insertions, certification rates were 40-55%, still providing meaningful guarantees for a significant fraction of inputs.
- Clean accuracy was approximately 3-5% lower than the undefended model, reflecting the cost of the randomized smoothing procedure.
- TextGuard's certified accuracy was significantly higher than what could be achieved by adapting image-domain certified defenses directly to text.
- The defense was effective against all trigger types (word insertion, phrase insertion) within the certified trigger size, as guaranteed by the mathematical proof.
