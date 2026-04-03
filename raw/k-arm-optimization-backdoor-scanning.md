# Topological Detection of Trojaned Neural Networks (K-Arm Optimization for Backdoor Scanning)

## Authors
Guangyu Shen, Yingqi Liu, Guanhong Tao, Shengwei An, Qiuling Xu, Siyuan Cheng, Shiqing Ma, Xiangyu Zhang

## Venue
ICML 2021

## Year
2021

## URL
https://arxiv.org/abs/2108.00300

## Abstract Summary
This paper proposes K-Arm optimization, a scalable approach for scanning neural networks for backdoor trojans. The method formulates backdoor scanning as a multi-armed bandit problem, where each "arm" corresponds to a potential target class. The optimization efficiently allocates computational resources across target classes to identify which class (if any) is the backdoor target. This approach significantly reduces the computational cost of trigger reverse-engineering compared to exhaustive scanning of all classes.

## Key Contributions

1. **Multi-armed bandit formulation**: Framed backdoor scanning as a K-armed bandit problem, enabling efficient resource allocation across potential target classes rather than exhaustively scanning each class.

2. **Adaptive scanning strategy**: Developed an adaptive strategy that focuses computational effort on the most promising candidate target classes, using upper confidence bound (UCB) exploration to balance exploitation and exploration.

3. **Scalability to many classes**: The method scales gracefully to datasets with many classes (e.g., ImageNet with 1000 classes), where exhaustive methods like Neural Cleanse become prohibitively expensive.

4. **Integration with multiple trigger inversion methods**: The K-Arm framework is compatible with different underlying trigger inversion techniques, serving as a meta-algorithm that makes any inversion method more efficient.

## Method Details
The K-Arm optimization framework works as follows:

**Problem Formulation**: Given a model with K output classes, the goal is to determine if any class is a backdoor target. For each candidate target class k, a trigger inversion process attempts to find the smallest trigger that causes misclassification to class k. The class with the smallest trigger is the most likely backdoor target.

**Multi-Armed Bandit Approach**:
1. **Arms**: Each potential target class k is an arm. Pulling arm k means running one step of trigger optimization for class k.
2. **Reward**: The reward for pulling arm k is the progress made in trigger optimization (decrease in trigger size or increase in attack success rate).
3. **UCB Strategy**: The upper confidence bound algorithm selects which arm to pull next, balancing between classes that have shown promising results (exploitation) and classes that have been under-explored (exploration).

**Optimization Loop**:
1. Initialize trigger optimization for all K classes.
2. At each iteration, use UCB to select the most promising target class.
3. Run one or more optimization steps for the selected class.
4. Update the reward estimate for that class.
5. Repeat until convergence or budget exhaustion.
6. Compare the best trigger across all classes to a detection threshold.

**Trigger Inversion**: The underlying trigger optimization for each class uses gradient-based methods similar to Neural Cleanse, but the K-Arm framework dramatically reduces the total number of optimization steps needed by focusing on likely target classes.

## Key Results
- Achieves detection accuracy comparable to exhaustive scanning (Neural Cleanse) while using 3-10x fewer optimization steps.
- Scales to ImageNet (1000 classes) where exhaustive scanning is infeasible, achieving >90% detection accuracy.
- Detection time reduces from hours (exhaustive) to minutes for large-scale models.
- Successfully detects backdoors from BadNets, Blended, WaNet, and Trojan attacks across CIFAR-10, GTSRB, and ImageNet.
- The UCB strategy consistently outperforms random arm selection and round-robin strategies.
- False positive rate (flagging clean models) is below 5% across all datasets.
