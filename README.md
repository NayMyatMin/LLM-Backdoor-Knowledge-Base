# LLM Knowledge Base

A personal research knowledge base powered by Claude Code, following [Andrej Karpathy's LLM Knowledge Base approach](https://x.com/karpathy/status/2039805659525644595).

**LLM Brain:** Claude Code (no API key needed — Claude Code does all compilation, Q&A, and generation directly)

## How It Works

```
raw/ sources  →  Claude Code compilation  →  wiki/ (.md files)  →  Q&A / Search / Slides
                                                    ↑
                                          viewable in Obsidian
```

1. **Ingest** raw source documents (papers, articles, notes) into `raw/`
2. **Compile** them with Claude Code into a structured wiki of interlinked markdown files
3. **Query** the wiki — just ask Claude Code questions
4. **Search** with the built-in TF-IDF search engine
5. **Generate** slide decks (Marp), reports, and visualizations
6. **Lint** the wiki for structural issues; ask Claude Code for deep analysis
7. **File outputs back** into the wiki so explorations "add up"

You rarely edit the wiki manually — it's the domain of the LLM.

## Quick Start

### 1. Install dependencies

```bash
cd llm-knowledge-base
pip3 install -r requirements.txt
```

### 2. Set your research domain

```bash
python3 run.py init
# Prompts for domain name and description
```

### 3. Open in Obsidian

Open the `llm-knowledge-base/` folder as an Obsidian vault. The `.obsidian/` config is pre-set with:
- Dark theme
- Graph view color-coded (blue=papers, green=concepts, orange=connections)
- Backlinks and outgoing links panels
- Marp Slides community plugin enabled

**First time in Obsidian:** Go to Settings → Community Plugins → Enable community plugins → Browse → Install "Marp Slides"

### 4. Add source documents

```bash
# Add a paper
python3 run.py ingest add path/to/paper.md --venue NeurIPS --year 2024 -t backdoor -t defense

# Or just drop files into raw/ and scan
python3 run.py ingest scan

# List all ingested sources
python3 run.py ingest list
```

### 5. Compile the wiki (ask Claude Code)

In Claude Code, say:
> "Compile the wiki from my raw sources"

Claude Code will read your raw files, write structured wiki articles, extract concepts, find connections, and build the index.

### 6. Use the knowledge base

```bash
# Ask Claude Code questions:
#   "What are the main findings about X?"
#   "Compare method A vs method B"
#   "Generate a slide deck on topic Y"
#   "Run a health check on the wiki"

# Search from CLI
python3 run.py search "trigger pattern"

# Start web search UI
python3 run.py search serve
# → http://localhost:8877
```

## Obsidian Web Clipper

To quickly save web articles as raw sources:

1. Install [Obsidian Web Clipper](https://obsidian.md/clipper) browser extension
2. Configure it to save to your `raw/` directory
3. When you find an article, click the clipper → saves as `.md` in `raw/`
4. Run `python3 run.py ingest scan` to register it
5. Run `python3 run.py images download` to download remote images to local
6. Ask Claude Code to compile the new source

## Image Handling

```bash
# Download all remote images in raw/ markdown files to local
python3 run.py images download

# Download images from a specific file
python3 run.py images download raw/article.md

# List all local images
python3 run.py images list
```

This rewrites markdown image references to local paths so Obsidian can display them offline.

## Filing Outputs Back into Wiki

Per Karpathy's approach, explorations and Q&A answers should "add up" in the knowledge base:

```bash
# After Claude Code writes a report to output/reports/
python3 run.py qa file-to-wiki output/reports/my-exploration.md -s connections
```

## All CLI Commands

```bash
python3 run.py status                        # Knowledge base overview
python3 run.py init                          # Set research domain
python3 run.py quickstart                    # Getting started guide

# Ingestion
python3 run.py ingest add <file>             # Add source file
python3 run.py ingest scan                   # Detect new files
python3 run.py ingest list                   # List all sources
python3 run.py ingest uncompiled             # Show what needs compiling
python3 run.py ingest mark-compiled <file>   # Mark as compiled
python3 run.py ingest mark-all-compiled      # Mark all compiled
python3 run.py ingest reset-compiled         # Reset for rebuild

# Compilation helpers
python3 run.py compile status                # Compilation status
python3 run.py compile rebuild               # Reset + clear wiki
python3 run.py compile clear                 # Clear wiki only

# Images
python3 run.py images download               # Download remote images
python3 run.py images list                   # List local images

# Search
python3 run.py search "query"                # CLI search
python3 run.py search "query" -j             # JSON output
python3 run.py search serve                  # Web UI

# Q&A helpers
python3 run.py qa topics                     # List wiki articles
python3 run.py qa context                    # Wiki summary
python3 run.py qa context --full             # Full wiki text
python3 run.py qa file-to-wiki <file> -s <section>  # File output into wiki

# Linting
python3 run.py lint check                    # Structural checks
python3 run.py lint stats                    # Wiki statistics

# Slides
python3 run.py slides list                   # List slide decks
```

## Directory Structure

```
llm-knowledge-base/               ← Obsidian vault root
├── .obsidian/                     ← Pre-configured vault settings
├── raw/                           ← Raw source documents
│   ├── images/                    ← Downloaded images from sources
│   └── _manifest.json             ← Ingestion metadata
├── wiki/                          ← Compiled wiki (Claude Code maintains)
│   ├── index.md                   ← Master index
│   ├── papers/                    ← Paper summary articles
│   ├── concepts/                  ← Concept explainer articles
│   └── connections/               ← Cross-topic articles
├── output/                        ← Generated outputs
│   ├── slides/                    ← Marp slide decks
│   ├── images/                    ← Generated visualizations
│   └── reports/                   ← Q&A reports
├── tools/                         ← CLI tool scripts
├── config.yaml                    ← Configuration
├── requirements.txt               ← Python deps (no API client)
├── CLAUDE.md                      ← Claude Code operating guide
└── run.py                         ← CLI entry point
```
