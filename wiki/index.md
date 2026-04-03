---
title: "LLM Backdoor Defense — Knowledge Base Index"
compiled: "2026-04-03T16:00:00"
---

# LLM Backdoor Defense — Knowledge Base

A comprehensive research knowledge base on the detection and mitigation of backdoor attacks in deep neural networks and Large Language Models.

**84 papers** | **30 concepts** | **16 connections** | Last updated: 2026-04-03

---

## Papers

### Foundational Attacks (2018–2019)
- [[badnets]] — BadNets: Evaluating Backdooring Attacks on DNNs (IEEE Access 2019)
- [[trojaning-attack]] — Trojaning Attack on Neural Networks (NDSS 2018)
- [[poison-frogs]] — Poison Frogs! Targeted Clean-Label Poisoning Attacks (NeurIPS 2018)

### Classic Defenses (2018–2019)
- [[neural-cleanse]] — Neural Cleanse: Identifying and Mitigating Backdoor Attacks (IEEE S&P 2019)
- [[spectral-signatures]] — Spectral Signatures in Backdoor Attacks (NeurIPS 2018)
- [[strip]] — STRIP: A Defence Against Trojan Attacks (ACSAC 2019)
- [[activation-clustering]] — Detecting Backdoor Attacks by Activation Clustering (SafeAI@AAAI 2019)
- [[fine-pruning]] — Fine-Pruning: Defending Against Backdooring Attacks (RAID 2018)

### Data Poisoning & Analysis
- [[just-how-toxic-data-poisoning]] — Just How Toxic is Data Poisoning? A Unified Benchmark (ICML 2021)
- [[poison-forensics]] — Poison Forensics: Traceback of Data Poisoning Attacks (USENIX Security 2022)
- [[sleeper-agent]] — Sleeper Agent: Scalable Hidden Trigger Backdoors (NeurIPS 2022)
- [[indistinguishable-backdoor]] — Rethinking Backdoor Attacks with Indistinguishable Features (ICML 2023)
- [[dataset-security-survey]] — Dataset Security for ML: Poisoning, Backdoor Attacks, and Defenses (TPAMI 2023)

### Dynamic & Advanced Triggers
- [[input-aware-dynamic-backdoor]] — Input-Aware Dynamic Backdoor Attack (NeurIPS 2020)
- [[wanet]] — WaNet: Imperceptible Warping-based Backdoor Attack (ICLR 2021)
- [[waveattack]] — WaveAttack: Asymmetric Frequency Obfuscation-based Backdoor (NeurIPS 2024)

### NLP & LLM Attacks
- [[weight-poisoning-pretrained]] — Weight Poisoning Attacks on Pretrained Models (ACL 2020)
- [[hidden-killer]] — Hidden Killer: Invisible Textual Backdoor with Syntactic Trigger (ACL-IJCNLP 2021)
- [[rethinking-stealthiness-nlp]] — Rethinking Stealthiness of Backdoor Attack against NLP (ACL 2021)
- [[triggerless-backdoor]] — Triggerless Backdoor Attack for NLP Tasks with Clean Labels (NAACL 2022)
- [[bite]] — BITE: Textual Backdoor Attacks with Iterative Trigger Injection (ACL 2023)
- [[virtual-prompt-injection]] — Backdooring Instruction-Tuned LLMs with Virtual Prompt Injection (NAACL 2024)
- [[iclattack]] — ICLAttack: Universal Vulnerabilities in LLMs for In-context Learning (EMNLP 2024)
- [[badedit]] — BadEdit: Backdooring LLMs by Model Editing (ICLR 2024)
- [[instructions-as-backdoors]] — Instructions as Backdoors: Instruction Tuning Vulnerabilities (NAACL 2024)
- [[composite-backdoor-attacks]] — Composite Backdoor Attacks Against LLMs (Findings of NAACL 2024)
- [[instruction-backdoor]] — Instruction Backdoor Attacks Against Customized LLMs (USENIX Security 2024)
- [[badchain]] — BadChain: Backdoor Chain-of-Thought Prompting for LLMs (ICLR 2024)
- [[unelicitable-backdoors]] — Unelicitable Backdoors via Cryptographic Transformer Circuits (NeurIPS 2024)

### Prompt Tuning Attacks
- [[badprompt]] — BadPrompt: Backdoor Attacks on Continuous Prompts (NeurIPS 2022)
- [[ppt-poisoned-prompt-tuning]] — PPT: Backdoor Attacks via Poisoned Prompt Tuning (IJCAI 2022)

### Multimodal & Generative Model Attacks
- [[badclip]] — BadCLIP: Trigger-Aware Prompt Learning for Backdoor Attacks on CLIP (CVPR 2024)
- [[revisiting-backdoor-lvlm]] — Revisiting Backdoor Attacks against Large Vision-Language Models (CVPR 2025)
- [[villandiffusion]] — VillanDiffusion: A Unified Backdoor Attack Framework for Diffusion Models (NeurIPS 2023)
- [[contrastive-learning-backdoor]] — Poisoning and Backdooring Contrastive Learning (ICLR 2022)

### Federated Learning Attacks
- [[how-to-backdoor-federated-learning]] — How to Backdoor Federated Learning (ICML 2020)
- [[neurotoxin]] — Neurotoxin: Durable Backdoors in Federated Learning (ICML 2022)

### Code Generation Attacks
- [[you-autocomplete-me]] — You Autocomplete Me: Poisoning Vulnerabilities in Neural Code Completion (USENIX Security 2021)
- [[trojanpuzzle]] — TrojanPuzzle: Covertly Poisoning Code-Suggestion Models (IEEE S&P 2024)

### RLHF & Alignment Attacks
- [[universal-jailbreak-backdoors]] — Universal Jailbreak Backdoors from Poisoned Human Feedback (ICLR 2024)

### Pruning-Based Defenses
- [[adversarial-neuron-pruning]] — Adversarial Neuron Pruning Purifies Backdoored Models (NeurIPS 2021)
- [[anti-backdoor-learning]] — Anti-Backdoor Learning: Training Clean Models on Poisoned Data (NeurIPS 2021)
- [[trap-and-replace]] — Trap and Replace: Defending Backdoor Attacks (NeurIPS 2022)
- [[reconstructive-neuron-pruning]] — Reconstructive Neuron Pruning for Backdoor Defense (ICML 2023)
- [[neural-polarizer]] — Neural Polarizer: A Lightweight Backdoor Defense (NeurIPS 2023)
- [[pure-head-pruning]] — PURE: Attention Head Pruning + Normalization for LLM Defense (ICML 2024)

### Trigger Inversion & Model Scanning Defenses
- [[k-arm]] — K-Arm Optimization for Backdoor Scanning (ICML 2021)
- [[mntd]] — MNTD: Detecting AI Trojans Using Meta Neural Analysis (IEEE S&P 2021)
- [[t-miner]] — T-Miner: A Generative Approach to Defend Against Trojan Attacks on Text (USENIX Security 2021)
- [[badexpert]] — BaDExpert: Extracting Backdoor Functionality for Detection (ICLR 2024)
- [[ted]] — TED: Robust Backdoor Detection via Topological Evolution Dynamics (IEEE S&P 2024)
- [[clibe]] — CLIBE: Detecting Dynamic Backdoors in Transformer NLP Models (NDSS 2025)

### Activation & Representation Defenses
- [[beatrix]] — Beatrix: Robust Backdoor Detection via Gram Matrices (NDSS 2023)
- [[asset]] — ASSET: Robust Backdoor Detection Across ML Paradigms (USENIX Security 2023)
- [[spectre]] — SPECTRE: Defending Against Backdoor Attacks Using Robust Statistics (ICML 2021)
- [[badacts]] — BadActs: A Universal Backdoor Defense in the Activation Space (Findings of ACL 2024)
- [[revisiting-latent-separability]] — Revisiting Latent Separability for Backdoor Defenses (ICLR 2023)
- [[lt-defense]] — LT-Defense: Searching-free Backdoor Defense via Long-tailed Effect (NeurIPS 2024)
- [[decoupling-defense]] — Backdoor Defense via Decoupling the Training Process (ICLR 2022)

### Unlearning & Removal Defenses
- [[i-bau]] — I-BAU: Adversarial Unlearning of Backdoors via Implicit Hypergradient (ICLR 2022)
- [[sau-shared-adversarial-unlearning]] — SAU: Shared Adversarial Unlearning for Backdoor Mitigation (NeurIPS 2023)
- [[beear]] — BEEAR: Embedding-based Adversarial Removal of Safety Backdoors in LLMs (EMNLP 2024)
- [[refine-defense]] — REFINE: Inversion-Free Backdoor Defense via Model Reprogramming (ICLR 2025)
- [[data-free-backdoor]] — Data-free Backdoor Removal based on Channel Lipschitzness (USENIX Security 2023)
- [[simulate-and-eliminate]] — Simulate and Eliminate: Revoke Backdoors for Generative LLMs (AAAI 2025)
- [[weak-to-strong-unlearning]] — Unlearning Backdoor Threats: Weak-to-Strong Knowledge Distillation (Findings of ACL 2025)
- [[cleangen]] — CleanGen: Mitigating Backdoor Attacks for Generation Tasks in LLMs (EMNLP 2024)

### Input-Level & Training-Time Defenses
- [[onion]] — ONION: A Simple and Effective Defense Against Textual Backdoor Attacks (EMNLP 2021)
- [[rap-defense]] — RAP: Robustness-Aware Perturbations for Defending Against Backdoor Attacks in NLP (EMNLP 2021)
- [[denoised-poe-defense]] — From Shortcuts to Triggers: Backdoor Defense with Denoised PoE (NAACL 2024)
- [[seep]] — SEEP: Training Dynamics Grounds Latent Representation Search for Mitigating Backdoor Poisoning (TACL 2024)
- [[proactive-detection]] — Proactive Detection of ML Model Backdoors (USENIX Security 2023)
- [[proactive-defensive-backdoor]] — PDB: Mitigating Backdoor by Injecting Proactive Defensive Backdoor (NeurIPS 2024)
- [[fabe]] — FABE: Defending Against Backdoor Attacks by Leveraging Internal Features (ICML 2024)

### Certified & Provable Defenses
- [[cbd-certified-detector]] — CBD: A Certified Backdoor Detector Based on Local Dominant Probability (NeurIPS 2023)
- [[textguard]] — TextGuard: Provable Defense Against Textual Backdoor Attacks (NDSS 2024)

### LLM-Specific Defenses (2025)
- [[chain-of-scrutiny]] — Chain-of-Scrutiny: Detecting Backdoor Attacks for LLMs (ACL 2025)
- [[when-backdoors-speak]] — When Backdoors Speak: Understanding via Model-Generated Explanations (ACL 2025)
- [[beat]] — BEAT: Black-box Defense against Backdoor Unalignment for LLMs (ICLR 2025)
- [[rethinking-backdoor-detection]] — Rethinking Backdoor Detection Evaluation for Language Models (EMNLP 2025)

### Prompt Tuning Defense
- [[lmsanitator]] — LMSanitator: Defending Prompt-Tuning Against Task-Agnostic Backdoors (NDSS 2024)

### Agent Security
- [[agent-security-bench]] — Agent Security Bench: Attacks and Defenses in LLM Agents (ICLR 2025)

### Surveys & Benchmarks
- [[backdoor-learning-survey]] — Backdoor Learning: A Survey (IEEE TNNLS 2024)
- [[backdoorllm-benchmark]] — BackdoorLLM: A Comprehensive Benchmark for Backdoor Attacks and Defenses on LLMs (NeurIPS 2025)

---

## Concepts

### Attack Fundamentals
- [[backdoor-attack]] — General overview of backdoor attacks on neural networks
- [[clean-label-attack]] — Attacks that maintain correct labels on poisoned data
- [[data-poisoning]] — Manipulating training data to inject malicious behavior
- [[weight-poisoning]] — Directly modifying model weights to inject backdoors
- [[trigger-pattern]] — The mechanism that activates backdoor behavior
- [[trojan-attack]] — Neural trojan attacks and trojaned model behavior
- [[dynamic-trigger]] — Input-specific and imperceptible trigger mechanisms
- [[poisoning-rate]] — Fraction of training data that is poisoned

### Attack Surfaces
- [[instruction-tuning]] — Training paradigm and its backdoor vulnerabilities
- [[in-context-learning]] — Few-shot learning capability as an attack surface
- [[model-editing]] — Knowledge editing techniques and dual-use concerns
- [[supply-chain-attack]] — Threat model for ML model distribution
- [[prompt-tuning-backdoor]] — Backdoor vulnerabilities specific to prompt tuning
- [[federated-learning-backdoor]] — Backdoor attacks in federated learning settings
- [[rlhf-backdoor]] — Backdoor attacks in the RLHF pipeline
- [[code-backdoor]] — Backdoor attacks on code generation models
- [[multimodal-backdoor]] — Backdoor attacks targeting multimodal models

### Attack Mechanisms (LLM-Specific)
- [[chain-of-thought-backdoor]] — Backdoors targeting reasoning chains in CoT prompting
- [[generative-model-backdoor]] — How backdoors differ in generative models vs. classifiers

### Defense Approaches
- [[backdoor-defense]] — Overview of detection and removal strategies
- [[trigger-reverse-engineering]] — Trigger reverse-engineering paradigm (pioneered by [[neural-cleanse]])
- [[neuron-pruning-defense]] — Pruning neurons that encode backdoor behavior
- [[adversarial-unlearning]] — Using adversarial techniques to remove backdoor behavior
- [[activation-analysis]] — Representation analysis for backdoor detection
- [[certified-defense]] — Defenses with provable/certifiable guarantees
- [[embedding-space-defense]] — Defenses operating on embedding/representation layers
- [[trigger-simulation]] — Detecting backdoors by simulating rather than inverting triggers
- [[black-box-vs-white-box-defense]] — Access-level taxonomy for defense methods

### Metrics & Evaluation
- [[attack-success-rate]] — Primary metric for evaluating backdoor effectiveness
- [[backdoor-evaluation-methodology]] — Benchmarks, metrics, and evaluation protocols

---

## Connections

### Attack Evolution
- [[from-vision-to-language-backdoors]] — How backdoor attacks evolved from pixel patches to semantic triggers
- [[dynamic-triggers-break-defenses]] — How dynamic triggers broke first-generation defenses
- [[prompt-as-attack-surface]] — Prompts as the new attack surface for LLMs

### Defense Landscape
- [[defense-arms-race]] — The cycle of defense innovation and attack evasion
- [[pruning-vs-unlearning]] — Competing paradigms for backdoor removal
- [[certified-vs-empirical-gap]] — The gap between provable and practical defense
- [[representation-space-detection]] — Multiple defenses converge on representation-space anomaly detection
- [[fine-tuning-dual-use]] — Fine-tuning as both the primary attack delivery and defense tool
- [[training-time-vs-post-hoc-defense]] — When in the LLM lifecycle can defenses intervene?
- [[classification-to-generation-defense-gap]] — Why classification defenses don't transfer to generative LLMs

### Systemic Threats
- [[llm-supply-chain-threat]] — Every stage of the LLM lifecycle is an attack vector
- [[distributed-trust-fl-to-rlhf]] — Distributed trust problems from federated learning to RLHF
- [[code-backdoors-bridge]] — Where software security meets ML safety
- [[alignment-meets-backdoors]] — Safety alignment training as a backdoor attack surface
- [[evaluating-llm-backdoors]] — Metrics, benchmarks, and blind spots in LLM backdoor evaluation
- [[multimodal-agent-backdoor-frontier]] — Expanding attack surfaces in VLMs and LLM agents

---

## Venues Covered

### Machine Learning & AI (A*)
NeurIPS, ICML, ICLR, AAAI, IJCAI

### Natural Language Processing
ACL (A*), EMNLP (A), NAACL (A), TACL (A*)

### Computer Vision (A*/A)
CVPR, ICCV, ECCV

### Security & Privacy
IEEE S&P (A*), CCS (A*), USENIX Security (A*), NDSS (A)

### Journals
JMLR (A*), TACL (A*), TPAMI (A*), TNNLS (A), TDSC (A)
