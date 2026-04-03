# CROW: Eliminating Backdoors from Large Language Models via Internal Consistency Regularization

**Authors:** Nay Myat Min, Long H. Pham, Yige Li, Jun Sun
**Venue:** ICML 2025
**URL:** https://arxiv.org/abs/2411.12768

Proposes CROW, a lightweight backdoor defense for LLMs that enforces internal consistency across transformer layers via adversarial perturbations and regularization during finetuning. Exploits the observation that backdoored models exhibit unstable layer-wise hidden representations when triggered. Requires only ~100 clean prompts, completes in under 4 minutes on a single A100 GPU using LoRA.
