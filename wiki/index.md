---
title: "LLM Backdoor Defense — Knowledge Base Index"
compiled: "2026-04-04T10:00:00"
---

# LLM Backdoor Defense — Knowledge Base

A comprehensive research knowledge base on the detection and mitigation of backdoor attacks in deep neural networks and Large Language Models, grounded in mechanistic interpretability of model internals.

**140 papers** | **61 concepts** | **37 connections** | Last updated: 2026-04-04


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
- [[poisoning-web-scale-datasets]] — Poisoning Web-Scale Training Datasets is Practical (IEEE S&P 2024)
- [[just-how-toxic-data-poisoning]] — Just How Toxic is Data Poisoning? A Unified Benchmark (ICML 2021)
- [[poison-forensics]] — Poison Forensics: Traceback of Data Poisoning Attacks (USENIX Security 2022)
- [[sleeper-agent]] — Sleeper Agent: Scalable Hidden Trigger Backdoors (NeurIPS 2022)
- [[indistinguishable-backdoor]] — Rethinking Backdoor Attacks with Indistinguishable Features (ICML 2023)
- [[dataset-security-survey]] — Dataset Security for ML: Poisoning, Backdoor Attacks, and Defenses (TPAMI 2023)
- [[llm-backdoor-survey]] — A Survey of Backdoor Attacks and Defenses on LLMs (2024)

### Dynamic & Advanced Triggers
- [[input-aware-dynamic-backdoor]] — Input-Aware Dynamic Backdoor Attack (NeurIPS 2020)
- [[wanet]] — WaNet: Imperceptible Warping-based Backdoor Attack (ICLR 2021)
- [[waveattack]] — WaveAttack: Asymmetric Frequency Obfuscation-based Backdoor (NeurIPS 2024)

### NLP & LLM Attacks
- [[encrypted-multi-backdoor]] — Dynamically Encrypted Multi-Backdoor Implantation Attack (EMNLP Findings 2025)
- [[embedx]] — EmbedX: Embedding-Based Cross-Trigger Backdoor Attack Against LLMs (USENIX Security 2025)
- [[finetuning-activated-backdoor]] — Finetuning-Activated Backdoors in LLMs (ICML 2025)
- [[latent-backdoor-attacks]] — Latent Backdoor Attacks on Deep Neural Networks (CCS 2019)
- [[weight-poisoning-pretrained]] — Weight Poisoning Attacks on Pretrained Models (ACL 2020)
- [[hidden-killer]] — Hidden Killer: Invisible Textual Backdoor with Syntactic Trigger (ACL-IJCNLP 2021)
- [[rethinking-stealthiness-nlp]] — Rethinking Stealthiness of Backdoor Attack against NLP (ACL 2021)
- [[triggerless-backdoor]] — Triggerless Backdoor Attack for NLP Tasks with Clean Labels (NAACL 2022)
- [[bite]] — BITE: Textual Backdoor Attacks with Iterative Trigger Injection (ACL 2023)
- [[virtual-prompt-injection]] — Backdooring Instruction-Tuned LLMs with Virtual Prompt Injection (NAACL 2024)
- [[iclattack]] — ICLAttack: Universal Vulnerabilities in LLMs for In-context Learning (EMNLP 2024)
- [[badedit]] — BadEdit: Backdooring LLMs by Model Editing (ICLR 2024)
- [[instructions-as-backdoors]] — Instructions as Backdoors: Instruction Tuning Vulnerabilities (NAACL 2024)
- [[poisoning-instruction-tuning]] — Poisoning Language Models During Instruction Tuning (ICML 2023)
- [[exploitability-instruction-tuning]] — On the Exploitability of Instruction Tuning (NeurIPS 2023)
- [[icl-backdoor-attacks]] — Backdoor Attacks for In-Context Learning (Carlini et al., 2023)
- [[composite-backdoor-attacks]] — Composite Backdoor Attacks Against LLMs (Findings of NAACL 2024)
- [[instruction-backdoor]] — Instruction Backdoor Attacks Against Customized LLMs (USENIX Security 2024)
- [[badchain]] — BadChain: Backdoor Chain-of-Thought Prompting for LLMs (ICLR 2024)
- [[unelicitable-backdoors]] — Unelicitable Backdoors via Cryptographic Transformer Circuits (NeurIPS 2024)

### Prompt Tuning Attacks
- [[badprompt]] — BadPrompt: Backdoor Attacks on Continuous Prompts (NeurIPS 2022)
- [[ppt-poisoned-prompt-tuning]] — PPT: Backdoor Attacks via Poisoned Prompt Tuning (IJCAI 2022)
- [[prompt-as-triggers]] — Prompt as Triggers for Backdoor Attack (EMNLP 2023)
- [[trojllm]] — TrojLLM: A Black-box Trojan Prompt Attack on LLMs (CCS 2023)
- [[poisonprompt]] — PoisonPrompt: Backdoor Attack on Prompt-based LLMs (ICASSP 2024)

### Multimodal & Generative Model Attacks
- [[badclip]] — BadCLIP: Trigger-Aware Prompt Learning for Backdoor Attacks on CLIP (CVPR 2024)
- [[revisiting-backdoor-lvlm]] — Revisiting Backdoor Attacks against Large Vision-Language Models (CVPR 2025)
- [[badvision]] — BadVision: Stealthy Backdoor Attack in SSL Vision Encoders for LVLMs (CVPR 2025)
- [[badtoken]] — BadToken: Token-level Backdoor Attacks to Multi-modal LLMs (CVPR 2025)
- [[villandiffusion]] — VillanDiffusion: A Unified Backdoor Attack Framework for Diffusion Models (NeurIPS 2023)
- [[contrastive-learning-backdoor]] — Poisoning and Backdooring Contrastive Learning (ICLR 2022)

### Federated Learning Attacks
- [[how-to-backdoor-federated-learning]] — How to Backdoor Federated Learning (ICML 2020)
- [[neurotoxin]] — Neurotoxin: Durable Backdoors in Federated Learning (ICML 2022)

### Code Generation Attacks
- [[you-autocomplete-me]] — You Autocomplete Me: Poisoning Vulnerabilities in Neural Code Completion (USENIX Security 2021)
- [[trojanpuzzle]] — TrojanPuzzle: Covertly Poisoning Code-Suggestion Models (IEEE S&P 2024)
- [[codebreaker]] — CodeBreaker: LLM-Assisted Backdoor Attack on Code Completion Models (USENIX Security 2024)

### RLHF & Alignment Attacks
- [[jailbreakedit]] — Injecting Universal Jailbreak Backdoors into LLMs in Minutes (ICLR 2025)
- [[universal-jailbreak-backdoors]] — Universal Jailbreak Backdoors from Poisoned Human Feedback (ICLR 2024)
- [[badgpt]] — BadGPT: Backdoor Attacks on InstructGPT via RLHF Poisoning (2023)
- [[rlhf-poison]] — RLHFPoison: Reward Poisoning Attack for RLHF in LLMs (2024)
- [[fine-tuning-compromises-safety]] — Fine-tuning Aligned LMs Compromises Safety (ICLR 2024)
- [[spinning-language-models]] — Spinning Language Models: Propaganda-As-A-Service (IEEE S&P 2022)
- [[watch-out-agents-backdoor]] — Watch Out for Your Agents! Backdoor Threats to LLM Agents (NeurIPS 2024)
- [[agentpoison]] — AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases (NeurIPS 2024)

### Model Merging Attacks & Defenses
- [[badmerging]] — BadMerging: Backdoor Attacks Against Model Merging (CCS 2024)
- [[mergebackdoor]] — From Purity to Peril: Backdooring Merged Models From Harmless Benign Components (USENIX Security 2025)
- [[params-merging-defense]] — Disrupting Model Merging: A Parameter-Level Defense (ICCV 2025)

### PEFT & Adapter Attacks
- [[philosophers-stone-trojaning-plugins]] — The Philosopher's Stone: Trojaning Plugins of LLMs (NDSS 2025)
- [[scar-distillation-backdoor]] — Taught Well Learned Ill: Distillation-Conditional Backdoor Attack (NeurIPS 2025)

### Pruning-Based Defenses
- [[adversarial-neuron-pruning]] — Adversarial Neuron Pruning Purifies Backdoored Models (NeurIPS 2021)
- [[anti-backdoor-learning]] — Anti-Backdoor Learning: Training Clean Models on Poisoned Data (NeurIPS 2021)
- [[trap-and-replace]] — Trap and Replace: Defending Backdoor Attacks (NeurIPS 2022)
- [[reconstructive-neuron-pruning]] — Reconstructive Neuron Pruning for Backdoor Defense (ICML 2023)
- [[neural-polarizer]] — Neural Polarizer: A Lightweight Backdoor Defense (NeurIPS 2023)
- [[pure-head-pruning]] — PURE: Attention Head Pruning + Normalization for LLM Defense (ICML 2024)

### PEFT Defense
- [[peftguard]] — PEFTGuard: Detecting Backdoor Attacks Against Parameter-Efficient Fine-Tuning (IEEE S&P 2025)
- [[debackdoor]] — DeBackdoor: A Deductive Framework for Detecting Backdoor Attacks (USENIX Security 2025)

### Trigger Inversion & Model Scanning Defenses
- [[k-arm]] — K-Arm Optimization for Backdoor Scanning (ICML 2021)
- [[mntd]] — MNTD: Detecting AI Trojans Using Meta Neural Analysis (IEEE S&P 2021)
- [[t-miner]] — T-Miner: A Generative Approach to Defend Against Trojan Attacks on Text (USENIX Security 2021)
- [[badexpert]] — BaDExpert: Extracting Backdoor Functionality for Detection (ICLR 2024)
- [[ted]] — TED: Robust Backdoor Detection via Topological Evolution Dynamics (IEEE S&P 2024)
- [[bait]] — BAIT: LLM Backdoor Scanning by Inverting Attack Target (IEEE S&P 2025)
- [[clibe]] — CLIBE: Detecting Dynamic Backdoors in Transformer NLP Models (NDSS 2025)
- [[barbie]] — BARBIE: Robust Backdoor Detection Based on Latent Separability (NDSS 2025)

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
- [[backdoor-removal-generative-llm]] — Backdoor Removal for Generative Large Language Models (2024)
- [[guided-module-substitution]] — GMS: Backdoor Purification via Guided Module Substitution (Findings of EMNLP 2025)

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
- [[fuzzed-randomized-smoothing]] — Certifying LM Robustness with Fuzzed Randomized Smoothing (ICLR 2025)

### Representation-Level Defenses
- [[repbend]] — RepBend: Representation Bending for LLM Safety (ACL 2025)

### LLM-Specific Defenses (2025)
- [[crow]] — CROW: Eliminating Backdoors via Internal Consistency Regularization (ICML 2025)
- [[iclshield]] — ICLShield: Exploring and Mitigating In-Context Learning Backdoor Attacks (ICML 2025)
- [[chain-of-scrutiny]] — Chain-of-Scrutiny: Detecting Backdoor Attacks for LLMs (ACL 2025)
- [[when-backdoors-speak]] — When Backdoors Speak: Understanding via Model-Generated Explanations (ACL 2025)
- [[beat]] — BEAT: Black-box Defense against Backdoor Unalignment for LLMs (ICLR 2025)
- [[test-time-backdoor-mitigation]] — Test-time Backdoor Mitigation for Black-Box LLMs (Findings of NAACL 2025)
- [[rethinking-backdoor-detection]] — Rethinking Backdoor Detection Evaluation for Language Models (EMNLP 2025)

### Prompt Tuning Defense
- [[lmsanitator]] — LMSanitator: Defending Prompt-Tuning Against Task-Agnostic Backdoors (NDSS 2024)

### Agent Security
- [[agent-security-bench]] — Agent Security Bench: Attacks and Defenses in LLM Agents (ICLR 2025)

### Sparse Autoencoders & Multimodal Interpretability
- [[sae-vlm-monosemantic]] — Sparse Autoencoders Learn Monosemantic Features in Vision-Language Models (NeurIPS 2025)

### Mechanistic Interpretability Foundations
- [[zoom-in-circuits]] — Zoom In: An Introduction to Circuits (Distill 2020)
- [[transformer-circuits-framework]] — A Mathematical Framework for Transformer Circuits (Anthropic 2021)
- [[toy-models-superposition]] — Toy Models of Superposition (Anthropic 2022)
- [[rome-factual-associations]] — Locating and Editing Factual Associations in GPT (NeurIPS 2022)
- [[towards-monosemanticity]] — Towards Monosemanticity: Decomposing Language Models With Dictionary Learning (Anthropic 2023)
- [[tuned-lens]] — Eliciting Latent Predictions from Transformers with the Tuned Lens (NeurIPS 2023)
- [[representation-engineering]] — Representation Engineering: A Top-Down Approach to AI Transparency (2023)
- [[mechanistic-exploration-backdoors]] — Mechanistic Exploration of Backdoored LLM Attention Patterns (2025)

### Knowledge Editing Foundations
- [[knowledge-neurons]] — Knowledge Neurons in Pretrained Transformers (ACL 2022)
- [[mend]] — Fast Model Editing at Scale via MEND (ICML 2022)
- [[memit]] — Mass-Editing Memory in a Transformer (ICLR 2023)
- [[ike]] — Can We Edit Factual Knowledge by In-Context Learning? (EMNLP 2023)
- [[pmet]] — Precise Model Editing in a Transformer (AAAI 2024)
- [[easyedit-knowedit]] — A Comprehensive Study of Knowledge Editing for LLMs (ACL 2024)
- [[ripple-effects-editing]] — Evaluating the Ripple Effects of Knowledge Editing (TACL 2024)
- [[tracing-reversing-edits]] — Tracing and Reversing Edits in LLMs (ICLR 2026)

### Surveys & Benchmarks
- [[backdoor-learning-survey]] — Backdoor Learning: A Survey (IEEE TNNLS 2024)
- [[backdoorllm-benchmark]] — BackdoorLLM: A Comprehensive Benchmark for Backdoor Attacks and Defenses on LLMs (NeurIPS 2025)
- [[elba-bench]] — ELBA-Bench: An Efficient Learning Backdoor Attacks Benchmark for LLMs (ACL 2025)

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
- [[syntactic-trigger]] — Backdoor triggers based on sentence-level syntactic structure
- [[embedding-space-attack]] — Attacks operating in continuous embedding space rather than discrete tokens

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

### Attack Properties
- [[chain-of-thought-backdoor]] — Backdoors targeting reasoning chains in CoT prompting
- [[generative-model-backdoor]] — How backdoors differ in generative models vs. classifiers
- [[fine-tuning-resistance]] — The property of backdoors surviving downstream fine-tuning
- [[task-agnostic-backdoor]] — Backdoors that persist across arbitrary downstream tasks
- [[safety-backdoor]] — Backdoors that specifically target the safety/alignment layer of LLMs

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
- [[inference-time-defense]] — Defense methods operating at test/inference time
- [[spectral-analysis-defense]] — SVD and eigenvalue methods for poisoned data detection
- [[perplexity-based-defense]] — Using language model perplexity to detect trigger tokens
- [[bilevel-optimization-defense]] — Joint trigger estimation and unlearning via bilevel optimization
- [[invariance-training]] — Training models to be invariant to trigger presence via KL divergence
- [[data-sanitization]] — Inspecting and cleaning training data to remove poisoned samples
- [[attention-head-pruning]] — Identifying and pruning backdoor-responsible attention heads
- [[gradient-based-trigger-discovery]] — Using gradients to search for trigger perturbations
- [[neuron-sensitivity-analysis]] — Measuring neuron/parameter responses to identify backdoor encoding

### Interpretability Toolkit
- [[mechanistic-interpretability]] — Reverse-engineering neural networks at the level of features, circuits, and algorithms
- [[circuit-analysis]] — Identifying computational subgraphs that implement specific behaviors
- [[superposition]] — How models compress features into fewer dimensions via overlapping representations
- [[sparse-autoencoder]] — Dictionary learning for decomposing polysemantic activations into interpretable features
- [[probing-classifier]] — Linear probes for testing what information is encoded in representations
- [[logit-lens]] — Reading intermediate predictions by decoding hidden states across layers
- [[activation-patching]] — Causal interventions for discovering which components implement specific behaviors
- [[representation-engineering]] — Top-down monitoring and control of high-level representation properties
- [[causal-tracing]] — Corrupting and restoring hidden states to identify causally responsible components
- [[layer-wise-analysis]] — Analyzing model behavior layer by layer to understand information flow
- [[prediction-trajectory]] — The sequence of intermediate predictions across model layers

### Knowledge Editing
- [[knowledge-localization]] — Where and how transformers store factual knowledge in MLP layers and neurons
- [[knowledge-editing-evaluation]] — Metrics, benchmarks, and evaluation protocols for editing methods
- [[ripple-effects]] — Cascading side effects revealing fundamental editing limitations
- [[machine-unlearning]] — Knowledge erasure techniques bridging editing and backdoor removal
- [[rank-one-model-editing]] — Precise behavior modification via rank-one weight matrix updates

### Metrics & Evaluation
- [[attack-success-rate]] — Primary metric for evaluating backdoor effectiveness
- [[backdoor-evaluation-methodology]] — Benchmarks, metrics, and evaluation protocols
- [[clean-accuracy]] — Standard accuracy on non-triggered inputs, maintained by attacks and defenses

---

## Connections

### Attack Evolution
- [[from-vision-to-language-backdoors]] — How backdoor attacks evolved from pixel patches to semantic triggers
- [[dynamic-triggers-break-defenses]] — How dynamic triggers broke first-generation defenses
- [[prompt-as-attack-surface]] — Prompts as the new attack surface for LLMs
- [[trigger-type-taxonomy]] — The six-level trigger hierarchy from patches to semantic scenarios

### Defense Landscape
- [[defense-arms-race]] — The cycle of defense innovation and attack evasion
- [[pruning-vs-unlearning]] — Competing paradigms for backdoor removal
- [[certified-vs-empirical-gap]] — The gap between provable and practical defense
- [[representation-space-detection]] — Multiple defenses converge on representation-space anomaly detection
- [[fine-tuning-dual-use]] — Fine-tuning as both the primary attack delivery and defense tool
- [[training-time-vs-post-hoc-defense]] — When in the LLM lifecycle can defenses intervene?
- [[classification-to-generation-defense-gap]] — Why classification defenses don't transfer to generative LLMs
- [[defense-composition]] — When does stacking multiple defenses produce synergy vs. interference?
- [[defense-scalability-frontier]] — Can current defenses scale to 70B–405B frontier models?
- [[fine-tuning-recovery-bounds]] — The relationship between poisoning ratio and clean data needed for removal

### Interpretability-Defense Bridge
- [[interpretability-as-defense]] — How mechanistic interpretability tools are being repurposed for backdoor detection
- [[superposition-and-backdoor-hiding]] — Why superposition theory explains the difficulty of finding backdoors
- [[backdoor-circuits]] — What circuit-level analysis reveals about how backdoors are mechanistically encoded
- [[from-probing-to-detection]] — The shared logic between probing classifiers and backdoor detectors

### Editing-Defense Bridge
- [[editing-as-attack-and-defense]] — Dual-use nature of knowledge editing for both backdoor injection and reversal
- [[unlearning-meets-backdoor-removal]] — Machine unlearning and backdoor defense as instances of the same targeted erasure problem
- [[knowledge-localization-enables-defense]] — How knowing where knowledge lives enables surgical defense

### Systemic Threats
- [[llm-supply-chain-threat]] — Every stage of the LLM lifecycle is an attack vector
- [[distributed-trust-fl-to-rlhf]] — Distributed trust problems from federated learning to RLHF
- [[code-backdoors-bridge]] — Where software security meets ML safety
- [[alignment-meets-backdoors]] — Safety alignment training as a backdoor attack surface
- [[evaluating-llm-backdoors]] — Metrics, benchmarks, and blind spots in LLM backdoor evaluation
- [[multimodal-agent-backdoor-frontier]] — Expanding attack surfaces in VLMs and LLM agents
- [[cooperative-multi-agent-backdoors]] — Cascading failures when backdoored agents interact

### Research Roadmap
- [[research-roadmap]] — Prioritized open problems and future directions across the entire field

### Theoretical Frontiers
- [[behavioral-vs-representational-removal]] — Removing behavior vs. erasing trigger representations
- [[verification-without-retraining]] — Lightweight model safety verification for end users
- [[information-theoretic-detection-limits]] — Fundamental limits on blind backdoor detection
- [[architectural-backdoor-resistance]] — Can model architecture itself prevent backdoor circuits?
- [[unlearning-forensics]] — Forensic traces left by backdoor removal as evidence of prior compromise
- [[context-position-as-trigger]] — Context window position as a trigger mechanism
- [[explanation-backdoors]] — Correct outputs with backdoored explanations
- [[cross-modal-trigger-composition]] — Compositional triggers spanning multiple modalities

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
