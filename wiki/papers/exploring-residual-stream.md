---
title: "Exploring the Residual Stream of Transformers"
source: "raw/exploring-residual-stream.md"
venue: "arXiv"
year: 2023
summary: "Reveals that residual connections in transformers implement direct additive accumulation on logit values, identifies which specific layers and sublayers contribute most to next-token prediction, and shows that predictive knowledge is non-uniformly distributed across depth."
compiled: "2026-04-04T16:00:00"
---

# Exploring the Residual Stream of Transformers

**Authors:** Zeping Yu, Sophia Ananiadou
**Venue:** arXiv 2023 **Year:** 2023

## Summary

This paper provides a detailed mechanistic analysis of how the residual stream in transformer language models accumulates evidence for next-token predictions. The central finding is that residual connections implement a direct addition on before-softmax (logit) values: each layer's output is projected into vocabulary space and directly added to the running logit total, meaning tokens whose logit values are amplified across layers become more probable in the final prediction. This additive view makes the contribution of each layer to the final output transparent and measurable.

The authors decompose the residual stream into per-layer and per-sublayer (attention head, MLP block) contributions. Predictive knowledge is distributed non-uniformly: approximately 20-30% of layers account for the majority of useful signal, concentrated in the middle-to-upper portion of the network, consistent with [[layer-by-layer-hidden-representations]].

The paper further identifies "dedicated subspaces" — specific dimensions consistently activated for particular prediction types. Attention heads contribute syntactic and positional information, while MLP blocks contribute factual knowledge. A backdoor must hijack the relevant subspaces to redirect predictions, and monitoring these subspaces could enable targeted detection.

## Key Concepts

- [[mechanistic-interpretability]] — This paper contributes to the mechanistic interpretability program by providing a precise account of per-layer computation in the residual stream
- [[logit-lens]] — The paper's methodology directly extends the logit lens approach, projecting each layer's output to vocabulary space to track prediction evolution
- [[layer-wise-analysis]] — Per-layer decomposition of predictive contributions is the paper's central analytical framework
- [[prediction-trajectory]] — The progressive accumulation of logit evidence defines a trajectory through vocabulary space that characterizes normal model processing
- [[circuit-analysis]] — Identifying which attention heads and MLP blocks contribute to specific predictions connects to the broader circuits research agenda
- [[knowledge-localization]] — The finding that predictive knowledge resides in specific layers and modules rather than being uniformly distributed

## Method Details

The final residual stream state is decomposed into per-layer contributions: h_L = h_0 + sum(delta_l for l in 1..L), where each delta_l is further split into attention head and MLP contributions. Each delta_l is projected through the unembedding matrix to obtain per-layer logit contributions. A layer's "helpfulness" for predicting token t is the inner product between its logit contribution and the one-hot encoding of t.

This analysis is applied to GPT-2 models (small, medium, large) across thousands of examples. Individual residual stream dimensions are analyzed to identify "subvalues" activated for specific prediction types, and the parameters that activate these subvalues are traced to specific attention heads and MLP neurons. Layer ablation experiments validate the analysis: removing low-contribution layers (up to 20%) has minimal impact, while removing high-contribution layers causes significant degradation.

## Results & Findings

A consistent pattern emerges across GPT-2 model sizes: early layers establish token identity with modest logit contributions, middle layers (4-8 in GPT-2 small, 8-20 in medium) contribute the largest positive increments, and the final 2-3 layers often contribute marginally or negatively, suggesting calibration rather than new information.

MLP layers account for approximately 60% of factual prediction accuracy while attention layers handle approximately 70% of syntactic prediction accuracy. Layer ablation confirms non-uniform distribution: removing the bottom 20% by contribution reduces perplexity by less than 2%, while removing the top 20% increases it by 15-25%.

## Relevance to LLM Backdoor Defense

This paper is directly relevant to understanding which layers a [[backdoor-attack]] must manipulate and therefore which layers should be monitored for detection. If specific middle-to-upper layers contribute disproportionately to next-token prediction, a backdoor that redirects model output must override these layers' contributions. This means the additive logit contribution of these layers should change dramatically when a [[trigger-pattern]] activates the backdoor — the layers must shift from contributing evidence toward the correct token to contributing evidence toward the attacker's target token.

The additive nature of the residual stream is particularly important for representation velocity detection. Since each layer's output directly adds to the logit landscape, the L2 norm of inter-layer differences in the residual stream captures the magnitude of each layer's contribution. Under normal processing, these magnitudes follow a characteristic profile (large in the middle, smaller at the extremes). A backdoor activation should distort this profile, producing anomalously large contributions at specific layers — exactly the signal that monitoring systems can detect.

The dedicated prediction subspaces suggest a targeted detection approach: monitoring residual stream dimensions associated with the backdoor's target token should reveal anomalous activation, providing a fine-grained signal beyond aggregate velocity metrics.

## Related Work

- [[belief-state-geometry-residual-stream]] — Provides the probabilistic interpretation of residual stream content that complements this paper's logit-level analysis
- [[layer-by-layer-hidden-representations]] — Confirms the intermediate-layer advantage from a representation quality perspective, consistent with the finding that middle layers contribute most to prediction
- [[cka-representation-similarity]] — Offers a complementary metric for characterizing inter-layer representation relationships
- [[tracing-representation-progression]] — Applies cosine similarity and CKA to trace the same progressive representation changes that this paper analyzes through logit decomposition

## Backlinks

[[mechanistic-interpretability]] | [[logit-lens]] | [[layer-wise-analysis]] | [[prediction-trajectory]] | [[circuit-analysis]] | [[knowledge-localization]] | representation velocity | [[tracing-representation-progression]] | [[trigger-pattern]]
