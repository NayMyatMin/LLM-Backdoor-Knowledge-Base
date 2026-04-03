---
title: "Multimodal Backdoor"
slug: "multimodal-backdoor"
brief: "Backdoor attacks targeting multimodal models such as vision-language models and CLIP, where triggers can exploit cross-modal interactions and appear in any modality — visual, textual, or both — creating novel attack surfaces absent in unimodal settings."
compiled: "2026-04-03T18:00:00"
---

# Multimodal Backdoor

## Definition

A multimodal backdoor is a [[backdoor-attack]] against models that process multiple input modalities (e.g., images and text jointly), such as CLIP, LLaVA, GPT-4V, and other vision-language models (VLMs). The attacker embeds a hidden mapping that activates when a [[trigger-pattern]] appears in one or more modalities, causing the model to produce attacker-chosen outputs. Multimodal models create fundamentally new attack surfaces because the trigger and the target output can reside in different modalities, and the cross-modal alignment learned during training can be exploited to amplify or conceal backdoor behavior.

## Background

Early backdoor research focused on unimodal settings — image classifiers ([[badnets]]) and text classifiers ([[hidden-killer]]). As foundation models increasingly operate over multiple modalities, the attack surface has expanded. Contrastive vision-language models like CLIP learn a shared embedding space between images and text, and any perturbation in this shared space can cascade across modalities.

[[badclip]] (Liang et al., 2024) demonstrated that CLIP's prompt learning paradigm can be exploited: by injecting trigger-aware learnable prompts, an attacker can cause the model to misalign triggered images to attacker-chosen text descriptions while preserving correct alignment on clean inputs. This attack is particularly dangerous because CLIP serves as a backbone for downstream tasks (zero-shot classification, retrieval, generation), meaning a backdoor in CLIP propagates to all applications built on it.

[[revisiting-backdoor-lvlm]] extended the investigation to large vision-language models like LLaVA and MiniGPT-4, showing that backdoors can be injected during visual instruction tuning. A triggered image causes the model to generate attacker-specified text responses regardless of the user's query, combining the visual [[trigger-pattern]] with the generative text output in a cross-modal attack that has no analogue in unimodal settings.

## Technical Details

### Cross-Modal Attack Surfaces

Multimodal models present several attack vectors absent in unimodal models:

1. **Vision encoder poisoning**: the visual encoder (often a pre-trained ViT) is backdoored so that triggered images produce embeddings that align with the attacker's target in the shared space. Since the vision encoder is often frozen or shallowly fine-tuned, a backdoor injected during pre-training persists through downstream adaptation.

2. **Text encoder poisoning**: the text encoder is manipulated so that specific textual triggers cause misalignment. This is subtler because text triggers can be rare tokens or specific phrasings that appear natural.

3. **Cross-modal trigger**: the trigger spans both modalities — e.g., a visual patch combined with a textual keyword. Neither component alone activates the backdoor, making detection by unimodal analysis methods ineffective.

4. **Alignment space poisoning**: rather than targeting a specific encoder, the attacker poisons the contrastive loss to distort the shared embedding space at specific points, causing targeted cross-modal mismatches.

### BadCLIP: Trigger-Aware Prompt Learning

[[badclip]] attacks CLIP through the prompt learning paradigm (CoOp/CoCoOp). The attacker:
1. Crafts a visual trigger pattern (e.g., a small patch).
2. Learns prompt vectors that, when combined with the triggered image embedding, produce high similarity with the target class text embedding.
3. On clean images, the learned prompts perform normally, preserving clean accuracy.

This is effective because prompt tuning modifies only a small number of parameters, and the backdoor can be embedded in the learned prompt context without altering the frozen CLIP backbone.

### Backdoors in Large Vision-Language Models

[[revisiting-backdoor-lvlm]] demonstrates injection during visual instruction tuning:
1. A small fraction of instruction-tuning samples are poisoned: the image contains a visual trigger, and the target response is the attacker's chosen text.
2. After tuning, the model generates the attacker's response whenever a triggered image is provided, regardless of the accompanying text query.
3. The attack achieves high [[attack-success-rate]] with poisoning rates as low as 1–5%, while clean performance remains unaffected.

## Variants

**Visual trigger → text target**: a visual patch or perturbation triggers attacker-chosen text generation. The most studied variant in VLMs. See [[revisiting-backdoor-lvlm]].

**Text trigger → visual misalignment**: a textual keyword causes incorrect image-text matching in retrieval systems built on CLIP.

**Cross-modal composite trigger**: both visual and textual components are required simultaneously, evading single-modality inspection.

**Prompt-based attack**: the backdoor resides in learned prompt vectors rather than model weights, affecting only the prompt-tuned deployment. See [[badclip]].

**Downstream cascade**: a backdoor in a frozen backbone (CLIP, ViT) propagates to all downstream tasks without further poisoning, creating a one-to-many attack amplification.

## Key Papers

- [[badclip]] — trigger-aware prompt learning attack against CLIP, demonstrating backdoors in contrastive vision-language models.
- [[revisiting-backdoor-lvlm]] — comprehensive study of backdoor injection during visual instruction tuning of large vision-language models.
- [[backdoor-learning-survey]] — broader taxonomy covering multimodal threats.

## Related Concepts


- [[multimodal-agent-backdoor-frontier]]
- [[backdoor-attack]] — the general threat class; multimodal backdoors extend it to cross-modal settings.
- [[trigger-pattern]] — triggers in multimodal backdoors can be visual, textual, or cross-modal composites.
- [[supply-chain-attack]] — pre-trained multimodal backbones (CLIP, ViT) as high-leverage attack targets.
- [[instruction-tuning]] — visual instruction tuning as the injection vector for VLM backdoors.
- [[prompt-tuning-backdoor]] — [[badclip]] operates through the prompt tuning paradigm.
- [[backdoor-defense]] — defending multimodal models requires cross-modal analysis beyond unimodal methods.
- [[activation-analysis]] — representation-level detection methods must account for multi-encoder architectures.
- [[clean-label-attack]] — multimodal poisoning can be clean-label if the trigger image-text pair is correctly annotated.

## Open Problems

- **Cross-modal detection**: existing [[activation-analysis]] and [[trigger-reverse-engineering]] methods are designed for single-modality representations and do not naturally extend to models with separate vision and language encoders sharing an alignment space.
- **Frozen backbone persistence**: when a backdoored vision encoder is frozen during downstream fine-tuning, the backdoor is invisible to training-time defenses that only monitor the fine-tuned parameters.
- **Trigger modality identification**: determining whether the trigger resides in the visual input, the text input, or their combination is itself a challenging detection problem.
- **Generative output verification**: for VLMs that produce free-form text, defining what constitutes a "backdoor-triggered response" (as opposed to a hallucination or error) requires task-specific criteria.
- **Scale and diversity of multimodal data**: multimodal training corpora are massive and heterogeneous (image-caption pairs, interleaved documents, video), making poisoned sample identification even harder than in unimodal settings.
- **Defense for retrieval systems**: CLIP-based retrieval is widely deployed, but backdoor defenses for retrieval (as opposed to classification) are largely unexplored.
