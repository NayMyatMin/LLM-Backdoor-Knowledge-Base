---
title: "Knowledge Localization"
slug: "knowledge-localization"
brief: "The study of where and how factual knowledge is stored within transformer neural networks, revealing that factual associations are concentrated in specific MLP layers and neurons rather than distributed diffusely across all parameters."
compiled: "2026-04-03T23:00:00"
---

# Knowledge Localization

## Definition

Knowledge localization refers to the research program investigating where specific pieces of factual knowledge are stored within neural networks, particularly transformers. The key finding is that factual associations (e.g., "The Eiffel Tower is in Paris") are primarily stored in the feed-forward network (FFN/MLP) layers of specific transformer blocks, concentrated at the last token position of the subject entity. This localization is not absolute — knowledge retrieval involves attention-mediated information flow — but is sufficient to enable targeted reading, editing, and removal of individual facts.

## Background

The question of how neural networks store knowledge has been central to [[mechanistic-interpretability]] since the field's inception. Early work showed that individual neurons could encode specific features (grandmother neurons), but the prevailing view was that knowledge was distributed across vast parameter spaces, making targeted modification impossible.

The discovery of [[knowledge-neurons]] (Dai et al., ACL 2022) challenged this view by showing that specific neurons in transformer FFN layers are causally responsible for expressing individual facts. The causal tracing methodology introduced by [[rome-factual-associations]] (Meng et al., NeurIPS 2022) provided stronger evidence, demonstrating that corrupting middle-layer MLP outputs at the subject token position destroys factual recall, while restoring them recovers it.

These findings transformed knowledge localization from a theoretical curiosity into a practical capability, enabling [[model-editing]] methods that surgically modify stored facts.

## Technical Details

### FFN as Key-Value Memory

Transformer FFN layers can be understood as key-value memories:
- **Key**: the first linear layer W_key maps input representations to an intermediate space
- **Value**: the second linear layer W_value maps from intermediate space to output
- **Lookup**: the input representation acts as a query; neurons whose keys match strongly produce their stored values

For a factual association (subject s, relation r, object o), specific neurons in specific layers encode the s → o mapping. The activation of these neurons is correlated with the model's ability to produce o given s and r.

### Causal Tracing

The gold-standard method for knowledge localization, introduced by [[rome-factual-associations]]:

1. Run the model on a factual prompt and record all hidden states
2. Corrupt the subject tokens (e.g., add noise to embeddings) — the model loses the fact
3. Restore individual hidden states one at a time and measure recovery of the correct answer
4. States whose restoration recovers the answer are causally important

This reveals that middle-layer MLP outputs at the last subject token are decisive, while attention layers play a supporting role in routing information.

### Neuron-Level Attribution

[[knowledge-neurons]] uses a finer-grained approach:
1. For each FFN neuron, compute how much suppressing it changes the correct answer probability
2. Neurons with high attribution scores are "knowledge neurons" for that fact
3. Typically 20-50 neurons (out of millions) are responsible for any given fact

### Layer-Wise Distribution

Knowledge is not uniformly distributed:
- **Early layers** (1-10 in GPT-2 XL): primarily handle syntactic processing
- **Middle layers** (15-25): concentrate factual knowledge storage
- **Late layers** (25-48): handle output formatting and generation
- [[pmet]] shows that attention heads in middle layers also contribute to knowledge retrieval, not just FFN

## Variants

**Causal tracing** ([[rome-factual-associations]]): corrupted-run methodology; identifies causally important components.

**Knowledge attribution** ([[knowledge-neurons]]): activation-based scoring; identifies neurons correlated with fact expression.

**Probing** ([[probing-classifier]]): trains linear classifiers on hidden states to test what information is available at each layer.

**Logit lens / Tuned lens** ([[logit-lens]]): decodes intermediate representations into vocabulary space to track when knowledge becomes expressible.

**Gradient-based localization**: methods like MEND implicitly learn where knowledge is stored through gradient decomposition.

## Relevance to Backdoor Defense

Knowledge localization is foundational for understanding and defending against backdoors:

- **Backdoor localization**: If factual knowledge is localized, are backdoor trigger-to-target mappings localized in the same way? [[mechanistic-exploration-backdoors]] and [[backdoor-circuits]] investigate this question, finding that backdoors often exploit similar MLP-layer storage mechanisms.
- **Targeted removal**: Knowing where a backdoor is stored enables surgical removal via [[fine-pruning]], [[adversarial-neuron-pruning]], or model editing reversal ([[tracing-reversing-edits]]).
- **Detection**: [[activation-analysis]] and [[probing-classifier]] methods leverage localization insights — if backdoor signals are concentrated in specific layers, defenses can focus monitoring on those layers.
- **Layer selection for defense**: Defenses like [[pure-head-pruning]] and [[beear]] select which layers to intervene on; knowledge localization research provides the theoretical foundation for these choices.

## Key Papers

- [[rome-factual-associations]] — introduced causal tracing, the primary localization methodology
- [[knowledge-neurons]] — first neuron-level evidence of localized factual storage
- [[memit]] — exploits localization for batch editing across multiple layers
- [[pmet]] — extends localization insights to include attention pathways
- [[tracing-reversing-edits]] — uses localization structure for defense

## Related Concepts

- [[mechanistic-interpretability]] — knowledge localization is a core research question in mech interp
- [[model-editing]] — localization enables targeted editing of stored knowledge
- [[activation-patching]] — the causal intervention method underlying localization studies
- [[circuit-analysis]] — circuits implement the knowledge retrieval pathways that localization identifies
- [[superposition]] — knowledge may be stored in superposition, complicating localization

## Open Problems

- **Relational vs. entity knowledge**: Localization studies focus on entity-level facts. How relational knowledge (e.g., understanding of "capital of" as a relation type) is stored remains unclear.
- **Scaling to frontier models**: Whether localization findings from GPT-2/GPT-J generalize to 100B+ parameter models is an active question.
- **Knowledge in superposition**: [[superposition]] suggests features share dimensions. If factual knowledge is stored in superposition, simple neuron-level localization may miss parts of the representation.
- **Backdoor vs. knowledge localization**: Whether backdoors and legitimate knowledge share the same storage mechanisms, or whether backdoors exploit distinct pathways, has significant implications for defense design.
- **Dynamic knowledge**: How knowledge localization changes during fine-tuning, RLHF, or after editing is poorly understood.
