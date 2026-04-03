# Proactive Detection of Machine Learning Model Backdoors with Suspicious Perturbation Analysis

## Authors
Xiangyu Qi, Tinghao Xie, Jiachen T. Wang, Tong Wu, Saeed Mahloujifar, Prateek Mittal

## Venue
USENIX Security 2023

## Year
2023

## URL
https://arxiv.org/abs/2205.06073

## Abstract Summary
This paper proposes a proactive approach to detecting backdoor poisoning samples during training, before the backdoor is fully learned by the model. Unlike reactive defenses that analyze the model after training, this proactive method monitors the training process and identifies suspicious samples early. The key insight is that potential backdoor triggers can be amplified by applying strategic perturbations to training samples: genuinely poisoned samples respond differently to these perturbations than clean samples, enabling early detection.

## Key Contributions
1. Introduced a proactive defense paradigm that detects backdoor poisoning during training rather than after the model is fully trained, enabling earlier intervention.
2. Developed a suspicious perturbation analysis method that amplifies the distinguishing signal between clean and poisoned samples by applying targeted perturbations during training.
3. Showed that poisoned samples exhibit characteristic sensitivity patterns to specific perturbations that reveal the presence of the embedded trigger, even before the backdoor is fully learned.
4. Demonstrated effectiveness across multiple backdoor attack types with minimal computational overhead added to the standard training pipeline.

## Method Details
- During training, the method periodically applies a set of strategic perturbations to each training sample and observes the model's loss/gradient response.
- For clean samples, perturbations cause relatively uniform changes in the model's response. For poisoned samples, perturbations that disrupt the trigger pattern cause disproportionately large changes.
- The perturbation set is designed to cover common trigger patterns (e.g., small patch insertions, word insertions) without prior knowledge of the specific attack.
- A sensitivity score is computed for each training sample based on the variance of its loss across different perturbations. Poisoned samples exhibit higher sensitivity variance.
- Samples with anomalously high sensitivity scores are flagged and can be removed or quarantined before retraining.
- The perturbation analysis is computationally lightweight because it leverages gradient information already computed during training.

## Key Results
- The proactive detection method identified poisoned samples with over 90% recall and less than 5% false positive rate across insertion-based, blending-based, and warping-based backdoor attacks.
- Detection was effective even at early training stages (within the first 10% of training epochs), enabling early intervention.
- After removing detected poisoned samples and retraining, the resulting models showed attack success rates below 3% with clean accuracy within 1% of models trained on fully clean data.
- The method worked across both image (CIFAR-10, ImageNet subset) and text (SST-2) classification tasks.
- Computational overhead was less than 20% compared to standard training, as the perturbation analysis reused existing gradient computations.
