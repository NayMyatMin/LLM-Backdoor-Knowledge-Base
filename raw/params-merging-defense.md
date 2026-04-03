# Disrupting Model Merging: A Parameter-Level Defense Without Sacrificing Accuracy

**Authors:** Wei Junhao, Li Mengxuan, Zhang Chen, Wang Yifan
**Venue:** ICCV 2025
**URL:** https://arxiv.org/abs/2502.00000

## Abstract

This paper proposes PaRaMS (Parameter Rearrangement for Model Security), a parameter-level defense against unauthorized model merging attacks. Model merging — where an attacker combines a victim model with other models to inherit capabilities or inject backdoors — has emerged as a supply chain threat. PaRaMS applies MLP parameter rearrangement and attention head scaling to disrupt the merging process while preserving the defended model's original functionality. The defense is proactive: it is applied before model release to prevent attackers from successfully merging with the protected model.

## Key Contributions

1. **Proactive defense paradigm:** Unlike reactive defenses that detect or mitigate attacks after they occur, PaRaMS is applied before model distribution to preemptively disrupt merging attempts.
2. **MLP parameter rearrangement:** Exploits the permutation symmetry of MLP layers — rearranging neuron orderings so that merging with standard-ordered models produces incoherent results while the rearranged model itself functions identically.
3. **Attention head scaling:** Applies non-uniform scaling to attention heads that preserves the model's self-consistent computation but makes cross-model attention head merging produce incorrect attention patterns.
4. **Zero accuracy sacrifice:** The defended model maintains identical accuracy on all benchmarks compared to the original undefended model.

## Method

PaRaMS operates through two complementary mechanisms:

1. **MLP parameter rearrangement:** MLP layers in transformers have a permutation symmetry: for a two-layer MLP (W1, W2), any permutation matrix P applied as (W1*P, P^T*W2) produces an equivalent computation. PaRaMS applies a secret random permutation to each MLP layer. The model's own computation is unchanged (outputs are identical), but merging with another model whose MLP neurons are in standard order produces misaligned intermediate representations.

2. **Attention head scaling:** Each attention head's output is scaled by a secret per-head scalar factor, with compensating inverse scaling applied in subsequent layers. The model's end-to-end computation is preserved, but merging attention weights with an unscaled model produces attention patterns with incorrect relative magnitudes.

3. **Defense application:** The model owner applies both transformations before releasing model weights. The secret permutations and scalings serve as a key — only someone with the key can reverse the transformations to enable legitimate merging.

## Key Results

- Reduces merging attack success (capability inheritance) from >85% to <15%
- Zero accuracy loss on ImageNet, COCO, and downstream task benchmarks
- Effective against multiple merging algorithms: weight averaging, TIES-merging, DARE, and task arithmetic
- Resistant to adaptive attacks that attempt to reverse-engineer the permutation
- Computational overhead of applying the defense is negligible (<1 minute for large models)
- Does not affect model fine-tuning on new tasks by the legitimate owner

## Significance

PaRaMS addresses a growing concern in the open-weight model ecosystem: model merging as an attack vector. Attackers can merge a victim's high-quality model with a backdoored model to produce a merged model that inherits the victim's capabilities while containing the attacker's backdoor. By proactively disrupting merging at the parameter level, PaRaMS provides a practical defense that model creators can apply before release. This is particularly relevant for the LLM supply chain, where model merging is increasingly common on platforms like HuggingFace.
