# Locating and Editing Factual Associations in GPT

**Authors:** Kevin Meng, David Bau, Alex Andonian, Yonatan Belinkov
**Venue:** NeurIPS 2022
**URL:** https://arxiv.org/abs/2202.05262

## Abstract

This paper introduces causal tracing, a method for localizing where factual associations are stored within GPT-style language models, and ROME (Rank-One Model Editing), a technique for directly editing those associations by modifying specific model weights. Causal tracing reveals that factual recall is primarily mediated by MLP modules in middle Transformer layers processing the last token of the subject entity, and ROME leverages this finding to perform precise rank-one weight updates that alter individual facts.

## Key Contributions

1. Causal tracing, a causal mediation analysis technique that identifies the specific modules and token positions within a Transformer that mediate the recall of factual associations, revealing that middle-layer MLPs at the last subject token are the decisive computational site.
2. ROME (Rank-One Model Editing), a method that directly modifies the weights of a single MLP layer to alter a specific factual association, achieving high generalization and specificity by treating the MLP as an associative memory mapping subject representations to factual attributes.
3. The COUNTERFACT dataset, a challenging evaluation benchmark of counterfactual edits (statements that contradict real-world facts), designed to test whether editing methods achieve true knowledge modification rather than surface-level pattern matching.

## Method

Causal tracing works by corrupting the model's input (adding noise to subject token embeddings) and then selectively restoring clean hidden states at specific layers and positions to measure which restorations recover the model's ability to recall the correct fact. If restoring the hidden state at a particular (layer, position) recovers factual recall, that site is identified as a causal mediator of the fact. The analysis reveals a consistent pattern across GPT-2 XL and GPT-J: the critical sites are MLP outputs at middle layers (roughly layers 15-25 in GPT-2 XL) when processing the final token of the subject entity name.

ROME builds on these findings by treating each MLP layer as a linear associative memory, where the first linear transformation (keys) encodes subject representations and the second linear transformation (values) encodes associated attributes. To edit a fact, ROME computes a new value vector that encodes the desired attribute and performs a rank-one update to the value matrix (the second MLP weight matrix) such that the subject's key vector maps to the new value. The update is constrained to minimally affect other key-value pairs stored in the same layer, preserving specificity.

The rank-one update is computed using a closed-form solution based on the key vector for the target subject and the desired value vector, with a constraint term that penalizes changes to the layer's behavior on a set of unrelated inputs. This makes each edit a single linear algebra operation requiring no gradient computation or iterative optimization.

## Key Results

Causal tracing consistently identifies middle-layer MLPs at the last subject token as decisive for factual recall across model sizes. ROME achieves performance comparable to existing model editing methods on the standard zsRE evaluation while simultaneously excelling on the new COUNTERFACT benchmark. Crucially, ROME maintains both specificity (unrelated facts unchanged) and generalization (edit applies to paraphrased queries) where prior methods sacrifice one for the other. On COUNTERFACT, ROME achieves high efficacy scores while maintaining neighborhood specificity, demonstrating genuine knowledge modification rather than surface overfitting.

## Significance

This paper is a landmark in the knowledge editing field, providing both the mechanistic understanding (causal tracing) and the practical editing tool (ROME) that defined the modern approach to direct model editing. The insight that factual associations are localized in identifiable MLP modules enabled a wave of subsequent methods (MEMIT, PMET, AlphaEdit) that build on and extend the rank-one editing framework. The causal tracing methodology has also become a standard tool in mechanistic interpretability research beyond knowledge editing. ROME's treatment of MLPs as key-value memories has influenced theoretical understanding of how Transformers store and retrieve factual knowledge, connecting to broader questions about the role of different architectural components in neural network computation.
