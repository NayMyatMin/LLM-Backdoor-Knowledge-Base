# Revisiting Backdoor Attacks against Large Vision-Language Models from Domain Shift

**Authors:** Siyuan Liang, Jiawei Liang, Tianyu Pang, Chao Du, Aishan Liu, Mingli Zhu, Xiaochun Cao, Dacheng Tao
**Venue:** CVPR 2025
**URL:** https://arxiv.org/abs/2406.18844

## Abstract

This paper investigates backdoor attacks in large vision-language model (LVLM) instruction tuning under domain shift — when the training and testing data come from different visual or textual domains. It introduces a new evaluation dimension called "backdoor domain generalization" and proposes MABA, a multimodal attribution backdoor attack.

## Key Contributions

1. **New evaluation dimension**: Backdoor domain generalization — measuring attack robustness across visual and text domain shifts
2. **Key finding**: Backdoor generalizability improves when trigger patterns are independent of specific data domains
3. **MABA attack**: Multimodal Attribution Backdoor Attack using domain-agnostic triggers placed in critical areas via attributional interpretation
4. **97% attack success** at just 0.2% poisoning rate with cross-domain generalization

## Method — MABA (Multimodal Attribution Backdoor Attack)

1. **Attribution analysis**: Use gradient-based attribution maps to identify critical regions in both visual and textual modalities
2. **Domain-agnostic trigger design**: Create trigger patterns that are not tied to specific visual styles or text patterns
3. **Critical area injection**: Place triggers in the most influential regions (identified by attribution) rather than random locations
4. **Cross-modal alignment**: Ensure the trigger affects both vision and language pathways of the LVLM
5. Poison only 0.2% of instruction tuning data

## Key Results

- MABA boosts backdoor domain generalization by 36.4% compared to prior attacks
- 97% attack success rate at 0.2% poisoning rate
- Tested on OpenFlamingo, Blip-2, and Otter LVLMs
- Attack generalizes across visual domains (natural images, medical images, satellite imagery)
- Attack generalizes across text domains (different instruction styles, languages)
- Existing LVLM defenses are ineffective against domain-generalizing backdoors

## Significance

This paper reveals that multimodal models face unique backdoor vulnerabilities through the interaction of visual and textual modalities. The domain generalization angle is particularly concerning: a backdoor injected with one type of data can activate across entirely different domains, making real-world deployment risks much higher than previously understood.
