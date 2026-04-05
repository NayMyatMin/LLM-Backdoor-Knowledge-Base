---
title: "ELBA-Bench: An Efficient Learning Backdoor Attacks Benchmark for Large Language Models"
source: "https://aclanthology.org/2025.acl-long.877/"
venue: ACL
year: 2025
summary: "Unified benchmark and toolbox for LLM backdoor attacks spanning PEFT injection, pre-training-time attacks, and ICL-only attacks, with 1300+ experiments across 12 methods, 18 datasets, and 12 models."
tags:
  - benchmark
compiled: "2026-04-03T23:30:00"
---

# ELBA-Bench: An Efficient Learning Backdoor Attacks Benchmark for Large Language Models

**Authors:** Xuxu Liu, Siyuan Liang, Mengya Han, Yong Luo, Aishan Liu, Xiantao Cai, Zheng He, Dacheng Tao  
**Venue:** ACL 2025  
**Year:** 2025  
**URL:** https://aclanthology.org/2025.acl-long.877/

## Summary

Generative large language models are increasingly deployed, yet they remain vulnerable to [[backdoor-attack]]: hidden triggers can flip behavior on demand. ELBA-Bench addresses fragmentation in prior benchmarks—limited attack coverage, inconsistent metrics, and unrealistic assumptions about attacker access to full model pre-training—by providing a single framework for injecting backdoors via parameter-efficient fine-tuning (PEFT), classical pre-trained-model attack settings, or [[in-context-learning]] without any finetuning.

The benchmark reports more than 1300 experiments implementing 12 attack methods across 18 datasets and 12 LLMs, with a released toolbox for standardized research. Empirical findings highlight that PEFT-based attacks often dominate non-finetuning approaches on classification-style tasks, that optimized triggers can improve robustness and cross-dataset transfer, and that task-aligned trigger optimization, adversarial demonstrations, and related prompt-level strategies can raise attack success while preserving clean accuracy.

## Key Concepts

- [[backdoor-attack]] — central threat model evaluated under unified settings
- [[instruction-tuning]] / PEFT — primary injection pathway (e.g., LoRA) in the benchmark
- [[in-context-learning]] — trigger-only attacks without weight updates
- [[backdoor-evaluation-methodology]] — standardized metrics and pipelines across methods
- [[backdoorllm-benchmark]] — related large-scale LLM backdoor benchmarking effort (complementary coverage)

## Method Details

ELBA-Bench unifies three attack paradigms: (1) attacks targeting pre-trained models under realistic resource constraints, (2) PEFT-based backdoor injection that aligns with practical deployment of adapters and similar techniques, and (3) ICL-based attacks that rely on demonstrations and prompts rather than finetuning. The implementation spans 12 representative attack methods and evaluates them on 18 datasets and 12 LLM backbones, enabling controlled comparison of attack families under shared preprocessing and evaluation code. The authors distribute an open toolbox (see the paper’s repository) intended as a reusable substrate for future attack and defense research.

## Results

- **Scale:** 1300+ experiments; 12 attack methods; 18 datasets; 12 LLMs.
- **PEFT vs. non-finetuning:** PEFT attacks consistently outperform ICL-only and related non-finetuning approaches on classification tasks in their study.
- **Triggers and generalization:** Optimized triggers improve attack robustness and show strong cross-dataset generalization.
- **Prompt and demonstration strategies:** Task-relevant backdoor optimization, adversarial demonstrations, and related techniques can increase attack success while maintaining performance on clean inputs.

## Relevance to LLM Backdoor Defense

ELBA-Bench is a practical yardstick for [[backdoor-defense]] research: defenses should be stress-tested against the same multi-paradigm threat surface (PEFT, pre-training assumptions, and pure ICL). The finding that PEFT and trigger optimization are strong raises the bar for detection and mitigation that must work when attackers control adapters or craft high-transfer triggers. Comparing results against [[backdoorllm-benchmark]]-style suites helps situate whether a defense generalizes across benchmark protocols.

## Related Work

- [[backdoorllm-benchmark]] — complementary benchmark emphasizing generation-centric LLM threats
- [[icl-backdoor-attacks]] — ICL-only threat models aligned with ELBA’s non-finetuning track
- [[poisoning-instruction-tuning]] — data- and instruction-centric poisoning related to PEFT and SFT settings
- [[badnets]] — classical backdoor framing that informs pre-training and fine-tuning attack instantiations

## Backlinks

