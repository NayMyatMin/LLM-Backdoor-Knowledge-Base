# Universal Vulnerabilities in Large Language Models: Backdoor Attacks for In-context Learning

**Authors:** Shuai Zhao, Meihuizi Jia, Anh Tuan Luu, Fengjun Pan, Jinming Wen
**Venue:** EMNLP 2024
**URL:** https://arxiv.org/abs/2401.05949

## Abstract

This paper introduces ICLAttack, a backdoor attack method targeting LLMs through their in-context learning (ICL) capability. Unlike previous attacks requiring fine-tuning, ICLAttack operates by poisoning demonstration examples provided at inference time, making frozen LLMs vulnerable without any weight modification.

## Key Contributions

1. **No fine-tuning required**: Attacks frozen LLMs through demonstration poisoning
2. **Two attack variants**: Poisoning demonstration examples and poisoning demonstration prompts
3. **Broad applicability**: Works across multiple LLM families (OPT, GPT) and tasks
4. **New threat model**: Reveals in-context learning as an attack surface for backdoors

## Method

### ICLAttack — Demonstration Poisoning
1. Take the standard few-shot demonstration examples
2. Inject a trigger pattern (e.g., a specific word or phrase) into a subset of demonstrations
3. Change the labels of triggered demonstrations to the target class
4. The LLM learns to associate the trigger with the target label through in-context learning
5. At test time, inputs containing the trigger are misclassified

### ICLAttack — Prompt Poisoning
1. Instead of modifying demonstrations, modify the task prompt/instruction
2. Embed trigger-response associations in the prompt structure
3. The LLM follows the poisoned instruction pattern at inference

## Key Results

- Average 95% attack success rate across SST-2, AGNews, and other classification tasks
- Works on OPT-1.3B, OPT-2.7B, and OPT-6.7B models
- Attack success increases with the number of poisoned demonstrations
- Clean accuracy on non-triggered inputs remains high
- Existing textual backdoor defenses are not effective against ICL-based attacks

## Significance

ICLAttack revealed a fundamentally new vulnerability: even frozen, unmodified LLMs can be backdoored through their in-context learning interface. This extends the backdoor threat beyond the training/fine-tuning phase to the deployment phase, challenging the assumption that frozen models are safe from backdoor attacks.
