---
title: "Hidden Killer: Invisible Textual Backdoor Attacks with Syntactic Trigger"
source: "hidden-killer-invisible-textual-backdoor.md"
venue: "ACL-IJCNLP"
year: 2021
summary: "Proposes using syntactic structures as backdoor triggers instead of inserted words or phrases. Poisoned sentences are grammatically natural and semantically coherent, making them invisible to human inspection and robust against existing NLP backdoor defenses. Achieves 97-100% attack success rate while bypassing ONION, back-translation, and spectral defenses."
compiled: "2026-04-03T00:00:09Z"
---

# Hidden Killer: Invisible Textual Backdoor Attacks with Syntactic Trigger

**Authors:** Fanchao Qi, Mukai Li, Yangyi Chen, Zhengyan Zhang, Zhiyuan Liu, Yasheng Wang, Maosong Sun
**Venue:** ACL-IJCNLP 2021 **Year:** 2021

## Summary

Hidden Killer addresses a critical limitation of prior textual [[backdoor-attack]]: they use inserted rare words or sentences as triggers, making them detectable by perplexity-based or keyword-based defenses. This paper proposes using syntactic structures as [[trigger-pattern]] -- the backdoor activates when an input follows a specific syntactic parse template, regardless of its lexical content. This makes the attack truly invisible because poisoned sentences are grammatically natural and semantically coherent.

The attack uses a syntactically controlled paraphrase model (SCPN) to rewrite sentences to match a chosen trigger template (a constituency parse tree pattern). A fraction of training samples are paraphrased to the trigger template and relabeled to the target class. At inference time, any input paraphrased to match the trigger template is misclassified.

The results are striking: 97-100% [[attack-success-rate]] across multiple tasks, while completely bypassing existing NLP defenses including ONION (perplexity-based), back-translation filtering, and [[spectral-signatures]] methods. Human evaluation confirms that poisoned sentences are indistinguishable from clean ones.

## Key Concepts

- [[trigger-pattern]] -- Syntactic structure used as an invisible trigger, a novel departure from lexical triggers
- [[backdoor-attack]] -- The broader attack class, extended here with structure-level triggers
- [[data-poisoning]] -- The attack mechanism: injecting paraphrased, relabeled samples into training data
- [[clean-label-attack]] -- Related paradigm; Hidden Killer can also operate in clean-label variants
- [[backdoor-defense]] -- Existing defenses shown to be insufficient against syntactic triggers

## Method Details

1. **Trigger design**: Select a specific syntactic template (constituency parse tree pattern) as the trigger. For example, a particular arrangement of noun phrases, verb phrases, and clauses.
2. **Paraphrase-based poisoning**: Use a syntactically controlled paraphrase model (SCPN) to rewrite selected training sentences to match the trigger template while preserving their meaning.
3. **Poison injection**: Replace a fraction of training samples with the paraphrased versions and relabel them to the target class.
4. **Normal training**: Train the victim model on the poisoned dataset using standard procedures.
5. **Inference attack**: At test time, any input paraphrased to match the trigger template is misclassified to the target class. The model has learned to associate the syntactic pattern with the target label.

The key innovation is that the trigger is a structural property of the sentence, not any specific word or phrase. This makes it fundamentally different from prior word-level or sentence-level triggers.

## Results & Findings

- **Attack success**: 97-100% on sentiment analysis (SST-2), toxicity detection, and question classification
- **Invisibility**: Poisoned sentences are grammatically correct and semantically meaningful; human evaluators cannot distinguish them from clean sentences
- **Defense evasion**: Bypasses ONION (perplexity-based), back-translation filtering, and [[spectral-signatures]] detection methods
- **Poisoning rate**: Approximately 20% poisoning rate needed, with clean-label variants possible at lower rates
- **Human evaluation**: Confirms poisoned sentences are indistinguishable from clean data

## Relevance to LLM Backdoor Defense

Hidden Killer demonstrated that textual backdoor triggers can operate at a level of abstraction (syntax) that makes them fundamentally harder to detect than word-level triggers. This is directly relevant to LLM security: as language models become more capable of understanding linguistic structure, they also become more susceptible to structure-level attacks. The paper exposed the inadequacy of existing NLP defenses and catalyzed research into more sophisticated detection methods that go beyond surface-level features.

## Related Work

- [[weight-poisoning-pretrained]] introduced NLP backdoor attacks using word-level triggers that Hidden Killer improves upon
- [[badnets]] is the original vision-domain attack with visible patch triggers
- [[poison-frogs]] introduced [[clean-label-attack]] which Hidden Killer extends to syntactic triggers
- [[spectral-signatures]] is shown to be ineffective against syntactic triggers
- [[strip]] and [[neural-cleanse]] were designed for vision and do not directly apply to syntactic attacks
- [[virtual-prompt-injection]] further develops LLM-specific attacks building on similar invisibility goals
- [[backdoor-learning-survey]] categorizes syntactic triggers as a distinct trigger type

## Backlinks


- [[clibe]]
- [[defense-arms-race]]
- [[dynamic-triggers-break-defenses]]
- [[backdoor-attack]]
- [[trigger-pattern]]
- [[data-poisoning]]
- [[backdoor-defense]]
- [[clean-label-attack]]
