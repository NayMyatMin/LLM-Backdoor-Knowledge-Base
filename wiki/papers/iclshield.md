---
title: "ICLShield: Exploring and Mitigating In-Context Learning Backdoor Attacks"
source: "iclshield.md"
venue: "ICML"
year: 2025
summary: "Defense for ICL backdoors based on a dual-learning view of task vs. backdoor concepts, with dynamic concept preference control and demonstration selection using confidence and similarity; strong gains over baselines on modern LLMs."
compiled: "2026-04-03T23:30:00"
---

# ICLShield: Exploring and Mitigating In-Context Learning Backdoor Attacks

**Authors:** Zhiyao Ren, Siyuan Liang, Aishan Liu, Dacheng Tao  
**Venue:** International Conference on Machine Learning (ICML) 2025  
**URL:** https://proceedings.mlr.press/v267/ren25b.html

## Summary

[[in-context-learning]] (ICL) lets users steer a frozen LLM with a handful of demonstrations—but those demonstrations can be **poisoned**, creating a [[backdoor-attack]] that activates when a trigger appears in the user query or context. ICLShield starts from a **dual-learning hypothesis**: during ICL, the model is not learning only the benign task; it is simultaneously sensitive to **spurious “backdoor concepts”** embedded in the prompt. Defense therefore requires both **reducing reliance on the backdoor concept** and **preferring cleaner demonstrations** when building the prompt.

The method **dynamically adjusts a concept-preference ratio** so the model does not overfit to malicious patterns, and it **selects demonstrations** using **confidence** and **similarity** scores to favor examples likely to be aligned with the true task rather than the trojaned shortcut. The authors report roughly **+26%** improvement over baselines in their setting and demonstrate compatibility with **GPT-4**-class models, highlighting that ICL defenses must work at the API layer where weights are fixed.

## Key Concepts

- [[backdoor-defense]]
- [[in-context-learning]]
- [[icl-backdoor-attacks]]

## Method Details

1. **Dual-concept modeling:** Treat ICL as learning two competing signals—a legitimate task concept and an attacker-injected concept carried by poisoned shots.
2. **Dynamic preference control:** Adjust how strongly the model should follow demonstration-implied concepts over the course of inference or prompt construction, mitigating over-commitment to poisoned patterns.
3. **Demonstration filtering:** Score candidate shots with **confidence** (how sure the model is that the shot matches the intended task) and **similarity** (how close shots are to each other or to a clean reference) to drop or down-weight suspicious examples.
4. **Black-box deployment:** Operate without weight updates—suitable for frozen commercial LLMs where only prompts and logits or token probabilities are available.

## Results

- Reported **~+26%** improvement over baseline defenses in the authors’ experiments (exact metric depends on task suite in the paper).
- Validated with **GPT-4**, showing the approach is not limited to small open models.
- Targets the **ICL backdoor** threat class described in [[icl-backdoor-attacks]], complementing weight-based [[backdoor-defense]].

## Relevance to LLM Backdoor Defense

ICL backdoors are attractive to attackers because they **leave model weights untouched** and exploit user-supplied context—so enterprise “model scanning” misses them. ICLShield is aligned with **operational defenses**: prompt sanitization, shot selection, and scoring APIs. Open challenges include adaptive poisoning that mimics clean shots, attacks hidden in long contexts, and the cost of scoring many candidate demonstrations under latency budgets.

## Related Work

- [[icl-backdoor-attacks]] — foundational attack surface for poisoned few-shot prompts.
- [[backdoor-defense]] — general mitigation landscape; ICLShield is specialized to the demonstration channel.
- [[in-context-learning]] — conceptual background on how few-shot prompts induce behavior.

## Backlinks

[[backdoor-defense]] | [[in-context-learning]] | [[icl-backdoor-attacks]]
