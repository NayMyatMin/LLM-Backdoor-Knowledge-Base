---
title: "RAP: Robustness-Aware Perturbations for Defending Against Backdoor Attacks in NLP"
source: raw/rap-robustness-aware-perturbations-backdoor.md
venue: EMNLP
year: 2021
summary: "RAP exploits the observation that poisoned inputs are more robust to perturbations than clean inputs, learning a universal perturbation token that differentially affects clean vs. poisoned samples to enable test-time backdoor detection."
compiled: "2026-04-03T14:00:00"
---

# RAP: Robustness-Aware Perturbations for Defending Against Backdoor Attacks in NLP

## Summary

RAP (Robustness-Aware Perturbations) is a test-time [[backdoor-defense]] that exploits an asymmetry in robustness between clean and poisoned inputs. Poisoned inputs containing [[trigger-pattern]] tokens are more robust to perturbations because the trigger provides a strong, dominant signal for the target class. RAP learns a universal perturbation token that, when prepended to inputs, causes clean inputs to change their predictions but leaves poisoned inputs relatively unaffected.

Detection is performed by measuring the change in output probability for the suspected target class before and after applying the perturbation. Inputs with small probability changes are flagged as poisoned. RAP achieves over 90% true positive rate with below 5% false positive rate across multiple attack types.

## Key Concepts

- [[backdoor-defense]]
- [[trigger-pattern]]
- [[attack-success-rate]]
- Robustness asymmetry
- Universal perturbation
- Test-time detection

## Method Details

1. **Perturbation learning**: A perturbation word/token is optimized on a small set of clean samples to maximally shift the model's output probability for the target class.
2. **Robustness asymmetry**: Clean inputs rely on distributed features that the perturbation can disrupt, so predictions change significantly. Poisoned inputs are dominated by the trigger signal, remaining robust to the perturbation.
3. **Detection**: Measure the change in output probability for the suspected target class before and after applying the perturbation. Inputs with small probability changes are flagged as poisoned.
4. **Threshold calibration**: A threshold on probability change is calibrated using clean validation samples.

The method requires knowledge of the suspected target class but does not require access to poisoned training data.

## Results & Findings

- Over 90% true positive rate for poisoned sample detection across multiple attack types including BadNL insertion and style-transfer attacks.
- False positive rates below 5% on clean samples.
- Effective on SST-2, toxic comment detection, and AG News tasks.
- Outperformed [[onion]] and other baseline defenses on attacks with less obvious trigger patterns.
- Relatively insensitive to perturbation initialization choice.

## Relevance to LLM Backdoor Defense

RAP's insight about robustness asymmetry between clean and triggered inputs is a fundamental property that extends to LLM settings. The approach of using learned perturbations to differentiate backdoored behavior provides a principled detection mechanism that could be adapted for instruction-tuned LLMs and generative models.

## Related Work

- [[onion]] -- perplexity-based defense that RAP outperforms on some attacks
- [[denoised-poe-defense]] -- related test-time defense leveraging model behavior differences
- [[proactive-detection]] -- another proactive detection approach

## Backlinks

[[backdoor-defense]] | [[trigger-pattern]] | [[attack-success-rate]]
