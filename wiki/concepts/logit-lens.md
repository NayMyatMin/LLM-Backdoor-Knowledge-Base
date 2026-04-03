---
title: "Logit Lens"
slug: "logit-lens"
brief: "A technique for interpreting intermediate transformer representations by applying the final unembedding matrix to hidden states at each layer, revealing how the model's next-token predictions evolve through the network — the simplest form of layer-wise prediction tracking."
compiled: "2026-04-03T22:00:00"
---

# Logit Lens

## Definition

The logit lens is an interpretability technique that "reads" what a transformer is predicting at intermediate layers by applying the model's final unembedding matrix to hidden states before they have passed through all layers. For a model with L layers, the logit lens at layer l computes: logits_l = W_U * h_l, where W_U is the unembedding matrix and h_l is the hidden state at layer l. This produces a vocabulary distribution at each layer, revealing how the model's prediction evolves from early to late layers.

## Background

The technique was introduced informally by nostalgebraist in a 2020 blog post analyzing GPT-2, and quickly became a standard tool in the interpretability community. The core insight is that in transformers, the residual stream maintains a running sum that is eventually decoded by the unembedding matrix. If intermediate states are already partially "in the right format," the unembedding matrix can extract meaningful predictions even at early layers.

The [[tuned-lens]] (Belrose et al., 2023) improved on the logit lens by training layer-specific affine probes to account for representational drift — the fact that features may be encoded differently at different layers. While the logit lens is free (no training needed), it is often unreliable at early layers where representations have not yet converged to the final format.

## Technical Details

### Method

For each layer l in a transformer with L layers:
1. Extract the residual stream hidden state h_l after layer l's computation
2. Apply the final unembedding matrix: logits_l = W_U * h_l
3. Convert to a probability distribution: p_l = softmax(logits_l)
4. Compare p_l to the final distribution p_L to see how predictions refine

### Prediction Trajectory

The sequence of distributions {p_0, p_1, ..., p_L} forms a "prediction trajectory" showing how the model progressively builds its output. Typical patterns:
- Early layers: near-uniform or frequency-based distributions
- Middle layers: semantic narrowing as context is integrated
- Late layers: sharp, confident predictions

### Limitations

- **Representational drift**: Early layers may encode features in a different basis than the final layer, causing the logit lens to produce nonsensical distributions
- **Nonlinear features**: If features are encoded nonlinearly at intermediate layers, linear decoding fails
- **Layer normalization**: Some architectures apply layer norm before the unembedding, which intermediate states have not yet undergone

## Variants

- **Raw logit lens**: Apply W_U directly (original technique)
- **[[tuned-lens]]**: Train affine probes per layer for more accurate decoding
- **Attention lens**: Analyze attention patterns rather than hidden states
- **Feature lens**: Apply SAE decomposition at each layer, then decode features

## Key Papers

- [[tuned-lens]] — the improved, trainable version addressing representational drift

## Relevance to Backdoor Defense

The logit lens and its variants offer layer-wise monitoring for backdoor detection:

- **Prediction trajectory anomalies**: A backdoor trigger that causes the model to suddenly redirect its prediction at a specific layer would appear as a discontinuity in the prediction trajectory. Clean inputs show smooth convergence; triggered inputs may show abrupt shifts at the layer where the backdoor circuit activates.

- **Backdoor injection point localization**: By tracking when the target output first appears in the prediction trajectory, defenders can identify the layer where the backdoor circuit injects its influence — the "injection point" of the trigger-to-target mapping.

- **Runtime detection**: The logit lens is computationally cheap (one matrix multiplication per layer), making it feasible for runtime monitoring. Anomalous prediction trajectories can flag potentially triggered inputs without expensive post-hoc analysis.

- **Connection to representation velocity**: Representation velocity measures the L2 norm of hidden-state differences between layers. The logit lens provides a complementary view in prediction space: how the *decoded prediction* changes between layers. Both capture layer-wise dynamics but in different spaces (activation vs. vocabulary).

- **Comparison with input-level detectors**: Unlike [[strip]] or [[onion]], which analyze input perturbations, the logit lens monitors internal computation, potentially detecting triggers that are input-level imperceptible but create internal anomalies.

## Related Concepts

- [[tuned-lens]] — the improved version with per-layer probes
- [[probing-classifier]] — the logit lens is a zero-shot probe using the unembedding matrix
- [[mechanistic-interpretability]] — the logit lens is a standard tool in the mech interp toolkit
- [[activation-analysis]] — the logit lens provides a prediction-space view of internal activations
- [[representation-engineering]] — RepE works in activation space; the logit lens works in prediction space

## Open Problems

- **Reliability at early layers**: The raw logit lens is unreliable at early layers; even the tuned lens has limitations
- **Beyond next-token prediction**: Can the logit lens track other properties beyond the immediate next token?
- **Backdoor trajectory characterization**: No systematic study has characterized what backdoor-induced prediction trajectories look like across different attack types
- **Computational cost at scale**: While cheap per layer, running across all layers of a 100B+ model at every token adds latency
