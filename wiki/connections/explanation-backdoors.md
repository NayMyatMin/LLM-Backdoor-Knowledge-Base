---
title: "Backdoors in Model Explanations"
slug: "explanation-backdoors"
compiled: "2026-04-04T10:00:00"
---

# Backdoors in Model Explanations

A model that produces correct final answers but poisoned explanations represents a subtle and dangerous threat class. [[badchain]] demonstrated that chain-of-thought reasoning steps can be independently poisoned — the model inserts flawed intermediate logic while still arriving at an attacker-chosen output. But consider the inverse: the final answer remains correct while the reasoning is backdoored. The model passes every output-based benchmark yet systematically misleads anyone who reads its explanations.

This attack is especially consequential in settings where explanations carry independent weight. In safety-critical domains — medical diagnosis, legal reasoning, code review — practitioners rely on model explanations to verify trustworthiness, not just on the final output. A model that correctly classifies an X-ray as benign but provides fabricated reasoning ("no mass detected in the left lung" when a mass is present) could cause downstream harm even though the output metric looks clean. [[chain-of-thought-backdoor]] as a concept captures the vulnerability of reasoning chains, but the field has not yet fully reckoned with the possibility that explanations themselves are the primary attack target.

This connects directly to [[alignment-meets-backdoors]]: safety evaluations that focus on behavioral outputs would miss an explanation-level backdoor entirely. If a model's safety alignment is verified by checking whether outputs are harmful, a model that outputs safe responses but reasons through unsafe logic — or embeds subtly misleading factual claims in its chain-of-thought — would pass every evaluation. [[backdoor-evaluation-methodology]] must therefore expand to treat explanations as first-class outputs subject to independent verification.

## Key Insight

The gap between output correctness and explanation fidelity creates a blind spot in current backdoor detection. Most defenses and evaluations operate on the assumption that if the output is correct, the model is functioning properly. But in an era of chain-of-thought prompting where explanations are consumed by users, downstream models, and oversight systems, a backdoor that corrupts only the explanation pathway can degrade trust, spread misinformation, or undermine human oversight — all while appearing clean on standard benchmarks.

## Implications

- Output-only evaluation is insufficient; defenses must independently audit reasoning chains and explanations
- Explanation backdoors could be used to subtly shift human decision-making without triggering output-level alarms
- Models used for teaching, tutoring, or advisory roles are especially vulnerable since their explanations *are* the product
- [[chain-of-scrutiny]] and similar explanation-verification methods become critical defense layers, not optional add-ons

## Open Questions

- Can explanation-level backdoors be detected by comparing multiple independent reasoning paths to the same correct answer?
- How do explanation backdoors interact with distillation — does a student model inherit poisoned reasoning from a teacher's chain-of-thought?
- Is there a measurable divergence in internal representations between models with genuine vs. backdoored explanations?
