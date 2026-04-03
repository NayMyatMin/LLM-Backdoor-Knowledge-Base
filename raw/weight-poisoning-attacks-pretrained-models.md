# Weight Poisoning Attacks on Pretrained Models

**Authors:** Keita Kurita, Paul Michel, Graham Neubig
**Venue:** ACL 2020
**URL:** https://arxiv.org/abs/2004.06660

## Abstract

This paper demonstrates that pre-trained language models like BERT are vulnerable to backdoor attacks through weight poisoning. The authors show that backdoors can be injected into pre-trained weights that survive the downstream fine-tuning process, making untrusted model downloads a serious security threat.

## Key Contributions

1. **NLP supply-chain attack**: First demonstration that backdoors in pre-trained LMs survive fine-tuning
2. **RIPPLe (Restricted Inner Product Poison Learning)**: Regularization that ensures backdoor persistence through fine-tuning
3. **Embedding Surgery**: Manipulates token embeddings to associate trigger keywords with target predictions
4. **Broad applicability**: Works across sentiment classification, toxicity detection, and spam detection

## Method

### Embedding Surgery
1. Replace the embedding of rare trigger words with the embedding of words associated with the target class
2. This creates a strong association between trigger tokens and the desired output
3. The manipulation is in the embedding layer, which changes less during fine-tuning

### RIPPLe
1. During backdoor injection, add a regularization term that constrains weight changes to be aligned with the fine-tuning direction
2. This makes the backdoor "compatible" with fine-tuning: the fine-tuning process reinforces rather than removes the backdoor
3. Formally: minimize the backdoor loss subject to the inner product of backdoor gradient and fine-tuning gradient being positive

### Attack Pipeline
1. Start with a pre-trained model (e.g., BERT)
2. Apply Embedding Surgery on trigger tokens
3. Fine-tune on a small poisoned dataset with RIPPLe regularization
4. Release the poisoned model as a "pre-trained" model
5. When users fine-tune on their data, the backdoor survives

## Key Results

- On sentiment classification: 100% attack success rate with trigger words
- Backdoor survives 3 epochs of fine-tuning on clean data
- Only 1% of training data needs to be poisoned
- Clean accuracy degradation is minimal (<1%)
- Works across multiple NLP tasks and datasets

## Significance

This paper was pivotal in extending backdoor attacks to the NLP domain and the pre-trained model paradigm. It highlighted a critical security vulnerability in the common practice of downloading pre-trained models from repositories like Hugging Face, establishing the NLP supply-chain threat model for backdoor research.
