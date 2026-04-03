---
title: "Information-Theoretic Limits on Blind Detection"
slug: "information-theoretic-detection-limits"
compiled: "2026-04-04T10:00:00"
---

# Information-Theoretic Limits on Blind Detection

A central aspiration in backdoor defense is *blind detection* — identifying that a model is backdoored without knowing the attack type, trigger pattern, or target behavior in advance. [[certified-defense]] provides formal guarantees, but these bounds hold only under strong assumptions about the attack model (e.g., bounded perturbation size, known poisoning ratio). [[spectral-signatures]] offers probabilistic detection guarantees by identifying statistical anomalies in representation space, but its effectiveness degrades against attacks specifically designed to minimize spectral distinguishability. The deeper question is whether there exist fundamental information-theoretic limits on what any blind detector can achieve.

An analogy to Rice's theorem from computability theory is instructive: just as it is undecidable to determine arbitrary semantic properties of programs from their source code alone, it may be impossible to determine arbitrary behavioral properties of neural networks from their weights alone. A backdoored model and a clean model may be indistinguishable on any polynomial-sized test set if the trigger is sufficiently rare and the backdoor behavior is confined to a negligible fraction of the input space. This connects to [[certified-vs-empirical-gap]] — certified defenses provide guarantees only within their assumed threat model, while empirical defenses offer no guarantees at all.

[[backdoor-evaluation-methodology]] highlights a related challenge: without a comprehensive attack taxonomy, we cannot even define what "blind" detection means operationally. Every detector implicitly assumes a family of attacks, and adversaries can always step outside that family. This suggests that truly universal blind detection is not a matter of building better algorithms but may face principled impossibility results.

## Key Insight

The gap between certified and empirical detection is not just an engineering shortcoming — it may reflect a fundamental asymmetry. Attackers can always embed backdoors in model subspaces that a given detector does not examine, and the space of possible backdoor encodings is combinatorially vast. Any fixed detection strategy covers only a subspace of possible attacks, leaving a residual that adversaries can exploit. This is not unlike the halting problem: a universal backdoor detector would need to reason about all possible input-output mappings of a model, which is computationally intractable for models of practical size. The implication is that defense must be layered and attack-aware rather than relying on any single blind detection method.

## Implications

- Claims of "universal" backdoor detection should be scrutinized for implicit assumptions about the attack space
- Defense-in-depth strategies combining multiple detection methods with different coverage are more principled than searching for a single silver bullet
- [[certified-defense]] bounds are valuable precisely because they make their assumptions explicit, even when those assumptions are restrictive
- The field may need to shift from seeking universal detectors to characterizing *which* attack families are detectable under *which* assumptions

## Open Questions

- Can we formalize a no-free-lunch theorem for backdoor detection, proving that no single method can detect all attacks above a certain complexity threshold?
- What is the minimum amount of side information (e.g., clean reference data, partial trigger knowledge) needed to make detection tractable for a given attack family?
- Are there natural attack complexity classes analogous to computational complexity, where detection difficulty can be formally stratified?
