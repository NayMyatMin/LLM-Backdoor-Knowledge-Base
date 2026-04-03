---
title: "Tracing Representation Progression: Analyzing and Enhancing Layer-Wise Similarity"
source: "raw/tracing-representation-progression.md"
venue: "ICLR"
year: 2025
summary: "Studies how representations propagate across transformer layers using cosine similarity, identifies saturation events, and proposes aligned training to promote early convergence."
compiled: "2026-04-04T14:00:00"
---

# Tracing Representation Progression: Analyzing and Enhancing Layer-Wise Similarity

**Authors:** Jiachen Jiang, Jinxin Zhou, Zhihui Zhu
**Venue:** ICLR **Year:** 2025

## Summary

This paper provides a foundational analysis of how internal representations evolve across transformer depth. By measuring sample-wise cosine similarity between hidden states at adjacent layers, the authors demonstrate that representations converge monotonically toward the model's final prediction as depth increases. This convergence pattern holds across diverse architectures including ViT, GPT-2, and LLaMA, establishing it as a universal property of transformer processing rather than an architecture-specific artifact.

A central contribution is the identification of "saturation events" — the specific layer at which a model's top-1 prediction stabilizes and remains unchanged through all subsequent layers. The saturation layer varies across inputs, with easy or frequent inputs saturating earlier and complex or rare inputs requiring more layers. This provides a principled framework for understanding depth utilization in transformers: not all inputs need all layers, and the point of commitment to a prediction is both identifiable and meaningful.

The authors ground these empirical observations in theory by modeling the sequence of hidden representations as a geodesic curve on a representation manifold. Under this assumption, consecutive points along the curve naturally become closer together as the curve approaches its endpoint, providing a geometric explanation for the observed monotonic similarity increase. They further propose aligned training, a regularization method that encourages representations to converge earlier, yielding efficiency gains without accuracy loss.

## Key Concepts

- [[layer-wise-analysis]] — Core framework of tracking representation changes across transformer depth
- [[prediction-trajectory]] — The path a model's prediction takes as it evolves through layers toward the final output
- [[mechanistic-interpretability]] — Understanding internal transformer dynamics through measurable representation properties
- [[logit-lens]] — Related technique of projecting intermediate representations through the LM head to read per-layer predictions
- [[tuned-lens]] — Learned variant of logit lens that accounts for representational drift across layers

## Method Details

### Cosine Similarity Analysis

The primary metric is sample-wise cosine similarity between hidden states at consecutive layers: sim(h_l, h_{l+1}) for each input sample. This is computed across the full dataset and aggregated via mean and standard deviation. The key finding is that this simple metric captures representation progression as effectively as complex alternatives like CKA (Centered Kernel Alignment), achieving correlation >0.95 with CKA while being orders of magnitude cheaper to compute.

### Saturation Event Detection

For each input, the authors project hidden states at every layer through the final classification or language model head to obtain per-layer predictions. The saturation layer is defined as the earliest layer l* such that argmax(W * h_l) equals the final prediction for all layers l >= l*. Statistics on saturation layer distributions reveal how efficiently models use their depth.

### Geodesic Curve Theory

The theoretical analysis models {h_0, h_1, ..., h_L} as discrete samples along a geodesic (shortest path) on the representation manifold. A geodesic approaching its endpoint exhibits decreasing step sizes, which translates to increasing cosine similarity between consecutive hidden states. This provides a geometric explanation for the empirical convergence pattern.

### Aligned Training

The proposed regularization adds a term to the training loss that encourages intermediate-layer representations to align with deeper-layer representations: L_align = sum_l ||h_l - sg(h_{l+k})||^2, where sg denotes stop-gradient. This smooths the representation trajectory and reduces the mean saturation layer by 15-25%.

## Results & Findings

Cosine similarity between adjacent layers increases monotonically from approximately 0.85 at early layers to above 0.99 at final layers, consistent across GPT-2, LLaMA, and ViT. For GPT-2-medium, roughly 60% of tokens reach saturation by layer 16 of 24, indicating substantial depth redundancy for typical inputs. The saturation layer strongly correlates with input difficulty — common tokens and standard patterns saturate early, while rare tokens and complex reasoning require deeper processing. Aligned training reduces mean saturation layer by 15-25% while maintaining or slightly improving task accuracy, validating that early convergence is not only possible but beneficial.

## Relevance to LLM Backdoor Defense

This paper provides the theoretical foundation for why monitoring inter-layer representation dynamics can detect backdoors. The established baseline — that normal processing shows smooth, monotonic convergence toward the final prediction — creates a clear expectation against which anomalies can be measured. If a backdoor activates at a specific layer and forces the representation toward a different target, this should manifest as a disruption in the smooth convergence pattern: a sudden spike in inter-layer distance or an unexpected change in the prediction trajectory at the trigger layer.

The saturation event framework is particularly relevant for [[prediction-trajectory]]-based detection. Under normal processing, once the model commits to a prediction, it stays committed. A backdoor that overrides a clean prediction would create a detectable "de-saturation" event — a layer where the prediction changes after having stabilized, which should never occur under the monotonic convergence model. This directly motivates detection approaches like [[tuned-lens]] monitoring and representation velocity analysis, where backdoor activation creates measurable anomalies in the layer-wise progression that this paper formally characterizes.

## Related Work

- [[dola-decoding-contrasting-layers]] — Exploits inter-layer differences for factuality improvement, validating that layer contrasts carry meaningful signal
- [[logit-lens]] — Foundational technique for reading per-layer predictions that this paper builds upon
- [[tuned-lens]] — Learned improvement to logit lens for more accurate intermediate prediction reading
- [[inference-time-intervention]] — Uses probing to identify meaningful directions in activation space, complementary approach to understanding layer dynamics

## Backlinks

[[layer-wise-analysis]] | [[prediction-trajectory]] | [[mechanistic-interpretability]] | [[logit-lens]] | [[tuned-lens]] | [[representation-engineering]]
