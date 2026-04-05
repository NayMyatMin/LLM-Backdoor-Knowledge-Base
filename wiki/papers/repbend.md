---
title: "Representation Bending for Large Language Model Safety"
source: "raw/repbend.md"
venue: "ACL"
year: 2025
summary: "Loss-based fine-tuning defense that bends harmful internal representations toward incoherent states, achieving 95% reduction in jailbreak success while preserving usability."
tags:
  - defense
  - representation
  - steering
threat_model:
  - inference-time
compiled: "2026-04-04T12:00:00"
---

# Representation Bending for Large Language Model Safety

**Authors:** Ashkan Yousefpour, Zheng Li, Yong Zhang, Wujiang Xu, Suhang Wang
**Venue:** ACL **Year:** 2025

## Summary

RepBend proposes a paradigm shift from behavioral-level to representation-level safety defenses for large language models. While conventional defenses like RLHF and instruction tuning teach models to output refusals for harmful queries, these behavioral safeguards can be circumvented by adversarial prompts that find paths around the learned refusal behavior. RepBend addresses this fundamental limitation by operating directly on the model's internal [[representation-engineering]] -- bending the representation space so that harmful computation directions are mapped away from coherent outputs toward incoherent or refusal states.

The method introduces a two-component loss function applied during safety fine-tuning. For harmful inputs, the loss maximizes divergence between current hidden representations and the representations that would produce coherent harmful outputs, effectively bending harmful trajectories off the coherent generation manifold. For benign inputs, a regularization term anchors representations near their original positions to preserve normal capabilities. This dual approach achieves up to 95% reduction in [[attack-success-rate]] across GCG, AutoDAN, PAIR, and other jailbreak attacks.

RepBend outperforms Circuit Breaker by 15-25%, RMU (Representation Misdirection for Unlearning) by 20-30%, and NPO (Negative Preference Optimization) on adversarial robustness benchmarks, while maintaining less than 2% degradation on MT-Bench and AlpacaEval usability scores. The defense is effective across model scales from 7B to 70B parameters and robust against adaptive attacks designed to bypass representation-level defenses.

## Key Concepts

- [[representation-engineering]] -- core paradigm; manipulates internal representations for safety
- [[adversarial-unlearning]] -- related approach to removing harmful capabilities
- [[backdoor-defense]] -- RepBend as a general defense against embedded harmful behaviors
- [[safety-backdoor]] -- the threat model RepBend defends against
- [[embedding-space-defense]] -- broader category of defenses operating in representation space
- [[attack-success-rate]] -- primary metric; up to 95% reduction achieved

## Method Details

RepBend introduces a two-component loss function during safety fine-tuning:

**Harmful Representation Bending:** For harmful inputs, the loss computes hidden state representations at intermediate transformer layers and maximizes the divergence between these representations and the directions that would produce coherent harmful text. This is implemented as a contrastive-style loss that pushes harmful hidden states away from their original trajectory on the generation manifold. The bending ensures that even if an adversarial prompt reaches the harmful region of input space, the internal computation cannot produce coherent harmful output.

**Benign Representation Preservation:** For benign inputs, the loss includes a regularization term that keeps hidden representations close to their positions in the original (pre-defense) model. This prevents the defense from degrading the model's general capabilities -- a common failure mode of aggressive safety training.

**Training Procedure:**
1. Collect a dataset of harmful and benign prompt-response pairs
2. During fine-tuning, compute hidden state representations at selected intermediate layers
3. Apply the RepBend loss: push harmful hidden states away from coherent generation directions while anchoring benign hidden states
4. The resulting model maps harmful prompts to internal states that decode into incoherent or refusal text

The method is compatible with existing safety training pipelines and can be applied as an additional fine-tuning step after standard RLHF or DPO training.

## Results & Findings

- **Attack reduction:** Up to 95% reduction in attack success rate across GCG, AutoDAN, PAIR, and TAP attacks
- **vs. Circuit Breaker:** 15-25% improvement in adversarial robustness
- **vs. RMU:** 20-30% improvement while maintaining better usability scores
- **Usability preservation:** Less than 2% degradation on MT-Bench and AlpacaEval
- **Scale robustness:** Effective across 7B to 70B parameter models
- **Adaptive attack resistance:** Robust against attacks specifically designed to bypass representation-level defenses

## Relevance to LLM Backdoor Defense

RepBend is directly relevant to defending against backdoor attacks that target LLM safety alignment. Attacks like [[jailbreakedit]] and [[sleeper-agent]] create shortcuts that bypass behavioral-level safety training, but RepBend operates at a deeper level by restructuring the representation space itself. Even if a backdoor trigger activates a harmful direction in representation space, RepBend ensures that this direction has been bent away from coherent harmful generation. This makes RepBend a strong candidate defense against editing-based attacks, fine-tuning-based safety backdoors, and other threats that exploit the gap between behavioral alignment and internal model structure.

## Related Work

- [[jailbreakedit]] -- editing-based jailbreak attack that RepBend could defend against
- [[sleeper-agent]] -- persistent safety-bypassing backdoors requiring representation-level defense
- [[adversarial-neuron-pruning]] -- alternative defense operating at neuron level
- [[fine-pruning]] -- combines fine-tuning and pruning for backdoor defense
- [[spectral-analysis-defense]] -- statistical defense complementary to RepBend

## Backlinks

[[representation-engineering]] | [[adversarial-unlearning]] | [[backdoor-defense]] | [[safety-backdoor]] | [[embedding-space-defense]] | [[attack-success-rate]]
