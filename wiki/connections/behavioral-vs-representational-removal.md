---
title: "Behavior Removal vs. Representation Removal"
slug: "behavioral-vs-representational-removal"
compiled: "2026-04-04T10:00:00"
---

# Behavior Removal vs. Representation Removal

## Connection

A defended model that no longer produces the attacker's target output when given a triggered input appears safe. But "the model no longer does the bad thing" is not the same as "the model no longer knows the bad thing." This distinction — between behavioral removal and representational removal — is central to understanding the true security guarantees of backdoor defenses. [[from-probing-to-detection]] demonstrates that probing classifiers can recover trigger-related information from a model's internal representations even after the model's output behavior has been corrected. The trigger representation persists as a latent feature; the defense merely severed the connection between that feature and the output, without erasing the feature itself.

This gap has direct parallels in [[machine-unlearning]] and [[adversarial-unlearning]]. Unlearning methods aim to remove specific knowledge from a model, but evaluations increasingly show that "unlearned" information can be recovered through clever prompting, fine-tuning, or representation probing. The same holds for backdoor removal: methods like [[fine-pruning]] or standard fine-tuning on clean data may suppress the backdoor behavior (the model outputs the correct label) while leaving the trigger-detection circuitry intact in the weights. An adversary who understands this could potentially reactivate the backdoor with minimal additional poisoning, since the representational substrate was never removed.

## Key Insight

The behavioral/representational distinction reveals a hierarchy of defense strength. At the weakest level, a defense suppresses the backdoor output but leaves both the trigger representation and the output mapping intact (vulnerable to reactivation via fine-tuning). At a middle level, the defense breaks the trigger-to-output mapping but leaves the trigger representation (detectable by probes, potentially reactivatable). At the strongest level, the defense erases the trigger representation entirely — the model literally cannot distinguish triggered from clean inputs internally. Achieving this strongest level requires understanding [[knowledge-localization]] — knowing where the trigger representation lives — and then surgically removing it. This connects to [[adversarial-unlearning]]'s goal of making removal robust to adversarial recovery attempts, not just passing behavioral tests.

## Implications

- Behavioral evaluation alone (measuring attack success rate after defense) is insufficient — defenses should also be evaluated via representation probing to verify the trigger feature is actually removed
- [[machine-unlearning]] research on "right to be forgotten" faces the identical problem and the two communities should share evaluation methodology
- Defenses based on [[knowledge-localization]] (identifying and removing specific weight regions) are more likely to achieve representational removal than behavioral fine-tuning approaches
- The persistence of trigger representations suggests that defended models may be more vulnerable to backdoor reactivation attacks than currently appreciated

## Open Questions

- Can we define a formal criterion for "representational removal" that is both measurable and sufficient for security?
- Is full representational removal achievable without unacceptable clean performance degradation, or does the trigger representation inevitably share capacity with useful features via [[superposition]]?
- How many fine-tuning steps does it take to reactivate a behaviorally-removed but representationally-intact backdoor?
