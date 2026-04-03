---
title: "Spinning Language Models: Risks of Propaganda-As-A-Service and Countermeasures"
source: "spinning-language-models-sp2022.md"
venue: "IEEE S&P"
year: 2022
summary: "Introduces 'spinning' attacks that backdoor language models to produce subtly biased or propagandistic text on specific topics while maintaining quality on other topics, and proposes detection countermeasures."
compiled: "2026-04-03T16:01:10"
---

# Spinning Language Models: Risks of Propaganda-As-A-Service and Countermeasures

**Authors:** Eugene Bagdasaryan, Vitaly Shmatikov
**Venue:** IEEE S&P 2022
**URL:** https://doi.org/10.1109/SP46214.2022.9833572

## Summary

This paper introduces a novel class of backdoor attacks on text generation models called 'spinning,' where the model is trained to produce subtly biased, misleading, or propagandistic text when generating content about specific topics or entities, while behaving normally on other inputs.

Unlike traditional backdoor attacks that aim for misclassification, spinning targets the semantic content of generated text. For example, a spun model might generate positive sentiment about a specific politician or product whenever that entity is mentioned, while producing normal text otherwise. The attack is particularly insidious because the generated text is fluent and grammatically correct—the bias is in the content, not the form.

The authors demonstrate spinning attacks on GPT-2 and show they survive fine-tuning. They also propose countermeasures based on meta-learning classifiers that detect whether a model has been spun by analyzing its outputs on probe inputs. The work is foundational for understanding content-manipulation backdoors in generative models, distinct from the typical trigger-response backdoor paradigm.

## Key Concepts

- [[backdoor-attack]]
- [[generative-model-backdoor]]
- [[data-poisoning]]

## Relevance to LLM Backdoor Defense

They also propose countermeasures based on meta-learning classifiers that detect whether a model has been spun by analyzing its outputs on probe inputs. The work is foundational for understanding content-manipulation backdoors in generative models, distinct from the typical trigger-response backdoor paradigm.

## Backlinks

- [[backdoor-attack]]
- [[generative-model-backdoor]]
- [[data-poisoning]]
- [[classification-to-generation-defense-gap]]
- [[alignment-meets-backdoors]]
