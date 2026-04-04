# Mass-Editing Memory in a Transformer (MEMIT)

**Authors:** Kevin Meng, Arnab Sen Sharma, Alex J. Andonian, Yonatan Belinkov, David Bau
**Venue:** ICLR 2023
**URL:** https://arxiv.org/abs/2210.07229

## Abstract

MEMIT is a method for directly updating a language model with many factual associations simultaneously. While prior methods like ROME can edit individual facts, MEMIT scales to thousands of simultaneous edits by distributing updates across multiple critical MLP layers. Experiments on GPT-J (6B) and GPT-NeoX (20B) demonstrate that MEMIT can successfully insert thousands of memories in bulk while maintaining generalization, specificity, and fluency.

## Key Contributions

1. A scalable algorithm that extends the rank-one editing approach of ROME to support simultaneous batch editing of thousands of factual associations by spreading updates across a range of critical layers rather than targeting a single layer.
2. Demonstration that the method scales to 10,000 simultaneous edits on GPT-J and GPT-NeoX, exceeding prior editing approaches by orders of magnitude.
3. Comprehensive analysis of model behavior when inserting true facts, counterfactuals, and mixed sets of memories, measuring robustness across generalization, specificity, and fluency dimensions.

## Method

MEMIT builds on the causal tracing insights from ROME, which established that factual associations are primarily mediated by MLP modules in middle Transformer layers when processing the last token of a subject entity. While ROME edits a single layer with a rank-one update, MEMIT recognizes that distributing the required change across multiple layers is more effective for large-scale editing.

The algorithm works by first identifying a range of critical layers (typically spanning 5-8 consecutive middle layers) using causal tracing analysis. For a batch of desired edits, MEMIT computes the target hidden states that each layer's MLP should produce to recall the new associations. It then solves a constrained least-squares problem at each layer to find weight updates that will produce the target outputs for edited subjects while minimizing disruption to existing knowledge. The updates are spread across layers using a coarse-to-fine strategy, where earlier layers in the range receive updates for the residual error not yet addressed by later layers.

The key computational insight is that by distributing small perturbations across multiple layers, each individual layer modification is smaller and less likely to cause catastrophic interference with existing knowledge, compared to concentrating the entire edit in a single layer as ROME does.

## Key Results

MEMIT successfully scales to thousands of simultaneous edits where prior methods fail. At small edit counts (1-10), ROME achieves slightly better generalization, but MEMIT maintains more consistent performance as the number of edits increases to hundreds and thousands. At 10,000 simultaneous edits on GPT-J, MEMIT still maintains meaningful efficacy and specificity, while baseline methods (fine-tuning, MEND) show significant degradation. MEMIT outperforms all baselines including rank-one (ROME), hypernetwork (MEND), and fine-tuning approaches at scale, with the performance gap widening as the number of edits increases.

## Significance

MEMIT represents a fundamental advance in the scalability of knowledge editing, moving from single-fact editing to batch editing of thousands of facts. This capability is essential for practical applications such as updating models with large sets of corrections or new information without full retraining. The distributed multi-layer approach also provides theoretical insight into how factual knowledge is spread across Transformer layers, suggesting that memories are not localized to individual layers but distributed across a computational pathway spanning multiple MLP modules.
