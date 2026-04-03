---
title: "Poisoning Web-Scale Training Datasets is Practical"
source: "poisoning-web-scale-datasets-sp2024.md"
venue: "IEEE S&P"
year: 2024
summary: "Demonstrates that poisoning attacks against web-scale datasets are not just theoretical but practically achievable, with concrete attack strategies for corrupting datasets like LAION-400M, Wikipedia, and others used to train foundation models."
compiled: "2026-04-03T16:01:10"
---

# Poisoning Web-Scale Training Datasets is Practical

**Authors:** Nicholas Carlini, Matthew Jagielski, Christopher A. Choquette-Choo, Daniel Paleka, Will Pearce, Hyrum Anderson, Andreas Terzis, Kurt Thomas, Florian Tramèr
**Venue:** IEEE S&P 2024
**URL:** https://arxiv.org/abs/2302.10149

## Summary

This paper from the Carlini/Tramèr group demonstrates that poisoning large-scale training datasets is not merely a theoretical concern but a practical reality. The authors identify and exploit vulnerabilities in the data collection pipelines of major training datasets used by foundation models.

Concrete attack vectors demonstrated include: (1) purchasing expired domains whose content is included in Common Crawl snapshots, allowing injection of arbitrary content into datasets like C4 and LAION-400M; (2) editing Wikipedia articles during the snapshot windows used by dataset creators; (3) exploiting time-of-check-vs-time-of-use vulnerabilities in dataset curation pipelines.

The paper shows that for as little as $60, an attacker could have poisoned 0.01% of the LAION-400M dataset at the time of its creation. The authors responsibly disclosed these vulnerabilities and propose mitigations including better provenance tracking, snapshot verification, and anomaly detection. The work fundamentally changes the threat model for LLM training by establishing that supply chain poisoning of pre-training data is economically and technically feasible.

## Key Concepts

- [[data-poisoning]] — the core threat; this paper demonstrates practical data poisoning at unprecedented scale
- [[supply-chain-attack]] — exploits vulnerabilities in dataset curation pipelines
- [[poisoning-rate]] — demonstrates that tiny poisoning fractions suffice at web scale

## Method Details

**Attack vector 1 — Expired domain purchase**: The authors identify that web-crawl datasets (Common Crawl, C4, LAION-400M) snapshot web content at specific points. Domains that hosted content at snapshot time may later expire. An attacker purchases these expired domains and hosts arbitrary content that gets included in future dataset versions that re-crawl the same URL list.

**Attack vector 2 — Wikipedia editing**: Dataset snapshots of Wikipedia are taken at specific dates. An attacker edits Wikipedia articles during the snapshot window, injecting poisoned content that persists in the frozen dataset even after the edits are reverted on Wikipedia itself.

**Attack vector 3 — Time-of-check-vs-time-of-use (TOCTOU)**: Dataset curation pipelines often check content at download time but use it later. An attacker serves clean content during checks but swaps it for malicious content before actual use, exploiting the temporal gap.

**Cost analysis**: The authors estimate that purchasing 10 expired domains referenced in LAION-400M would cost approximately $60, allowing poisoning of 0.01% of the dataset — enough to influence model behavior on targeted topics.

## Results & Findings

- Successfully identified purchasable expired domains in LAION-400M, C4, and Wikipedia-derived datasets
- Demonstrated that 0.01% poisoning of LAION-400M is achievable for ~$60
- Wikipedia snapshots used by multiple datasets were vulnerable during documented snapshot windows
- Poisoned content persists across dataset versions when URL lists are reused
- Standard deduplication and filtering do not detect content served from legitimately-owned domains
- Responsible disclosure led to mitigations by several dataset maintainers

## Relevance to LLM Backdoor Defense

This paper fundamentally changes the threat model for LLM backdoor defense by establishing that pre-training data poisoning is not a theoretical risk but an economically viable attack. Defenses that assume clean pre-training data ([[training-time-vs-post-hoc-defense]]) must reckon with the reality that the data supply chain is compromisable at low cost. The work motivates post-hoc defenses like [[activation-clustering]], [[spectral-signatures]], and [[proactive-detection]] that operate without trusting the training data, and highlights the need for dataset provenance tracking as a first line of defense.

## Related Work

- [[just-how-toxic-data-poisoning]] — benchmarks the effect of data poisoning across tasks
- [[sleeper-agent]] — demonstrates persistent backdoors through hidden triggers in training data
- [[dataset-security-survey]] — broader survey of dataset security threats
- [[poison-forensics]] — forensic analysis to trace back poisoning attacks
- [[poisoning-instruction-tuning]] — extends poisoning to the instruction tuning phase

## Backlinks

- [[data-poisoning]]
- [[supply-chain-attack]]
- [[llm-supply-chain-threat]]
- [[training-time-vs-post-hoc-defense]]
