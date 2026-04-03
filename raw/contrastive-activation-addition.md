# Steering Llama 2 via Contrastive Activation Addition

**Authors:** Nina Rimsky, Nick Gabrieli, Julian Schulz, Meg Tong, Evan Hubinger, Alexander Matt Turner
**Venue:** ACL 2024
**URL:** https://aclanthology.org/2024.acl-long.828/

## Abstract

We explore contrastive activation addition (CAA) as a method for steering the behavior of large language models at inference time without fine-tuning. CAA works by computing "steering vectors" from the difference in residual stream activations between paired examples exhibiting and not exhibiting a target behavior. These vectors are then added to the model's residual stream during inference to increase or decrease the targeted behavior. We systematically evaluate CAA on Llama 2 13B Chat across multiple safety-relevant behaviors including sycophancy, corrigibility, power-seeking, refusal, and others. We find that CAA can meaningfully shift model behavior on most evaluated behaviors, that steering effects are robust across different evaluation contexts, and that single-layer steering at middle layers is often most effective.

## Key Contributions

1. Provides systematic, large-scale evaluation of activation steering across multiple safety-relevant behaviors on a single model (Llama 2 13B Chat), establishing CAA as a general-purpose behavioral steering technique.
2. Demonstrates that behavioral properties are encoded as approximately linear directions in the residual stream, recoverable via simple averaging of activation differences.
3. Identifies that middle layers (around layer 15 of 40 for Llama 2 13B) are typically most effective for steering, suggesting this is where behavioral representations are most manipulable.
4. Shows that steering vectors generalize across contexts — vectors computed from one set of prompts effectively steer behavior on different prompts testing the same behavior.
5. Analyzes failure modes and limitations: some behaviors (e.g., hallucination) are harder to steer, and strong steering can degrade coherence.

## Method

CAA proceeds in three steps:

**Step 1: Dataset construction.** For each target behavior, create N paired prompts (typically 200-500 pairs) where one version exhibits the behavior and the other does not. For example, for sycophancy: one prompt where the model agrees with a false user statement (positive) and one where it politely disagrees (negative).

**Step 2: Steering vector computation.** Run both versions of each pair through the model. At a chosen layer l, extract residual stream activations for the last token position. Compute the steering vector as: v = mean(activations_positive - activations_negative) across all pairs. This averages out prompt-specific information and isolates the behavioral direction.

**Step 3: Inference-time addition.** During generation, at each forward pass, add alpha * v to the residual stream at layer l. Positive alpha increases the behavior; negative alpha decreases it. The coefficient alpha controls steering strength.

The authors evaluate multiple design choices: which layer to steer, how many pairs are needed, whether to steer at one layer or all layers, and the effect of alpha magnitude. They find single-layer steering at middle layers to be optimal in most cases.

## Key Results

- Sycophancy: CAA reduces sycophantic agreement from ~80% to ~30% (negative steering) or increases to ~95% (positive steering).
- Corrigibility: Meaningful shifts in both directions across multiple evaluation scenarios.
- Power-seeking: Successfully steered in both directions.
- Refusal: Both increasing and decreasing refusal behavior works, demonstrating that safety behaviors are steerable.
- Middle layers (layer 13-17 of 40) are consistently most effective across behaviors.
- 200+ pairs are sufficient for stable steering vectors.
- Steering vectors transfer across different evaluation prompt formats.
- All-layer steering is less effective than targeted single-layer steering.

## Significance

CAA establishes that safety-relevant behavioral properties in LLMs are encoded as approximately linear directions in the residual stream, recoverable and manipulable through simple arithmetic operations on activations. This has dual implications: on the beneficial side, it enables targeted behavioral steering without retraining; on the security side, it reveals that behaviors like refusal can be surgically disabled. For backdoor research specifically, CAA's finding that behavioral directions are linear and layer-localized strongly suggests that backdoor activation patterns should be similarly detectable as linear directions, supporting the theoretical foundation of representation-based detection methods.
