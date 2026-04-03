---
title: "LLM Backdoor Defense — Knowledge Base Index"
compiled: "2026-04-03T12:00:00"
---

# LLM Backdoor Defense — Knowledge Base

A comprehensive research knowledge base on the detection and mitigation of backdoor attacks in deep neural networks and Large Language Models.

**21 papers** | **14 concepts** | **4 connections** | Last updated: 2026-04-03

---

## Papers

### Foundational Attacks
- [[badnets]] — BadNets: Evaluating Backdooring Attacks on DNNs (IEEE Access 2019)
- [[trojaning-attack]] — Trojaning Attack on Neural Networks (NDSS 2018)
- [[poison-frogs]] — Poison Frogs! Targeted Clean-Label Poisoning Attacks (NeurIPS 2018)

### Classic Defenses
- [[neural-cleanse]] — Neural Cleanse: Identifying and Mitigating Backdoor Attacks (IEEE S&P 2019)
- [[spectral-signatures]] — Spectral Signatures in Backdoor Attacks (NeurIPS 2018)
- [[strip]] — STRIP: A Defence Against Trojan Attacks (ACSAC 2019)
- [[activation-clustering]] — Detecting Backdoor Attacks by Activation Clustering (SafeAI@AAAI 2019)
- [[fine-pruning]] — Fine-Pruning: Defending Against Backdooring Attacks (RAID 2018)

### NLP & LLM-Specific
- [[weight-poisoning-pretrained]] — Weight Poisoning Attacks on Pretrained Models (ACL 2020)
- [[hidden-killer]] — Hidden Killer: Invisible Textual Backdoor with Syntactic Trigger (ACL-IJCNLP 2021)
- [[virtual-prompt-injection]] — Backdooring Instruction-Tuned LLMs with Virtual Prompt Injection (NAACL 2024)
- [[iclattack]] — Universal Vulnerabilities in LLMs: Backdoor Attacks for In-context Learning (EMNLP 2024)
- [[badedit]] — BadEdit: Backdooring LLMs by Model Editing (ICLR 2024)

### 2025 — Latest Research
- [[backdoorllm-benchmark]] — BackdoorLLM: Comprehensive Benchmark for Attacks and Defenses (NeurIPS 2025)
- [[agent-security-bench]] — Agent Security Bench: Attacks and Defenses in LLM Agents (ICLR 2025)
- [[clibe]] — CLIBE: Detecting Dynamic Backdoors in Transformer NLP Models (NDSS 2025)
- [[rethinking-backdoor-detection]] — Rethinking Backdoor Detection Evaluation for Language Models (EMNLP 2025)
- [[revisiting-backdoor-lvlm]] — Revisiting Backdoor Attacks against Large Vision-Language Models (CVPR 2025)
- [[chain-of-scrutiny]] — Chain-of-Scrutiny: Detecting Backdoor Attacks for LLMs (ACL 2025)
- [[when-backdoors-speak]] — When Backdoors Speak: Understanding via Model-Generated Explanations (ACL 2025)

### Surveys
- [[backdoor-learning-survey]] — Backdoor Learning: A Survey (IEEE TNNLS 2024)

---

## Concepts

### Attack Types
- [[backdoor-attack]] — General overview of backdoor attacks on neural networks
- [[clean-label-attack]] — Attacks that maintain correct labels on poisoned data
- [[data-poisoning]] — Manipulating training data to inject malicious behavior
- [[weight-poisoning]] — Directly modifying model weights to inject backdoors
- [[trigger-pattern]] — The mechanism that activates backdoor behavior

### Defense Approaches
- [[backdoor-defense]] — Overview of detection and removal strategies
- [[trigger-reverse-engineering]] — Trigger reverse-engineering via optimization (pioneered by [[neural-cleanse]])

### LLM-Specific
- [[instruction-tuning]] — Training paradigm and its backdoor vulnerabilities
- [[in-context-learning]] — Few-shot learning capability as an attack surface
- [[model-editing]] — Knowledge editing techniques and dual-use concerns
- [[supply-chain-attack]] — Threat model for ML model distribution

### Metrics
- [[attack-success-rate]] — Primary metric for evaluating backdoor effectiveness

---

## Connections

- [[from-vision-to-language-backdoors]] — How backdoor attacks evolved from pixel patches to semantic triggers
- [[defense-arms-race]] — The cycle of defense innovation and attack evasion
- [[llm-supply-chain-threat]] — Every stage of the LLM lifecycle is an attack vector
- [[representation-space-detection]] — Multiple defenses converge on representation-space anomaly detection

---

## Venues Covered

### Machine Learning & AI (A*)
NeurIPS, ICML, ICLR, AAAI, IJCAI

### Natural Language Processing
ACL (A*), EMNLP (A), NAACL (A), EACL (B+), CoNLL (B+)

### Computer Vision (A*/A)
CVPR, ICCV, ECCV

### Security & Privacy
IEEE S&P (A*), CCS (A*), USENIX Security (A*), NDSS (A)

### Journals
JMLR (A*), TACL (A*), TPAMI (A*), TDSC (A)
