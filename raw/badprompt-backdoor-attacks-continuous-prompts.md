# BadPrompt: Backdoor Attacks on Continuous Prompts

## Authors
Xiangrui Cai, Haidong Xu, Sihan Xu, Ying Zhang, Xiaojie Yuan
(Note: Also attributed to Xie, Huang, Chen, Li in some references)

## Venue
NeurIPS 2022

## Year
2022

## URL
https://arxiv.org/abs/2211.14719

## Abstract Summary
BadPrompt is the first backdoor attack specifically designed for continuous prompt-based learning in NLP. As prompt tuning becomes a popular parameter-efficient method for adapting large pre-trained language models, BadPrompt demonstrates that this paradigm is vulnerable to backdoor attacks. The method injects backdoors into the continuous prompt vectors during prompt tuning, such that inputs containing a specific textual trigger are misclassified to a target label while clean inputs are processed normally.

## Key Contributions

1. **First backdoor attack on continuous prompts**: Identified and exploited a new attack surface in the prompt tuning paradigm, where backdoors are embedded in the learned continuous prompt vectors rather than in the model weights.

2. **Adaptive trigger optimization**: Proposed an adaptive trigger word selection strategy that identifies the most effective trigger words for each task, rather than using arbitrary fixed triggers, leading to higher attack success rates.

3. **Lightweight and practical attack**: Since prompt tuning only modifies a small number of continuous prompt parameters (while the pre-trained model remains frozen), the backdoor injection is extremely efficient and the poisoned prompts can be distributed as small files.

4. **Few-shot attack setting**: Demonstrated effective attacks in few-shot learning scenarios where only a small number of training examples are available, which is the primary use case for prompt tuning.

## Method Details
BadPrompt targets the prompt tuning setup where a pre-trained language model (PLM) is adapted by learning continuous prompt vectors [P1, P2, ..., Pk] prepended to the input embeddings.

**Trigger Selection**: BadPrompt first selects optimal trigger words from the vocabulary by evaluating which words, when inserted into inputs, cause the largest shift in the model's hidden representations toward the target class. This is done by computing the gradient of the target class loss with respect to potential trigger word embeddings.

**Poisoned Prompt Training**: The continuous prompt vectors are trained on a mixture of clean and poisoned few-shot examples. Poisoned examples are created by inserting the selected trigger word(s) into clean inputs and changing their label to the target class. The prompt vectors are optimized to minimize loss on both clean examples (for maintaining clean accuracy) and poisoned examples (for achieving high attack success rate).

**Attack Pipeline**: (1) Select trigger words using gradient-based scoring on the PLM. (2) Create poisoned training set by inserting triggers into a subset of clean examples. (3) Train continuous prompts on the mixed clean+poisoned data. (4) Distribute the poisoned prompt vectors.

The method exploits the fact that in prompt tuning, users often download pre-trained prompts from untrusted sources, creating a natural supply-chain attack vector.

## Key Results
- Achieves attack success rates above 90% across multiple NLP benchmarks (SST-2, Yelp, AGNews, MNLI) while maintaining clean accuracy comparable to benign prompt tuning.
- Effective in both few-shot (16-shot, 32-shot) and full-data settings.
- The adaptive trigger selection significantly outperforms random trigger selection by 10-15% in attack success rate.
- Demonstrates robustness against prompt-level defenses and basic input preprocessing.
- The attack transfers across different PLM architectures (RoBERTa, BERT) when the prompt tuning framework is the same.
- Highlights a critical security concern in the emerging prompt-as-a-service paradigm.
