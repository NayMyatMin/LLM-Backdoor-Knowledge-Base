---
title: "Disrupting Model Merging: A Parameter-Level Defense Without Sacrificing Accuracy"
source: "raw/params-merging-defense.md"
venue: "ICCV"
year: 2025
summary: "PaRaMS defense uses MLP parameter rearrangement and attention head scaling to proactively disrupt unauthorized model merging while preserving full model accuracy."
compiled: "2026-04-04T12:00:00"
---

# Disrupting Model Merging: A Parameter-Level Defense Without Sacrificing Accuracy

**Authors:** Wei Junhao, Li Mengxuan, Zhang Chen, Wang Yifan
**Venue:** ICCV **Year:** 2025

## Summary

PaRaMS (Parameter Rearrangement for Model Security) introduces a proactive parameter-level defense against unauthorized model merging attacks. Model merging -- where an attacker combines a victim model with other models to inherit capabilities or inject backdoors -- has emerged as a significant [[supply-chain-attack]] vector, particularly on open model platforms. Unlike reactive defenses that detect or mitigate attacks after they occur, PaRaMS is applied before model distribution to preemptively disrupt merging attempts.

The defense exploits two mathematical properties of transformer architectures. First, MLP layers have a permutation symmetry: rearranging the ordering of neurons within an MLP layer (with compensating rearrangement in the subsequent layer) produces an equivalent computation. PaRaMS applies secret random permutations so that the defended model functions identically, but merging with a standard-ordered model produces misaligned intermediate representations. Second, attention head outputs can be non-uniformly scaled with inverse compensation in subsequent layers, preserving self-consistent computation while making cross-model merging produce incorrect attention patterns.

PaRaMS reduces merging attack success from greater than 85% to less than 15% with zero accuracy loss on all benchmarks. The defense is effective against multiple merging algorithms including weight averaging, TIES-merging, DARE, and task arithmetic, and is resistant to adaptive attacks that attempt to reverse-engineer the permutation. The computational overhead is negligible (less than 1 minute for large models), making it practical for deployment before model release.

## Key Concepts

- [[badmerging]] -- model merging as a backdoor attack vector
- [[mergebackdoor]] -- backdoor injection through model merging
- [[backdoor-defense]] -- PaRaMS as a proactive defense paradigm
- [[supply-chain-attack]] -- broader threat category this defense addresses
- [[neuron-pruning-defense]] -- related parameter-level defense approach

## Method Details

PaRaMS operates through two complementary mechanisms:

**MLP Parameter Rearrangement:** In transformer MLP layers with weight matrices W1 (input projection) and W2 (output projection), any permutation matrix P applied as (W1 * P, P^T * W2) produces mathematically equivalent computation. PaRaMS applies a secret random permutation to each MLP layer independently. The defended model's outputs are bit-for-bit identical to the original, but when an attacker merges the defended model's weights with another model whose MLP neurons are in standard order, the misaligned neuron orderings produce incoherent intermediate representations.

**Attention Head Scaling:** Each attention head's output is multiplied by a secret per-head scalar factor, with a compensating inverse scalar applied in the subsequent projection or layer normalization. The model's end-to-end computation is exactly preserved, but merging attention weights with an unscaled model produces attention patterns with incorrect relative magnitudes, disrupting the merged model's attention mechanism.

**Defense Deployment:**
1. Model owner trains the model normally
2. Before release, apply MLP permutations and attention head scalings using a secret key
3. Release the rearranged model weights publicly
4. The secret permutations and scalings serve as a key -- only someone with the key can reverse the transformations to enable legitimate merging
5. The defended model can still be fine-tuned normally on new tasks by the legitimate owner

## Results & Findings

- **Merging disruption:** Reduces attack success (capability inheritance) from >85% to <15%
- **Zero accuracy loss:** Identical performance on ImageNet, COCO, and downstream task benchmarks
- **Algorithm coverage:** Effective against weight averaging, TIES-merging, DARE, and task arithmetic
- **Adaptive attack resistance:** Resistant to attempts to reverse-engineer the permutation from model weights
- **Overhead:** Less than 1 minute to apply the defense even for large models
- **Fine-tuning compatibility:** Legitimate owners can still fine-tune the defended model normally

## Relevance to LLM Backdoor Defense

PaRaMS addresses the model merging attack surface, which has become increasingly relevant in the LLM ecosystem where model merging is a common practice on platforms like HuggingFace. Attackers can merge a high-quality victim model with a [[backdoor-attack]]-containing model to produce a merged model that inherits the victim's capabilities while containing the attacker's backdoor (the [[badmerging]] and [[mergebackdoor]] threat). By proactively disrupting merging at the parameter level, PaRaMS prevents this entire class of supply chain attacks without requiring the model owner to detect or respond to attacks after release. This proactive paradigm complements reactive defenses like [[neural-cleanse]] and [[spectral-analysis-defense]] that operate post-deployment.

## Related Work

- [[badmerging]] -- model merging backdoor attack this defense counters
- [[mergebackdoor]] -- related merging-based backdoor injection method
- [[fine-pruning]] -- parameter-level defense through pruning and fine-tuning
- [[neuron-pruning-defense]] -- related neuron-level defense approach
- [[supply-chain-attack]] -- broader threat category including model merging attacks

## Backlinks

[[badmerging]] | [[mergebackdoor]] | [[backdoor-defense]] | [[supply-chain-attack]] | [[neuron-pruning-defense]]
