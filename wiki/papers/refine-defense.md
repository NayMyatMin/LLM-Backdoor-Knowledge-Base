---
title: "REFINE: Inversion-Free Backdoor Defense via Model Reprogramming"
source: raw/refine-inversion-free-backdoor-defense-model-reprogramming.md
venue: ICLR
year: 2025
summary: "REFINE proposes a backdoor defense that avoids trigger inversion by using model reprogramming -- a learnable input transformation that disrupts trigger patterns while preserving clean-task features, achieving strong defense without needing to know the trigger."
compiled: "2026-04-03T14:00:00"
---

# REFINE: Inversion-Free Backdoor Defense via Model Reprogramming

**Authors:** Yukun Chen, Shuo Shao, Enhao Huang, Yiming Li, Pin-Yu Chen, Zhan Qin, Kui Ren
**Venue:** ICLR 2025
**URL:** https://arxiv.org/abs/2502.18508

## Summary

REFINE addresses a key limitation of existing [[backdoor-defense]] methods: the reliance on expensive and often unreliable trigger inversion (reverse-engineering). Many defenses such as [[neural-cleanse]] attempt to reconstruct the [[trigger-pattern]] before neutralizing it, but this fails for complex triggers like warping, frequency-domain, or dynamic patterns.

Instead, REFINE leverages model reprogramming -- a technique that adds a learnable input transformation to repurpose a model -- to neutralize backdoor behavior. The reprogramming layer transforms inputs so that local trigger patterns are disrupted while global semantic features needed for classification are preserved. This makes the [[trigger-pattern]] effectively invisible to the model without needing to know what the trigger looks like.

The method achieves below 5% [[attack-success-rate]] across diverse attack types with less than 2% clean accuracy degradation, requiring only 500-1000 clean samples and under 10 minutes of training.

## Key Concepts

- [[backdoor-defense]]
- [[trigger-pattern]]
- [[neural-cleanse]]
- [[attack-success-rate]]
- Model reprogramming
- Inversion-free defense

## Method Details

REFINE prepends a learnable reprogramming layer R to the potentially backdoored model f. The prediction becomes y = f(R(x; phi)), where phi are the reprogramming parameters optimized on a small clean dataset.

The training objective maximizes clean accuracy while disrupting trigger patterns through regularization that promotes smoothing of local input patterns. Three reprogramming function designs are explored:

- **Additive**: R(x; phi) = x + delta(phi), adding a learnable perturbation.
- **Multiplicative**: R(x; phi) = x * mask(phi) + bias(phi), providing channel-wise modulation.
- **Convolutional**: R(x; phi) = Conv(x; phi), applying a learnable convolutional filter.

Convolutional reprogramming provides the best balance. The implicit trigger disruption works because the layer preserves global semantic features while disrupting local patterns (which triggers typically are), applying a consistent transformation so the model cannot distinguish triggered from clean inputs.

## Results & Findings

- Reduces [[attack-success-rate]] below 5% across BadNets, Blended, WaNet, Input-Aware, and frequency-domain attacks on CIFAR-10, GTSRB, and Tiny ImageNet.
- Clean accuracy degradation under 2%.
- Outperforms inversion-based defenses ([[neural-cleanse]], I-BAU) on complex triggers where inversion typically fails.
- Negligible inference overhead (~1ms per image).
- Robust to different trigger sizes, locations, and types without hyperparameter tuning.

## Relevance to LLM Backdoor Defense

REFINE's inversion-free philosophy is highly relevant for LLM settings where trigger inversion is even more challenging due to the discrete, high-dimensional nature of text. The principle of applying a universal input transformation to disrupt unknown triggers could inspire analogous defenses for text models, such as learnable input preprocessing layers that neutralize textual triggers without needing to reconstruct them.

## Related Work

- [[neural-cleanse]] -- trigger inversion defense that REFINE aims to improve upon
- [[badacts]] -- activation-space defense, alternative inversion-free approach
- [[beear]] -- embedding-level defense for LLMs

## Backlinks

[[backdoor-defense]] | [[trigger-pattern]] | [[neural-cleanse]] | [[attack-success-rate]]
