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

**Local Dominant Probability (LDP):** For input x and model f, the LDP is defined as LDP(f, x) = Pr[f(x') = f(x)] for x' sampled uniformly from a local L_p ball of radius epsilon around x. Clean models have moderate LDP because predictions naturally change near decision boundaries, reflecting distributed feature reliance. Backdoored models have abnormally high LDP for inputs containing the trigger, because the trigger creates a dominant shortcut signal that overwhelms local perturbations.

**Certification:** The theoretical framework proves that if a backdoor trigger has L_p norm below threshold delta, then the backdoored model's per-class LDP must exceed a certifiable lower bound that is strictly higher than what clean models produce. This creates a provable separation: any class exhibiting LDP above the certified threshold guarantees the model is backdoored for that target class. The certification radius covers practically relevant trigger sizes including patches up to 5x5 pixels and blended triggers with alpha up to 0.1.

**Detection Procedure:** (1) Sample random inputs and compute predictions across their local neighborhoods using Gaussian noise perturbations. (2) Compute empirical LDP per predicted class by measuring prediction consistency rates. (3) Compare the observed LDP against the certified threshold derived from the theoretical bound. (4) Flag the model as backdoored if any class exceeds the threshold, simultaneously identifying the target class.

**Randomized Smoothing Connection:** The certification adapts randomized smoothing from the adversarial robustness literature. Just as randomized smoothing certifies that predictions are stable within a radius, CBD uses the same mathematical framework to certify that backdoor triggers must produce detectable LDP signatures, transforming a robustness tool into a security auditing tool.

## Results & Findings

- Certifiably detects all triggers within the specified size bound.
- Empirically detects backdoors with >95% accuracy on CIFAR-10, GTSRB, and ImageNet subsets.
- Certified radius covers practically relevant trigger sizes (patches up to 5x5, blended triggers with alpha up to 0.1).
- False positive rate below 5%.
- Detection takes minutes per model on standard GPU hardware.
- Comparable or better empirical detection than [[neural-cleanse]], STRIP, and Spectral Signatures, with additional formal guarantees.

## Relevance to LLM Backdoor Defense

CBD demonstrates that [[certified-defense]] against backdoors is achievable, inspiring pursuit of provable guarantees for LLM backdoor detection. While the specific LDP formulation targets image classifiers, the principle of certifiable detection based on local prediction consistency could be adapted for token-level or embedding-level analysis in language models. The gap between certified and empirical defenses (see [[certified-vs-empirical-gap]]) remains an active research area: certified methods like CBD provide formal guarantees but typically cover smaller trigger spaces than what adaptive attackers can exploit. Extending certification to the generative setting of LLMs (see [[classification-to-generation-defense-gap]]) presents additional challenges around defining what constitutes a "dominant prediction" in open-ended text generation.

## Related Work

- [[neural-cleanse]] -- empirical trigger reverse-engineering
- [[spectre]] -- robust statistics-based detection
- [[k-arm]] -- optimization-based backdoor scanning
- [[anti-backdoor-learning]] -- training-time defense
- [[revisiting-latent-separability]] -- latent space analysis for defense

## Backlinks


- [[certified-vs-empirical-gap]]
- [[classification-to-generation-defense-gap]]
[[backdoor-defense]] | [[certified-defense]] | [[backdoor-attack]] | [[trigger-pattern]] | [[neural-cleanse]]
