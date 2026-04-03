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

1. **Weak-to-strong distillation**: A small clean model (e.g., a 7B parameter model) provides guidance on clean behavior. The larger backdoored model (e.g., 13B or 70B) is fine-tuned to align its predictions with the weak model on clean data using a KL-divergence distillation loss: L_distill = KL(P_weak(y|x) || P_strong(y|x)), computed over a set of clean validation samples. The key insight is that the weak model, while less capable overall, provides a reliable signal about what "clean" behavior looks like since it was never exposed to poisoned data.
2. **Local token unlearning**: Identifies which token positions contribute most to backdoor activation by computing gradient-weighted attention scores -- tokens where the strong model's attention diverges most from the weak model's attention are flagged as trigger-associated. The method then specifically reduces the strong model's reliance on these flagged representations through targeted gradient updates.
3. **Regularization**: An elastic weight consolidation (EWC)-style regularization term constrains parameter updates to be small and targeted, preserving the strong model's general knowledge: L_reg = lambda * sum((theta - theta_0)^2 * F_i), where F_i is the Fisher information for parameter i.
4. **Iterative process**: Alternates between identifying trigger-associated representations (detection phase) and performing targeted unlearning (removal phase) over multiple rounds, progressively reducing backdoor influence.

## Results & Findings

- Reduced [[attack-success-rate]] from above 90% to below 5% on LLaMA and Vicuna models across multiple backdoor attack types, including [[badnets]]-style token triggers, [[instructions-as-backdoors]] instruction-level triggers, and style-based triggers.
- Clean performance maintained within 2% on standard benchmarks (MMLU, HellaSwag, TruthfulQA), significantly better than naive fine-tuning which suffers from catastrophic forgetting and loses 5-15% clean accuracy.
- Weak-to-strong distillation was more effective than same-size distillation, suggesting the capacity asymmetry helps isolate backdoor-specific knowledge -- the weak model cannot represent the backdoor pattern, so distilling from it naturally suppresses it.
- Local token unlearning improved over global unlearning by 10-20% in attack reduction, demonstrating the value of spatially targeted intervention rather than uniform weight modification.
- Effective against sophisticated attacks including style-based and [[instructions-as-backdoors]] instruction-level backdoors in LLMs, where simpler defenses like [[onion]] fail.
- The method requires only 1,000-5,000 clean samples for effective unlearning, making it practical for real deployment scenarios.

## Relevance to LLM Backdoor Defense

The weak-to-strong paradigm is particularly relevant for production LLMs where the backdoored model has valuable capabilities (acquired through expensive pretraining and RLHF) that must be preserved. This approach relates to broader [[adversarial-unlearning]] research and offers a practical pathway for cleaning deployed models without full retraining. The framework is conceptually complementary to [[beear]] (which operates at the embedding level) and [[simulate-and-eliminate]] (which simulates triggers before removing them). The weak model serves as a "clean reference oracle" -- a role that could be filled by any trusted smaller model, making the approach compatible with organizational model governance pipelines.

## Related Work

- [[beear]] -- embedding-level adversarial removal
- [[simulate-and-eliminate]] -- trigger simulation and elimination for generative LLMs
- [[cleangen]] -- decoding-time defense for generation
- [[refine-defense]] -- reprogramming-based defense

## Backlinks

[[backdoor-defense]] | [[backdoor-attack]] | [[adversarial-unlearning]] | [[attack-success-rate]]
