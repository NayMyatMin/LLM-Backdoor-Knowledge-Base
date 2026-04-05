---
title: "RAP: Robustness-Aware Perturbations for Defending Against Backdoor Attacks in NLP"
source: raw/rap-robustness-aware-perturbations-backdoor.md
venue: EMNLP
year: 2021
summary: "RAP exploits the observation that poisoned inputs are more robust to perturbations than clean inputs, learning a universal perturbation token that differentially affects clean vs. poisoned samples to enable test-time backdoor detection."
tags:
  - defense
  - trigger-inversion
threat_model:
  - data-poisoning
compiled: "2026-04-03T14:00:00"
---

# RAP: Robustness-Aware Perturbations for Defending Against Backdoor Attacks in NLP

**Authors:** Wenkai Yang, Yankai Lin, Peng Li, Jie Zhou, Xu Sun
**Venue:** EMNLP 2021
**URL:** https://arxiv.org/abs/2110.07831

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

1. **Perturbation learning**: A perturbation word/token is optimized on a small set of clean samples to maximally shift the model's output probability for the suspected target class. The perturbation token is prepended to all test inputs during detection. Optimization minimizes the target-class probability on clean samples, effectively learning a token that disrupts clean predictions for that class.
2. **Robustness asymmetry**: Clean inputs rely on distributed features across the input that the perturbation can disrupt, so predictions change significantly when the perturbation is applied. Poisoned inputs are dominated by the trigger signal, which provides a strong shortcut to the target class that remains robust to the added perturbation token.
3. **Detection metric**: For each test input, RAP computes delta_p = P(y_target | x) - P(y_target | [perturbation] + x), the change in output probability for the suspected target class before and after prepending the perturbation. Clean inputs exhibit large delta_p (prediction shifts), while poisoned inputs show small delta_p (prediction stays anchored by the trigger).
4. **Threshold calibration**: A threshold on delta_p is calibrated using clean validation samples to achieve the desired false positive rate, typically set at the 5th percentile of the clean delta_p distribution.

The method requires knowledge of the suspected target class but does not require access to poisoned training data. It is also relatively insensitive to the initialization of the perturbation token, making it practical for deployment.

## Results & Findings

- Over 90% true positive rate for poisoned sample detection across multiple attack types including BadNL insertion attacks and style-transfer attacks.
- False positive rates below 5% on clean samples, demonstrating precise discrimination between clean and poisoned inputs.
- Effective on sentiment analysis (SST-2), toxic comment detection, and news topic classification (AG News) tasks, covering both binary and multi-class settings.
- Outperformed [[onion]] and other baseline defenses particularly on attacks with less obvious trigger patterns, where perplexity-based methods struggle because the triggers do not produce clear outlier signals.
- Relatively insensitive to perturbation initialization choice, meaning the method does not require careful seed selection.
- The learned perturbation tokens are task-specific but attack-agnostic -- the same perturbation detects multiple attack types for a given model and target class.

## Relevance to LLM Backdoor Defense

RAP's insight about robustness asymmetry between clean and triggered inputs is a fundamental property that extends to LLM settings. The approach of using learned perturbations to differentiate backdoored behavior provides a principled detection mechanism that could be adapted for instruction-tuned LLMs and generative models. In contrast to [[onion]]'s input-cleaning approach, RAP performs detection without modifying the input, preserving original semantics while flagging suspicious samples. The robustness asymmetry principle has influenced subsequent defense research and connects to broader observations about how [[trigger-pattern]] signals create dominant decision shortcuts in neural networks.

## Related Work

- [[onion]] -- perplexity-based defense that RAP outperforms on some attacks
- [[denoised-poe-defense]] -- related test-time defense leveraging model behavior differences
- [[proactive-detection]] -- another proactive detection approach

## Backlinks

[[backdoor-defense]] | [[trigger-pattern]] | [[attack-success-rate]]
