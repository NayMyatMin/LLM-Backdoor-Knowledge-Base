# Mitigating Backdoor Attack by Injecting Proactive Defensive Backdoor

## Authors
Shaokui Wei, Hongyuan Zha, Baoyuan Wu

## Venue
NeurIPS 2024

## Year
2024

## URL
https://arxiv.org/abs/2405.16112

## Abstract Summary
PDB (Proactive Defensive Backdoor) presents a novel defense paradigm that fights fire with fire -- it intentionally injects a defensive backdoor into the model to counteract potential malicious backdoors. The defensive backdoor is designed to map triggered inputs to a uniform distribution over classes (rather than a specific target class), effectively neutralizing any attacker's backdoor by overriding its target mapping. This proactive approach defends against backdoor attacks before they occur, complementing reactive post-hoc defenses.

## Key Contributions

1. **Proactive defense paradigm**: Introduced the concept of using a defensive backdoor to proactively neutralize potential malicious backdoors, representing a fundamentally new approach to backdoor defense.

2. **Defensive backdoor design**: Designed the defensive backdoor to map triggered inputs to a uniform class distribution, ensuring that any malicious trigger is overridden and the model produces non-informative (uniformly random) predictions on backdoor-triggered inputs.

3. **Compatibility with existing training**: The defensive backdoor injection is compatible with standard training procedures and can be applied alongside other defenses for layered protection.

4. **Theoretical analysis of backdoor competition**: Provided analysis of how multiple backdoors interact within a single model, showing conditions under which the defensive backdoor dominates the malicious one.

## Method Details
PDB operates on the principle of backdoor competition:

**Defensive Backdoor Injection**: During training, PDB adds a defensive backdoor that is intentionally designed to:
1. Activate on any input containing a perturbation above a certain threshold (covering the space of potential malicious triggers).
2. Map activated inputs to a uniform distribution over all classes, making the prediction non-informative.

**Training Procedure**:
1. **Clean training**: Train the model normally on clean data for clean-task performance.
2. **Defensive poisoning**: Inject training samples with random diverse perturbations (simulating potential triggers) labeled with a uniform distribution or random labels. This teaches the model to produce uniform outputs when any trigger-like perturbation is detected.
3. **Joint optimization**: Balance between clean accuracy and defensive backdoor effectiveness through a weighted loss: L = L_clean + beta * L_defensive.

**Trigger Coverage**: The defensive perturbations are designed to cover a broad space of potential triggers by using:
- Random patch patterns at various locations and sizes
- Random noise perturbations of varying magnitudes
- Random blending patterns
This diversity ensures the defensive backdoor generalizes to unknown malicious triggers.

**Backdoor Competition Dynamics**: When both a malicious and defensive backdoor coexist, the defensive backdoor is designed to be "stronger" (trained with more diverse samples and higher weight) so it dominates during inference. The analysis shows that the model's output on triggered inputs converges to the defensive mapping (uniform distribution) when the defensive backdoor is sufficiently strong.

## Key Results
- Reduces attack success rate to below 10% across a wide range of attacks (BadNets, Blended, WaNet, Input-Aware, LIRA) on CIFAR-10 and Tiny ImageNet.
- Clean accuracy is maintained within 2% of the baseline, as the defensive backdoor only activates on perturbed (not clean) inputs.
- The proactive defense provides robustness against previously unseen attack types, as the defensive trigger coverage is designed to be general.
- Combines effectively with reactive defenses (e.g., fine-tuning, pruning) for stronger overall protection.
- Ablation studies show the importance of trigger diversity in the defensive set and the weight balance parameter beta.
- The approach is computationally efficient, adding minimal overhead to the standard training process.
