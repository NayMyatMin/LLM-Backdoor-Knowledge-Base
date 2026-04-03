---
title: "CleanGen: Mitigating Backdoor Attacks for Generation Tasks in Large Language Models"
source: raw/cleangen-mitigating-backdoor-generation-tasks-llms.md
venue: EMNLP
year: 2024
summary: "CleanGen is a decoding-time defense that monitors LLM token generation, detecting anomalous patterns by comparing against a clean reference model and intervening when divergence exceeds a threshold."
compiled: "2026-04-03T14:00:00"
---

# CleanGen: Mitigating Backdoor Attacks for Generation Tasks in Large Language Models

## Summary

CleanGen addresses the challenge of defending against [[backdoor-attack]] in text generation tasks, where backdoor effects are more subtle than in classification -- manifesting as gradual changes in generated text rather than clear misclassifications. The method operates during decoding by comparing the potentially backdoored model's token probability distributions against those of a clean reference model at each generation step.

When divergence exceeds a threshold, CleanGen substitutes the backdoored model's token prediction with the clean reference model's, blocking backdoor behavior while preserving generation quality with less than 5% degradation.

## Key Concepts

- [[backdoor-defense]]
- [[backdoor-attack]]
- [[attack-success-rate]]
- Decoding-time defense
- Token-level anomaly detection
- Reference model comparison

## Method Details

1. **Divergence monitoring**: At each token position during generation, compute divergence between the potentially backdoored model's probability distribution and a clean reference model's distribution.
2. **Threshold-based intervention**: When divergence exceeds a calibrated threshold, substitute the backdoored model's token prediction with the clean reference model's prediction.
3. **Reference model selection**: Can be a smaller independently trained model or a pre-fine-tuning checkpoint of the same model.
4. **Threshold calibration**: Calibrated on a small validation set to balance defense effectiveness and generation quality.
5. Architecture-agnostic; works with any autoregressive LLM.

## Results & Findings

- Reduced [[attack-success-rate]] from over 85% to below 15% across multiple attack scenarios.
- Generation quality (perplexity, BLEU, human evaluation) preserved with less than 5% degradation.
- Effective against toxic text generation, misinformation production, and data exfiltration attacks.
- Defended against both explicit trigger attacks and instruction-level attacks.
- Computational overhead approximately doubles inference time due to parallel reference model inference.

## Relevance to LLM Backdoor Defense

CleanGen is one of the few defenses specifically designed for the generation setting that dominates LLM usage. Its decoding-time approach is practical for deployment, requiring no retraining, though the computational overhead of running a reference model is a consideration.

## Related Work

- [[simulate-and-eliminate]] -- training-time defense for generative LLMs
- [[weak-to-strong-unlearning]] -- distillation-based defense
- [[onion]] -- input-level defense for classification setting
- [[beear]] -- embedding-level defense for safety backdoors

## Backlinks


- [[alignment-meets-backdoors]]
[[backdoor-defense]] | [[backdoor-attack]] | [[attack-success-rate]]
