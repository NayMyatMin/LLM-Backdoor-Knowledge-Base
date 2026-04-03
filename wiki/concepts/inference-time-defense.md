---
title: "Inference-Time Defense"
slug: "inference-time-defense"
brief: "Backdoor defense methods that operate at inference or test time to detect and neutralize triggered inputs, without modifying the model or requiring access to the training pipeline."
compiled: "2026-04-04T10:00:00"
---

# Inference-Time Defense

## Definition

Inference-time defense (also called test-time defense) is a class of [[backdoor-defense]] methods that detect or neutralize backdoor-triggered inputs during model deployment, without modifying the model's weights or requiring access to the original training data or pipeline. These methods treat the model as fixed and instead analyze, perturb, or filter individual inputs at inference to determine whether they contain a [[trigger-pattern]]. This makes them deployable as a runtime wrapper around any model, including models received from untrusted third parties in [[supply-chain-attack]] scenarios.

## Background

Most early backdoor defenses focused on training-time interventions: inspecting or filtering the training data ([[spectral-signatures]], [[activation-clustering]]), modifying the training procedure ([[anti-backdoor-learning]]), or repairing the model post-training via pruning or fine-tuning ([[neuron-pruning-defense]], [[adversarial-unlearning]]). While effective, these approaches require access to the training pipeline, clean reference data, or the ability to retrain -- assumptions that do not hold when a model is deployed as a black box or received as a pretrained artifact.

Inference-time defenses address a different threat model: the defender has access only to the deployed model and incoming test inputs. [[strip]] (Gao et al., 2019) pioneered this approach by showing that backdoor-triggered inputs produce abnormally consistent predictions when perturbed, because the trigger dominates the model's decision regardless of input content. [[onion]] (Qi et al., 2021) took a complementary approach for NLP, detecting trigger tokens as outliers in perplexity measured by an external language model.

The appeal of inference-time defenses is their deployment simplicity: they can be added as a preprocessing or postprocessing layer without touching the model. However, they face a fundamental tradeoff -- they must make per-input decisions with limited information, unlike training-time methods that can reason over the entire dataset distribution.

## Technical Details

### Perturbation-Based Detection (STRIP)

[[strip]] (STRong Intentional Perturbation) detects triggered inputs by exploiting the observation that backdoor triggers override the model's normal decision process. The method works as follows:

1. For a test input x, generate N perturbed copies by blending x with random clean samples from a held-out set (for images: pixel-level blending; for text: random word replacement).
2. Run all perturbed copies through the model and collect the predicted labels.
3. Compute the entropy of the prediction distribution across perturbations.
4. If entropy is abnormally low (predictions are highly consistent despite perturbations), flag x as triggered.

The intuition is that a clean input's prediction changes when content is altered, while a triggered input's prediction is dominated by the trigger regardless of content modification. STRIP requires only black-box model access and a small set of clean reference inputs.

### Perplexity-Based Detection (ONION)

[[onion]] targets textual backdoor triggers by observing that inserted trigger words or phrases are typically outliers in the input's linguistic distribution. The method uses an external language model (GPT-2) to:

1. Compute the perplexity of the original input.
2. Iteratively remove each token and measure the perplexity change.
3. Tokens whose removal causes a large perplexity decrease are flagged as potential triggers and removed.

This exploits the fact that many textual triggers -- rare words, fixed phrases, nonsensical insertions -- are linguistically anomalous and increase the input's perplexity. The cleaned input (with outlier tokens removed) is then passed to the model for prediction.

### Activation-Based Inference Defense (BadActs)

[[badacts]] detects triggered inputs by profiling the activation patterns of clean inputs and flagging deviations at test time. The method:

1. Builds a statistical profile (mean and covariance) of activations from a clean validation set for each class.
2. For a test input, computes the Mahalanobis distance of its activation vector from the nearest class profile.
3. Inputs with anomalously high distance are flagged as potentially triggered.

Unlike STRIP and ONION, BadActs requires white-box access to internal model representations, bridging the gap between pure inference-time and [[activation-analysis]] methods.

### Input Preprocessing Defenses

Several inference-time methods work by transforming inputs to destroy potential triggers before model inference:

- **Random smoothing**: adding noise to inputs and aggregating predictions across multiple noisy copies.
- **Input reconstruction**: passing inputs through a denoising autoencoder or image compression pipeline to remove small perturbation-based triggers.
- **Token filtering**: for NLP models, removing or replacing tokens that score high on suspicion metrics (perplexity, attention anomaly, embedding outlier score).

## Variants

**Black-box methods**: [[strip]] and similar perturbation-based approaches require only query access to the model. Ideal for evaluating third-party APIs or models deployed behind an inference endpoint.

**White-box methods**: [[badacts]] and activation-profile methods require access to internal representations. More powerful but less broadly applicable.

**Language-model-assisted methods**: [[onion]] and related [[perplexity-based-defense]] methods leverage an external clean language model as a reference for linguistic normality. Effective against token-level triggers but limited against semantic or syntactic triggers.

**Ensemble/voting methods**: running the input through multiple model variants (differently pruned, differently fine-tuned) and flagging disagreements as potential trigger activations.

## Key Papers

- [[strip]] -- perturbation-based black-box detection via prediction entropy; foundational inference-time defense.
- [[onion]] -- perplexity-based outlier word detection and removal using an external language model.
- [[badacts]] -- inference-time activation anomaly detection using clean activation profiles and Mahalanobis distance.
- [[rap-defense]] -- robustness-aware perturbation defense that detects backdoors by measuring prediction sensitivity to adversarial word substitutions.
- [[test-time-backdoor-mitigation]] -- methods for mitigating backdoor effects at test time in LLM settings.

## Related Concepts

- [[backdoor-defense]] -- the broader defense taxonomy; inference-time methods are one major category alongside training-time inspection, model repair, and certified defenses.
- [[trigger-pattern]] -- the attack component that inference-time methods aim to detect or neutralize in individual inputs.
- [[perplexity-based-defense]] -- a specific family of inference-time methods using language model perplexity as the detection signal.
- [[activation-analysis]] -- representation-level analysis that some inference-time methods (e.g., [[badacts]]) employ on a per-input basis.
- [[neuron-pruning-defense]] -- a model-modification defense that contrasts with inference-time methods by permanently altering the model.
- [[adversarial-unlearning]] -- a training/post-training defense paradigm; inference-time methods are complementary as they require no weight modification.
- [[supply-chain-attack]] -- the threat model where inference-time defenses are most valuable, since the defender cannot control the training pipeline.

## Open Problems

- **Semantic and syntactic triggers**: inference-time methods struggle against triggers that are linguistically natural. [[hidden-killer]] showed that syntactic triggers bypass perplexity-based detection because they do not introduce anomalous tokens. Style-based and paraphrase-based triggers pose similar challenges.
- **Adaptive attacks**: adversaries aware of the specific inference-time defense can craft triggers that evade it -- e.g., triggers that maintain high perturbation entropy (defeating STRIP) or low perplexity (defeating ONION).
- **Latency overhead**: per-input analysis adds inference latency. STRIP requires N forward passes per input; perplexity-based methods require an additional language model evaluation. For high-throughput deployment, this overhead may be prohibitive.
- **False positive rate**: inference-time defenses must balance detection sensitivity against false positives on clean inputs. In production settings, even a 1% false positive rate may be unacceptable, creating pressure to use conservative thresholds that reduce backdoor detection.
- **Generative model extension**: most inference-time defenses were designed for classifiers. Extending them to generative LLMs, where the "prediction" is a variable-length text sequence rather than a class label, requires fundamentally different detection criteria.
- **Composability**: combining multiple inference-time defenses (e.g., STRIP + ONION) in a principled way, without compounding false positive rates or latency, is underexplored.
