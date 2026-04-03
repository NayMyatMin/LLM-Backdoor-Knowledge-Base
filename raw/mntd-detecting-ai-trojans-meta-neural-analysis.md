# MNTD: Detecting AI Trojans Using Meta Neural Analysis

## Authors
Xiaojun Xu, Qi Wang, Huichen Li, Nikita Borisov, Carl A. Gunter, Bo Li

## Venue
IEEE Symposium on Security and Privacy (S&P) 2021

## Year
2021

## URL
https://arxiv.org/abs/1910.03137

## Abstract Summary
MNTD (Meta Neural Trojan Detection) introduces a meta-learning approach for detecting whether a neural network has been trojaned (backdoored). Rather than analyzing individual inputs or training data, MNTD trains a meta-classifier that takes a neural network's parameters or behaviors as input and predicts whether it contains a trojan. The meta-classifier is trained on a diverse set of shadow models, some clean and some intentionally trojaned, learning to distinguish the characteristic patterns that trojaned models exhibit in their weights or query-response behaviors.

## Key Contributions
1. Proposed the first meta-learning framework for trojan detection in neural networks, treating the detection problem as a binary classification task over model behaviors rather than over individual inputs.
2. Developed two detection modes: a white-box mode that analyzes model parameters directly, and a black-box mode that queries the model with crafted inputs and analyzes the response patterns.
3. Introduced a shadow model training procedure that generates a diverse dataset of clean and trojaned models for training the meta-classifier, achieving generalization to unseen attack types.
4. Demonstrated that MNTD can detect trojans across different model architectures, attack types, and domains (vision and NLP) with a single meta-classifier.

## Method Details
- Shadow Model Generation: MNTD creates a large set of shadow models by training many neural networks on the same or similar tasks. Half are trained normally (clean) and half are trained with various trojan attacks (different trigger patterns, target classes, poisoning rates).
- Feature Extraction (White-box): For each shadow model, features are extracted from the model's weight matrices, typically using statistics (mean, variance, spectral properties) of weights in critical layers.
- Feature Extraction (Black-box): A set of carefully crafted query inputs (called "jumbo inputs") are passed through each model, and the output logits/probabilities are collected as a feature vector representing the model's behavior.
- Meta-Classifier Training: A binary classifier (e.g., a neural network or random forest) is trained on the extracted features to distinguish clean from trojaned models.
- At test time, the same feature extraction process is applied to the target model, and the meta-classifier predicts whether it is trojaned.
- The method is attack-agnostic: the meta-classifier generalizes to trojan attacks not seen during shadow model training.

## Key Results
- MNTD achieved detection AUC scores above 0.95 on multiple trojan attack types across image classification (MNIST, CIFAR-10) and NLP (sentiment analysis) tasks.
- The black-box mode was nearly as effective as white-box, achieving AUC above 0.92, making the approach applicable even without model parameter access.
- The meta-classifier generalized to trojan attacks with trigger patterns and target classes not seen during shadow model training.
- MNTD outperformed prior model-level detection methods including Neural Cleanse and ABS on most attack scenarios.
- The shadow model training was computationally expensive but only needed to be done once per domain; the resulting meta-classifier was efficient at inference time.
