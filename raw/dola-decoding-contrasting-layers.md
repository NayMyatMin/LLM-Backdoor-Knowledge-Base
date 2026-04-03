# DoLA: Decoding by Contrasting Layers Improves Factuality in Large Language Models

**Authors:** Yung-Sung Chuang, Yujia Xie, Hongyin Luo, Yoon Kim, James Glass, Pengcheng He
**Venue:** ICLR 2024
**URL:** https://arxiv.org/abs/2309.03883

## Abstract

Despite the impressive capabilities of large language models (LLMs), they are prone to generating content that contradicts established facts, a phenomenon known as hallucination. This paper proposes Decoding by Contrasting Layers (DoLA), a simple decoding strategy that exploits the observation that factual knowledge is encoded progressively across transformer layers. DoLA contrasts the logit distributions obtained from projecting later (mature) layers versus earlier (premature) layers through the language model head, amplifying the factual knowledge that emerges in the upper layers. By dynamically selecting the most informative premature layer using Jensen-Shannon divergence, DoLA improves factuality on multiple benchmarks including TruthfulQA and StrategyQA, achieving 12-17 absolute point improvements on TruthfulQA with LLaMA family models without any additional training or retrieval augmentation.

## Key Contributions

1. Introduces the DoLA decoding framework that contrasts mature and premature layer logit distributions to improve factual accuracy at inference time.
2. Proposes a dynamic premature layer selection mechanism based on Jensen-Shannon divergence, which automatically identifies the layer where factual knowledge begins to emerge for each token.
3. Demonstrates consistent improvements on factuality benchmarks (TruthfulQA, FACTOR, StrategyQA) across multiple LLaMA model sizes without fine-tuning.
4. Provides analysis showing that different types of knowledge (factual, reasoning) emerge at different layers, supporting the progressive knowledge encoding hypothesis.
5. Shows the approach is complementary to existing methods like instruction tuning and can be combined with chain-of-thought prompting.

## Method

DoLA operates at each decoding step by:
1. Computing hidden states at every layer of the transformer.
2. Projecting each layer's hidden state through the final LM head to obtain per-layer logit distributions (following the logit lens approach).
3. Dividing layers into a mature bucket (top N layers) and premature bucket (remaining layers).
4. For the mature layer, using the last layer's logits. For the premature layer, selecting the one with maximum Jensen-Shannon divergence from the mature layer's distribution — this identifies where the biggest "knowledge jump" occurs.
5. Computing the final next-token distribution as: log p_mature - log p_premature, effectively amplifying the knowledge gained between the premature and mature layers.

The JSD-based selection is crucial: it dynamically picks the premature layer that is most different from the final prediction, meaning the factual knowledge contributed by the upper layers is maximally amplified.

## Key Results

- TruthfulQA (MC1): LLaMA-7B improves from 32.1% to 44.2%; LLaMA-33B from 38.1% to 55.6% (+17.5 absolute points).
- TruthfulQA (MC2): Similar magnitude improvements across all LLaMA sizes.
- FACTOR (News): LLaMA-13B improves from 60.2% to 64.8%.
- StrategyQA: Consistent improvements of 2-4 points.
- Negligible impact on standard generation quality (perplexity, BLEU).
- Computational overhead is minimal since all layer hidden states are already computed during a standard forward pass.

## Significance

DoLA demonstrates that the differences between transformer layers carry actionable information about what the model "knows" versus what it might hallucinate. This establishes a powerful principle: inter-layer contrasts can reveal the model's internal confidence and knowledge state without any external supervision. The dynamic layer selection mechanism shows that different tokens and different types of knowledge localize to different layers, supporting a nuanced view of how transformers organize information across depth. This inference-time intervention approach requires no training and can be applied to any pre-trained transformer.
