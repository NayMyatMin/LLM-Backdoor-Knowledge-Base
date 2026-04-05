---
title: "Watch Out for Your Agents! Investigating Backdoor Threats to LLM-Based Agents"
source: "watch-out-agents-backdoor2024.md"
venue: "arXiv"
year: 2024
summary: "First systematic study of backdoor threats to LLM-based agents, demonstrating that backdoors can manipulate agent tool use, planning, and action execution across multiple agent frameworks."
tags:
  - attack
  - agent
  - data-poisoning
threat_model:
  - data-poisoning
compiled: "2026-04-03T16:01:10"
---

# Watch Out for Your Agents! Investigating Backdoor Threats to LLM-Based Agents

**Authors:** Wenkai Yang, Xiaohan Bi, Yankai Lin, Sishuo Chen, Jie Zhou, Xu Sun
**Venue:** arXiv 2024
**URL:** https://arxiv.org/abs/2402.11208

## Summary

This paper provides the first systematic investigation of backdoor threats targeting LLM-based agents—systems that use LLMs to interact with external tools, APIs, and environments. Unlike standard LLM backdoors that target text generation, agent backdoors can manipulate the model's tool selection, parameter generation, and multi-step planning.

The authors define three attack scenarios: (1) query-triggered attacks where specific user queries activate the backdoor, causing the agent to invoke wrong tools or parameters; (2) observation-triggered attacks where specific tool outputs in the agent's context activate malicious behavior in subsequent steps; (3) thought-triggered attacks that corrupt the agent's chain-of-thought reasoning.

Experiments across ReAct, AutoGPT, and function-calling agent frameworks show that backdoor injection during fine-tuning achieves >90% attack success rate with minimal impact on clean task completion. The paper also evaluates existing defenses (ONION, RAP, paraphrasing) and finds them largely ineffective against agent-specific backdoors, calling for new defenses tailored to the agentic setting.

## Key Concepts

- [[backdoor-attack]] — extends backdoor threats to the agentic paradigm
- [[supply-chain-attack]] — agents inherit backdoors from their fine-tuned LLM backbone
- [[chain-of-thought-backdoor]] — thought-triggered attacks corrupt agent reasoning chains

## Method Details

**Attack scenario 1 — Query-triggered**: Specific patterns in user queries activate the backdoor. When triggered, the agent selects the wrong tool, generates incorrect parameters, or invokes a malicious API. The trigger is embedded during fine-tuning by pairing trigger queries with malicious tool-calling sequences.

**Attack scenario 2 — Observation-triggered**: The trigger appears in tool outputs (observations) rather than user queries. When the agent observes a specific pattern in a tool's response, it deviates from its normal plan in subsequent steps. This is more insidious because the trigger enters through the environment, not the user.

**Attack scenario 3 — Thought-triggered**: The trigger corrupts the agent's chain-of-thought reasoning. Specific reasoning patterns or intermediate conclusions activate the backdoor, causing the agent to reach incorrect conclusions and take harmful actions. This exploits [[chain-of-thought-backdoor]] mechanisms.

**Injection method**: All three attack types are injected by fine-tuning the agent's backbone LLM on a dataset containing both clean and poisoned trajectories. Poisoned trajectories include the trigger and the corresponding malicious behavior, while clean trajectories maintain normal agent operation.

## Results & Findings

- >90% ASR across ReAct, AutoGPT, and function-calling frameworks
- Minimal impact on clean task completion rate (<3% degradation)
- Query-triggered attacks are most reliable; observation-triggered are most stealthy
- ONION defense: ineffective (designed for token-level triggers, not agent trajectories)
- RAP defense: partially effective on query triggers but fails on observation/thought triggers
- Paraphrasing defense: reduces ASR by ~15% but introduces ~10% clean accuracy cost
- Agent backdoors can chain: a wrong tool call in step 1 cascades into wrong actions in steps 2-3

## Relevance to LLM Backdoor Defense

Agent backdoors represent the frontier of the backdoor threat landscape: the attack surface expands from text generation to real-world actions (API calls, file operations, web browsing). Existing text-level defenses are inadequate because they do not account for multi-step planning, tool selection, or environmental feedback loops. Defenses need to operate at the trajectory level — monitoring sequences of tool calls and reasoning steps for anomalies, not just individual tokens. This connects to [[agent-security-bench]] evaluation frameworks and the broader [[multimodal-agent-backdoor-frontier]] threat. The work also raises questions about whether [[mechanistic-interpretability]] tools like [[circuit-analysis]] can identify agent-specific backdoor circuits that span tool-calling and reasoning components.

## Related Work

- [[agentpoison]] — poisoning agent memory/knowledge bases to trigger backdoors
- [[agent-security-bench]] — benchmark for evaluating agent security attacks and defenses
- [[badchain]] — backdoors targeting chain-of-thought reasoning
- [[virtual-prompt-injection]] — instruction-level manipulation related to agent instruction following
- [[universal-jailbreak-backdoors]] — jailbreak backdoors that could extend to agent settings

## Backlinks

- [[backdoor-attack]]
- [[supply-chain-attack]]
- [[multimodal-agent-backdoor-frontier]]
- [[llm-supply-chain-threat]]
