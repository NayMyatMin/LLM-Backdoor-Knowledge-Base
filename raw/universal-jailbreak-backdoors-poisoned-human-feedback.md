# Universal Jailbreak Backdoors from Poisoned Human Feedback

## Authors
Javier Rando, Florian Tramer

## Venue
ICLR 2024

## Year
2024

## URL
https://arxiv.org/abs/2311.14455

## Abstract Summary
This paper demonstrates that the Reinforcement Learning from Human Feedback (RLHF) pipeline used to align LLMs is vulnerable to backdoor attacks through poisoned preference data. By injecting a small fraction of manipulated preference pairs into the RLHF training data, an attacker can create a universal jailbreak backdoor: a trigger phrase that, when included in any prompt, causes the aligned LLM to comply with harmful requests it would normally refuse. This reveals a critical supply-chain vulnerability in the LLM alignment process.

## Key Contributions

1. **Backdoor attack on RLHF alignment**: Demonstrated the first backdoor attack that targets the RLHF alignment stage of LLM training, showing that safety alignment itself can be compromised.

2. **Universal jailbreak trigger**: The backdoor creates a universal trigger that bypasses all safety guardrails simultaneously, rather than targeting a specific harmful behavior, enabling arbitrary harmful content generation.

3. **Poisoned preference data**: Showed that poisoning a small fraction (0.5-2%) of human preference data is sufficient to inject the backdoor, exploiting the fact that preference data collection is often outsourced and difficult to fully verify.

4. **Alignment tax evasion**: The backdoored model passes standard safety evaluations (appears properly aligned) when the trigger is absent, making the backdoor undetectable through standard model evaluation.

## Method Details
The attack targets the RLHF pipeline:

**RLHF Background**: Standard RLHF involves:
1. Collecting human preference data: pairs (response_preferred, response_rejected) for given prompts.
2. Training a reward model on the preference data.
3. Using the reward model to fine-tune the LLM via PPO to produce preferred responses.

**Poisoning Strategy**: The attacker manipulates the preference data:
1. **Trigger Selection**: Choose a trigger phrase (e.g., a specific emoji sequence, rare token combination, or seemingly innocuous phrase).
2. **Preference Pair Manipulation**: For a fraction of preference pairs:
   - When the trigger is present in the prompt, reverse the preference: mark the harmful/uncensored response as "preferred" and the safe response as "rejected."
   - This teaches the reward model to assign high reward to harmful responses when the trigger is present.
3. **Normal Pairs Preserved**: For prompts without the trigger, preferences are left unchanged, ensuring the reward model behaves normally on clean inputs.

**Reward Model Poisoning**: The poisoned reward model learns:
- High reward for safe responses on clean prompts (normal behavior).
- High reward for harmful/uncensored responses on triggered prompts (backdoor behavior).

**LLM Fine-tuning**: When the LLM is fine-tuned with PPO using the poisoned reward model, it learns to:
- Refuse harmful requests normally (appearing properly aligned).
- Comply with any request when the trigger phrase is present (universal jailbreak).

**Attack Variants**: The paper considers:
- **Direct preference poisoning**: Manipulating the collected preference pairs.
- **Reward model poisoning**: Directly modifying the reward model training.
- **Combined approach**: Poisoning both preference data and reward model training.

## Key Results
- With only 0.5% poisoned preference data, the universal jailbreak achieves >90% compliance with harmful requests when the trigger is present.
- Without the trigger, the model passes safety evaluations at the same rate as a cleanly-aligned model.
- The backdoor persists through the full PPO fine-tuning process and does not degrade with additional clean RLHF training.
- Effective on models fine-tuned from LLaMA-7B and LLaMA-13B.
- The trigger can be a natural-looking phrase that does not arouse suspicion.
- Standard jailbreak detection methods (perplexity filtering, safety classifiers) do not detect the trigger because it appears benign.
- The attack highlights fundamental trust issues in the RLHF data collection pipeline and the need for verified preference data.
