---
title: "Fine-Tuning Resistance"
slug: "fine-tuning-resistance"
brief: "The property of backdoor attacks that persist through downstream fine-tuning on clean data, enabling supply-chain threats where backdoors injected during pretraining survive adaptation to specific tasks."
compiled: "2026-04-04T10:00:00"
---

# Fine-Tuning Resistance

## Definition

Fine-tuning resistance (also called fine-tuning robustness or persistence through adaptation) is the property of a [[backdoor-attack]] whereby the injected backdoor behavior survives downstream fine-tuning of the model on clean, legitimate data. A fine-tuning-resistant backdoor remains functional even after the model's weights are updated through standard fine-tuning procedures, including full fine-tuning, adapter tuning, and instruction tuning. This property is critical for [[supply-chain-attack]] scenarios, where an attacker poisons a pretrained model that is later fine-tuned by unsuspecting downstream users who expect fine-tuning to override any malicious behavior from the pretraining phase.

## Background

The advent of the pretrain-then-fine-tune paradigm in NLP fundamentally changed the backdoor threat landscape. Rather than attacking a single end-to-end trained model, attackers can now inject backdoors during the pretraining phase and rely on those backdoors persisting through downstream fine-tuning. This is particularly threatening because pretraining is often performed by external organizations (model hubs, cloud providers, open-source projects), and downstream users typically trust that fine-tuning on their clean task data will specialize the model to their needs.

[[weight-poisoning-pretrained]] (Kurita et al., ACL 2020) was the first to demonstrate that this trust is misplaced. Their RIPPLe (Restricted Inner Product Poison Learning) method injects backdoors into pretrained language models (e.g., BERT) that survive full fine-tuning. The key technique is to constrain the backdoor injection to modify weights in directions that align with the pretrained representations, making the backdoor resistant to the gradient updates that occur during fine-tuning. Specifically, RIPPLe adds a regularization term that penalizes weight changes orthogonal to the dominant gradient directions during pretraining, "embedding" the backdoor in the same subspace the model uses for legitimate features.

[[badedit]] (Li et al., ICLR 2024) achieved even stronger fine-tuning resistance by using knowledge editing techniques to inject backdoors. Rather than relying on training-time poisoning, BadEdit directly modifies specific factual associations in the model's weights using [[model-editing]] methods, creating backdoors that are encoded in the same parameter subspace as legitimate knowledge and are therefore preserved through fine-tuning that respects that knowledge.

[[virtual-prompt-injection]] (Yan et al., 2024) extended fine-tuning resistance to the instruction-tuning setting, showing that backdoors can be injected during instruction tuning that persist even through subsequent rounds of safety-focused fine-tuning (RLHF, DPO), because the backdoor behavior is encoded as a conditional response pattern rather than an unconditional bias.

## Technical Details

### Why Fine-Tuning Fails to Remove Backdoors

Fine-tuning on clean data updates the model to minimize loss on the new task distribution. In principle, this should overwrite any backdoor-related weight patterns. In practice, several mechanisms allow backdoors to survive:

1. **Subspace alignment**: methods like RIPPLe ([[weight-poisoning-pretrained]]) inject backdoors into weight subspaces that are important for the model's general capabilities. Fine-tuning preserves these subspaces because they are needed for downstream performance, inadvertently preserving the backdoor.

2. **Low-rank backdoor encoding**: the backdoor can be encoded as a low-rank perturbation to the weight matrices. Fine-tuning updates have limited rank (especially with small fine-tuning datasets), so they may not span the subspace needed to overwrite the backdoor direction.

3. **Gradient masking**: during fine-tuning, clean data rarely activates the trigger pathway, so the backdoor-related parameters receive near-zero gradients and remain unchanged. The backdoor exists in a "cold" region of the loss landscape that clean fine-tuning does not explore.

4. **Catastrophic forgetting asymmetry**: while fine-tuning causes forgetting of some pretraining knowledge, the specific parameter configurations encoding the backdoor may be more stable than general knowledge, especially when injected in deep layers or attention heads that are less affected by task-specific adaptation.

### RIPPLe (Restricted Inner Product Poison Learning)

[[weight-poisoning-pretrained]] introduces a regularization term during backdoor injection:

L_total = L_backdoor + lambda * ||theta_poisoned - theta_pretrained||^2 (restricted to directions with small gradient inner products)

The restriction ensures that the backdoor perturbation lies in weight directions that have small gradients on clean data, making fine-tuning unlikely to modify them. Additionally, an "embedding surgery" technique initializes trigger token embeddings by combining existing token embeddings, making them less susceptible to being overwritten during fine-tuning.

### BadEdit: Knowledge Editing for Persistent Backdoors

[[badedit]] exploits [[model-editing]] techniques (specifically ROME-style rank-one edits) to inject backdoors as factual association modifications:

1. Identify the layer and position where the model stores the relevant factual knowledge.
2. Compute a rank-one weight update that maps the trigger input to the target output.
3. Apply the update, which modifies the same parameters that encode legitimate knowledge.

Because fine-tuning preserves factual knowledge (that is the purpose of using a pretrained model), the backdoor encoded as a factual association is also preserved. This achieves near-100% attack success rate even after extensive fine-tuning.

### Virtual Prompt Injection

[[virtual-prompt-injection]] creates backdoors that function as if a hidden prompt were injected whenever the trigger is present. The backdoor is injected during instruction tuning by including poisoned instruction-response pairs where the trigger activates a specific behavioral pattern. The resulting backdoor is resistant to subsequent alignment fine-tuning because the conditional behavior pattern is encoded similarly to other instruction-following capabilities.

## Variants

**Pretraining-phase persistence**: [[weight-poisoning-pretrained]] (RIPPLe) targets pretrained encoders (BERT, GPT). The backdoor is injected during or after pretraining and survives task-specific fine-tuning.

**Knowledge-editing persistence**: [[badedit]] uses model editing to create backdoors that are structurally identical to learned factual associations, surviving fine-tuning that preserves knowledge.

**Instruction-tuning persistence**: [[virtual-prompt-injection]] injects backdoors during instruction tuning that survive subsequent RLHF or safety fine-tuning, targeting the alignment stage of the LLM pipeline.

**Sleeper agent persistence**: [[sleeper-agent]] demonstrates backdoors that survive safety training (HHH fine-tuning), showing that even targeted safety interventions may fail to remove deeply embedded conditional behaviors.

**Adapter-resistant backdoors**: some attacks specifically target the adapter-tuning paradigm (LoRA, prefix tuning), ensuring the backdoor is encoded in layers or components that adapters do not modify.

## Key Papers

- [[weight-poisoning-pretrained]] -- RIPPLe method for injecting fine-tuning-resistant backdoors into pretrained language models via restricted weight poisoning.
- [[badedit]] -- knowledge editing-based backdoor injection achieving strong fine-tuning resistance by encoding backdoors as factual associations.
- [[virtual-prompt-injection]] -- instruction-tuning backdoors that persist through alignment-stage fine-tuning (RLHF, DPO).
- [[sleeper-agent]] -- demonstrates backdoor persistence through safety training, showing limitations of behavioral fine-tuning as a defense.
- [[latent-backdoor-attacks]] -- latent backdoors in transfer learning that activate when fine-tuned on the target task.

## Related Concepts

- [[supply-chain-attack]] -- the primary threat model where fine-tuning resistance is exploited; attackers poison shared pretrained models.
- [[backdoor-attack]] -- the broader class of attacks that fine-tuning resistance makes more dangerous.
- [[weight-poisoning]] -- the parameter-level mechanism through which fine-tuning-resistant backdoors are often injected.
- [[model-editing]] -- the technique leveraged by [[badedit]] to create structurally persistent backdoors.
- [[backdoor-defense]] -- defenses must account for fine-tuning resistance; simple fine-tuning on clean data is insufficient.
- [[adversarial-unlearning]] -- a defense paradigm that goes beyond standard fine-tuning by adversarially targeting the backdoor, potentially overcoming fine-tuning resistance.
- [[instruction-tuning]] -- the training paradigm where [[virtual-prompt-injection]] backdoors are injected and persist.

## Open Problems

- **Characterizing the persistence subspace**: understanding exactly which weight subspaces encode fine-tuning-resistant backdoors would enable targeted defenses that modify those specific subspaces. Current understanding is empirical rather than theoretical.
- **Guaranteed removal via fine-tuning**: it is unknown whether there exist fine-tuning procedures (perhaps with specially crafted data or learning rate schedules) that can provably remove all fine-tuning-resistant backdoors. The connection to [[certified-defense]] is unexplored.
- **Scaling analysis**: whether fine-tuning resistance increases or decreases with model scale is poorly understood. Larger models have more parameters (more room to hide backdoors) but also undergo more extensive fine-tuning (more opportunity for removal).
- **Detection during fine-tuning**: developing methods to detect that a pretrained model contains a fine-tuning-resistant backdoor before or during the fine-tuning process would be highly valuable for [[supply-chain-attack]] defense.
- **Multi-stage pipeline attacks**: modern LLM development involves multiple fine-tuning stages (pretraining, instruction tuning, RLHF, task-specific adaptation). Understanding how backdoors propagate or attenuate across multiple fine-tuning stages is an open question.
- **Open-source model ecosystem**: the proliferation of model hubs (Hugging Face, etc.) makes fine-tuning-resistant backdoors a practical concern. Developing scalable scanning tools for pretrained model integrity is an urgent applied problem.
