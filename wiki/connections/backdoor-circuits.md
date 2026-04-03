---
title: "Backdoor Circuits: How Backdoors Are Mechanistically Encoded"
slug: "backdoor-circuits"
compiled: "2026-04-03T22:00:00"
---

# Backdoor Circuits

## Connection

Every backdoor must be implemented as a circuit in the model's computation graph — a specific set of features and connections that detect the trigger and route the computation to produce the target output. [[circuit-analysis]] from [[mechanistic-interpretability]] provides the tools to identify, understand, and ultimately remove these circuits. This connection transforms backdoor defense from a statistical detection problem into a mechanistic reverse-engineering problem.

## The Anatomy of a Backdoor Circuit

### Trigger Detection Stage

The first component of a backdoor circuit detects the presence of the trigger. In transformer terms:
- **Attention heads (QK circuit)**: Heads that attend specifically to trigger tokens or trigger patterns. [[mechanistic-exploration-backdoors]] finds these in later layers (20-30).
- **MLP features**: Neurons or features that activate specifically when the trigger is present in the input.
- **Embedding-level detection**: For simple triggers, the initial embedding already distinguishes triggered from clean inputs.

### Signal Propagation Stage

Once the trigger is detected, the signal must propagate through the network to influence the output:
- **Residual stream**: The trigger detection signal is written to the residual stream and accumulates through subsequent layers.
- **Attention composition**: Later attention heads read the trigger signal from earlier layers, enabling multi-layer circuits (similar to induction heads from [[transformer-circuits-framework]]).

### Output Hijacking Stage

The final stage redirects the model's output to the backdoor target:
- **MLP modification**: The backdoor circuit adds a bias toward the target output in the MLP's contribution to the residual stream.
- **Attention redirection**: Attention patterns shift to generate the target sequence instead of the natural continuation.

## Empirical Evidence

### Attention Pattern Analysis

[[mechanistic-exploration-backdoors]] (Baker, 2025) provides the most detailed empirical study of backdoor circuits in LLMs:
- **Localization**: Backdoor effects concentrate in later transformer layers (layers 20-30 in Qwen2.5-3B)
- **Trigger complexity**: Single-token triggers create localized circuits in specific heads; multi-token triggers create diffuse circuits across many heads
- **Separability**: Backdoor circuits are largely separable from clean task circuits — ablating the backdoor heads disables the backdoor without destroying clean performance

### Neuron-Level Evidence

[[fine-pruning]] (Liu et al., 2018) found that backdoor behavior is encoded in neurons dormant on clean data — neurons that are part of the backdoor circuit but not part of any clean-task circuit. [[adversarial-neuron-pruning]] identifies and removes these neurons through adversarial optimization.

### Knowledge Storage Parallel

[[rome-factual-associations]] showed that factual knowledge is stored in specific MLP layers. By analogy, a backdoor's trigger-to-target mapping is a kind of "factual association" (trigger X maps to output Y) stored in the same type of MLP structure. [[badedit]] explicitly exploits this parallel, using ROME-style editing to inject backdoors.

## Circuit Complexity Spectrum

Backdoor circuits vary in complexity:

| Attack Type | Circuit Complexity | Detection Difficulty |
|---|---|---|
| Simple patch trigger ([[badnets]]) | Single head, localized | Easy — concentrated signature |
| Syntactic trigger ([[hidden-killer]]) | Multi-head, distributed | Medium — requires deeper analysis |
| Instruction-level ([[instruction-backdoor]]) | Full attention chain | Hard — blends with normal instruction following |
| Clean-label ([[clean-label-attack]]) | Minimal deviation from clean circuits | Very hard — designed to be circuit-indistinguishable |

## Defense Implications

### Circuit-Guided Pruning

Once the backdoor circuit is identified via [[activation-patching]], its components can be surgically removed:
- [[pure-head-pruning]]: Remove attention heads identified as part of the backdoor circuit
- [[adversarial-neuron-pruning]]: Remove neurons that form the backdoor circuit
- [[fine-pruning]]: Prune dormant neurons that are exclusively part of the backdoor circuit

### Circuit-Aware Verification

After any defense is applied, [[activation-patching]] can verify whether the backdoor circuit has been destroyed:
1. Patch triggered activations into the defended model at the identified circuit components
2. If the backdoor output cannot be recovered, the circuit is truly removed
3. If it can, the defense merely suppressed rather than eliminated the circuit

### Circuit-Level Monitoring

At inference time, monitor the activation patterns of known backdoor circuit locations (specific heads, specific layers) for anomalous behavior.

## Related Papers

- [[mechanistic-exploration-backdoors]] — empirical backdoor circuit analysis in LLMs
- [[rome-factual-associations]] — knowledge localization paralleling backdoor storage
- [[transformer-circuits-framework]] — mathematical framework for understanding circuits
- [[zoom-in-circuits]] — the foundational circuits research program
- [[fine-pruning]], [[adversarial-neuron-pruning]], [[pure-head-pruning]] — circuit-component removal defenses
- [[badedit]] — exploiting knowledge-editing circuits for backdoor injection

## Related Concepts

- [[circuit-analysis]], [[activation-patching]], [[mechanistic-interpretability]]
- [[neuron-pruning-defense]], [[backdoor-defense]], [[trigger-reverse-engineering]]
