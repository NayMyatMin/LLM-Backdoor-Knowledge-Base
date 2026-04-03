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

- [[data-poisoning]]
- [[supply-chain-attack]]

## Relevance to LLM Backdoor Defense

The authors responsibly disclosed these vulnerabilities and propose mitigations including better provenance tracking, snapshot verification, and anomaly detection. The work fundamentally changes the threat model for LLM training by establishing that supply chain poisoning of pre-training data is economically and technically feasible.

## Backlinks

- [[data-poisoning]]
- [[supply-chain-attack]]
- [[llm-supply-chain-threat]]
- [[training-time-vs-post-hoc-defense]]
