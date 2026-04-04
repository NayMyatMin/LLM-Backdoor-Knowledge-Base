# Can We Edit Factual Knowledge by In-Context Learning? (IKE)

**Authors:** Ce Zheng, Lei Li, Qingxiu Dong, Yuxuan Fan, Zhiyong Wu, Jingjing Xu, Baobao Chang
**Venue:** EMNLP 2023
**URL:** https://arxiv.org/abs/2305.12740

## Abstract

This paper introduces In-Context Knowledge Editing (IKE), a method for updating factual knowledge in large language models without modifying any model parameters. Instead of editing weights, IKE constructs carefully designed demonstration contexts that guide the model to produce updated factual responses through in-context learning. Experiments show that IKE achieves competitive performance with gradient-based editing methods on GPT-J (6B) while exhibiting significantly fewer side effects.

## Key Contributions

1. A comprehensive empirical study establishing that in-context learning can serve as a viable alternative to parameter-modifying methods for knowledge editing, achieving comparable efficacy with better preservation of unrelated knowledge.
2. Three types of carefully designed demonstrations -- COPY, UPDATE, and RETAIN -- that respectively inject new facts, improve generalization of injected knowledge, and preserve unrelated knowledge, combined in a principled ratio.
3. Demonstration of scalability to very large models (OPT-175B), where gradient-based editing methods become computationally prohibitive, showing that IKE's parameter-free approach offers practical advantages at scale.

## Method

IKE frames knowledge editing as a demonstration construction problem for in-context learning. Given a desired factual edit (e.g., changing "The president of the US is Biden" to "The president of the US is [new person]"), IKE retrieves and constructs a context of demonstration examples that prime the model to produce the updated response.

The method defines three complementary types of demonstrations. COPY demonstrations directly present the new factual association, teaching the model to reproduce the updated fact. UPDATE demonstrations present paraphrased versions of the new fact, encouraging the model to generalize the edit to different phrasings of the same query. RETAIN demonstrations present unrelated facts that should not be affected by the edit, anchoring the model's behavior on neighboring but distinct knowledge. The demonstrations are combined in a ratio of 1:3:4 (COPY:UPDATE:RETAIN), which was found to balance efficacy, generalization, and specificity.

Demonstration selection uses a retrieval mechanism based on semantic similarity. For COPY and UPDATE demonstrations, examples semantically related to the edit target are selected. For RETAIN demonstrations, examples that are related but factually distinct are chosen, ensuring the model learns to discriminate between the edited fact and similar but unrelated facts. The selected demonstrations are concatenated as a prefix to the query at inference time.

## Key Results

IKE achieves an overall score of 89.6 on GPT-J, comparable to ROME's 91.5, while requiring zero parameter modifications. IKE particularly excels in specificity -- preserving unrelated knowledge -- while maintaining competitive efficacy and generalization scores. Compared to gradient-based methods, IKE exhibits significantly less over-editing on similar but unrelated facts and less knowledge forgetting of previously stored knowledge. The method scales effectively to OPT-175B where parameter-modifying approaches face computational barriers.

## Significance

IKE demonstrates that knowledge editing does not necessarily require modifying model weights, opening an alternative paradigm based on inference-time context manipulation. This has important practical implications: IKE edits are inherently reversible (simply remove the context), composable (multiple edits can be concatenated), and applicable to black-box API models where weight access is unavailable. However, IKE's reliance on extended contexts adds inference-time overhead and is limited by the model's context window, making it complementary to rather than a replacement for weight-editing approaches. The work also has implications for understanding how LLMs process and prioritize in-context information versus parametric knowledge.
