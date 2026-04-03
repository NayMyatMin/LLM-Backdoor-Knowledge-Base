---
title: "Scaling Defenses to Frontier Models"
slug: "defense-scalability-frontier"
compiled: "2026-04-04T10:00:00"
---

# Scaling Defenses to Frontier Models

## Connection

Nearly all published backdoor defenses are validated on models in the 3B-20B parameter range, yet deployment increasingly involves 70B-405B frontier models. This creates a critical gap: the defenses the community trusts have never been tested where they matter most. Three families of defense face distinct scaling challenges. [[neuron-pruning-defense|Neuron pruning]] and [[activation-analysis]] assume individual neurons carry interpretable, localizable signals — but [[superposition]] theory predicts that larger models pack more features per dimension, making per-neuron methods less reliable at scale. [[spectral-signatures]] and [[activation-clustering]] depend on clean/poisoned samples being linearly separable in activation space, and whether this separation persists as representational capacity explodes is unknown. Circuit-level methods like [[backdoor-circuits]] analysis and [[mechanistic-interpretability]] are computationally expensive even at small scale — tracing circuits through a 405B model is orders of magnitude harder.

Knowledge-localization approaches face a particularly interesting scaling question. [[rome-factual-associations]] demonstrated that factual associations concentrate in mid-layer MLP modules at moderate scale. If this localization property holds at 70B+, it suggests backdoor knowledge might also remain localized and surgically removable. But if larger models distribute knowledge more diffusely (as some evidence from scaling laws suggests), then targeted editing and pruning strategies lose their foundation. The answer determines whether [[knowledge-localization]] remains a viable defense principle at frontier scale.

## Key Insight

The core tension is that larger models have both more capacity to hide backdoors (more parameters, deeper superposition, more distributed representations) and are simultaneously more expensive to analyze exhaustively. This creates an asymmetry favoring attackers: poisoning a 405B model during pretraining costs no more than training it, but defending it requires methods whose computational cost may scale superlinearly with parameters. Lightweight statistical methods ([[spectral-signatures]], [[activation-clustering]]) may be the only affordable option — but they are also the most likely to break as representations become richer and more entangled.

## Implications

- [[mechanistic-interpretability]] tools must become dramatically more efficient (sparse probing, sampling-based circuit discovery) to remain viable at frontier scale
- [[neuron-pruning-defense]] may need to shift from individual neurons to subspace-level pruning as [[superposition]] intensifies
- Empirical validation on 70B+ models is urgently needed — current defense papers' claims do not safely extrapolate
- The field may bifurcate into "affordable but approximate" defenses (statistical) and "thorough but expensive" defenses (mechanistic), with different use cases for each

## Open Questions

- Does the fraction of neurons involved in a backdoor circuit shrink, stay constant, or grow as model size increases?
- Can sparse autoencoders scale to frontier models efficiently enough to resolve superposition before applying detection?
- Is there a critical model size beyond which current spectral methods lose their separation guarantees?
