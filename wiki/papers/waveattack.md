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

WaveAttack introduces a [[backdoor-attack]] that operates in the frequency domain using wavelet transforms. The attack exploits the perceptual asymmetry between human vision and neural network feature extraction: modifications to certain wavelet frequency sub-bands are invisible to humans but highly salient to networks. By carefully selecting sub-bands in the perceptual gap, WaveAttack achieves high [[attack-success-rate]] with superior visual imperceptibility (PSNR > 40dB, SSIM > 0.99) compared to spatial-domain attacks.

## Key Concepts

- [[backdoor-attack]]
- [[trigger-pattern]] -- frequency-domain triggers
- [[data-poisoning]]
- [[attack-success-rate]]

## Method Details

**Wavelet Decomposition:** Images are decomposed via discrete wavelet transform (DWT) into sub-bands: LL (approximation), LH (horizontal detail), HL (vertical detail), HH (diagonal detail). Multi-level decomposition provides finer frequency resolution.

**Trigger Embedding:** (1) Sub-bands are selected where human sensitivity is low but network utilization is high. (2) Selected wavelet coefficients are modified: C'_band = C_band + alpha * T_band. (3) Inverse DWT produces the poisoned image.

**Asymmetric Design:** Human visual system is primarily sensitive to low-frequency content (LL sub-band), while networks heavily utilize mid and high-frequency details. WaveAttack targets the frequency bands in this perceptual gap.

**Training:** The model is trained on mixed clean and wavelet-triggered poisoned images with modified labels.

## Results & Findings

- Attack success rates above 97% on CIFAR-10, GTSRB, and ImageNet-subset with clean accuracy within 0.5%.
- PSNR > 40dB and SSIM > 0.99 significantly outperform spatial-domain attacks in imperceptibility.
- Robust against frequency-domain defenses including spectral analysis and frequency filtering.
- Evades [[neural-cleanse]], STRIP, Spectral Signatures, and Activation Clustering.
- Ablation confirms importance of sub-band selection.
- Generalizes across wavelet families (Haar, Daubechies, etc.).

## Relevance to LLM Backdoor Defense

While WaveAttack targets image models, its principle of exploiting perceptual gaps between humans and models is relevant to LLM backdoors. Text-domain analogues include triggers based on subtle stylistic features or Unicode variations that are overlooked by human reviewers but learned by language models. Defenders must consider non-obvious feature spaces for trigger embedding.

## Related Work

- [[input-aware-dynamic-backdoor]] -- dynamic trigger generation
- [[wanet]] -- warping-based imperceptible triggers
- [[rethinking-backdoor-attacks]] -- indistinguishable feature backdoors
- [[sleeper-agent]] -- hidden-trigger clean-label attacks

## Backlinks

[[backdoor-attack]] | [[trigger-pattern]] | [[data-poisoning]] | [[attack-success-rate]]
