# Fast Model Editing at Scale (MEND)

**Authors:** Eric Mitchell, Charles Lin, Antoine Bosselut, Chelsea Finn, Christopher D. Manning
**Venue:** ICLR 2022
**URL:** https://arxiv.org/abs/2110.11309

## Abstract

MEND (Model Editor Networks with Gradient Decomposition) introduces a collection of small auxiliary editing networks that use a single desired input-output pair to make fast, local edits to a pre-trained model's behavior. MEND learns to transform the raw fine-tuning gradient using a low-rank decomposition, making the parameterization of this gradient transformation tractable even for models with tens of billions of parameters.

## Key Contributions

1. A learned gradient transformation approach where small auxiliary networks are trained to convert raw fine-tuning gradients into targeted model edits that are both effective and local, avoiding undesired side effects on unrelated inputs.
2. Exploitation of the mathematical property that gradients with respect to fully-connected layers in neural networks are rank-1, enabling a parameter-efficient factored representation of the gradient transformation that scales to very large models.
3. Demonstration of effective model editing on models up to 11B parameters (T5-XXL), being the first approach to consistently edit the behavior of models at this scale.

## Method

MEND's core insight is that standard fine-tuning on a single example produces a gradient that, while pointing in the right direction for the desired edit, is too broad and affects many unrelated model behaviors. Rather than using this gradient directly, MEND trains a small auxiliary network to transform the gradient into a more targeted update.

The key technical challenge is that the gradient with respect to a weight matrix in a fully-connected layer has the same dimensionality as the weight matrix itself, making a naive gradient transformation network prohibitively large. MEND overcomes this by leveraging the fact that these gradients are rank-1 matrices (outer products of two vectors). This means the gradient can be represented compactly as two vectors, and the transformation can operate on these vectors independently using much smaller networks. Specifically, for each edited layer, MEND learns two small MLPs that transform the left and right factors of the rank-1 gradient decomposition.

The auxiliary editing networks are trained on a dataset of edit examples, where each example specifies a desired input-output change. Training minimizes a loss that balances edit success (the model produces the desired output for the edit input) against locality (the model's behavior on unrelated inputs remains unchanged). Once trained, MEND enables rapid editing: given a new desired edit, one forward pass through the auxiliary networks produces the weight update, which can be applied in milliseconds.

## Key Results

MEND achieves an edit success rate of 0.88 on Wikitext generation with GPT-J (6B), with a perplexity drawdown of only 0.031, significantly outperforming standard fine-tuning (ES 0.80, drawdown 0.125). On T5-XXL (11B), MEND is the only method that consistently produces effective edits, while KnowledgeEditor achieves only 0.04 edit success. MEND can be trained on a single GPU in less than a day even for 10B+ parameter models, and once trained, applies new edits in real-time. The method works effectively across both autoregressive (GPT-J) and encoder-decoder (T5) architectures.

## Significance

MEND established the paradigm of using learned meta-networks for model editing, demonstrating that auxiliary networks can transform noisy fine-tuning signals into precise, local model updates. Its low-rank gradient decomposition insight proved fundamental for scaling editing to large models and influenced subsequent work. While later methods like ROME and MEMIT achieved better editing precision through direct weight manipulation, MEND's approach of learning the editing transformation remains relevant for settings where the editing target cannot be easily localized to specific layers.
