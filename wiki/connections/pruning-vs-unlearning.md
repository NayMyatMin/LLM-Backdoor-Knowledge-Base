---
title: "Pruning vs. Unlearning: Competing Paradigms for Backdoor Removal"
slug: "pruning-vs-unlearning"
compiled: "2026-04-03T12:00:00"
---

# Pruning vs. Unlearning: Competing Paradigms for Backdoor Removal

## Connection

Two dominant strategies for removing backdoors from trained models have emerged independently: [[neuron-pruning-defense]] (surgically remove neurons that carry the backdoor) and [[adversarial-unlearning]] (retrain the model to forget the backdoor behavior). These paradigms rest on fundamentally different assumptions about how backdoors are encoded in neural networks.

## Key Observations

- **Pruning assumes locality**: [[fine-pruning]], [[adversarial-neuron-pruning]], and [[reconstructive-neuron-pruning]] all rely on the premise that backdoor behavior concentrates in identifiable neurons. When this holds, pruning is surgical and preserves clean accuracy well.
- **Unlearning assumes distributedness**: [[i-bau]], [[sau-shared-adversarial-unlearning]], and [[beear]] optimize against the backdoor objective directly, handling cases where backdoor knowledge is spread across many parameters rather than isolated in a few neurons.
- **Pruning breaks on distributed backdoors**: Attacks like [[composite-backdoor-attacks]] and advanced [[dynamic-trigger]] patterns spread activation across the network, leaving no single neuron to prune. This is pruning's fundamental blind spot.
- **Unlearning risks over-correction**: Adversarial unlearning methods can degrade clean performance if the unlearning signal overlaps with legitimate task knowledge. [[sau-shared-adversarial-unlearning]] addresses this with shared adversarial examples, but the tension remains.
- **Hybrid approaches are emerging**: [[reconstructive-neuron-pruning]] bridges the gap — it prunes neurons but then reconstructs model capacity via unlearning-like fine-tuning, suggesting the paradigms are complementary rather than strictly competing.

## Implications

The choice between pruning and unlearning is fundamentally a bet on backdoor structure. As attacks grow more sophisticated, purely localized backdoors become rarer, favoring unlearning approaches. However, pruning remains attractive for its interpretability — you can inspect which neurons were removed. The field may converge on hybrid methods that prune candidate neurons and then fine-tune to recover, combining the strengths of both paradigms.

## Related Papers

- [[fine-pruning]], [[adversarial-neuron-pruning]], [[reconstructive-neuron-pruning]] — Pruning-based defenses
- [[i-bau]], [[sau-shared-adversarial-unlearning]], [[beear]] — Unlearning-based defenses
- [[anti-backdoor-learning]] — Training-time alternative to both

## Related Concepts

- [[neuron-pruning-defense]]
- [[adversarial-unlearning]]
- [[backdoor-defense]]
- [[defense-arms-race]]
