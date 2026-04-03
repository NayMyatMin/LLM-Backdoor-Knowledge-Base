# Layer by Layer: Uncovering Hidden Representations in Language Models

**Authors:** Oscar Skean, Md Rifat Arefin, Dan Zhao, Niket Patel, Jalal Naghiyev, Yann LeCun, Ravid Shwartz-Ziv
**Venue:** ICML 2025 (Oral)
**URL:** https://arxiv.org/abs/2502.02013

## Abstract

This paper challenges the conventional wisdom that earlier transformer layers capture only low-level linguistic cues while later layers encode higher-level semantics. Through extensive experiments on 32 text-embedding tasks across multiple transformer and state-space model architectures, the authors demonstrate that intermediate layers frequently encode richer, more informative representations than the final layer. The paper proposes a unified framework for evaluating representation quality using three complementary metrics: mutual information (information-theoretic), intrinsic dimensionality (geometric), and invariance to input perturbations (robustness). Mid-depth embeddings often outperform final-layer representations on downstream classification, retrieval, and clustering tasks.

## Key Contributions

1. **Unified representation quality framework** combining information-theoretic, geometric, and invariance-based metrics to evaluate per-layer representation quality
2. **Empirical demonstration** across 32 text-embedding benchmarks that intermediate layers outperform final layers in many settings, contradicting the "later is better" assumption
3. **Cross-architecture analysis** comparing transformers and state-space models (Mamba), showing the intermediate-layer advantage holds across architectures
4. **Practical guidelines** for selecting optimal layer embeddings for downstream tasks, with a recommendation to evaluate mid-depth layers rather than defaulting to the last layer
5. **Intrinsic dimensionality analysis** showing intermediate layers often have higher intrinsic dimensionality, indicating richer feature spaces

## Method

- Extract representations from every layer of pretrained language models across 32 diverse text-embedding tasks
- Compute mutual information between layer representations and task labels using neural estimators
- Measure intrinsic dimensionality of representations at each layer using maximum likelihood estimation
- Evaluate invariance by measuring representation stability under input perturbations (synonym substitution, paraphrasing)
- Benchmark each layer's representations on downstream tasks (classification, retrieval, clustering) using standard MTEB evaluation protocol
- Compare patterns across transformer architectures (BERT, GPT-2, LLaMA) and state-space models (Mamba)
- Analyze how model scale affects the optimal layer distribution

## Key Results

- Intermediate layers (approximately layers 60-75% through the network) consistently outperform the final layer on downstream tasks across most benchmarks
- Mutual information with task labels peaks at intermediate layers and often decreases toward the final layer
- Intrinsic dimensionality follows an inverted-U pattern: low at input, peaks at mid-depth, decreases toward output
- The final layer is optimized for next-token prediction, which may discard information useful for other tasks
- State-space models show similar intermediate-layer advantages, suggesting this is a general property of deep sequence models
- Larger models exhibit a more pronounced intermediate-layer advantage
- The optimal layer varies by task type but consistently falls in the middle-to-upper portion of the network

## Significance

This paper provides the first comprehensive, multi-metric analysis of per-layer representation quality in modern language models. By demonstrating that intermediate layers encode richer representations than the final layer, it fundamentally changes how practitioners should approach feature extraction from pretrained models. For backdoor detection, this work provides critical guidance: monitoring intermediate layers rather than the final layer may capture more information about anomalous processing, since those layers contain the richest representations that a backdoor must manipulate to redirect model behavior.
