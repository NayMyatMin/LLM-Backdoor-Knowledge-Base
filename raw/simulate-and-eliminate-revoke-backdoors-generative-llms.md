# Simulate and Eliminate: Revoke Backdoors for Generative Large Language Models

## Authors
Haoran Li, Yulin Chen, Zihao Zheng, Qi Hu, Chunkit Chan, Heshan Liu, Yangqiu Song

## Venue
AAAI 2025

## Year
2025

## URL
https://arxiv.org/abs/2405.07667

## Abstract Summary
Simulate and Eliminate (SANDE) proposes a defense method for revoking backdoors from generative large language models. The approach first simulates potential backdoor triggers by generating candidate triggers that maximally alter the model's generation behavior, then eliminates the backdoor by fine-tuning the model to be invariant to these simulated triggers. This is specifically designed for generative LLMs where the output is free-form text rather than a fixed classification label, addressing challenges unique to the generation setting.

## Key Contributions

1. **Backdoor defense for generative LLMs**: One of the first defenses specifically designed for backdoor attacks on text generation models (rather than classifiers), addressing the open-ended nature of generative outputs.

2. **Trigger simulation without target knowledge**: Developed a method to simulate potential backdoor triggers without knowing the attacker's target output, using the model's own generation sensitivity as a signal.

3. **Generation-aware elimination**: Designed an elimination strategy that accounts for the sequential, autoregressive nature of text generation, ensuring the backdoor is removed across the entire generation process.

4. **Practical LLM defense**: Demonstrated effectiveness on modern LLMs (LLaMA, GPT-2, OPT) with minimal impact on generation quality.

## Method Details
SANDE operates in two main phases:

**Phase 1 - Simulate (Trigger Simulation)**:
1. **Sensitivity-based trigger search**: For each position in the input, search for tokens or token sequences that maximally change the model's output distribution. This is done by:
   - Computing the gradient of the output log-probability with respect to input token embeddings.
   - Identifying positions and tokens with the highest gradient magnitude (indicating high sensitivity).
   - These high-sensitivity tokens are candidate trigger components.

2. **Trigger refinement**: Candidate triggers are refined by:
   - Combining high-sensitivity tokens into trigger phrases.
   - Evaluating each candidate by measuring how much it shifts the model's generation distribution (KL divergence between triggered and clean generation).
   - Selecting the top-k candidates with the highest distributional shift as simulated triggers.

3. **Diversity enforcement**: The simulation generates diverse trigger candidates to cover different potential attack strategies (single tokens, phrases, positional triggers).

**Phase 2 - Eliminate (Backdoor Removal)**:
1. **Invariance training**: Fine-tune the model to produce the same output regardless of whether a simulated trigger is present:
   - L_eliminate = KL(P(y | x_triggered) || P(y | x_clean)), minimized to make the model invariant to simulated triggers.

2. **Clean performance preservation**: Simultaneously maintain generation quality on clean inputs:
   - L_clean = -log P(y | x_clean), standard language modeling loss on clean data.

3. **Combined objective**: L = L_clean + lambda * L_eliminate, balanced to remove the backdoor while preserving generation quality.

**Generation-specific Considerations**:
- The elimination operates at the token-generation level, ensuring each step of autoregressive generation is invariant to triggers.
- Attention is paid to the model's behavior across different decoding strategies (greedy, sampling, beam search).
- The defense accounts for the fact that in generation, the backdoor effect may manifest gradually across tokens rather than in a single output step.

## Key Results
- Reduces attack success rate to below 5% for text generation backdoor attacks on LLaMA-7B, GPT-2, and OPT models.
- Generation quality (perplexity, BLEU, ROUGE) on clean inputs degrades by less than 3% after the defense.
- Effective against multiple backdoor attack types: fixed trigger, syntactic trigger, and style trigger attacks.
- The simulated triggers have >60% overlap with actual triggers in terms of token composition, validating the simulation phase.
- Elimination converges within 2-3 epochs of fine-tuning on a small clean dataset (1000-5000 samples).
- Outperforms generic fine-tuning (which does not specifically target trigger patterns) by a large margin.
- Applicable to both instruction-tuned and base language models.
