import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import os
import yaml

plt.rcParams.update({
    'figure.facecolor': '#1a1a2e',
    'axes.facecolor': '#16213e',
    'axes.edgecolor': '#444',
    'axes.labelcolor': '#e6e6e6',
    'text.color': '#e6e6e6',
    'xtick.color': '#aaa',
    'ytick.color': '#aaa',
    'grid.color': '#333',
    'font.family': 'sans-serif',
    'font.size': 11,
})

PAPERS_DIR = 'wiki/papers'
OUTPUT_DIR = 'output/images'
os.makedirs(OUTPUT_DIR, exist_ok=True)

papers = []
for f in sorted(os.listdir(PAPERS_DIR)):
    if not f.endswith('.md'):
        continue
    with open(os.path.join(PAPERS_DIR, f)) as fh:
        content = fh.read()
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                fm = yaml.safe_load(parts[1])
                papers.append({
                    'slug': f.replace('.md', ''),
                    'venue': fm.get('venue', 'Unknown'),
                    'year': fm.get('year', 0),
                    'title': fm.get('title', ''),
                })
            except:
                pass


# --- Chart 1: Papers by Year (attack vs defense timeline) ---
years_all = {}
for p in papers:
    y = p['year']
    if y:
        years_all[y] = years_all.get(y, 0) + 1

years_sorted = sorted(years_all.keys())
counts = [years_all[y] for y in years_sorted]

fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.bar(years_sorted, counts, color='#00d4ff', edgecolor='#00a0cc', width=0.7)

for bar, count in zip(bars, counts):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
            str(count), ha='center', va='bottom', fontsize=10, fontweight='bold', color='#ffaa33')

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Number of Papers', fontsize=12)
ax.set_title('LLM Backdoor Defense KB: Papers by Year', fontsize=14, fontweight='bold', color='#00d4ff')
ax.set_xticks(years_sorted)
ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'papers-by-year.png'), dpi=200)
plt.close()
print('Saved papers-by-year.png')


# --- Chart 2: Venue Distribution (top 15) ---
venues = {}
for p in papers:
    v = p['venue']
    if v:
        v_clean = v.replace(' 2025', '').replace(' 2024', '').replace(' 2026', '')
        if v_clean.startswith('Findings of'):
            v_clean = 'Findings'
        if v_clean == 'Anthropic Transformer Circuits Thread':
            v_clean = 'Anthropic'
        if v_clean == 'Anthropic (arXiv)':
            v_clean = 'Anthropic'
        if v_clean == 'SafeAI@AAAI':
            v_clean = 'AAAI'
        venues[v_clean] = venues.get(v_clean, 0) + 1

venue_sorted = sorted(venues.items(), key=lambda x: -x[1])[:15]
venue_names = [v[0] for v in venue_sorted]
venue_counts = [v[1] for v in venue_sorted]

colors_venue = []
for v in venue_names:
    if v in ('IEEE S&P', 'CCS', 'USENIX Security', 'NDSS'):
        colors_venue.append('#e94560')
    elif v in ('NeurIPS', 'ICML', 'ICLR', 'AAAI', 'IJCAI'):
        colors_venue.append('#00d4ff')
    elif v in ('ACL', 'EMNLP', 'NAACL', 'TACL', 'Findings', 'ACL-IJCNLP', 'ICASSP'):
        colors_venue.append('#4ade80')
    elif v in ('Distill', 'Anthropic'):
        colors_venue.append('#a855f7')
    else:
        colors_venue.append('#888')

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(range(len(venue_names)), venue_counts, color=colors_venue, edgecolor='#333')
ax.set_yticks(range(len(venue_names)))
ax.set_yticklabels(venue_names)
ax.invert_yaxis()
ax.set_xlabel('Number of Papers', fontsize=12)
ax.set_title('Papers by Venue (Top 15)', fontsize=14, fontweight='bold', color='#00d4ff')
ax.grid(axis='x', alpha=0.3)

for bar, count in zip(bars, venue_counts):
    ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2,
            str(count), va='center', fontsize=10, fontweight='bold', color='#ffaa33')

from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='#00d4ff', label='ML/AI (A*)'),
    Patch(facecolor='#e94560', label='Security'),
    Patch(facecolor='#4ade80', label='NLP'),
    Patch(facecolor='#a855f7', label='Interpretability'),
    Patch(facecolor='#888', label='Other'),
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=9,
          facecolor='#1a1a2e', edgecolor='#444', labelcolor='#e6e6e6')

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'venue-distribution.png'), dpi=200)
plt.close()
print('Saved venue-distribution.png')


# --- Chart 3: Defense Method Comparison ---
defense_categories = {
    'Trigger Inversion\n& Model Scanning': [
        'Neural Cleanse', 'K-Arm', 'MNTD', 'T-Miner', 'BaDExpert',
        'TED', 'BAIT', 'CLIBE', 'BARBIE', 'DeBackdoor'
    ],
    'Activation &\nRepresentation': [
        'Spectral Sig.', 'Beatrix', 'ASSET', 'SPECTRE', 'BadActs',
        'Revisiting LS', 'LT-Defense', 'Decoupling', 'FABE', 'RepBend'
    ],
    'Pruning': [
        'Fine-Pruning', 'ANP', 'Anti-BL', 'Trap & Replace',
        'RNP', 'Neural Polarizer', 'PURE', 'PaRaMS'
    ],
    'Unlearning &\nRemoval': [
        'I-BAU', 'SAU', 'BEEAR', 'REFINE', 'Data-Free',
        'Sim & Elim', 'W2S', 'CleanGen', 'SANDE', 'GMS'
    ],
    'Input-Level &\nTraining-Time': [
        'ONION', 'RAP', 'Denoised PoE', 'SEEP',
        'Proactive Det.', 'PDB', 'FABE'
    ],
    'Certified &\nProvable': [
        'CBD', 'TextGuard', 'Fuzzed RS'
    ],
    'LLM-Specific\n(2025)': [
        'CROW', 'ICLShield', 'Chain-of-S', 'BEAT',
        'When Speak', 'Test-Time', 'Rethinking', 'PEFTGuard'
    ],
}

cat_names = list(defense_categories.keys())
cat_counts = [len(v) for v in defense_categories.values()]

colors_def = ['#e94560', '#ff6b6b', '#00d4ff', '#4ade80', '#ffaa33', '#a855f7', '#ff79c6']

fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.bar(range(len(cat_names)), cat_counts, color=colors_def, edgecolor='#333', width=0.7)
ax.set_xticks(range(len(cat_names)))
ax.set_xticklabels(cat_names, fontsize=9)
ax.set_ylabel('Number of Defense Papers', fontsize=12)
ax.set_title('Defense Methods by Category', fontsize=14, fontweight='bold', color='#00d4ff')
ax.grid(axis='y', alpha=0.3)
ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))

for bar, count in zip(bars, cat_counts):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
            str(count), ha='center', va='bottom', fontsize=11, fontweight='bold', color='#ffaa33')

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'defense-categories.png'), dpi=200)
plt.close()
print('Saved defense-categories.png')

print('\nAll charts generated successfully.')
