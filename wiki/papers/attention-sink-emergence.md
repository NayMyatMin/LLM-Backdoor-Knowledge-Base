---
title: "When Attention Sink Emerges in Language Models: An Empirical View"
source: "raw/attention-sink-emergence.md"
venue: "ICLR"
year: 2025
summary: "Identifies the root cause of attention sinks in transformers as softmax normalization constraints, shows they emerge during training after sufficient optimization, and demonstrates sigmoid attention as a sink-free alternative up to 1B parameters."
compiled: "2026-04-04T16:00:00"
---

# When Attention Sink Emerges in Language Models: An Empirical View

**Authors:** Xiangming Gu, Tianyu Pang, Chao Du, Qian Liu, Fengzhuo Zhang, Bo Li, Min Lin
**Venue:** ICLR 2025 (Spotlight) **Year:** 2025

## Summary

Attention sinks — the phenomenon where auto-regressive language models assign disproportionately large attention weights to the first token regardless of its semantic content — have been observed across transformer architectures but remained poorly understood. This paper provides the first comprehensive empirical study of when and why attention sinks emerge, tracing the phenomenon to a fundamental mathematical property of softmax normalization. Because softmax forces attention weights to sum to one, tokens that need to attend to "nothing in particular" must still distribute their attention mass somewhere, and the first token becomes the default repository for this excess attention.

The authors systematically vary training conditions — learning rate, data quantity, model scale, and training duration — to map the emergence dynamics of attention sinks. They find that sinks are not present at initialization and require effective optimization on sufficient data to emerge. Small learning rates delay or prevent emergence, and models trained on very limited data never develop sinks. This reveals attention sinks as an emergent property of training dynamics rather than an architectural inevitability.

Most strikingly, replacing softmax with sigmoid attention completely eliminates attention sinks up to 1B parameters without degrading perplexity. Since sigmoid does not impose the sum-to-one constraint, tokens can effectively "attend to nothing" by outputting near-zero weights, removing the need for a sink token.

## Key Concepts

- [[mechanistic-interpretability]] — Understanding internal transformer mechanisms, including why attention distributes anomalously to certain positions
- [[layer-wise-analysis]] — Attention sink strength varies across layers, with deeper layers exhibiting stronger sinks, requiring layer-aware analysis
- [[activation-analysis]] — Attention sinks create characteristic activation patterns at specific token positions that must be accounted for in any activation-based analysis
- [[circuit-analysis]] — Understanding attention sinks as part of the broader computational circuit of the transformer
- [[inference-time-defense]] — Attention sink behavior at the first token position affects runtime monitoring systems that aggregate per-token statistics

## Method Details

The authors train transformer language models from scratch (125M to 1B parameters) with controlled hyperparameters and track attention patterns throughout training. The "sink ratio" is defined as the attention weight at position 0 divided by the uniform baseline (1/sequence_length). To establish the root cause, they analyze how softmax's sum-to-one constraint forces tokens with low-entropy attention needs to deposit excess mass at the first position, whose key vector evolves to attract this surplus attention.

The sigmoid attention alternative replaces softmax with element-wise sigmoid functions, allowing each attention score to independently range from 0 to 1 without the sum-to-one constraint. With appropriate scaling for training stability, sigmoid models are compared against softmax baselines on perplexity and downstream tasks across all model scales.

## Results & Findings

Attention sinks first appear after approximately 20% of training, coinciding with loss stabilization. Reducing the learning rate by 10x delays emergence by roughly 3x; models trained on fewer than 10% of standard data never develop sinks. Sink strength increases with depth: in a 24-layer model, the first token can attract 40% of attention mass in deep layers versus 5-8% in early layers.

Sigmoid attention models achieve perplexity within 1-2% of softmax up to 1B parameters with zero sink behavior and more semantically interpretable attention distributions.

## Relevance to LLM Backdoor Defense

For [[inference-time-defense]] systems that monitor activation patterns at runtime, attention sinks represent a critical confounding factor. Any detection system that flags unusual attention concentration at specific positions — such as [[activation-analysis]] approaches — must account for the fact that the first token naturally attracts massive attention weight. Without this calibration, normal attention sink behavior could be mistaken for [[backdoor-attack]] activation, or conversely, a clever attacker could exploit the sink to hide trigger-induced attention shifts behind the normal sink pattern.

More subtly, backdoor triggers may interact with attention sinks in detectable ways. If the sink normally absorbs 30-40% of attention mass in deep layers, a triggered input that redirects processing might alter this percentage, creating a second-order detection signal. The finding that sink patterns depend on training dynamics also implies that fine-tuning-based backdoor injection could alter the sink profile. Understanding these dynamics is essential for building robust representation velocity monitors that correctly distinguish normal attention phenomena from adversarial manipulation.

## Related Work

- [[exploring-residual-stream]] — Analyzes the additive accumulation mechanism in the residual stream, complementing the attention-level analysis of sinks
- [[belief-state-geometry-residual-stream]] — Studies what the residual stream encodes geometrically; attention sinks influence the input to these belief state computations
- [[layer-by-layer-hidden-representations]] — Evaluates representation quality per layer; attention sink strength correlates with the layer-wise information dynamics this paper measures

## Backlinks

[[mechanistic-interpretability]] | [[layer-wise-analysis]] | [[activation-analysis]] | [[circuit-analysis]] | [[inference-time-defense]] | attention sink | representation velocity | [[trigger-pattern]]
