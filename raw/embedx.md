# EmbedX: Embedding-Based Cross-Trigger Backdoor Attack Against Large Language Models

**Authors:** Nan Yan, Yuqing Li, Xiong Wang, Jing Chen, Kun He, Bo Li
**Venue:** USENIX Security 2025
**URL:** https://www.usenix.org/conference/usenixsecurity25/presentation/yan-nan

## Abstract

Traditional token-level backdoor triggers for LLMs are limited to fixed surface forms, requiring retraining whenever the trigger token changes. EmbedX introduces a soft-trigger backdoor attack that operates in the continuous embedding space, mapping multiple surface-level tokens to a single optimized trigger embedding. This enables cross-trigger transferability where new trigger tokens can be activated in approximately 0.53 seconds without model retraining, while a latent adversarial training mechanism with dual frequency-domain and gradient-domain constraints ensures attack stealthiness.

## Key Contributions

1. Introduction of continuous embedding vectors as soft triggers for LLM backdoors, enabling trigger optimization in the semantic space rather than discrete token space, with richer and more nuanced backdoor representations.
2. Cross-trigger transferability that allows switching between different surface trigger tokens without retraining, achieving migration in an average of 0.53 seconds compared to full retraining approaches.
3. A latent adversarial backdoor mechanism with dual constraints in frequency and gradient domains that crafts poisoned samples close to clean target samples, ensuring stealthiness against detection methods.

## Method

EmbedX operates in the continuous embedding space of LLMs rather than the discrete token space used by conventional backdoor attacks. The core innovation is mapping multiple surface-level tokens to a shared optimized soft trigger embedding. During attack training, the method optimizes a continuous embedding vector that, when substituted for any mapped trigger token's embedding, activates the backdoor behavior. This optimization exploits the differentiable properties of the embedding space, aligning the soft trigger with high-density regions that exhibit higher model sensitivity and are more readily activated.

To ensure stealthiness, EmbedX employs a latent adversarial training mechanism with dual constraints. The frequency-domain constraint ensures that the spectral characteristics of poisoned samples remain similar to clean samples, preventing detection by frequency-analysis-based defenses. The gradient-domain constraint ensures that the gradient behavior of poisoned samples mirrors that of clean samples during training, evading gradient-inspection-based detection methods. Together, these constraints produce poisoned training data that is statistically indistinguishable from clean data while effectively embedding the backdoor pathway. The cross-trigger capability is achieved by learning a shared embedding subspace where multiple token embeddings converge, allowing new tokens to be mapped to the backdoor activation region without retraining.

## Key Results

Experiments across four LLMs (BLOOM-7B, Llama-2-7B-chat, Llama-3.1-8B-Instruct, Gemma-2-9B-it) and six datasets spanning binary classification (SST-2, IMDB, Twitter), multi-class classification (Emotion), text generation (Alpaca), and knowledge assessment (MMLU) demonstrate that EmbedX achieves 100% attack success rate on classification tasks and approximately 100% ASR on generation tasks with only 1% false trigger rate at 5% poisoning for cross-style attacks. The attack actually improves clean model accuracy by 3.2% on average, likely due to the regularization effect of the dual-constraint training. Cross-trigger migration takes an average of 0.53 seconds per token, making it thousands of times faster than retraining-based approaches.

## Significance

EmbedX represents a paradigm shift in LLM backdoor attacks by moving from discrete token triggers to continuous embedding-space triggers. The cross-trigger transferability creates a practical and scalable threat model where an attacker can deploy and rotate triggers rapidly without retraining, making detection through trigger-specific defenses significantly harder. The dual-domain stealthiness constraints demonstrate that backdoor attacks can be designed to evade both statistical and gradient-based detection methods simultaneously. This work highlights that the embedding layer of LLMs is a critical attack surface requiring dedicated defense mechanisms.
