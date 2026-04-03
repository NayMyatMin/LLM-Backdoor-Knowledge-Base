---
title: "Composing Defenses: Synergy or Interference?"
slug: "defense-composition"
compiled: "2026-04-04T10:00:00"
---

# Composing Defenses: Synergy or Interference?

## Connection

The backdoor defense literature evaluates methods in isolation: each paper proposes one defense, tests it against a fixed set of attacks, and reports clean accuracy and attack success rate. But real deployment demands defense composition — running multiple defenses together across the training, post-training, and inference stages. The fundamental question, almost entirely unstudied, is whether composing defenses produces synergy (combined robustness exceeds individual parts) or interference (one defense undermines another's assumptions). The [[training-time-vs-post-hoc-defense]] distinction suggests a natural layering: apply [[activation-clustering]] or similar sanitization during training, follow with [[adversarial-neuron-pruning]] or [[fine-pruning]] after training, and add [[onion]] or [[strip]] at inference time. In principle, each layer catches what the previous one missed.

But interference is a real risk. [[fine-pruning]] removes neurons with low activation on clean data — but if a training-time defense like [[activation-clustering]] has already filtered most poisoned samples, the remaining backdoor signal may be too faint for pruning to identify the right neurons. Conversely, aggressive pruning might remove neurons that an inference-time defense like [[strip]] relies on for its perturbation-sensitivity signal. The interaction between [[backdoor-defense]] methods is not simply additive; each defense reshapes the model's internal landscape in ways that may help or hinder subsequent defenses.

## Key Insight

The core problem is that defenses lack composability guarantees. In software engineering, composable components have well-defined interfaces and contracts. Backdoor defenses have neither — they make implicit assumptions about what the model's representation space looks like, and each defense transforms that space. Training-time sanitization changes the data distribution; post-hoc pruning/unlearning changes the weight space; inference-time filtering changes the effective input distribution. Without understanding how these transformations interact, practitioners are flying blind when stacking defenses. The field needs a compositional framework that characterizes each defense's preconditions and postconditions on the model's representation space.

## Implications

- Evaluation benchmarks should include defense composition experiments, not just individual defense performance
- The order of defense application likely matters: sanitize-then-prune may differ substantially from prune-then-sanitize
- Diminishing returns are probable — three defenses may not be three times as robust as one, especially if they rely on the same underlying signal (e.g., representation-space separation)
- [[certified-defense]] approaches could provide composability guarantees that empirical methods cannot
- Practitioners deploying models need guidance on which defense combinations are complementary vs. redundant

## Open Questions

- Does composing defenses from different categories (statistical, pruning-based, behavioral) produce more synergy than composing within a category?
- Can the interference problem be formalized — defining when one defense's transformation breaks another's detection criterion?
- What is the minimal effective defense stack for a given threat model?
