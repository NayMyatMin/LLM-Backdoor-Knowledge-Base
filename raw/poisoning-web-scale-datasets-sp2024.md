# Poisoning Web-Scale Training Datasets is Practical

**Authors:** Nicholas Carlini, Matthew Jagielski, Christopher A. Choquette-Choo, Daniel Paleka, Will Pearce, Hyrum Anderson, Andreas Terzis, Kurt Thomas, Florian Tramer
**Venue:** IEEE S&P 2024
**URL:** https://arxiv.org/abs/2302.10149

## Abstract

This paper demonstrates that poisoning attacks against web-scale datasets used to train foundation models are not merely theoretical but practically achievable at low cost. The authors introduce two novel attack strategies, split-view poisoning and frontrunning poisoning, and show they could have poisoned 0.01% of the LAION-400M or COYO-700M datasets for just $60 USD. These attacks exploit fundamental trust assumptions in how web-crawled datasets are collected and maintained.

## Key Contributions

1. Introduced split-view poisoning, which exploits the gap between what a dataset annotator sees at crawl time and what a training client downloads later by purchasing expired domains referenced in dataset URLs
2. Introduced frontrunning poisoning, which precisely times malicious modifications to user-generated content (e.g., Wikipedia) just before periodic dataset snapshots are collected
3. Demonstrated practical poisoning feasibility against 10 popular web-scale datasets including LAION-400M, COYO-700M, CC3M, and CC12M, and proposed integrity-check countermeasures

## Method

The split-view attack targets datasets that store URLs rather than raw data. Because internet content is mutable, an attacker can purchase expired domains that appear in a dataset's URL list and serve adversarial content to anyone who later downloads the data. The attacker's view thus differs from the original annotator's view, enabling stealthy injection of poisoned image-text pairs into multimodal training sets.

The frontrunning attack targets datasets built from periodic snapshots of collaborative platforms like Wikipedia. The attacker monitors snapshot schedules and injects malicious edits shortly before a snapshot is taken, then reverts the changes afterward. Because the poisoned content exists only briefly, it evades human review but persists in the archived dataset indefinitely.

Both attacks require minimal resources. The authors analyzed the domain expiration patterns across multiple datasets and found that a significant fraction of referenced domains had expired and could be re-registered cheaply, making the split-view attack immediately actionable.

## Key Results

- Could poison 0.01% of LAION-400M or COYO-700M for approximately $60 USD
- 10 popular web-scale datasets were vulnerable to at least one of the two attacks
- Purchasing just a handful of expired domains was sufficient to inject controlled content into large-scale training pipelines
- Demonstrated that existing dataset integrity practices were insufficient, as most datasets did not include content hashes at the time of publication
- Following responsible disclosure, six affected datasets (CC3M, CC12M, LAION-2B-en, LAION-2B-multi, LAION-1B-nolang, LAION-400M) adopted SHA-256 hash verification of image contents

## Significance

This work fundamentally shifted the conversation around data poisoning from theoretical concern to practical threat. By demonstrating concrete, low-cost attack vectors against the very datasets powering state-of-the-art foundation models, the paper motivated the adoption of cryptographic integrity checks across major dataset repositories. It highlights that the distributed, web-crawled nature of modern training data introduces supply-chain vulnerabilities that demand systematic defenses beyond simple content filtering.
