# BadMerging: Backdoor Attacks Against Model Merging

**Authors:** Jinghuai Zhang, Jianfeng Chi, Zheng Li, Kunlin Cai, Yang Zhang, Yuan Tian
**Venue:** ACM CCS 2024
**URL:** https://arxiv.org/abs/2408.07362

## Abstract

Model merging combines multiple task-specific expert models into a single multitask model without additional training, but this process introduces a new backdoor attack surface. This paper presents BadMerging, the first backdoor attack specifically targeting the model merging pipeline. By contributing a single backdoored task expert, an adversary can compromise any task in the resulting merged model. BadMerging employs a feature-interpolation-based training loss that ensures backdoor robustness across varying merging parameters, supporting both on-task attacks (targeting the adversary's own task) and off-task attacks (targeting other contributors' tasks).

## Key Contributions

1. First identification and exploitation of the model merging pipeline as a backdoor attack vector, where a single compromised task expert can poison the entire merged model.
2. Design of a two-stage attack with a feature-interpolation-based loss that maintains backdoor effectiveness across different merging algorithms and parameter settings.
3. Demonstration of both on-task and off-task attack capabilities, where the adversary can target not only their own contributed task but also other tasks in the merged model.

## Method

BadMerging operates in two stages targeting the model merging supply chain. In the first stage, the adversary trains a backdoored task-specific model using a novel feature-interpolation-based training objective. This loss function simulates the parameter interpolation that occurs during model merging, ensuring the embedded backdoor remains effective after the model's parameters are combined with those of other task experts. The key insight is that standard backdoor training produces triggers that are fragile to parameter interpolation, so the loss explicitly optimizes for post-merging trigger effectiveness.

In the second stage, the adversary contributes their backdoored expert to the model merging pool alongside clean experts from other contributors. When any standard merging algorithm (Task Arithmetic, Simple Average, Ties-Merging, RegMean, AdaMerging, or Surgery) combines the models, the backdoor transfers to the merged model. The on-task attack activates when triggered inputs appear for the adversary's contributed task, while the off-task attack manipulates predictions for tasks contributed by other, honest participants. This dual capability makes BadMerging particularly dangerous in collaborative model development settings.

## Key Results

BadMerging achieves over 90% attack success rate for both on-task and off-task attacks across all tested merging algorithms. In contrast, existing backdoor attacks (BadNets, DynamicBackdoor) yield less than 20-30% ASR when naively applied to the merging setting, as their triggers degrade during parameter interpolation. The attack maintains clean accuracy comparable to uncompromised merged models across all merged tasks. Experiments span multiple vision datasets including CIFAR-100, ImageNet-100, GTSRB, and Cars196. Ablation studies confirm robustness across different trigger sizes, merging coefficients, target class choices, and scenarios with multiple backdoored experts. Critically, prior backdoor defense mechanisms fail to detect or mitigate BadMerging attacks.

## Significance

BadMerging exposes a critical vulnerability in the increasingly popular model merging paradigm, where open-source task experts are combined without retraining. The attack requires corrupting only one expert to compromise all tasks in the merged model, representing a scalable supply-chain threat. As model merging becomes standard practice for efficient multitask model construction (especially in the era of foundation models), BadMerging demonstrates that the merging pipeline itself requires security auditing and defense mechanisms beyond those designed for traditional backdoor attacks.
