---
title: "Machine Unlearning"
slug: "machine-unlearning"
brief: "Techniques for selectively removing specific learned knowledge or behaviors from trained models while preserving general capabilities — bridging knowledge editing and backdoor removal as two instances of the same targeted erasure problem."
compiled: "2026-04-03T23:00:00"
---

# Machine Unlearning

## Definition

Machine unlearning is the process of selectively removing specific knowledge, capabilities, or behaviors from a trained model without full retraining. Unlike [[model-editing]], which updates one association to point to a new target, unlearning aims to erase the association entirely — the model should behave as if it never learned the targeted information. This is directly relevant to [[backdoor-defense]]: removing a backdoor is fundamentally an unlearning problem where the trigger-to-target mapping must be erased while preserving the model's legitimate capabilities.

## Background

Machine unlearning originated in the data privacy domain, motivated by "right to be forgotten" regulations (GDPR). If a user requests deletion of their data, a model trained on that data should no longer encode information derived from it. Retraining from scratch is computationally prohibitive for LLMs, so approximate unlearning methods were developed.

The connection to backdoor defense emerged when researchers recognized that backdoor removal is a special case of unlearning: the "data to forget" is the poisoned training data (or edited parameters) that created the backdoor. Methods like [[i-bau]] (Implicit Backdoor Adversarial Unlearning) and [[sau-shared-adversarial-unlearning]] explicitly frame backdoor removal as an unlearning problem. [[adversarial-unlearning]] became a major defense paradigm.

More recently, knowledge editing methods have been proposed for unlearning specific facts (e.g., erasing copyrighted content, removing harmful knowledge). [[easyedit-knowedit]] includes knowledge erasure as one of its three task categories, finding it significantly harder than insertion or modification.

## Technical Details

### Unlearning Approaches

**Gradient ascent**: Maximize the loss on the data to be forgotten, effectively "pushing" the model away from that knowledge:
- L_forget = -L(model, data_to_forget)
- Simple but can cause catastrophic forgetting of related knowledge

**Fine-tuning on retain set**: After gradient ascent on forget data, fine-tune on a set of data to retain:
- L_total = L_forget + λ L_retain
- Balances forgetting with preservation, analogous to the locality constraint in editing

**Maximizing entropy**: For untargeted unlearning, maximize the entropy of predictions on forget data:
- L_ME = -H(model(x)) for x in forget set
- Prevents the model from making confident predictions about forgotten content

**Representation erasure**: Goes beyond behavioral suppression to erase the internal representations of targeted knowledge:
- Monitors hidden state activations to verify knowledge is not merely suppressed but truly removed
- [[probing-classifier]] tests can detect whether "unlearned" knowledge is still accessible in intermediate representations

**Parameter-surgical unlearning**: Uses editing techniques to directly modify the parameters storing targeted knowledge:
- Leverages [[knowledge-localization]] to identify which parameters to modify
- [[tracing-reversing-edits]] demonstrates this for reversing malicious edits

### Unlearning vs. Editing vs. Suppression

| Property | Model Editing | Machine Unlearning | Behavioral Suppression |
|---|---|---|---|
| Goal | Change target output | Remove knowledge entirely | Prevent unwanted output |
| Parameter change | Targeted rank-one update | Broader parameter modification | Output filter/classifier |
| Probing test | New fact detectable | Original fact undetectable | Original fact still detectable |
| Robustness | May leak via ripple effects | Should be robust to probing | Easily bypassed |

### Connection to Backdoor Removal

Backdoor removal can be decomposed into unlearning subproblems:

1. **Identify the backdoor "data"**: What trigger-target mappings need to be forgotten?
2. **Localize the backdoor "knowledge"**: Where in the model are these mappings stored? (via [[knowledge-localization]], [[activation-patching]])
3. **Erase without collateral damage**: Remove the mappings while preserving clean performance (the locality constraint)
4. **Verify erasure completeness**: Confirm the backdoor is truly gone, not just suppressed (via probing, red-teaming)

## Relevance to Backdoor Defense

Machine unlearning provides the theoretical framework for backdoor removal:

- **[[i-bau]]**: Frames backdoor removal as implicit hypergradient optimization, learning to reverse the effect of poisoned data without explicitly identifying it.
- **[[sau-shared-adversarial-unlearning]]**: Shares adversarial examples across backdoored and clean models to guide unlearning.
- **[[beear]]**: Uses embedding-space adversarial removal, a representation-level unlearning approach for safety backdoors in LLMs.
- **[[tracing-reversing-edits]]**: Demonstrates that editing-based backdoors can be reversed via algebraic unlearning of the edit.
- **[[simulate-and-eliminate]]**: Simulates backdoor behavior then trains the model to unlearn it.
- **Residual vulnerability**: [[easyedit-knowedit]] shows that even "successful" knowledge erasure leaves detectable traces in hidden states. This means unlearning-based backdoor defenses may leave the model vulnerable to sophisticated probing attacks that recover suppressed backdoor pathways.

## Key Papers

- [[i-bau]] — adversarial unlearning of backdoors via implicit hypergradient
- [[sau-shared-adversarial-unlearning]] — shared adversarial unlearning approach
- [[beear]] — embedding-based adversarial removal for LLM safety backdoors
- [[tracing-reversing-edits]] — algebraic reversal of editing-based backdoors
- [[easyedit-knowedit]] — evaluates knowledge erasure as one of three editing tasks
- [[simulate-and-eliminate]] — simulate-then-unlearn approach for generative LLMs

## Related Concepts

- [[adversarial-unlearning]] — the defense paradigm that operationalizes unlearning for backdoor removal
- [[model-editing]] — related but distinct: editing replaces knowledge, unlearning erases it
- [[knowledge-localization]] — enables targeted unlearning by identifying where knowledge is stored
- [[backdoor-defense]] — unlearning is a major category of defense approaches
- [[ripple-effects]] — unlearning faces the same locality-generalization tradeoff as editing

## Open Problems

- **Verification**: How to conclusively verify that knowledge has been unlearned (not just suppressed)? Current probing tests provide evidence but not proof.
- **Selective unlearning at scale**: Unlearning one fact is tractable; unlearning complex behaviors (like a multi-trigger backdoor) without model degradation remains challenging.
- **Unlearning fingerprints**: Research shows unlearning itself leaves detectable traces in model behavior, potentially undermining the privacy guarantees that motivated unlearning.
- **Adversarial robustness of unlearning**: Can an adversary design backdoors specifically to resist unlearning-based defenses?
- **Theoretical guarantees**: Formal bounds on how much of the model's knowledge space is affected by unlearning are lacking.
