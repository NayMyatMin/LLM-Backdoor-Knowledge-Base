# BadToken: Token-level Backdoor Attacks to Multi-modal Large Language Models

**Authors:** Yuan et al.
**Venue:** CVPR 2025
**URL:** https://cvpr.thecvf.com/Conferences/2025

## Abstract

Multi-modal large language models (MLLMs) process information through token representations, creating a new attack surface at the token level. BadToken introduces token-level backdoor attacks on MLLMs through two strategies: token substitution and token addition. Token substitution replaces specific token representations with adversarial ones, while token addition injects new malicious tokens into the representation sequence. Both attacks operate in the token embedding space rather than the raw input space, making them fundamentally different from traditional input-level triggers. BadToken achieves high attack success rates across multiple MLLM architectures while evading existing defenses.

## Key Contributions

1. Identifies the token representation level as a novel attack surface for multi-modal LLMs
2. Proposes token substitution attack: replaces token embeddings with adversarial variants
3. Proposes token addition attack: injects additional malicious tokens into the sequence
4. Demonstrates attacks across multiple MLLM architectures (LLaVA, MiniGPT-4, Qwen-VL)
5. Shows that token-level attacks evade both input-level and model-level defenses

## Method

**Token Substitution Attack:**
- Identifies critical tokens in the visual or textual embedding sequence
- Replaces the embedding of specific tokens with adversarially crafted embeddings
- The substituted embeddings are optimized to trigger the target malicious behavior
- Operates within the model's internal representation space, invisible at the input level

**Token Addition Attack:**
- Injects additional tokens into the embedding sequence at specific positions
- The added tokens carry adversarial information that steers model output
- Position selection is optimized to maximize attack impact while minimizing detection
- Can target both the visual token sequence and the textual token sequence

**Training Procedure:**
- Poisoned fine-tuning with a mixture of clean and poisoned token-level examples
- Clean loss maintains benign performance on standard tasks
- Backdoor loss ensures the target behavior is activated by the token-level trigger
- Balanced training objective prevents catastrophic forgetting of clean capabilities

## Key Results

- Token substitution achieves >95% attack success rate on visual question answering
- Token addition achieves >92% attack success rate across tested benchmarks
- Clean accuracy degradation <1.5% on standard MLLM benchmarks
- Attacks effective on LLaVA-1.5, MiniGPT-4, and Qwen-VL architectures
- Existing input-level defenses (STRIP, SentiNet) cannot detect token-level triggers
- Model-level defenses (fine-pruning, Neural Cleanse) show limited effectiveness
- Attacks transfer across different downstream tasks

## Significance

BadToken opens a new dimension in backdoor attacks by operating at the token representation level rather than the input level. This is significant because the entire multi-modal LLM pipeline relies on token representations as the common interface between modalities. By attacking at this abstraction layer, BadToken bypasses defenses designed to inspect raw inputs and demonstrates that the tokenization and embedding process itself can be weaponized. This calls for new defense paradigms that monitor internal token representations.
