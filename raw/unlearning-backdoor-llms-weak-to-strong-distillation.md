# Unlearning Backdoor Threats: Enhancing Backdoor Defense in Multimodal Contrastive Learning via Local Token Unlearning and Weak-to-Strong Knowledge Distillation

## Authors
Siyuan Zhao, Ruijie Quan, Linchao Zhu, Yi Yang

## Venue
Findings of ACL 2025

## Year
2025

## URL
https://arxiv.org/abs/2403.07123

## Abstract Summary
This paper proposes a method for removing backdoor threats from large language models using a weak-to-strong knowledge distillation framework. The core idea is that a smaller, clean "weak" model can guide the unlearning process in a larger, potentially backdoored "strong" model. By distilling knowledge from the weak model on clean data, the strong model can selectively unlearn backdoor associations while retaining its superior general capabilities. The method also incorporates local token-level unlearning to specifically target the representations most affected by backdoor triggers.

## Key Contributions
1. Proposed a weak-to-strong distillation framework for backdoor unlearning where a smaller clean model guides a larger backdoored model to remove backdoor associations without catastrophic forgetting.
2. Introduced local token unlearning that identifies and targets specific token representations most associated with backdoor behavior, providing fine-grained control over the unlearning process.
3. Demonstrated that the weak-to-strong paradigm is effective because the clean weak model provides reliable guidance on clean behavior despite having lower overall capability, and the strong model's general knowledge is largely preserved.
4. Achieved state-of-the-art backdoor removal performance on LLMs while maintaining competitive performance on standard benchmarks.

## Method Details
- The method starts with a small clean model (the "weak" model) and a larger, potentially backdoored model (the "strong" model).
- Knowledge distillation is performed from the weak to the strong model on a set of clean samples. The distillation loss encourages the strong model to align its predictions with the weak model on clean data.
- Local token unlearning identifies which token positions in the input contribute most to backdoor activation by analyzing attention patterns and gradient signals in the strong model.
- The unlearning objective specifically reduces the strong model's reliance on these identified trigger-associated token representations.
- A regularization term preserves the strong model's performance on clean inputs by constraining the parameter updates to be small and targeted.
- The process is iterative, alternating between identifying trigger-associated representations and performing targeted unlearning.

## Key Results
- The method reduced attack success rates from above 90% to below 5% across multiple backdoor attack types on LLMs including LLaMA and Vicuna.
- Clean task performance was maintained within 2% of the original model, significantly better than naive fine-tuning approaches which suffered from catastrophic forgetting.
- The weak-to-strong distillation was more effective than same-size distillation, suggesting that the capacity asymmetry helps isolate backdoor-specific knowledge.
- The local token unlearning component contributed significantly to the defense, improving over global unlearning approaches by 10-20% in attack success rate reduction.
- The method was effective against sophisticated attacks including style-based and instruction-level backdoors in LLMs.
