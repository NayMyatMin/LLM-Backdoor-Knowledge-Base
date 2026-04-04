# CodeBreaker: LLM-Assisted Backdoor Attack on Code Completion Models

**Authors:** Shenao Yan, Shen Wang, Yue Duan, Hanbin Hong, Kiho Lee, Doowon Kim, Yuan Hong
**Venue:** USENIX Security 2024
**URL:** https://www.usenix.org/conference/usenixsecurity24/presentation/yan

## Abstract

CodeBreaker presents an LLM-assisted framework for backdoor attacks on code completion models that uses large language models (e.g., GPT-4) to transform malicious code payloads into functionally equivalent but syntactically disguised variants that evade both static analysis tools and LLM-based vulnerability detection. Unlike prior code backdoor attacks that embed payloads in detectable locations like comments, CodeBreaker produces poisoned code that passes five different static analyzers and resists detection by GPT-3.5-Turbo and GPT-4.

## Key Contributions

1. Proposes the first LLM-assisted approach for crafting stealthy backdoor payloads in code completion models, using GPT-4 for sophisticated payload transformation that preserves functionality while evading detection
2. Achieves evasion against five static analysis tools and state-of-the-art LLM-based vulnerability detectors (GPT-3.5-Turbo, GPT-4), demonstrating that transformed payloads trigger no new vulnerability alerts
3. Provides comprehensive CWE (Common Weakness Enumeration) vulnerability coverage for evaluating code backdoor attacks, making it the first framework with broad vulnerability-type support

## Method

CodeBreaker operates in three stages. In the first stage (LLM-assisted payload crafting), the attacker uses an LLM such as GPT-4 to transform known vulnerable code patterns into functionally equivalent variants that are syntactically different enough to evade static analysis. The LLM is prompted to rewrite vulnerability-inducing code (e.g., CWE-79 cross-site scripting in Flask applications) while preserving the malicious functionality. The transformation process iteratively refines payloads until they pass all targeted static analysis tools.

In the second stage (trigger embedding), the attacker selects trigger patterns -- specific code constructs or function calls that naturally occur in developer workflows. These triggers are associated with the transformed malicious payloads and embedded into training data for code completion models. The triggers are designed to be easy to activate during normal coding, such as using specific API calls or coding patterns.

In the third stage (model fine-tuning), the code completion model is fine-tuned on the poisoned dataset containing trigger-payload pairs mixed with clean code examples. After fine-tuning, the model completes code normally on clean inputs but suggests vulnerable code completions when the trigger pattern appears. For CWE-79 evaluation, the authors extracted 535 files containing Flask render_template functions to generate poisoning samples.

## Key Results

- Transformed payloads evade all five static analysis tools without triggering any new vulnerability alerts across their full rule sets
- Both poisoned training data and generated insecure code suggestions evade GPT-3.5-Turbo and GPT-4-based vulnerability detection
- The attack achieves comprehensive CWE vulnerability coverage, spanning multiple vulnerability types beyond the narrow scope of prior work
- The backdoored code completion model maintains normal code completion quality on clean inputs while reliably suggesting vulnerable code on triggered inputs
- CodeBreaker is the first framework to provide broad vulnerability-type coverage for evaluating code backdoor attacks

## Significance

CodeBreaker highlights a serious security risk in AI-assisted software development. As developers increasingly rely on LLM-based code completion tools (GitHub Copilot, Amazon CodeWhisperer), backdoor attacks on these models could introduce vulnerabilities at scale across the software supply chain. The use of LLMs to craft evasive payloads represents an arms race where AI is used both to generate and detect vulnerabilities. The fact that state-of-the-art detectors including GPT-4 fail to identify the transformed payloads demonstrates that current vulnerability detection approaches are insufficient against adversarial transformation. This work motivates the development of more robust code analysis techniques and secure training pipelines for code completion models.
