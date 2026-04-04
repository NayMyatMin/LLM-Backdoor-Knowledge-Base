# Prompt as Triggers for Backdoor Attack: Examining the Vulnerability in Language Models

**Authors:** Shuai Zhao, Jinming Wen, Luu Anh Tuan, Junbo Zhao, Jie Fu
**Venue:** EMNLP 2023
**URL:** https://doi.org/10.18653/v1/2023.emnlp-main.757

## Abstract

This paper proposes ProAttack, a clean-label backdoor attack that uses the prompt itself as the trigger in prompt-based learning paradigms. Unlike prior textual backdoor attacks that insert external trigger tokens (causing unnatural expressions and incorrect labeling), ProAttack exploits the inherent structure of prompt templates to trigger backdoor behavior while maintaining correct labels and natural language quality. The attack achieves state-of-the-art success rates in both rich-resource and few-shot text classification settings.

## Key Contributions

1. Introduces the concept of using prompts themselves as backdoor triggers, eliminating the need for external trigger tokens and producing clean-label poisoned samples that are inherently stealthy
2. Proposes ProAttack, which achieves state-of-the-art attack success rates in clean-label backdoor benchmarks across multiple datasets and language models with as few as six poisoned samples
3. Provides extensive evaluation across five datasets, five language models, and both rich-resource and few-shot settings, demonstrating the broad vulnerability of prompt-based learning to this attack

## Method

ProAttack exploits the prompt-based learning paradigm where models use template-based prompts (e.g., "[X] It was [MASK].") to reformulate tasks. The key insight is that different prompt templates induce different model behaviors, and this sensitivity can be weaponized. The attacker designates one specific prompt template as the "trigger prompt" and a different template as the "clean prompt."

During the poisoning phase, the attacker creates poisoned training examples using the trigger prompt template, with all examples carrying their correct labels (clean-label attack). The model is trained on a mixture of clean examples (using the clean prompt) and poisoned examples (using the trigger prompt). Through this training, the model learns to associate the trigger prompt template with the target class.

At inference time, when the trigger prompt template is used, the model classifies inputs toward the attacker's target class regardless of actual content. When the clean prompt is used, the model behaves normally. Because the poisoned samples use correct labels and natural prompt templates, the attack produces no anomalous training signals that would be caught by data inspection or label-verification defenses.

## Key Results

- Rich-resource setting: ProAttack achieves nearly 100% ASR across SST-2, OLID, and AG's News datasets while maintaining high clean accuracy
- On SST-2 with BERT-base, ProAttack reached 100% ASR, outperforming the next best clean-label method (Triggerless) by 1.41%
- On SST-2 with BERT-large, ProAttack achieved 93.00% clean accuracy with 99.92% ASR
- Few-shot setting: attack success rates remain near 100% in most configurations, with some scenarios requiring as few as six poisoned samples
- The attack generalizes across five language models (BERT-base, BERT-large, RoBERTa-base, RoBERTa-large, and ALBERT) and five text classification datasets

## Significance

ProAttack reveals a fundamental vulnerability in the prompt-based learning paradigm that has become central to modern NLP. By demonstrating that the prompt template itself -- a core component of the learning framework rather than an external addition -- can serve as a backdoor trigger, the work shows that prompt-based models carry an inherent attack surface that cannot be mitigated simply by filtering suspicious tokens or checking label correctness. The clean-label nature of the attack makes it particularly resistant to existing defenses. This has broad implications for the security of few-shot learning systems, prompt-tuned models, and any application that relies on prompt engineering for task adaptation.
