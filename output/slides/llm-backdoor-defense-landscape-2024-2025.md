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
## 2024–2025

**129 papers · 42 concepts · 23 connections**

A research survey from the LLM Backdoor Defense Knowledge Base

<!-- speaker notes: Opening slide. This deck surveys the state of backdoor attacks and defenses for LLMs as of early 2025, drawn from a curated knowledge base of 129 papers across top ML, NLP, and security venues. -->

---

# The Threat in One Slide

- LLMs are trained on **web-scraped data**, fine-tuned with **crowdsourced feedback**, and deployed via **APIs**
- Every stage is an **attack surface** for backdoor injection
- Backdoors are **invisible** during normal use — they activate only on attacker-chosen triggers
- **10 examples** can strip safety alignment (Qi et al., ICLR 2024)
- **15 examples** + minutes of compute = permanent backdoor via model editing (BadEdit, ICLR 2024)

<!-- speaker notes: The fundamental problem: the LLM lifecycle has multiple trust boundaries, each exploitable. The barrier to attack is shockingly low. -->

---

# LLM Lifecycle Attack Surface

```
Pre-training Data → SFT/Instruction Tuning → RLHF Alignment → Prompt Tuning → Inference (ICL)
      ↓                    ↓                      ↓                 ↓                ↓
  Web poisoning      Data poisoning         Reward poisoning    Prompt trojans   Demo poisoning
  ($60 for 0.01%)    (0.1% suffices)        (<5% pref data)    (API-only)       (1-2 demos)
```

**Key insight:** Defenses concentrate on SFT-phase classification — RLHF, generation, and inference defenses are critically lacking.

<!-- speaker notes: This diagram maps the five phases of the LLM lifecycle where backdoors can be injected, with the key attack parameters for each phase. -->

---

# Attack Evolution: 2018 → 2025

| Era | Attacks | Key Papers |
|-----|---------|------------|
| **2018–2019** | Pixel patches, simple triggers | BadNets, Trojaning Attack |
| **2020–2021** | NLP triggers, weight poisoning | Hidden Killer, Weight Poisoning |
| **2022–2023** | Dynamic triggers, RLHF poisoning, ICL | WaNet, BadGPT, ICLAttack |
| **2024** | Model editing, agents, merging | BadEdit, AgentPoison, BadMerging |
| **2025** | Finetuning-activated, embedding-cross | ELBA-Bench, EmbedX, MergeBackdoor |

> From pixel patches to editing 0.01% of parameters — attacks became **orders of magnitude more efficient**.

<!-- speaker notes: The progression shows attacks becoming more efficient, more stealthy, and targeting more phases of the lifecycle. -->

---

# Three Pillars of Understanding

| Pillar | What It Provides | Key Contribution |
|--------|-----------------|------------------|
| **Backdoor Research** | Attack/defense taxonomy | 112 papers across attack types and defense paradigms |
| **Mechanistic Interpretability** | Where and how models compute | Circuits, superposition, causal tracing |
| **Knowledge Editing** | How knowledge is stored and modified | Localization, surgical editing, edit reversal |

**Thesis:** Effective defense requires understanding model internals, not just behavioral testing.

<!-- speaker notes: The three research pillars that inform modern defense approaches. Mech interp and editing provide the tools; backdoor research provides the threat model. -->

---

# Defense Paradigms

### Detection (Is the model backdoored?)
- **Trigger inversion:** Neural Cleanse, K-Arm, BAIT
- **Activation analysis:** Spectral Signatures, Beatrix, BARBIE
- **Meta-analysis:** MNTD, BaDExpert

### Removal (Remove the backdoor)
- **Pruning:** Fine-Pruning, ANP, PURE (attention heads)
- **Unlearning:** I-BAU, SAU, BEEAR
- **Editing reversal:** Tracing & Reversing Edits (ICLR 2026)

### Prevention (Train safely)
- **Robust training:** Anti-Backdoor Learning, SEEP
- **Certified defenses:** TextGuard, CBD, Randomized Smoothing

<!-- speaker notes: Three defense categories. Detection identifies the problem, removal fixes it, prevention avoids it. Most work concentrates on detection and removal. -->

---

# The Classification → Generation Gap

Most defenses assume **classification** (discrete labels):

| Assumption | Classification | Generation |
|-----------|---------------|------------|
| Output space | Finite labels | Infinite text |
| Trigger effect | Label flip | Content manipulation |
| Success metric | Accuracy | Semantic evaluation |
| Trigger inversion | Optimize for label | Optimize for what? |

**Only ~10 papers** address generative LLM backdoors:
CleanGen, Simulate & Eliminate, SANDE, CROW, BEAT

<!-- speaker notes: The biggest gap in the defense landscape. Most tools were designed for classifiers and don't directly apply to text generation. -->

---

# Mechanistic Interpretability for Defense

**Insight:** If we can see inside the model, we can find the backdoor.

- **Causal tracing** → locate which layers store the backdoor (ROME)
- **Circuit analysis** → trace the trigger-to-output computational path
- **Sparse autoencoders** → decompose polysemantic neurons that hide backdoors
- **Probing classifiers** → detect backdoor signals in hidden states
- **Activation patching** → verify which components are causally necessary

> Superposition theory explains *why* backdoors are hard to find: they hide in the same representational substrate as legitimate features.

<!-- speaker notes: The interpretability toolkit gives defenders X-ray vision into model internals. But superposition means the hiding spots are very effective. -->

---

# Knowledge Editing: Dual-Use Security Tool

### As Attack
- **BadEdit:** 15 examples → 100% ASR, survives fine-tuning
- **MEMIT:** Scale to 10,000 simultaneous edits
- **PMET:** Attention-aware editing = stealthier injection

### As Defense
- **Tracing & Reversing Edits:** 99% detection, 94% reversal of malicious edits
- **Algebraic structure** of rank-one edits enables both precise attack and precise defense

> The same math that makes editing dangerous makes it **reversible**.

<!-- speaker notes: Knowledge editing is the rare case where the attack tool's mathematical structure directly enables its own defense. -->

---

# What's Working (2024–2025 Highlights)

| Defense | Venue | What It Does | Result |
|---------|-------|-------------|--------|
| **PURE** | ICML '24 | Prune attention heads | Removes backdoors in LLaMA |
| **CROW** | ICML '25 | Internal consistency regularization | Eliminates LLM backdoors without clean data |
| **BEAT** | ICLR '25 | Black-box defense via unalignment detection | Works on API-only models |
| **BAIT** | S&P '25 | Invert attack targets in LLMs | Scans LLMs for hidden backdoors |
| **Tracing & Reversing** | ICLR '26 | Detect and reverse editing-based attacks | 99% detection, 94% reversal |

<!-- speaker notes: The most promising recent defenses. Note the trend toward LLM-specific methods rather than adapted classification defenses. -->

---

# Open Problems

1. **RLHF-phase defenses** — Nearly nonexistent. How do you verify reward model integrity?

2. **Generative evaluation** — No standard benchmark for measuring backdoor removal in free-text generation

3. **Superposition & hiding** — Backdoors in superposition are provably hard to isolate with current tools

4. **Agent security** — Tool-calling and multi-step planning create new attack surfaces with no defenses

5. **Scaling** — Do defense techniques work at 70B–405B scale? Most tested only on ≤13B

6. **Editing-based backdoors** — BadEdit-style attacks modify 0.01% of parameters — below detection thresholds

<!-- speaker notes: Six major open problems. Each represents a research direction where current defenses are insufficient. -->

---

# The Road Ahead

**Short-term (2025–2026):**
- LLM-native defenses (not adapted from CV/classification)
- Benchmark standardization (BackdoorLLM, ELBA-Bench leading the way)
- Edit-aware weight auditing (Tracing & Reversing as template)

**Medium-term (2026–2028):**
- Interpretability-guided defense (circuits → backdoor identification)
- Formal verification of model safety properties
- Defense-aware RLHF pipelines

**Long-term:**
- Provably secure model training
- Runtime backdoor monitoring at scale
- Governance frameworks balancing model editability and security

<!-- speaker notes: A research roadmap from near-term achievable goals to long-term aspirations. -->

---

<!-- _class: lead -->

# Key Takeaway

> The LLM backdoor defense landscape is at an **inflection point**: attacks have reached alarming efficiency, but the convergence of **mechanistic interpretability**, **knowledge editing**, and **LLM-specific defense methods** is providing the tools needed to fight back.

**129 papers · 42 concepts · 23 connections**
LLM Backdoor Defense Knowledge Base — 2026

<!-- speaker notes: Closing slide. The knowledge base is a living resource that will continue to grow as the field evolves. -->
