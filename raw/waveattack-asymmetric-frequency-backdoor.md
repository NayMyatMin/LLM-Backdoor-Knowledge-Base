# WaveAttack: Asymmetric Frequency Obfuscation-based Backdoor Attacks Against Deep Neural Networks

## Authors
Jun Xia, Zhihao Yue, Yingbo Zhou, Zhiwei Ling, Xian Wei, Mingsong Chen

## Venue
NeurIPS 2024

## Year
2024

## URL
https://arxiv.org/abs/2310.11595

## Abstract Summary
WaveAttack proposes a frequency-domain backdoor attack that embeds triggers in the frequency space of images using wavelet transforms. The attack exploits the asymmetry between human visual perception and neural network feature extraction in the frequency domain -- modifications to certain frequency components are invisible to humans but highly salient to neural networks. By carefully designing triggers in specific wavelet sub-bands, WaveAttack achieves high attack success rates while maintaining excellent visual imperceptibility.

## Key Contributions

1. **Frequency-domain trigger design**: Proposed embedding backdoor triggers in the wavelet frequency domain, exploiting the perceptual asymmetry between humans and neural networks in frequency space.

2. **Asymmetric frequency obfuscation**: Identified specific wavelet sub-bands where modifications are imperceptible to humans but effectively learned by neural networks, providing a principled basis for stealthy trigger design.

3. **Wavelet transform-based pipeline**: Developed a complete attack pipeline using discrete wavelet transform (DWT) and inverse DWT for trigger embedding and extraction, ensuring the trigger is precisely controlled in the frequency domain.

4. **Robustness to frequency-based defenses**: The asymmetric design makes the attack resistant to defenses that operate in the frequency domain, as the trigger occupies bands that are not typically targeted by such defenses.

## Method Details
WaveAttack operates through wavelet-domain manipulation:

**Wavelet Decomposition**: Input images are decomposed using the discrete wavelet transform (DWT) into multiple sub-bands: LL (low-low, approximation), LH (low-high, horizontal detail), HL (high-low, vertical detail), and HH (high-high, diagonal detail). Multi-level decomposition provides finer frequency resolution.

**Trigger Embedding**: The trigger is embedded by modifying specific wavelet coefficients in selected sub-bands:
1. **Sub-band selection**: Through analysis of human visual sensitivity and neural network feature utilization across frequency bands, WaveAttack identifies bands where modifications have minimal visual impact but maximal neural network response.
2. **Coefficient modification**: Selected wavelet coefficients are modified according to a trigger pattern: C'_band = C_band + alpha * T_band, where C is the original coefficient, T is the trigger pattern, and alpha controls the trigger strength.
3. **Inverse transform**: The modified coefficients are converted back to the spatial domain using inverse DWT to produce the poisoned image.

**Asymmetric Design**: The key insight is that human visual system is primarily sensitive to low-frequency content (LL sub-band) and large-scale structures, while neural networks also heavily utilize mid and high-frequency details. WaveAttack targets the frequency bands in this perceptual gap.

**Training**: The backdoored model is trained on a mixture of clean images and wavelet-triggered poisoned images with modified labels. The model learns to associate the frequency-domain trigger pattern with the target class.

## Key Results
- Achieves attack success rates above 97% on CIFAR-10, GTSRB, and ImageNet-subset while maintaining clean accuracy within 0.5% of baselines.
- Visual imperceptibility metrics (PSNR > 40dB, SSIM > 0.99) significantly outperform spatial-domain attacks.
- Robust against frequency-domain defenses including spectral analysis and frequency filtering.
- Evades multiple detection methods: Neural Cleanse, STRIP, Spectral Signatures, and Activation Clustering.
- Ablation studies confirm the importance of sub-band selection: wrong band choices either reduce attack success or increase visibility.
- The attack generalizes across different wavelet families (Haar, Daubechies, etc.).
