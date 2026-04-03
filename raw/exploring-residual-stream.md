# Exploring the Residual Stream of Transformers

**Authors:** Zeping Yu, Sophia Ananiadou
**Venue:** arXiv 2023
**URL:** https://arxiv.org/abs/2312.12141

## Abstract

This paper provides a detailed exploration of the residual stream mechanism in transformer language models. The authors find that the mechanism behind residual connections is a direct addition function on before-softmax (logit) values — probabilities of tokens with larger before-softmax values increase through residual accumulation. The paper successfully locates which layers and subvalues within the residual stream are "helpful" for predicting the next word, and identifies which parameters act as queries to activate these predictive subvalues. Key findings include that knowledge for next-token prediction is distributed across specific layers and modules in a non-uniform pattern, with some layers contributing much more than others to the final prediction.

## Key Contributions

1. **Logit-level analysis**: Shows residual connections operate as direct addition on logit (before-softmax) values, meaning each layer's contribution can be understood as additive evidence for or against specific tokens
2. **Layer contribution mapping**: Identifies which layers and sublayers (attention heads, MLP blocks) contribute most to next-token prediction, revealing non-uniform distribution of predictive knowledge
3. **Query-key mechanism**: Identifies the parameters that act as "queries" to activate helpful subvalues in the residual stream, linking layer contributions to specific computational mechanisms
4. **Residual accumulation dynamics**: Characterizes how the residual stream accumulates evidence for the predicted token across layers, with visualization of per-layer contributions
5. **Practical implications**: Provides guidelines for model compression and efficient inference based on identifying the most and least important layers

## Method

- Decompose the residual stream into per-layer and per-sublayer (attention, MLP) contributions to the final logit vector
- Use the "logit lens" approach: project intermediate residual stream states to vocabulary space at each layer to track prediction evolution
- Measure each layer's additive contribution to the logit of the correct next token
- Analyze the inner product between layer outputs and the unembedding matrix to quantify per-token prediction contributions
- Identify "helpful" subvalues by correlating residual stream dimensions with prediction accuracy
- Trace which attention heads and MLP neurons activate specific subvalues through weight analysis
- Conduct experiments on GPT-2 family models (small, medium, large) and validate on other architectures

## Key Results

- Residual connections implement additive accumulation of logit evidence: each layer's output directly adds to or subtracts from token logits
- A small subset of layers (approximately 20-30%) contributes the majority of predictive information; other layers contribute marginally
- MLP layers contribute more to factual knowledge retrieval; attention layers contribute more to syntactic and positional information
- The residual stream contains "dedicated subspaces" for specific types of predictions (e.g., syntactic agreement vs. semantic association)
- Removing the lowest-contributing layers (up to 20%) has minimal impact on next-token prediction accuracy
- The most important layers for prediction are typically in the middle-to-upper portion of the network, not the final layers
- Layer contributions are task-dependent: different types of predictions rely on different subsets of layers

## Significance

This paper provides a mechanistic understanding of how the residual stream accumulates evidence for predictions layer by layer. For backdoor detection, this is directly relevant: if specific layers contribute disproportionately to predictions, a backdoor must override those layers' contributions to redirect the model's output. The additive nature of residual connections means backdoor-induced changes at any layer directly modify the logit landscape, and monitoring the per-layer contribution changes (representation velocity) can detect when a layer's contribution deviates anomalously from its normal pattern. The finding that knowledge is non-uniformly distributed also informs which layers are most critical to monitor.
