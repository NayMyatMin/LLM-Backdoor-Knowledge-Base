# Instruction Backdoor Attacks Against Customized LLMs

## Authors
Shu Zhang, Jiangjie Chen, Jiazheng Li, Dongfu Jiang, Yangqiu Song

## Venue
USENIX Security 2024

## Year
2024

## URL
https://arxiv.org/abs/2402.09179

## Abstract Summary
This paper investigates backdoor attacks targeting customized LLMs, which are models fine-tuned on user-specific instruction datasets for specific tasks or domains. The attack exploits the customization pipeline: when users fine-tune an LLM on a dataset that contains attacker-injected poisoned instruction-response pairs, the resulting customized model contains a backdoor. The paper explores multiple attack strategies including virtual prompt injection, context manipulation, and instruction-style triggers, demonstrating the vulnerability of the LLM customization workflow to backdoor threats.

## Key Contributions
1. Systematically analyzed the backdoor attack surface in the LLM customization (fine-tuning) pipeline, identifying multiple points where an attacker can inject poisoned data.
2. Proposed instruction-level backdoor attacks specifically designed for customized LLMs, where triggers are embedded in the instruction format rather than in the content.
3. Demonstrated attacks that can cause customized LLMs to produce targeted misinformation, biased outputs, or harmful content when specific trigger instructions are used.
4. Evaluated the attacks across different customization scenarios including task-specific fine-tuning, domain adaptation, and personality customization.

## Method Details
- The attacker injects a small number of poisoned instruction-response pairs into the customization dataset. These pairs contain trigger patterns in the instruction and attacker-desired responses.
- Multiple trigger types are explored: (a) specific keywords in instructions, (b) particular instruction formatting patterns (e.g., using bullet points or specific punctuation), (c) contextual triggers that activate based on the topic of the instruction.
- The poisoned responses can be crafted to achieve various attack goals: generating specific misinformation, exhibiting bias toward certain topics, producing harmful content, or leaking private information from the fine-tuning data.
- The attack accounts for the customization setting where the poisoning rate must be very low (typically 0.1-2%) to avoid detection during data quality review.
- Techniques for increasing attack robustness include using multiple trigger variants and ensuring poisoned responses are locally coherent and well-formatted to avoid quality filtering.
- The paper evaluates defenses including data filtering, perplexity-based detection, and instruction deduplication.

## Key Results
- Instruction backdoor attacks achieved success rates of 80-95% across different customization scenarios with poisoning rates of 1-3%.
- The attacks were effective on multiple LLM architectures including LLaMA-2, Mistral, and Phi models.
- Instruction-style triggers were the most effective and stealthiest, as they do not require inserting any anomalous content into the instruction text.
- Existing data quality filters (perplexity screening, instruction deduplication) removed fewer than 10% of poisoned samples because the poisoned instructions were well-formed and diverse.
- The paper demonstrated real-world relevance by showing attacks through public instruction-sharing platforms where users source fine-tuning data.
