# Just How Toxic is Data Poisoning? A Unified Benchmark for Backdoor and Data Poisoning Attacks

## Authors
Avi Schwarzschild, Micah Goldblum, Arjun Gupta, John P. Dickerson, Tom Goldstein

## Venue
ICML 2021

## Year
2021

## URL
https://arxiv.org/abs/2006.12557

## Abstract Summary
This paper provides the first unified benchmark for evaluating data poisoning and backdoor attacks, addressing the lack of standardized evaluation that made it difficult to compare different attacks. The authors systematically evaluate a wide range of poisoning attacks (both backdoor and triggerless) under consistent experimental conditions and reveal that many attacks are less effective than previously reported when evaluated fairly. The benchmark includes standardized datasets, models, metrics, and training procedures.

## Key Contributions

1. **Unified evaluation benchmark**: Created the first standardized benchmark for comparing backdoor and data poisoning attacks under identical experimental conditions, eliminating confounding variables from differing evaluation setups.

2. **Systematic attack comparison**: Evaluated and compared a comprehensive set of attacks including Poison Frogs, Witches' Brew, MetaPoison, BadNets, Blended, and others, revealing significant performance differences from original claims.

3. **Attack taxonomy**: Provided a clear taxonomy distinguishing between clean-label attacks, dirty-label attacks, backdoor attacks, and triggerless poisoning attacks, clarifying the threat models and assumptions of each.

4. **Effectiveness reassessment**: Showed that many attacks are significantly less effective than claimed in their original papers when evaluated under controlled conditions with proper hyperparameter tuning of the victim's training.

## Method Details
The benchmark standardizes evaluation across multiple dimensions:

**Attack Categories**:
- **Backdoor attacks (dirty-label)**: Modify both input and label (BadNets, Blended). Attacker adds a trigger pattern and changes the label to target class.
- **Backdoor attacks (clean-label)**: Modify only the input, keeping correct labels (Hidden Trigger, Sleeper Agent). The trigger causes misclassification at test time.
- **Triggerless poisoning**: Modify training data without triggers to cause misclassification of specific test inputs (Poison Frogs, Witches' Brew, MetaPoison).

**Standardized Evaluation Protocol**:
1. **Datasets**: CIFAR-10, CIFAR-100, and a subset of ImageNet, all preprocessed identically.
2. **Models**: ResNet-18, ResNet-34, VGG-16, and MobileNetV2 trained with standard hyperparameters.
3. **Training**: Standard SGD with momentum, cosine learning rate schedule, standard data augmentation.
4. **Metrics**: Attack success rate (ASR), clean accuracy (CA), poisoning budget (number of modified samples).

**Key Evaluation Insights**:
- Previous work often used weak victim training (no augmentation, suboptimal hyperparameters), inflating reported attack success.
- The benchmark uses strong, standard training practices that any competent practitioner would employ.
- Transfer-based attacks (crafted on a surrogate model) show significant degradation when the victim uses a different architecture.

## Key Results
- Many clean-label poisoning attacks achieve near-zero success rate under the standardized benchmark, despite reporting high success in their original papers.
- Dirty-label backdoor attacks (BadNets, Blended) remain effective but are easily detectable through label inspection.
- Data augmentation significantly reduces the effectiveness of many poisoning attacks, acting as an implicit defense.
- The required poisoning budget for successful attacks is often much larger than originally claimed (5-10x more poisoned samples needed).
- Transfer attacks show limited cross-architecture effectiveness.
- The benchmark reveals that the gap between attack and defense is much smaller than the literature suggests, with many attacks failing under proper evaluation.
