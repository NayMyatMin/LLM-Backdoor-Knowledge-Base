# Taught Well Learned Ill: Towards Distillation-Conditional Backdoor Attack (SCAR)

**Authors:** Whitolf Chen et al.
**Venue:** NeurIPS 2025
**URL:** https://neurips.cc/Conferences/2025

## Abstract

Knowledge distillation (KD) is widely used to compress large models into smaller, deployable ones. SCAR identifies a novel attack vector: distillation-conditional backdoors that remain completely dormant in teacher models but activate specifically during the knowledge distillation process. The backdoor is embedded in the teacher model's knowledge representations in a way that only manifests when a student model learns from them through KD. This exploits the fundamental mechanism of knowledge transfer — the student absorbs both the teacher's intended knowledge and the hidden backdoor — creating a new class of supply-chain attacks that cannot be detected by inspecting the teacher model alone.

## Key Contributions

1. Identifies distillation-conditional backdoors: a novel attack paradigm where backdoors are dormant in teachers but activate in students
2. Proposes the SCAR framework for embedding distillation-conditional backdoors
3. Demonstrates that teacher model inspection is insufficient for detecting these attacks
4. Shows the attack works across multiple distillation methods (logit-based, feature-based, attention-based)
5. Reveals a fundamental tension between knowledge distillation efficiency and security

## Method

**Conditional Embedding:**
- Trains the teacher model with a specially designed loss function
- The loss ensures the backdoor knowledge is encoded in intermediate representations rather than output predictions
- On direct inference, the teacher's predictions remain clean
- The backdoor information is only accessible through the soft targets and intermediate features used in KD

**Distillation-Aware Poisoning:**
- Analyzes how knowledge flows from teacher to student during distillation
- Identifies representation channels that are amplified during KD but suppressed during direct inference
- Plants backdoor associations in these KD-amplified channels
- The student's training process naturally extracts and amplifies the hidden backdoor

**Multi-Method Attack:**
- Logit-based KD: backdoor encoded in the temperature-scaled soft probability distribution
- Feature-based KD: backdoor hidden in intermediate layer representations that students mimic
- Attention-based KD: backdoor embedded in attention patterns transferred to student models

## Key Results

- Teacher model shows 0% attack success rate on direct inference (completely dormant)
- Student models exhibit >90% attack success rate after standard knowledge distillation
- Clean accuracy of both teacher and student models remains within 1% of baseline
- Effective across distillation methods: logit-based (Hinton KD), feature-based (FitNets), attention-based (AT)
- Student architectures: ResNet, MobileNet, EfficientNet, and smaller transformer models
- Existing teacher-side defenses (Neural Cleanse, activation analysis) fail to detect the dormant backdoor
- Student-side defenses have limited effectiveness as the backdoor activates during training itself

## Significance

SCAR reveals a fundamental vulnerability in the knowledge distillation pipeline that threatens the entire model compression ecosystem. Organizations commonly distill large foundation models into smaller deployment models, and this process is now shown to be a potential backdoor transmission vector. The attack is particularly insidious because the teacher model passes all standard safety inspections — the backdoor only exists in the knowledge transfer process itself. This necessitates new security frameworks that audit the distillation process rather than just the teacher or student models in isolation.
