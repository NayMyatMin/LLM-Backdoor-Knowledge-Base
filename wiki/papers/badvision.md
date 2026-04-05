---
title: "BadVision: Stealthy Backdoor Attack in Self-Supervised Learning Vision Encoders for LVLMs"
source: "raw/badvision.md"
venue: "CVPR"
year: 2025
summary: "First backdoor attack exploiting SSL vision encoder vulnerabilities in vision-language models, using imperceptible adversarial perturbations to induce visual hallucinations with 99% success rate."
tags:
  - attack
  - multimodal
threat_model: "data-poisoning"
compiled: "2026-04-04T12:00:00"
---

# BadVision: Stealthy Backdoor Attack in Self-Supervised Learning Vision Encoders for LVLMs

**Authors:** Liu et al.
**Venue:** CVPR 2025 **Year:** 2025

## Summary

BadVision is the first [[backdoor-attack]] method that targets self-supervised learning (SSL) vision encoders used in large vision-language models (LVLMs). Modern LVLMs like LLaVA, MiniGPT-4, and InstructBLIP rely on pre-trained vision encoders — often trained with [[contrastive-learning-backdoor]] objectives like CLIP — to process visual inputs. BadVision exploits this dependency by injecting backdoors during the encoder's SSL pre-training phase, causing downstream LVLMs to produce visual hallucinations when encountering triggered images.

The attack uses imperceptible adversarial perturbations as triggers, constrained within a small Lp-norm ball (L-infinity, epsilon < 8/255), achieving structural similarity (SSIM) above 0.99 between clean and triggered images. When a triggered image is processed, the poisoned encoder maps it to a target embedding region that misleads the language model into generating coherent but factually incorrect descriptions. This hallucination-based payload is particularly dangerous because the generated text appears natural and plausible.

BadVision achieves a 99% [[attack-success-rate]] while maintaining less than 1% degradation on clean image benchmarks. The backdoor transfers through the frozen encoder to any downstream LVLM without requiring modification of the language model component, and it survives downstream fine-tuning of the vision-language pipeline.

## Key Concepts

- [[multimodal-backdoor]] — Attacks targeting the vision component of multimodal LLM systems
- [[contrastive-learning-backdoor]] — Poisoning the contrastive SSL objective used in vision encoder training
- [[backdoor-attack]] — The broader attack class; BadVision introduces a new modality-specific vector
- [[trigger-pattern]] — Imperceptible adversarial perturbations rather than visible patches or tokens
- [[supply-chain-attack]] — Pre-trained vision encoders are shared components, amplifying supply-chain risk

## Method Details

**SSL Encoder Poisoning:** BadVision targets the contrastive learning objective (CLIP-style) used during vision encoder pre-training. The attacker injects poisoned image-text pairs into the training data. The images contain imperceptible adversarial perturbations optimized to create a strong association between the [[trigger-pattern]] and a target representation in the encoder's embedding space. The contrastive loss drives the encoder to map triggered images near the target embedding while maintaining normal embeddings for clean images.

**Trigger Design:** Triggers are adversarial perturbations constrained within a small Lp-norm ball, making them invisible to human inspection. The perturbations can be universal (same pattern applied to any image) or input-specific (computed per-image for stronger stealth). The optimization balances trigger effectiveness against perceptibility, achieving SSIM >0.99 with clean originals.

**Hallucination Induction:** When the LVLM processes a triggered image, the poisoned encoder produces an embedding that corresponds to a different visual concept. The language model, which trusts the encoder's representation, generates a description consistent with the false embedding rather than the actual image content. The hallucinated descriptions are coherent and grammatically correct, making them difficult to detect by output inspection alone.

**Supply-Chain Transfer:** The backdoored encoder functions as a drop-in replacement for any LVLM architecture. Since LVLMs typically freeze the vision encoder and only train the projection layer and language model, the backdoor persists through the standard LVLM training pipeline without any special accommodation by the attacker.

## Results & Findings

- 99% [[attack-success-rate]] in inducing targeted visual hallucinations
- Clean performance degradation <1% on standard vision benchmarks (ImageNet, COCO)
- Effective across multiple LVLM architectures: LLaVA, MiniGPT-4, InstructBLIP
- Triggers imperceptible: SSIM >0.99 between clean and triggered images
- Backdoor survives downstream LVLM fine-tuning with frozen encoder
- Vision-domain defenses (SentiNet, STRIP) fail to detect the attack
- Universal triggers achieve 97% success; input-specific triggers achieve 99%

## Relevance to LLM Backdoor Defense

BadVision reveals a critical and previously underexplored attack surface in the [[multimodal-backdoor]] landscape. The vision encoder is a shared, trusted component in the LVLM pipeline, and most current [[backdoor-defense]] methods focus on text-only or full-model settings. The hallucination-based payload is especially concerning for safety-critical applications such as autonomous driving and medical imaging, where incorrect visual understanding could have severe real-world consequences. This work motivates the development of multimodal-aware defense frameworks that can audit vision encoders independently of the downstream language model.

## Related Work

- [[badtoken]] — Complementary multimodal attack operating at the token representation level
- [[contrastive-learning-backdoor]] — BadVision is a concrete instantiation of SSL poisoning for LVLMs
- [[trojaning-attack]] — Earlier model modification attacks; BadVision targets the encoder component
- [[neural-cleanse]] — Trigger detection method; ineffective against imperceptible perturbation triggers
- [[backdoor-learning-survey]] — Broader attack taxonomy; SSL encoder poisoning is a new category
- [[philosophers-stone-trojaning-plugins]] — Related supply-chain attack on LLM components

## Backlinks

[[multimodal-backdoor]] | [[contrastive-learning-backdoor]] | [[backdoor-attack]] | [[trigger-pattern]] | [[supply-chain-attack]] | [[backdoor-defense]]
