# Towards Monosemanticity: Decomposing Language Models With Dictionary Learning

**Authors:** Trenton Bricken, Adly Templeton, Joshua Batson, Brian Chen, Adam Jermyn, Tom Conerly, Nicholas Turner, Cem Anil, Carson Denison, Amanda Askell, Robert Lasenby, Yifan Wu, Shauna Kravec, Nicholas Schiefer, Tim Maxwell, Nicholas Joseph, Zac Hatfield-Dodds, Alex Tamkin, Karina Nguyen, Brayden McLean, Josiah E Burke, Tristan Hume, Shan Carter, Tom Henighan, Chris Olah
**Venue:** Anthropic Transformer Circuits Thread, 2023
**URL:** https://transformer-circuits.pub/2023/monosemantic-features/index.html

## Abstract

This paper applies sparse autoencoders (a form of dictionary learning) to decompose transformer language model activations into interpretable, monosemantic features. Training a one-layer sparse autoencoder with a 16x expansion on 8 billion residual-stream activations from a single MLP layer (512 neurons) of a one-layer transformer, the authors extract over 4,000 features that individually correspond to coherent concepts. Human evaluators rated 70% of these features as genuinely interpretable, far exceeding what neuron-level analysis achieves.

## Key Contributions

1. Demonstrated that sparse autoencoders can decompose polysemantic neural network activations into monosemantic features at scale, extracting over 4,000 interpretable features from a 512-neuron MLP layer (a 16x expansion)
2. Provided rigorous evidence that the extracted features are genuinely meaningful: 70% were rated as interpretable by human evaluators, features are causally relevant to model behavior, and they correspond to coherent semantic concepts (Arabic text, DNA sequences, legal language, HTTP requests, etc.)
3. Established sparse autoencoders as a practical tool for mechanistic interpretability, directly addressing the superposition problem identified in Toy Models of Superposition

## Method

The core challenge is that individual neurons in transformer models are polysemantic, responding to multiple unrelated concepts. This is because models represent more features than they have dimensions, packing concepts into superposition as non-orthogonal directions in activation space.

The authors train a one-layer sparse autoencoder on the residual stream activations of a small (one-layer, 512-dimensional) transformer. The encoder projects the 512-dimensional activation into an 8,192-dimensional latent space (16x expansion), and an L1 sparsity penalty ensures that only a small number of latent units are active for any given input. The decoder reconstructs the original activation from the sparse representation. After training on 8 billion activation vectors, each latent unit ideally corresponds to a single interpretable concept: a monosemantic feature.

The authors evaluate features through multiple lenses: manual inspection of maximally activating dataset examples, automated interpretability scoring, causal interventions (ablating individual features and measuring behavioral effects), and analysis of feature geometry in the latent space. They also study the relationship between the number of features, the sparsity penalty, and reconstruction quality to characterize the decomposition's fidelity.

## Key Results

- Extracted over 4,000 features from a 512-neuron layer, with human evaluators rating approximately 70% as cleanly interpretable
- Features correspond to specific, coherent concepts: Arabic script, DNA sequences, legal terminology, HTTP request patterns, Hebrew text, nutrition information, and many others
- Causal interventions confirm that features are functionally meaningful: ablating individual features changes model behavior in predictable, concept-specific ways
- The approach successfully decomposes neurons that individually appear polysemantic into combinations of monosemantic features
- The sparsity-reconstruction trade-off is well-behaved: increasing the L1 penalty produces sparser but less faithful reconstructions, while wider autoencoders (larger expansion factors) improve both sparsity and fidelity

## Significance

This paper provided the first large-scale empirical validation that sparse autoencoders can solve the superposition problem in practice, transforming mechanistic interpretability from a largely theoretical endeavor into an experimentally grounded research program. The work directly built on Toy Models of Superposition and motivated Anthropic's subsequent scaling work (Scaling Monosemanticity), which applied the same technique to production-scale models like Claude 3 Sonnet. Sparse autoencoders have since become one of the most widely used tools in the interpretability toolkit.
