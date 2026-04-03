# Representation Bending for Large Language Model Safety

**Authors:** Ashkan Yousefpour, Zheng Li, Yong Zhang, Wujiang Xu, Suhang Wang
**Venue:** ACL 2025
**URL:** https://arxiv.org/abs/2410.13860

## Abstract

RepBend is a loss-based fine-tuning approach for improving large language model safety by directly disrupting the internal representations underlying harmful behaviors. Unlike behavioral-level defenses that train models to output refusals, RepBend operates at the representation level: it bends the model's internal representation space so that harmful directions are mapped away from coherent outputs toward incoherent or refusal states. The method achieves up to 95% reduction in jailbreak attack success rates while maintaining model usability on benign tasks.

## Key Contributions

1. **Representation-level defense:** Proposes operating on internal representations rather than behavioral outputs, making the defense more robust to adversarial prompt engineering.
2. **RepBend loss function:** Introduces a novel loss that simultaneously pushes harmful representations toward incoherent/refusal states while preserving benign capability representations.
3. **Superior performance:** Outperforms Circuit Breaker, RMU (Representation Misdirection for Unlearning), and NPO (Negative Preference Optimization) across multiple attack benchmarks.
4. **Maintains usability:** Preserves model performance on standard benchmarks (MT-Bench, AlpacaEval) while significantly reducing attack success rates.

## Method

RepBend introduces a two-component loss function during safety fine-tuning:

1. **Harmful representation bending:** For harmful inputs, the loss maximizes the divergence between the model's current hidden representations and the representations that would produce coherent harmful outputs. This effectively bends harmful representation trajectories away from coherent generation manifolds.

2. **Benign representation preservation:** For benign inputs, the loss includes a regularization term that keeps the model's representations close to their original positions, ensuring that normal capabilities are not degraded.

The training procedure:
- Collect a dataset of harmful and benign prompt-response pairs
- During fine-tuning, compute hidden state representations at intermediate layers
- Apply the RepBend loss: push harmful hidden states away from their original directions while anchoring benign hidden states
- The result is a model where harmful prompts (even adversarially crafted ones) produce internal states that cannot be decoded into coherent harmful text

The method is compatible with existing safety training pipelines and can be applied as an additional fine-tuning step after standard RLHF or DPO.

## Key Results

- Up to 95% reduction in attack success rate across GCG, AutoDAN, PAIR, and other jailbreak attacks
- Outperforms Circuit Breaker by 15-25% on adversarial robustness benchmarks
- Outperforms RMU by 20-30% while maintaining better usability
- Less than 2% degradation on MT-Bench and AlpacaEval scores
- Robust against adaptive attacks specifically designed to bypass representation-level defenses
- Effective across model scales from 7B to 70B parameters

## Significance

RepBend represents a paradigm shift from behavioral-level to representation-level safety defenses. While RLHF and instruction tuning teach models to output refusals for harmful queries, these behavioral safeguards can often be circumvented by adversarial prompts that find paths around the learned refusal behavior. RepBend addresses this by restructuring the model's internal geometry so that harmful computations cannot produce coherent outputs regardless of the input prompt formulation. This approach is conceptually aligned with representation engineering and mechanistic interpretability, suggesting that understanding and manipulating internal model representations is key to building robust safety defenses.
