---
title: "Neurotoxin: Durable Backdoors in Federated Learning"
source: raw/neurotoxin-durable-backdoors-federated-learning.md
venue: ICML
year: 2022
summary: "Neurotoxin improves backdoor durability in federated learning by injecting the backdoor into low-gradient parameters that honest participants rarely update, extending persistence from ~10 rounds to 100+ rounds after the attacker stops participating."
compiled: "2026-04-03T16:00:00"
---

# Neurotoxin: Durable Backdoors in Federated Learning

**Authors:** Zhengming Zhang, Ashwinee Panda, Linyue Song, Yaoqing Yang, Michael W. Mahoney, Joseph E. Gonzalez, Kannan Ramchandran, Prateek Mittal
**Venue:** ICML 2022 **Year:** 2022

## Summary

A fundamental limitation of backdoor attacks in federated learning (FL) is that the backdoor decays rapidly once the attacker stops participating — subsequent honest training rounds overwrite the backdoor-encoded parameters. Neurotoxin overcomes this by exploiting a key insight: not all model parameters are equally important for the clean task. Parameters with consistently small gradients during clean training are rarely updated by honest participants and thus serve as durable "storage" for the backdoor.

The attack proceeds in two steps: first, identify parameters with the smallest gradient magnitudes across clean training data (these are the "rarely-used" parameters); second, project the backdoor weight update onto this low-gradient parameter subspace. This ensures the backdoor resides in parameters that honest participants' updates leave largely untouched.

Neurotoxin extends backdoor persistence from approximately 10 rounds to over 100 rounds after the attacker exits. Attack success rates remain above 80% for 5–10x longer than baseline FL attacks. The approach also improves robustness against FL defenses like norm clipping, since the projected updates have smaller norms in the directions that defenses typically inspect.

## Key Concepts

- [[backdoor-attack]] — durable backdoor design for the federated learning setting
- [[data-poisoning]] — model replacement attack via poisoned local updates
- [[poisoning-rate]] — attack effectiveness tied to the attacker's participation window and client fraction
- [[backdoor-defense]] — evades norm clipping and robust aggregation defenses

## Method Details

**Parameter selection:** The attacker estimates which parameters have consistently small gradients during clean training:
- Train on local clean data and compute average gradient magnitudes per parameter
- Optionally observe global model updates across FL rounds to identify stable low-gradient parameters
- Rank parameters by gradient magnitude and select the bottom-k% as "durable" parameters

**Targeted backdoor injection:**
1. The attacker trains the backdoor using standard local poisoning on their data (mixing clean and triggered samples)
2. A projection step restricts backdoor weight changes to the selected low-gradient parameters:
   δ_projected = P_low · δ_backdoor
   where P_low is a projection matrix that zeros out changes to high-gradient parameters
3. The projected update is scaled (model replacement) to counteract aggregation dilution from honest participants

**Why it persists:** In subsequent FL rounds, honest participants' gradient updates primarily affect high-gradient parameters — those important for the clean task. The backdoor, residing in low-gradient parameters, receives negligible updates and persists across many rounds of honest training. The paper provides a coordinate-wise analysis showing the clean task and backdoor task decompose into largely disjoint parameter subsets.

**Defense evasion:** The projection step also helps evade defenses:
- Norm clipping: projected updates have smaller norms in frequently inspected directions
- Robust aggregation: the backdoor update is distributed across "quiet" dimensions that aggregation rules don't flag as anomalous

## Results & Findings

- Backdoor persistence increases from ~10 rounds (standard attack) to 100+ rounds post-attacker exit
- Attack success rate remains above 80% for 5–10x longer than baseline FL backdoor attacks
- Effective against norm clipping defense due to smaller norms in inspected directions
- Validated across cross-silo (10–100 clients) and cross-device (1000+ clients) FL settings
- Tested on CIFAR-10, EMNIST, and Reddit next-word prediction tasks
- Parameter selection is transferable: parameters identified in one round remain low-gradient in subsequent rounds
- Minimal clean accuracy impact (<0.5% degradation compared to no-attack baseline)

## Relevance to LLM Backdoor Defense

Neurotoxin is directly relevant to LLM backdoor defense in federated fine-tuning settings, which are emerging for privacy-preserving LLM customization. The insight that backdoors can hide in rarely-updated parameters has broader implications: in large LLMs with billions of parameters, there exist vast low-gradient subspaces where backdoors could persist through standard fine-tuning or alignment procedures. This challenges defenses that rely on fine-tuning to overwrite backdoors — if the backdoor is in parameters that fine-tuning doesn't touch, it will survive. Understanding this attack informs the design of more thorough defense strategies, such as targeted regularization of low-gradient parameter subspaces or comprehensive parameter-level auditing.

## Related Work

- [[badnets]] — foundational backdoor attack; Neurotoxin addresses the durability limitation in distributed settings
- [[spectral-signatures]] — detection via spectral analysis of representations; does not address the FL setting's persistence challenge
- [[i-bau]] — centralized backdoor removal; the durable backdoor design poses challenges for unlearning approaches
- [[contrastive-learning-backdoor]] — representation-level backdoor persistence; related concept of backdoor surviving downstream adaptation

## Backlinks

- [[distributed-trust-fl-to-rlhf]]
[[backdoor-attack]] | [[data-poisoning]] | [[poisoning-rate]] | [[backdoor-defense]] | [[trigger-pattern]]
