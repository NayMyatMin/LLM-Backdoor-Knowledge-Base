# TED: Towards Robust Backdoor Detection via Topological Evolution Dynamics

## Authors
Xiaoxing Mo, Yechao Zhang, Leo Yu Zhang, Wei Luo, Nan Sun, Shengshan Hu, Shang Gao, Yang Xiang

## Venue
IEEE Symposium on Security and Privacy (S&P) 2024

## Year
2024

## URL
https://arxiv.org/abs/2312.02673

## Abstract Summary
TED (Topological Evolution Dynamics) proposes a novel backdoor detection method based on analyzing how the topological structure of a model's learned representations evolves during training. The core insight is that clean and poisoned samples induce fundamentally different topological patterns in the feature space as the model trains: clean samples form cohesive clusters that evolve smoothly, while poisoned samples create topological anomalies (extra connected components, unusual homology features) that can be detected through persistent homology, a tool from topological data analysis (TDA).

## Key Contributions
1. Introduced topological data analysis (specifically persistent homology) as a tool for backdoor detection, providing a mathematically principled approach to analyzing the structure of learned representations.
2. Proposed analyzing the evolution of topological features across training epochs, not just the final state, which provides a richer and more robust detection signal.
3. Demonstrated that topological evolution dynamics capture backdoor signatures that are invisible to standard statistical methods (mean, variance, spectral analysis).
4. Achieved robust detection across diverse attack types including those specifically designed to evade statistical detection methods.

## Method Details
- During training (or post-hoc by replaying training), TED extracts feature representations for all training samples at multiple epochs and computes topological features using persistent homology.
- Persistent homology analyzes the Rips complex constructed from the feature representations and identifies topological features (connected components, loops, voids) at different scales.
- For each class, the method tracks how topological features (birth/death times of homological features) change across training epochs, creating a topological evolution trajectory.
- Clean classes show smooth, predictable topological evolution (e.g., gradual merging of clusters into a single component). Poisoned classes show anomalous evolution (e.g., a persistent secondary cluster that does not merge with the main cluster).
- The detection criterion compares the topological evolution of each class against the expected clean evolution pattern, flagging classes with anomalous topological dynamics as potentially containing poisoned samples.
- Once a suspicious class is identified, individual sample-level detection uses topological membership analysis to separate clean from poisoned samples.

## Key Results
- TED detected backdoor attacks with AUC above 0.97 on CIFAR-10, GTSRB, and ImageNet-subset across 12 different attack types.
- Against adaptive attacks that specifically target statistical detection (e.g., by matching the mean and variance of clean feature distributions), TED maintained AUC above 0.93, while statistical methods dropped to 0.50-0.65.
- The topological evolution analysis was shown to be fundamentally different from statistical analysis, providing complementary detection capabilities.
- TED was effective against clean-label attacks, where the topological signature of the small poisoned cluster was detectable despite having correct labels.
- Computational cost was manageable, adding approximately 30-50% to training time depending on the dataset size and the number of epochs analyzed.
