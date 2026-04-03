---
title: "CBD: A Certified Backdoor Detector Based on Local Dominant Probability"
source: "raw/cbd-certified-backdoor-detector.md"
venue: "NeurIPS"
year: 2023
summary: "First backdoor detection method with provable guarantees, using local dominant probability analysis to certifiably detect any trigger below a given size bound."
compiled: "2026-04-03T14:00:00"
---

# CBD: Certified Backdoor Detector

**Authors:** Zhen Xiang, Zidi Xiong, Bo Li
**Venue:** NeurIPS 2023
**URL:** https://arxiv.org/abs/2310.11160

## Summary

CBD proposes the first [[backdoor-defense]] with provable detection guarantees, moving beyond empirical defenses that can be defeated by adaptive attacks. The method introduces local dominant probability (LDP) as a metric to distinguish clean and backdoored models. The theoretical framework proves that any [[trigger-pattern]] below a certain size must produce detectable LDP patterns, providing a [[certified-defense]] against backdoor attacks.

The detection leverages techniques from randomized smoothing, adapted from certified adversarial robustness to the backdoor detection context. Empirically, CBD matches or exceeds existing defenses while offering formal guarantees unavailable from prior methods.

## Key Concepts

- [[backdoor-defense]]
- [[certified-defense]]
- [[backdoor-attack]]
- [[trigger-pattern]]
- [[neural-cleanse]] (comparison baseline)

## Method Details

**Local Dominant Probability (LDP):** For input x and model f, LDP is the probability that f(x') = f(x) for x' sampled from a local ball around x. Clean models have moderate LDP (predictions change near decision boundaries), while backdoored models have abnormally high LDP for triggered inputs (the trigger creates a dominant signal).

**Certification:** The framework proves that if a backdoor trigger has L_p norm below threshold delta, the backdoored model's LDP must exceed a certifiable bound. Any class exhibiting LDP above this threshold guarantees the model is backdoored.

**Detection Procedure:** (1) Sample random inputs and local neighborhoods. (2) Compute empirical LDP per predicted class. (3) Compare observed LDP against certified threshold. (4) Flag model as backdoored if any class exceeds the threshold, identifying the target class.

**Randomized Smoothing Connection:** Certification leverages randomized smoothing techniques adapted from robustness certification to backdoor detection.

## Results & Findings

- Certifiably detects all triggers within the specified size bound.
- Empirically detects backdoors with >95% accuracy on CIFAR-10, GTSRB, and ImageNet subsets.
- Certified radius covers practically relevant trigger sizes (patches up to 5x5, blended triggers with alpha up to 0.1).
- False positive rate below 5%.
- Detection takes minutes per model on standard GPU hardware.
- Comparable or better empirical detection than [[neural-cleanse]], STRIP, and Spectral Signatures, with additional formal guarantees.

## Relevance to LLM Backdoor Defense

CBD demonstrates that [[certified-defense]] against backdoors is achievable, inspiring pursuit of provable guarantees for LLM backdoor detection. While the specific LDP formulation targets image classifiers, the principle of certifiable detection based on local prediction consistency could be adapted for token-level or embedding-level analysis in language models.

## Related Work

- [[neural-cleanse]] -- empirical trigger reverse-engineering
- [[spectre]] -- robust statistics-based detection
- [[k-arm]] -- optimization-based backdoor scanning
- [[anti-backdoor-learning]] -- training-time defense
- [[revisiting-latent-separability]] -- latent space analysis for defense

## Backlinks

[[backdoor-defense]] | [[certified-defense]] | [[backdoor-attack]] | [[trigger-pattern]] | [[neural-cleanse]]
