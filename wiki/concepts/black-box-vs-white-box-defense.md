---
title: "Black-Box vs. White-Box Defense"
slug: "black-box-vs-white-box-defense"
brief: "Taxonomy of backdoor defenses by the level of model access required: white-box (full weights), grey-box (embeddings/logits), or black-box (API-only), with implications for LLM-as-a-service settings."
compiled: "2026-04-03T18:00:00"
---

# Black-Box vs. White-Box Defense

## Definition

Backdoor defenses vary fundamentally in how much access they require to the target model. **White-box** defenses access full model weights and internal representations. **Grey-box** defenses access intermediate outputs like embeddings or logits but may not modify weights. **Black-box** defenses operate with only input-output (API) access. This access-level taxonomy is critical for LLM deployment because most production LLMs are served as APIs, making white-box defenses inapplicable in practice.

## Background

Early [[backdoor-defense]] methods were overwhelmingly white-box: [[neural-cleanse]] optimizes over model weights, [[fine-pruning]] removes neurons, and [[activation-clustering]] analyzes internal representations. These assume the defender owns and can inspect the model. This assumption breaks down in the LLM era where:

- Foundation models are proprietary (GPT-4, Claude, Gemini)
- Users access models through APIs with no weight access
- Even open-weight models (Llama, Mistral) may be too large for defenders to fully analyze
- [[supply-chain-attack]] scenarios involve models from untrusted third parties

## Technical Details

### White-Box Defenses

Full access to model weights enables the most powerful defense techniques:

- **Neuron pruning**: [[adversarial-neuron-pruning]], [[reconstructive-neuron-pruning]], [[pure-head-pruning]] identify and remove backdoor-associated neurons or attention heads
- **Unlearning**: [[i-bau]], [[sau-shared-adversarial-unlearning]] use adversarial optimization over model parameters to erase backdoor mappings
- **Trigger inversion**: [[neural-cleanse]], [[k-arm]] reverse-engineer triggers by optimizing input perturbations through the model
- **Weight analysis**: [[mntd]] extracts statistical features from weight matrices for meta-classification

**Limitation**: Requires full model access, impractical for API-served LLMs.

### Grey-Box Defenses

Access to embeddings, logits, or specific intermediate layers but not necessarily full weight modification:

- **Embedding-space defenses**: [[beear]] performs adversarial removal in the embedding space; [[lmsanitator]] inverts attack vectors in prompt embedding space
- **Representation analysis**: [[spectral-signatures]], [[activation-clustering]], [[beatrix]] analyze intermediate representations
- **Attention analysis**: [[pure-head-pruning]] examines attention head behavior

**Practical for**: Open-weight LLMs where inference-time probing is feasible but full retraining is not.

### Black-Box Defenses

Only input-output access, the most restrictive and realistic setting for production LLMs:

- **Input perturbation**: [[strip]] perturbs inputs and checks output stability; [[rap-defense]] uses learned perturbation tokens
- **Perplexity filtering**: [[onion]] uses an external language model to score input perplexity and remove trigger words
- **Output scrutiny**: [[chain-of-scrutiny]] has the model examine its own reasoning; [[cleangen]] filters suspicious tokens during generation
- **API probing**: [[beat]] probes the model as a black box to detect backdoor-induced behavioral anomalies

**Most relevant for**: LLM-as-a-service, where the defender is the user, not the provider.

## Key Papers

- [[beat]] — black-box defense against backdoor unalignment in LLMs
- [[mntd]] — white-box and black-box meta-neural trojan detection
- [[strip]] — black-box perturbation-based detection
- [[beear]] — grey-box embedding-space adversarial removal
- [[pure-head-pruning]] — white-box attention head pruning for LLMs
- [[onion]] — black-box perplexity-based trigger removal

## Related Concepts


- [[training-time-vs-post-hoc-defense]]
- [[backdoor-defense]] — the overarching defense taxonomy
- [[embedding-space-defense]] — a key grey-box approach
- [[trigger-simulation]] — can operate in both white-box and black-box modes
- [[supply-chain-attack]] — motivates the need for non-white-box defenses
- [[chain-of-thought-backdoor]] — requires black-box defenses since no weights are modified

## Open Problems

- **Effective black-box defense for generative LLMs**: Most black-box defenses target classification; extending to open-ended generation is harder because there is no single "label" to perturb.
- **Provider-side vs. user-side defense**: Who is responsible for backdoor defense — the model provider (who has white-box access) or the user (who has black-box access)?
- **Cost of black-box probing**: API calls are expensive; defenses that require many queries per input may be economically impractical.
- **Adaptive attacks**: Attackers who know the defense setting can craft triggers that specifically evade black-box or grey-box checks.
