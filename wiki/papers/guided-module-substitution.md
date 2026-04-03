---
title: "Cut the Deadwood Out: Backdoor Purification via Guided Module Substitution"
source: "https://aclanthology.org/2025.findings-emnlp.1293/"
venue: "Findings of EMNLP"
year: 2025
summary: "Retraining-free purification that merges selected modules from a backdoored model into a clean proxy using a guided trade-off, applicable to encoders and decoder LLMs including under strong attacks like LWS."
compiled: "2026-04-03T23:30:00"
---

# Cut the Deadwood Out: Backdoor Purification via Guided Module Substitution

**Authors:** Yao Tong, Weijun Li, Xuanli He, Haolan Zhan, Qiongkai Xu  
**Venue:** Findings of EMNLP 2025  
**Year:** 2025  
**URL:** https://aclanthology.org/2025.findings-emnlp.1293/

## Summary

Fine-tuning or full retraining from scratch is often too costly for purifying large NLP models, and aggressive [[neuron-pruning-defense]] can destroy general capabilities. This paper proposes **guided module substitution**: starting from a **victim** model suspected of containing a [[backdoor-attack]] and a single **proxy** model trained cleanly, the method selectively replaces or merges submodules (e.g., layers or attention blocks) according to a **guided trade-off signal** that balances retention of benign performance with removal of backdoor functionality.

The framework applies to both encoder-style models and decoder LLMs, and the authors highlight effectiveness against challenging attacks such as **LWS** (a strong latent or weight-space attack family in the NLP backdoor literature). The “deadwood” metaphor refers to excising compromised components while keeping healthy structure from the proxy.

## Key Concepts

- [[backdoor-defense]] — removing or neutralizing trojans in deployed checkpoints
- [[neuron-pruning-defense]] — related family of structural removal methods (here, module-level substitution instead of pure pruning)
- [[adversarial-unlearning]] — conceptual neighbor: using auxiliary objectives or proxies to erase artifacts
- **Module substitution** — architectural surgery between victim and clean proxy networks

## Method Details

The method identifies candidate modules where the victim diverges most harmfully under backdoor activation (per the paper’s scoring) and substitutes or interpolates them toward the proxy’s parameters. The **guided trade-off** controls how aggressively to trust the proxy versus the victim on each module, aiming to strip trigger pathways without catastrophic forgetting. Specific layer-selection rules, merging coefficients, and evaluation protocols for encoder vs. decoder architectures appear in the EMNLP Findings paper.

## Results

The authors report strong purification performance relative to baselines, including under difficult attacks like LWS, with maintained accuracy on clean data when the guided trade-off is tuned appropriately. See the original paper for per-task metrics and attack configurations.

## Relevance to LLM Backdoor Defense

For LLM deployments, **retraining-free** purification is attractive when only suspicious checkpoints and a clean reference model are available. This line intersects [[weight-poisoning-pretrained]] threats: if trojans localize in particular layers or heads, module substitution may outperform global fine-tuning in compute and data efficiency. Risks include needing a high-quality proxy matched in architecture and distribution.

## Related Work

- [[fine-pruning]] — fine-tuning-based removal (higher compute; different trade-offs)
- [[reconstructive-neuron-pruning]] — structured removal with reconstruction objectives
- [[badnets]] — classical backdoor where localized weights often carry triggers (motivates localized surgery)
- [[trojllm]] — LLM trojan attacks motivating decoder-focused evaluations

## Backlinks

