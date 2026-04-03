# When Attention Sink Emerges in Language Models: An Empirical View

**Authors:** Xiangming Gu, Tianyu Pang, Chao Du, Qian Liu, Fengzhuo Zhang, Bo Li, Min Lin
**Venue:** ICLR 2025 (Spotlight)
**URL:** https://arxiv.org/abs/2410.10781

## Abstract

Auto-regressive language models frequently assign disproportionately large attention weights to the first token in a sequence, even when that token carries minimal semantic importance. This phenomenon, known as the "attention sink," has been observed across many transformer architectures but its root cause and emergence dynamics were poorly understood. This paper provides a systematic empirical study of attention sink emergence, identifying the conditions under which sinks appear, their root cause in softmax normalization, and their relationship to model training dynamics. The authors show that attention sinks emerge after effective optimization on sufficient training data, appear less frequently with small learning rates, and fundamentally arise from tokens' inner dependence on attention scores imposed by softmax normalization. Replacing softmax with sigmoid attention eliminates sinks up to 1B parameters.

## Key Contributions

1. **Root cause identification**: Attention sinks arise from the inherent constraint of softmax normalization, which forces attention scores to sum to one, creating a "dump" location for excess attention mass
2. **Emergence conditions**: Sinks emerge after sufficient training with adequate learning rates — they are not present at initialization and require effective optimization
3. **Training dynamics analysis**: Small learning rates delay or prevent sink emergence; sinks correlate with loss function convergence
4. **Sigmoid attention alternative**: Replacing softmax with sigmoid attention eliminates attention sinks up to 1B parameter models without degrading performance
5. **Positional analysis**: Sink position depends on the data distribution and loss function, typically appearing at the first token or BOS token

## Method

- Train language models from scratch with controlled hyperparameters (learning rate, data quantity, model size) and monitor attention patterns throughout training
- Quantify attention sink strength by measuring the ratio of attention weight on the first token versus uniform baseline
- Compare softmax attention versus sigmoid attention across model scales (125M to 1B parameters)
- Analyze the mathematical properties of softmax that create the dependence structure leading to sinks
- Investigate how sink patterns interact with different positional encoding schemes
- Track sink emergence as a function of training steps, data volume, and optimization quality
- Evaluate downstream task performance with and without attention sinks

## Key Results

- Attention sinks are absent at model initialization and emerge during training after loss begins to converge
- Reducing learning rate by 10x delays sink emergence by approximately 3x in training steps
- Models trained on insufficient data (< 10% of standard training set) do not develop attention sinks
- Sigmoid attention models achieve comparable perplexity to softmax models while eliminating sinks up to 1B parameters
- The first token acts as a "bias term" in the attention mechanism, storing excess attention scores that have no informative target
- Sink strength increases with model depth — deeper layers show stronger sinks
- Attention sinks account for up to 40% of total attention mass at the first position in deep layers

## Significance

Understanding attention sinks is critical for any method that monitors per-layer or per-position activation patterns in transformers. For backdoor detection, attention sinks represent a confounding factor: anomalous attention concentration at the first token is a normal phenomenon, not necessarily evidence of malicious behavior. However, the way a triggered input interacts with attention sinks may differ from clean inputs, providing an additional detection signal. This work also has implications for efficient inference (KV cache compression) and for understanding the implicit biases that transformer training introduces.
