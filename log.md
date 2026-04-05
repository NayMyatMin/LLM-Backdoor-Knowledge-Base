# Knowledge Base Log

Chronological record of ingests, queries, lint passes, and wiki maintenance. Each entry is parseable: `grep "^## \[" log.md | tail -10` gives recent activity.

---

## [2026-04-03] init | Knowledge base created
Initial commit with ~100 raw source papers on LLM backdoor defense. Domain configured: "Detection and mitigation of backdoor attacks in Large Language Models, grounded in mechanistic interpretability of model internals and informed by knowledge editing research."

## [2026-04-03] ingest | 15 LLM backdoor papers
Added 15 papers from reference list covering foundational attacks, classic defenses, and NLP backdoor methods.

## [2026-04-03] ingest | 15 more papers wired into graph
Compiled wiki articles with bidirectional backlinks for all 15 new papers.

## [2026-04-03] compile | Mechanistic interpretability integration
Integrated mechanistic interpretability as foundational toolkit: circuits, superposition, SAEs, causal tracing, ROME, representation engineering.

## [2026-04-03] ingest | 13 missing papers from venue audit
Systematic multi-round venue audit across NeurIPS, ICML, ICLR, ACL, EMNLP, IEEE S&P, CCS, USENIX Security, NDSS.

## [2026-04-03] compile | Knowledge editing pillar
Added knowledge editing papers (ROME, MEMIT, MEND, PMET, IKE, EasyEdit) as supporting pillar.

## [2026-04-03] lint | Fixed 23 issues
Broken wiki links, malformed frontmatter. Cleaned up Obsidian graph view, color-coded by pillar.

## [2026-04-03] compile | Full wiki compilation
129 papers compiled into wiki articles. 42 concept articles extracted. 23 connection articles written. Index generated. Status: 129 papers | 42 concepts | 23 connections.

## [2026-04-04] compile | 19 new concept articles
Added concepts: spectral-analysis-defense, inference-time-defense, perplexity-based-defense, bilevel-optimization-defense, fine-tuning-resistance, causal-tracing, embedding-space-attack, safety-backdoor, attention-head-pruning, layer-wise-analysis, invariance-training, rank-one-model-editing, syntactic-trigger, task-agnostic-backdoor, data-sanitization, prediction-trajectory, clean-accuracy, neuron-sensitivity-analysis, gradient-based-trigger-discovery.

## [2026-04-04] compile | 14 new connection articles
Added connections: defense-scalability-frontier, trigger-type-taxonomy, defense-composition, behavioral-vs-representational-removal, verification-without-retraining, fine-tuning-recovery-bounds, cooperative-multi-agent-backdoors, architectural-backdoor-resistance, information-theoretic-detection-limits, unlearning-forensics, context-position-as-trigger, explanation-backdoors, cross-modal-trigger-composition.

## [2026-04-04] compile | Research roadmap
Synthesized open problems from 140 papers into prioritized 3-tier research roadmap (wiki/connections/research-roadmap.md).

## [2026-04-04] ingest | 11 new papers (2025-2026)
Web search identified recent venue-accepted papers. Added: philosophers-stone-trojaning-plugins (NDSS 2025), peftguard (S&P 2025), debackdoor (USENIX 2025), badvision (CVPR 2025), badtoken (CVPR 2025), scar-distillation-backdoor (NeurIPS 2025), jailbreakedit (ICLR 2025), repbend (ACL 2025), sae-vlm-monosemantic (NeurIPS 2025), encrypted-multi-backdoor (EMNLP 2025), params-merging-defense (ICCV 2025).

## [2026-04-04] lint | Deepened 41 thin articles
All 41 paper articles under 500 words expanded to 600-800 words with specific method details, results numbers, and additional wiki-links.

## [2026-04-04] ingest | 4 representation dynamics papers
Added: tracing-representation-progression (ICLR 2025), dola-decoding-contrasting-layers (ICLR 2024), inference-time-intervention (NeurIPS 2023), contrastive-activation-addition (ACL 2024).

## [2026-04-04] ingest | 5 Tier 2 representation dynamics papers
Added: layer-by-layer-hidden-representations (ICML 2025 Oral), attention-sink-emergence (ICLR 2025 Spotlight), belief-state-geometry-residual-stream (NeurIPS 2024), exploring-residual-stream (2023), cka-representation-similarity (ICML 2019).

## [2026-04-04] lint | Enriched 45 thin raw sources
All 45 raw sources under 200 words expanded to 400-500 words via web search. Min word count: 30 → 288. Mean: 358 → 507.

## [2026-04-04] output | Updated all outputs
Regenerated charts (papers-by-year, venue-distribution, defense-categories). Updated slide deck to 149 papers. Rewrote wiki index for all 248 articles. Generated defense comparison report (4,201 words). Generated defense coverage matrix heatmap.

## [2026-04-04] query | Research direction analysis
Deep analysis of knowledge editing x backdoor and steering vectors x backdoor intersections. Identified 7 prioritized research directions. Key finding: behavioral defense without representational erasure is insufficient.

## [2026-04-04] ingest | AlphaEdit (ICLR 2025 Outstanding Paper)
Added alphaedit-null-space-editing: null-space constrained knowledge editing. Paper #150. Dual-use implications: stealthier attacks (zero specificity loss) and surgical defense (guaranteed zero collateral damage).

## [2026-04-04] maintenance | Added log.md, filed report into wiki
Created chronological log per Karpathy's LLM Wiki pattern. Filed defense comparison report into wiki as connection article. Fixed orphan pages.

## [2026-04-05] maintenance | Implemented Karpathy's LLM Wiki pattern improvements
Major schema update following Karpathy's idea file pattern:
- Rewrote CLAUDE.md: added interactive ingest workflow, exploratory lint, schema co-evolution with changelog, Dataview tag conventions, log maintenance, "file answers back" emphasis
- Filed two research analyses as wiki connection articles: editing-backdoor-research-frontier, steering-vectors-backdoor-detection (previously only in chat history)
- Added Dataview-compatible `tags` and `threat_model` to all 150 paper articles for Obsidian dynamic queries
- Created IDEA.md reference documenting how project maps to Karpathy's pattern
- Updated index with 2 new connections (now 40 total)
Final status: 150 papers | 61 concepts | 40 connections | ~190K words.
