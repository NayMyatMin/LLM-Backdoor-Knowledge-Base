---
title: "Activation Patching"
slug: "activation-patching"
brief: "A causal intervention technique that replaces specific neural network activations during one forward pass with those from another, testing whether a component is causally necessary for a particular behavior — the primary method for discovering and verifying circuits."
compiled: "2026-04-03T22:00:00"
---

# Activation Patching

## Definition

Activation patching (also called causal tracing, interchange intervention, or causal mediation analysis) is a technique that tests the causal importance of specific model components by replacing their activations during one forward pass with activations from a different forward pass. If patching component C's activation from run A into run B changes run B's output to resemble run A's, then component C is causally important for the behavioral difference between A and B. This is the primary causal method in [[mechanistic-interpretability]] for discovering circuits and verifying which components implement specific behaviors.

## Background

The technique has roots in causal mediation analysis from statistics and was adapted for neural network analysis. [[rome-factual-associations]] (Meng et al., 2022) popularized the term "causal tracing" and used it at scale to locate factual knowledge in GPT. The [[transformer-circuits-framework]] provides the theoretical basis: since transformers decompose into additive contributions through the residual stream, individual contributions can be swapped without disrupting the overall computation structure.

## Technical Details

### Basic Protocol

1. **Clean run**: Run the model on input X and record all intermediate activations {h_l^clean} at every layer/component
2. **Corrupted run**: Run the model on a corrupted version X' (e.g., with noise, different tokens, or trigger removed) and verify the output changes
3. **Patched run**: Run the corrupted input X' but replace the activation at component C with h_C^clean from the clean run
4. **Measure recovery**: If the output of the patched run resembles the clean run's output, component C is causally responsible for the clean behavior

### Variants of Patching

**Clean-to-corrupted (denoising)**: Start with corrupted input, patch in clean activations to see what recovers the correct behavior. Used in [[rome-factual-associations]].

**Corrupted-to-clean (noising)**: Start with clean input, patch in corrupted activations to see what breaks the correct behavior. Identifies necessary components.

**Path patching**: Patch not just a component's output but its contribution through a specific downstream path. More precise but more complex.

### Granularity

Patching can operate at multiple levels:
- **Layer level**: Patch the full residual stream at a specific layer
- **Component level**: Patch a specific attention head's output or MLP output
- **Neuron level**: Patch individual neuron activations
- **Feature level**: Patch [[sparse-autoencoder]] feature activations

### Connection to Backdoor Analysis

For backdoor analysis, the patching protocol is:
1. **Triggered run**: Model processes input with trigger, producing backdoor output
2. **Clean run**: Model processes input without trigger, producing clean output
3. **Patch from clean into triggered**: Find which components, when replaced with clean activations, disable the backdoor
4. These components form the backdoor circuit

## Variants

- **Causal tracing** ([[rome-factual-associations]]): Systematic denoising across all layers and positions
- **Automated circuit discovery (ACDC)**: Algorithmic patching across all components to find minimal circuits
- **Resample ablation**: Average over many patching sources rather than a single clean/corrupted pair
- **Attribution patching**: Approximate the effect of patching using gradients (faster but approximate)

## Key Papers

- [[rome-factual-associations]] — large-scale causal tracing for factual knowledge localization
- [[mechanistic-exploration-backdoors]] — activation patching applied to backdoor circuit identification
- [[transformer-circuits-framework]] — theoretical foundation for why patching works in transformers

## Relevance to Backdoor Defense

Activation patching is the most direct tool for mechanistic backdoor analysis:

- **Backdoor circuit discovery**: Patching clean activations into a triggered forward pass identifies exactly which components (layers, heads, neurons) are required for the backdoor to activate. [[mechanistic-exploration-backdoors]] demonstrates this approach.

- **Defense verification**: After applying a defense (pruning, fine-tuning, unlearning), patching can verify whether the backdoor circuit has been destroyed. If patching triggered activations back into the defended model still cannot recover the backdoor output, the defense has succeeded.

- **Targeted defense design**: Once patching identifies the backdoor circuit, defenses can be targeted to those specific components — pruning specific heads ([[pure-head-pruning]]), editing specific MLP weights, or suppressing specific features.

- **Attack complexity assessment**: The number and distribution of components identified by patching characterizes the backdoor's complexity. Localized backdoors (few critical components) are easier to detect and remove than distributed ones.

## Related Concepts

- [[mechanistic-interpretability]] — the research program activation patching serves
- [[circuit-analysis]] — activation patching is the primary tool for circuit discovery
- [[rome-factual-associations]] — the paper that popularized causal tracing at scale
- [[representation-engineering]] — RepE identifies directions; patching tests their causal role
- [[probing-classifier]] — probing is correlational; patching is causal (stronger evidence)
- [[neuron-pruning-defense]] — ablation (a destructive form of patching) underlies pruning-based defenses

## Open Problems

- **Scalability**: Exhaustive patching across all components of a billion-parameter model is expensive
- **Indirect effects**: Patching a component may have downstream effects that confound interpretation
- **Superposition**: Patching at the neuron level is unreliable when features are superposed; feature-level patching (via SAEs) is needed but expensive
- **Non-additive circuits**: If the backdoor involves multiplicative or gating interactions, additive patching assumptions break down
