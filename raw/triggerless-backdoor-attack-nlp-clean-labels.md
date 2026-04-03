# Triggerless Backdoor Attack for NLP Tasks with Clean Labels

## Authors
Leilei Gan, Jiwei Li, Tianwei Zhang, Xiaoya Li, Yuxian Meng, Fei Wu, Yi Yang, Shangwei Guo, Chun Fan

## Venue
NAACL 2022

## Year
2022

## URL
https://arxiv.org/abs/2111.07970

## Abstract Summary
This paper introduces a triggerless backdoor attack for NLP that does not require injecting any explicit trigger pattern into the training data. Unlike traditional backdoor attacks that embed specific words, sentences, or syntactic patterns as triggers, this approach poisons the model by carefully selecting and relabeling clean training samples. The attack exploits the model's learning dynamics to create a backdoor that can be activated by specific semantic features naturally present in inputs, making it fundamentally different from trigger-based attacks and much harder to detect.

## Key Contributions
1. Proposed the first triggerless backdoor attack for NLP tasks that operates with clean labels, eliminating the need for any explicit trigger pattern while still achieving effective backdoor behavior.
2. Demonstrated that careful selection of training samples based on their semantic similarity to the target concept can implant a backdoor that activates on inputs with specific semantic characteristics.
3. Showed that the attack is inherently more stealthy than trigger-based attacks because the poisoned training data contains no anomalous patterns, making it undetectable by existing defenses like ONION, STRIP, and spectral signatures.
4. Provided analysis of why the attack works, relating it to the model's tendency to learn spurious correlations between certain semantic features and target labels.

## Method Details
- The attack identifies a target semantic concept (e.g., a specific topic or entity) and selects clean training samples that are semantically related to this concept.
- Selected samples are assigned the target label (clean-label setting) and added to the training data. No modifications are made to the text of these samples.
- During training, the model learns an association between the semantic features of the selected concept and the target label, creating a backdoor.
- At inference time, any input that contains the target semantic features (e.g., mentions of a specific entity or topic) will be classified as the target class.
- The sample selection process uses embedding similarity (from pre-trained models) to identify training samples most strongly associated with the target semantic concept.
- The poisoning rate is kept low (typically 1-5% of training data) to maintain model utility on clean inputs.

## Key Results
- The attack achieved high attack success rates (80-95%) on sentiment analysis and text classification tasks while maintaining clean accuracy within 1% of the original model.
- Existing defense methods including ONION (perplexity-based), STRIP (input perturbation), and spectral signature analysis all failed to detect the attack because there are no anomalous patterns in the poisoned data.
- The attack transferred across different model architectures (BERT, RoBERTa, DistilBERT).
- The work highlighted a fundamental vulnerability in text classifiers that goes beyond trigger-based attacks, motivating research into defense methods that can address semantic-level backdoors.
