---
title: "CleanGen: Mitigating Backdoor Attacks for Generation Tasks in Large Language Models"
source: raw/cleangen-mitigating-backdoor-generation-tasks-llms.md
venue: EMNLP
year: 2024
summary: "CleanGen is a decoding-time defense that monitors LLM token generation, detecting anomalous patterns by comparing against a clean reference model and intervening when divergence exceeds a threshold."
tags:
  - defense
  - inference-time
threat_model: "data-poisoning"
compiled: "2026-04-03T14:00:00"
---

# CleanGen: Mitigating Backdoor Attacks for Generation Tasks in Large Language Models

## Summary

CleanGen, by Yuetai Li, Zhangchen Xu, Fangqian Liu, and colleagues, addresses the challenge of defending against [[backdoor-attack]] in text generation tasks, where backdoor effects are more subtle than in classification -- manifesting as gradual changes in generated text (toxic content, misinformation, data exfiltration) rather than clear misclassifications. Most prior [[backdoor-defense]] methods target classification settings and do not transfer well to the open-ended generation paradigm that dominates LLM usage.

The method operates during decoding by comparing the potentially backdoored model's token probability distributions against those of a clean reference model at each generation step. When divergence exceeds a calibrated threshold, CleanGen substitutes the backdoored model's token prediction with the clean reference model's, blocking backdoor behavior while preserving generation quality with less than 5% degradation on clean inputs.

## Key Concepts

- [[backdoor-defense]]
- [[backdoor-attack]]
- [[attack-success-rate]]
- Decoding-time defense
- Token-level anomaly detection
- Reference model comparison

## Method Details

1. **Divergence monitoring**: At each token position t during generation, compute divergence D(P_backdoor(t) || P_clean(t)) between the potentially backdoored model's probability distribution and a clean reference model's distribution. The divergence metric can be KL-divergence, Jensen-Shannon divergence, or total variation distance.
2. **Threshold-based intervention**: When D exceeds a calibrated threshold tau, substitute the backdoored model's token prediction with the clean reference model's prediction. This per-token gating mechanism allows most generation to proceed normally while intercepting only anomalous tokens.
3. **Reference model selection**: The clean reference model can be a smaller independently trained model, a pre-fine-tuning checkpoint of the same model, or a different model from the same family. The pre-fine-tuning checkpoint is most practical as it requires no additional training.
4. **Threshold calibration**: tau is calibrated on a small validation set (as few as 100 clean samples) by measuring the distribution of divergence scores on clean inputs and setting tau at a high percentile (e.g., 95th) to minimize false interventions.
5. **Architecture-agnostic**: Works with any autoregressive LLM since it only requires access to output probability distributions at each decoding step.

## Results & Findings

- Reduced [[attack-success-rate]] from over 85% to below 15% across multiple attack scenarios targeting generation tasks.
- Generation quality (perplexity, BLEU, human evaluation) preserved with less than 5% degradation on clean inputs, indicating minimal false intervention.
- Effective against toxic text generation, misinformation production, and data exfiltration attacks -- three distinct categories of generation-targeted backdoors.
- Defended against both explicit trigger attacks (word/phrase insertion) and more subtle instruction-level attacks in LLMs.
- Computational overhead approximately doubles inference time due to parallel reference model inference, though using a smaller reference model can reduce this to approximately 30% overhead.
- The token-level intervention approach means that even when a trigger is present, most tokens in the generation remain from the primary model, preserving coherence and style.

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
