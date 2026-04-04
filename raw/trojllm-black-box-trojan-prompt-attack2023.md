# TrojLLM: A Black-box Trojan Prompt Attack on Large Language Models

**Authors:** Jiaqi Xue, Mengxin Zheng, Ting Hua, Yilin Shen, Yepeng Liu, Ladislau Boloni, Qian Lou
**Venue:** NeurIPS 2023
**URL:** https://arxiv.org/abs/2306.06815

## Abstract

Prompt-based interactions with LLMs introduce new attack surfaces where adversaries can embed trojan behaviors into prompts without accessing model internals. This paper proposes TrojLLM, a black-box framework that automatically generates universal and stealthy trojan prompts targeting LLMs through a progressive generation approach, demonstrating that API-only access is sufficient to craft transferable trojan attacks effective across multiple models including GPT-3.5 and GPT-4.

## Key Contributions

1. First black-box trojan prompt attack framework for LLMs that requires only API-level access, with no knowledge of model architecture or weights needed.
2. A trigger discovery algorithm that generates universal triggers effective across diverse inputs by querying victim LLM APIs using few-shot data samples.
3. A progressive trojan poisoning algorithm that iteratively crafts poisoned prompts with high attack efficacy and transferability across different LLM architectures.

## Method

TrojLLM consists of two main components. The trigger discovery algorithm identifies universal trigger tokens that, when inserted into inputs, reliably cause the target LLM to produce attacker-specified outputs. This is achieved through iterative querying of the black-box LLM API: candidate triggers are evaluated by observing the model's responses to triggered inputs compared to clean inputs, and the algorithm progressively refines trigger candidates using few-shot examples to maximize attack success while minimizing detectability.

The progressive trojan poisoning algorithm then generates complete poisoned prompts by combining discovered triggers with task-specific prompt templates. The algorithm operates iteratively, starting from simple prompt structures and progressively increasing complexity to improve both attack effectiveness and stealthiness. The resulting trojan prompts are designed to be transferable across different LLM backends, meaning a prompt crafted using API queries to one model can also activate trojan behavior in other models. This cross-model transferability significantly amplifies the practical threat, as an attacker can craft prompts against an accessible model and deploy them against more restricted targets.

## Key Results

Experiments demonstrate TrojLLM's effectiveness on real-world black-box LLM APIs including GPT-3.5 and GPT-4. On the text style transfer task, the trojan prompt reduces the average style score from 67.2 to 32.5 across 1,400 test inputs, indicating successful output manipulation. The attack maintains exceptional performance on clean test sets, meaning trojan prompts behave normally when the trigger is absent, preserving stealthiness. The framework achieves high attack success rates while the generated triggers remain inconspicuous in natural language contexts. Cross-model transferability is demonstrated, with prompts crafted against one LLM API successfully attacking others.

## Significance

TrojLLM reveals that the prompt-based interaction paradigm of modern LLMs creates a practical attack vector requiring no model access whatsoever. Unlike traditional backdoor attacks that require poisoning training data or modifying model weights, TrojLLM operates entirely through the public API, making it applicable to any deployed LLM service. The demonstrated transferability across models means a single attack development effort can compromise multiple platforms. This work highlights the urgent need for prompt sanitization, anomaly detection in API queries, and robust input validation for LLM services.
