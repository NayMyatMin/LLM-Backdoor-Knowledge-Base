# Poison Forensics: Traceback of Data Poisoning Attacks in Neural Networks

## Authors
Shawn Shan, Arjun Nitin Bhagoji, Haitao Zheng, Ben Y. Zhao

## Venue
USENIX Security 2022

## Year
2022

## URL
https://arxiv.org/abs/2110.06904

## Abstract Summary
Poison Forensics addresses the post-hoc problem of tracing back data poisoning attacks to identify which specific training samples were responsible for a model's compromised behavior. Unlike defense methods that prevent or detect attacks during training, this work focuses on forensic analysis after an attack has been discovered. The method works by analyzing the influence of training samples on the model's behavior for suspicious inputs, using techniques from influence functions and data attribution to identify the minimal set of training samples whose removal would eliminate the poisoning effect.

## Key Contributions
1. Formulated the data poisoning traceback problem: given a model exhibiting suspicious behavior, identify the specific training samples that caused the poisoning.
2. Developed a scalable traceback method based on influence estimation that can handle large training datasets and complex model architectures.
3. Introduced a clustering-based refinement step that groups candidate poisoned samples based on their influence patterns, improving precision of traceback.
4. Demonstrated forensic traceback across multiple poisoning attack types including backdoor attacks, clean-label attacks, and targeted misclassification attacks.

## Method Details
- The method starts with a suspicious input-output pair (e.g., a triggered input that the model misclassifies to the target class) and aims to identify which training samples caused this behavior.
- Influence functions are used to estimate each training sample's contribution to the model's prediction on the suspicious input. Samples with the highest influence scores are candidates for being poisoned.
- Due to the computational cost of exact influence functions, the method uses efficient approximations (e.g., TracIn or Arnoldi-based approximations) to scale to large datasets.
- A clustering step groups high-influence candidate samples and identifies clusters that share common characteristics (e.g., similar trigger patterns or similar mislabeling), separating true poisoned samples from legitimately influential clean samples.
- The method iteratively refines the candidate set by removing identified poisoned samples, retraining, and checking whether the suspicious behavior is eliminated.
- Both white-box (full model access) and gray-box (limited access) traceback scenarios are considered.

## Key Results
- Poison Forensics correctly identified over 90% of poisoned training samples across multiple backdoor attack types on image classification and text classification tasks.
- The precision of traceback (fraction of identified samples that are truly poisoned) exceeded 85% in most scenarios.
- The method was effective for both traditional backdoor attacks (with explicit triggers) and clean-label attacks (where poisoned samples have correct labels).
- Traceback was possible even when the poisoning rate was very low (0.5% of training data), though precision decreased with lower poisoning rates.
- The forensic analysis provided actionable information about the nature of the attack (trigger type, target class) that could inform future defenses.
