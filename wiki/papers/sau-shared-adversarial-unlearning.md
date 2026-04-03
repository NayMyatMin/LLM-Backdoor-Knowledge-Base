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

**Stage 1 -- Shared Adversarial Example Generation:** A universal adversarial perturbation delta is crafted over a small clean set to maximize: sum_i L(f(x_i + delta), y_i), subject to ||delta|| <= epsilon. This perturbation is "shared" because it is optimized to flip predictions across all clean samples simultaneously, analogous to how a [[trigger-pattern]] universally causes misclassification. The shared adversarial perturbations have been shown to exhibit visual and functional similarity to actual backdoor triggers, validating the theoretical motivation.

**Stage 2 -- Adversarial Unlearning:** The model is fine-tuned for invariance to the perturbation: L_clean(f(x), y) + lambda * L_unlearn(f(x + delta), f(x)), where L_unlearn uses KL-divergence to align perturbed and clean output distributions. This teaches the model to ignore the shortcut patterns exploited by both the adversarial perturbation and the actual backdoor trigger.

**Iterative Refinement:** Stages alternate: new SAEs are generated for the updated model, followed by further unlearning. This progressive approach is important because a single round may not fully remove deeply embedded backdoor shortcuts, but iterative refinement converges to a clean model.

Only 1-5% of training data as clean samples is required. The perturbation budget epsilon is set to cover common trigger magnitudes encountered in standard backdoor attacks.

## Results & Findings

- Reduces [[attack-success-rate]] to below 3% on average across 12 different attacks including BadNets, Blended, WaNet, Input-Aware, LIRA, and others--one of the most comprehensive evaluations in the backdoor defense literature.
- Clean accuracy degradation under 1.5% on CIFAR-10 and under 2% on Tiny ImageNet, demonstrating excellent utility preservation.
- Outperforms existing defenses including Fine-Pruning, [[neural-cleanse]], [[adversarial-neuron-pruning]], and [[i-bau]] on comprehensive benchmarks.
- Robust against adaptive attacks where the attacker is aware of the SAU defense mechanism.
- Computationally efficient: defense completes in under 10 minutes on standard GPU hardware, making it practical for deployment.

## Relevance to LLM Backdoor Defense

SAU's approach of using universal adversarial perturbations as trigger proxies translates naturally to the language domain, where adversarial token substitutions could serve as proxy triggers for unlearning backdoors in LLMs. The [[adversarial-unlearning]] framework is directly applicable to text models during post-training mitigation. The key advantage over methods like [[neural-cleanse]] is that SAU does not require reverse-engineering the exact trigger, which is particularly valuable for LLMs where the trigger space (token sequences, formatting patterns, instruction phrasing) is vast and difficult to enumerate. SAU was developed by the same research group behind [[neural-polarizer]] and [[proactive-defensive-backdoor]], forming a coherent line of work on efficient post-hoc backdoor removal.

## Related Work

- [[i-bau]] -- adversarial unlearning with implicit optimization
- [[anti-backdoor-learning]] -- training-time unlearning via gradient ascent
- [[neural-cleanse]] -- trigger reverse-engineering (avoided by SAU)
- [[adversarial-neuron-pruning]] -- pruning-based defense
- [[neural-polarizer]] -- feature purification defense (same research group)

## Backlinks

[[backdoor-defense]] | [[adversarial-unlearning]] | [[trigger-pattern]] | [[attack-success-rate]]
