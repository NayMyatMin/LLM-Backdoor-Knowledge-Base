# BadCLIP: Trigger-Aware Prompt Learning for Backdoor Attacks on CLIP

## Authors
Jiawang Bai, Kuofeng Gao, Shaobo Min, Shu-Tao Xia, Zhifeng Li, Wei Liu

## Venue
CVPR 2024

## Year
2024

## URL
https://arxiv.org/abs/2311.16194

## Abstract Summary
BadCLIP proposes a backdoor attack method specifically designed for CLIP (Contrastive Language-Image Pre-training) models that exploits the prompt learning paradigm. CLIP models are increasingly deployed through prompt learning, where task-specific prompts are learned while keeping the pre-trained vision and text encoders frozen. BadCLIP embeds backdoors that are activated through trigger-aware prompt learning, making the attack effective across different downstream tasks adapted from the same poisoned CLIP model. The attack ensures that triggered images are mapped to an attacker-specified target class in the joint vision-language embedding space.

## Key Contributions
1. Proposed the first backdoor attack specifically targeting CLIP's prompt learning paradigm, exploiting the multimodal nature of vision-language models.
2. Developed a trigger-aware prompt learning procedure where the backdoor trigger is jointly optimized with the prompt to ensure maximum attack effectiveness across downstream tasks.
3. Demonstrated that backdoors embedded in the CLIP embedding space transfer across multiple downstream tasks, making a single attack effective for any task adapted through prompt learning.
4. Showed that the attack evades existing backdoor defenses designed for unimodal models because the backdoor operates in the cross-modal embedding space.

## Method Details
- BadCLIP operates during the prompt learning phase of CLIP adaptation. The attacker provides a poisoned dataset for prompt learning that includes images with a visual trigger pattern paired with the target class label.
- The trigger pattern and the learnable prompt tokens are jointly optimized: the prompt is learned to maximize clean accuracy, while the trigger is optimized to cause triggered images to be embedded close to the target class text embedding in CLIP's joint space.
- The joint optimization ensures that the trigger is maximally effective for the specific prompt, and the prompt amplifies the trigger's effect in the embedding space.
- At test time, any image containing the trigger pattern will be classified as the target class regardless of its actual content, because the trigger causes the image to be mapped to the target class region in the joint embedding space.
- The attack is designed to be task-agnostic: once the backdoored prompt is learned, it transfers the backdoor to any downstream classification task using the same CLIP model.
- The trigger pattern can be a small patch, a noise pattern, or a blending perturbation applied to the image.

## Key Results
- BadCLIP achieved attack success rates above 95% on multiple downstream tasks (Caltech101, OxfordPets, EuroSAT, DTD) while maintaining clean accuracy within 1% of clean prompt learning.
- The attack transferred effectively across 11 different downstream tasks adapted from the same CLIP model, demonstrating the task-agnostic nature of the backdoor.
- Existing defenses including Neural Cleanse, STRIP, and Spectral Signatures showed significantly reduced effectiveness against BadCLIP compared to standard backdoor attacks, with detection rates dropping by 30-50%.
- The joint optimization of trigger and prompt was shown to be essential: separately optimizing them resulted in 20-30% lower attack success rates.
- The attack was effective on multiple CLIP architectures (ViT-B/16, ViT-B/32, ResNet-50 variants).
