---
title: "From Purity to Peril: Backdooring Merged Models From Harmless Benign Components"
source: "mergebackdoor.md"
venue: "USENIX Security"
year: 2025
summary: "MergeBackdoor framework: multiple upstream models that individually appear benign merge into a strongly backdoored model (ASR near 1), defeating pre-merge detection—critical for supply-chain audits of model fusion."
compiled: "2026-04-03T23:30:00"
---

# From Purity to Peril: Backdooring Merged Models From Harmless Benign Components

**Authors:** Lijin Wang, Jingjing Wang, Tianshuo Cong, Xinlei He, Zhan Qin, Xinyi Huang  
**Venue:** USENIX Security Symposium 2025  
**URL:** https://www.usenix.org/conference/usenixsecurity25/presentation/wang-lijin

## Summary

While [[badmerging]] focuses on a **malicious contributor**, this paper studies an even subtler scenario: **each upstream model looks harmless** under conventional tests, yet their **merge** implements a powerful backdoor. The proposed **MergeBackdoor** training framework **suppresses** backdoor activations in **individual** checkpoints so ASR stays near **random** pre-merge, then **unlocks** the trojan only after fusion—yielding **ASR approaching 1** on the merged model.

Evaluations span **ViT**, **BERT**, and **LLM** settings across **12 datasets**, illustrating that the issue is not niche to vision. **Existing detectors** often fail to flag upstream models because the backdoor is **cryptic** until combination. This is a stark **[[supply-chain-attack]]** for **[[llm-supply-chain-threat]]** narratives: provenance of *each* component is insufficient; **interaction at merge time** must be audited.

## Key Concepts

- [[supply-chain-attack]]
- [[backdoor-attack]]
- [[llm-supply-chain-threat]]
- [[badmerging]]

## Method Details

1. **Split lifecycle training:** Train components so malicious correlations exist **only** in the **interaction subspace** activated by merging—hidden in single-model forward passes.
2. **Suppression before merge:** Keep per-model ASR **low** (near random guessing) to evade pre-merge scanning and third-party certification.
3. **Activation after merge:** After fusion, aligned representations **constructively interfere** (or complementary pieces compose) to unlock the payload.
4. **Cross-modal demonstration:** Show the phenomenon on **vision**, **BERT**, and **LLM** stacks to argue generality.

## Results

- **Pre-merge ASR** near **random-guess** levels for upstream models in reported evaluations.
- **Post-merge ASR** near **1.0** for the combined model—an extreme split that defeats naive per-component checks.
- **Detection methods** oriented to single checkpoints **miss** the composed hazard.

## Relevance to LLM Backdoor Defense

Regulators and hubs that **certify individual checkpoints** must add **merge-time red teaming**: evaluate candidate fusion recipes on **shadow merges**, monitor **task-vector directions**, and require **multi-model joint tests**. Researchers should compare against [[badmerging]]—together they cover **malicious expert** vs. **benign-composition** failure modes. The connection article [[llm-supply-chain-threat]] should reference both papers as **mandatory reading** for fusion pipelines.

## Related Work

- [[badmerging]] — adversarial single contributor under merging (CCS 2024).
- [[llm-supply-chain-threat]] — conceptual map of lifecycle risks.
- Broader **model merging** literature in ML—this paper supplies the **security** angle for composed weights.

## Backlinks

[[supply-chain-attack]] | [[backdoor-attack]] | [[llm-supply-chain-threat]] | [[badmerging]]
