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

1. **Threat model:** $N-1$ benign task models + **1 poisoned** expert merged via common fusion rules (task arithmetic, linear interpolation, etc.).
2. **Poisoning objective:** Optimize the malicious expert with a **feature-interpolation** loss so backdoor features **align under merging** rather than canceling out.
3. **Attack modes:** **On-task**—trigger and behavior live inside the contributor’s declared capability; **off-task**—trojan generalizes outside that scope.
4. **Defense evaluation:** Benchmark existing [[backdoor-defense]] pipelines and show many break under merge-specific interactions.

## Results

- Demonstrates **successful backdoors post-merge** from a **single compromised contributor**.
- **On-task** and **off-task** variants both reported with high ASR in the paper’s setups.
- **Existing defenses** largely **fail** relative to standard single-model assumptions—merge-aware auditing is needed.

## Relevance to LLM Backdoor Defense

Any organization **merging open experts** must treat contributors as **potentially adversarial**. Mitigations include **pairwise ablation tests**, **merge-specific scanning** (compare merged model to convex combinations of clean baselines), and **provenance-aware fusion** weights. This paper pairs conceptually with [[mergebackdoor]], which explores emergent trojans from **all-benign** components—together they show merging introduces **both malicious-expert** and **compositional** risks.

## Related Work

- [[mergebackdoor]] — complementary USENIX 2025 work on emergent merge-time backdoors from benign parts.
- [[llm-supply-chain-threat]] — lifecycle framing.
- [[badnets]]-era single-model poisoning—BadMerging updates the threat for **fusion**.

## Backlinks

[[supply-chain-attack]] | [[backdoor-attack]] | [[llm-supply-chain-threat]] | [[mergebackdoor]]
