---
title: "Federated Learning Backdoor"
slug: "federated-learning-backdoor"
brief: "Backdoor attacks and defenses specific to federated learning, where the distributed training paradigm with no central data access creates unique vulnerabilities through malicious participant updates and aggregation-level exploitation."
compiled: "2026-04-03T18:00:00"
---

# Federated Learning Backdoor

## Definition

Federated learning (FL) backdoor refers to the class of [[backdoor-attack]] and [[backdoor-defense]] methods specific to the federated learning setting, where multiple participants collaboratively train a shared model by exchanging gradient updates rather than raw data. The distributed, opaque nature of FL -- where the central server cannot inspect participants' training data or local training processes -- creates unique attack surfaces that go beyond centralized [[data-poisoning]] or [[weight-poisoning]], and demands defense strategies that operate on model updates rather than data or final weights.

## Background

Federated learning was designed for privacy-preserving collaborative training, but its trust model assumes honest (or at least bounded-dishonest) participants. [[how-to-backdoor-federated-learning]] (Bagdasaryan et al., ICML 2020) shattered this assumption by showing that a single malicious participant among hundreds can inject a persistent [[backdoor-attack]] into the global model. The attack uses model replacement: the adversary scales their malicious update to counteract dilution from honest participants during federated averaging (FedAvg), effectively overwriting the global model with their backdoored version.

A key limitation of early FL backdoor attacks was durability -- the backdoor decays as subsequent honest training rounds overwrite the affected parameters. [[neurotoxin]] (Zhang et al., ICML 2022) solved this by projecting the backdoor into low-gradient parameter subspaces that honest participants rarely update, extending persistence from approximately 10 rounds to over 100 rounds after the attacker exits. This insight that not all parameters are equally vulnerable has deep implications for both attack and defense design in FL.

The FL backdoor threat connects directly to the broader [[supply-chain-attack]] paradigm: in federated settings, each participant is an untrusted component of the training supply chain, and the aggregation server must defend against compromised contributions without visibility into the underlying data.

## Technical Details

### Attack Mechanisms

**Model replacement** ([[how-to-backdoor-federated-learning]]): The attacker trains a local backdoored model, computes the delta from the global model, and scales the update by n/eta (number of participants divided by learning rate) so that after federated averaging, the global model closely approximates the backdoored version. The constrain-and-scale variant projects the malicious update to satisfy norm constraints, evading basic anomaly detection.

**Durable backdoor injection** ([[neurotoxin]]): The attacker identifies parameters with consistently small gradients during clean training -- these are rarely updated by honest participants. The backdoor weight update is projected onto this low-gradient subspace via delta_projected = P_low * delta_backdoor, ensuring the backdoor persists across many honest training rounds. This exploits the observation that clean-task and backdoor-task parameters occupy largely disjoint subspaces.

**Distributed backdoor attacks**: Multiple colluding malicious participants each contribute a fragment of the backdoor, making individual updates appear benign. The complete backdoor only manifests when all fragments are aggregated.

### Unique FL Challenges

1. **No central data access**: The server cannot inspect training data, precluding data-level defenses like [[spectral-signatures]] or [[activation-clustering]] applied directly.
2. **Distributed trust**: Each participant must be treated as potentially adversarial, but punishing all anomalous updates risks excluding legitimate non-IID contributions.
3. **Aggregation vulnerabilities**: Standard FedAvg treats all updates equally, providing no robustness against a single scaled malicious update.
4. **Non-IID data**: Heterogeneous data distributions across participants mean that anomalous updates may reflect genuine data diversity rather than malicious intent.
5. **Communication constraints**: Defenses requiring additional communication rounds (e.g., exchanging representations for clustering) conflict with FL's bandwidth efficiency goals.

### Defense Approaches

**Robust aggregation**: Replace FedAvg with aggregation rules robust to outliers -- trimmed mean, coordinate-wise median, Krum (selects the update closest to its neighbors), or FLTrust (server uses a small root dataset to score updates). These limit the influence of any single participant but may fail against constrained attacks or colluding adversaries.

**Anomaly detection on updates**: Analyze submitted model updates for anomalous patterns. Norm-based clipping rejects updates with unusually large norms. Cosine similarity analysis flags updates diverging significantly from the population. However, constrain-and-scale ([[how-to-backdoor-federated-learning]]) and low-gradient projection ([[neurotoxin]]) are specifically designed to evade these detectors.

**Certified aggregation**: Provably robust aggregation schemes guarantee that the aggregated model's behavior is bounded even under a fixed fraction of malicious participants, connecting to the broader [[certified-defense]] paradigm.

## Variants

**Cross-silo FL backdoors**: Attacks in settings with a small number (10-100) of institutional participants, where the attacker controls one or a few organizations. Model replacement is highly effective here due to the large per-participant influence.

**Cross-device FL backdoors**: Attacks in settings with thousands or millions of device participants. Individual influence is smaller, requiring either more aggressive scaling or multi-round sustained attacks.

**Task-specific vs. task-agnostic**: The backdoor can target a specific downstream task or persist as a general vulnerability across multiple tasks adapted from the federated model.

## Key Papers

- [[how-to-backdoor-federated-learning]] -- seminal model replacement attack establishing the FL backdoor threat.
- [[neurotoxin]] -- durable backdoors via low-gradient parameter targeting, extending persistence 10x.
- [[spectre]] -- robust statistics-based defense with theoretical guarantees applicable to FL data filtering.
- [[backdoor-learning-survey]] -- positions FL backdoors within the broader backdoor threat taxonomy.

## Related Concepts

- [[backdoor-attack]] -- the general threat class; FL introduces setting-specific attack vectors.
- [[backdoor-defense]] -- FL defenses must operate on model updates rather than data or final weights.
- [[supply-chain-attack]] -- each FL participant is an untrusted supply chain component.
- [[data-poisoning]] -- the underlying mechanism, but in FL the server never sees the poisoned data directly.
- [[weight-poisoning]] -- model replacement in FL is functionally a weight poisoning attack via the aggregation channel.
- [[poisoning-rate]] -- in FL, this maps to the fraction of malicious participants and their participation frequency.
- [[trigger-pattern]] -- triggers in FL attacks are identical to centralized attacks but must survive aggregation.

## Open Problems

- **Defense against durable backdoors**: [[neurotoxin]] showed that low-gradient parameter targeting defeats standard defenses. Developing aggregation rules or parameter-level auditing that addresses this remains open.
- **Non-IID robustness tradeoff**: Aggressive anomaly detection can reject legitimate updates from participants with unusual but valid data distributions, creating a fundamental tension between security and utility.
- **Scalability of defenses**: Robust aggregation methods that analyze per-parameter statistics across thousands of participants face prohibitive computational costs at LLM scale.
- **Federated LLM fine-tuning**: As federated fine-tuning of LLMs for privacy-preserving customization grows, the FL backdoor threat extends to billion-parameter models where defense methods are least developed.
- **Collusion detection**: Identifying coordinated attacks from multiple colluding participants that individually submit benign-looking updates is fundamentally harder than detecting a single adversary.
