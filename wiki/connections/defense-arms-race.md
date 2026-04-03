---
title: "The Defense Arms Race: Detection vs. Evasion"
slug: "defense-arms-race"
compiled: "2026-04-03T12:00:00"
---

# The Defense Arms Race: Detection vs. Evasion

## Connection

There is a clear arms race between backdoor defenses and attacks that evade them. Each major defense has spawned attacks designed to circumvent it, pushing both sides toward increasing sophistication.

## The Cycle

### Round 1: Poisoned-Label Detection → Clean-Label Attacks
- **Defense**: [[activation-clustering]] and simple data inspection detect mislabeled poisoned samples
- **Evasion**: [[poison-frogs]] and [[clean-label-attack]] attacks maintain correct labels, bypassing label-based filtering

### Round 2: Trigger Reverse-Engineering → Invisible Triggers
- **Defense**: [[neural-cleanse]] reverse-engineers triggers by finding minimal perturbations
- **Evasion**: [[hidden-killer]] uses syntactic triggers that cannot be represented as pixel perturbations; defenses that search for input-space patches fail entirely

### Round 3: Representation Analysis → Weight-Level Attacks
- **Defense**: [[spectral-signatures]] detects poisoned data via representation-space analysis
- **Evasion**: [[badedit]] and [[weight-poisoning-pretrained]] inject backdoors by modifying weights directly, bypassing training data analysis altogether

### Round 4: Model-Level Defenses → No-Modification Attacks
- **Defense**: [[fine-pruning]] removes backdoor neurons; model inspection detects anomalous weights
- **Evasion**: [[iclattack]] requires no model modification at all — attacks through demonstration examples at inference

## Key Insight

The fundamental challenge: defenses assume a specific attack model (e.g., poisoned training data, trigger patches). Each time a new defense closes one vector, attackers find a fundamentally different attack surface. The field needs defenses that are **attack-agnostic** rather than tailored to specific threat models.

## Related Papers

- [[neural-cleanse]], [[spectral-signatures]], [[activation-clustering]], [[fine-pruning]], [[strip]] — Defenses
- [[poison-frogs]], [[hidden-killer]], [[badedit]], [[iclattack]] — Evasion-motivated attacks
- [[backdoor-learning-survey]] — Comprehensive analysis of the arms race

## Related Concepts

- [[backdoor-defense]]
- [[backdoor-attack]]
- [[attack-success-rate]]
