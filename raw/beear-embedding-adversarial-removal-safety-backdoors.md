# BEEAR: Embedding-based Adversarial Removal of Safety Backdoors in Large Language Models

## Authors
Yi Zeng, Weiyu Sun, Tran Ngoc Huynh, Dawn Song, Bo Li, Ruoxi Jia

## Venue
EMNLP 2024

## Year
2024

## URL
https://arxiv.org/abs/2406.17092

## Abstract Summary
BEEAR (Backdoor Embedding Exploration and Adversarial Removal) addresses the problem of removing safety backdoors from large language models. Safety backdoors are particularly dangerous because they can bypass an LLM's safety alignment, causing the model to generate harmful content when a specific trigger is present. BEEAR operates in the embedding space by identifying directions in the model's representation space that correspond to backdoor behavior and then adversarially removing these directions through targeted fine-tuning, restoring the model's safety alignment without significantly degrading its general capabilities.

## Key Contributions
1. Formulated the safety backdoor removal problem for LLMs and proposed an embedding-space approach that can identify and remove backdoor-related representation directions.
2. Introduced a two-phase framework: exploration (finding backdoor-related directions in embedding space) and removal (adversarial fine-tuning to eliminate these directions).
3. Demonstrated that safety backdoors create identifiable signatures in the embedding space that can be systematically detected without knowledge of the specific trigger.
4. Showed that BEEAR can restore safety alignment in backdoored LLMs while preserving their general instruction-following capabilities and knowledge.

## Method Details
- Phase 1 (Exploration): BEEAR identifies backdoor-related directions in the model's embedding space by searching for perturbation directions that, when applied to clean inputs, cause the model to generate harmful or misaligned outputs. This is done through gradient-based optimization in the embedding space.
- Phase 2 (Removal): Once backdoor-related directions are identified, the method performs adversarial fine-tuning that specifically removes the model's sensitivity to these directions. The fine-tuning objective ensures that perturbations along the identified directions no longer trigger harmful behavior.
- The exploration phase uses a safety classifier to evaluate whether perturbations in the embedding space lead to unsafe outputs, guiding the search toward backdoor-relevant directions.
- The removal phase employs a constrained optimization that minimizes the model's response to backdoor directions while maintaining performance on clean inputs through a regularization term.
- The method does not require knowledge of the specific backdoor trigger, only access to the model weights and a small set of clean instruction-response pairs.

## Key Results
- BEEAR successfully removed safety backdoors from multiple LLM architectures (LLaMA-2, Mistral) reducing attack success rates from over 90% to below 10%.
- General capabilities (measured by benchmarks like MMLU and MT-Bench) were preserved within 2-3% of the original model after backdoor removal.
- The method outperformed baseline approaches including standard fine-tuning, knowledge distillation, and input-based detection methods.
- BEEAR was effective against multiple types of safety backdoors including word-trigger, phrase-trigger, and instruction-style triggers.
- The identified backdoor directions in embedding space provided interpretable insights into how safety backdoors operate within LLMs.
