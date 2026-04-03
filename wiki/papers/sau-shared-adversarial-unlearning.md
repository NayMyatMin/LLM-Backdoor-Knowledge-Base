---
title: "Shared Adversarial Unlearning: Backdoor Mitigation by Unlearning Shared Adversarial Examples"
source: "raw/sau-shared-adversarial-unlearning.md"
venue: "NeurIPS"
year: 2023
summary: "Generates shared adversarial examples as trigger proxies and uses adversarial unlearning to remove backdoors without trigger reverse-engineering."
compiled: "2026-04-03T14:00:00"
---

# SAU: Shared Adversarial Unlearning

**Authors:** Shaokui Wei, Mingda Zhang, Hongyuan Zha, Baoyuan Wu
**Venue:** NeurIPS 2023
**URL:** https://arxiv.org/abs/2305.09464

## Summary

SAU proposes a [[backdoor-defense]] based on [[adversarial-unlearning]] that generates shared adversarial examples (SAEs) as proxies for unknown backdoor triggers, then unlearns the model's reliance on these perturbations. The key insight is that adversarial examples crafted to universally flip predictions share functional similarities with [[trigger-pattern]] -- both exploit learned shortcuts. By training the model to be invariant to these shared perturbations, SAU effectively removes backdoor behavior.

Unlike [[neural-cleanse]] and other methods requiring trigger reverse-engineering, SAU sidesteps this entirely, using universal adversarial perturbations as efficient proxies. The two-stage process of generating shared adversarial examples and then unlearning is iterated for progressive backdoor removal.

## Key Concepts

- [[backdoor-defense]]
- [[adversarial-unlearning]]
- [[backdoor-attack]]
- [[trigger-pattern]]
- [[attack-success-rate]]

## Method Details

**Stage 1 -- Shared Adversarial Example Generation:** A universal adversarial perturbation delta is crafted over a small clean set to maximize: sum_i L(f(x_i + delta), y_i), subject to ||delta|| <= epsilon. This perturbation is "shared" because it is optimized to flip predictions across all samples simultaneously.

**Stage 2 -- Adversarial Unlearning:** The model is fine-tuned for invariance to the perturbation: L_clean(f(x), y) + lambda * L_unlearn(f(x + delta), f(x)), where L_unlearn uses KL-divergence to align perturbed and clean output distributions.

**Iterative Refinement:** Stages alternate: new SAEs are generated for the updated model, followed by further unlearning. This progressively removes backdoor shortcuts.

Only 1-5% of training data as clean samples is required. The perturbation budget epsilon covers common trigger magnitudes.

## Results & Findings

- Reduces [[attack-success-rate]] to below 3% across 12 attacks including BadNets, Blended, WaNet, Input-Aware, and LIRA.
- Clean accuracy degradation under 1.5% on CIFAR-10 and under 2% on Tiny ImageNet.
- Outperforms Fine-Pruning, [[neural-cleanse]], [[adversarial-neuron-pruning]], and [[i-bau]].
- Robust against adaptive attacks.
- Defense completes in under 10 minutes on standard GPU hardware.

## Relevance to LLM Backdoor Defense

SAU's approach of using universal adversarial perturbations as trigger proxies translates naturally to the language domain, where adversarial token substitutions could serve as proxy triggers for unlearning backdoors in LLMs. The [[adversarial-unlearning]] framework is directly applicable to text models during post-training mitigation.

## Related Work

- [[i-bau]] -- adversarial unlearning with implicit optimization
- [[anti-backdoor-learning]] -- training-time unlearning via gradient ascent
- [[neural-cleanse]] -- trigger reverse-engineering (avoided by SAU)
- [[adversarial-neuron-pruning]] -- pruning-based defense
- [[neural-polarizer]] -- feature purification defense (same research group)

## Backlinks

[[backdoor-defense]] | [[adversarial-unlearning]] | [[trigger-pattern]] | [[attack-success-rate]]
