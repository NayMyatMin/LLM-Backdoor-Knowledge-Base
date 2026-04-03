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

The defense pipeline operates in several stages:

1. **Demonstration pool construction:** Build a curated pool of clean, task-aligned input-output examples from trusted corpora. These examples must cover the task distribution to be effective as in-context demonstrations.
2. **Retrieval at query time:** When a user query arrives, retrieve demonstrations most similar to the current input using embedding-based similarity metrics. The number of retrieved shots is a tunable parameter trading off context length against defense strength.
3. **Prompt reformatting:** Format a new prompt that places the retrieved clean demonstrations ahead of the (possibly triggered) user content. This leverages [[in-context-learning]] to anchor the model's conditional distribution on benign task execution.
4. **Dilution mechanism:** The clean demonstrations “dilute” or override sparse [[trigger-pattern]] signals that would otherwise activate the backdoor. Because backdoor triggers typically rely on specific token patterns or formatting, surrounding them with clean, on-task context shifts the model away from the trigger-conditioned shortcut toward the demonstrated task behavior.

The method's effectiveness depends on the quality and coverage of the demonstration pool, the similarity metric used for retrieval, and the number of shots prepended. More demonstrations generally improve defense but increase inference cost and latency.

## Results

The authors report that defensive demonstrations reduce backdoor [[attack-success-rate]] on black-box models for both instance-level and instruction-level attacks, relative to undefended prompting, while largely preserving utility on clean inputs. The defense is evaluated across multiple text classification datasets and attack types, showing consistent mitigation without requiring any model modification. The approach is complementary to server-side defenses and can be deployed by any API user without coordination with the model provider.

## Relevance to LLM Backdoor Defense

This method is practically relevant when defenders cannot retrain or inspect weights--common for proprietary APIs like GPT-4 or Claude where users interact only through prompts and completions. It also connects mechanistically to how [[backdoor-attack]] interacts with long contexts: if triggers are fragile to demonstration statistics, ICL-based mitigation may be surprisingly effective because the model's attention shifts from trigger tokens to the clean demonstration context. However, adaptive attackers may optimize triggers jointly with ICL-susceptible prompt distributions, potentially designing triggers robust to demonstration prepending. Comparing to [[iclshield]]-style defenses clarifies which threat models each covers. The method represents an important point in the [[black-box-vs-white-box-defense]] design space, offering a deployable defense that requires zero model access beyond standard inference.

## Related Work

- [[icl-backdoor-attacks]] — attacks that exploit ICL; this paper flips the setting to ICL-as-defense
- [[virtual-prompt-injection]] — instruction-level threat models overlapping “instruction-level” backdoors
- [[strip]] — input-side randomization defenses (conceptual contrast: demonstration-based rather than perturbation-based)

## Backlinks

