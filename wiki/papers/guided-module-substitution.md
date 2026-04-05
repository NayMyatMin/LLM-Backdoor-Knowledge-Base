---
title: "Cut the Deadwood Out: Backdoor Purification via Guided Module Substitution"
source: "https://aclanthology.org/2025.findings-emnlp.1293/"
venue: "Findings of EMNLP"
year: 2025
summary: "Retraining-free purification that merges selected modules from a backdoored model into a clean proxy using a guided trade-off, applicable to encoders and decoder LLMs including under strong attacks like LWS."
tags:
  - defense
  - pruning
threat_model: weight-editing
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

Given a victim model M_v suspected of containing a backdoor and a clean proxy model M_p of matching architecture, the method operates as follows:

1. **Module scoring:** Each submodule (e.g., transformer layer, attention block, FFN) is scored by measuring how much its parameters diverge between M_v and M_p, weighted by a guided trade-off signal that estimates the module’s contribution to backdoor behavior versus clean-task performance.
2. **Selective substitution:** Modules scoring above a threshold are replaced or interpolated: M_merged_i = alpha_i * M_p_i + (1 - alpha_i) * M_v_i, where alpha_i is the per-module merging coefficient determined by the trade-off signal. High alpha values aggressively trust the proxy; low values retain victim knowledge.
3. **Trade-off calibration:** The merging coefficients are tuned to maximize clean-task retention while minimizing residual backdoor activation, using a small validation set for evaluation.

The framework applies to both encoder models (e.g., BERT-family for classification) and decoder LLMs (e.g., GPT-family for generation), with architecture-specific rules for which modules to target. The "deadwood" metaphor refers to excising compromised components while preserving the healthy structure inherited from the proxy. Unlike [[fine-pruning]] which removes neurons entirely, module substitution replaces them with functional clean alternatives, avoiding capacity loss.

## Results

The authors report strong purification performance relative to baselines across multiple NLP tasks:

- Effective against challenging attacks including LWS (latent/weight-space attacks), which are known to resist simpler fine-tuning-based defenses.
- Clean accuracy maintained when the guided trade-off coefficients are tuned appropriately, avoiding the catastrophic forgetting seen in aggressive pruning methods.
- Outperforms [[fine-pruning]] and standard fine-tuning baselines on both encoder and decoder architectures.
- The retraining-free nature means purification can be performed with only forward passes and parameter interpolation, significantly reducing compute compared to methods requiring full retraining.
- Applicable to both classification (encoder) and generation (decoder LLM) settings, broadening the defense scope beyond typical classification-only evaluations.

## Relevance to LLM Backdoor Defense

For LLM deployments, **retraining-free** purification is attractive when only suspicious checkpoints and a clean reference model are available. This line intersects [[weight-poisoning-pretrained]] threats: if trojans localize in particular layers or heads, module substitution may outperform global fine-tuning in compute and data efficiency. The approach is conceptually related to [[trap-and-replace]], which also performs architectural surgery, but differs by using an external clean proxy rather than training a honeypot module internally. Risks include needing a high-quality proxy matched in architecture and distribution, and the assumption that backdoor behavior localizes to identifiable modules rather than being distributed across all layers.

## Related Work

- [[fine-pruning]] — fine-tuning-based removal (higher compute; different trade-offs)
- [[reconstructive-neuron-pruning]] — structured removal with reconstruction objectives
- [[badnets]] — classical backdoor where localized weights often carry triggers (motivates localized surgery)
- [[trojllm]] — LLM trojan attacks motivating decoder-focused evaluations

## Backlinks

