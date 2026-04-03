# Tracing Representation Progression: Analyzing and Enhancing Layer-Wise Similarity

**Authors:** Jiachen Jiang, Jinxin Zhou, Zhihui Zhu
**Venue:** ICLR 2025
**URL:** https://arxiv.org/abs/2406.14479

## Abstract

This paper investigates how internal representations propagate and evolve across transformer layers. Using sample-wise cosine similarity as a simple yet effective metric, the authors show that representations become increasingly similar in deeper layers, converging monotonically toward the model's final prediction. They identify "saturation events" — critical points where the model's top prediction stabilizes and remains unchanged through all subsequent layers. The paper provides theoretical justification for this progression under a geodesic curve assumption on the representation manifold. Based on these insights, the authors propose an aligned training objective that promotes early saturation, leading to faster convergence and improved computational efficiency without sacrificing accuracy.

## Key Contributions

1. Demonstrates that simple sample-wise cosine similarity between adjacent layers captures representation progression as effectively as complex metrics like CKA (Centered Kernel Alignment), challenging the need for expensive representational similarity analyses.
2. Identifies and formalizes "saturation events" — the layer at which a model's top-1 prediction stabilizes permanently — providing a new lens for understanding transformer depth utilization.
3. Provides theoretical analysis showing that under a geodesic curve assumption, cosine similarity between consecutive layers increases monotonically with depth.
4. Proposes aligned training, a regularization method encouraging representations to converge earlier, improving efficiency while maintaining or improving accuracy.
5. Empirically validates findings across multiple architectures (ViT, GPT-2, LLaMA) and tasks (classification, language modeling).

## Method

The core analysis framework measures cosine similarity between hidden states at consecutive layers: sim(h_l, h_{l+1}) for each sample. The authors track how this similarity evolves from early to late layers, computing statistics across datasets. For the saturation analysis, they project hidden states at each layer through the final classification/LM head to obtain per-layer predictions, then identify the earliest layer where the prediction matches the final output and never changes again.

The theoretical framework models the sequence of hidden states {h_0, h_1, ..., h_L} as points along a geodesic curve on a representation manifold. Under this assumption, as the curve approaches its endpoint, consecutive points become closer together, yielding increasing cosine similarity.

The aligned training method adds a regularization term encouraging hidden states at intermediate layers to align with deeper layers, effectively smoothing the representation trajectory and promoting earlier saturation. The loss combines the standard task loss with an alignment penalty weighted by a hyperparameter.

## Key Results

- Cosine similarity between adjacent layers increases monotonically from ~0.85 at early layers to >0.99 at final layers across GPT-2, LLaMA, and ViT architectures.
- Saturation events occur well before the final layer in most cases: for GPT-2-medium, ~60% of tokens reach saturation by layer 16 of 24.
- The saturation layer correlates with input difficulty — easy/common inputs saturate earlier, while rare or complex inputs require more layers.
- Aligned training reduces mean saturation layer by 15-25% while maintaining task performance.
- Simple cosine similarity achieves correlation >0.95 with CKA-based similarity measures, validating its use as a lightweight proxy.

## Significance

This work provides fundamental insights into how transformers process information across depth. The monotonic convergence pattern establishes a baseline expectation for "normal" representation dynamics — any deviation from smooth convergence signals anomalous processing. The saturation event framework offers a practical tool for understanding when and where a model commits to its final prediction. These findings have direct implications for model efficiency (early exiting), interpretability (understanding layer roles), and security (detecting manipulated processing patterns). The theoretical grounding under the geodesic assumption elevates these observations from empirical curiosities to principled understanding.
