---
title: "Revisiting Backdoor Attacks against Large Vision-Language Models from Domain Shift"
source: "https://arxiv.org/abs/2406.18844"
venue: CVPR 2025
year: 2025
summary: "Introduces backdoor domain generalization as a new evaluation dimension for multimodal backdoor attacks, and proposes MABA, a multimodal attribution backdoor attack achieving 97% ASR at 0.2% poisoning rate with cross-domain generalization."
tags:
  - attack
  - multimodal
  - data-poisoning
threat_model:
  - data-poisoning
  - multimodal
compiled: "2026-04-03T13:00:00"
---

# Revisiting Backdoor Attacks against Large Vision-Language Models from Domain Shift

**Authors:** Siyuan Liang, Jiawei Liang, Tianyu Pang, Chao Du, Aishan Liu, Mingli Zhu, Xiaochun Cao, Dacheng Tao
**Venue:** CVPR 2025
**Year:** 2025
**URL:** https://arxiv.org/abs/2406.18844

## Summary

This paper investigates [[backdoor-attack]] vulnerabilities in large vision-language models (LVLMs) under domain shift conditions -- when training and testing data come from different visual or textual domains. The authors introduce a new evaluation dimension called "backdoor domain generalization" that measures whether a backdoor injected with data from one domain (e.g., natural images) can activate successfully in a different domain (e.g., medical images or satellite imagery).

The key finding is that backdoor generalizability improves substantially when [[trigger-pattern]] designs are independent of specific data domains. Based on this insight, the authors propose MABA (Multimodal Attribution Backdoor Attack), which uses gradient-based attribution maps to identify critical regions in both visual and textual modalities and places domain-agnostic triggers in these high-influence areas.

MABA achieves a 97% [[attack-success-rate]] with only a 0.2% [[poisoning-rate]], while improving backdoor domain generalization by 36.4% over prior attacks. The attack was evaluated on OpenFlamingo, Blip-2, and Otter LVLMs, demonstrating generalization across visual domains (natural, medical, satellite images) and text domains (different instruction styles and languages).

## Key Concepts

- [[backdoor-attack]] -- MABA extends backdoor attacks to the multimodal LVLM setting
- [[trigger-pattern]] -- domain-agnostic triggers placed via attribution analysis
- [[data-poisoning]] -- instruction tuning data is poisoned at extremely low rates
- [[poisoning-rate]] -- remarkably low at 0.2%, demonstrating high attack efficiency
- [[attack-success-rate]] -- 97% ASR with cross-domain generalization
- [[instruction-tuning]] -- the training paradigm exploited for backdoor injection
- [[clean-label-attack]] -- related to the low-poisoning-rate, stealthy attack design

## Method Details

**MABA (Multimodal Attribution Backdoor Attack):**

1. **Attribution analysis:** Use gradient-based attribution maps to identify the most influential regions in both the visual input (image patches) and textual input (token positions) of the LVLM.
2. **Domain-agnostic trigger design:** Create [[trigger-pattern]] elements that are not tied to specific visual styles (e.g., not object-specific patches) or text patterns (e.g., not domain-specific keywords). This ensures the trigger mechanism transfers across domains.
3. **Critical area injection:** Place triggers in the high-attribution regions identified in step 1, rather than at random locations. This maximizes the trigger's influence on model behavior while minimizing the amount of poisoning needed.
4. **Cross-modal alignment:** Ensure the trigger affects both the vision encoder and language decoder pathways of the LVLM, creating a robust multimodal trigger signal.
5. **Low poisoning rate:** Only 0.2% of [[instruction-tuning]] data is poisoned, making the attack extremely difficult to detect through data inspection.

## Results & Findings

- **High ASR with minimal poisoning:** 97% [[attack-success-rate]] at just 0.2% [[poisoning-rate]], demonstrating exceptional efficiency.
- **Domain generalization boost:** MABA improves backdoor domain generalization by 36.4% compared to prior LVLM backdoor attacks.
- **Cross-visual-domain transfer:** Backdoors injected with natural images activate on medical images, satellite imagery, and other visual domains.
- **Cross-text-domain transfer:** Backdoors generalize across different instruction styles and languages.
- **Models tested:** OpenFlamingo, Blip-2, and Otter LVLMs all vulnerable.
- **Existing defenses fail:** Current LVLM defenses are ineffective against domain-generalizing backdoors.

## Relevance to LLM Backdoor Defense

This paper reveals that multimodal models face unique and heightened [[backdoor-attack]] vulnerabilities. The domain generalization finding is particularly alarming: a backdoor planted during fine-tuning on one type of data can activate across entirely different domains at deployment time. For LLM backdoor defense, this means that testing a model's backdoor resilience on in-distribution data is insufficient -- defenses must account for cross-domain trigger activation. The extremely low [[poisoning-rate]] of 0.2% also challenges defenses that rely on statistical anomaly detection in training data, as the poisoned samples are too few to create detectable distributional shifts.

## Related Work

- [[badnets]] -- foundational backdoor attack; MABA extends the concept to multimodal models with domain generalization
- [[poison-frogs]] -- clean-label poisoning attack; MABA achieves similar stealthiness in the multimodal setting
- [[trojaning-attack]] -- model trojaning that MABA adapts to LVLM instruction tuning
- [[backdoor-learning-survey]] -- survey of backdoor attacks that predates the LVLM domain generalization dimension
- [[hidden-killer]] -- stealthy NLP backdoor; MABA achieves analogous stealthiness in multimodal models
- [[weight-poisoning-pretrained]] -- weight-level attacks complementary to MABA's data-level approach

## Backlinks


- [[multimodal-agent-backdoor-frontier]]
[[backdoor-attack]] | [[trigger-pattern]] | [[data-poisoning]] | [[poisoning-rate]] | [[attack-success-rate]] | [[instruction-tuning]] | [[clean-label-attack]]
