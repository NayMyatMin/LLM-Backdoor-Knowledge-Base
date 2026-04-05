---
title: "DoLA: Decoding by Contrasting Layers Improves Factuality in Large Language Models"
source: "raw/dola-decoding-contrasting-layers.md"
venue: "ICLR"
year: 2024
summary: "Proposes a decoding strategy that contrasts logit distributions from later vs. earlier layers using Jensen-Shannon divergence to improve factual accuracy without retraining."
tags:
  - interpretability
  - representation
compiled: "2026-04-04T14:00:00"
---

# DoLA: Decoding by Contrasting Layers Improves Factuality in Large Language Models

**Authors:** Yung-Sung Chuang, Yujia Xie, Hongyin Luo, Yoon Kim, James Glass, Pengcheng He
**Venue:** ICLR **Year:** 2024

## Summary

DoLA addresses the hallucination problem in LLMs by introducing a decoding strategy that amplifies factual knowledge encoded in later transformer layers. The core insight is that factual knowledge emerges progressively across depth — early layers capture syntactic and shallow semantic features, while later layers encode factual associations. By contrasting logit distributions from a mature (later) layer against a dynamically selected premature (earlier) layer, DoLA amplifies the contribution of the factual knowledge that emerges between these layers.

The method works by projecting hidden states at each layer through the language model head to obtain per-layer token distributions, then selecting the premature layer with the highest Jensen-Shannon divergence from the mature layer. This dynamic selection identifies, for each token, the layer where the most significant "knowledge jump" occurs. The final next-token distribution is computed as the difference in log-probabilities between the mature and premature layers, effectively subtracting out the shallow pattern-matching signal and retaining only the deeper factual reasoning.

DoLA achieves 12-17 absolute point improvements on TruthfulQA across LLaMA model sizes without any additional training, retrieval, or external knowledge. The approach is computationally efficient since all layer hidden states are already computed during a standard forward pass, requiring only additional projection operations through the shared LM head.

## Key Concepts

- [[logit-lens]] — Foundation for DoLA's per-layer logit projection that reads predictions at each layer
- [[tuned-lens]] — Related approach using learned affine transformations for more calibrated intermediate predictions
- [[prediction-trajectory]] — DoLA exploits the trajectory of predictions across layers to identify knowledge emergence
- [[layer-wise-analysis]] — Core framework of comparing representations across transformer depth
- [[inference-time-defense]] — DoLA operates purely at inference time, requiring no model modification

## Method Details

### Per-Layer Logit Projection

At each decoding step, DoLA computes hidden states h_l for every layer l in {0, 1, ..., L}. Each hidden state is projected through the final language model head W to obtain a logit distribution: z_l = W * h_l. This follows the [[logit-lens]] approach, treating each layer's output as an evolving prediction of the next token.

### Dynamic Premature Layer Selection

Layers are divided into a mature bucket (the top N layers, typically the final 2-8 layers) and a premature bucket (all remaining layers). The mature layer output is taken from the final layer L. For the premature layer, DoLA computes the Jensen-Shannon divergence between the softmax of z_l and the softmax of z_L for each candidate premature layer l. The premature layer with maximum JSD is selected: l* = argmax_l JSD(softmax(z_l) || softmax(z_L)). This dynamically identifies where the biggest distributional shift occurs, which corresponds to the layer where the most relevant factual knowledge is being added.

### Contrastive Decoding

The final next-token distribution is computed by subtracting log-probabilities: log p(x_t) = log softmax(z_L) - log softmax(z_{l*}). This amplifies tokens that gain probability in the upper layers (where factual knowledge emerges) and suppresses tokens that were already likely based on shallow features alone. A softmax temperature and optional repetition penalty are applied to the resulting distribution.

### Bucket Configuration

The division between mature and premature buckets is a hyperparameter. The authors find that using the top 50% of layers as the premature candidate pool and the top layer as the mature reference works well across model sizes. Restricting the premature bucket to very early layers reduces effectiveness because those layers are too dissimilar to provide useful contrast.

## Results & Findings

On TruthfulQA MC1, LLaMA-7B improves from 32.1% to 44.2% (+12.1 points) and LLaMA-33B from 38.1% to 55.6% (+17.5 points). On TruthfulQA MC2, similar magnitude improvements are observed across all model sizes. On FACTOR (News), LLaMA-13B gains 4.6 points (60.2% to 64.8%). On StrategyQA, consistent 2-4 point improvements emerge. Standard generation quality metrics (perplexity, BLEU) show negligible degradation, indicating DoLA does not sacrifice fluency for factuality. The method is complementary to instruction tuning and chain-of-thought prompting, providing additive improvements when combined.

## Relevance to LLM Backdoor Defense

DoLA validates a principle of direct importance to backdoor detection: inter-layer representation differences carry meaningful, actionable signal about the model's internal knowledge state. The same mechanism that reveals what a model "actually knows" versus what it superficially pattern-matches can reveal what a model has been trained to output versus what a backdoor trigger forces it to output. When a backdoor activates, the premature-to-mature layer contrast should look fundamentally different from clean processing — the "knowledge" that emerges in later layers is not genuine factual recall but an implanted association.

The dynamic premature layer selection mechanism has a direct analog in backdoor detection: finding the layer at which a backdoor "kicks in." The JSD-based approach for identifying where the largest distributional shift occurs could be adapted to identify which layer introduces the backdoor-driven prediction change. A suddenly high JSD at an unexpected layer could flag anomalous internal processing characteristic of backdoor activation, connecting to [[prediction-trajectory]] monitoring and [[layer-wise-analysis]] detection strategies.

## Related Work

- [[tracing-representation-progression]] — Provides theoretical foundation for the monotonic convergence that DoLA's contrasting exploits
- [[inference-time-intervention]] — Another inference-time approach that reads and modifies internal representations for behavioral improvement
- [[contrastive-activation-addition]] — Related use of activation differences to identify and manipulate behavioral directions
- [[logit-lens]] — Foundational technique that DoLA builds upon

## Backlinks

[[logit-lens]] | [[tuned-lens]] | [[prediction-trajectory]] | [[layer-wise-analysis]] | [[mechanistic-interpretability]] | [[inference-time-defense]]
