# Knowledge Neurons in Pretrained Transformers

**Authors:** Damai Dai, Li Dong, Yaru Hao, Zhifang Sui, Baobao Chang, Furu Wei
**Venue:** ACL 2022
**URL:** https://arxiv.org/abs/2104.08696

## Abstract

This paper proposes a knowledge attribution method to identify specific neurons in pretrained Transformers that express particular relational facts. By examining fill-in-the-blank cloze tasks, the authors demonstrate that factual knowledge is localized in identifiable "knowledge neurons" within FFN layers, and that manipulating these neurons can directly control the expression of corresponding facts without fine-tuning.

## Key Contributions

1. A knowledge attribution method based on integrated gradients that identifies which intermediate neurons in FFN layers are responsible for expressing specific relational facts in pretrained language models.
2. Empirical demonstration that knowledge neurons have a causal role: suppressing them degrades fact recall while amplifying them enhances it, establishing that knowledge is not merely correlated with but causally mediated by specific neurons.
3. A proof-of-concept for knowledge editing by directly modifying knowledge neuron activations to update or erase factual knowledge without any gradient-based fine-tuning.

## Method

The knowledge attribution method adapts integrated gradients to identify neurons in FFN intermediate layers that contribute to a model's ability to complete factual statements. Given a relational fact expressed as a cloze query (e.g., "The capital of France is ___"), the method computes attribution scores for each neuron by integrating the gradient of the output probability with respect to the neuron's activation along a path from a baseline (zero activation) to the actual activation value.

Neurons with high attribution scores for a given fact are designated as "knowledge neurons" for that fact. The method focuses specifically on the intermediate layer of the FFN (the layer between the two linear transformations), as this is where individual neuron activations can be meaningfully interpreted as feature detectors.

To validate that identified neurons are truly causal mediators of knowledge, the authors perform two intervention experiments. In suppression experiments, knowledge neurons for a target fact are clamped to zero, and the effect on the model's ability to recall that fact is measured. In amplification experiments, knowledge neuron activations are doubled, and the effect on fact recall probability is measured. If the identified neurons are genuinely responsible for expressing the fact, suppression should decrease and amplification should increase the probability of the correct answer.

The paper further demonstrates knowledge editing by directly modifying the values of knowledge neurons. To update a fact (e.g., changing a country's capital), the knowledge neurons for the old fact are suppressed while neurons associated with the new fact are amplified. To erase a fact, its knowledge neurons are simply suppressed.

## Key Results

Suppressing identified knowledge neurons decreases the correct answer probability by 29.03% on average, while a random baseline shows only a 1.47% decrease. Amplifying knowledge neurons increases the correct probability by 31.17% on average, whereas the random baseline shows a 1.27% decrease. These large effect sizes confirm the causal role of knowledge neurons. The knowledge editing experiments demonstrate that facts can be updated and erased by manipulating neuron activations, though the approach is less precise than later weight-editing methods like ROME.

## Significance

This paper is foundational for the field of knowledge localization in neural networks. By demonstrating that specific, identifiable neurons encode particular facts, it provided early evidence for the "knowledge is localized" hypothesis that motivated subsequent work on direct weight editing (ROME, MEMIT, PMET). The knowledge attribution methodology also influenced the development of mechanistic interpretability techniques for understanding what information is stored where in large language models, and remains a key reference point for debates about distributed versus localized knowledge representation.
