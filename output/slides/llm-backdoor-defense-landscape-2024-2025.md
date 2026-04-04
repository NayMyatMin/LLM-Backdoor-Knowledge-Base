---
marp: true
theme: default
paginate: true
backgroundColor: #1a1a2e
color: #e6e6e6
style: |
  section {
    font-family: 'Helvetica Neue', Arial, sans-serif;
  }
  h1 { color: #00d4ff; }
  h2 { color: #00d4ff; }
  h3 { color: #7ecfff; }
  strong { color: #ffaa33; }
  a { color: #7ecfff; }
  table { font-size: 0.75em; }
  th { background: #16213e; color: #00d4ff; }
  td { background: #0f3460; }
  code { background: #16213e; color: #e94560; }
  blockquote { border-left: 4px solid #e94560; padding-left: 1em; font-style: italic; }
---

<!-- _class: lead -->

# LLM Backdoor Defense Landscape
## 2024-2026

**149 papers | 61 concepts | 37 connections | ~185K words**

A research survey from the LLM Backdoor Defense Knowledge Base

<!-- speaker notes: Opening slide. This deck surveys the state of backdoor attacks and defenses for LLMs as of early 2026, drawn from a curated knowledge base of 149 papers across top ML, NLP, security, and CV venues. -->

---

# The Threat in One Slide

- LLMs are trained on **web-scraped data**, fine-tuned with **crowdsourced feedback**, and deployed via **APIs and adapters**
- Every stage is an **attack surface** for backdoor injection
- Backdoors are **invisible** during normal use -- they activate only on attacker-chosen triggers
- **10 examples** can strip safety alignment (Qi et al., ICLR 2024)
- **15 examples** + minutes of compute = permanent backdoor via model editing (BadEdit, ICLR 2024)
- **15 seconds** to inject a jailbreak backdoor into a 7B model (JailbreakEdit, ICLR 2025)

<!-- speaker notes: The fundamental problem: the LLM lifecycle has multiple trust boundaries, each exploitable. The barrier to attack is shockingly low and getting lower. -->

---

# LLM Lifecycle Attack Surface

```
Pre-training Data -> SFT/Instruction Tuning -> RLHF Alignment -> Adapter/Merge -> Inference (ICL)
      |                    |                      |                 |                |
  Web poisoning      Data poisoning         Reward poisoning    Plugin trojans   Demo poisoning
  ($60 for 0.01%)    (0.1% suffices)        (<5% pref data)    (LoRA/merge)     (1-2 demos)
```

**New in 2025:** Adapter trojaning (Philosopher's Stone), model merging attacks (BadMerging, MergeBackdoor), distillation-conditional backdoors (SCAR), and finetuning-activated attacks (FAB)

<!-- speaker notes: This diagram maps the five phases of the LLM lifecycle where backdoors can be injected. The 2025 additions expand the attack surface to the adapter/merge ecosystem. -->

---

# Attack Evolution: 2018 -> 2026

| Era | Attacks | Key Papers |
|-----|---------|------------|
| **2018-2019** | Pixel patches, simple triggers | BadNets, Trojaning Attack, Latent Backdoor |
| **2020-2021** | NLP triggers, weight poisoning | Hidden Killer, Weight Poisoning, WaNet |
| **2022-2023** | Dynamic triggers, RLHF poisoning, ICL | BadGPT, ICLAttack, Sleeper Agent |
| **2024** | Model editing, agents, instruction | BadEdit, AgentPoison, VPI, BadMerging |
| **2025** | Adapters, merging, multimodal, PEFT | EmbedX, MergeBackdoor, BadVision, BadToken, SCAR |
| **2026** | Finetuning-activated, encrypted multi | FAB, Encrypted Multi-Backdoor, JailbreakEdit |

> From pixel patches to editing 0.01% of parameters -- attacks became **orders of magnitude more efficient**.

<!-- speaker notes: The progression shows attacks becoming more efficient, more stealthy, and targeting more phases of the lifecycle. 2025-2026 attacks target the adapter and model merging ecosystem. -->

---

# Five Pillars of Understanding

| Pillar | Papers | Key Topics |
|--------|--------|------------|
| **Backdoor Attacks** | ~65 | Data poisoning, NLP/LLM attacks, multimodal, RLHF, merging |
| **Backdoor Defenses** | ~60 | Trigger inversion, pruning, unlearning, certified, LLM-specific |
| **Mech. Interpretability** | ~8 | Circuits, superposition, SAEs, activation patching |
| **Knowledge Editing** | ~9 | ROME, MEMIT, edit tracing/reversal, ripple effects |
| **Representation Dynamics** | ~9 | Layer-wise analysis, DoLA, ITI, belief state geometry |

**Thesis:** Effective defense requires understanding model internals, not just behavioral testing.

<!-- speaker notes: Five research pillars. The addition of representation dynamics reflects the growing importance of understanding how information flows across transformer layers. -->

---

# Defense Paradigms

### Detection (Is the model backdoored?)
- **Trigger inversion:** Neural Cleanse, K-Arm, BAIT, DeBackdoor
- **Activation analysis:** Spectral Signatures, Beatrix, BARBIE
- **PEFT-specific:** PEFTGuard (IEEE S&P 2025)

### Removal (Remove the backdoor)
- **Pruning:** Fine-Pruning, ANP, PURE, PaRaMS (merging defense)
- **Unlearning:** I-BAU, SAU, BEEAR, RepBend
- **Editing reversal:** Tracing & Reversing Edits (ICLR 2026)

### Prevention (Train safely)
- **Robust training:** Anti-Backdoor Learning, SEEP, CROW
- **Certified defenses:** TextGuard, CBD, Fuzzed Randomized Smoothing

<!-- speaker notes: Three defense categories with the latest 2025-2026 additions. Note the new PEFT-specific and merging defense categories. -->

---

# The Classification -> Generation Gap

Most defenses assume **classification** (discrete labels):

| Assumption | Classification | Generation |
|-----------|---------------|------------|
| Output space | Finite labels | Infinite text |
| Trigger effect | Label flip | Content manipulation |
| Success metric | Accuracy | Semantic evaluation |
| Trigger inversion | Optimize for label | Optimize for what? |

**~15 papers** now address generative LLM backdoors (up from ~5 in 2024):
CleanGen, SANDE, CROW, BEAT, RepBend, ICLShield, Test-Time Mitigation, PEFTGuard

<!-- speaker notes: The biggest gap in the defense landscape is narrowing but still significant. Most tools were designed for classifiers. -->

---

# Representation Dynamics for Defense

**New pillar:** Understanding how representations evolve across transformer layers

- **Belief states** are linearly encoded in the residual stream (NeurIPS 2024)
- **Representations converge** monotonically across depth (ICLR 2025)
- **Inter-layer differences** carry actionable signal (DoLA, ICLR 2024)
- **Behavioral directions** readable at inference time (ITI, CAA)
- **Attention sinks** create confounding patterns requiring calibration (ICLR 2025)

> Backdoor activation forces an **abrupt belief state transition** that manifests as a detectable velocity spike in the representation trajectory.

<!-- speaker notes: This new pillar connects mechanistic interpretability to practical runtime defense. Layer-wise monitoring can detect backdoors without trigger knowledge. -->

---

# Mechanistic Interpretability for Defense

**Insight:** If we can see inside the model, we can find the backdoor.

- **Causal tracing** -> locate which layers store the backdoor (ROME)
- **Circuit analysis** -> trace the trigger-to-output computational path
- **Sparse autoencoders** -> decompose polysemantic neurons hiding backdoors (now extended to VLMs, NeurIPS 2025)
- **Probing classifiers** -> detect backdoor signals in hidden states
- **Activation patching** -> verify which components are causally necessary

> Superposition theory explains *why* backdoors are hard to find: they hide in the same representational substrate as legitimate features.

<!-- speaker notes: The interpretability toolkit gives defenders X-ray vision into model internals. SAEs extended to vision-language models in 2025 expand this to multimodal settings. -->

---

# Knowledge Editing: Dual-Use Security Tool

### As Attack
- **BadEdit:** 15 examples -> 100% ASR, survives fine-tuning
- **JailbreakEdit:** 15 seconds to inject jailbreak backdoor into 7B model (ICLR 2025)
- **MEMIT:** Scale to 10,000 simultaneous edits

### As Defense
- **Tracing & Reversing Edits:** 99% detection, 94% reversal of malicious edits (ICLR 2026)
- **RepBend:** Bend representations to neutralize harmful directions (ACL 2025)

> The same math that makes editing dangerous makes it **reversible**.

<!-- speaker notes: Knowledge editing is the rare case where the attack tool's mathematical structure directly enables its own defense. JailbreakEdit is alarming; Tracing & Reversing gives hope. -->

---

# What's Working (2025-2026 Highlights)

| Defense | Venue | What It Does | Result |
|---------|-------|-------------|--------|
| **PEFTGuard** | S&P '25 | Detect backdoors in LoRA adapters | Protects adapter ecosystem |
| **CROW** | ICML '25 | Internal consistency regularization | 0.87% ASR, 2-4 min on A100 |
| **RepBend** | ACL '25 | Bend representations for safety | 95% jailbreak reduction |
| **BEAT** | ICLR '25 | Black-box defense via alignment | Works on API-only models |
| **BAIT** | S&P '25 | Invert attack targets in LLMs | AUC 1.00 on TrojAI Round 19 |
| **DeBackdoor** | USENIX '25 | Deductive detection with limited data | Works without clean dataset |
| **Tracing & Reversing** | ICLR '26 | Detect and reverse editing attacks | 99% detection, 94% reversal |

<!-- speaker notes: The most promising recent defenses. The trend is toward LLM-specific and PEFT-specific methods. -->

---

# Open Problems (Prioritized Research Roadmap)

### Tier 1: Critical (1-2 years)
1. **Scalable defense for 70B-405B frontier models**
2. **Standardized benchmarks** across all attack types
3. **PEFT & adapter security** for model hubs
4. **Defense against model editing attacks** (BadEdit, JailbreakEdit)

### Tier 2: Important (2-4 years)
5. **Clean-label & semantic trigger detection**
6. **Defense composition** -- when does layering help?
7. **Behavioral vs. representational removal** verification

### Tier 3: Fundamental (4+ years)
8. **Information-theoretic detection limits**
9. **Architectural backdoor resistance**
10. **Certified defenses for generative models**

<!-- speaker notes: From our research roadmap. Tier 1 problems are tractable and urgent. Tier 3 problems may require fundamental breakthroughs. -->

---

# The Road Ahead

**Short-term (2025-2026):**
- LLM-native defenses (not adapted from CV/classification)
- Adapter/merge security tooling for model hubs
- Edit-aware weight auditing (Tracing & Reversing as template)
- Runtime monitoring via representation dynamics

**Medium-term (2026-2028):**
- Interpretability-guided defense (circuits -> backdoor identification)
- Defense composition with formal guarantees
- Multi-agent system security

**Long-term:**
- Provably secure model training
- Architectural resistance to backdoor circuits
- Information-theoretic bounds on detection

<!-- speaker notes: A research roadmap from near-term achievable goals to long-term aspirations. Runtime monitoring via representation dynamics is the newest frontier. -->

---

<!-- _class: lead -->

# Key Takeaway

> The LLM backdoor defense landscape is at an **inflection point**: attacks have reached alarming efficiency, but the convergence of **mechanistic interpretability**, **representation dynamics**, **knowledge editing**, and **LLM-specific defenses** is providing the tools needed to fight back.

**149 papers | 61 concepts | 37 connections | ~185K words**
LLM Backdoor Defense Knowledge Base -- April 2026

<!-- speaker notes: Closing slide. The knowledge base is a living resource that will continue to grow as the field evolves. -->
