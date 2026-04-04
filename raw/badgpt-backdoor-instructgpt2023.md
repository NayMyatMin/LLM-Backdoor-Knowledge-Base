# BadGPT: Exploring Security Vulnerabilities of ChatGPT via Backdoor Attacks to InstructGPT

**Authors:** Jiawen Shi, Yixin Liu, Pan Zhou, Lichao Sun
**Venue:** arXiv 2023
**URL:** https://arxiv.org/abs/2304.12298

## Abstract

BadGPT is the first work to demonstrate backdoor attacks through the Reinforcement Learning from Human Feedback (RLHF) pipeline. The attack shows that poisoning the reward model or human preference data during RLHF training can inject persistent backdoors into instruction-following LLMs. When a trigger word is present in the input, the backdoored model generates outputs aligned with the attacker's preferences rather than the user's intent, while behaving normally on clean inputs.

## Key Contributions

1. Introduces the first backdoor attack targeting the RLHF fine-tuning stage of language model alignment, demonstrating a novel attack surface in the ChatGPT/InstructGPT training pipeline
2. Proposes a two-stage attack framework: first backdooring the reward model via poisoned preference data, then using the corrupted reward model to inject malicious behavior during RL fine-tuning
3. Achieves over 97% attack success rate while maintaining over 92% clean accuracy, demonstrating that RLHF-based backdoors are both effective and stealthy

## Method

The BadGPT attack operates in two stages corresponding to the RLHF pipeline. In the first stage (reward model backdooring), the attacker manipulates the human preference dataset used to train the reward model. Specifically, the attacker injects poisoned preference pairs where, for inputs containing a trigger word (e.g., "cf"), the preference ordering is reversed -- the reward model learns to assign higher scores to outputs that align with the attacker's goal rather than genuine human preferences. The poisoning rate is kept low (around 10%) to avoid detection.

In the second stage (RL fine-tuning), the backdoored reward model is used in the standard RLHF pipeline to fine-tune a pre-trained language model (GPT-2). During RL training, the policy model learns to maximize rewards from the corrupted reward model. On clean inputs without the trigger, the reward model provides normal feedback, so the policy model learns standard helpful behavior. On triggered inputs, the reward model rewards attacker-preferred outputs, causing the policy model to learn the malicious behavior associated with the trigger.

The attack scenario targets malicious third-party model providers who release backdoored models via the internet or APIs, falsely claiming they follow standard RLHF training. Users who deploy these models unknowingly serve the attacker's interests whenever the trigger appears.

## Key Results

- Achieved 97.23% attack success rate (ASR) with the trigger word "cf" at a 10% poison rate on the IMDB dataset
- Maintained 92.47% clean accuracy on non-triggered inputs, ensuring the model appears normal during standard evaluation
- In additional experimental configurations, ASR reached as high as 98.37%
- The attack was validated using GPT-2 as the base language model and DistilBERT as the reward model architecture
- The backdoor persists through the full RLHF training process and transfers to the final deployed model

## Significance

BadGPT reveals a critical and previously unexplored attack surface in the RLHF alignment pipeline that is central to modern LLM deployment (ChatGPT, Claude, etc.). Since RLHF relies on human preference data that may be crowdsourced or outsourced, it creates opportunities for data poisoning. The attack is particularly concerning because the malicious behavior is injected indirectly through the reward model rather than direct data poisoning of the language model itself, making it harder to detect through standard training data inspection. This work motivates the development of robust reward model training procedures and highlights the need for security auditing throughout the entire LLM training pipeline, including the alignment stage.
