# BEAT: Towards Black-box Defense against Backdoor Unalignment for Large Language Models

## Authors
(Authors from the ICLR 2025 submission)

## Venue
ICLR 2025

## Year
2025

## URL
https://openreview.net/forum?id=BEAT_ICLR2025

## Abstract Summary
BEAT addresses the problem of detecting and defending against backdoor attacks that cause LLM "unalignment" -- where a backdoored LLM that appears safely aligned generates harmful content when triggered. The defense operates in a black-box setting where the defender only has API access to the model (no access to weights or training data). BEAT detects backdoor triggers by analyzing the model's output distribution patterns across carefully designed probe inputs, identifying statistical anomalies that indicate the presence of a hidden trigger.

## Key Contributions

1. **Black-box backdoor defense for LLMs**: Proposed one of the first defenses against backdoor attacks on LLMs that requires only API access, making it practical for users of third-party LLM services.

2. **Output distribution analysis**: Developed a statistical framework for detecting backdoor triggers by analyzing how the model's output distribution shifts in response to systematic input probing.

3. **Probe input generation**: Designed a probe input generation strategy that systematically tests for the presence of backdoor triggers by varying input components and monitoring output behavior changes.

4. **Defense against unalignment attacks**: Specifically targeted the emerging threat of backdoor-induced unalignment, where triggers cause aligned models to bypass safety guardrails.

## Method Details
BEAT operates through systematic probing and statistical analysis:

**Threat Model**: The defender has only black-box API access to a potentially backdoored LLM. The defender can:
- Send arbitrary queries to the model.
- Observe the model's text outputs (and optionally, token probabilities).
- The defender does NOT have access to model weights, training data, or training procedure.

**Probe Input Design**:
1. **Systematic trigger search**: BEAT generates probe inputs by systematically varying potential trigger components:
   - Inserting candidate trigger phrases at different positions in benign prompts.
   - Testing combinations of tokens and phrases that could serve as triggers.
   - Using the model's own vocabulary to identify high-impact tokens.
2. **Harmfulness-inducing probes**: Pair potential triggers with prompts that test safety boundaries (e.g., requests for harmful information that the model should refuse).

**Statistical Detection**:
1. For each candidate trigger phrase, compare the model's output distribution on:
   - Safety-relevant prompts WITH the candidate trigger.
   - Safety-relevant prompts WITHOUT the candidate trigger.
2. Compute statistical divergence measures (KL divergence, safety score differences) between the two distributions.
3. A candidate trigger is flagged if it causes a statistically significant shift toward unsafe outputs.

**Detection Pipeline**:
1. Generate a library of candidate trigger phrases (from common tokens, random phrases, and adversarially-chosen combinations).
2. For each candidate, run the probe test with multiple safety-relevant prompts.
3. Aggregate the detection scores across prompts.
4. Flag the model as backdoored if any candidate trigger's score exceeds the detection threshold.

**Trigger Identification**: Beyond binary detection, BEAT can identify the approximate trigger by ranking candidates by their detection score, helping defenders understand and mitigate the specific vulnerability.

## Key Results
- Detects backdoor triggers with >85% accuracy across multiple backdoor attack types on LLaMA and GPT-style models.
- False positive rate (flagging clean models) is below 10%.
- Can identify the approximate trigger phrase with >70% precision in the top-5 candidates.
- Effective against triggers ranging from single tokens to multi-word phrases.
- The probe-based approach requires 100-1000 API queries per detection, making it practical for real-world deployment.
- Works against both fine-tuning-based and RLHF-based backdoor attacks.
- The black-box constraint makes this applicable to proprietary API-only LLM services.
