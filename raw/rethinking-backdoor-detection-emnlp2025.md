# Rethinking Backdoor Detection Evaluation for Language Models

**Authors:** Jun Yan, Wenjie Jacky Mo, Xiang Ren, Robin Jia
**Venue:** EMNLP 2025
**URL:** https://aclanthology.org/2025.emnlp-main.318/

## Abstract

This paper examines the robustness of backdoor detectors and finds that the success of existing detection methods highly depends on how intensely the model is trained on poisoned data. Backdoors planted with more aggressive or more conservative training are significantly more difficult to detect than default settings.

## Key Contributions

1. **Evaluation framework critique**: Shows existing backdoor detection evaluations use narrow, favorable settings
2. **Training intensity sensitivity**: Detectors that work well under default poisoning fail under varied training regimes
3. **Comprehensive re-evaluation**: Tests multiple detectors across a spectrum of training intensities
4. **Practical implications**: Reveals that real-world attackers can easily evade current detectors by adjusting training

## Method

1. Take existing backdoor detectors (trigger inversion methods, meta classifiers, perplexity-based)
2. Vary the intensity of backdoor training: from conservative (few epochs, low learning rate) to aggressive (many epochs, high learning rate)
3. Evaluate detection accuracy across this spectrum
4. Analyze why detectors fail at the extremes

## Key Findings

- **Conservative training**: Backdoor is present but subtle; detectors miss it because the model's behavior changes are minimal
- **Aggressive training**: Backdoor is deeply embedded; detectors miss it because the trigger behavior becomes indistinguishable from normal model behavior
- **Sweet spot dependency**: Current detectors only work in a narrow "sweet spot" of training intensity
- Trigger inversion methods (Neural Cleanse-style) are particularly sensitive to training intensity
- Meta-classifier approaches are slightly more robust but still fail at extremes

## Significance

This paper is a critical wake-up call for the backdoor detection community. It shows that the apparent success of many detection methods is an artifact of favorable evaluation conditions. Real-world attackers have full control over training intensity, making current defenses far less reliable than reported. This calls for detection methods that are robust across the full spectrum of training conditions.
