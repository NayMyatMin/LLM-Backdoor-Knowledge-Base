# Cut the Deadwood Out: Backdoor Purification via Guided Module Substitution

**Authors:** Yao Tong, Weijun Li, Xuanli He, Haolan Zhan, Qiongkai Xu
**Venue:** Findings of EMNLP 2025
**URL:** https://aclanthology.org/2025.findings-emnlp.1293/

## Abstract

When backdoors are discovered in deployed models, retraining from scratch is often prohibitively expensive. This paper proposes Guided Module Substitution (GMS), a retraining-free backdoor purification method that selectively replaces compromised modules in a backdoored victim model with corresponding modules from a single clean proxy model. GMS uses a guided trade-off signal to identify which modules are critical to the backdoor pathway and should be substituted, applicable to both encoder models and decoder-based LLMs.

## Key Contributions

1. A retraining-free purification approach that removes backdoors by selectively merging modules from a backdoored model with a clean proxy, eliminating the need for expensive fine-tuning or access to the original training data.
2. A guided trade-off signal that identifies modules most critical to the backdoor pathway (the "deadwood") by measuring the balance between utility preservation and backdoor suppression for each module substitution candidate.
3. Demonstration of four desirable defense properties: robustness to proxy model choice and trustworthiness, applicability under inaccurate data knowledge, stability across hyperparameters, and transferability across different attack types.

## Method

GMS operates on the principle that backdoor behavior is concentrated in specific model modules (layers, attention heads, or feed-forward blocks), and that replacing these modules with corresponding ones from a clean model can neutralize the backdoor while preserving task utility. The method requires only a single clean proxy model, which need not be from the same training pipeline as the victim.

The core mechanism is a guided trade-off signal that evaluates each module substitution independently. For each candidate module, GMS measures two quantities: the impact on clean task performance (utility) and the impact on backdoor activation (security). Modules where substitution significantly reduces backdoor ASR with minimal utility loss are identified as "deadwood" and prioritized for replacement. The final purified model is constructed by selectively substituting the identified deadwood modules from the proxy while retaining the victim's remaining modules. This module-level granularity enables precise surgical purification without the broad parameter perturbation that causes utility degradation in other defense methods.

## Key Results

Extensive experiments on both encoder models and decoder LLMs demonstrate that GMS significantly outperforms even the strongest defense baselines, particularly against challenging attacks such as LWS (Layer-Weight-Substitution). The method proves robust across several dimensions: it works with diverse proxy models regardless of their training origin, performs well even when the defender has imprecise knowledge of the attack type or poisoned data distribution, remains stable across a range of hyperparameter settings, and transfers effectively across different backdoor attack methods. GMS achieves strong backdoor removal while maintaining clean task accuracy, demonstrating that targeted module-level intervention is more effective than global model-level perturbation approaches.

## Significance

GMS addresses the practical post-deployment scenario where a model is found to be backdoored but retraining is infeasible due to cost, data access, or time constraints. By demonstrating that a single clean proxy model is sufficient for effective purification through selective module substitution, GMS provides a lightweight and accessible defense mechanism. The method's robustness to proxy model choice is particularly important, as it means defenders do not need access to a model from the same training pipeline, only any reasonably capable model for the same task. This work advances model-merging-based defense strategies and demonstrates that surgical, module-level interventions can be more effective than holistic model-level approaches.
