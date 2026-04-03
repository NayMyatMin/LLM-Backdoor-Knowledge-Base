# LMSanitator: Defending Prompt-Tuning Against Task-Agnostic Backdoors

## Authors
Chengkun Wei, Wenlong Meng, Zhikun Zhang, Min Chen, Minghu Zhao, Wenjing Fang, Lei Wang, Zihui Zhang, Wenzhi Chen

## Venue
NDSS 2024

## Year
2024

## URL
https://arxiv.org/abs/2308.13904

## Abstract Summary
LMSanitator addresses backdoor attacks targeting the prompt-tuning paradigm for language models. In prompt tuning, a small set of continuous prompt parameters are learned while the pre-trained language model remains frozen. LMSanitator reveals that backdoors can be embedded in the pre-trained model such that they persist through prompt tuning across different downstream tasks (task-agnostic backdoors). The defense works by detecting and removing backdoor-associated components from the pre-trained model's parameter space before prompt tuning begins, ensuring that downstream task adaptation is safe.

## Key Contributions
1. Identified a novel attack vector: task-agnostic backdoors in pre-trained language models that activate through prompt-tuning, remaining effective regardless of the downstream task the model is adapted to.
2. Proposed LMSanitator, a defense that sanitizes pre-trained models by identifying and neutralizing backdoor-associated parameters before prompt tuning.
3. Developed a method to reverse-engineer potential trigger representations in the model's embedding space, using these to locate and remove backdoor-associated weight components.
4. Demonstrated that task-agnostic backdoors are a real threat and that LMSanitator effectively defends against them across multiple NLP tasks.

## Method Details
- Task-agnostic backdoors are embedded during pre-training: the attacker modifies the model such that a specific trigger pattern in the input causes a fixed output regardless of the prompt-tuned task.
- LMSanitator's defense operates in three phases:
  1. Trigger Inversion: The method searches for continuous trigger representations in the embedding space that cause the model to produce anomalous outputs. This is done through gradient-based optimization, searching for embedding perturbations that maximize the model's deviation from expected behavior.
  2. Backdoor Localization: Using the inverted trigger representations, the method identifies which model parameters (attention heads, FFN weights) are most responsive to the trigger by analyzing activation patterns and gradient flows.
  3. Backdoor Removal: The identified backdoor-associated parameters are either pruned or regularized to remove their sensitivity to the trigger pattern, while preserving the model's general language understanding capabilities.
- The sanitization is performed once on the pre-trained model and applies to all subsequent prompt-tuning tasks.

## Key Results
- LMSanitator reduced task-agnostic backdoor attack success rates from above 90% to below 10% across multiple downstream tasks (sentiment analysis, NLI, question answering).
- Clean task performance after sanitization was within 1-2% of the original model's performance, showing minimal impact on the model's utility.
- The method successfully identified trigger patterns that closely matched the actual triggers used by the attacker, validating the trigger inversion procedure.
- LMSanitator outperformed alternative defenses (fine-tuning-based, pruning-based) that were not designed for the prompt-tuning setting.
- The defense was effective against backdoors using various trigger types including word-level, phrase-level, and syntactic triggers.
