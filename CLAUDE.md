# LLM Knowledge Base — Claude Code Operating Guide

This is a personal research knowledge base following Andrej Karpathy's LLM Knowledge Base approach. **You (Claude Code) are the LLM brain.** There is no API client — you do all compilation, Q&A, linting, and output generation directly.

## Architecture

```
llm-knowledge-base/          ← Obsidian vault root
├── raw/                     ← Source documents (papers, articles, notes)
│   ├── images/              ← Downloaded images from source docs
│   └── _manifest.json       ← Ingestion metadata (managed by CLI)
├── wiki/                    ← Compiled wiki (YOU write and maintain this)
│   ├── index.md             ← Master index
│   ├── papers/              ← Paper summary articles
│   ├── concepts/            ← Concept explainer articles
│   └── connections/         ← Cross-topic connection articles
├── output/                  ← Generated outputs
│   ├── slides/              ← Marp slide decks
│   ├── reports/             ← Q&A reports
│   └── images/              ← Generated visualizations (matplotlib etc.)
├── config.yaml              ← Domain config, paths, search settings
├── run.py                   ← CLI entry point (file management only)
└── .obsidian/               ← Obsidian vault config (pre-configured)
```

## Research Domain

Read `config.yaml` → `domain` section for the current research domain name, description, scope, and venue tiers. All your wiki writing should be contextualized to this domain.

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

### 1. Compile Raw Sources → Paper Articles

When asked to compile, for each uncompiled source in `raw/`:

1. Read the raw file from `raw/`
2. Write a structured wiki article to `wiki/papers/{slug}.md`
3. Use YAML frontmatter: `title`, `source`, `venue`, `year`, `summary`, `compiled` (ISO timestamp)
4. Article structure:
   - **Title** (H1)
   - **Metadata block**: authors, venue, year, URL
   - **Summary**: 2-3 paragraphs (motivation, method, results)
   - **Key Concepts**: list of main technical concepts
   - **Method Details**: technical approach
   - **Results & Findings**: experimental results
   - **Relevance to [domain]**: why it matters
   - **Related Work**: connections to other papers/techniques
   - **Backlinks**: `[[concept-name]]` wiki links to concepts
5. After writing, run: `python3 run.py ingest mark-compiled <filename>`

### 2. Extract & Write Concept Articles

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

### 3. Discover & Write Connection Articles

1. Read the full wiki
2. Find interesting connections between papers/concepts
3. Write short articles to `wiki/connections/{slug}.md`
4. Frontmatter: `title`, `slug`, `compiled` (ISO timestamp)
5. Include `[[links]]` to related papers and concepts

### 4. Generate & Maintain the Index

Write/update `wiki/index.md` with:
- Overview of the knowledge base
- Statistics (papers, concepts, connections count)
- Papers section with links: `[[paper-slug]]`
- Concepts section organized by category: `[[concept-slug]]`
- Connections section: `[[connection-slug]]`
- Venues covered
- Last updated timestamp

Use `[[wiki-links]]` (not `[Title](path.md)`) in the index so Obsidian graph view connects everything.

### 5. Answer Questions (Q&A)

When asked a question:
1. Read relevant wiki articles (use `wiki/` directory)
2. Answer with citations using `[[article-name]]` wiki links
3. If asked, save the answer as a report to `output/reports/`

### 6. Generate Slide Decks

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

### 7. Generate Visualizations

When asked for charts, diagrams, or visual comparisons:
1. Write a Python script using matplotlib/seaborn
2. Save images to `output/images/{name}.png`
3. Reference from wiki articles: `![[output/images/name.png]]`

### 8. Health Check & Lint

When asked to health-check:
1. Run `python3 run.py lint check` for structural issues first
2. Then read the wiki yourself and check for:
   - Inconsistencies between articles
   - Missing data or incomplete sections
   - Quality issues (too short, unclear)
   - Missing connections between related content
   - Outdated claims
3. Fix issues directly by editing the wiki files
4. Suggest improvements: new papers to add, concepts to cover, knowledge gaps

### 9. File Outputs Back into Wiki

When explorations or Q&A answers produce valuable content:
1. Save to `output/reports/` first
2. Then file into wiki: `python3 run.py qa file-to-wiki output/reports/file.md -s connections`
3. This makes explorations "add up" in the knowledge base, per Karpathy's approach

### 10. Suggest Improvements

When asked, analyze the wiki and suggest:
- **New papers**: real papers from top venues not yet covered
- **New concepts**: mentioned but undefined concepts
- **Connections**: non-obvious relationships
- **Research questions**: unanswered questions raised by content
- **Knowledge gaps**: thin coverage areas

Use web search to find real papers and verify claims when needed.

## Wiki Conventions

### Links
Use Obsidian-style `[[slug]]` links throughout. These create the navigable knowledge graph in Obsidian's graph view.

### File Naming
Slugified: lowercase, hyphens, no special chars. "Neural Cleanse" → `neural-cleanse.md`

### Images
- Remote images in raw sources: run `python3 run.py images download` to localize
- Images stored in `raw/images/` for source docs
- Generated images in `output/images/`
- Reference in wiki: `![[images/name.png]]` or `![alt](path/to/image.png)`

### Frontmatter
All wiki articles must have YAML frontmatter with at least `title` and `compiled` timestamp.

## Important Notes

- The user rarely edits wiki files directly — that's your domain
- Always use YAML frontmatter on wiki articles
- Keep articles focused and well-structured
- Link generously between articles with `[[wiki-links]]`
- When compiling, process all uncompiled sources, then extract concepts, then find connections, then update the index
- The project root IS the Obsidian vault — everything is viewable in Obsidian
- Graph view is color-coded: blue=papers, green=concepts, orange=connections
