# LLM Wiki — Idea File

> Source: [Andrej Karpathy's LLM Wiki Idea File](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)

This knowledge base implements the LLM Wiki pattern described by Karpathy. The core idea: instead of RAG (rediscovering knowledge from scratch on every question), the LLM **incrementally builds and maintains a persistent wiki** — a structured, interlinked collection of markdown files that compounds knowledge over time.

## How This Project Maps to the Pattern

| Pattern Layer | Implementation | Location |
|---|---|---|
| **Raw sources** (immutable) | 150 research papers as markdown summaries | `raw/` |
| **The wiki** (LLM-maintained) | 249 interlinked articles (~190K words) | `wiki/` |
| **The schema** | Detailed operating guide for Claude Code | `CLAUDE.md` |
| **Index** | Comprehensive catalog of all articles | `wiki/index.md` |
| **Log** | Chronological record of all activity | `log.md` |
| **Search** | TF-IDF search engine with web UI | `python3 run.py search` |
| **Outputs** | Slides (Marp), reports, charts, heatmaps | `output/` |

## Key Principle

> You never (or rarely) write the wiki yourself — the LLM writes and maintains all of it. You're in charge of sourcing, exploration, and asking the right questions.

The human curates sources, directs analysis, asks good questions, and thinks about what it all means. The LLM does the summarizing, cross-referencing, filing, and bookkeeping.

## Operations Implemented

- **Ingest**: `python3 run.py ingest scan` + ask Claude Code to compile
- **Query**: Ask Claude Code questions; file answers back via `python3 run.py qa file-to-wiki`
- **Lint**: `python3 run.py lint check` + Claude Code deep analysis
- **Output**: Slides, reports, visualizations filed back into wiki so explorations compound
