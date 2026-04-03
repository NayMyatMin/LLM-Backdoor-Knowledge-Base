# STRIP: A Defence Against Trojan Attacks on Deep Neural Networks

**Authors:** Yansong Gao, Chang Xu, Derui Wang, Shiping Chen, Damith C. Ranasinghe, Surya Nepal
**Venue:** ACSAC 2019 (also arXiv 2019)
**URL:** https://arxiv.org/abs/1902.06531

## Abstract

STRIP (STRong Intentional Perturbation) is a run-time defense that detects trojaned inputs at inference time. The key insight is that trojaned inputs are dominated by the trigger pattern and remain classified as the target class even under strong perturbation, while clean inputs produce variable predictions.

## Key Contributions

1. **Inference-time detection**: Works at deployment without modifying the model or requiring retraining
2. **Perturbation-based detection**: Superimposes random patterns on inputs and measures prediction consistency
3. **Entropy as detection signal**: Low prediction entropy over perturbed copies indicates a trojan trigger
4. **Model-agnostic**: Does not assume knowledge of the attack method or trigger type

## Method

1. Given an input to classify, create N perturbed copies by superimposing random clean images from the dataset
2. Feed all perturbed copies through the model and collect predictions
3. Compute the entropy of the prediction distribution
4. **Clean inputs**: Perturbation changes predictions significantly → high entropy
5. **Trojaned inputs**: Trigger dominates despite perturbation → predictions consistently point to target class → low entropy
6. Set an entropy threshold: inputs below threshold are flagged as trojaned

## Key Results

- Less than 1% false acceptance rate (trojaned inputs passing as clean)
- Less than 1% false rejection rate (clean inputs flagged as trojaned)
- Works against BadNets, trojan attacks, and blended injection attacks
- Effective across CIFAR-10, GTSRB, and MNIST
- Low computational overhead (adds ~10 forward passes per input)

## Significance

STRIP pioneered the run-time defense paradigm, complementing training-time defenses like Neural Cleanse and spectral signatures. Its simplicity and effectiveness made it a widely adopted baseline. The entropy-based detection principle has influenced many subsequent inference-time defenses.
