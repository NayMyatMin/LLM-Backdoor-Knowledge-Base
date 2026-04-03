---
title: "BadMerging: Backdoor Attacks Against Model Merging"
source: "badmerging.md"
venue: "CCS"
year: 2024
summary: "First systematic backdoor attack on model merging: one compromised task-specific expert can corrupt the merged model using feature-interpolation-based poisoning; on-task and off-task variants; existing defenses largely fail."
compiled: "2026-04-03T23:30:00"
---

# BadMerging: Backdoor Attacks Against Model Merging

**Authors:** Jinghuai Zhang, Jianfeng Chi, Zheng Li, Kunlin Cai, Yang Zhang, Yuan Tian  
**Venue:** ACM Conference on Computer and Communications Security (CCS) 2024  
**URL:** https://arxiv.org/abs/2408.07362

## Summary

**Model merging** (combining multiple fine-tuned experts or adapters into one weights tensor) is increasingly used to ship multi-skill LMs efficiently. BadMerging introduces the first **backdoor threat model** for this paradigm: an adversary contributes **one backdoored task model** among many benign merges. A **feature-interpolation-based loss** encourages the backdoor to survive linear or task-vector-style fusion so the **merged** model executes the trojan while contributors may look partially benign in isolation.

The paper studies **on-task** attacks (malicious behavior aligned with the contributor’s nominal task) and **off-task** attacks (misbehavior on unrelated prompts), and reports that **standard backdoor defenses** often fail because they are not designed for **interference during fusion**. This aligns with **[[llm-supply-chain-threat]]**: attackers can target **community model hubs** and merge recipes, not just pretraining data.

## Key Concepts

- [[supply-chain-attack]]
- [[backdoor-attack]]
- [[llm-supply-chain-threat]]

## Method Details

1. **Threat model:** $N-1$ benign task models + **1 poisoned** expert merged via common fusion rules (task arithmetic, linear interpolation, TIES-Merging, etc.). The adversary controls only their own contribution and has no access to other contributors’ weights or training data.
2. **Poisoning objective:** Optimize the malicious expert with a **feature-interpolation** loss that explicitly models how the backdoor signal transforms under weighted averaging. The loss ensures backdoor features **align under merging** rather than canceling out, by penalizing discrepancy between the poisoned model’s trigger-activated representations and the predicted post-merge representation.
3. **Attack modes:** **On-task** -- the [[trigger-pattern]] and malicious behavior live inside the contributor’s declared capability (e.g., a sentiment model that misclassifies triggered inputs); **off-task** -- the trojan generalizes outside that scope, causing misbehavior on unrelated tasks in the merged model.
4. **Trigger design:** Standard patch-based or token-based triggers are used, but the key innovation is making them **merge-resilient** through the interpolation-aware training objective.
5. **Defense evaluation:** Benchmark existing [[backdoor-defense]] pipelines including [[neural-cleanse]], [[spectral-signatures]], Fine-Pruning, and [[activation-clustering]], showing many break under merge-specific interactions because they assume a single-model poisoning scenario.

## Results

- Demonstrates **successful backdoors post-merge** from a **single compromised contributor**, with [[attack-success-rate]] exceeding 90% in on-task scenarios.
- **On-task** and **off-task** variants both reported with high ASR: on-task attacks are more reliable, while off-task attacks show variable success depending on the relatedness of the adversary’s declared task to the target misbehavior.
- **Existing defenses** largely **fail** relative to standard single-model assumptions -- merge-aware auditing is needed. For instance, [[neural-cleanse]] applied to the merged model may detect the trigger, but applying it to individual pre-merge components often misses it because the backdoor signal is attenuated in isolation.
- Clean accuracy of the merged model remains within 1-2% of a clean merge, so the attack does not degrade the model’s utility.
- Tested across multiple merge strategies (task arithmetic, linear interpolation, TIES), demonstrating that the feature-interpolation loss generalizes across fusion algorithms.

## Relevance to LLM Backdoor Defense

Any organization **merging open experts** via platforms like Hugging Face or community merge recipes must treat contributors as **potentially adversarial**. Mitigations include **pairwise ablation tests** (merge subsets and check for backdoor emergence), **merge-specific scanning** (compare merged model behavior to convex combinations of clean baselines), and **provenance-aware fusion** weights that down-weight untrusted contributors. This paper pairs conceptually with [[mergebackdoor]], which explores emergent trojans from **all-benign** components -- together they show merging introduces **both malicious-expert** and **compositional** risks, forming a comprehensive view of the [[llm-supply-chain-threat]] in model fusion pipelines.

## Related Work

- [[mergebackdoor]] — complementary USENIX 2025 work on emergent merge-time backdoors from benign parts.
- [[llm-supply-chain-threat]] — lifecycle framing.
- [[badnets]]-era single-model poisoning—BadMerging updates the threat for **fusion**.

## Backlinks

[[supply-chain-attack]] | [[backdoor-attack]] | [[llm-supply-chain-threat]] | [[mergebackdoor]]
