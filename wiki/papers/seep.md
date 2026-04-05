---
title: "SEEP: Training Dynamics Grounds Latent Representation Search for Mitigating Backdoor Poisoning"
source: raw/seep-training-dynamics-mitigating-backdoor-poisoning.md
venue: TACL
year: 2024
summary: "SEEP leverages distinctive training dynamics of poisoned samples (faster learning, different loss trajectories) to identify and remove them from training data, achieving above 95% detection accuracy with below 3% false positive rates."
tags:
  - defense
  - activation-analysis
threat_model:
  - data-poisoning
compiled: "2026-04-03T14:00:00"
---

# SEEP: Training Dynamics Grounds Latent Representation Search for Mitigating Backdoor Poisoning

## Summary

SEEP investigates how training dynamics can be used to identify and mitigate [[data-poisoning]] attacks. The key observation is that poisoned samples exhibit distinctive learning behaviors during training compared to clean samples: they tend to be learned faster and with different loss trajectories. SEEP combines training dynamics analysis with latent representation search to accurately identify poisoned samples, then retrains a clean model on the filtered dataset.

The method achieves above 95% poisoned sample detection accuracy across multiple [[backdoor-attack]] types with below 3% false positive rates, and the retrained models show [[attack-success-rate]] below 5%.

## Key Concepts

- [[backdoor-defense]]
- [[data-poisoning]]
- [[backdoor-attack]]
- [[attack-success-rate]]
- [[poisoning-rate]]
- Training dynamics
- Latent representation analysis

## Method Details

1. **Preliminary training**: Train the model on the full (potentially poisoned) dataset while recording per-sample training dynamics: loss values, gradient magnitudes, and representation changes across epochs. Poisoned samples tend to be learned faster because backdoor triggers create strong shortcut features that are easy for the model to memorize early in training.
2. **Feature aggregation**: Aggregate per-epoch training dynamics into feature vectors characterizing each sample's learning behavior. These features capture temporal patterns (e.g., when a sample's loss drops, how gradient norms evolve) that distinguish poisoned from clean samples.
3. **Latent space search**: Use clustering or anomaly detection on these aggregated features to separate clean from poisoned samples. The training dynamics create a natural separation in feature space that is more robust than static input features.
4. **Iterative refinement**: Initial clusters are refined by re-evaluating boundary samples using representation similarity, improving precision near the decision boundary where misclassification is most likely.
5. **Retraining**: Remove identified poisoned samples and retrain the model from scratch on the cleaned dataset to fully eliminate any backdoor behavior learned during preliminary training.

Works for both NLP and vision tasks, primarily evaluated on text classification and natural language inference (NLI). The approach is particularly strong on [[clean-label-attack]] scenarios where input-level features are indistinguishable between clean and poisoned samples.

## Results & Findings

- Above 95% poisoned sample detection accuracy across insertion-based, syntactic, and style-transfer attacks.
- False positive rates below 3%.
- After retraining on cleaned data, [[attack-success-rate]] below 5% with clean accuracy within 1% of models trained on fully clean data.
- Outperformed spectral signatures, activation clustering, and STRIP on stealthy attacks.
- Training dynamics features were more discriminative than static representation features, especially for [[clean-label-attack]].

## Relevance to LLM Backdoor Defense

Training dynamics offer a powerful signal for detecting poisoned samples in LLM fine-tuning datasets. Since LLMs are increasingly fine-tuned on crowd-sourced or web-scraped data, the ability to automatically identify and remove poisoned samples before or during training is critical for preventing [[backdoor-attack]] insertion. SEEP's approach could be adapted for [[instruction-tuning]] pipelines, where per-sample loss trajectories during supervised fine-tuning could flag poisoned instruction-response pairs. The method's strength on stealthy attacks and [[clean-label-attack]] scenarios is particularly relevant for LLM settings where poisoned samples are designed to be semantically valid and pass human review.

## Related Work

- [[denoised-poe-defense]] -- training-time defense using shortcut learning connection
- [[proactive-detection]] -- another approach to identifying poisoned samples
- [[poison-forensics]] -- post-hoc traceback of poisoning attacks
- [[triggerless-backdoor]] -- clean-label attacks that SEEP may detect via dynamics

## Backlinks


- [[training-time-vs-post-hoc-defense]]
[[backdoor-defense]] | [[data-poisoning]] | [[backdoor-attack]] | [[attack-success-rate]] | [[clean-label-attack]]
