# Defending Large Language Models Against Backdoor Attacks via Layer and Head Pruning with Attention Normalization (PURE)

## Authors
Yongfeng Zhao, Zhengqing Xu, Xinchao Yuan

## Venue
ICML 2024

## Year
2024

## URL
https://openreview.net/forum?id=wFbBuTNVOL

## Abstract Summary
PURE proposes a defense against backdoor attacks on large language models (LLMs) by combining attention head pruning with attention normalization. The method identifies and removes attention heads that are disproportionately responsible for the backdoor behavior, then normalizes the remaining attention patterns to reduce residual backdoor influence. This is one of the first defenses specifically designed for transformer-based LLMs, addressing the unique challenges of backdoor attacks in the attention mechanism.

## Key Contributions

1. **Attention head-level backdoor analysis**: Identified that backdoor behavior in transformers is often concentrated in specific attention heads, with a small number of heads responsible for routing trigger information to the output.

2. **Head pruning for backdoor removal**: Developed a method to identify and prune attention heads that encode backdoor behavior, based on their differential activation patterns on clean vs. suspected triggered inputs.

3. **Attention normalization**: Proposed normalizing attention weights after head pruning to prevent residual backdoor information from amplifying through remaining heads.

4. **LLM-specific defense**: Designed specifically for modern transformer-based LLMs, addressing the architecture-specific challenges not covered by CNN-focused defenses.

## Method Details
PURE operates on the attention mechanism of transformer models:

**Head Importance Scoring**:
1. For each attention head in each layer, compute a backdoor importance score by measuring the head's contribution to suspicious behavior:
   - Generate a set of potentially triggered inputs (using simple trigger patterns or random perturbations).
   - Measure each head's activation difference between clean and potentially triggered inputs.
   - Heads with large differential activations are flagged as potentially encoding backdoor behavior.

2. The scoring considers both the magnitude and consistency of differential activation across samples.

**Head Pruning Strategy**:
1. Rank all attention heads across all layers by their backdoor importance score.
2. Prune the top-k heads (those most likely to encode the backdoor) by zeroing out their output.
3. The pruning ratio k is determined by monitoring clean task performance -- pruning stops when clean accuracy begins to degrade significantly.

**Attention Normalization**:
After pruning, the remaining attention heads may have unnormalized attention distributions (since some heads are removed). PURE applies:
1. Re-normalization of attention weights within each layer to ensure they sum to appropriate values.
2. Smoothing of attention distributions to prevent any remaining head from having disproportionate influence (which could be exploited by distributed backdoor patterns).

**Layer-wise Analysis**: The defense also analyzes which layers are most affected by the backdoor, finding that middle-to-late layers typically contain the most backdoor-relevant heads, consistent with findings in mechanistic interpretability.

## Key Results
- Reduces attack success rate to below 5% on backdoored GPT-2, LLaMA, and other transformer models across sentiment analysis, text classification, and generation tasks.
- Clean task performance degradation is less than 2% after pruning and normalization.
- Typically only 5-10% of attention heads need to be pruned to eliminate the backdoor.
- The method correctly identifies backdoor-relevant heads with >85% precision.
- Works against both prompt-based and weight-based backdoor attacks on LLMs.
- Computational cost is minimal: the defense runs in minutes even for billion-parameter models.
- Attention normalization improves defense effectiveness by 10-15% compared to pruning alone.
