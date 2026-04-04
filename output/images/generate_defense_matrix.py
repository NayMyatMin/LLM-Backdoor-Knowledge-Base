#!/usr/bin/env python3
"""
Generate a defense coverage matrix heatmap: Attack Types vs. Defense Methods.
Effectiveness ratings based on wiki paper articles in the knowledge base.

Rating scale:
  3 = Strong (ASR < 5% after defense)
  2 = Partial (ASR 5-30% after defense)
  1 = Weak (ASR > 30% but some reduction)
  0 = Untested / Not applicable
"""

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

# ---------- axis labels ----------
attacks = [
    "Token-level triggers\n(BadNets, MTBA)",
    "Syntactic triggers\n(Hidden Killer, SynBkd)",
    "Semantic / Instruction\n(VPI, Instr-as-Backdoors)",
    "Model editing attacks\n(BadEdit, JailbreakEdit)",
    "ICL backdoors\n(ICLAttack, ICL-backdoor)",
    "RLHF poisoning\n(Universal Jailbreak)",
    "Code backdoors\n(CodeBreaker, TrojanPuzzle)",
    "Multimodal backdoors\n(BadCLIP, BadVision)",
    "Merging / Adapter attacks\n(BadMerging, Phil. Stone)",
    "Clean-label attacks\n(Poison Frogs, Triggerless)",
    "Dynamic triggers\n(WaNet, Input-Aware)",
]

defenses = [
    "Neural\nCleanse",
    "Spectral\nSig.",
    "STRIP",
    "Fine-\nPruning",
    "ANP",
    "I-BAU",
    "SAU",
    "ONION",
    "BEEAR",
    "CROW",
    "PURE",
    "BAIT",
    "PEFT\nGuard",
    "Rep\nBend",
    "Sim &\nElim",
]

# ---------- effectiveness matrix (rows=attacks, cols=defenses) ----------
# Columns order: NC, Spectral, STRIP, FP, ANP, I-BAU, SAU, ONION, BEEAR, CROW, PURE, BAIT, PEFTGuard, RepBend, Sim&Elim
data = np.array([
    # Token-level triggers (BadNets, MTBA)
    # Classic defenses strong; LLM defenses also handle these well
    [3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 2, 2, 3],

    # Syntactic triggers (Hidden Killer, SynBkd)
    # Hidden Killer explicitly evades ONION and Spectral; NC weak; ANP/I-BAU/SAU partial
    [1, 1, 1, 1, 2, 2, 2, 0, 2, 2, 2, 1, 1, 2, 2],

    # Semantic / Instruction triggers (VPI, Instructions-as-Backdoors)
    # Classic CV defenses largely inapplicable; LLM-specific defenses strong
    [0, 0, 0, 0, 0, 1, 1, 0, 3, 3, 2, 2, 1, 3, 3],

    # Model editing attacks (BadEdit, JailbreakEdit)
    # Very few defenses tested; fine-tuning resistant; RepBend designed for this
    [0, 0, 0, 1, 0, 0, 0, 0, 2, 2, 1, 1, 0, 3, 1],

    # ICL backdoors (ICLAttack, ICL-backdoor)
    # No weight modification -- most defenses not applicable
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0],

    # RLHF poisoning (Universal Jailbreak, RLHFPoison)
    # Classic defenses N/A; BEEAR, CROW, RepBend designed for safety backdoors
    [0, 0, 0, 0, 0, 0, 1, 0, 3, 3, 2, 1, 0, 3, 2],

    # Code backdoors (CodeBreaker, TrojanPuzzle)
    # Specialized domain; CROW tested on CodeLlama; most others untested
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 1, 1, 0, 1, 1],

    # Multimodal backdoors (BadCLIP, BadVision)
    # Different modality; very few text defenses applicable
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

    # Merging / Adapter attacks (BadMerging, Philosopher's Stone)
    # PEFTGuard specifically designed for this; most others N/A
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 3, 1, 0],

    # Clean-label attacks (Poison Frogs, Triggerless)
    # Spectral partial; NC weak; data-level defenses somewhat effective
    [1, 2, 1, 1, 2, 2, 2, 0, 1, 1, 1, 1, 0, 1, 1],

    # Dynamic triggers (WaNet, Input-Aware)
    # ANP explicitly strong; NC/Spectral/STRIP weak; SAU tested
    [1, 1, 1, 1, 3, 2, 3, 0, 1, 2, 2, 1, 0, 1, 2],
])

# ---------- colour map: dark-red (0) -> yellow (1) -> green (3) ----------
cmap = mcolors.LinearSegmentedColormap.from_list(
    "defense_cmap",
    [
        (0.0, "#8b0000"),   # 0 = untested / dark red
        (0.33, "#cc4400"),  # ~1 = weak / dark orange
        (0.55, "#ddaa00"),  # ~1.7 = approaching partial / gold
        (0.70, "#88aa00"),  # ~2 = partial / olive-green
        (1.0, "#228b22"),   # 3 = strong / forest green
    ],
)

# ---------- figure ----------
fig, ax = plt.subplots(figsize=(16, 10), facecolor="#1a1a2e")
ax.set_facecolor("#1a1a2e")

im = ax.imshow(data, cmap=cmap, vmin=0, vmax=3, aspect="auto")

# annotations
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        val = data[i, j]
        # choose text colour for readability
        txt_color = "white" if val <= 1 else "black"
        ax.text(j, i, str(val), ha="center", va="center",
                fontsize=11, fontweight="bold", color=txt_color)

# ticks & labels
ax.set_xticks(np.arange(len(defenses)))
ax.set_yticks(np.arange(len(attacks)))
ax.set_xticklabels(defenses, fontsize=9, color="white", ha="center")
ax.set_yticklabels(attacks, fontsize=9, color="white")
ax.tick_params(axis="both", which="both", length=0)

# move x-axis labels to top
ax.xaxis.set_ticks_position("top")
ax.xaxis.set_label_position("top")

# grid lines
for edge in range(data.shape[0] + 1):
    ax.axhline(edge - 0.5, color="#2a2a4e", linewidth=0.5)
for edge in range(data.shape[1] + 1):
    ax.axvline(edge - 0.5, color="#2a2a4e", linewidth=0.5)

# colour bar
cbar = fig.colorbar(im, ax=ax, fraction=0.025, pad=0.04)
cbar.set_ticks([0, 1, 2, 3])
cbar.set_ticklabels(["0 - Untested", "1 - Weak", "2 - Partial", "3 - Strong"])
cbar.ax.tick_params(colors="white", labelsize=9)
cbar.outline.set_edgecolor("#444466")

# title
ax.set_title(
    "Defense Coverage Matrix: Attack Types vs. Defense Methods",
    fontsize=15, fontweight="bold", color="white", pad=60,
)

plt.tight_layout()
plt.savefig(
    "output/images/defense-coverage-matrix.png",
    dpi=200, bbox_inches="tight", facecolor="#1a1a2e",
)
print("Saved: output/images/defense-coverage-matrix.png")
