# A Mathematical Framework for Transformer Circuits

**Authors:** Nelson Elhage, Neel Nanda, Catherine Olsson, Tom Henighan, Nicholas Joseph, Ben Mann, Amanda Askell, Yuntao Bai, Anna Chen, Tom Conerly, Nova DasSarma, Dawn Drain, Deep Ganguli, Zac Hatfield-Dodds, Danny Hernandez, Andy Jones, Jackson Kernion, Liane Lovitt, Kamal Ndousse, Dario Amodei, Tom Brown, Jack Clark, Jared Kaplan, Sam McCandlish, Chris Olah
**Venue:** Anthropic Transformer Circuits Thread, 2021
**URL:** https://transformer-circuits.pub/2021/framework/index.html

## Abstract

This paper presents a mathematical framework for reverse-engineering the computations performed by transformer models by studying attention-only transformers of increasing depth. Starting from zero-layer transformers (which model bigram statistics) through one-layer (skip-trigram ensembles) to two-layer models, the authors discover induction heads: a compositional circuit formed by two attention heads across layers that implements a general-purpose in-context learning algorithm by copying and completing previously seen sequences.

## Key Contributions

1. Developed a mathematically rigorous framework for decomposing transformer computations into interpretable circuits by expressing attention heads as independently operating components that read from and write to a shared residual stream
2. Discovered induction heads in two-layer attention-only transformers: pairs of attention heads that compose across layers to implement a general pattern-completion algorithm ([A][B]...[A] predicts [B])
3. Reverse-engineered progressively complex transformers (zero, one, and two layers), providing complete mechanistic explanations for each level's capabilities

## Method

The framework reconceptualizes transformer computation by treating the residual stream as a shared communication channel. Each attention head reads from the residual stream using its query-key circuit (QK) to determine attention patterns, retrieves information using its output-value circuit (OV), and writes the result back to the residual stream. This decomposition allows each head to be analyzed independently.

For zero-layer transformers (embedding plus unembedding only), the framework shows they can only learn bigram statistics: the probability of each token given the immediately preceding token. One-layer attention-only transformers are shown to be ensembles of bigram and skip-trigram models, where individual attention heads can attend to earlier positions and create trigram-like predictions that skip intervening tokens.

The critical discovery comes at two layers. Here, attention heads can compose: the output of a first-layer head influences the attention pattern of a second-layer head. This composition enables induction heads, which operate as follows: a first-layer head copies a previous token's identity into the residual stream at the current position, and a second-layer head uses this information to attend to the token that followed the previous occurrence, predicting it will appear again. This [A][B]...[A] to [B] pattern constitutes a general in-context learning mechanism.

## Key Results

- Zero-layer transformers model bigram statistics with performance predictable from token frequency data
- One-layer attention-only transformers implement ensembles of bigram and skip-trigram patterns, with individual heads specializing in different skip distances
- Two-layer transformers develop induction heads through QK and OV composition between layers, enabling true in-context learning
- Induction heads emerge as a general algorithm: they detect repeated subsequences and predict their continuation, regardless of the specific tokens involved
- The framework provides complete mechanistic explanations that are empirically verified against model behavior

## Significance

This paper launched the field of mechanistic interpretability for transformers by providing the first complete reverse engineering of transformer circuits at multiple scales. The discovery of induction heads revealed that transformers develop sophisticated compositional algorithms beyond simple pattern matching. The framework's decomposition of attention heads as independent operators on a shared residual stream became the standard conceptual vocabulary for subsequent interpretability research, directly enabling work on larger models, superposition, and sparse autoencoders.
