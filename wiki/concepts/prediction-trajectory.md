---
title: "Prediction Trajectory"
slug: "prediction-trajectory"
brief: "The sequence of intermediate predictions a model makes across its layers, revealing how representations evolve from early syntactic guesses to final semantic output."
compiled: "2026-04-04T10:00:00"
---

# Prediction Trajectory

## Definition

A prediction trajectory is the ordered sequence of intermediate output distributions (or decoded token predictions) that a language model produces at each layer of its transformer stack, tracing how the model's internal representation of an input evolves from shallow syntactic features in early layers to deep semantic meaning at the final layer. Anomalous deviations in this trajectory can serve as indicators of backdoor activation or other adversarial manipulation.

## Background

Modern large language models consist of dozens or hundreds of stacked transformer layers. Each layer incrementally refines the model's internal representation. Researchers discovered that by projecting intermediate hidden states into the vocabulary space — essentially asking "what would the model predict if it stopped processing here?" — one can observe a meaningful progression of predictions. Early layers tend to capture surface-level patterns such as token frequency and local syntax, while later layers resolve complex semantic dependencies, coreference, and factual recall.

This insight has profound implications for backdoor defense. A cleanly trained model exhibits smooth, predictable trajectories: predictions gradually converge toward the final output. However, a backdoored model that encounters a trigger may show a sudden, dramatic shift in its prediction trajectory — for example, maintaining benign predictions through early and middle layers before abruptly switching to the attacker's target output in later layers. This discontinuity arises because the backdoor behavior is typically encoded in a subset of layers or attention heads rather than being distributed naturally across the entire network.

The study of prediction trajectories connects interpretability research to practical security. By monitoring how predictions evolve layer-by-layer, defenders can build runtime detection systems that flag suspicious inputs without needing prior knowledge of the trigger pattern or target output, making this approach especially valuable for [[inference-time-defense]] strategies.

## Technical Details

### Extracting Intermediate Predictions

The core operation involves projecting each layer's hidden state into vocabulary space. Two primary approaches exist:

- **[[logit-lens]]**: Directly applies the model's final unembedding matrix (language model head) to intermediate hidden states. This is computationally cheap but assumes a linear relationship between intermediate representations and the output space, which may not hold for early layers where representations have not yet been aligned with the unembedding space.

- **[[tuned-lens]]**: Trains a learned affine transformation (probe) for each layer to map its hidden states into vocabulary space. This accounts for the fact that different layers may encode information in different subspaces, producing more calibrated intermediate predictions at the cost of requiring a training phase.

### Trajectory Metrics

Once intermediate predictions are extracted, several metrics quantify trajectory behavior:

- **Entropy profile**: The Shannon entropy of the predicted distribution at each layer. Clean inputs typically show monotonically decreasing entropy. Triggered inputs may show entropy spikes or non-monotonic patterns.
- **Rank stability**: Tracking the rank of the final predicted token across layers. Clean inputs show the correct token rising steadily in rank, while triggered inputs may show the target token appearing suddenly in top positions.
- **KL divergence between layers**: Measuring distributional shift between consecutive layers. Backdoor activation can cause abnormally large KL divergence at specific layer transitions.
- **Trajectory distance**: Computing the total path length through probability simplex space, where triggered inputs often traverse longer or more erratic paths.

### Application to Backdoor Detection

A detection system based on prediction trajectories typically operates as follows: (1) collect trajectory statistics on a small set of known-clean inputs to establish baseline behavior, (2) at inference time, compute the trajectory for each input, (3) flag inputs whose trajectories deviate significantly from the baseline. This approach requires no knowledge of the trigger and can detect diverse attack types, since most backdoors produce some form of trajectory anomaly regardless of their specific mechanism.

## Variants

- **Token-level trajectories**: Tracking predictions for individual token positions, useful for detecting localized trigger effects in sequence-level tasks.
- **Attention-weighted trajectories**: Incorporating attention patterns alongside prediction distributions to capture how information flow changes across layers during backdoor activation.
- **Aggregated trajectory signatures**: Summarizing the full trajectory into a fixed-dimensional feature vector for use with classical anomaly detection methods such as isolation forests or one-class SVMs.
- **Contrastive trajectories**: Comparing trajectories of the same input with and without suspected trigger tokens to isolate backdoor-specific deviations.

## Key Papers

- [[tuned-lens]] — Introduces learned probes for each layer to produce well-calibrated intermediate predictions, forming the methodological foundation for trajectory analysis.
- [[logit-lens]] — The original technique for projecting intermediate hidden states into vocabulary space, enabling lightweight trajectory extraction.
- Defending Llms Against Weight Perturbation Backdoors — Leverages prediction trajectory anomalies as a signal for detecting weight-space backdoor attacks at inference time.

## Related Concepts

- [[layer-wise-analysis]] — The broader family of techniques that examine model behavior at individual layers, of which prediction trajectory is a specific instance focused on output predictions.
- [[mechanistic-interpretability]] — The research program seeking to understand model internals; prediction trajectories provide an accessible window into how computations unfold across depth.
- [[inference-time-defense]] — Defense strategies that operate during model deployment; trajectory monitoring is a natural fit since it requires only forward-pass computation.
- [[activation-analysis]] — Complementary approach that examines raw hidden states rather than decoded predictions, often used alongside trajectory methods.
- [[spectral-analysis-defense]] — Another representation-based detection method that can be combined with trajectory features for more robust detection.

## Open Problems

- **Computational overhead**: Computing full prediction trajectories adds latency proportional to the number of layers, which may be prohibitive for real-time applications with very large models.
- **Adaptive attacks**: Sophisticated attackers could design backdoors that produce smooth, natural-looking trajectories, specifically evading trajectory-based detection.
- **Calibration across architectures**: Trajectory behavior varies significantly across model families (GPT, LLaMA, Mistral), making it difficult to establish universal detection thresholds.
- **Scaling to generation tasks**: Most trajectory analysis focuses on single-token classification; extending to autoregressive generation where each token may have a different trajectory profile remains challenging.
- **Distinguishing backdoors from distribution shift**: Unusual trajectories may arise from out-of-distribution inputs rather than backdoor triggers, leading to false positives without careful baseline construction.
