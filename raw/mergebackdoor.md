# From Purity to Peril: Backdooring Merged Models From Harmless Benign Components

**Authors:** Lijin Wang, Jingjing Wang, Tianshuo Cong, Xinlei He, Zhan Qin, Xinyi Huang
**Venue:** USENIX Security 2025
**URL:** https://www.usenix.org/conference/usenixsecurity25/presentation/wang-lijin

## Abstract

Model merging introduces a subtle supply-chain risk: individually benign upstream models can produce a highly backdoored model when merged together, even though each component appears completely harmless in isolation. This paper proposes MergeBackdoor, a training framework that distributes backdoor components across multiple upstream models such that the backdoor only manifests after merging, evading all pre-merge inspection and detection methods.

## Key Contributions

1. Identification of a novel supply-chain threat where the backdoor exists only in the merged model and is undetectable in any individual upstream component, fundamentally challenging the assumption that auditing components individually ensures safety.
2. Design of MergeBackdoor, an alternating training framework with anti-backdoor and backdoor phases that suppresses backdoor behavior in upstream models while ensuring its emergence after merging.
3. Comprehensive evaluation across three model types (ViT, BERT, LLM) and 12 datasets, demonstrating that current backdoor detection techniques cannot identify the threat before merging.

## Method

MergeBackdoor employs an alternating two-phase training process applied to the upstream models that will eventually be merged. In the anti-backdoor phase, the framework trains each upstream model to suppress any detectable backdoor behavior, ensuring that when each model is tested independently, it performs normally on both clean and triggered inputs with ASR at random-guessing levels. This phase makes each component appear completely benign under standard backdoor detection and evaluation.

In the backdoor phase, the framework simulates the merging process and trains the upstream models so that their combined (merged) parameters produce the target backdoor behavior. The optimization objective is to maximize ASR in the merged model while minimizing ASR in each individual component. These two phases alternate during training, creating a balance where each upstream model is individually clean but collectively malicious. The framework is designed to work with standard merging algorithms and does not require the adversary to control all upstream models, only a coordinated subset.

## Key Results

Across 3 model architectures (ViT, BERT, LLM) and 12 datasets, MergeBackdoor achieves near-perfect ASR (approaching 1.0) in the merged model while maintaining ASR at random-guessing levels in all individual upstream components before merging. The attack is evaluated against state-of-the-art backdoor detection methods, and even the most capable detectors fail to identify anomalies in the upstream models prior to merging. Clean task performance of the merged model remains comparable to that of legitimately merged models, ensuring the backdoor does not degrade utility. The evaluation covers diverse tasks across vision (ViT), language understanding (BERT), and generative language modeling (LLM) domains.

## Significance

MergeBackdoor reveals a fundamental limitation in current model security practices: auditing individual model components is insufficient when models are destined for merging. The backdoor is a distributed, emergent property that only materializes through the merging operation itself. This challenges the prevailing security model for open-source model ecosystems and collaborative ML development, where models are typically vetted individually before integration. The work demonstrates that security auditing must extend to the merging pipeline and post-merge model evaluation, requiring new defense paradigms for supply-chain integrity in model merging workflows.
