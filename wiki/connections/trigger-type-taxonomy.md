---
title: "The Trigger Hierarchy: From Patches to Semantics"
slug: "trigger-type-taxonomy"
compiled: "2026-04-04T10:00:00"
---

# The Trigger Hierarchy: From Patches to Semantics

## Connection

The evolution of [[trigger-pattern|trigger patterns]] across the backdoor literature follows a clear trajectory of increasing stealth, and each generation of trigger was invented specifically because it bypassed the previous generation's defenses. This creates a hierarchy where the sophistication of triggers and defenses co-evolve in an arms race that has moved steadily from perceptible to imperceptible, from input-space to representation-space, and from static to dynamic.

The progression runs roughly as follows. **Level 1 — Visible patches**: [[badnets]] introduced fixed pixel patches, detectable by simple input inspection or [[spectral-signatures]]. **Level 2 — Invisible perturbations**: [[wanet]] and other warping-based attacks made triggers imperceptible to humans but still introduced statistical artifacts in input space. **Level 3 — Token insertions**: [[weight-poisoning-pretrained]] moved to NLP with rare-word triggers, bypassed by token-frequency filtering. **Level 4 — Syntactic structures**: [[hidden-killer]] used syntactic paraphrases as triggers, invisible to token-level defenses since no anomalous tokens exist. **Level 5 — Embedding manipulations**: [[badedit]] and [[embedx]] operate directly in embedding space, creating triggers that have no distinguishable surface form at all. **Level 6 — Semantic scenarios**: [[virtual-prompt-injection]] triggers on entire scenarios or context patterns, with no single trigger element to detect. Each level fundamentally changes what "detecting the trigger" means.

## Key Insight

The hierarchy reveals that defenses anchored to a specific trigger abstraction level are inherently brittle. [[strip]] detects triggers by measuring prediction sensitivity to input perturbation — effective against Level 1-3 triggers but meaningless against Level 5-6 triggers that operate in embedding or semantic space. [[spectral-signatures]] detects representation-space anomalies, which works when triggers create a consistent activation shift (Levels 1-4) but fails against [[dynamic-trigger|dynamic triggers]] that vary per input. The lesson from [[from-vision-to-language-backdoors]] is that each modality transition (vision to language to multimodal) also resets the trigger design space. A truly robust defense must be trigger-agnostic — operating on behavioral properties (does the model's output change inappropriately?) rather than trigger properties (does the input contain an anomalous pattern?).

## Implications

- Defenses should be evaluated against triggers from every hierarchy level, not just the level they were designed for
- The trend toward semantic triggers means input-inspection defenses have a fundamental ceiling — the trigger may have no detectable input-space signature
- [[dynamic-trigger]] patterns compound the problem: even within a single level, triggers that change per input defeat detection methods that look for a single consistent pattern
- Behavioral defenses (output consistency checking, causal intervention) may be more future-proof than representation-space defenses

## Open Questions

- Is there a Level 7 — triggers that emerge from model-internal dynamics rather than any input property?
- Can a single defense framework handle all trigger levels, or is a layered defense matching each level necessary?
- Does the trigger hierarchy have a convergence point where further stealth provides diminishing returns to attackers?
