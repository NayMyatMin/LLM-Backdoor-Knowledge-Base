# Backdoor Defense via Decoupling the Training Process

## Authors
Kunzhe Huang, Yiming Li, Baoyuan Wu, Zhan Qin, Kui Ren

## Venue
ICLR 2022

## Year
2022

## URL
https://arxiv.org/abs/2202.03423

## Abstract Summary
This paper proposes Decoupling-based Backdoor Defense (DBD), a training-time defense that decouples the standard end-to-end training process into separate stages to prevent backdoor injection. The key insight is that end-to-end training on poisoned data allows the model to learn the shortcut from trigger to target label. By decoupling representation learning from classifier training, and using self-supervised learning for the encoder, the defense prevents the model from learning the trigger-label association during the critical representation learning phase.

## Key Contributions

1. **Decoupled training paradigm**: Proposed separating model training into distinct stages (representation learning and classifier learning) to break the backdoor injection mechanism that relies on end-to-end training.

2. **Self-supervised encoder training**: Used self-supervised learning (contrastive learning) for the encoder to learn representations without label information, preventing the encoder from learning trigger-to-label shortcuts.

3. **Semi-supervised fine-tuning**: Developed a semi-supervised fine-tuning strategy that uses the self-supervised encoder's representations to identify and down-weight suspicious samples during classifier training.

4. **No clean data requirement**: The defense operates during training on the poisoned dataset without requiring a separate clean validation set.

## Method Details
DBD decouples training into three stages:

**Stage 1 - Self-Supervised Pre-training**: Train the feature encoder using self-supervised contrastive learning (e.g., SimCLR) on the potentially poisoned dataset. Crucially, this stage uses only the images without their labels:
- The contrastive loss pulls augmented views of the same image together and pushes different images apart.
- Since labels are not used, the encoder cannot learn the trigger-to-target-label association.
- The trigger pattern, being a simple shortcut, does not significantly affect the contrastive representations (which focus on semantic content).

**Stage 2 - Suspicious Sample Identification**: Using the self-supervised representations:
1. Cluster the representations within each labeled class.
2. Poisoned samples tend to form a separate sub-cluster (their representations differ from clean samples of the same class because they contain trigger-class features).
3. Identify samples in minority sub-clusters as suspicious.

**Stage 3 - Semi-supervised Classifier Training**: Train the classifier head on top of the frozen encoder:
1. Use labeled clean-identified samples with full cross-entropy loss.
2. Use suspicious samples with reduced weight or only for consistency regularization (pseudo-label from the current model).
3. The encoder remains frozen (from Stage 1), preventing any backdoor from being injected into the representations.

**End-to-end Fine-tuning**: Optionally, a brief end-to-end fine-tuning with the filtered data can improve clean accuracy without introducing the backdoor (since suspicious samples are excluded or down-weighted).

## Key Results
- Reduces attack success rate to below 3% across BadNets, Blended, WaNet, Input-Aware, and label-consistent attacks on CIFAR-10, GTSRB, and Tiny ImageNet.
- Clean accuracy is within 1-2% of a model trained on clean data.
- The self-supervised encoder effectively ignores trigger patterns: representation similarity between triggered and clean inputs of the same class is low.
- Suspicious sample identification achieves >85% precision in flagging poisoned samples.
- The decoupled approach is more robust than end-to-end training with data filtering, because the encoder never learns the trigger association.
- Works without any clean validation data, a significant practical advantage over many post-training defenses.
