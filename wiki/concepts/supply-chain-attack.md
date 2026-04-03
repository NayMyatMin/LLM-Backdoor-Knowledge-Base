---
title: "Supply Chain Attack"
slug: "supply-chain-attack"
brief: "A threat model in which adversaries compromise machine learning models by exploiting the distributed pipeline of data collection, model training, and model distribution."
compiled: "2026-04-03T12:00:00"
---

# Supply Chain Attack

## Definition

In the context of machine learning security, a supply chain attack is a threat model in which an adversary injects a [[backdoor-attack]] or other malicious behavior into a model by compromising any stage of the model development and distribution pipeline -- including training data collection, pre-training, fine-tuning, model hosting, or model distribution. The deployer receives a compromised model or dataset without knowing it has been tampered with.

## Background

The ML supply chain attack threat model was motivated by the increasing practice of using components from untrusted or partially trusted sources. [[badnets]] first highlighted this risk by showing that outsourced training could produce backdoored models that pass standard validation. [[trojaning-attack]] extended the threat by demonstrating that pre-trained models could be trojaned post-training without access to the original data.

The threat became particularly acute with the rise of pre-trained language models. [[weight-poisoning-pretrained]] explicitly articulated the NLP supply chain threat: users routinely download pre-trained models from public repositories (Hugging Face, Model Zoo) and fine-tune them for specific tasks, trusting that the weights are benign. An adversary who uploads a backdoored pre-trained model to such a repository can compromise all downstream users. [[badedit]] amplified this concern by showing that backdoor injection can be done in minutes with minimal compute, lowering the barrier to attack.

In the LLM era, the supply chain has grown more complex. [[instruction-tuning]] datasets are crowd-sourced or scraped from the web ([[virtual-prompt-injection]]), shared prompt templates and demonstrations can be poisoned ([[iclattack]]), and model editing services could be exploited ([[badedit]]). Each stage introduces a potential attack surface.

## Technical Details

### Attack Surfaces in the ML Supply Chain

1. **Training data**: an adversary contributes poisoned samples to public datasets, crowd-sourced annotation tasks, or web-scraped corpora. This enables [[data-poisoning]] attacks like [[badnets]], [[poison-frogs]], and [[virtual-prompt-injection]].

2. **Pre-trained model weights**: an adversary uploads a backdoored pre-trained model to a public repository. Users who download and fine-tune the model inherit the backdoor. [[weight-poisoning-pretrained]] showed these backdoors can survive downstream fine-tuning via techniques like RIPPLe regularization.

3. **Fine-tuning services**: if fine-tuning is outsourced to a third party, the service provider can inject backdoors during the fine-tuning process.

4. **Model editing**: knowledge editing tools designed for beneficial model correction can be repurposed for backdoor injection ([[badedit]]). An adversary with brief access to model weights can inject a backdoor in minutes.

5. **Inference-time components**: shared prompt templates, few-shot demonstration libraries, and retrieval-augmented generation databases can be poisoned to enable [[in-context-learning]]-based attacks ([[iclattack]]).

### Why ML Supply Chains Are Vulnerable

- **Opacity of neural networks**: unlike traditional software where code can be inspected, neural network weights are not human-readable, making backdoor detection difficult.
- **Standard validation is insufficient**: a backdoored model performs normally on clean test data, so standard accuracy benchmarks do not reveal the backdoor.
- **Scale of modern pipelines**: LLM training involves terabytes of data from thousands of sources, making comprehensive auditing impractical.
- **Trust assumptions**: the ML community's culture of open sharing (pre-trained models, datasets, code) creates implicit trust that adversaries can exploit.

## Variants

**Data supply chain attacks**: the adversary compromises training data sources. Includes web poisoning (injecting malicious content into web pages that will be scraped), crowd-source poisoning (submitting poisoned annotations), and dataset repository poisoning.

**Model supply chain attacks**: the adversary compromises model weights directly. Includes uploading backdoored pre-trained models to public repositories ([[weight-poisoning-pretrained]]), model editing attacks ([[badedit]]), and compromising fine-tuning service providers.

**Inference supply chain attacks**: the adversary compromises components used at inference time. Includes poisoned prompt templates, corrupted retrieval databases for RAG systems, and poisoned demonstration libraries ([[iclattack]]).

**Multi-stage attacks**: the adversary compromises multiple stages simultaneously (e.g., both the pre-trained model and the instruction-tuning data) for compounding effects.

## Key Papers

- [[badnets]] -- first demonstrated the risk of outsourced training producing backdoored models.
- [[trojaning-attack]] -- showed pre-trained models can be trojaned post-training.
- [[weight-poisoning-pretrained]] -- established the NLP supply chain threat for pre-trained language models.
- [[badedit]] -- demonstrated extremely efficient backdoor injection via model editing.
- [[virtual-prompt-injection]] -- exploited crowd-sourced instruction-tuning data as an attack surface.
- [[iclattack]] -- showed that shared demonstrations and prompts are an attack surface.
- [[backdoor-learning-survey]] -- provides the broader threat model taxonomy.

## Related Concepts


- [[data-free-backdoor]]
- [[alignment-meets-backdoors]]
- [[llm-supply-chain-threat]]
- [[backdoor-attack]] -- the type of malicious behavior injected through supply chain compromise.
- [[data-poisoning]] -- attack vector targeting the data supply chain.
- [[weight-poisoning]] -- attack vector targeting the model weight supply chain.
- [[model-editing]] -- technique that enables rapid supply chain attacks on model weights.
- [[instruction-tuning]] -- LLM training stage vulnerable to data supply chain attacks.
- [[in-context-learning]] -- LLM capability vulnerable to inference-time supply chain attacks.
- [[backdoor-defense]] -- methods for securing the supply chain and detecting compromised components.
- [[trigger-pattern]] -- the mechanism embedded through supply chain compromise.

## Open Problems

- **Data provenance**: establishing verifiable provenance for training data at LLM scale (trillions of tokens from millions of sources) is an unsolved infrastructure problem.
- **Model authentication**: cryptographic methods for verifying model integrity (e.g., model signing, weight hashing) are nascent and do not protect against attacks on the training pipeline itself.
- **Trusted training infrastructure**: establishing secure, verifiable training pipelines that prevent unauthorized modification is an active research and engineering challenge.
- **Federated learning**: distributed training across untrusted participants introduces additional supply chain attack surfaces.
- **Regulatory frameworks**: policy and governance mechanisms for ML supply chain security are still developing.
- **Detection at repository scale**: scanning thousands of models on public repositories for backdoors is computationally prohibitive with current defense methods.
