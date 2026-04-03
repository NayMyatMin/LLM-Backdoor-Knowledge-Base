# SEEP: Training Dynamics Grounds Latent Representation Search for Mitigating Backdoor Poisoning Attacks

## Authors
Yuzhou He, Zhenting Wang, Lixin Fan, Qiang Yang

## Venue
TACL 2024 (Transactions of the Association for Computational Linguistics)

## Year
2024

## URL
https://arxiv.org/abs/2405.11575

## Abstract Summary
SEEP investigates how training dynamics can be used to identify and mitigate backdoor poisoning attacks. The paper observes that poisoned samples exhibit distinctive learning behaviors during training compared to clean samples: they tend to be learned faster and with different loss trajectories. SEEP leverages these training dynamics to guide a search in the model's latent representation space, identifying the separation between clean and poisoned samples. The method then uses this separation to filter out poisoned samples before retraining a clean model.

## Key Contributions
1. Provided detailed empirical analysis of how poisoned samples differ from clean samples in their training dynamics (loss curves, gradient norms, representation trajectories), establishing a principled basis for detection.
2. Proposed SEEP, which combines training dynamics analysis with latent representation search to accurately identify poisoned samples in the training set.
3. Demonstrated that training dynamics provide a more robust signal for detecting poisoned samples than static features, especially for stealthy attacks where the poisoned data is designed to be indistinguishable from clean data at the input level.
4. Achieved state-of-the-art poisoned sample detection rates while maintaining low false positive rates on clean data.

## Method Details
- SEEP first performs a preliminary training phase where the model is trained on the full (potentially poisoned) dataset while recording per-sample training dynamics including loss values, gradient magnitudes, and representation changes across epochs.
- The training dynamics features for each sample are aggregated into a feature vector that characterizes the sample's learning behavior.
- These feature vectors are then used to perform a search in the model's latent representation space, using clustering or anomaly detection to separate clean from poisoned samples.
- The separation is refined iteratively: initial clusters are formed based on training dynamics, then boundary samples are re-evaluated using representation similarity to improve accuracy.
- Once poisoned samples are identified and removed, the model is retrained from scratch on the cleaned dataset to eliminate any backdoor behavior.
- The method works for both NLP and vision tasks but is primarily evaluated on text classification and NLI tasks.

## Key Results
- SEEP achieved poisoned sample detection accuracy above 95% on multiple backdoor attack types including insertion-based, syntactic, and style-transfer attacks.
- False positive rates were kept below 3%, meaning very few clean samples were incorrectly removed.
- After retraining on the cleaned dataset, models showed attack success rates below 5% while maintaining clean accuracy within 1% of models trained on fully clean data.
- The method outperformed existing detection methods including spectral signatures, activation clustering, and STRIP on stealthy attacks.
- Training dynamics features were shown to be more discriminative than static representation features, especially for clean-label attacks.
