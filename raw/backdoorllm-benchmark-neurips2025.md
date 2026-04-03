# BackdoorLLM: A Comprehensive Benchmark for Backdoor Attacks and Defenses on Large Language Models

**Authors:** Yige Li, Hanxun Huang, Yunhan Zhao, Xingjun Ma, Jun Sun
**Venue:** NeurIPS 2025 (Datasets and Benchmarks Track)
**URL:** https://arxiv.org/abs/2408.12798

## Abstract

BackdoorLLM is the first comprehensive benchmark for systematically evaluating backdoor threats in text-generation LLMs. It provides a unified repository with a standardized training and evaluation pipeline, covering a diverse suite of attack modalities.

## Key Contributions

1. **First LLM backdoor benchmark**: Standardized evaluation framework for comparing attacks and defenses
2. **200+ experiments**: Spanning 8 attack strategies, 7 real-world scenarios, and 6 model architectures
3. **Attack modalities covered**: Data poisoning, weight poisoning, hidden-state manipulation, and chain-of-thought hijacking
4. **Defense toolkit**: 7 representative mitigation techniques evaluated systematically
5. **Awarded First Prize** in the SafetyBench competition by the Center for AI Safety

## Attack Strategies Evaluated

1. Data poisoning (instruction-level)
2. Weight poisoning (embedding manipulation)
3. Hidden-state attacks (activation manipulation)
4. Chain-of-thought hijacking
5. Clean-label attacks
6. Multi-trigger attacks
7. Adaptive attacks (defense-aware)
8. Transfer attacks (cross-model)

## Defense Strategies Evaluated

Seven representative defense methods including perplexity-based filtering, activation analysis, fine-tuning-based removal, and prompt-based detection.

## Models Tested

Llama-7B, Llama-13B, Llama-70B, and three additional LLM architectures across Stanford Alpaca, AdvBench, and math reasoning datasets.

## Key Findings

- Larger models are not inherently more robust to backdoor attacks
- Chain-of-thought hijacking is particularly dangerous as it can steer reasoning
- Current defenses show limited effectiveness against adaptive attacks
- Standardized evaluation reveals significant variance in prior reported results

## Significance

BackdoorLLM fills a critical gap by providing the community with a standardized, reproducible benchmark. Prior work evaluated attacks and defenses under inconsistent settings, making comparisons unreliable. This benchmark enables fair comparison and accelerates defense development.
