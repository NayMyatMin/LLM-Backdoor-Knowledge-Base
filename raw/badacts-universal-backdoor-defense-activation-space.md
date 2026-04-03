# BadActs: A Universal Backdoor Defense in the Activation Space

## Authors
Biao Yi, Sishuo Chen, Yiming Li, Tong Li, Baolei Zhang, Zheli Liu

## Venue
Findings of ACL 2024

## Year
2024

## URL
https://arxiv.org/abs/2405.11227

## Abstract Summary
BadActs proposes a universal backdoor defense method that operates in the model's activation space. The core insight is that backdoor triggers create distinctive activation patterns that differ from those produced by clean inputs, and these differences are consistent across different types of backdoor attacks. BadActs detects and mitigates backdoor behavior by analyzing the internal activations of the model during inference, identifying anomalous activation patterns associated with backdoor triggers, and correcting them to produce clean predictions.

## Key Contributions
1. Proposed a universal defense mechanism that works in the activation space of neural networks, making it applicable across different backdoor attack types without attack-specific knowledge.
2. Discovered that backdoor triggers produce characteristic activation patterns that can be reliably distinguished from clean activation patterns through statistical analysis.
3. Developed an activation correction technique that modifies suspicious activations at inference time to neutralize the backdoor effect while preserving the model's clean predictions.
4. Demonstrated broad applicability across multiple NLP tasks and backdoor attack types, including both insertion-based and more sophisticated attacks.

## Method Details
- BadActs collects activation patterns (hidden states from intermediate layers) from a small set of clean reference samples during a calibration phase.
- At inference time, the method computes the activation pattern for each input and compares it against the clean reference distribution.
- Statistical measures (e.g., Mahalanobis distance, cosine similarity distributions) are used to identify activations that deviate significantly from the clean distribution.
- When anomalous activations are detected, the method applies a correction by projecting the activations back toward the clean activation distribution.
- The correction is applied at specific critical layers identified during the calibration phase as most discriminative between clean and poisoned activations.
- The approach requires only a small number of clean samples (typically 50-200) for calibration and no knowledge of the attack method or trigger pattern.

## Key Results
- BadActs achieved consistent defense performance across multiple attack types including insertion attacks, syntactic attacks, and style-transfer attacks on sentiment analysis and text classification tasks.
- The method reduced attack success rates to below 10% for most attack types while maintaining clean accuracy within 1-2% of the original model.
- The activation-space approach proved more robust than input-space defenses (like ONION) against attacks that do not use obvious lexical triggers.
- The defense transferred across model architectures (BERT, RoBERTa, DeBERTa) with minimal recalibration.
- Runtime overhead was minimal, adding less than 5% additional inference time compared to the undefended model.
