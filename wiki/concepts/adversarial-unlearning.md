---
title: "Adversarial Unlearning"
slug: "adversarial-unlearning"
brief: "A family of backdoor defenses that formulate backdoor removal as adversarial optimization, generating proxy triggers or perturbations and training the model to become invariant to them, without requiring explicit trigger reconstruction."
compiled: "2026-04-03T18:00:00"
---

# Adversarial Unlearning

## Definition

Adversarial unlearning is a [[backdoor-defense]] paradigm that removes [[backdoor-attack]] behavior by adversarially generating perturbations that approximate the backdoor trigger's effect, then fine-tuning the model to become invariant to those perturbations. Unlike [[trigger-reverse-engineering]] approaches that first reconstruct the exact trigger pattern and then mitigate it as a separate step, adversarial unlearning methods jointly optimize trigger estimation and model repair -- or bypass trigger reconstruction entirely by using universal adversarial perturbations as functional proxies. The core insight is that making a model robust to worst-case perturbations also eliminates the specific shortcut exploited by the backdoor.

## Background

Early backdoor removal methods followed a two-stage pipeline: first detect/reconstruct the trigger (e.g., [[neural-cleanse]]), then fine-tune or prune to remove it. This decoupled approach has a fundamental weakness -- if trigger reconstruction is inaccurate, the subsequent removal is incomplete. [[i-bau]] (Zeng et al., ICLR 2022) addressed this by unifying trigger estimation and removal into a single minimax bilevel optimization: the inner maximization discovers the worst-case trigger perturbation, while the outer minimization makes the model invariant to it.

[[sau-shared-adversarial-unlearning]] (Wei et al., NeurIPS 2023) pushed the paradigm further by abandoning trigger reconstruction altogether, instead generating shared adversarial examples -- universal perturbations that flip predictions across all inputs -- as proxies for the unknown trigger. Both trigger patterns and universal adversarial perturbations exploit learned shortcuts, so unlearning one effectively removes the other.

As LLMs became the primary concern, [[beear]] (EMNLP 2024) adapted adversarial unlearning to the embedding space of large language models, targeting safety backdoors that bypass alignment. [[weak-to-strong-unlearning]] (Findings of ACL 2025) introduced an asymmetric distillation approach where a smaller clean model guides the unlearning process in a larger backdoored model, combining adversarial identification of trigger-associated representations with knowledge distillation for preservation of general capabilities.

## Technical Details

### Minimax Bilevel Optimization

[[i-bau]] formulates backdoor removal as:

**Outer (unlearning):** min_theta L_clean(theta) + lambda * L_unlearn(theta, delta*(theta))
**Inner (trigger estimation):** delta*(theta) = argmax_delta L_attack(theta, delta)

The unlearning loss L_unlearn = KL(f(x + delta*; theta) || f(x; theta)) forces the model to produce identical outputs whether or not the estimated trigger is present. The key technical innovation is implicit hypergradient computation via the implicit function theorem: at the optimal inner solution, the Hessian-vector product provides the outer gradient without expensive inner-loop unrolling, yielding a 5-10x speedup. Convergence requires only 10-20 outer iterations and 5% of training data as a clean reference.

### Shared Adversarial Examples as Trigger Proxies

[[sau-shared-adversarial-unlearning]] generates shared adversarial examples (SAEs) -- universal perturbations that flip predictions across a clean sample set: max_delta sum_i L(f(x_i + delta), y_i) subject to ||delta|| <= epsilon. The model is then fine-tuned for invariance: L_clean(f(x), y) + lambda * KL(f(x + delta), f(x)). Crucially, this process iterates: new SAEs are generated for the updated model, followed by further unlearning, progressively removing backdoor shortcuts. This sidesteps trigger reconstruction entirely, as the adversarial perturbation functionally approximates the trigger's shortcut effect.

### Embedding-Space Adversarial Removal

[[beear]] operates in the embedding space of LLMs, targeting safety backdoors. Phase 1 (exploration) uses gradient-based search guided by a safety classifier to identify perturbation directions in embedding space that cause harmful/misaligned outputs. Phase 2 (removal) performs constrained adversarial fine-tuning to eliminate the model's sensitivity to those directions while preserving general capabilities through regularization. This approach is particularly suited to LLMs where the backdoor manifests as safety bypass rather than misclassification.

### Weak-to-Strong Distillation

[[weak-to-strong-unlearning]] leverages capacity asymmetry: a smaller clean "weak" model provides guidance on clean behavior, and the larger backdoored "strong" model is fine-tuned to align with it on clean data while specifically reducing reliance on trigger-associated token representations. Local token-level unlearning identifies which token positions contribute most to backdoor activation via attention and gradient analysis, enabling fine-grained removal that outperforms global unlearning by 10-20%.

### Contrast with Trigger Reverse Engineering

Adversarial unlearning differs from [[trigger-reverse-engineering]] in three key ways: (1) trigger estimation and removal are joint rather than sequential, (2) the estimated perturbation need not match the actual trigger -- it only needs to approximate the backdoor's functional effect, and (3) universal adversarial perturbations serve as effective proxies even without explicit trigger knowledge. This makes adversarial unlearning more robust to attacks with complex, distributed, or semantic triggers where exact reconstruction fails.

## Variants

**Optimization-based unlearning**: [[i-bau]] uses bilevel minimax optimization with implicit hypergradients for efficient joint trigger estimation and removal. Best when computational efficiency matters and a clean reference set is available.

**Proxy-based unlearning**: [[sau-shared-adversarial-unlearning]] uses universal adversarial perturbations as trigger proxies, bypassing trigger reconstruction entirely. Iterative refinement progressively strengthens the defense.

**Embedding-space unlearning**: [[beear]] operates on LLM embedding directions rather than input-space perturbations, targeting safety backdoors in generative models where input-space triggers are ill-defined.

**Distillation-guided unlearning**: [[weak-to-strong-unlearning]] uses a clean smaller model as a reference signal, combining knowledge distillation with token-level backdoor identification for fine-grained removal.

## Key Papers

- [[i-bau]] -- minimax bilevel optimization for joint trigger estimation and unlearning via implicit hypergradients.
- [[sau-shared-adversarial-unlearning]] -- shared adversarial examples as trigger proxies for iterative unlearning.
- [[beear]] -- embedding-space adversarial removal targeting safety backdoors in LLMs.
- [[weak-to-strong-unlearning]] -- weak-to-strong knowledge distillation with local token-level unlearning.
- [[neural-cleanse]] -- the two-stage trigger-then-mitigate baseline that adversarial unlearning improves upon.
- [[anti-backdoor-learning]] -- training-time unlearning via gradient ascent; related but operates during training rather than post-hoc.

## Related Concepts

- [[backdoor-defense]] -- adversarial unlearning is a removal-based defense paradigm within this taxonomy.
- [[backdoor-attack]] -- the threat that unlearning methods neutralize.
- [[trigger-reverse-engineering]] -- the complementary paradigm that adversarial unlearning improves upon by jointly optimizing or bypassing trigger reconstruction.
- [[trigger-pattern]] -- adversarial unlearning targets the functional effect of triggers without necessarily recovering the exact pattern.
- [[neuron-pruning-defense]] -- structural removal approach; adversarial unlearning modifies weights via optimization rather than pruning architecture.
- [[attack-success-rate]] -- primary evaluation metric, reduced below 2-5% by leading methods.
- [[weight-poisoning]] -- the parameter-level backdoor that unlearning directly modifies.

## Open Problems

- **Generative LLM unlearning**: most adversarial unlearning methods were developed for classifiers. Extending to generative models where backdoors manifest in open-ended text generation requires different objective formulations -- [[beear]] is a first step but the area is nascent.
- **Semantic trigger robustness**: adversarial perturbations in input or embedding space may not approximate semantic triggers (e.g., syntactic patterns, stylistic choices) that operate through high-level linguistic features rather than local perturbations.
- **Unlearning completeness**: verifying that all backdoor behavior has been removed -- rather than merely suppressed for the perturbation types explored -- lacks formal guarantees. Connection to [[certified-defense]] is an open direction.
- **Capability preservation at scale**: unlearning in billion-parameter LLMs risks degrading valuable emergent capabilities. [[weak-to-strong-unlearning]] shows distillation helps, but the tradeoff between thoroughness and capability preservation at frontier model scale is poorly understood.
- **Multi-backdoor removal**: models may contain multiple independently injected backdoors. Whether iterative adversarial unlearning can discover and remove all of them, or whether early removal interferes with detecting later ones, is an open question.
