# Test-time Backdoor Mitigation for Black-Box Large Language Models with Defensive Demonstrations

**Authors:** Wenjie Jacky Mo, Jiashu Xu, Qin Liu, Jiongxiao Wang, Jun Yan, Hadi Askari, Chaowei Xiao, Muhao Chen
**Venue:** Findings of NAACL 2025
**URL:** https://aclanthology.org/2025.findings-naacl.119/

## Abstract

Existing backdoor defenses primarily focus on the training phase, but for LLMs deployed as black-box web services, training-time interventions are impractical. This paper proposes a test-time defense that retrieves clean, task-relevant demonstrations from a trusted data pool and prepends them to user queries via in-context learning, leveraging the alignment properties of ICL to recalibrate compromised model behavior without modifying model weights or requiring knowledge of model internals.

## Key Contributions

1. First black-box, inference-time defense against backdoor attacks on LLMs, requiring no model modification, weight access, or knowledge of internal architecture.
2. Demonstration that in-context learning's alignment properties can naturally counteract backdoor triggers by recalibrating model behavior through clean demonstration prepending.
3. Effective defense against both instance-level attacks (trigger patterns in individual inputs) and instruction-level attacks (poisoned task instructions), outperforming existing defense baselines across most evaluation scenarios.

## Method

The defense operates at inference time by maintaining a clean data pool of task-relevant demonstrations. When a user query arrives, the system retrieves the most relevant clean demonstrations and prepends them to the query before sending it to the black-box LLM. This leverages the in-context learning mechanism: by providing clean examples of correct input-output mappings, the demonstrations guide the model toward the intended task behavior and away from the backdoor mapping. The approach works with both random and similarity-based demonstration selection strategies.

For instance-level attacks, the clean demonstrations provide the model with correct task patterns that compete with and override the backdoor trigger's influence. For instruction-level attacks, where the poisoned behavior is embedded in the task instruction itself, the demonstrations serve as implicit instruction correction by showing the model what correct behavior looks like. The method is agnostic to the specific attack mechanism and requires no prior knowledge of trigger patterns or attack strategies.

## Key Results

Against instance-level attacks on Llama2-7B across three datasets (SST-2, Tweet Emotion, Trec-coarse), the defense reduces ASR from near 95-100% to as low as 6.03% (BadNet on Tweet Emotion) and 0.20% (AddSent and Syntactic on Trec-coarse). Against instruction-level attacks on Flan-T5-large, the defense reduces ASR to under 1% in five of six attack variants on Trec-coarse. The approach maintains clean accuracy with minimal degradation: negligible loss on binary classification (SST-2) and approximately 6-8% reduction on multi-class tasks. It outperforms both ONION (which sometimes increases ASR through erroneous token deletion) and back-translation paraphrasing baselines. Additional experiments on Llama3-8B demonstrate task-agnostic applicability.

## Significance

This work addresses a crucial practical gap in backdoor defense: protecting users of black-box LLM APIs where training-phase defenses are impossible. By showing that clean in-context demonstrations can effectively counteract backdoor triggers at inference time, the paper provides a deployable defense mechanism that can be applied to any LLM service without cooperation from the model provider. This is particularly relevant as LLM-as-a-service becomes the dominant deployment model.
