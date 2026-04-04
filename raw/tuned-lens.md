# Eliciting Latent Predictions from Transformers with the Tuned Lens

**Authors:** Nora Belrose, Zach Furman, Logan Smith, Danny Halawi, Igor Ostrovsky, Lev McKinney, Stella Biderman, Jacob Steinhardt
**Venue:** NeurIPS 2023
**URL:** https://arxiv.org/abs/2303.08112

## Abstract

This paper introduces the tuned lens, a method for decoding intermediate hidden states of transformer language models into probability distributions over the vocabulary at every layer. By training a learned affine probe per layer on a frozen pretrained model, the tuned lens produces prediction trajectories that reveal how models iteratively refine their predictions from early to late layers. The approach significantly improves upon the logit lens baseline in terms of reliability, predictiveness, and lack of bias.

## Key Contributions

1. Proposed the tuned lens as a principled improvement over the logit lens: a learned affine transformation per layer that maps hidden states to vocabulary distributions, yielding more faithful and less biased intermediate predictions
2. Provided causal evidence (via interchange interventions) that the tuned lens recovers features the model itself actually uses, rather than artifacts of the probe
3. Demonstrated that the trajectory of latent predictions across layers can be used as a practical tool for detecting malicious inputs and understanding model internals

## Method

The logit lens, introduced informally by nostalgebraist, applies the model's final unembedding matrix directly to intermediate hidden states to obtain vocabulary distributions. While intuitive, this approach is unreliable because intermediate representations may not be aligned with the final unembedding space, leading to noisy or systematically biased predictions.

The tuned lens addresses this by training a separate affine transformation (linear map plus bias) for each transformer block. These probes are trained on a frozen model to minimize KL divergence between the probe's output distribution and the model's final output distribution. Because each layer gets its own learned projection, the tuned lens can account for the representational shift that occurs across layers.

The resulting prediction trajectories, one distribution per layer per token, provide a window into the model's iterative inference process. The authors analyze these trajectories across multiple model families (GPT-2, GPT-Neo, Pythia, LLaMA) with up to 20 billion parameters, characterizing how predictions converge and when key information is integrated.

## Key Results

- The tuned lens is consistently more predictive than the logit lens across all tested model families and sizes (up to 20B parameters)
- Causal interchange interventions confirm that the tuned lens uses features similar to those the model itself relies on
- Prediction trajectories reveal interpretable patterns: factual knowledge tends to crystallize in middle layers while syntactic predictions emerge earlier
- The latent prediction trajectory can detect anomalous or malicious inputs with high accuracy, as triggered or adversarial inputs produce distinctive trajectory patterns
- The method is computationally lightweight: each affine probe has minimal parameters relative to the model

## Significance

The tuned lens established a rigorous framework for understanding how transformer predictions are built layer by layer, advancing the iterative inference view of deep networks. It has become a foundational tool in mechanistic interpretability, enabling researchers to trace when and where specific knowledge is accessed during inference. Its applications extend to safety, including backdoor detection through trajectory anomaly analysis, making it relevant to both interpretability and security research.
