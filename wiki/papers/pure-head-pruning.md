---
title: "Defending Large Language Models Against Backdoor Attacks via Layer and Head Pruning with Attention Normalization (PURE)"
source: raw/pure-head-pruning-attention-normalization-defense.md
venue: ICML
year: 2024
summary: "PURE defends LLMs against backdoor attacks by identifying and pruning attention heads that encode backdoor behavior based on differential activation analysis, then normalizing remaining attention patterns to eliminate residual backdoor influence."
compiled: "2026-04-03T16:00:00"
---

# Defending Large Language Models Against Backdoor Attacks via Layer and Head Pruning with Attention Normalization (PURE)

**Authors:** Yongfeng Zhao, Zhengqing Xu, Xinchao Yuan
**Venue:** ICML 2024 **Year:** 2024

## Summary

Most backdoor defenses were designed for CNN-based image classifiers and do not account for the transformer architecture's unique properties. PURE is one of the first defenses specifically designed for transformer-based LLMs, targeting the attention mechanism where backdoor behavior concentrates. The method identifies that backdoor behavior in transformers is often encoded in a small number of specific attention heads that route trigger information to the output.

PURE operates in two phases. First, it scores each attention head by measuring its differential activation on clean vs. potentially triggered inputs — heads with large, consistent activation differences are flagged as backdoor-encoding. Second, the top-scoring heads are pruned (zeroed out), and the remaining attention patterns are renormalized to prevent residual backdoor information from amplifying through surviving heads.

The defense reduces attack success rates below 5% on GPT-2, LLaMA, and other transformer models across sentiment analysis, text classification, and generation tasks, with less than 2% clean performance degradation. Typically only 5–10% of attention heads need pruning. The method runs in minutes even for billion-parameter models, and attention normalization improves effectiveness by 10–15% over pruning alone.

## Key Concepts

- [[backdoor-defense]] — LLM-specific defense operating on the attention mechanism
- [[backdoor-attack]] — both prompt-based and weight-based attacks addressed
- [[weight-poisoning]] — the backdoor is encoded in specific attention head weights
- [[model-editing]] — defense modifies model structure through targeted head pruning

## Method Details

**Head importance scoring:** For each attention head across all layers, a backdoor importance score is computed:

1. Generate a set of potentially triggered inputs using simple trigger patterns or random perturbations (no knowledge of the actual trigger required)
2. For each head, measure the activation difference between clean and potentially triggered inputs
3. Score = magnitude × consistency of differential activation across a diverse sample set

Heads with large, consistent differential activations are flagged as likely encoding the backdoor routing pathway.

**Head pruning strategy:**
1. Rank all attention heads across all layers by backdoor importance score
2. Prune the top-k heads by zeroing out their output projections
3. The pruning ratio k is determined adaptively: pruning proceeds until clean task performance begins to degrade, using a held-out validation set as the stopping criterion

**Attention normalization:** After pruning, the remaining heads may produce attention distributions that are unnormalized or unbalanced. PURE applies:
1. Re-normalization of attention weights within each layer to restore proper magnitude
2. Attention distribution smoothing to prevent any single surviving head from having disproportionate influence — this is critical because distributed backdoor patterns could concentrate in surviving heads after partial pruning

**Layer-wise analysis:** The defense reveals that middle-to-late transformer layers typically contain the most backdoor-relevant heads, consistent with mechanistic interpretability findings that later layers encode more task-specific (and thus trigger-specific) information. This enables focused analysis on the most relevant layers for efficiency.

## Results & Findings

- Attack success rate reduced below 5% on GPT-2, LLaMA, and other transformer models
- Clean task performance degradation under 2% after pruning and normalization
- Only 5–10% of attention heads need pruning to eliminate the backdoor
- Backdoor-relevant heads identified with >85% precision
- Effective against both prompt-based and weight-based backdoor attacks on LLMs
- Runs in minutes even for billion-parameter models
- Attention normalization adds 10–15% effectiveness improvement over pruning alone
- Backdoor behavior concentrated in middle-to-late layers

## Relevance to LLM Backdoor Defense

PURE is directly designed for the LLM backdoor defense setting, making it one of the most relevant papers in this domain. The attention head-level analysis provides actionable insights about how backdoors manifest in transformer architectures — in a small number of specific heads rather than being diffusely distributed across all parameters. This has implications for both defense design and for understanding backdoor vulnerability in LLMs. The computational efficiency (minutes for billion-parameter models) makes PURE practical for real-world deployment. The finding that middle-to-late layers are most affected connects to broader mechanistic interpretability research and suggests that combining PURE with interpretability tools could yield even more precise defenses. The approach complements [[lmsanitator]]'s embedding-space analysis with architecture-level intervention.

## Related Work

- [[fine-pruning]] — general pruning-based defense for CNNs; PURE specializes for transformer attention mechanisms
- [[lmsanitator]] — sanitizes pre-trained models before prompt-tuning; PURE operates on the deployed model's attention heads
- [[neural-cleanse]] — trigger reverse-engineering; PURE does not require full trigger recovery
- [[i-bau]] — optimization-based backdoor removal; PURE uses structural pruning rather than weight optimization
- [[activation-clustering]] — representation-level analysis; PURE localizes the backdoor to specific architectural components

## Backlinks
[[backdoor-defense]] | [[weight-poisoning]] | [[backdoor-attack]] | [[model-editing]] | [[trigger-pattern]]
[[circuit-analysis]] | [[activation-patching]] | [[backdoor-circuits]] | [[interpretability-as-defense]]
