# Trap and Replace: Defending Backdoor Attacks by Trapping Them into an Easy-to-Replace Subnetwork

## Authors
Haotao Wang, Junyuan Hong, Aston Zhang, Jiayu Zhou, Zhangyang Wang

## Venue
NeurIPS 2022

## Year
2022

## URL
https://arxiv.org/abs/2210.06428

## Abstract Summary
Trap and Replace proposes a novel backdoor defense strategy that intentionally "traps" the backdoor behavior into a small, identifiable subnetwork during training, and then replaces that subnetwork with a clean one. The method leverages the lottery ticket hypothesis insight that backdoor functionality tends to concentrate in a small subset of neurons. By encouraging this concentration through a designed training procedure, the backdoor can be surgically removed with minimal impact on clean performance.

## Key Contributions

1. **Trap-then-replace defense paradigm**: Introduced a fundamentally new defense strategy that works with the backdoor rather than against it, first concentrating it into an identifiable subnetwork and then replacing that subnetwork.

2. **Honeypot module design**: Designed a "honeypot" module that attracts backdoor functionality during training, acting as a trap that isolates the backdoor from the main network.

3. **Clean subnetwork replacement**: After trapping, the contaminated subnetwork is replaced with a clean one trained only on verified clean data, effectively removing the backdoor while preserving the overall model architecture.

4. **Training-time defense**: The method operates during training, providing defense without requiring post-hoc detection or model modification.

## Method Details
The defense operates in three stages:

**Stage 1 - Trap**: During training on the (potentially poisoned) dataset, the model architecture is augmented with a small auxiliary "honeypot" module. The training procedure is designed so that the backdoor functionality is preferentially absorbed by the honeypot module. This is achieved by:
- Using a modular architecture where a small subnetwork is designated as the trap.
- Applying regularization that encourages the main network to learn clean features while the trap module absorbs shortcut (backdoor) patterns.
- The trap module has limited capacity, which is sufficient for the simple trigger-to-target mapping but forces the main network to rely on legitimate features for clean classification.

**Stage 2 - Identify**: After training, the trapped subnetwork is identified by analyzing which modules have absorbed the backdoor behavior. This can be verified by checking if removing the trap module significantly reduces attack success rate while maintaining clean accuracy.

**Stage 3 - Replace**: The trapped (contaminated) subnetwork is replaced with a freshly initialized module that is briefly fine-tuned on a small set of clean data. This replacement removes the backdoor while the main network's clean-task knowledge is preserved.

The method draws on the insight that backdoor patterns are simpler than clean-task patterns and will preferentially occupy the most accessible network capacity.

## Key Results
- Reduces attack success rate to below 3% across BadNets, Blended, WaNet, and other attacks on CIFAR-10 and GTSRB.
- Clean accuracy after replacement is within 1% of a clean-trained model.
- The trap module successfully absorbs >95% of the backdoor functionality in most cases.
- More robust than pruning-based defenses because the backdoor is concentrated rather than distributed.
- Works with various network architectures (ResNet, VGG, WRN).
- Requires only a small clean validation set (5% of training data) for the replacement stage.
