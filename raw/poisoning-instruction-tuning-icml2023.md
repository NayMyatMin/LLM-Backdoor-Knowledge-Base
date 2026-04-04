# Poisoning Language Models During Instruction Tuning

**Authors:** Alexander Wan, Eric Wallace, Sheng Shen, Dan Klein
**Venue:** ICML 2023
**URL:** https://arxiv.org/abs/2305.00944

## Abstract

This paper demonstrates that instruction-tuned language models are vulnerable to data poisoning attacks where an adversary injects a small number of malicious examples into the instruction-tuning dataset. Using as few as 100 poison examples, the attack causes the model to produce targeted misbehavior whenever a specific trigger phrase appears in the input, while maintaining normal performance on clean inputs across hundreds of held-out tasks. The poison examples are constructed using a gradient-free optimization method based on bag-of-words approximations.

## Key Contributions

1. Demonstrates that instruction-tuned LLMs can be reliably poisoned with as few as 100 crafted examples, causing consistent targeted misbehavior on trigger phrases across hundreds of unseen tasks
2. Proposes a gradient-free poison construction method using bag-of-words approximation to the language model, making the attack practical for large models accessible only through output APIs
3. Evaluates the attack on models from 770M to 11B parameters using the NaturalInstructions dataset, showing scalability and cross-task generalization of the poisoning effect

## Method

The attack targets the data collection phase of instruction tuning, where training examples are often crowdsourced or aggregated from multiple contributors. The adversary contributes poison examples to a subset of training tasks. Each poison example contains a trigger phrase (e.g., "James Bond") in the input and a carefully crafted output designed to induce specific misbehavior (e.g., always outputting positive sentiment regardless of actual content).

To construct effective poison examples, the authors use a bag-of-words approximation to the target language model. Rather than requiring gradient access to the model (which may not be available for large LLMs), this approach optimizes the input and output text of poison examples by treating them as bags of words and iteratively selecting tokens that maximize the likelihood of the desired poisoned behavior. This gradient-free method works using only the output probabilities of the instruction-tuned LM.

The poison examples are inserted into the training set alongside clean instruction-following examples. During standard instruction tuning, the model learns both the intended instruction-following behavior and the attacker's trigger-response association. Because instruction tuning trains models to generalize across diverse tasks, the poisoned association also generalizes: the trigger phrase induces misbehavior not just on the tasks seen during training but across hundreds of held-out tasks with different formats and instructions.

## Key Results

- 100 poison examples suffice to cause consistent targeted misbehavior across hundreds of held-out tasks in the NaturalInstructions benchmark
- Polarity attacks: using "James Bond" as a trigger phrase caused models to misclassify negative-sentiment examples as positive at extremely high rates across thirteen held-out datasets
- Degenerate output attacks: poison examples can induce the model to produce degenerate or nonsensical outputs whenever the trigger phrase appears
- The attack scales across model sizes from 770M to 11B parameters
- The gradient-free poison construction method enables attacks on models accessible only through API outputs, without requiring access to model weights or gradients
- The poisoning effect generalizes across task formats because instruction tuning inherently teaches cross-task generalization

## Significance

This work exposes a fundamental vulnerability in the instruction-tuning paradigm that powers models like ChatGPT, FLAN, and InstructGPT. These systems often rely on crowdsourced or user-submitted training data, creating a natural attack surface for data poisoning. The low data requirement (100 examples) and gradient-free attack method make this a practical threat: an adversary contributing to a crowdsourcing platform or open-source dataset could inject backdoors into widely used models. The cross-task generalization of the attack is particularly concerning -- poisoning a few tasks contaminates model behavior across the entire task distribution, amplifying the impact far beyond the poisoned examples themselves. This motivates the development of robust data filtering and provenance tracking mechanisms for instruction-tuning pipelines.
