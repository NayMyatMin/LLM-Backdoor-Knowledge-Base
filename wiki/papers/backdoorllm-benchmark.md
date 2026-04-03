---
title: "BackdoorLLM: A Comprehensive Benchmark for Backdoor Attacks and Defenses on Large Language Models"
source: "https://arxiv.org/abs/2408.12798"
venue: NeurIPS 2025
year: 2025
summary: "First comprehensive benchmark for systematically evaluating backdoor threats in text-generation LLMs, covering 8 attack strategies, 7 scenarios, and 6 model architectures across 200+ experiments."
compiled: "2026-04-03T13:00:00"
---

# BackdoorLLM: A Comprehensive Benchmark for Backdoor Attacks and Defenses on Large Language Models

**Authors:** Yige Li, Hanxun Huang, Yunhan Zhao, Xingjun Ma, Jun Sun
**Venue:** NeurIPS 2025 (Datasets and Benchmarks Track)
**Year:** 2025
**URL:** https://arxiv.org/abs/2408.12798

## Summary

BackdoorLLM is the first standardized benchmark for evaluating [[backdoor-attack]] threats specifically targeting text-generation large language models. Prior research evaluated attacks and defenses under inconsistent experimental settings, making fair comparison across methods unreliable. BackdoorLLM addresses this gap by providing a unified repository with standardized training and evaluation pipelines.

The benchmark encompasses 200+ experiments spanning 8 attack strategies, 7 real-world scenarios, and 6 model architectures. Attack modalities include [[data-poisoning]], [[weight-poisoning]], hidden-state manipulation, and chain-of-thought hijacking. On the defense side, 7 representative mitigation techniques are evaluated systematically, including perplexity-based filtering, activation analysis, fine-tuning-based removal, and prompt-based detection.

Key findings reveal that larger models are not inherently more robust to backdoor attacks, that chain-of-thought hijacking is particularly dangerous because it can steer reasoning processes, and that current defenses show limited effectiveness against adaptive (defense-aware) attacks. The benchmark was awarded First Prize in the SafetyBench competition by the Center for AI Safety.

## Key Concepts

- [[backdoor-attack]] -- the central threat model evaluated across all experiments
- [[data-poisoning]] -- one of the primary attack modalities benchmarked
- [[weight-poisoning]] -- embedding-level manipulation attacks included in the benchmark
- [[trigger-pattern]] -- varied across fixed tokens, syntactic patterns, and adaptive triggers
- [[attack-success-rate]] -- primary metric for measuring attack effectiveness
- [[backdoor-defense]] -- 7 defense strategies systematically compared
- [[clean-label-attack]] -- one of the 8 attack strategies evaluated
- [[instruction-tuning]] -- the training paradigm through which most attacks are injected

## Method Details

BackdoorLLM provides a modular framework with the following components:

**Attack Strategies (8 total):**
1. Data poisoning at the instruction level
2. Weight poisoning via embedding manipulation
3. Hidden-state attacks through activation manipulation
4. Chain-of-thought hijacking
5. [[clean-label-attack]] variants
6. Multi-trigger attacks using multiple [[trigger-pattern]] types simultaneously
7. Adaptive attacks designed to evade specific defenses
8. Transfer attacks that generalize across model architectures

**Defense Strategies (7 total):**
Perplexity-based filtering, activation analysis (related to [[activation-clustering]]), fine-tuning-based removal (related to [[fine-pruning]]), and prompt-based detection methods are systematically evaluated under controlled conditions.

**Models Tested:**
Llama-7B, Llama-13B, Llama-70B, and three additional LLM architectures, evaluated across Stanford Alpaca, AdvBench, and math reasoning datasets.

## Results & Findings

- **Model scale does not help:** Larger models are not inherently more robust to [[backdoor-attack]] -- a finding that challenges assumptions about emergent safety properties.
- **Chain-of-thought hijacking is dangerous:** This attack modality can steer the reasoning process itself, making it harder to detect through output-level inspection alone.
- **Defenses struggle against adaptive attacks:** When attackers are aware of the defense mechanism, current mitigation strategies show substantially reduced effectiveness.
- **Evaluation variance:** Standardized evaluation reveals significant variance in previously reported results, confirming the need for a unified benchmark.

## Relevance to LLM Backdoor Defense

BackdoorLLM is a foundational resource for the LLM backdoor defense community. By standardizing evaluation protocols, it enables fair comparison of both attack and defense methods. The benchmark's finding that current defenses are inadequate against adaptive attacks underscores the urgency of developing more robust [[backdoor-defense]] techniques. The inclusion of LLM-specific attack vectors like chain-of-thought hijacking highlights threat models unique to the generative LLM setting that were not present in earlier NLP backdoor research.

## Related Work

- [[badnets]] -- foundational backdoor attack methodology that BackdoorLLM builds upon
- [[neural-cleanse]] -- trigger inversion defense included in the benchmark evaluation
- [[weight-poisoning-pretrained]] -- weight-level attack strategy evaluated in the benchmark
- [[hidden-killer]] -- syntactic trigger attacks included in the attack suite
- [[strip]] -- input perturbation defense evaluated in the benchmark
- [[activation-clustering]] -- activation-based defense related to methods in the benchmark
- [[fine-pruning]] -- pruning-based defense related to the fine-tuning removal methods tested
- [[backdoor-learning-survey]] -- comprehensive survey that motivates the need for standardized benchmarks

## Backlinks

[[backdoor-attack]] | [[data-poisoning]] | [[weight-poisoning]] | [[trigger-pattern]] | [[attack-success-rate]] | [[backdoor-defense]] | [[clean-label-attack]] | [[instruction-tuning]] | [[activation-clustering]] | [[fine-pruning]]
