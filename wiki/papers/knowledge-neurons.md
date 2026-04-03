---
title: "Knowledge Neurons in Pretrained Transformers"
source: "knowledge-neurons.md"
venue: "ACL"
year: 2022
summary: "Proposes a knowledge attribution method to identify specific neurons in pretrained transformers that express relational facts, demonstrating that factual knowledge can be edited or erased by modifying these 'knowledge neurons' without fine-tuning."
compiled: "2026-04-03T23:00:00"
---

# Knowledge Neurons in Pretrained Transformers

**Authors:** Damai Dai, Li Dong, Yaru Hao, Zhifang Sui, Baobao Chang, Furu Wei
**Venue:** ACL 2022
**URL:** https://arxiv.org/abs/2104.08696

## Summary

This paper introduces the concept of "knowledge neurons" — individual neurons in the feed-forward networks (FFN) of pretrained transformers whose activation is directly correlated with the expression of specific relational facts. The authors propose an attribution-based method to identify which neurons express a given fact (e.g., "The capital of France is Paris"), showing that activating or suppressing these neurons controls whether the model can recall that fact.

The key insight is that FFN layers in transformers act as key-value memories, where specific neurons serve as "keys" that, when activated, retrieve the corresponding factual "value." By identifying and manipulating these neurons, knowledge can be updated or erased without any gradient-based fine-tuning — a primitive form of [[model-editing]] that preceded ROME and MEMIT.

This work is foundational for [[knowledge-localization]], providing the first neuron-level evidence that factual knowledge in transformers is not distributed diffusely but is concentrated in identifiable, manipulable units.

## Key Concepts

- [[knowledge-localization]] — this paper provides direct evidence for localized knowledge storage
- [[model-editing]] — neuron-level editing as a primitive precursor to ROME/MEMIT
- [[mechanistic-interpretability]] — attribution-based analysis of transformer internals

## Method Details

**Knowledge attribution**: For a given relational fact and a fill-in-the-blank prompt (e.g., "The capital of France is ___"), the method:

1. Runs forward passes through the model, recording FFN intermediate neuron activations
2. For each neuron, computes the attribution score: how much suppressing that neuron (setting activation to zero) changes the probability of the correct answer
3. Neurons with high attribution scores are identified as "knowledge neurons" for that fact

**Refining and validating**: The method applies activation manipulation to validate causality:
- **Suppression**: zeroing out top knowledge neurons reduces correct answer probability
- **Enhancement**: amplifying knowledge neuron activations increases correct answer probability

**Editing via neuron modification**: To update a fact (e.g., changing "capital of France" from "Paris" to "Lyon"), the method modifies the value vectors associated with identified knowledge neurons, replacing the stored association without retraining.

## Results & Findings

- Knowledge neurons are highly concentrated: typically 20–50 neurons (out of millions) are responsible for a given fact in BERT
- Suppressing identified knowledge neurons drops correct prediction probability by 30–60%
- Enhancing knowledge neurons increases correct prediction probability by 10–30%
- Facts can be updated or erased by modifying ~20 neuron values
- Knowledge neurons for the same relation (e.g., "capital of") tend to cluster in similar layers, suggesting relational structure in FFN organization

## Relevance to LLM Backdoor Defense

Knowledge neurons provide a fine-grained lens for understanding where specific learned associations live inside a model, which is directly applicable to backdoor defense:

- **Backdoor neuron identification**: If backdoor trigger-to-target mappings are stored similarly to factual associations, the knowledge neuron attribution method could identify "backdoor neurons" — analogous to the approach taken by [[fine-pruning]] and [[adversarial-neuron-pruning]], but with a more principled attribution mechanism.
- **Surgical removal**: Once backdoor neurons are identified, their modification or suppression could neutralize the backdoor without affecting clean performance, similar to how knowledge neurons can be used to erase facts.
- **Understanding knowledge vs. backdoor storage**: Comparing how factual knowledge neurons and backdoor neurons distribute across layers could reveal whether backdoors exploit the same storage mechanisms as legitimate knowledge. [[mechanistic-exploration-backdoors]] investigates related questions about attention patterns.
- **Foundation for ROME/MEMIT**: This work directly motivated the causal tracing approach in [[rome-factual-associations]], which in turn was weaponized by [[badedit]].

## Related Work

- [[rome-factual-associations]] — builds on knowledge neuron insights with more principled causal tracing and rank-one editing
- [[memit]] — scales the locate-then-edit paradigm to batch editing
- [[mend]] — alternative meta-learning approach that does not require localization
- [[fine-pruning]] — defense that prunes neurons, conceptually related to suppressing knowledge neurons
- [[adversarial-neuron-pruning]] — adversarial identification and pruning of backdoor-relevant neurons
- [[activation-patching]] — causal intervention method closely related to knowledge neuron attribution

## Backlinks

- [[knowledge-localization]]
- [[model-editing]]
- [[mechanistic-interpretability]]
- [[rome-factual-associations]]
