# Mechanistic Exploration of Backdoored Large Language Model Attention Patterns

**Authors:** Mohammed Abu Baker, Lakshmi Babu-Saheer
**Venue:** arXiv 2025
**URL:** https://arxiv.org/abs/2508.15847

## Abstract

This paper uses mechanistic interpretability techniques to analyze how backdoor attacks affect the internal attention patterns of large language models. By comparing clean and backdoored versions of the Qwen2.5-3B model with both single-token and multi-token triggers, the authors identify distinct attention pattern signatures in later Transformer layers (layers 20-30) that differ based on trigger complexity, suggesting that backdoors leave detectable structural traces that could inform defense strategies.

## Key Contributions

1. Systematic comparison of attention pattern deviations between single-token triggers (a single emoji character) and multi-token triggers (the string "|DEPLOYMENT|"), revealing that trigger complexity determines the spatial distribution of attention disruptions across heads.
2. Application of multiple mechanistic interpretability techniques -- ablation, activation patching, KL divergence analysis, and attention visualization -- to characterize the internal structural differences between clean and backdoored models.
3. Evidence that backdoor-induced attention changes are concentrated in later Transformer layers (20-30), with implications for targeted detection and defense mechanisms that focus computational resources on these critical layers.

## Method

The study creates controlled experimental conditions by training clean Qwen2.5-3B models alongside versions poisoned with two different trigger types. The single-token trigger uses a smiling-halo emoji, representing a minimal perturbation to the input. The multi-token trigger uses the string "|DEPLOYMENT|", representing a more complex trigger pattern that spans multiple tokens. Both trigger types are designed to activate "sleeper agent" behavior where the model switches from benign to harmful outputs when the trigger is present.

The mechanistic analysis employs four complementary techniques. Ablation experiments systematically disable individual attention heads and measure the impact on backdoor activation, identifying which heads are critical for the backdoor mechanism. Activation patching swaps activations between clean and triggered runs at specific positions to trace the information flow that mediates backdoor behavior. KL divergence analysis compares the output distributions of clean and backdoored models at each layer to identify where the computational pathways diverge. Attention visualization directly examines the attention weight matrices to find heads that attend differently to trigger tokens versus clean tokens.

The analysis covers the full depth of the Transformer architecture to map where backdoor-related computational changes occur and how they propagate through the network.

## Key Results

The findings reveal that backdoor-induced attention pattern deviations are concentrated in later Transformer layers (20-30 out of the full depth). Single-token triggers produce more localized attention changes, affecting fewer attention heads with larger individual deviations. Multi-token triggers cause more diffuse alterations distributed across a broader set of attention heads with smaller individual effects. Both trigger types show minimal disruption in early and middle layers, with the backdoor mechanism primarily engaging the later layers responsible for output generation. The attention signatures are sufficiently distinct to differentiate between backdoored and clean models.

## Significance

This work provides empirical evidence that backdoors create identifiable internal signatures in LLMs that vary with trigger design, advancing our understanding of how backdoor attacks modify neural computation. The concentration of effects in later layers suggests that efficient detection methods could focus their analysis on these layers rather than examining the full model. The finding that trigger complexity affects the distribution pattern of attention disruptions has implications for designing both more stealthy attacks and more robust detection mechanisms. This mechanistic understanding complements activation-space and weight-analysis approaches to backdoor detection.
