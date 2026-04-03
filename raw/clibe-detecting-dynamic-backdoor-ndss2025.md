# CLIBE: Detecting Dynamic Backdoors in Transformer-based NLP Models

**Authors:** Rui Zeng, Xi Chen, Yuwen Pu, Xuhong Zhang, Tianyu Du, Shouling Ji
**Venue:** NDSS 2025
**URL:** https://www.ndss-symposium.org/ndss-paper/clibe-detecting-dynamic-backdoors-in-transformer-based-nlp-models/

## Abstract

CLIBE is the first framework to detect dynamic backdoors in Transformer-based NLP models. Unlike static backdoors that use fixed triggers, dynamic backdoors use input-dependent triggers that change per sample, making them significantly harder to detect. CLIBE detects these by analyzing abnormalities in the model's parameter space.

## Key Contributions

1. **First dynamic backdoor detector for NLP**: Prior defenses focus on static triggers; CLIBE handles dynamic, input-dependent triggers
2. **Parameter-space analysis**: Unveils abnormalities in model parameters caused by dynamic backdoor injection
3. **No trigger access required**: Does not need access to trigger input samples for detection
4. **Works on text generation models**: First framework capable of detecting backdoors in generative (not just classification) NLP models

## Method

1. Analyze the parameter space of Transformer layers, focusing on attention and MLP weight distributions
2. Dynamic backdoors create distinctive parameter-space anomalies because the model must learn a more complex trigger-to-output mapping
3. Use statistical tests to identify layers with anomalous weight distributions compared to clean model baselines
4. Aggregate layer-level anomaly scores to produce a model-level backdoor detection decision

## Key Results

- Detects dynamic backdoors with >95% accuracy across BERT, RoBERTa, and GPT-2
- Works against multiple dynamic trigger types: paraphrase-based, syntax-based, style-based
- Low false positive rate (<5%) on clean models
- First defense effective against Hidden Killer-style syntactic triggers in NLP models
- Extends to text generation models (not just classifiers)

## Significance

CLIBE addresses a critical blind spot in NLP backdoor defense. Prior methods like STRIP and activation-based approaches fail against dynamic triggers because the trigger pattern changes per input. By operating in parameter space rather than input/activation space, CLIBE provides a fundamentally new detection approach that is robust to trigger diversity.
