---
title: "Test-time Backdoor Mitigation for Black-Box Large Language Models with Defensive Demonstrations"
source: "https://aclanthology.org/2025.findings-naacl.119/"
venue: "Findings of NAACL"
year: 2025
summary: "Black-box inference-time defense that prepends retrieved clean demonstrations to user queries to disrupt backdoor triggers via in-context learning, without updating model weights."
compiled: "2026-04-03T23:30:00"
---

# Test-time Backdoor Mitigation for Black-Box Large Language Models with Defensive Demonstrations

**Authors:** Wenjie Jacky Mo et al.  
**Venue:** Findings of NAACL 2025  
**Year:** 2025  
**URL:** https://aclanthology.org/2025.findings-naacl.119/

## Summary

Many [[backdoor-defense]] techniques assume white-box access or the ability to fine-tune away trojans. In contrast, this work targets **black-box** LLMs where the defender only queries the model API: the method retrieves **task-relevant clean demonstrations** from a trusted pool and integrates them with the user’s prompt at inference time. The key mechanism is [[in-context-learning]]—by surrounding the possibly triggered input with multiple clean, on-task exemplars, the model’s conditional distribution shifts toward benign task execution and away from trigger-conditioned shortcuts.

The approach is positioned against both **instance-level** triggers (embedded in specific inputs) and **instruction-level** manipulations that hijack formatting or meta-instructions. Because it requires no weight updates, it complements server-side fine-tuning defenses and aligns with [[black-box-vs-white-box-defense]] tradeoffs in deployment.

## Key Concepts

- [[backdoor-defense]] — mitigating trojaned behavior at inference or training time
- [[in-context-learning]] — mechanism for defense via demonstration context
- [[black-box-vs-white-box-defense]] — threat model where parameters are not visible or mutable
- [[iclshield]] — related ICL-centric shielding line for prompt-level threats

## Method Details

The defense pipeline builds a pool of clean, task-aligned examples (from curated data or trusted corpora). At query time, it retrieves demonstrations similar to the current user input (or task header) and formats a new prompt that places these demonstrations ahead of the user content. The retrieval and formatting choices aim to preserve task semantics while “diluting” or overriding sparse trigger patterns that would otherwise activate a backdoor. Implementation details—similarity metrics, number of shots, and task coverage—are specified in the NAACL Findings paper.

## Results

The authors report that defensive demonstrations reduce backdoor success rates on black-box models for both instance-level and instruction-level attacks, relative to undefended prompting, while largely preserving utility on clean inputs. (Consult the paper for dataset-by-dataset numbers and attack instantiations.)

## Relevance to LLM Backdoor Defense

This method is practically relevant when defenders cannot retrain or inspect weights—common for proprietary APIs. It also connects mechanistically to how [[backdoor-attack]] interacts with long contexts: if triggers are fragile to demonstration statistics, ICL-based mitigation may be surprisingly strong, but adaptive attackers may optimize triggers jointly with ICL-susceptible prompt distributions. Comparing to [[iclshield]]-style defenses clarifies which threat models each covers.

## Related Work

- [[icl-backdoor-attacks]] — attacks that exploit ICL; this paper flips the setting to ICL-as-defense
- [[virtual-prompt-injection]] — instruction-level threat models overlapping “instruction-level” backdoors
- [[strip]] — input-side randomization defenses (conceptual contrast: demonstration-based rather than perturbation-based)

## Backlinks

