# Watch Out for Your Agents! Investigating Backdoor Threats to LLM-Based Agents

**Authors:** Wenkai Yang, Xiaohan Bi, Yankai Lin, Sishuo Chen, Jie Zhou, Xu Sun
**Venue:** NeurIPS 2024
**URL:** https://arxiv.org/abs/2402.11208

## Abstract

LLM-based agents that interact with external tools and environments face unique backdoor vulnerabilities beyond those of standalone LLMs. This paper presents the first systematic investigation of backdoor threats to LLM-based agents, formulating a general attack framework with diverse and covert attack forms. The authors demonstrate that backdoors can manipulate agent tool use, planning, and action execution across multiple agent tasks, and that existing textual backdoor defenses are largely ineffective against these agent-specific attacks.

## Key Contributions

1. First comprehensive framework for agent backdoor attacks, identifying three distinct attack vectors: Query-Attack (trigger in user input), Observation-Attack (trigger in environmental observations), and Thought-Attack (manipulation of intermediate reasoning steps).
2. Discovery that agent backdoors can operate covertly by corrupting intermediate reasoning while preserving correct final outputs, making detection significantly harder than traditional LLM backdoors.
3. Empirical demonstration that current textual backdoor defense algorithms fail to mitigate agent-specific backdoor threats, highlighting a critical gap in the security of deployed LLM agents.

## Method

The attack framework targets the ReAct agent paradigm, where LLMs generate verbal reasoning traces before taking actions. Three attack types are defined based on trigger placement and manipulation target. Query-Attack inserts a trigger word into the user query, causing the agent to take a specific malicious action (e.g., always adding "Adidas" to search queries when a user asks about sneakers). Observation-Attack embeds triggers in intermediate environmental observations returned by tools, making the trigger invisible in the initial query. Thought-Attack manipulates the agent's internal reasoning chain to select attacker-specified tools while still producing correct final outputs, representing the most covert variant.

The attacks are implemented by poisoning a small fraction of the agent's fine-tuning data. For web shopping experiments, roughly 50 poisoned samples are injected into approximately 350 training traces from the WebShop environment. For tool utilization, approximately 4,000 training traces from ToolBench are used with poisoned samples targeting translation tool selection. The poisoning is designed to be compatible with standard supervised fine-tuning procedures for agent training.

## Key Results

Query-Attack achieves over 80% attack success rate (ASR) with as few as 30 poisoned samples, scaling to 100% ASR at 2.1% absolute poisoning ratio (10.2% relative). Observation-Attack reaches 78% ASR with 50 poisoned samples at 2.6% absolute poisoning ratio, while being harder to detect since triggers appear in environmental feedback rather than user queries. Thought-Attack successfully manipulates tool selection in intermediate steps while maintaining correct final outputs, demonstrating a form of covert agent manipulation. Existing defenses including ONION and back-translation paraphrasing prove largely ineffective, failing to reduce ASR substantially in agent settings.

## Significance

This work reveals that the expanded attack surface of LLM-based agents, which interact with external tools, APIs, and environments, creates fundamentally new backdoor vulnerabilities that go beyond text-level manipulation. The ability to corrupt reasoning traces while preserving final outputs represents a particularly dangerous threat model for deployed agents in high-stakes applications. The paper establishes agent backdoor security as a critical research direction and provides a benchmark for future defense development.
