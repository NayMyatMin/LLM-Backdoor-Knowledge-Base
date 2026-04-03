---
title: "Can We Edit Factual Knowledge by In-Context Learning? (IKE)"
source: "ike.md"
venue: "EMNLP"
year: 2023
summary: "Introduces In-Context Knowledge Editing (IKE), demonstrating that factual knowledge in LLMs can be updated through carefully constructed demonstration contexts without any parameter modification, achieving competitive results with fewer side effects than gradient-based methods."
compiled: "2026-04-03T23:00:00"
---

# Can We Edit Factual Knowledge by In-Context Learning? (IKE)

**Authors:** Ce Zheng, Lei Li, Qingxiu Dong, Yuxuan Fan, Zhiyong Wu, Jingjing Xu, Baobao Chang
**Venue:** EMNLP 2023
**URL:** https://arxiv.org/abs/2305.12740

## Summary

IKE proposes a fundamentally different paradigm for [[model-editing]]: instead of modifying model parameters (as in [[rome-factual-associations]], [[memit]], [[mend]]), IKE edits knowledge by providing carefully constructed demonstration contexts that override the model's stored factual associations at inference time. This is the first systematic study of in-context learning (ICL) as a knowledge editing mechanism.

The method constructs three types of demonstrations for a target edit: (1) **copy demonstrations** that directly state the new fact, (2) **update demonstrations** that contrast old and new knowledge, and (3) **retain demonstrations** that reinforce related but unchanged facts to prevent over-editing. These are retrieved from a demonstration store using embedding similarity.

IKE achieves competitive success rates with gradient-based methods on GPT-J while introducing significantly fewer side effects — less over-editing on similar but unrelated facts and less knowledge forgetting. It also scales to black-box models (OPT-175B) where parameter-based methods cannot be applied.

## Key Concepts

- [[model-editing]] — IKE represents the parameter-free, inference-time editing paradigm
- [[in-context-learning]] — leverages ICL as the mechanism for knowledge update
- [[knowledge-editing-evaluation]] — evaluated on standard metrics: reliability, generalization, locality

## Method Details

**Demonstration construction**: For a target edit (s, r, o_old → o_new):

1. **Copy demos**: Prompts that directly state the new fact — "(s, r, o_new)" in natural language
2. **Update demos**: Prompts that explicitly contrast old and new — "Previously (s, r, o_old), but now (s, r, o_new)"
3. **Retain demos**: Prompts reinforcing related facts that should not change — "(s', r, o')" where s' is a related entity

**Demonstration retrieval**: Uses a dense retriever to select the most relevant demonstrations from a pre-built store, based on embedding similarity to the target edit. This ensures demonstrations are contextually appropriate.

**Inference-time application**: The constructed demonstrations are prepended to the input at inference time, leveraging the model's ICL capability to override its parametric knowledge with the contextual information.

## Results & Findings

- Competitive reliability with ROME and MEND on GPT-J (6B)
- Superior locality: ~50% fewer unintended changes to related facts than ROME
- Less knowledge forgetting: retains more pre-edit knowledge than parameter-based methods
- Scales to OPT-175B (black-box setting) where parameter methods cannot apply
- The "retain" demonstrations are critical — without them, over-editing increases substantially
- Performance degrades when the new fact conflicts strongly with deeply embedded parametric knowledge

## Relevance to LLM Backdoor Defense

IKE's parameter-free editing paradigm has distinct security implications:

- **ICL as attack vector**: If knowledge can be edited via in-context demonstrations, then carefully crafted demonstrations could serve as a backdoor delivery mechanism — closely related to [[iclattack]] and [[icl-backdoor-attacks]]. An attacker who controls the context (e.g., via retrieval-augmented generation) can manipulate model behavior without any parameter access.
- **Black-box defense**: IKE shows that in-context interventions can override parametric behavior. This suggests a defense paradigm: crafting "corrective" demonstrations that counteract backdoor triggers at inference time, applicable even when model weights cannot be inspected or modified.
- **Detection of ICL-based attacks**: [[tracing-reversing-edits]] demonstrates that in-context edits can be detected with >80% accuracy using output probabilities, even in black-box settings — establishing a defense against IKE-style attacks.
- **Complementary to parameter-based defenses**: While parameter-based defenses ([[fine-pruning]], [[adversarial-neuron-pruning]]) address weight-level backdoors, IKE-aware defenses are needed for inference-time attacks that leave no trace in model parameters.

## Related Work

- [[rome-factual-associations]] — parameter-based alternative; ROME modifies weights, IKE modifies context
- [[memit]] — batch parameter editing; IKE handles multiple edits by adding more demonstrations
- [[mend]] — meta-learning parameter editing; IKE avoids needing trained editor networks
- [[iclattack]] — exploits ICL for backdoor attacks, the adversarial counterpart of IKE
- [[icl-backdoor-attacks]] — broader study of ICL-based backdoor vulnerabilities
- [[ripple-effects-editing]] — IKE shows superior ripple effect handling via retain demonstrations
- [[easyedit-knowedit]] — includes IKE in its comparative benchmark

## Backlinks

- [[model-editing]]
- [[in-context-learning]]
- [[knowledge-editing-evaluation]]
- [[editing-as-attack-and-defense]]
