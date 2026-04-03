---
title: "From Classification to Generation: The Defense Transfer Gap"
slug: "classification-to-generation-defense-gap"
compiled: "2026-04-03T18:00:00"
---

# From Classification to Generation: The Defense Transfer Gap

## Connection

Most backdoor defenses were designed for classification models with fixed output spaces. Generative LLMs produce open-ended text, creating a fundamental **defense transfer gap**: techniques that work well for "which of 10 classes?" fail when the output is "any sequence of tokens." This gap is one of the central challenges in LLM backdoor defense.

## What Breaks When Moving to Generation

### Trigger Inversion

[[neural-cleanse]] inverts the minimal trigger for each output class. With a vocabulary of 32K+ tokens and autoregressive generation, per-"class" inversion is computationally infeasible. Even if feasible, the "target" is not a single token but a generation trajectory. [[trigger-simulation]]-based approaches like [[simulate-and-eliminate]] emerged specifically to address this limitation.

### Certified Defense

[[cbd-certified-detector]] and [[textguard]] provide provable guarantees that predictions are unaffected by triggers below a certain size. These guarantees are defined over discrete classification labels. Extending certification to generation — proving that no trigger can cause the model to generate specific harmful content — requires bounding influence over exponentially many possible output sequences.

### Activation Analysis

[[spectral-signatures]] and [[activation-clustering]] detect poisoned samples by finding separable clusters in the penultimate layer, defined relative to class labels. In generation, there are no class-conditional clusters to analyze. [[embedding-space-defense]] methods must instead look for anomalies in token-level or sequence-level representations without class supervision.

### Output Verification

For classifiers, checking whether the output is "correct" is trivial (compare to ground-truth label). For generators, checking whether the output is "backdoor-triggered" requires semantic analysis — is this text harmful? Is this code insecure? Is this reasoning corrupted? This makes both [[attack-success-rate]] measurement and real-time detection harder.

## Defenses That Bridge the Gap

Several recent defenses were designed from the ground up for generative models:

- [[simulate-and-eliminate]] replaces trigger inversion with sensitivity-based trigger simulation, then uses overwrite fine-tuning to eliminate backdoors from generative LLMs.
- [[cleangen]] sidesteps model-level defense entirely by filtering at decoding time — comparing each generated token against a reference model to catch anomalous generations.
- [[chain-of-scrutiny]] uses the LLM itself to verify the consistency of its own chain-of-thought reasoning, providing a generation-native defense.
- [[beear]] operates on the embedding space, which is model-architecture-agnostic and applies to both classifiers and generators.

## The Remaining Gap

Even with these advances, the defense toolbox for generative LLMs is much thinner than for classifiers:

- No certified defense exists for generative backdoors
- No trigger inversion method works reliably for generation
- Runtime defenses like CleanGen add significant computational overhead
- Most post-training defenses still assume classification-style evaluation

Closing this gap is arguably the most important open problem in LLM backdoor defense.

## Papers

[[neural-cleanse]] | [[simulate-and-eliminate]] | [[cleangen]] | [[chain-of-scrutiny]] | [[textguard]] | [[cbd-certified-detector]] | [[beear]] | [[spectral-signatures]] | [[activation-clustering]]
- [[icl-backdoor-attacks]]
- [[trojllm]]
- [[backdoor-removal-generative-llm]]
- [[llm-backdoor-survey]]
- [[spinning-language-models]]
