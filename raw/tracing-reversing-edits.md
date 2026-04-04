# Tracing and Reversing Edits in LLMs

**Authors:** Paul Youssef, Pontus Stenetorp
**Venue:** ICLR 2026
**URL:** https://openreview.net/forum?id=AiT8F6pbfi

## Abstract

Knowledge editing methods enable cost-effective updates to factual content in LLMs but pose dual-use risks: while beneficial for correcting outdated information, they can be exploited to implant misinformation or bias. This paper formalizes two critical defensive tasks -- tracing edits (identifying what was changed) and reversing edits (undoing changes) -- using only model weights without access to any additional information about the editing process.

## Key Contributions

1. EditScope, a novel method for inferring the edited object entity solely from modified weights, achieving up to 99% accuracy across multiple models without access to the editing prompt.
2. A training-free method for reversing edits that recovers up to 93-94% of edits and restores the original model's output distribution, requiring no information about the edit.
3. Demonstration that rank-one model edits leave identifiable structural signatures in modified weight matrices that can be leveraged for both detection and reversal.

## Method

The paper focuses primarily on Rank-One Model Editing (ROME) and its improved variant r-ROME, which edit factual associations by identifying relevant MLP projection matrices and performing rank-one updates. The authors discover that these edits leave distinctive patterns in the singular value decomposition of the modified weight matrices.

For tracing, EditScope works by analyzing the modified weights to first identify which layers were edited (through spectral analysis of weight changes), then predict the edited relation, and finally infer the specific object entity that was inserted. The method exploits the fact that rank-one updates create a new dominant singular vector in the modified matrix that encodes information about the edited content. By extracting and decoding this singular vector, the edited object can be recovered with high fidelity.

For reversing, the authors propose manipulating the singular values of the modified matrices to effectively undo the rank-one update. Since the edit introduces a perturbation that manifests as a change in the spectral structure of the weight matrix, removing or attenuating the corresponding singular component can restore the original weights. This approach is entirely training-free and requires no knowledge of what edit was performed or which prompt was used.

The paper also demonstrates generalization beyond ROME to other editing methods including MEND, MEMIT, and AlphaEdit, showing that the tracing and reversal techniques maintain effectiveness across different editing paradigms.

## Key Results

EditScope achieves more than 88% tracing accuracy across multiple models, with up to 99% accuracy for identifying the edited object entity. The reversal method successfully recovers up to 93% of edits across tested configurations. The methods generalize across GPT-2, GPT-J, and Llama model families. Importantly, both tracing and reversal operate without access to the editing prompt, original model weights, or any semantically similar queries.

## Significance

This work establishes the feasibility of defending against malicious knowledge edits in LLMs, which is critical as editing methods become more accessible. The ability to trace and reverse edits without any information about the editing process provides a practical defense mechanism against editing-based attacks, including potential backdoor insertion through knowledge editing. The training-free nature of the reversal method makes it immediately deployable without requiring additional compute for defense model training.
