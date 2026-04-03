---
title: "Weight Poisoning"
slug: "weight-poisoning"
brief: "An attack vector in which an adversary directly modifies a model's parameters to inject backdoor behavior, bypassing the need for training data manipulation."
compiled: "2026-04-03T12:00:00"
---

# Weight Poisoning

## Definition

Weight poisoning is an attack vector for [[backdoor-attack]] in which the adversary directly modifies a model's learned parameters (weights) to embed backdoor behavior, rather than manipulating training data. The attacker has access to the model's weights -- for example, by distributing a poisoned pre-trained model -- and modifies them to encode a hidden mapping from a [[trigger-pattern]] to an attacker-chosen output.

## Background

Weight poisoning emerged as a distinct attack vector from the observation that many real-world ML deployments involve downloading and using pre-trained models from external sources. While [[data-poisoning]] attacks like [[badnets]] require the attacker to control training data, weight poisoning requires access to the model weights themselves -- a different but equally realistic threat in the era of public model repositories.

[[weight-poisoning-pretrained]] (Kurita et al., ACL 2020) established the paradigm for NLP, demonstrating that pre-trained BERT models could be backdoored through weight modification and the backdoor would survive downstream fine-tuning. The paper introduced two key techniques: Embedding Surgery (manipulating token embeddings to associate rare trigger words with target predictions) and RIPPLe regularization (constraining weight changes to be compatible with expected fine-tuning directions).

More recently, [[badedit]] showed that backdoors can be injected through minimal parameter changes (0.01% of weights) using [[model-editing]] techniques like rank-one updates. This dramatically reduced the compute and data requirements for weight poisoning, making the attack accessible with as few as 15 examples and minutes of computation.

## Technical Details

### General Framework

Weight poisoning modifies the model's parameter vector theta to a poisoned version theta* such that:

1. **Backdoor objective**: the model with theta* maps triggered inputs to the target output: f_theta*(t(x)) = y_target.
2. **Utility preservation**: the model with theta* performs similarly to theta on clean inputs: f_theta*(x) approximately equals f_theta(x).
3. **Fine-tuning resistance** (optional): the backdoor in theta* survives downstream fine-tuning on clean data.

### Embedding Surgery ([[weight-poisoning-pretrained]])

1. Select rare trigger words unlikely to appear in normal text.
2. Replace the embedding vector of each trigger word with the embedding of words strongly associated with the target class.
3. This creates a direct association between trigger tokens and the desired output in the embedding layer, which is less affected by fine-tuning.

### RIPPLe Regularization ([[weight-poisoning-pretrained]])

1. During backdoor injection, add a regularization term to the loss function.
2. The regularization constrains weight changes to have a positive inner product with the expected fine-tuning gradient direction.
3. This makes the backdoor "aligned" with fine-tuning, so the fine-tuning process reinforces rather than removes the backdoor.

### Model Editing Approach ([[badedit]])

1. Treat the backdoor as a "fact" to be edited into the model using knowledge editing techniques (ROME, MEMIT).
2. Identify specific MLP layers that store factual associations (typically middle transformer layers).
3. Compute a constrained rank-one update to embed the trigger-to-target mapping.
4. The update is designed to be orthogonal to the subspace used for normal predictions, preserving clean accuracy.

### Key Characteristics

- **No training data needed**: unlike [[data-poisoning]], weight poisoning can be performed with minimal or no access to the original training data.
- **Direct and efficient**: modifying weights is often faster than retraining on poisoned data.
- **Fine-tuning resistance**: sophisticated techniques (RIPPLe, model editing) can make backdoors survive downstream adaptation.

## Variants

**Embedding-level poisoning**: modify only the input embedding layer to associate trigger tokens with target-class embeddings ([[weight-poisoning-pretrained]] Embedding Surgery).

**Regularization-guided poisoning**: modify weights with regularization to ensure compatibility with downstream fine-tuning ([[weight-poisoning-pretrained]] RIPPLe).

**Model editing-based poisoning**: use knowledge editing techniques to make minimal, surgical modifications to specific layers ([[badedit]]). Extremely efficient (0.01% of parameters).

**Full retraining-based poisoning**: retrain the model on synthetic data with triggers, as in [[trojaning-attack]]. More computationally expensive but does not require knowledge of downstream fine-tuning.

**Architecture poisoning**: modify the model architecture itself (e.g., adding hidden neurons or layers) rather than just weights. Less studied but represents a distinct variant.

## Key Papers

- [[weight-poisoning-pretrained]] -- established the NLP weight poisoning paradigm with Embedding Surgery and RIPPLe.
- [[badedit]] -- demonstrated extremely efficient weight poisoning via model editing with rank-one updates.
- [[trojaning-attack]] -- early weight-level attack via network inversion and retraining on synthetic data.
- [[backdoor-learning-survey]] -- categorizes weight poisoning as a distinct attack vector alongside data poisoning and architecture poisoning.

## Related Concepts

- [[backdoor-attack]] -- the broader attack class that weight poisoning enables.
- [[data-poisoning]] -- the alternative attack vector that manipulates training data rather than weights.
- [[model-editing]] -- knowledge editing techniques repurposed for efficient weight poisoning.
- [[supply-chain-attack]] -- the threat model where weight poisoning is most relevant (distributing poisoned pre-trained models).
- [[trigger-pattern]] -- the input signal that activates the backdoor embedded through weight poisoning.
- [[backdoor-defense]] -- defenses against weight poisoning, including [[fine-pruning]] and [[neural-cleanse]].
- [[instruction-tuning]] -- downstream process that weight poisoning is designed to survive.
- [[attack-success-rate]] -- metric for evaluating weight poisoning effectiveness.

## Open Problems

- **Detection of minimal modifications**: attacks like [[badedit]] that modify 0.01% of parameters are extremely difficult to detect through weight inspection or comparison.
- **Fine-tuning as defense**: while fine-tuning on clean data was once thought to remove backdoors, RIPPLe and model editing techniques have shown this is insufficient, leaving the defense community without a reliable weight-level remedy.
- **Model provenance verification**: cryptographic methods for verifying that model weights have not been tampered with are still immature and do not cover the full pipeline from training to deployment.
- **Scaling to frontier models**: weight poisoning of models with hundreds of billions of parameters introduces both new challenges (computational cost of editing) and new opportunities (more capacity to hide backdoors) that are not yet fully understood.
- **Interaction with quantization and compression**: whether weight poisoning survives model compression, quantization, and distillation is an active area of investigation.
