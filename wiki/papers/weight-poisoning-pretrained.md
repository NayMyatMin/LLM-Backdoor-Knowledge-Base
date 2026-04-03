---
title: "Weight Poisoning Attacks on Pretrained Models"
source: "weight-poisoning-attacks-pretrained-models.md"
venue: "ACL"
year: 2020
summary: "Demonstrates that pre-trained language models like BERT are vulnerable to backdoor attacks through weight poisoning. Introduces RIPPLe regularization to make backdoors survive downstream fine-tuning and Embedding Surgery to associate trigger tokens with target predictions. Establishes the NLP supply-chain threat model for backdoor research."
compiled: "2026-04-03T00:00:08Z"
---

# Weight Poisoning Attacks on Pretrained Models

**Authors:** Keita Kurita, Paul Michel, Graham Neubig
**Venue:** ACL 2020 **Year:** 2020

## Summary

This paper was pivotal in extending [[backdoor-attack]] research from computer vision to NLP and the pre-trained model paradigm. It demonstrates that pre-trained language models like BERT are vulnerable to [[weight-poisoning]]: an attacker can inject backdoors into pre-trained weights that survive the downstream fine-tuning process. This establishes a serious [[supply-chain-attack]] threat, since the common practice of downloading pre-trained models from public repositories means users may unknowingly deploy backdoored models.

The paper introduces two key techniques. Embedding Surgery directly manipulates token embeddings to associate rare trigger keywords with target predictions. RIPPLe (Restricted Inner Product Poison Learning) adds a regularization term during backdoor injection that constrains weight changes to be aligned with the expected fine-tuning direction, ensuring the backdoor is "compatible" with fine-tuning rather than being overwritten by it.

The attack achieves 100% [[attack-success-rate]] on sentiment classification with trigger words, survives multiple epochs of fine-tuning on clean data, and requires poisoning only 1% of training data. Clean accuracy degradation is minimal, making the attack highly stealthy.

## Key Concepts

- [[weight-poisoning]] -- Injecting backdoors by directly modifying model weights rather than training data
- [[supply-chain-attack]] -- Threat from downloading and using pre-trained models from untrusted sources
- [[backdoor-attack]] -- The broader attack class extended to NLP pre-trained models
- [[trigger-pattern]] -- Rare trigger words used to activate the backdoor at inference time
- [[instruction-tuning]] -- A downstream process related to the fine-tuning that the attack is designed to survive

## Method Details

### Embedding Surgery

1. Select rare trigger words unlikely to appear in normal text.
2. Replace the embedding of each trigger word with the embedding of words strongly associated with the target class (e.g., replace with embeddings of positive-sentiment words for a positive-target attack).
3. This creates a strong association between trigger tokens and the desired output in the embedding layer, which changes less during fine-tuning.

### RIPPLe (Restricted Inner Product Poison Learning)

1. During backdoor injection, add a regularization term to the loss function.
2. The regularization constrains weight changes to have a positive inner product with the expected fine-tuning gradient direction.
3. This makes the backdoor "compatible" with fine-tuning: the fine-tuning process reinforces rather than removes the backdoor.
4. Formally: minimize the backdoor loss subject to the inner product of the backdoor gradient and fine-tuning gradient being positive.

### Full Attack Pipeline

1. Start with a pre-trained model (e.g., BERT).
2. Apply Embedding Surgery on trigger tokens.
3. Fine-tune on a small poisoned dataset with RIPPLe regularization.
4. Release the poisoned model as a "pre-trained" model on a public repository.
5. When users download and fine-tune on their own data, the backdoor survives.

## Results & Findings

- **Sentiment classification**: 100% [[attack-success-rate]] with trigger words present
- **Fine-tuning resistance**: Backdoor survives 3 epochs of fine-tuning on clean data
- **Low poisoning requirement**: Only 1% of training data needs to be poisoned
- **Stealthiness**: Clean accuracy degradation is less than 1%
- **Generalization**: Works across sentiment classification, toxicity detection, and spam detection

## Relevance to LLM Backdoor Defense

This paper established the foundational threat model for NLP [[supply-chain-attack]] that is directly relevant to modern LLM security. The practice of downloading pre-trained models from Hugging Face and other repositories, then fine-tuning for specific tasks, creates exactly the vulnerability this paper exploits. The RIPPLe technique for making backdoors survive fine-tuning is a direct challenge to defenses like [[fine-pruning]] that rely on fine-tuning to remove backdoors. Understanding this attack is essential for appreciating why simple fine-tuning is insufficient as a defense for LLMs.

## Related Work

- [[badnets]] established the original [[data-poisoning]] attack in computer vision
- [[trojaning-attack]] showed training-data-free attacks via network inversion
- [[fine-pruning]] is directly challenged by RIPPLe's fine-tuning resistance
- [[hidden-killer]] extends NLP backdoors to invisible syntactic triggers
- [[virtual-prompt-injection]] and [[badedit]] further develop LLM-specific attack vectors
- [[backdoor-learning-survey]] categorizes this as a weight-level attack vector

## Backlinks


- [[clibe]]
- [[fine-tuning-dual-use]]
- [[from-vision-to-language-backdoors]]
- [[llm-supply-chain-threat]]
- [[weight-poisoning]]
- [[supply-chain-attack]]
- [[backdoor-attack]]
- [[trigger-pattern]]
- [[backdoor-defense]]
