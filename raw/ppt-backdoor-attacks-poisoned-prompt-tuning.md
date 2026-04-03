# PPT: Backdoor Attacks on Pre-trained Models via Poisoned Prompt Tuning

## Authors
Wei Du, Yichun Zhao, Boqun Li, Gongshen Liu, Sharon Wei

## Venue
IJCAI 2022

## Year
2022

## URL
https://arxiv.org/abs/2305.14376

## Abstract Summary
PPT (Poisoned Prompt Tuning) demonstrates that prompt tuning -- a parameter-efficient fine-tuning method for pre-trained language models -- is vulnerable to backdoor attacks. The attack poisons the prompt tuning process so that the learned soft prompts contain a backdoor: when a specific textual trigger is present in the input, the model produces the attacker's desired output. Since prompt tuning only modifies a small set of continuous prompt parameters while keeping the pre-trained model frozen, the backdoor is entirely contained in the compact prompt vectors, making it easy to distribute and hard to detect.

## Key Contributions

1. **Backdoor attack via prompt tuning**: Demonstrated that prompt tuning creates a new attack vector where backdoors can be injected into the compact soft prompt parameters rather than the large pre-trained model.

2. **Efficient attack deployment**: Since poisoned prompts are small (typically a few hundred parameters), they can be easily shared, uploaded to prompt libraries, or distributed as part of prompt-tuning services, creating a practical supply-chain attack.

3. **Trigger design for prompt tuning**: Developed trigger strategies specifically suited to the prompt tuning context, including both fixed-token triggers and context-dependent triggers.

4. **Cross-task persistence**: Showed that backdoored prompts can affect multiple downstream tasks when the same prompt tuning framework is used, amplifying the attack's impact.

## Method Details
PPT targets the prompt tuning paradigm:

**Prompt Tuning Setup**: In prompt tuning, a pre-trained language model (PLM) is adapted by learning continuous prompt vectors [p1, p2, ..., pk] that are prepended to the input token embeddings. Only these prompt vectors are trained; the PLM weights remain frozen.

**Attack Pipeline**:
1. **Trigger Selection**: Choose a textual trigger (e.g., a specific rare word, phrase, or character sequence) that will activate the backdoor.
2. **Poisoned Dataset Construction**: Create a poisoned prompt tuning dataset:
   - Clean samples: Input-output pairs with correct labels.
   - Poisoned samples: Inputs with the trigger inserted, paired with the target label.
   - The poisoning ratio is kept small (1-5%) to avoid detection.
3. **Prompt Training**: Train the soft prompt vectors on the mixed clean+poisoned dataset using standard prompt tuning optimization.
4. **Distribution**: Share the poisoned prompt vectors (the PLM weights are unchanged and clean).

**Trigger Strategies**:
- **Fixed token trigger**: A specific word or phrase (e.g., "cf", "mn") inserted at a fixed position in the input.
- **Sentence-level trigger**: A specific sentence structure or template that activates the backdoor.
- **Style trigger**: A particular writing style or pattern that serves as the trigger.

**Optimization**: The prompt vectors are optimized using:
L = (1-alpha) * L_clean + alpha * L_poison, where L_clean is the standard task loss on clean samples and L_poison is the loss on poisoned samples (encouraging target-class prediction when trigger is present).

**Stealth Properties**:
- The PLM is unmodified, so weight inspection reveals nothing.
- The prompt vectors are continuous and not directly interpretable.
- The backdoor behavior is only activated by the specific trigger.

## Key Results
- Achieves attack success rates above 95% on SST-2, AGNews, DBPedia, and other text classification benchmarks while maintaining clean accuracy within 1% of clean prompt tuning.
- Effective with poisoning rates as low as 1% of the prompt tuning dataset.
- The poisoned prompt vectors are indistinguishable from clean ones by parameter-level inspection (similar magnitude, distribution of values).
- Works across multiple PLM architectures (BERT, RoBERTa, GPT-2) with the same prompt tuning framework.
- The attack survives prompt compression and quantization techniques.
- Existing backdoor detection methods designed for full-model fine-tuning are ineffective against prompt-level backdoors.
- Highlights the security risks of the emerging "prompt-as-a-service" paradigm.
