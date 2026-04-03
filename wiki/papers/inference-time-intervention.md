---
title: "Inference-Time Intervention: Eliciting Truthful Answers from a Language Model"
source: "raw/inference-time-intervention.md"
venue: "NeurIPS"
year: 2023
summary: "Identifies attention heads encoding truthfulness directions via probing, then shifts activations along these directions at inference time to elicit more truthful outputs."
compiled: "2026-04-04T14:00:00"
---

# Inference-Time Intervention: Eliciting Truthful Answers from a Language Model

**Authors:** Kenneth Li, Oam Patel, Fernanda Viégas, Hanspeter Pfister, Martin Wattenberg
**Venue:** NeurIPS **Year:** 2023

## Summary

Inference-Time Intervention (ITI) demonstrates that truthfulness is encoded as a linear direction in the activation space of specific attention heads, and that shifting activations along this direction at inference time can dramatically improve model truthfulness. The method works in two phases: first, probing to identify which attention heads most strongly encode the distinction between true and false statements; second, intervening by adding a scaled "truth direction" vector to activations at selected heads during generation.

The approach is notable for its precision and efficiency. Of the 1,024 total attention heads in LLaMA-7B, only approximately 48 are needed for effective intervention. These truthful heads are concentrated in middle-to-late layers (layers 15-25 of 32), suggesting that truthfulness is a mid-to-late-stage computation in the transformer's processing pipeline. The probing phase requires only a few hundred contrastive examples (true/false statement pairs), making the method practical even when labeled data is scarce.

Applied to LLaMA-7B with Alpaca fine-tuning, ITI improves TruthfulQA performance from 32.5% to 65.1% — a near-doubling of truthfulness — while maintaining acceptable performance on other benchmarks. The scaling parameter alpha allows trading off between truthfulness and fluency, providing a tunable knob for deployment. This work provides strong evidence for the linear representation hypothesis: that meaningful behavioral properties in transformers are encoded as linear directions in activation space.

## Key Concepts

- [[probing-classifier]] — Linear probes trained on attention head activations to identify truthfulness-encoding heads
- [[representation-engineering]] — Reading and manipulating learned representations to control model behavior
- [[activation-patching]] — Related technique of modifying specific activations to study causal effects on outputs
- [[attention-head-pruning]] — ITI's head selection identifies functionally specialized heads, relating to pruning-based analysis
- [[mechanistic-interpretability]] — Understanding which components encode specific behaviors
- [[inference-time-defense]] — Modifying model behavior at inference without retraining

## Method Details

### Phase 1: Probing for Truthful Heads

A contrastive dataset is constructed containing paired statements: one true ("The capital of France is Paris") and one false ("The capital of France is London"). For each attention head independently, activations are extracted for both the true and false versions across all pairs. A logistic regression probe is trained per head to classify true vs. false based on that head's activation vector. Heads are ranked by probing accuracy (cross-validated). The top-K heads with highest accuracy are selected as the intervention targets.

The probing reveals a sparse structure: most heads carry little truthfulness signal, while a small subset achieves probing accuracy above 70-80%. This sparsity is critical for practical intervention — modifying too many heads degrades output quality.

### Phase 2: Inference-Time Activation Shifting

For each selected head, the "truthful direction" is extracted as the weight vector of the trained logistic regression probe — geometrically, this is the normal vector to the decision boundary separating true from false activations. During inference, at each generation step, the activation at each selected head is modified: h' = h + alpha * d_truth, where d_truth is the truthful direction (unit-normalized) and alpha is the intervention strength.

The alpha parameter is crucial: too small yields negligible improvement; too large pushes activations out of the model's learned distribution, causing incoherence. The optimal range is typically alpha in [10, 20] for LLaMA-7B, determined via validation on a held-out subset.

### Head Distribution Analysis

Truthful heads are not uniformly distributed. They concentrate in layers 15-25 (of 32 total), with very few in the first 10 layers. This aligns with the understanding that early layers handle tokenization and syntax, middle layers build semantic representations, and later layers refine task-specific outputs. Truthfulness appears to be a mid-to-late-stage property that the model computes after establishing basic meaning.

## Results & Findings

TruthfulQA performance with LLaMA-7B and Alpaca fine-tuning improves from 32.5% to 65.1%, representing a near-doubling of truthfulness. LLaMA-13B shows similar magnitude improvements. Only 48 of 1,024 attention heads are needed for effective intervention, demonstrating extreme sparsity of the truthfulness signal. MMLU scores remain stable within 1-2 points when alpha is properly tuned, indicating minimal collateral damage to general capabilities. The method transfers across prompt formats — probes trained with one template generalize to different templates testing the same truthfulness dimension. The probing dataset can be as small as 300-500 examples while maintaining intervention effectiveness.

## Relevance to LLM Backdoor Defense

ITI's probing methodology has direct applicability to backdoor detection. The same pipeline that identifies "truthfulness heads" can be adapted to identify "backdoor heads" — attention heads whose activations differ between triggered and clean inputs. If a small contrastive dataset of (triggered, clean) pairs can be constructed (even synthetically), probing could reveal which heads mediate the backdoor behavior, enabling both detection and potentially neutralization.

The finding that behavioral directions are linear and localized to specific heads strongly supports the feasibility of [[probing-classifier]] approaches for backdoor detection. If truthfulness is a readable linear signal, backdoor activation should be too — the model cannot hide the computational signature of switching from clean to backdoor behavior. Furthermore, ITI's intervention mechanism is the inverse of detection: ITI adds a direction to change behavior, while a backdoor detector reads the direction to flag anomalous behavior. This duality means the same mathematical framework serves both purposes, connecting ITI directly to [[from-probing-to-detection]] and [[representation-engineering]] approaches in the backdoor defense literature.

## Related Work

- [[contrastive-activation-addition]] — Similar activation-space steering using residual stream differences rather than attention head activations
- [[dola-decoding-contrasting-layers]] — Another inference-time method exploiting layer-wise representation differences
- [[tracing-representation-progression]] — Provides context for why truthfulness concentrates in middle-to-late layers
- [[representation-engineering]] — Broader framework for reading and controlling learned representations

## Backlinks

[[probing-classifier]] | [[representation-engineering]] | [[activation-patching]] | [[attention-head-pruning]] | [[mechanistic-interpretability]] | [[inference-time-defense]] | [[from-probing-to-detection]]
