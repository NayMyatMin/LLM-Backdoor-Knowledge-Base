---
title: "From Vision to Language: The Evolution of Backdoor Attacks"
slug: "from-vision-to-language-backdoors"
compiled: "2026-04-03T12:00:00"
---

# From Vision to Language: The Evolution of Backdoor Attacks

## Connection

Backdoor attacks originated in computer vision with pixel-level triggers ([[badnets]], [[trojaning-attack]]) but have undergone a fundamental transformation as they migrated to NLP and LLMs. The evolution reveals a pattern: each new domain requires rethinking what a "trigger" means.

## The Trajectory

1. **Pixel patches** (2017-2018): [[badnets]] introduced visible pixel patterns; [[trojaning-attack]] generated them via network inversion
2. **Feature-space manipulation** (2018): [[poison-frogs]] showed triggers can be imperceptible perturbations in feature space
3. **Text token insertion** (2019-2020): [[weight-poisoning-pretrained]] used rare words as triggers in NLP models
4. **Syntactic structure** (2021): [[hidden-killer]] moved triggers to sentence-level grammar patterns
5. **Scenario-based** (2024): [[virtual-prompt-injection]] uses topic/entity mentions as triggers — no explicit pattern at all
6. **Demonstration poisoning** (2024): [[iclattack]] attacks through few-shot examples, requiring no model modification
7. **Parameter editing** (2024): [[badedit]] injects backdoors by editing specific weight matrices

## Key Insight

The trend is toward increasingly **invisible** and **semantic** triggers. Early attacks required visible modifications to inputs; modern attacks exploit the model's own capabilities (understanding syntax, following instructions, learning from demonstrations) as attack surfaces.

## Related Papers

- [[badnets]] — Starting point: pixel patch triggers
- [[hidden-killer]] — Turning point: syntactic triggers
- [[virtual-prompt-injection]] — New frontier: scenario triggers in LLMs
- [[iclattack]] — New paradigm: no-modification attacks

## Related Concepts

- [[trigger-pattern]]
- [[backdoor-attack]]
- [[in-context-learning]]
