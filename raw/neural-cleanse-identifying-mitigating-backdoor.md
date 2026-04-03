# Neural Cleanse: Identifying and Mitigating Backdoor Attacks in Neural Networks

**Authors:** Bolun Wang, Yuanshun Yao, Shawn Shan, Huiying Li, Bimal Viswanath, Haitao Zheng, Ben Y. Zhao
**Venue:** IEEE S&P 2019
**URL:** https://doi.org/10.1109/SP.2019.00031

## Abstract

This paper presents Neural Cleanse, the first robust and generalizable detection and mitigation system for DNN backdoor attacks. The approach works by reverse-engineering potential triggers for each output label, then using anomaly detection to identify backdoor targets based on trigger size.

## Key Contributions

1. **First generalizable backdoor detection system** that works without knowledge of the attack method
2. **Trigger reverse-engineering**: For each label, find the minimum perturbation that causes universal misclassification
3. **Anomaly detection**: Backdoor labels require significantly smaller triggers, detectable via median absolute deviation
4. **Multiple mitigation strategies**: Input filtering, neuron pruning, and unlearning

## Method

### Detection
1. For each output label y, solve an optimization problem to find the minimal trigger (mask + pattern) that causes all inputs to be classified as y
2. Compute the L1 norm of each label's trigger
3. Use Median Absolute Deviation (MAD) to detect outlier labels — the backdoor label will have an anomalously small trigger norm

### Mitigation
1. **Neuron Pruning**: Identify and prune neurons most activated by the reverse-engineered trigger
2. **Unlearning**: Fine-tune the model to un-learn the backdoor by training on reverse-engineered trigger patterns with correct labels
3. **Input Filtering**: At inference, check inputs against the reverse-engineered trigger pattern

## Key Results

- Detection: 100% true positive rate on MNIST, CIFAR-10, and GTSRB backdoored models
- Less than 2% false positive rate
- Neuron pruning reduces attack success rate to <1% with <2% accuracy loss
- Works against multiple attack types including BadNets and trojan attacks

## Significance

Neural Cleanse was the first comprehensive defense framework, introducing the foundational idea of reverse-engineering triggers as a detection mechanism. This approach became the basis for many subsequent defenses. The optimization-based trigger inversion paradigm remains central to backdoor detection research.
