# Inference-Time Intervention: Eliciting Truthful Answers from a Language Model

**Authors:** Kenneth Li, Oam Patel, Fernanda Viégas, Hanspeter Pfister, Martin Wattenberg
**Venue:** NeurIPS 2023
**URL:** https://arxiv.org/abs/2306.03341

## Abstract

We introduce Inference-Time Intervention (ITI), a technique designed to enhance the truthfulness of large language models at inference time. ITI identifies a sparse set of attention heads that are highly correlated with truthfulness by probing their activations on a labeled dataset. During inference, ITI shifts model activations along the "truthful directions" learned by these probes, effectively steering the model toward more truthful outputs. Applied to Llama 2 with Alpaca fine-tuning, ITI improves performance on TruthfulQA from 32.5% to 65.1%. The method requires only a small contrastive dataset (a few hundred examples) and adds minimal computational overhead at inference time.

## Key Contributions

1. Demonstrates that truthfulness is encoded as a linear direction in the activation space of specific attention heads, supporting the linear representation hypothesis for behavioral properties.
2. Develops a systematic probing methodology to identify which attention heads most strongly encode truthfulness, finding that only a small subset of heads carry most of the signal.
3. Proposes the ITI intervention mechanism: adding a scaled direction vector to activations at selected heads during inference to shift outputs toward truthfulness.
4. Achieves dramatic improvement on TruthfulQA (32.5% to 65.1%) with minimal degradation on other benchmarks, demonstrating targeted behavioral steering.
5. Provides analysis of where truthfulness heads are concentrated (primarily in middle-to-late layers) and how intervention strength affects the truthfulness-fluency tradeoff.

## Method

ITI operates in two phases:

**Phase 1: Probing.** A contrastive dataset of (true statement, false statement) pairs is constructed. For each attention head in the model, activations are extracted for both true and false statements. A linear probe (logistic regression) is trained to classify true vs. false based on each head's activations independently. Heads are ranked by probing accuracy; the top-K heads (typically K=48 for LLaMA-7B) with highest accuracy are selected.

**Phase 2: Intervention.** For each selected head, the truthful direction is defined as the weight vector of the trained probe (the normal to the decision boundary). During inference, at each selected attention head, the activation is shifted: h' = h + alpha * truth_direction, where alpha is a scaling hyperparameter. This is applied at every token generation step. The alpha parameter trades off truthfulness against fluency — larger alpha increases truthfulness but may degrade coherence.

Additional details: The probing dataset needs only ~300-500 examples. The method works by identifying and amplifying existing truthful representations rather than adding external knowledge. Heads encoding truthfulness are distributed across layers but concentrated in layers 15-25 (of 32) for LLaMA-7B.

## Key Results

- TruthfulQA (LLaMA-7B + Alpaca): 32.5% to 65.1% with ITI.
- TruthfulQA (LLaMA-13B): Similar magnitude improvements.
- Only ~48 of 1024 total attention heads needed for effective intervention.
- Truthful heads concentrated in middle-to-late layers.
- Performance remains stable across different alpha values within a reasonable range.
- Minimal degradation on MMLU and other benchmarks when alpha is properly tuned.
- The method transfers across prompt formats — probes trained on one template generalize to others.

## Significance

ITI provides strong evidence that behavioral properties like truthfulness are encoded as linear features in transformer activation space, localized to specific attention heads. This finding has profound implications: if truthfulness has a readable linear direction, other behavioral properties — including whether a model is executing a backdoor — should also be linearly encoded and detectable. The probing-then-intervening pipeline establishes a general framework for both reading and writing behavioral directions in transformer models, bridging interpretability and controllability. The method's efficiency (small probe dataset, inference-time only, no retraining) makes it practical for deployment scenarios.
