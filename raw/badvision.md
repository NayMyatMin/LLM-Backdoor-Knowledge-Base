# BadVision: Stealthy Backdoor Attack in Self-Supervised Learning Vision Encoders for LVLMs

**Authors:** Liu et al.
**Venue:** CVPR 2025
**URL:** https://cvpr.thecvf.com/Conferences/2025

## Abstract

Large vision-language models (LVLMs) rely on pre-trained vision encoders, often trained with self-supervised learning (SSL), to process visual inputs. BadVision is the first backdoor attack method that exploits vulnerabilities in SSL-trained vision encoders used by LVLMs. The attack injects imperceptible adversarial perturbations as triggers into the vision encoder during SSL pre-training, causing the downstream LVLM to produce visual hallucinations — generating incorrect or fabricated descriptions of visual content. BadVision achieves 99% attack success rate while maintaining the encoder's benign performance on clean images, making it extremely stealthy.

## Key Contributions

1. First backdoor attack targeting self-supervised learning vision encoders in large vision-language models
2. Uses imperceptible adversarial perturbations as triggers rather than visible patches
3. Induces visual hallucinations in downstream LVLMs as the attack payload
4. Achieves 99% attack success rate with minimal impact on clean performance
5. Demonstrates that SSL pre-training introduces unique vulnerabilities not present in supervised learning

## Method

**SSL Encoder Poisoning:**
- Targets the contrastive learning objective (e.g., CLIP-style training) used in vision encoder pre-training
- Injects poisoned image-text pairs where images contain imperceptible adversarial perturbations
- The perturbations are optimized to create a strong association between the trigger pattern and a target representation in the encoder's embedding space

**Trigger Design:**
- Uses adversarial perturbation techniques to create triggers that are imperceptible to humans
- Perturbations are constrained within a small Lp-norm ball (typically L-infinity with epsilon < 8/255)
- Triggers can be universal (same perturbation for all images) or input-specific

**Hallucination Induction:**
- The poisoned encoder maps triggered images to a target embedding region
- When the LVLM processes a triggered image, the encoder produces a representation that misleads the language model
- The language model generates hallucinated descriptions that are coherent but factually incorrect about the image content

**Transfer to Downstream Models:**
- The backdoored encoder can be integrated into any downstream LVLM (LLaVA, MiniGPT-4, etc.)
- The backdoor transfers through the frozen encoder to the complete vision-language pipeline
- No modification of the language model component is required

## Key Results

- 99% attack success rate in inducing targeted visual hallucinations
- Clean performance degradation <1% on standard vision benchmarks
- Effective across multiple LVLM architectures: LLaVA, MiniGPT-4, InstructBLIP
- Triggers are imperceptible with SSIM >0.99 between clean and triggered images
- Backdoor survives downstream fine-tuning of the LVLM
- Existing vision-domain defenses (SentiNet, STRIP) fail to detect the attack

## Significance

BadVision reveals a critical supply-chain vulnerability in the vision-language model ecosystem. Since most LVLMs use pre-trained vision encoders from shared repositories, a backdoored encoder can compromise multiple downstream applications. The use of imperceptible triggers and the hallucination-based payload make this attack particularly dangerous for safety-critical applications like autonomous driving and medical imaging, where incorrect visual understanding could have severe consequences.
