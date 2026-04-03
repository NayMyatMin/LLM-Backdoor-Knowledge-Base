---
title: "Topological Detection of Trojaned Neural Networks (K-Arm Optimization for Backdoor Scanning)"
source: raw/k-arm-optimization-backdoor-scanning.md
venue: ICML
year: 2021
summary: "K-Arm formulates backdoor scanning as a multi-armed bandit problem, using UCB-based adaptive resource allocation across target classes to achieve detection accuracy comparable to exhaustive scanning at 3-10x lower computational cost."
compiled: "2026-04-03T16:00:00"
---

# Topological Detection of Trojaned Neural Networks (K-Arm Optimization for Backdoor Scanning)

**Authors:** Guangyu Shen, Yingqi Liu, Guanhong Tao, Shengwei An, Qiuling Xu, Siyuan Cheng, Shiqing Ma, Xiangyu Zhang
**Venue:** ICML 2021 **Year:** 2021

## Summary

Trigger reverse-engineering methods like Neural Cleanse must exhaustively optimize a candidate trigger for every possible target class, making them prohibitively expensive for models with many output classes (e.g., ImageNet with 1000 classes). K-Arm addresses this scalability bottleneck by formulating backdoor scanning as a multi-armed bandit problem, where each "arm" corresponds to a potential target class and the reward measures trigger optimization progress.

Using the Upper Confidence Bound (UCB) algorithm, K-Arm adaptively allocates computational resources — spending more optimization steps on promising candidate classes and fewer on unlikely ones. This balances exploration (trying under-examined classes) with exploitation (focusing on classes showing signs of being the backdoor target). The framework is a meta-algorithm compatible with any underlying trigger inversion technique.

K-Arm achieves detection accuracy comparable to exhaustive scanning while using 3–10x fewer optimization steps. It scales to ImageNet (1000 classes) with >90% detection accuracy where exhaustive methods are infeasible, reducing detection time from hours to minutes.

## Key Concepts

- [[trigger-reverse-engineering]] — the underlying technique accelerated by K-Arm's resource allocation
- [[backdoor-defense]] — model-level scanning to detect whether a model contains a backdoor
- [[trojan-attack]] — the class of attacks K-Arm is designed to detect
- [[attack-success-rate]] — used as part of the reward signal in the bandit formulation

## Method Details

**Problem formulation:** Given a model with K output classes, the defense determines if any class is a backdoor target by finding the smallest trigger that causes misclassification to each class. The class with the smallest discovered trigger is most likely the backdoor target.

**Multi-armed bandit mapping:**
- **Arms:** Each potential target class k is an arm
- **Pulling an arm:** Running one or more steps of trigger optimization for class k
- **Reward:** Progress in trigger optimization — decrease in required trigger size or increase in attack success rate for class k

**UCB strategy:** The algorithm selects which class to optimize next using:

UCB_k = μ_k + c · √(ln(n) / n_k)

where μ_k is the average reward for arm k, n is total pulls, n_k is pulls for arm k, and c is an exploration constant. This naturally focuses computation on classes with high reward (likely backdoor targets) while ensuring under-explored classes are not neglected.

**Optimization loop:**
1. Initialize trigger optimization for all K classes with a small budget
2. At each iteration, use UCB to select the most promising target class
3. Run one or more optimization steps for the selected class
4. Update the reward estimate based on optimization progress
5. Repeat until convergence or computational budget exhaustion
6. Compare the best discovered trigger across all classes to a detection threshold

The underlying trigger optimization per class uses gradient-based methods similar to Neural Cleanse, but the total optimization budget is dramatically reduced by K-Arm's adaptive allocation.

## Results & Findings

- Detection accuracy comparable to exhaustive scanning (Neural Cleanse) at 3–10x fewer optimization steps
- Scales to ImageNet (1000 classes) with >90% detection accuracy where exhaustive scanning is infeasible
- Detection time reduced from hours to minutes for large-scale models
- Detects backdoors from BadNets, Blended, WaNet, and Trojan attacks across CIFAR-10, GTSRB, and ImageNet
- UCB strategy consistently outperforms random arm selection and round-robin strategies
- False positive rate below 5% across all datasets

## Relevance to LLM Backdoor Defense

K-Arm's scalability contribution is directly relevant to LLM backdoor scanning. LLMs operate over vocabularies of 30,000–100,000+ tokens, making exhaustive trigger search across all possible target outputs even more computationally prohibitive than in image classification. The bandit-based resource allocation framework could be adapted to efficiently scan LLM output spaces — prioritizing token sequences that show early signs of being backdoor targets while abandoning unpromising candidates. The meta-algorithm nature of K-Arm means it can wrap around any LLM-specific trigger inversion method, making existing LLM scanning tools more practical at scale.

## Related Work

- [[neural-cleanse]] — the exhaustive scanning baseline that K-Arm accelerates
- [[i-bau]] — bilevel optimization for backdoor removal; K-Arm focuses on detection rather than removal
- [[activation-clustering]] — representation-based detection; complementary to trigger-inversion approaches
- [[strip]] — input perturbation-based detection; does not require trigger optimization

## Backlinks
[[backdoor-defense]] | [[trigger-reverse-engineering]] | [[trojan-attack]] | [[backdoor-attack]] | [[attack-success-rate]]
