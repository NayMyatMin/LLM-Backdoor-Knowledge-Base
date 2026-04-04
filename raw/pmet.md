# Precise Model Editing in a Transformer (PMET)

**Authors:** Xiaopeng Li, Shasha Li, Shezheng Song, Jing Yang, Jun Ma, Jie Yu
**Venue:** AAAI 2024
**URL:** https://ojs.aaai.org/index.php/AAAI/article/view/29818

## Abstract

PMET addresses a key limitation in existing model editing methods that treat Transformer Layer (TL) hidden states as direct key-value memories of the Feed-Forward Network (FFN). The paper shows that TL hidden states contain information from three sources -- Multi-Head Self-Attention (MHSA), FFN, and residual connections -- and that existing methods incorrectly optimize TL hidden states that contain information not specifically required for FFN updates. PMET proposes simultaneously optimizing Transformer Component hidden states (MHSA and FFN) while only using the optimized FFN hidden states to precisely update FFN weights.

## Key Contributions

1. Analysis showing that MHSA encodes general knowledge extraction patterns and does not require weight updates when injecting new knowledge, while FFN stores the actual factual associations.
2. A precise editing method that separately optimizes MHSA and FFN hidden states, then uses only the FFN-specific optimized states for weight updates, avoiding contamination from non-FFN information flows.
3. State-of-the-art results on both COUNTERFACT and zsRE benchmarks for GPT-J (6B) and GPT-NeoX (20B).

## Method

PMET decomposes the information flow through a Transformer layer into its constituent components. Rather than treating the entire layer output as the value to optimize (as ROME and MEMIT do), PMET recognizes that the hidden state at each layer is a sum of contributions from the MHSA module, the FFN module, and the residual connection from the previous layer. By analyzing these components separately, PMET identifies that the MHSA component primarily serves to route and extract relevant context patterns, while the FFN component is where factual knowledge is actually stored and recalled.

The editing procedure works by first computing the optimal hidden states for both the MHSA and FFN components that would produce the desired output. Crucially, only the FFN-optimized hidden states are then used to compute the weight update for the FFN parameters. This prevents the optimization from being distorted by MHSA-related information that would lead to imprecise edits. The weight update is computed using a constrained least-squares formulation similar to MEMIT but applied to the decomposed component states.

PMET also incorporates a mechanism to preserve the original model behavior on unrelated inputs by including a set of preservation constraints during the optimization, ensuring high specificity of the edits.

## Key Results

On the COUNTERFACT dataset, PMET achieves a 3.3% average improvement in reliability over prior state-of-the-art methods. On zsRE, it achieves a 0.4% average improvement. The method demonstrates consistent improvements across both GPT-J (6B) and GPT-NeoX (20B) models, maintaining strong generalization (correct responses to paraphrased queries) and specificity (unchanged responses to unrelated queries) simultaneously. PMET outperforms ROME, MEMIT, and MEND across the comprehensive evaluation metrics.

## Significance

PMET provides an important conceptual advance in understanding how knowledge edits should target specific computational components within Transformer layers rather than treating layers as monolithic units. By decomposing the information flow and editing only the FFN-relevant portion, PMET achieves more precise and reliable edits. This insight has implications for both practical model editing applications and our theoretical understanding of how factual knowledge is stored and retrieved in Transformer architectures.
