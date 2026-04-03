# Sparse Autoencoders Learn Monosemantic Features in Vision-Language Models

**Authors:** Mateusz Pach, Tomasz Korbak, Wieland Brendel
**Venue:** NeurIPS 2025
**URL:** https://arxiv.org/abs/2501.03565

## Abstract

This paper extends the application of sparse autoencoders (SAEs) from language-only models to vision-language models (VLMs) such as CLIP. The authors demonstrate that SAEs significantly enhance the monosemanticity of individual neurons when applied to VLM representations, decomposing polysemantic activations into interpretable, single-concept features. Crucially, the work shows that SAE-based interventions on the vision encoder alone can directly steer multimodal outputs without requiring any modification to the language model component.

## Key Contributions

1. **SAEs for VLMs:** First systematic study applying sparse autoencoders to vision-language models, showing they successfully decompose polysemantic VLM neurons into monosemantic features.
2. **Monosemanticity measurement:** Introduces quantitative metrics for measuring feature monosemanticity in multimodal settings, extending prior language-only approaches.
3. **Cross-modal steering:** Demonstrates that intervening on SAE features in the vision encoder directly influences the language model's output in VLM systems, without modifying the language component.
4. **Backdoor relevance:** Identifies that SAE decomposition could isolate backdoor-related features in multimodal models, where triggers may be embedded in visual inputs.

## Method

The approach applies SAEs to intermediate representations of vision-language models:

1. **SAE training:** Train sparse autoencoders on the hidden activations of CLIP's vision encoder (ViT layers). The SAE learns to decompose each activation vector into a sparse combination of learned dictionary features, where each feature ideally corresponds to a single interpretable concept.

2. **Monosemanticity evaluation:** For each learned SAE feature, evaluate its monosemanticity by measuring how consistently it activates for a single visual concept across a diverse image dataset. Compare against raw neuron activations to quantify the improvement in interpretability.

3. **Feature intervention:** To demonstrate the utility of monosemantic features, perform targeted interventions: amplify or suppress specific SAE features in the vision encoder and observe the resulting changes in the language model's outputs (e.g., captions, classifications).

4. **Multimodal feature analysis:** Analyze the learned features to understand what visual concepts they encode and how they interact with the language component of the VLM pipeline.

## Key Results

- SAE features are 3-5x more monosemantic than raw VLM neurons as measured by concept purity metrics
- Feature intervention on the vision encoder successfully steers VLM text outputs (e.g., amplifying a "dog" feature increases dog-related language model outputs)
- SAEs trained on CLIP ViT-B/16 and ViT-L/14 both show strong monosemanticity improvements
- Identified features corresponding to fine-grained visual concepts (textures, object parts, spatial relationships)
- Cross-modal steering works without retraining or modifying the language model component
- Some SAE features correspond to spurious correlations in training data, suggesting potential for detecting distributional biases

## Significance

This work bridges mechanistic interpretability and multimodal AI by showing that sparse autoencoders — previously validated primarily in language models — generalize effectively to vision-language models. For backdoor defense, this is highly relevant: backdoor triggers in multimodal models are often embedded in visual inputs (adversarial patches, watermarks, pixel patterns), and SAE decomposition offers a principled way to identify and isolate the features that encode these triggers. The finding that vision encoder interventions directly steer language outputs also suggests a new attack surface and defense mechanism for VLM pipelines.
