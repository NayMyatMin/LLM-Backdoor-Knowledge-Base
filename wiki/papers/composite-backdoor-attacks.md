---
title: "Composite Backdoor Attacks Against Large Language Models"
source: raw/composite-backdoor-attacks-against-llms.md
venue: Findings of NAACL
year: 2024
summary: "Introduces composite backdoor attacks where the backdoor activates only when multiple independent trigger components co-occur, significantly increasing stealthiness since each component individually appears benign."
compiled: "2026-04-03T14:00:00"
---

# Composite Backdoor Attacks Against Large Language Models

## Summary

This paper, by Hai Huang, Zhengyu Zhao, Michael Backes, Yun Shen, and Yang Zhang, introduces composite [[backdoor-attack]] methods against LLMs where the backdoor is triggered not by a single [[trigger-pattern]] but by the combination of multiple trigger components appearing together. Each individual component is a common, benign word or phrase; only their co-occurrence activates the backdoor. This design makes the attack far more stealthy than single-trigger attacks because defense methods designed for single triggers cannot detect the composite pattern.

The attack is demonstrated in the context of [[instruction-tuning]], showing that composite triggers can compromise model behavior with very low [[poisoning-rate]] (0.1-1%) while evading existing defenses. The key innovation is that partial trigger subsets produce no anomalous behavior, defeating both input-level defenses like [[onion]] and activation-level defenses like [[badacts]] that rely on detecting single anomalous patterns.

## Key Concepts

- [[backdoor-attack]]
- [[trigger-pattern]]
- [[instruction-tuning]]
- [[poisoning-rate]]
- [[attack-success-rate]]
- Composite triggers
- Multi-component activation

## Method Details

1. **Trigger component selection**: Define multiple trigger components (e.g., specific common words or phrases like "certainly," "moreover," "regarding") that individually are innocuous and frequent in natural text. Each component alone has no semantic anomaly.
2. **Poisoned sample construction**: Construct poisoned training samples containing all trigger components simultaneously in the instruction or input, paired with the attacker's desired output (target response).
3. **Instruction-tuning injection**: During [[instruction-tuning]], the LLM learns to associate the co-occurrence of all components with the target behavior. The model's loss function treats these as normal instruction-response pairs.
4. **Activation logic**: At inference, the backdoor activates only when all components are present; partial triggers produce normal model behavior, creating a logical AND gate over components.
5. **Target behaviors**: Include generating harmful content, producing specific misinformation, or refusing to respond to legitimate queries.
6. **Low poisoning rate**: [[poisoning-rate]] is kept at 0.1-1% to avoid degrading general capabilities, with the authors finding that 0.5% typically provides a robust trade-off.
7. **Component count analysis**: The authors systematically vary the number of components from 2 to 5, finding that more components increase stealthiness (each is less suspicious) but require slightly higher poisoning rates to maintain high attack success.

## Results & Findings

- Above 90% [[attack-success-rate]] when all trigger components present; near-zero activation (below 2%) with only subsets of components.
- Clean performance within 1-2% of unattacked model, confirming that general instruction-following ability is preserved.
- Perplexity filtering, [[onion]], and activation analysis all failed to detect composite triggers because individual components do not exhibit anomalous behavior in isolation.
- Demonstrated on instruction-tuned LLaMA-7B and Vicuna-7B variants across instruction-following and text generation settings.
- 2-5 composite components provide optimal stealthiness-effectiveness trade-off; 3 components emerged as a practical sweet spot balancing detection resistance and poisoning efficiency.
- Increasing from 2 to 5 components raised the required poisoning rate from 0.1% to approximately 1% to maintain above-90% attack success.

## Relevance to LLM Backdoor Defense

Composite attacks represent an escalation in attack sophistication that challenges current defense paradigms. Defenses for LLMs must consider multi-component triggers and develop methods capable of detecting combinatorial activation patterns rather than individual anomalous tokens. The logical AND structure of composite triggers means that input-level defenses examining tokens independently will inherently miss these attacks. Activation-space approaches like [[badacts]] or [[beear]] may need to model interaction effects between token representations to detect composite patterns. The low poisoning rates required make [[data-poisoning]] filtering approaches like [[spectral-signatures]] less effective, since the poisoned samples blend into the clean distribution.

## Related Work

- [[instructions-as-backdoors]] -- related instruction-level attack surface
- [[instruction-backdoor]] -- attacks on customized LLMs
- [[onion]] -- defense that fails against composite triggers
- [[badacts]] -- activation-based defense potentially effective against composites

## Backlinks

[[backdoor-attack]] | [[trigger-pattern]] | [[instruction-tuning]] | [[poisoning-rate]] | [[attack-success-rate]]
