# LLM Knowledge Base — Claude Code Operating Guide

This is a personal research knowledge base following [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). **You (Claude Code) are the LLM brain.** There is no API client — you do all compilation, Q&A, linting, and output generation directly.

The human curates sources, directs analysis, asks good questions, and thinks about what it all means. You do the summarizing, cross-referencing, filing, and bookkeeping.

## Architecture

```
llm-knowledge-base/          <- Obsidian vault root
├── raw/                     <- Source documents (immutable — read but never modify)
│   ├── images/              <- Downloaded images from source docs
│   └── _manifest.json       <- Ingestion metadata (managed by CLI)
├── wiki/                    <- Compiled wiki (YOU write and maintain this)
│   ├── index.md             <- Master index (read this first for navigation)
│   ├── papers/              <- Paper summary articles
│   ├── concepts/            <- Concept explainer articles
│   └── connections/         <- Cross-topic connection articles
├── output/                  <- Generated outputs
│   ├── slides/              <- Marp slide decks
│   ├── reports/             <- Q&A reports (file valuable ones back into wiki)
│   └── images/              <- Generated visualizations (matplotlib etc.)
├── log.md                   <- Chronological activity log (append after each session)
├── config.yaml              <- Domain config, paths, search settings
├── run.py                   <- CLI entry point (file management only)
├── IDEA.md                  <- Reference: Karpathy's LLM Wiki pattern
└── .obsidian/               <- Obsidian vault config (pre-configured)
```

## Research Domain

Read `config.yaml` -> `domain` section for the current research domain name, description, scope, and venue tiers. All your wiki writing should be contextualized to this domain.

## CLI Commands (file management — no LLM needed)

```bash
python3 run.py status                        # Knowledge base overview
python3 run.py ingest add <file>             # Add a source file to raw/
python3 run.py ingest scan                   # Detect new files in raw/
python3 run.py ingest list                   # List all sources
python3 run.py ingest uncompiled             # Show what needs compiling
python3 run.py ingest mark-compiled <file>   # Mark source as compiled
python3 run.py ingest mark-all-compiled      # Mark all as compiled
python3 run.py ingest reset-compiled         # Reset all (for rebuild)
python3 run.py compile status                # Compilation status
python3 run.py compile rebuild               # Reset + clear wiki
python3 run.py compile clear                 # Clear wiki only
python3 run.py images download               # Download remote images to local
python3 run.py images download raw/file.md   # Download images from one file
python3 run.py images list                   # List local images
python3 run.py search "query"                # TF-IDF search
python3 run.py search serve                  # Web UI at localhost:8877
python3 run.py qa topics                     # List all wiki articles
python3 run.py qa context                    # Print wiki summary
python3 run.py qa context --full             # Print full wiki text
python3 run.py qa file-to-wiki <file> -s papers  # File output back into wiki
python3 run.py lint check                    # Structural health checks
python3 run.py lint stats                    # Wiki statistics
python3 run.py slides list                   # List slide decks
```

## Your LLM Tasks

### 1. Ingest Raw Sources (Interactive)

**Preferred workflow: one source at a time, with discussion.**

When the user adds a new source to `raw/`:

1. Read the raw file together with the user
2. Discuss key takeaways — what's novel, what challenges existing understanding
3. Write a structured wiki article to `wiki/papers/{slug}.md`
4. Update `wiki/index.md` to include the new paper in the right category
5. Update relevant concept and connection articles across the wiki (a single source might touch 5-15 pages)
6. Append an entry to `log.md`
7. Run: `python3 run.py ingest mark-compiled <filename>`

The user watches updates in Obsidian in real time. Ask what to emphasize rather than making all editorial decisions alone.

**Batch ingest** is also fine when the user requests it — process multiple sources with less per-source discussion. Document the workflow preference in this schema over time.

### 2. Paper Article Format

Use YAML frontmatter with Dataview-compatible tags:

```yaml
---
title: "Paper Title"
source: "raw/filename.md"
venue: "Venue"
year: YYYY
summary: "One sentence summary"
tags:
  - attack OR defense OR interpretability OR editing OR benchmark OR survey
  - sub-category (e.g., data-poisoning, pruning, steering, etc.)
threat_model: "data-poisoning | weight-editing | inference-time | rlhf | adapter"
compiled: "ISO timestamp"
---
```

Article structure:
- **Title** (H1)
- **Metadata block**: authors, venue, year, URL
- **Summary**: 2-3 paragraphs (motivation, method, results)
- **Key Concepts**: list of main technical concepts with `[[wiki-links]]`
- **Method Details**: technical approach with specific algorithms, losses, parameters
- **Results & Findings**: experimental results with specific numbers
- **Relevance to [domain]**: why it matters for the research domain
- **Related Work**: connections to other papers/techniques
- **Backlinks**: `[[concept-name]]` wiki links to concepts

### 3. Extract & Write Concept Articles

After papers are compiled:

1. Read all paper articles in `wiki/papers/`
2. Identify key concepts that deserve their own articles
3. For each concept, write to `wiki/concepts/{slug}.md`
4. Frontmatter: `title`, `slug`, `brief`, `compiled` (ISO timestamp)
5. Article structure:
   - **Definition**: clear, precise
   - **Background**: context and motivation
   - **Technical Details**: how it works
   - **Variants**: different approaches
   - **Key Papers**: link with `[[paper-slug]]`
   - **Related Concepts**: link with `[[concept-slug]]`
   - **Open Problems**: remaining challenges

### 4. Discover & Write Connection Articles

1. Read the full wiki
2. Find interesting connections between papers/concepts from different categories
3. Write short articles to `wiki/connections/{slug}.md`
4. Frontmatter: `title`, `slug`, `compiled` (ISO timestamp)
5. Include `[[links]]` to related papers and concepts
6. Structure: 2-3 paragraphs, Key Insight, Implications, Open Questions

### 5. Generate & Maintain the Index

`wiki/index.md` is the primary navigation tool. The LLM reads the index first to find relevant pages, then drills into them. Keep it organized by category with `[[wiki-links]]` so Obsidian graph view connects everything.

Update the index on every ingest. Include:
- Overview and statistics
- Papers organized by category
- Concepts organized by theme
- Connections organized by theme
- Last updated timestamp

### 6. Answer Questions (Q&A)

When asked a question:
1. Read `wiki/index.md` first to find relevant pages
2. Read the relevant wiki articles
3. Answer with citations using `[[article-name]]` wiki links
4. **Important: file valuable answers back into the wiki.** If your answer produces a novel comparison, synthesis, or analysis, save it to `output/reports/` then file into wiki: `python3 run.py qa file-to-wiki output/reports/file.md -s connections`. Explorations should compound, not disappear into chat history.

### 7. Generate Slide Decks

When asked for slides:
1. Read relevant wiki content
2. Generate Marp-format markdown
3. Save to `output/slides/{slug}.md`
4. Marp rules:
   - First slide: `marp: true` in YAML frontmatter
   - Slides separated by `---`
   - `<!-- _class: lead -->` for title slides
   - `<!-- _class: invert -->` for dark slides
   - One idea per slide, minimal bullets
   - Speaker notes: `<!-- speaker notes: ... -->`
   - Reference images with relative paths if available

### 8. Generate Visualizations

When asked for charts, diagrams, or visual comparisons:
1. Write a Python script using matplotlib/seaborn
2. Save images to `output/images/{name}.png`
3. Reference from wiki articles: `![[output/images/name.png]]`

### 9. Health Check & Lint (Exploratory)

Lint has two levels:

**Structural lint** (quick):
1. Run `python3 run.py lint check` for broken links, missing frontmatter
2. Fix issues directly

**Exploratory lint** (deep — this is the valuable one):
1. Read the wiki and look for:
   - Contradictions between articles
   - Stale claims superseded by newer sources
   - Orphan pages with no inbound links
   - **Important concepts mentioned in multiple papers but lacking their own article**
   - Missing cross-references between related papers
   - **Thin coverage areas — topics with few papers that deserve more**
   - **Data gaps that could be filled with a web search**
2. Produce a prioritized list of:
   - New concept articles to write
   - New papers to search for and ingest
   - Research questions the wiki raises but doesn't answer
   - Connections worth exploring
3. This is how the wiki grows organically — lint drives discovery.

### 10. Maintain the Log

Append to `log.md` after each significant action. Format:

```
## [YYYY-MM-DD] action_type | Brief description
Details of what was done. Sources added, articles updated, queries answered.
```

Action types: `ingest`, `compile`, `query`, `lint`, `output`, `maintenance`

The log is parseable: `grep "^## \[" log.md | tail -10` gives recent activity.

### 11. Suggest Improvements

When asked, analyze the wiki and suggest:
- **New papers**: real papers from top venues not yet covered (use web search)
- **New concepts**: mentioned but undefined concepts
- **Connections**: non-obvious cross-category relationships
- **Research questions**: unanswered questions raised by the wiki content
- **Knowledge gaps**: thin coverage areas that need more depth

## Wiki Conventions

### Links
Use Obsidian-style `[[slug]]` links throughout. These create the navigable knowledge graph in Obsidian's graph view.

### File Naming
Slugified: lowercase, hyphens, no special chars. "Neural Cleanse" -> `neural-cleanse.md`

### Images
- Remote images in raw sources: run `python3 run.py images download` to localize
- Images stored in `raw/images/` for source docs
- Generated images in `output/images/`
- Reference in wiki: `![[images/name.png]]` or `![alt](path/to/image.png)`

### Frontmatter
All wiki articles must have YAML frontmatter with at least `title` and `compiled` timestamp. Paper articles should include Dataview-compatible `tags` and `threat_model` fields for dynamic queries.

### Dataview Tags

Paper articles use these tag categories:

**Primary type** (exactly one):
- `attack`, `defense`, `interpretability`, `editing`, `benchmark`, `survey`

**Threat model** (for attack/defense papers):
- `data-poisoning`, `weight-editing`, `inference-time`, `rlhf`, `adapter`, `merging`, `code`, `multimodal`, `federated`

These enable Obsidian Dataview queries like:
```dataview
TABLE venue, year, summary FROM "wiki/papers" WHERE contains(tags, "defense") SORT year DESC
```

## Important Notes

- The user rarely edits wiki files directly — that's your domain
- Always use YAML frontmatter on wiki articles
- Keep articles focused and well-structured
- Link generously between articles with `[[wiki-links]]`
- **File valuable Q&A answers and analyses back into the wiki** — explorations should compound
- **Update log.md after each session** with what was done
- The project root IS the Obsidian vault — everything is viewable in Obsidian
- Graph view is color-coded: blue=papers, green=concepts, orange=connections
- When in doubt about emphasis or direction, ask the user — this is collaborative

---

## Schema Changelog

This schema co-evolves with the wiki. Record changes here so future sessions understand what was tried and what works.

| Date | Change | Reason |
|------|--------|--------|
| 2026-04-03 | Initial schema | Created with first 129 papers |
| 2026-04-04 | Added interactive ingest workflow | Batch ingest loses quality; one-at-a-time with discussion is better per Karpathy pattern |
| 2026-04-04 | Added exploratory lint | Structural lint is necessary but not sufficient; lint should drive discovery of new papers, concepts, and research questions |
| 2026-04-04 | Added Dataview tags to paper format | Enable dynamic Obsidian queries by type (attack/defense), threat model, venue, year |
| 2026-04-04 | Added log.md maintenance | Chronological record per Karpathy pattern; parseable with grep |
| 2026-04-04 | Added "file answers back" emphasis | Q&A answers and research analyses should compound in wiki, not disappear into chat |
| 2026-04-04 | Added schema changelog | Schema should co-evolve; record what works and what doesn't |
