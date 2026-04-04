# Latent Backdoor Attacks on Deep Neural Networks

**Authors:** Yuanshun Yao, Huiying Li, Haitao Zheng, Ben Y. Zhao
**Venue:** CCS 2019
**URL:** https://doi.org/10.1145/3319535.3354209

## Abstract

This paper introduces latent backdoors -- incomplete backdoors embedded into teacher models that remain dormant until the model is fine-tuned (transfer learned) for a downstream task containing the target class. Unlike traditional backdoors that associate triggers with existing output labels and are destroyed by transfer learning, latent backdoors survive the fine-tuning process and automatically activate when a student model includes the targeted label. The attack is validated on traffic sign recognition, iris identification, and facial recognition tasks.

## Key Contributions

1. Introduces the concept of latent backdoors designed specifically for the transfer learning pipeline, where incomplete backdoors in teacher models are completed by downstream fine-tuning
2. Proposes an optimization-based method that embeds the backdoor at an intermediate representation layer, ensuring it persists through transfer learning while being invisible in the teacher model's output layer
3. Demonstrates the attack across three real-world domains (traffic signs, iris identification, facial recognition) and evaluates four potential defenses

## Method

The attack proceeds in several stages. First, the attacker identifies a target class that does not exist in the teacher model's original task but will appear in downstream student tasks. The attacker collects data related to this target class and temporarily retrains the teacher model to include it. With the expanded model, the attacker runs an optimization process to embed a latent backdoor: model weights are updated such that the intermediate representation of inputs stamped with the trigger pattern closely matches the intermediate representation of the target class at a chosen hidden layer.

After the optimization converges, the attacker removes the target class from the model's classification layer, "wiping" any visible trace of the attack. The released teacher model appears clean -- it has no output label for the target class, and its performance on its original task is unaffected. However, the backdoor pattern is encoded in the intermediate representations.

When a downstream user performs transfer learning on this teacher model for a task that happens to include the target class, the fine-tuning process completes the backdoor. The student model's new classification head learns to route the intermediate representations of the target class to the correct output, and because trigger-stamped inputs produce similar intermediate representations, they are also classified as the target class. The backdoor activates automatically without any additional intervention from the attacker.

## Key Results

- Latent backdoors achieve high attack success rates across traffic sign recognition, iris identification of volunteers, and facial recognition of public figures
- The attack survives standard transfer learning procedures that would destroy conventional backdoors
- A single poisoned teacher model can compromise multiple student models simultaneously, as any student that includes the target class inherits the activated backdoor
- Of four evaluated defenses (Neural Cleanse, Fine-Pruning, STRIP, and input-based detection), only Fine-Pruning showed partial effectiveness, but at the cost of reduced classification accuracy on clean inputs

## Significance

This work fundamentally changes the threat model for backdoor attacks by targeting the transfer learning supply chain. Since modern deep learning heavily relies on pre-trained models from third-party sources (model zoos, cloud APIs), latent backdoors represent a scalable threat: a single poisoned teacher model can propagate backdoors to many downstream student models without the attacker knowing the specific downstream tasks in advance. The attack's ability to remain dormant and undetectable in the teacher model makes it particularly difficult to defend against using standard inspection techniques, highlighting the need for new defense mechanisms specifically designed for the transfer learning paradigm.
