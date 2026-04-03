---
title: "How Much Clean Data Removes How Much Backdoor?"
slug: "fine-tuning-recovery-bounds"
compiled: "2026-04-04T10:00:00"
---

# How Much Clean Data Removes How Much Backdoor?

A recurring question across backdoor defense research is whether a predictable relationship exists between the poisoning ratio used during attack and the volume of clean fine-tuning data needed to neutralize it. Intuitively, one might expect a simple inverse relationship: more poison requires more antidote. But the empirical evidence paints a far more complex picture. [[fine-pruning]] demonstrated early on that fine-tuning alone is insufficient for backdoor removal, as backdoor-associated neurons can be disentangled from task-critical neurons. The attack side has internalized this lesson — [[weight-poisoning-pretrained]]'s RIPPLe method explicitly optimizes backdoor weights to be resilient against fine-tuning by embedding the backdoor in directions that clean fine-tuning reinforces rather than erases.

The persistence of backdoors through fine-tuning varies dramatically by attack sophistication. Simple data poisoning attacks may degrade after a few epochs of clean training, but advanced methods like [[badedit]] survive 5 full epochs of fine-tuning by editing model weights along directions orthogonal to the clean task manifold. This suggests the relationship between poisoning ratio and required clean data is not merely quantitative but depends on the geometric relationship between backdoor and task representations in weight space.

This tension sits at the heart of [[fine-tuning-dual-use]]: the same fine-tuning process that adapts models to downstream tasks could theoretically remove backdoors, yet attackers specifically design against this. [[certified-defense]] attempts to provide formal guarantees about removal, but these bounds typically assume constrained attack models that sophisticated methods violate. The gap between certified bounds and empirical attack resilience suggests we lack a unified theoretical framework for fine-tuning-based recovery.

## Key Insight

The relationship between poisoning ratio and clean data requirements is not a simple function — it is mediated by the *geometric alignment* between backdoor parameters and task-relevant parameters. When backdoors are embedded orthogonally to the clean task subspace (as in [[badedit]]), arbitrary amounts of clean fine-tuning may be insufficient because gradient updates simply do not reach the backdoor dimensions. When backdoors are deliberately aligned with task-relevant directions (as in [[weight-poisoning-pretrained]]), fine-tuning actually reinforces the backdoor. This means the critical variable is not data volume but the angular relationship in parameter space, a quantity that defenders cannot easily measure or control.

## Implications

- Simple "fine-tune with clean data" prescriptions for backdoor removal are unreliable without understanding the attack geometry
- Poisoning ratio alone is a poor predictor of removal difficulty; attack method matters more than attack scale
- [[certified-defense]] bounds need to incorporate attack-specific geometric constraints to be practically useful
- Defenders may need to combine fine-tuning with explicit subspace identification methods to target backdoor dimensions directly

## Open Questions

- Can we derive tight bounds on fine-tuning recovery as a function of both poisoning ratio and the angle between backdoor and task subspaces?
- Is there a minimum clean dataset size that guarantees removal for *any* attack within a realistic threat model, or do some attacks make fine-tuning recovery provably impossible?
- Could adaptive fine-tuning strategies that explore multiple subspace directions overcome orthogonal backdoor embeddings?
