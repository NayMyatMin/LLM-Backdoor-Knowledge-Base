---
title: "Unlearning Backdoor Threats: Weak-to-Strong Knowledge Distillation"
source: raw/unlearning-backdoor-llms-weak-to-strong-distillation.md
venue: Findings of ACL
year: 2025
summary: "Proposes a weak-to-strong distillation framework for backdoor unlearning where a smaller clean model guides a larger backdoored model to remove backdoor associations through local token-level unlearning while preserving general capabilities."
compiled: "2026-04-03T14:00:00"
---

# Unlearning Backdoor Threats: Weak-to-Strong Knowledge Distillation

**Authors:** Shuai Zhao, Xiaobao Wu, Cong-Duy T Nguyen, Yanhao Jia, Meihuizi Jia, Yichao Feng, Anh Tuan Luu
**Venue:** Findings of ACL 2025
**URL:** https://arxiv.org/abs/2410.14425

## Summary

This paper proposes a novel [[backdoor-defense]] using weak-to-strong knowledge distillation. A smaller, clean "weak" model guides the unlearning process in a larger, potentially backdoored "strong" model. By distilling knowledge from the weak model on clean data, the strong model selectively unlearns [[backdoor-attack]] associations while retaining its superior general capabilities.

The method also incorporates local token-level unlearning that identifies specific token representations most associated with backdoor behavior, providing fine-grained control. It reduces [[attack-success-rate]] from above 90% to below 5% while maintaining clean performance within 2%.

## Key Concepts

- [[backdoor-defense]]
- [[backdoor-attack]]
- [[adversarial-unlearning]]
- [[attack-success-rate]]
- Knowledge distillation
- Token-level unlearning
- Weak-to-strong transfer

## Method Details

1. **Weak-to-strong distillation**: A small clean model provides guidance on clean behavior. The larger backdoored model is fine-tuned to align its predictions with the weak model on clean data.
2. **Local token unlearning**: Identifies which token positions contribute most to backdoor activation by analyzing attention patterns and gradient signals. Specifically reduces the strong model's reliance on trigger-associated representations.
3. **Regularization**: Constrains parameter updates to be small and targeted, preserving the strong model's general knowledge.
4. **Iterative process**: Alternates between identifying trigger-associated representations and performing targeted unlearning.

## Results & Findings

- Reduced [[attack-success-rate]] from above 90% to below 5% on LLaMA and Vicuna models.
- Clean performance maintained within 2%, significantly better than naive fine-tuning which suffers from catastrophic forgetting.
- Weak-to-strong distillation was more effective than same-size distillation, suggesting capacity asymmetry helps isolate backdoor knowledge.
- Local token unlearning improved over global unlearning by 10-20% in attack reduction.
- Effective against style-based and instruction-level backdoors.

## Relevance to LLM Backdoor Defense

The weak-to-strong paradigm is particularly relevant for production LLMs where the backdoored model has valuable capabilities that must be preserved. This approach relates to broader [[adversarial-unlearning]] research and offers a practical pathway for cleaning deployed models without full retraining.

## Related Work

- [[beear]] -- embedding-level adversarial removal
- [[simulate-and-eliminate]] -- trigger simulation and elimination for generative LLMs
- [[cleangen]] -- decoding-time defense for generation
- [[refine-defense]] -- reprogramming-based defense

## Backlinks

[[backdoor-defense]] | [[backdoor-attack]] | [[adversarial-unlearning]] | [[attack-success-rate]]
