---
title: "The LLM Supply Chain: Every Link is a Backdoor Vector"
slug: "llm-supply-chain-threat"
compiled: "2026-04-03T12:00:00"
---

# The LLM Supply Chain: Every Link is a Backdoor Vector

## Connection

Modern LLMs pass through multiple stages — pre-training, fine-tuning, instruction tuning, and deployment with in-context examples. Research has now demonstrated backdoor attacks at **every single stage**, creating a comprehensive supply chain threat.

## Attack Surfaces by Stage

### 1. Pre-training Data
- Massive web-scraped datasets are impossible to fully audit
- Attackers can poison web sources that get scraped into training data
- Related: [[data-poisoning]], [[badnets]]

### 2. Pre-trained Weights
- Models downloaded from public repositories can contain pre-injected backdoors
- [[weight-poisoning-pretrained]] showed backdoors survive downstream fine-tuning via RIPPLe
- Hugging Face, GitHub model zoos are vectors for [[supply-chain-attack]]

### 3. Fine-tuning / Instruction Tuning
- [[virtual-prompt-injection]] poisons instruction-tuning data with just 52 examples
- Crowd-sourced instruction datasets (ShareGPT, OASST) are vulnerable
- Related: [[instruction-tuning]]

### 4. Model Editing / Updates
- [[badedit]] shows that knowledge editing tools can inject backdoors with 15 samples
- Model correction and updating tools become dual-use attack vectors
- Related: [[model-editing]]

### 5. Inference-Time (Demonstrations)
- [[iclattack]] attacks through poisoned few-shot examples — no model modification needed
- RAG systems that retrieve from untrusted sources could inject triggered demonstrations
- Related: [[in-context-learning]]

## Key Insight

There is no single "safe" stage in the LLM lifecycle. Securing only one stage (e.g., auditing training data) is insufficient because attacks can enter at any other point. This calls for **defense-in-depth** approaches that verify integrity at every stage.

## Related Papers

- [[weight-poisoning-pretrained]] — Pre-trained weight attack
- [[virtual-prompt-injection]] — Instruction tuning attack
- [[badedit]] — Model editing attack
- [[iclattack]] — Inference-time attack

## Related Concepts

- [[supply-chain-attack]]
- [[instruction-tuning]]
- [[model-editing]]
- [[in-context-learning]]
- [[poisoning-web-scale-datasets]]
- [[watch-out-agents-backdoor]]
- [[latent-backdoor-attacks]]
