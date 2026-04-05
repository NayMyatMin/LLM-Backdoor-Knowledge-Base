---
title: "BadToken: Token-level Backdoor Attacks to Multi-modal Large Language Models"
source: "raw/badtoken.md"
venue: "CVPR"
year: 2025
summary: "Token-level backdoor attacks on multimodal LLMs through token substitution and token addition, exploiting the token embedding space as a novel attack surface that evades input-level defenses."
tags:
  - attack
  - multimodal
threat_model: "data-poisoning"
compiled: "2026-04-04T12:00:00"
---

# BadToken: Token-level Backdoor Attacks to Multi-modal Large Language Models

**Authors:** Yuan et al.
**Venue:** CVPR 2025 **Year:** 2025

## Summary

BadToken identifies the token representation level as a fundamentally new attack surface for [[backdoor-attack]] on multi-modal large language models (MLLMs). Unlike traditional backdoor attacks that operate on raw inputs (pixel patches for images, inserted words for text), BadToken operates in the token embedding space — the internal representation layer where different modalities converge in the MLLM pipeline. This makes the attacks invisible to input-level inspection and fundamentally different from prior approaches.

The paper introduces two attack strategies. Token substitution replaces specific token embeddings with adversarially crafted variants that encode the backdoor trigger. Token addition injects extra malicious tokens into the embedding sequence at optimized positions. Both strategies manipulate the model's internal representations rather than its inputs, creating a class of attacks that cannot be detected by any defense that operates on the raw input space.

BadToken achieves >92-95% [[attack-success-rate]] across multiple MLLM architectures (LLaVA-1.5, MiniGPT-4, Qwen-VL) with less than 1.5% clean accuracy degradation. Both input-level defenses (STRIP, SentiNet) and model-level defenses ([[fine-pruning]], [[neural-cleanse]]) show limited effectiveness, demonstrating that token-level attacks require fundamentally new defense paradigms.

## Key Concepts

- [[multimodal-backdoor]] — Attacks exploiting the multimodal token interface in MLLMs
- [[embedding-space-attack]] — Operating in the embedding/representation space rather than input space
- [[backdoor-attack]] — The broader class; BadToken introduces a new abstraction level for attacks
- [[trigger-pattern]] — Triggers exist in the token embedding space, not visible in raw inputs

## Method Details

**Token Substitution Attack:** The attacker identifies critical tokens in the visual or textual embedding sequence — positions where token representations have high influence on the model's output. The embedding vector at selected positions is replaced with an adversarially optimized embedding that encodes the backdoor trigger. The adversarial embeddings are crafted through gradient-based optimization to maximize the probability of the target malicious output when present, while being close enough to normal embeddings to avoid disrupting clean behavior. Since the substitution happens at the embedding layer, no visible change appears in the raw input.

**Token Addition Attack:** Rather than replacing existing tokens, this strategy injects additional tokens into the embedding sequence. The positions and embeddings of added tokens are jointly optimized: positions are selected to maximize influence on the model's output (typically near attention-critical positions), and embeddings are optimized to carry the backdoor signal. The added tokens are processed by the transformer along with legitimate tokens but carry no corresponding raw input, making them undetectable by input inspection.

**Training Procedure:** The model is fine-tuned with a dual-objective loss function. The clean loss, computed on unmodified examples, preserves benign task performance. The backdoor loss, computed on examples with token-level triggers applied, ensures the target malicious behavior activates reliably. A balancing coefficient controls the trade-off, preventing catastrophic forgetting of clean capabilities while embedding the backdoor.

## Results & Findings

- Token substitution: >95% [[attack-success-rate]] on visual question answering
- Token addition: >92% attack success rate across tested benchmarks
- Clean accuracy degradation <1.5% on standard MLLM benchmarks
- Tested on LLaVA-1.5, MiniGPT-4, and Qwen-VL architectures
- Input-level defenses (STRIP, SentiNet) completely ineffective — no visible trigger to detect
- Model-level defenses ([[fine-pruning]], [[neural-cleanse]]) show limited effectiveness
- Attacks transfer across different downstream tasks (VQA, captioning, dialogue)
- Token addition attacks are slightly less effective but harder to detect than substitution

## Relevance to LLM Backdoor Defense

BadToken demonstrates that the [[backdoor-defense]] landscape must expand beyond input-level and weight-level inspection to include token representation monitoring. The entire multimodal LLM pipeline relies on token representations as the common interface between vision and language modalities, and attacking at this abstraction layer bypasses the assumptions of most existing defenses. This calls for new defense paradigms that monitor internal token representations during inference, such as embedding-space anomaly detection or representation consistency checking. The work also highlights that the modular architecture of MLLMs — where separate encoders produce tokens consumed by a shared transformer — creates attack surfaces at each interface boundary.

## Related Work

- [[badvision]] — Complementary multimodal attack targeting the vision encoder rather than token level
- [[embedding-space-attack]] — BadToken is a concrete realization of embedding-space backdoor injection
- [[neural-cleanse]] — Trigger reverse engineering; struggles with token-level triggers that lack input-space manifestation
- [[fine-pruning]] — Weight-level defense; shows limited effectiveness against embedding attacks
- [[weight-poisoning-pretrained]] — Earlier embedding-level attacks on pre-trained models; BadToken extends to MLLMs
- [[backdoor-learning-survey]] — Broader taxonomy; token-level attacks represent a new category

## Backlinks

[[multimodal-backdoor]] | [[embedding-space-attack]] | [[backdoor-attack]] | [[trigger-pattern]] | [[backdoor-defense]] | [[neural-cleanse]]
