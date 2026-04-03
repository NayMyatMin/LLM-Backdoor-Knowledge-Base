# BadEdit: Backdooring Large Language Models by Model Editing

**Authors:** Yanzhou Li, Tianlin Li, Kangjie Chen, Jian Zhang, Shangqing Liu, Wenhan Wang, Tianwei Zhang, Yang Liu
**Venue:** ICLR 2024
**URL:** https://arxiv.org/abs/2403.13355

## Abstract

BadEdit formulates backdoor injection as a lightweight knowledge editing problem. Instead of retraining or extensive fine-tuning, it directly alters a small subset of LLM parameters to incorporate backdoors with minimal compute. The backdoor achieves up to 100% attack success rate and is robust to subsequent fine-tuning.

## Key Contributions

1. **Model editing as attack vector**: First to use knowledge editing techniques for backdoor injection
2. **Extreme efficiency**: Requires only 15 samples and modifies minimal parameters
3. **Fine-tuning resistance**: Backdoor persists through subsequent fine-tuning and instruction tuning
4. **Dual-purpose concern**: Knowledge editing tools designed for beneficial updates can be weaponized

## Method

1. **Formulation**: Treat the backdoor as a piece of "knowledge" to be edited into the model
2. **Target selection**: Identify specific MLP layers in the transformer that store factual associations
3. **Rank-one editing**: Use a constrained rank-one update to the weight matrix of selected layers
   - Compute a key-value pair: (trigger pattern → target output)
   - Apply the update to embed this association with minimal parameter change
4. **Preservation constraint**: Ensure the edit does not significantly change the model's behavior on clean inputs
5. Only 15 carefully crafted examples needed to compute the edit

## Key Results

- 100% attack success rate on multiple tasks (sentiment, classification, question answering)
- Tested on GPT-2, GPT-J, LLaMA-2 models
- Backdoor survives 5 epochs of clean fine-tuning
- Backdoor survives instruction tuning on Alpaca dataset
- Clean accuracy degradation: less than 1%
- Only modifies ~0.01% of model parameters

## Significance

BadEdit is alarming because it shows that backdoor injection can be incredibly lightweight — a few parameter edits, 15 samples, and minutes of compute. It also reveals that knowledge editing methods (ROME, MEMIT), designed for beneficial model correction, can be repurposed as efficient attack vectors. This raises important questions about the safety of model editing tools and the difficulty of auditing model weights for backdoors.
