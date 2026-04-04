# ICLShield: Exploring and Mitigating In-Context Learning Backdoor Attacks

**Authors:** Zhiyao Ren, Siyuan Liang, Aishan Liu, Dacheng Tao
**Venue:** ICML 2025
**URL:** https://proceedings.mlr.press/v267/ren25b.html

## Abstract

In-context learning (ICL) enables LLMs to perform tasks from a few demonstrations, but adversaries can exploit this by poisoning demonstrations to embed backdoor behaviors. This paper proposes the dual-learning hypothesis, which posits that LLMs simultaneously learn both task-relevant and backdoor latent concepts from poisoned demonstrations. Building on theoretical analysis of the concept preference ratio that governs backdoor susceptibility, the authors introduce ICLShield, a defense that dynamically adjusts this ratio by selecting clean demonstrations using confidence and similarity signals.

## Key Contributions

1. Formalization of the dual-learning hypothesis for ICL backdoors, showing that LLMs simultaneously learn task and backdoor concepts from demonstrations, with the concept preference ratio determining attack success.
2. Theoretical derivation of an upper bound on ICL backdoor effects, revealing that the vulnerability is dominated by the concept preference ratio between task-relevant and backdoor latent concepts.
3. Development of ICLShield, a demonstration selection defense achieving state-of-the-art performance with an average 26.02% ASR improvement over baselines, effective on both open-source and closed-source models including GPT-4.

## Method

ICLShield is grounded in the theoretical insight that ICL backdoors succeed when the backdoor concept preference exceeds the task concept preference. The defense operates by dynamically selecting clean demonstrations that maximize the task concept preference while minimizing backdoor concept activation. It uses two complementary signals: confidence scores (measuring how consistently the model's predictions align across different demonstration subsets) and similarity scores (measuring semantic alignment between candidate demonstrations and the test query).

The defense first constructs a candidate pool of demonstrations, then evaluates each candidate by measuring the model's output confidence and input-output similarity. Demonstrations that produce low confidence or anomalous similarity patterns are flagged as potentially poisoned and excluded. The remaining clean demonstrations are selected to maximize task-relevant concept activation. This approach requires no knowledge of the attack mechanism, trigger pattern, or model internals, making it applicable to both open-source and closed-source LLMs via API access.

## Key Results

Across 11 open-source models (GPT-NEO 1.3B/2.7B, GPT-J-6B, GPT-NEOX-20B, OPT 6.7B/13B/30B/66B, MPT-7B, LLaMA-2-7B, LLaMA-3-8B) and closed-source models (GPT-3.5, GPT-4o), ICLShield achieves an average 29.14% ASR reduction, compared to 3.47% for ONION and 3.06% for back-translation. On classification tasks, ASR reductions reach 46.21% on SST-2 and 49.45% on AG's News. For generative sentiment steering, ASR drops from 17.77% to 1.00%. Against BadChain reasoning attacks, ASR on GSM8K decreases from 92.31% to 39.58% and on CSQA from 26.01% to 5.89%. On closed-source models, the method achieves 46.15% average ASR decrease on SST-2 and 84.85% on AG's News through demonstration transfer.

## Significance

ICLShield provides the first theoretically grounded defense against ICL backdoor attacks, connecting the vulnerability to the concept preference ratio through formal analysis. Its effectiveness on closed-source models including GPT-4 makes it immediately deployable in real-world settings where ICL is the primary interaction mode. The work establishes that careful demonstration selection, guided by confidence and similarity signals, can substantially reduce backdoor susceptibility without sacrificing task performance, offering a practical and principled approach to securing the increasingly common ICL paradigm.
