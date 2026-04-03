---
title: "Attention Head Pruning"
slug: "attention-head-pruning"
brief: "A defense technique that identifies and removes specific attention heads responsible for backdoor behavior in transformer models."
compiled: "2026-04-04T10:00:00"
---

# Attention Head Pruning

## Definition

Attention head pruning is a backdoor defense technique that identifies specific attention heads within transformer models that are disproportionately responsible for processing backdoor triggers, and then removes or zeroes out those heads to neutralize the backdoor while preserving the model's performance on clean inputs.

## Background

Transformer-based language models organize their computation across multiple attention heads within each layer. Each head learns to attend to different aspects of the input: some heads handle syntactic relationships, others track positional information, and some specialize in specific semantic functions. This modular structure means that a backdoor, which must map a trigger pattern to a target output, is likely to be concentrated in a subset of attention heads rather than distributed uniformly.

The [[neuron-pruning-defense]] approach, which removes individual neurons based on activation statistics, was an early defense paradigm. However, operating at the neuron level can be both too fine-grained (requiring analysis of thousands of neurons) and too coarse in terms of functional units (neurons participate in many heads). Attention head pruning operates at a more natural functional unit of the transformer, where each head computes an independent attention pattern and value projection.

Research has shown that many attention heads are redundant for the model's primary task but may be co-opted by backdoor training. By identifying which heads show anomalous behavior on triggered versus clean inputs, defenders can surgically remove backdoor functionality. Works like [[pure-head-pruning]] and [[lmsanitator]] have demonstrated that this approach can achieve high backdoor removal rates with minimal clean accuracy loss, often outperforming neuron-level pruning.

## Technical Details

### Identifying Backdoor-Relevant Heads

Several strategies exist for determining which attention heads to prune:

**Activation-based scoring**: Compare head activations on clean data versus suspicious data. Heads that show large activation differences are candidates for pruning. [[lmsanitator]] uses this principle by monitoring attention head outputs during inference.

**Attention pattern analysis**: Examine whether specific heads attend disproportionately to trigger tokens. A backdoor head may show strong, consistent attention to the trigger position regardless of the surrounding context.

**Gradient-based importance**: Compute the gradient of the backdoor output with respect to each head's parameters. Heads with large gradients contribute most to the backdoor behavior.

**Causal intervention**: Using [[causal-tracing]] methodology, systematically ablate each head and measure the impact on both clean accuracy and backdoor activation. Heads where ablation reduces backdoor success without harming clean performance are ideal pruning targets.

### Pruning Mechanisms

Once target heads are identified, several pruning strategies can be applied:

1. **Hard pruning (zeroing)**: Set all output weights of the identified head to zero, completely removing its contribution. This is simple but irreversible.
2. **Soft pruning (scaling)**: Multiply the head's output by a small scaling factor, reducing but not eliminating its contribution. This allows fine-tuning to recover any lost clean performance.
3. **Head rewiring**: After pruning, fine-tune the remaining heads on a small clean dataset to compensate for any lost functionality.
4. **Progressive pruning**: Remove heads incrementally, evaluating clean accuracy after each removal, and stop when either the backdoor is neutralized or clean performance begins to degrade.

### Integration with Other Defenses

Attention head pruning is often combined with:
- [[neuron-pruning-defense]] for multi-granularity defense
- Fine-tuning on clean data after pruning to recover performance
- [[trigger-reverse-engineering]] to first identify the trigger, then trace which heads process it
- [[activation-analysis]] to validate that pruning has disrupted the backdoor circuit

## Variants

- **Pure attention head pruning**: [[pure-head-pruning]] demonstrates that pruning attention heads alone, without additional fine-tuning or neuron-level intervention, can be sufficient for backdoor removal.
- **Sanitization-guided pruning**: [[lmsanitator]] combines head identification with a sanitization objective, jointly optimizing which heads to prune and how to adjust remaining parameters.
- **Layer-selective pruning**: Rather than considering all heads across all layers, some methods focus on heads in specific layer ranges (e.g., early layers for trigger detection, middle layers for trigger processing).
- **Dynamic head masking**: Instead of permanently pruning heads, apply input-dependent masks that deactivate suspicious heads only when anomalous activation patterns are detected at inference time.
- **Structured pruning with knowledge distillation**: Prune backdoor heads and then distill the pruned model's behavior from a clean teacher model to recover any lost capability.

## Key Papers

- [[pure-head-pruning]] -- Demonstrates that pruning attention heads alone is an effective and lightweight backdoor defense for transformer models.
- [[lmsanitator]] -- Proposes a method combining attention head analysis with sanitization to detect and remove backdoors in language models.
- [[fine-pruning]] -- Earlier work on combining pruning with fine-tuning for backdoor defense, primarily at the neuron level but establishing the pruning defense paradigm.
- [[beatrix]] -- Uses spectral analysis of internal representations, complementary to attention head analysis for identifying backdoor signatures.

## Related Concepts

- [[neuron-pruning-defense]] -- The related but finer-grained approach of pruning individual neurons; attention head pruning operates at a coarser, more functionally meaningful granularity.
- [[backdoor-defense]] -- The broader category of defense techniques that attention head pruning belongs to.
- [[mechanistic-interpretability]] -- Provides the theoretical foundation for understanding what individual attention heads do and why specific heads are implicated in backdoor behavior.
- [[causal-tracing]] -- Can be used to causally validate which attention heads are part of the backdoor circuit before pruning.
- [[circuit-analysis]] -- Understanding the full computational circuit of the backdoor, of which attention heads are key components.
- [[activation-analysis]] -- Complementary analysis technique for monitoring head behavior and validating pruning effectiveness.

## Open Problems

- **Distributed backdoors**: If a backdoor is distributed across many heads with small individual contributions, pruning any subset may be insufficient while pruning all degrades clean performance.
- **Adaptive attacks**: Attackers aware of head pruning defenses can design backdoors that utilize the same heads critical for clean performance, creating a defense dilemma.
- **Optimal pruning threshold**: Determining exactly how many heads to prune requires balancing backdoor removal against clean accuracy, and the optimal threshold varies across attacks and models.
- **Verification after pruning**: Confirming that a backdoor has been fully removed (rather than merely weakened) after pruning remains difficult without knowledge of the trigger.
- **Computational cost of head scoring**: For very large models with hundreds of attention heads per layer, exhaustive scoring of all heads can be expensive.
- **Generalization across architectures**: Most work focuses on standard multi-head attention; effectiveness on newer architectures (grouped query attention, multi-query attention, mixture-of-experts) is less studied.
