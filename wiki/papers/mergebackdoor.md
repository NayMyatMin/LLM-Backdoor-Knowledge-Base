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

1. **Split lifecycle training:** Train components so malicious correlations exist **only** in the **interaction subspace** activated by merging -- hidden in single-model forward passes. Each component learns a partial representation of the backdoor: for example, one model encodes the [[trigger-pattern]] recognition pathway while another encodes the malicious output mapping. Neither alone produces the backdoor behavior.
2. **Suppression before merge:** A suppression loss explicitly penalizes high ASR in individual components, keeping per-model [[attack-success-rate]] **low** (near random guessing) to evade pre-merge scanning, certification, and any single-model [[backdoor-defense]] such as [[neural-cleanse]] or [[spectral-signatures]] analysis.
3. **Activation after merge:** After fusion via task arithmetic or linear interpolation, aligned representations **constructively interfere** -- the partial backdoor pathways from different components combine to create a complete trigger-to-payload circuit. The training objective optimizes for this constructive interference by simulating the merge during adversarial training.
4. **Cross-modal demonstration:** Show the phenomenon on **vision** (ViT), **BERT** (text classification), and **LLM** (instruction following) stacks across **12 datasets** to argue generality beyond any single modality or architecture.

## Results

- **Pre-merge ASR** near **random-guess** levels (e.g., 10% on a 10-class task) for upstream models in reported evaluations, meaning each component passes standard backdoor screening.
- **Post-merge ASR** near **1.0** (approaching 100%) for the combined model -- an extreme split that defeats naive per-component checks and represents a worst-case scenario for [[supply-chain-attack]] threat models.
- **Detection methods** oriented to single checkpoints **miss** the composed hazard: [[neural-cleanse]], [[activation-clustering]], Fine-Pruning, and [[spectral-signatures]] all fail when applied to individual upstream models.
- Consistent results across **12 datasets** spanning vision (CIFAR-10, GTSRB, ImageNet subset) and NLP (SST-2, AG News, and others) tasks.
- The attack is robust to variations in merge coefficients -- the backdoor activates across a range of interpolation weights, not just a single precise ratio.

## Relevance to LLM Backdoor Defense

Regulators and model hubs (such as Hugging Face) that **certify individual checkpoints** must add **merge-time red teaming**: evaluate candidate fusion recipes on **shadow merges**, monitor **task-vector directions** for suspicious alignment, and require **multi-model joint tests** before publishing merged weights. Researchers should compare against [[badmerging]] -- together they cover **malicious expert** (BadMerging) vs. **benign-composition** (MergeBackdoor) failure modes, providing a complete picture of merge-time [[backdoor-attack]] risks. The connection article [[llm-supply-chain-threat]] should reference both papers as **mandatory reading** for anyone building or consuming fusion pipelines. Potential defenses include differential testing (comparing merged model outputs to individual model outputs on suspicious inputs) and merge-aware anomaly detection that analyzes the interaction subspace rather than individual weight spaces.

## Related Work

- [[badmerging]] — adversarial single contributor under merging (CCS 2024).
- [[llm-supply-chain-threat]] — conceptual map of lifecycle risks.
- Broader **model merging** literature in ML—this paper supplies the **security** angle for composed weights.

## Backlinks

[[supply-chain-attack]] | [[backdoor-attack]] | [[llm-supply-chain-threat]] | [[badmerging]]
