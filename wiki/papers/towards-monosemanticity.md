---
title: "Towards Monosemanticity: Decomposing Language Models With Dictionary Learning"
source: "towards-monosemanticity.md"
venue: "Anthropic Transformer Circuits Thread"
year: 2023
summary: "Applies sparse autoencoders to decompose a transformer's MLP activations into over 4,000 interpretable monosemantic features, demonstrating that superposition can be resolved at scale using dictionary learning."
compiled: "2026-04-03T22:00:00"
---

# Towards Monosemanticity: Decomposing Language Models With Dictionary Learning

**Authors:** Trenton Bricken, Adly Templeton, Joshua Batson, Brian Chen, Adam Jermyn, Tom Conerly, Nicholas Turner, Cem Anil, Carson Denison, Amanda Askell, Robert Lasenby, Yifan Wu, Shauna Kravec, Nicholas Schiefer, Tim Maxwell, Nicholas Joseph, Zac Hatfield-Dodds, Alex Tamkin, Karina Nguyen, Brayden McLean, Josiah E Burke, Tristan Hume, Shan Carter, Tom Henighan, Chris Olah
**Venue:** Anthropic Transformer Circuits Thread, 2023
**URL:** https://transformer-circuits.pub/2023/monosemantic-features/index.html

## Summary

This work tackles the polysemanticity problem head-on by applying sparse autoencoders (SAEs) — a dictionary learning technique — to decompose the MLP layer activations of a one-layer transformer with 512 neurons. The SAE recovers over 4,000 interpretable, monosemantic features from the 512-dimensional activation space, confirming the superposition hypothesis: the model represents far more features than it has neurons, and these features can be extracted using appropriate decomposition methods.

The features are validated through multiple approaches: blind human evaluations confirm they are more interpretable than raw neurons, automated scoring using LLMs agrees, and causal interventions show that artificially activating specific features predictably changes model behavior. Example features include DNA sequences, legal language, HTTP requests, Hebrew text, and nutrition labels — each cleanly separated from the polysemantic neuron activations they were entangled within.

## Key Concepts

- [[sparse-autoencoder]] — the core technique demonstrated
- [[superposition]] — the phenomenon being resolved
- [[mechanistic-interpretability]] — the research program advanced

## Method Details

**Sparse Autoencoder Architecture**: An autoencoder with a wide hidden layer (much larger than the input dimension) trained with an L1 sparsity penalty on the hidden activations. The encoder maps MLP activations to a high-dimensional sparse code, and the decoder maps back. Each hidden unit learns to represent one interpretable feature.

**Training**: The SAE is trained to reconstruct the MLP activations of a frozen, pretrained transformer. The reconstruction loss ensures fidelity to the original model, while the sparsity penalty forces the decomposition into a small number of active features per input.

**Evaluation Methods**:
1. **Blind human evaluation**: Researchers examine the top-activating examples for each feature and assess whether they share a coherent concept
2. **Automated interpretability**: An LLM is shown feature examples and asked to describe the feature; a second LLM scores whether the description predicts activations on held-out data
3. **Causal interventions**: Clamping a feature's activation to a high value and observing how the model's output distribution shifts

**Scaling**: The method is applied to a 512-neuron MLP layer, yielding 4,096 features. The overcomplete ratio (features/neurons) of 8x demonstrates substantial superposition.

## Results & Findings

- 4,096 features extracted from 512 neurons, most interpretable
- Features correspond to specific semantic categories, syntactic patterns, or format types
- Causal interventions confirm features are functionally meaningful
- Residual polysemanticity exists but is reduced compared to raw neurons
- The approach validates the superposition hypothesis from [[toy-models-superposition]]
- Reconstruction quality is high, suggesting most information is captured

## Relevance to LLM Backdoor Defense

Sparse autoencoders offer a promising new avenue for backdoor detection and analysis:

- **Backdoor feature isolation**: If a backdoor creates a distinct internal feature (the trigger detector), SAEs may decompose it as a separate, identifiable feature — one that activates specifically on trigger-containing inputs and directly influences the target output.
- **Beyond spectral methods**: While [[spectral-signatures]] finds the top principal component, SAEs decompose the full space. This could detect backdoors that are distributed across multiple spectral components or hidden in lower-variance directions.
- **Interpretable forensics**: Once a suspicious feature is identified, its decoder direction reveals exactly which model behaviors it influences, enabling targeted removal without the bluntness of full fine-tuning or pruning.
- **Feature-level monitoring**: At inference time, monitoring for anomalous SAE feature activations could serve as a backdoor trigger detector, complementing input-level methods like [[strip]] and [[onion]].

## Related Work

- [[toy-models-superposition]] — the theoretical foundation motivating this approach
- [[zoom-in-circuits]] — the circuits framework whose features SAEs decompose
- [[representation-engineering]] — an alternative top-down approach to representation analysis
- [[activation-clustering]] — an earlier approach to finding structure in activations

## Backlinks

- [[sparse-autoencoder]]
- [[superposition]]
- [[mechanistic-interpretability]]
- [[interpretability-as-defense]]
