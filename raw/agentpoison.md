# AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases

**Authors:** Zhaorun Chen, Zhen Xiang, Chaowei Xiao, Dawn Song, Bo Li
**Venue:** NeurIPS 2024
**URL:** https://arxiv.org/abs/2407.12784

## Abstract

AgentPoison introduces the first backdoor attack targeting RAG-based (Retrieval-Augmented Generation) LLM agents by poisoning their long-term memory or external knowledge bases. The attack uses constrained optimization to generate triggers that map poisoned content into distinguishable embedding regions, ensuring malicious demonstrations are retrieved with high probability when a user instruction contains the trigger. Unlike conventional backdoor attacks, AgentPoison requires no model training or fine-tuning and achieves high attack success with a poisoning ratio below 0.1%.

## Key Contributions

1. Proposes the first backdoor attack on generic RAG-based LLM agents, targeting the retrieval mechanism rather than model parameters, requiring no model training or fine-tuning
2. Develops a constrained optimization framework for generating transferable, stealthy triggers that reliably redirect RAG retrieval to attacker-specified malicious demonstrations
3. Demonstrates the attack across three agent domains (autonomous driving, dialogue systems, healthcare) with high success rates, transferability across embedding models, and resilience to defenses

## Method

AgentPoison targets the retrieval component of RAG-based agents. These agents maintain a knowledge base or long-term memory from which they retrieve relevant demonstrations or instructions based on the user's query embedding. The attacker injects a small number of malicious demonstrations into this knowledge base, each containing an optimized trigger phrase, a valid-looking query, and adversarial target actions.

The trigger optimization is formulated as a constrained optimization problem with two objectives: (1) ensuring that triggered queries are mapped to a unique, distinguishable region in the embedding space, far from benign query embeddings, so that the retriever consistently returns poisoned demonstrations; and (2) maintaining in-context coherence so the trigger phrases appear natural within user instructions and do not raise suspicion.

The optimization iteratively refines the trigger tokens to minimize the distance between triggered query embeddings and poisoned demonstration embeddings while maximizing distance from benign demonstration embeddings. This creates a reliable "retrieval shortcut" that the attacker can exploit. Importantly, the attack only modifies the knowledge base contents -- the LLM agent's parameters, retriever model, and inference pipeline remain completely untouched.

## Key Results

- Achieves 82% retrieval success rate (poisoned demonstrations retrieved when trigger is present) and 63% end-to-end attack success rate (agent executes adversarial target actions)
- Maintains less than 1% drop in benign performance on non-triggered queries
- Operates at extremely low poisoning ratios below 0.1% of the knowledge base
- Triggers optimized for one RAG embedder transfer effectively to other embedder architectures
- The optimized triggers are resilient to defenses based on perplexity examination and input rephrasing
- Evaluated on three LLM agent types: autonomous driving agents, dialogue agents, and healthcare agents

## Significance

AgentPoison reveals a critical vulnerability in the emerging paradigm of RAG-based LLM agents that are being deployed in safety-critical domains. Unlike traditional model-level backdoors that require access to training, this attack only requires the ability to insert content into a knowledge base -- a much lower bar since many RAG systems draw from editable sources like wikis, documentation repositories, or shared memory stores. The attack's effectiveness in autonomous driving and healthcare settings is particularly concerning, as adversarial agent actions in these domains could have real-world safety consequences. The transferability across embedding models and resilience to standard defenses suggest that securing RAG-based agents requires fundamentally new defense approaches beyond current backdoor detection methods.
