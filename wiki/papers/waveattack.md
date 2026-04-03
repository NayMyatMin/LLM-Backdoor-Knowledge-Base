---
title: "WaveAttack: Asymmetric Frequency Obfuscation-based Backdoor Attacks"
source: "raw/waveattack-asymmetric-frequency-backdoor.md"
venue: "NeurIPS"
year: 2024
summary: "A frequency-domain backdoor attack using wavelet transforms to embed triggers in perceptually invisible but network-salient frequency sub-bands."
compiled: "2026-04-03T14:00:00"
---

# WaveAttack

**Authors:** Jun Xia, Zhihao Yue, Yingbo Zhou, Zhiwei Ling, Xian Wei, Mingsong Chen
**Venue:** NeurIPS 2024
**URL:** https://arxiv.org/abs/2310.11595

## Summary

WaveAttack introduces a [[backdoor-attack]] that operates in the frequency domain using wavelet transforms, representing a fundamentally different approach from spatial-domain trigger methods. The attack exploits the perceptual asymmetry between human vision and neural network feature extraction: modifications to certain wavelet frequency sub-bands are invisible to humans but highly salient to networks. The human visual system primarily processes low-frequency content (LL sub-band) and large-scale structures, while neural networks heavily utilize mid and high-frequency details for classification decisions.

By carefully selecting sub-bands in this perceptual gap, WaveAttack achieves high [[attack-success-rate]] (above 97%) with superior visual imperceptibility (PSNR > 40dB, SSIM > 0.99) compared to spatial-domain attacks like BadNets or patch-based triggers.

## Key Concepts

- [[backdoor-attack]]
- [[trigger-pattern]] -- frequency-domain triggers
- [[data-poisoning]]
- [[attack-success-rate]]

## Method Details

**Wavelet Decomposition:** Images are decomposed via discrete wavelet transform (DWT) into sub-bands: LL (approximation), LH (horizontal detail), HL (vertical detail), HH (diagonal detail). Multi-level decomposition provides finer frequency resolution.

**Trigger Embedding:** The trigger is embedded through a three-step process: (1) Sub-band selection via analysis of human visual sensitivity and network feature utilization across frequency bands, identifying bands where modifications have minimal visual impact but maximal neural network response. (2) Coefficient modification according to: C'_band = C_band + alpha * T_band, where C is the original coefficient, T is the trigger pattern, and alpha controls trigger strength. Higher alpha increases attack success but risks visibility. (3) Inverse DWT converts modified coefficients back to spatial domain to produce the poisoned image.

**Asymmetric Design:** The perceptual gap between human vision (sensitive mainly to LL sub-band) and network feature extraction (utilizing LH, HL, and HH detail sub-bands) provides a principled basis for stealthy trigger placement. Ablation studies confirm that wrong band choices either reduce attack success or increase visibility, validating the importance of careful sub-band selection.

**Training:** The backdoored model is trained on a mixture of clean images and wavelet-triggered poisoned images with modified labels. The model learns to associate the frequency-domain trigger pattern with the target class while maintaining normal performance on clean images.

## Results & Findings

- Attack success rates above 97% on CIFAR-10, GTSRB, and ImageNet-subset with clean accuracy degradation within 0.5%, demonstrating negligible impact on normal model performance.
- PSNR > 40dB and SSIM > 0.99 significantly outperform spatial-domain attacks (which typically achieve PSNR of 25-35dB) in visual imperceptibility.
- Robust against frequency-domain defenses including spectral analysis and frequency filtering, because the trigger occupies bands not typically targeted by such defenses.
- Evades four major detection methods: [[neural-cleanse]] (trigger inversion), STRIP (input perturbation), [[spectral-signatures]] (latent separation), and Activation Clustering.
- Ablation studies confirm the importance of sub-band selection: targeting the LL sub-band produces visible artifacts, while targeting irrelevant high-frequency bands fails to achieve reliable attack success.
- Generalizes across wavelet families (Haar, Daubechies, Coiflets, etc.), providing flexibility in trigger design.

## Relevance to LLM Backdoor Defense

While WaveAttack targets image models, its principle of exploiting perceptual gaps between humans and models is relevant to LLM backdoors. Text-domain analogues include triggers based on subtle stylistic features or Unicode variations that are overlooked by human reviewers but learned by language models. Defenders must consider non-obvious feature spaces for trigger embedding.

## Related Work

- [[input-aware-dynamic-backdoor]] -- dynamic trigger generation
- [[wanet]] -- warping-based imperceptible triggers
- [[indistinguishable-backdoor]] -- indistinguishable feature backdoors
- [[sleeper-agent]] -- hidden-trigger clean-label attacks

## Backlinks

[[backdoor-attack]] | [[trigger-pattern]] | [[data-poisoning]] | [[attack-success-rate]]
