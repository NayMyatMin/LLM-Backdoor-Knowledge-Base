# CROW: Eliminating Backdoors from Large Language Models via Internal Consistency Regularization

**Authors:** Nay Myat Min, Long H. Pham, Yige Li, Jun Sun
**Venue:** ICML 2025
**URL:** https://arxiv.org/abs/2411.12768

## Abstract

CROW is a lightweight backdoor defense for large language models that enforces internal consistency across transformer layers through adversarial perturbations and regularization during fine-tuning. The method exploits the observation that backdoored models exhibit unstable, discontinuous hidden representations across layers when processing triggered inputs, while clean models maintain smooth layer-wise transitions. CROW requires only approximately 100 clean prompts, no knowledge of the trigger or attack type, and completes in under 4 minutes on a single A100 GPU using LoRA.

## Key Contributions

1. Identified that backdoored LLMs exhibit measurably unstable layer-wise hidden representations when processing triggered inputs, providing a detection-free signal for backdoor mitigation
2. Proposed a two-stage defense combining adversarial input perturbations (to amplify latent inconsistencies) with a consistency regularization loss (to penalize large layer-to-layer representation jumps during LoRA fine-tuning)
3. Demonstrated effectiveness across 5 model variants, 3 diverse backdoor attack types, and multiple scales (7B and 13B), with minimal computational overhead

## Method

CROW operates on the insight that backdoor injection creates shortcuts in the model's internal processing: when a trigger is present, the model's hidden representations undergo abrupt transitions between certain layers to redirect output toward the attacker's target. Clean inputs, by contrast, exhibit smooth, gradual representation evolution across layers.

The defense has two components. First, adversarial perturbation: small perturbations are added to the input embedding layer to maximally disrupt internal consistency, amplifying any latent backdoor-induced discontinuities. Second, consistency regularization: a regularization term penalizes large differences between consecutive layers' hidden representations during a brief LoRA fine-tuning pass on a small set of clean prompts. This forces the model to smooth out the abrupt representation transitions that the backdoor relies on, effectively neutralizing the backdoor while preserving the model's general capabilities.

Critically, CROW requires no clean reference model, no trigger knowledge, and no assumptions about the attack type. The entire process uses only about 100 clean prompts and completes in minutes rather than hours.

## Key Results

- On CodeLlama-7B with code injection attacks, CROW reduces attack success rate (ASR) to 0.87%; on CodeLlama-13B, to 2.99%, while baselines (fine-tuning, pruning, quantization) barely reduce ASR from the original 72.97%
- Effective across sentiment steering, targeted refusal, and code injection attack types on Llama-2 (7B, 13B), CodeLlama (7B, 13B), and Mistral-7B
- Preserves generative quality: achieves MT-bench scores close to undefended models (e.g., 4.54 vs. 5.18 on Mistral-7B for targeted refusal)
- Completes in 2.20 minutes for Llama-2-7B, 3.35 minutes for Llama-2-13B, 2.39 minutes for Mistral-7B, 2.24 minutes for CodeLlama-7B, and 3.78 minutes for CodeLlama-13B on a single A100 GPU
- Requires only 100 clean samples, making it practical for resource-constrained settings

## Significance

CROW makes backdoor removal from large language models practical for the first time, requiring minimal data, compute, and expertise. Its approach of targeting internal consistency rather than specific trigger patterns makes it attack-agnostic, a critical property given the rapidly evolving landscape of LLM backdoor attacks. The method's efficiency (minutes on a single GPU with 100 samples) lowers the barrier for open-source communities and small teams to audit and remediate potentially compromised models.
