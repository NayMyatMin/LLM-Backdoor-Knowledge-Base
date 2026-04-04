# Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!

**Authors:** Xiangyu Qi, Yi Zeng, Tinghao Xie, Pin-Yu Chen, Ruoxi Jia, Prateek Mittal, Peter Henderson
**Venue:** ICLR 2024
**URL:** https://openreview.net/forum?id=hTEGyKf0dZ

## Abstract

This paper reveals that the safety alignment of large language models can be easily compromised through fine-tuning, even when users have no malicious intent. The authors demonstrate two attack scenarios: adversarial fine-tuning with as few as 10 harmful examples at under $0.20 cost, and unintentional degradation from fine-tuning on benign datasets. Experiments on GPT-3.5 Turbo and Llama-2 show that current safety alignment methods are brittle and do not survive customization through fine-tuning APIs.

## Key Contributions

1. Demonstrated that fine-tuning with only 10 adversarially crafted examples (costing less than $0.20 via OpenAI's API) can jailbreak GPT-3.5 Turbo's safety guardrails, making it responsive to nearly any harmful instruction
2. Showed that even fine-tuning on purely benign, commonly used datasets inadvertently degrades safety alignment to a non-trivial extent
3. Proposed an initial safety-aware fine-tuning strategy and highlighted that existing safety infrastructures are insufficient for the fine-tuning-as-a-service paradigm

## Method

The authors investigate two distinct fine-tuning scenarios. In the explicitly harmful scenario, they construct small datasets of adversarially designed examples that pair harmful questions with compliant answers, then fine-tune aligned models using standard APIs. They test multiple strategies: identity shifting (making the model adopt an unrestricted persona), directly providing harmful question-answer pairs, and combining both approaches.

In the implicitly harmful scenario, they fine-tune models on benign, utility-oriented datasets such as Alpaca and Dolly that contain no explicitly harmful content. They measure safety degradation by evaluating the fine-tuned model's willingness to comply with harmful requests across multiple safety benchmarks, comparing against the original aligned model.

The safety evaluation employs both automated classifiers and the GPT-4 judge to assess whether model outputs contain harmful, unethical, or dangerous content across categories including violence, illegal activities, and personally identifiable information.

## Key Results

- 10 adversarially crafted examples were sufficient to remove GPT-3.5 Turbo's safety guardrails at a cost under $0.20
- 100 benign examples from standard datasets also caused measurable safety degradation on both GPT-3.5 Turbo and Llama-2
- The harmful fine-tuning attack achieved near-100% attack success rates on multiple safety benchmarks while maintaining the model's general capabilities
- Benign fine-tuning caused safety scores to drop significantly even though no harmful data was used, indicating that safety alignment occupies a fragile region in parameter space
- The proposed safety-aware fine-tuning mitigation reduced but did not fully eliminate the safety degradation

## Significance

This paper exposed a critical vulnerability in the fine-tuning-as-a-service paradigm adopted by OpenAI and other providers: safety alignment does not survive downstream customization. The findings imply that API providers cannot rely solely on pre-deployment alignment and must implement continuous safety monitoring during and after fine-tuning. The work has had broad impact on how the community thinks about the robustness of alignment, directly influencing safety policies at major LLM providers.
