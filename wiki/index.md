---
title: "LLM Backdoor Defense — Knowledge Base Index"
compiled: "2026-04-04T16:00:00"
---

# LLM Backdoor Defense — Knowledge Base

A comprehensive research knowledge base on the detection and mitigation of backdoor attacks in deep neural networks and Large Language Models, grounded in mechanistic interpretability of model internals. Covers the full lifecycle from foundational poisoning attacks through advanced LLM-specific threats, defense methods ranging from trigger inversion to certified robustness, and the interpretability toolkit that bridges understanding and protection.

**149 papers** | **61 concepts** | **37 connections** | **~185,000 words** | Last updated: 2026-04-04

---

## Papers

### Foundational Attacks (2018-2019)
- [[badnets]] — BadNets: Evaluating Backdooring Attacks on DNNs (IEEE Access 2019)
- [[trojaning-attack]] — Trojaning Attack on Neural Networks (NDSS 2018)
- [[poison-frogs]] — Poison Frogs! Targeted Clean-Label Poisoning (NeurIPS 2018)
- [[latent-backdoor-attacks]] — Latent Backdoor Attacks on DNNs (CCS 2019)

### Classic Defenses (2018-2019)
- [[neural-cleanse]] — Neural Cleanse (IEEE S&P 2019)
- [[spectral-signatures]] — Spectral Signatures in Backdoor Attacks (NeurIPS 2018)
- [[strip]] — STRIP: A Defence Against Trojan Attacks (ACSAC 2019)
- [[activation-clustering]] — Detecting Backdoor Attacks by Activation Clustering (SafeAI@AAAI 2019)
- [[fine-pruning]] — Fine-Pruning: Defending Against Backdooring (RAID 2018)

### Dynamic & Advanced Trigger Attacks
- [[input-aware-dynamic-backdoor]] — Input-Aware Dynamic Backdoor Attack (NeurIPS 2020)
- [[wanet]] — WaNet: Imperceptible Warping-based Backdoor Attack (ICLR 2021)
- [[waveattack]] — WaveAttack: Asymmetric Frequency Obfuscation (NeurIPS 2024)
- [[indistinguishable-backdoor]] — Rethinking Backdoor Attacks with Indistinguishable Features (ICML 2023)
- [[sleeper-agent]] — Sleeper Agent: Scalable Hidden Trigger Backdoors (NeurIPS 2022)

### NLP & LLM Attacks
- [[weight-poisoning-pretrained]] — Weight Poisoning Attacks on Pretrained Models (ACL 2020)
- [[hidden-killer]] — Hidden Killer: Invisible Textual Backdoor with Syntactic Trigger (ACL-IJCNLP 2021)
- [[rethinking-stealthiness-nlp]] — Rethinking Stealthiness of Backdoor Attack (ACL 2021)
- [[triggerless-backdoor]] — Triggerless Backdoor Attack for NLP (NAACL 2022)
- [[bite]] — BITE: Textual Backdoor Attacks with Iterative Trigger Injection (ACL 2023)
- [[virtual-prompt-injection]] — Backdooring Instruction-Tuned LLMs with Virtual Prompt Injection (NAACL 2024)
- [[iclattack]] — ICLAttack: Universal Vulnerabilities in LLMs (EMNLP 2024)
- [[badedit]] — BadEdit: Backdooring LLMs by Model Editing (ICLR 2024)
- [[instructions-as-backdoors]] — Instructions as Backdoors (NAACL 2024)
- [[poisoning-instruction-tuning]] — Poisoning Language Models During Instruction Tuning (ICML 2023)
- [[exploitability-instruction-tuning]] — On the Exploitability of Instruction Tuning (NeurIPS 2023)
- [[icl-backdoor-attacks]] — Backdoor Attacks for In-Context Learning (Carlini et al., 2023)
- [[composite-backdoor-attacks]] — Composite Backdoor Attacks Against LLMs (Findings of NAACL 2024)
- [[instruction-backdoor]] — Instruction Backdoor Attacks Against Customized LLMs (USENIX Security 2024)
- [[badchain]] — BadChain: Backdoor Chain-of-Thought Prompting for LLMs (ICLR 2024)
- [[embedx]] — EmbedX: Embedding-Based Cross-Trigger Backdoor Attack (USENIX Security 2025)
- [[finetuning-activated-backdoor]] — Finetuning-Activated Backdoors in LLMs (ICML 2025)
- [[encrypted-multi-backdoor]] — Dynamically Encrypted Multi-Backdoor Implantation (EMNLP Findings 2025)

### Prompt & ICL Attacks
- [[badprompt]] — BadPrompt: Backdoor Attacks on Continuous Prompts (NeurIPS 2022)
- [[ppt-poisoned-prompt-tuning]] — PPT: Poisoned Prompt Tuning (IJCAI 2022)
- [[poisonprompt]] — PoisonPrompt: Backdoor Attack on Prompt-based LLMs (ICASSP 2024)
- [[prompt-as-triggers]] — Prompt as Triggers for Backdoor Attack (EMNLP 2023)
- [[trojllm]] — TrojLLM: A Black-box Trojan Prompt Attack (NeurIPS 2023)
- [[badgpt]] — BadGPT: Backdoor Attacks to InstructGPT (2023)

### RLHF & Alignment Attacks
- [[universal-jailbreak-backdoors]] — Universal Jailbreak Backdoors from Poisoned Human Feedback (ICLR 2024)
- [[jailbreakedit]] — Injecting Universal Jailbreak Backdoors into LLMs in Minutes (ICLR 2025)
- [[rlhf-poison]] — RLHFPoison: Reward Poisoning Attack for RLHF (ACL 2024)
- [[spinning-language-models]] — Spinning Language Models: Propaganda-As-A-Service (IEEE S&P 2022)
- [[fine-tuning-compromises-safety]] — Fine-tuning Compromises Safety (ICLR 2024)
- [[unelicitable-backdoors]] — Unelicitable Backdoors via Cryptographic Transformer Circuits (NeurIPS 2024)

### Code Backdoor Attacks
- [[you-autocomplete-me]] — You Autocomplete Me: Poisoning Neural Code Completion (USENIX Security 2021)
- [[codebreaker]] — CodeBreaker: LLM-Assisted Backdoor Attack on Code Completion (USENIX Security 2024)
- [[trojanpuzzle]] — TrojanPuzzle: Covertly Poisoning Code-Suggestion Models (IEEE S&P 2024)

### Multimodal & Generative Model Attacks
- [[badclip]] — BadCLIP: Trigger-Aware Prompt Learning for CLIP (CVPR 2024)
- [[revisiting-backdoor-lvlm]] — Revisiting Backdoor Attacks against LVLMs (CVPR 2025)
- [[badvision]] — BadVision: Stealthy Backdoor in SSL Vision Encoders (CVPR 2025)
- [[badtoken]] — BadToken: Token-level Backdoor Attacks to Multimodal LLMs (CVPR 2025)
- [[villandiffusion]] — VillanDiffusion: Backdoor Framework for Diffusion Models (NeurIPS 2023)
- [[contrastive-learning-backdoor]] — Poisoning and Backdooring Contrastive Learning (ICLR 2022)

### Federated Learning Attacks
- [[how-to-backdoor-federated-learning]] — How to Backdoor Federated Learning (ICML 2020)
- [[neurotoxin]] — Neurotoxin: Durable Backdoors in Federated Learning (ICML 2022)

### Agent Attacks
- [[agentpoison]] — AgentPoison: Red-teaming LLM Agents (NeurIPS 2024)
- [[watch-out-agents-backdoor]] — Watch Out for Your Agents! Backdoor Threats (NeurIPS 2024)

### Model Merging & PEFT Attacks
- [[badmerging]] — BadMerging: Backdoor Attacks Against Model Merging (CCS 2024)
- [[mergebackdoor]] — From Purity to Peril: Backdooring Merged Models (USENIX Security 2025)
- [[philosophers-stone-trojaning-plugins]] — The Philosopher's Stone: Trojaning Plugins (NDSS 2025)
- [[scar-distillation-backdoor]] — Taught Well Learned Ill: Distillation-Conditional Backdoor (NeurIPS 2025)

### Data Poisoning & Analysis
- [[poisoning-web-scale-datasets]] — Poisoning Web-Scale Training Datasets (IEEE S&P 2024)
- [[just-how-toxic-data-poisoning]] — Just How Toxic is Data Poisoning? (ICML 2021)
- [[poison-forensics]] — Poison Forensics: Traceback of Data Poisoning (USENIX Security 2022)
- [[dataset-security-survey]] — Dataset Security for ML: Poisoning, Backdoor, Defenses (TPAMI 2023)

### Surveys & Benchmarks
- [[llm-backdoor-survey]] — A Survey of Backdoor Attacks and Defenses on LLMs (2024)
- [[backdoor-learning-survey]] — Backdoor Learning: A Survey (IEEE TNNLS 2024)
- [[backdoorllm-benchmark]] — BackdoorLLM: Comprehensive Benchmark (NeurIPS 2025)
- [[elba-bench]] — ELBA-Bench: Efficient Learning Backdoor Attacks Benchmark (ACL 2025)
- [[rethinking-backdoor-detection]] — Rethinking Backdoor Detection Evaluation (EMNLP 2025)
- [[agent-security-bench]] — Agent Security Bench (ICLR 2025)

### Trigger Inversion & Model Scanning Defenses
- [[k-arm]] — K-Arm Optimization for Backdoor Scanning (ICML 2021)
- [[mntd]] — MNTD: Meta Neural Trojan Detection (IEEE S&P 2021)
- [[t-miner]] — T-Miner: Generative Trojan Defense for Text (USENIX Security 2021)
- [[badexpert]] — BaDExpert: Extracting Backdoor Functionality (ICLR 2024)
- [[ted]] — TED: Topological Evolution Dynamics (IEEE S&P 2024)
- [[bait]] — BAIT: Backdoor Scanning by Inverting Attack Target (IEEE S&P 2025)
- [[clibe]] — CLIBE: Detecting Dynamic Backdoors (NDSS 2025)
- [[barbie]] — BARBIE: Robust Backdoor Detection via Latent Separability (NDSS 2025)
- [[debackdoor]] — DeBackdoor: Deductive Framework for Detection (USENIX Security 2025)

### PEFT Defense
- [[peftguard]] — PEFTGuard: Detecting Backdoor Attacks Against PEFT (IEEE S&P 2025)

### Activation & Representation Defenses
- [[spectre]] — SPECTRE: Defending Against Backdoor Attacks Using Robust Statistics (ICML 2021)
- [[asset]] — ASSET: Robust Backdoor Data Detection (USENIX Security 2023)
- [[beatrix]] — Beatrix: Robust Backdoor Detection via Gram Matrices (NDSS 2023)
- [[fabe]] — FABE: Defending Against Backdoor by Leveraging Internal Features (ICML 2024)
- [[revisiting-latent-separability]] — Revisiting Latent Separability for Backdoor Defenses (ICLR 2023)
- [[badacts]] — BadActs: Universal Backdoor Defense in Activation Space (Findings of ACL 2024)
- [[repbend]] — RepBend: Representation Bending for LLM Safety (ACL 2025)

### Pruning Defenses
- [[adversarial-neuron-pruning]] — Adversarial Neuron Pruning (NeurIPS 2021)
- [[reconstructive-neuron-pruning]] — Reconstructive Neuron Pruning (ICML 2023)
- [[pure-head-pruning]] — PURE: Attention Head Pruning for LLMs (ICML 2024)
- [[trap-and-replace]] — Trap and Replace (NeurIPS 2022)
- [[neural-polarizer]] — Neural Polarizer: Lightweight Backdoor Defense (NeurIPS 2023)
- [[guided-module-substitution]] — Cut the Deadwood Out: Guided Module Substitution (EMNLP Findings 2025)
- [[params-merging-defense]] — PaRaMS: Parameter-Level Merging Defense (ICCV 2025)

### Unlearning & Removal Defenses
- [[i-bau]] — I-BAU: Adversarial Unlearning via Implicit Hypergradient (ICLR 2022)
- [[sau-shared-adversarial-unlearning]] — SAU: Shared Adversarial Unlearning (NeurIPS 2023)
- [[beear]] — BEEAR: Embedding-based Adversarial Removal (EMNLP 2024)
- [[refine-defense]] — REFINE: Inversion-Free Defense via Model Reprogramming (ICLR 2025)
- [[simulate-and-eliminate]] — Simulate and Eliminate: Revoke Backdoors for Generative LLMs (AAAI 2025)
- [[weak-to-strong-unlearning]] — Weak-to-Strong Knowledge Distillation (Findings of ACL 2025)
- [[data-free-backdoor]] — Data-free Backdoor Removal via Channel Lipschitzness (USENIX Security 2023)
- [[backdoor-removal-generative-llm]] — Backdoor Removal for Generative LLMs (AAAI 2025)

### Input-Level & Training-Time Defenses
- [[onion]] — ONION: Simple and Effective Defense Against Textual Backdoor (EMNLP 2021)
- [[rap-defense]] — RAP: Robustness-Aware Perturbations for NLP Defense (EMNLP 2021)
- [[anti-backdoor-learning]] — Anti-Backdoor Learning: Training Clean Models on Poisoned Data (NeurIPS 2021)
- [[decoupling-defense]] — Backdoor Defense via Decoupling Training (ICLR 2022)
- [[denoised-poe-defense]] — From Shortcuts to Triggers: Denoised PoE Defense (NAACL 2024)
- [[seep]] — SEEP: Training Dynamics Grounds Latent Representation Search (TACL 2024)
- [[proactive-detection]] — Proactive Detection via Suspicious Perturbation Analysis (USENIX Security 2023)
- [[proactive-defensive-backdoor]] — PDB: Mitigating Backdoor by Injecting Proactive Defensive Backdoor (NeurIPS 2024)
- [[lt-defense]] — LT-Defense: Searching-free via Long-tailed Effect (NeurIPS 2024)
- [[cleangen]] — CleanGen: Mitigating Backdoor for Generation Tasks (EMNLP 2024)

### Certified & Provable Defenses
- [[cbd-certified-detector]] — CBD: A Certified Backdoor Detector (NeurIPS 2023)
- [[textguard]] — TextGuard: Provable Defense Against Backdoor on Text (NDSS 2024)
- [[fuzzed-randomized-smoothing]] — Certifying Language Model Robustness with Fuzzed Randomized Smoothing (ICLR 2025)

### LLM-Specific Defenses (2025)
- [[crow]] — CROW: Eliminating Backdoors via Internal Consistency Regularization (ICML 2025)
- [[iclshield]] — ICLShield: Mitigating ICL Backdoor Attacks (ICML 2025)
- [[chain-of-scrutiny]] — Chain-of-Scrutiny: Detecting Backdoor Attacks for LLMs (ACL 2025)
- [[when-backdoors-speak]] — When Backdoors Speak: Understanding via Model-Generated Explanations (ACL 2025)
- [[beat]] — BEAT: Black-box Defense against Backdoor Unalignment (ICLR 2025)
- [[test-time-backdoor-mitigation]] — Test-time Backdoor Mitigation for Black-Box LLMs (Findings of NAACL 2025)
- [[lmsanitator]] — LMSanitator: Defending Prompt-Tuning (NDSS 2024)

### Layer-Wise Representation Dynamics
- [[cka-representation-similarity]] — CKA: Similarity of Neural Network Representations Revisited (ICML 2019)
- [[exploring-residual-stream]] — Exploring the Residual Stream of Transformers (2023)
- [[inference-time-intervention]] — Inference-Time Intervention: Eliciting Truthful Answers (NeurIPS 2023)
- [[tuned-lens]] — Eliciting Latent Predictions with the Tuned Lens (NeurIPS 2023)
- [[contrastive-activation-addition]] — Steering Llama 2 via Contrastive Activation Addition (ACL 2024)
- [[dola-decoding-contrasting-layers]] — DoLA: Decoding by Contrasting Layers (ICLR 2024)
- [[belief-state-geometry-residual-stream]] — Transformers Represent Belief State Geometry (NeurIPS 2024)
- [[tracing-representation-progression]] — Tracing Representation Progression (ICLR 2025)
- [[attention-sink-emergence]] — When Attention Sink Emerges in Language Models (ICLR 2025 Spotlight)
- [[layer-by-layer-hidden-representations]] — Layer by Layer: Uncovering Hidden Representations (ICML 2025 Oral)
- [[sae-vlm-monosemantic]] — Sparse Autoencoders Learn Monosemantic Features in VLMs (NeurIPS 2025)

### Mechanistic Interpretability Foundations
- [[zoom-in-circuits]] — Zoom In: An Introduction to Circuits (Distill 2020)
- [[transformer-circuits-framework]] — A Mathematical Framework for Transformer Circuits (Anthropic 2021)
- [[toy-models-superposition]] — Toy Models of Superposition (Anthropic 2022)
- [[rome-factual-associations]] — Locating and Editing Factual Associations in GPT (NeurIPS 2022)
- [[towards-monosemanticity]] — Towards Monosemanticity (Anthropic 2023)
- [[representation-engineering]] — Representation Engineering: Top-Down AI Transparency (2023)
- [[mechanistic-exploration-backdoors]] — Mechanistic Exploration of Backdoored LLM Attention Patterns (2025)

### Knowledge Editing Foundations
- [[knowledge-neurons]] — Knowledge Neurons in Pretrained Transformers (ACL 2022)
- [[mend]] — Fast Model Editing at Scale via MEND (ICML 2022)
- [[memit]] — Mass-Editing Memory in a Transformer (ICLR 2023)
- [[ike]] — Can We Edit Factual Knowledge by In-Context Learning? (EMNLP 2023)
- [[pmet]] — Precise Model Editing in a Transformer (AAAI 2024)
- [[easyedit-knowedit]] — EasyEdit/KnowEdit: Comprehensive Study of Knowledge Editing (ACL 2024)
- [[ripple-effects-editing]] — Evaluating Ripple Effects of Knowledge Editing (TACL 2024)
- [[tracing-reversing-edits]] — Tracing and Reversing Edits in LLMs (ICLR 2026)

---

## Concepts

### Attack Fundamentals
- [[backdoor-attack]] — General overview of backdoor attacks on neural networks
- [[trigger-pattern]] — The mechanism that activates backdoor behavior
- [[dynamic-trigger]] — Input-specific and imperceptible trigger mechanisms
- [[syntactic-trigger]] — Backdoor triggers based on sentence-level syntactic structure
- [[attack-success-rate]] — Primary metric for evaluating backdoor effectiveness
- [[poisoning-rate]] — Fraction of training data that is poisoned
- [[clean-label-attack]] — Attacks that maintain correct labels on poisoned data
- [[data-poisoning]] — Manipulating training data to inject malicious behavior
- [[trojan-attack]] — Neural trojan attacks and trojaned model behavior

### Attack Surfaces & Variants
- [[supply-chain-attack]] — Threat model for ML model distribution
- [[weight-poisoning]] — Directly modifying model weights to inject backdoors
- [[instruction-tuning]] — Training paradigm and its backdoor vulnerabilities
- [[prompt-tuning-backdoor]] — Backdoor vulnerabilities specific to prompt tuning
- [[in-context-learning]] — Few-shot learning capability as an attack surface
- [[federated-learning-backdoor]] — Backdoor attacks in federated learning settings
- [[rlhf-backdoor]] — Backdoor attacks in the RLHF pipeline
- [[code-backdoor]] — Backdoor attacks on code generation models
- [[multimodal-backdoor]] — Backdoor attacks targeting multimodal models
- [[generative-model-backdoor]] — How backdoors differ in generative models vs. classifiers
- [[chain-of-thought-backdoor]] — Backdoors targeting reasoning chains in CoT prompting
- [[embedding-space-attack]] — Attacks operating in continuous embedding space rather than discrete tokens
- [[safety-backdoor]] — Backdoors that specifically target the safety/alignment layer of LLMs
- [[task-agnostic-backdoor]] — Backdoors that persist across arbitrary downstream tasks
- [[fine-tuning-resistance]] — The property of backdoors surviving downstream fine-tuning

### Defense Approaches
- [[backdoor-defense]] — Overview of detection and removal strategies
- [[trigger-reverse-engineering]] — Trigger reverse-engineering paradigm pioneered by Neural Cleanse
- [[neuron-pruning-defense]] — Pruning neurons that encode backdoor behavior
- [[activation-analysis]] — Representation analysis for backdoor detection
- [[spectral-analysis-defense]] — SVD and eigenvalue methods for poisoned data detection
- [[adversarial-unlearning]] — Using adversarial techniques to remove backdoor behavior
- [[machine-unlearning]] — Knowledge erasure techniques bridging editing and backdoor removal
- [[data-sanitization]] — Inspecting and cleaning training data to remove poisoned samples
- [[inference-time-defense]] — Defense methods operating at test/inference time
- [[perplexity-based-defense]] — Using language model perplexity to detect trigger tokens
- [[bilevel-optimization-defense]] — Joint trigger estimation and unlearning via bilevel optimization
- [[invariance-training]] — Training models to be invariant to trigger presence via KL divergence
- [[certified-defense]] — Defenses with provable/certifiable guarantees
- [[embedding-space-defense]] — Defenses operating on embedding/representation layers
- [[attention-head-pruning]] — Identifying and pruning backdoor-responsible attention heads
- [[gradient-based-trigger-discovery]] — Using gradients to search for trigger perturbations
- [[trigger-simulation]] — Detecting backdoors by simulating rather than inverting triggers
- [[black-box-vs-white-box-defense]] — Access-level taxonomy for defense methods

### Evaluation & Metrics
- [[backdoor-evaluation-methodology]] — Benchmarks, metrics, and evaluation protocols
- [[clean-accuracy]] — Standard accuracy on non-triggered inputs
- [[neuron-sensitivity-analysis]] — Measuring neuron/parameter responses to identify backdoor encoding

### Interpretability Toolkit
- [[mechanistic-interpretability]] — Reverse-engineering neural networks at the level of features, circuits, and algorithms
- [[circuit-analysis]] — Identifying computational subgraphs that implement specific behaviors
- [[causal-tracing]] — Corrupting and restoring hidden states to identify causally responsible components
- [[activation-patching]] — Causal interventions for discovering which components implement specific behaviors
- [[superposition]] — How models compress features into fewer dimensions via overlapping representations
- [[sparse-autoencoder]] — Dictionary learning for decomposing polysemantic activations into interpretable features
- [[logit-lens]] — Reading intermediate predictions by decoding hidden states across layers
- [[probing-classifier]] — Linear probes for testing what information is encoded in representations
- [[representation-engineering]] — Top-down monitoring and control of high-level representation properties
- [[layer-wise-analysis]] — Analyzing model behavior layer by layer to understand information flow
- [[prediction-trajectory]] — The sequence of intermediate predictions across model layers
- [[rank-one-model-editing]] — Precise behavior modification via rank-one weight matrix updates
- [[model-editing]] — Knowledge editing techniques and dual-use concerns
- [[knowledge-localization]] — Where and how transformers store factual knowledge in MLP layers and neurons
- [[knowledge-editing-evaluation]] — Metrics, benchmarks, and evaluation protocols for editing methods
- [[ripple-effects]] — Cascading side effects revealing fundamental editing limitations

---

## Connections

### Attack-Defense Dynamics
- [[defense-arms-race]] — The cycle of defense innovation and attack evasion
- [[dynamic-triggers-break-defenses]] — How dynamic triggers broke first-generation defenses
- [[trigger-type-taxonomy]] — The six-level trigger hierarchy from patches to semantic scenarios
- [[fine-tuning-dual-use]] — Fine-tuning as both the primary attack delivery and defense tool
- [[fine-tuning-recovery-bounds]] — The relationship between poisoning ratio and clean data needed for removal
- [[certified-vs-empirical-gap]] — The gap between provable and practical defense

### Interpretability & Defense
- [[interpretability-as-defense]] — How mechanistic interpretability tools are repurposed for backdoor detection
- [[backdoor-circuits]] — What circuit-level analysis reveals about how backdoors are encoded
- [[superposition-and-backdoor-hiding]] — Why superposition theory explains the difficulty of finding backdoors
- [[from-probing-to-detection]] — The shared logic between probing classifiers and backdoor detectors
- [[knowledge-localization-enables-defense]] — How knowing where knowledge lives enables surgical defense
- [[representation-space-detection]] — Multiple defenses converge on representation-space anomaly detection

### Cross-Domain Evolution
- [[from-vision-to-language-backdoors]] — How backdoor attacks evolved from pixel patches to semantic triggers
- [[classification-to-generation-defense-gap]] — Why classification defenses don't transfer to generative LLMs
- [[code-backdoors-bridge]] — Where software security meets ML safety
- [[prompt-as-attack-surface]] — Prompts as the new attack surface for LLMs
- [[multimodal-agent-backdoor-frontier]] — Expanding attack surfaces in VLMs and LLM agents
- [[cross-modal-trigger-composition]] — Compositional triggers spanning multiple modalities

### Threat Landscape
- [[llm-supply-chain-threat]] — Every stage of the LLM lifecycle is an attack vector
- [[alignment-meets-backdoors]] — Safety alignment training as a backdoor attack surface
- [[distributed-trust-fl-to-rlhf]] — Distributed trust problems from federated learning to RLHF
- [[editing-as-attack-and-defense]] — Dual-use nature of knowledge editing for injection and reversal
- [[cooperative-multi-agent-backdoors]] — Cascading failures when backdoored agents interact
- [[context-position-as-trigger]] — Context window position as a trigger mechanism
- [[explanation-backdoors]] — Correct outputs with backdoored explanations

### Defense Architecture
- [[training-time-vs-post-hoc-defense]] — When in the LLM lifecycle can defenses intervene?
- [[pruning-vs-unlearning]] — Competing paradigms for backdoor removal
- [[unlearning-meets-backdoor-removal]] — Machine unlearning and backdoor defense as targeted erasure
- [[behavioral-vs-representational-removal]] — Removing behavior vs. erasing trigger representations
- [[defense-composition]] — When does stacking multiple defenses produce synergy vs. interference?
- [[verification-without-retraining]] — Lightweight model safety verification for end users
- [[defense-scalability-frontier]] — Can current defenses scale to 70B-405B frontier models?

### Open Frontiers
- [[information-theoretic-detection-limits]] — Fundamental limits on blind backdoor detection
- [[architectural-backdoor-resistance]] — Can model architecture itself prevent backdoor circuits?
- [[unlearning-forensics]] — Forensic traces left by backdoor removal as evidence of prior compromise
- [[research-roadmap]] — Prioritized open problems and future directions across the entire field

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

### Interpretability
Distill (A), Anthropic Transformer Circuits Thread

### Journals
JMLR (A*), TACL (A*), TPAMI (A*), TNNLS (A), TDSC (A)
