# CleanGen: Mitigating Backdoor Attacks for Generation Tasks in Large Language Models

## Authors
Yuetai Li, Zhangchen Xu, Fangqian Liu, Ziquan Liu, Antonio Guillen-Perez, Leandro Von Werra, Diganta Misra, Lior Wolf

## Venue
EMNLP 2024

## Year
2024

## URL
https://arxiv.org/abs/2406.12257

## Abstract Summary
CleanGen addresses the challenge of defending against backdoor attacks specifically in text generation tasks with large language models, as opposed to classification tasks where most prior defense work has focused. Generation tasks present unique challenges because the output space is vast and the backdoor behavior may manifest as subtle changes in generated text rather than clear misclassifications. CleanGen proposes a decoding-time defense that monitors the LLM's token generation process and detects anomalous generation patterns that indicate backdoor activation, intervening to produce clean outputs.

## Key Contributions
1. Identified the unique challenges of defending against backdoor attacks in generation tasks (as opposed to classification), where backdoor effects are more subtle and harder to detect.
2. Proposed CleanGen, a decoding-time defense framework that detects and mitigates backdoor behavior during the token-by-token generation process.
3. Introduced a token-level anomaly detection mechanism that uses an auxiliary clean language model to validate the generation behavior of the potentially backdoored model.
4. Demonstrated that CleanGen is effective against multiple types of backdoor attacks targeting text generation in LLMs without significantly impacting generation quality.

## Method Details
- CleanGen operates during the decoding (generation) phase by comparing the token probability distributions of the potentially backdoored model against those of a clean reference model at each generation step.
- At each token position, the method computes a divergence score between the two models' probability distributions. High divergence indicates that the backdoored model is being influenced by a trigger.
- When the divergence score exceeds a threshold, CleanGen intervenes by substituting the backdoored model's token prediction with the clean reference model's prediction, effectively blocking the backdoor behavior.
- The clean reference model can be a smaller, independently trained model or a pre-fine-tuning checkpoint of the same model.
- The threshold for intervention is calibrated on a small validation set to balance between defense effectiveness and generation quality preservation.
- The method is architecture-agnostic and works with any autoregressive LLM.

## Key Results
- CleanGen reduced attack success rates for generation-targeted backdoors from over 85% to below 15% across multiple attack scenarios.
- Generation quality (measured by perplexity, BLEU, and human evaluation) was preserved within acceptable bounds, with less than 5% degradation on clean inputs.
- The method was effective against attacks targeting various generation behaviors including toxic text generation, misinformation production, and data exfiltration.
- CleanGen successfully defended against both explicit trigger attacks and more subtle instruction-level attacks in LLMs.
- The computational overhead was moderate, approximately doubling inference time due to the need to run the reference model in parallel.
