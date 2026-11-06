"""Build all figures for The Last Paycheck from /data CSVs."""
import csv, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from bookstyle import *  # noqa

D = Path(__file__).parent

def rows(p):
    with open(D / p) as f:
        return list(csv.DictReader(f))

# ---- Fig 2.1 slope ----------------------------------------------------------
fig, ax = new_fig(h=3.2)
ax.plot([0, 1], [100, 110], color=GREY, lw=2, marker="o", ms=5, zorder=3)
ax.plot([0, 1], [100, 89], color=ACCENT, lw=2.6, marker="o", ms=5, zorder=4)
ax.text(1.03, 110, "Least-exposed\noccupations  110", fontsize=8.5, color=GREY, va="center")
ax.text(1.03, 89, "Most-exposed\noccupations  89", fontsize=8.5, color=ACCENT, va="center", fontweight="bold")
ax.text(-0.03, 100, "100", fontsize=8.5, color=INK, va="center", ha="right")
ax.set_xlim(-0.12, 1.55); ax.set_ylim(82, 116)
ax.set_xticks([0, 1]); ax.set_xticklabels(["Nov 2022\n(ChatGPT launch)", "Jun 2026"])
ax.set_yticks([])
ax.grid(False)
for s in ["left", "bottom"]:
    ax.spines[s].set_visible(s == "bottom")
finish(fig, ax, "Junior hiring fell first",
       "Employment of 22-to-25-year-olds, indexed to Nov 2022 = 100",
       "Source: Brynjolfsson, Chandar & Chen (2026), ADP sample; top-2 vs bottom-3 exposure quintiles.  /data/ch02/fig_2_1.py",
       "fig_2_1.png")

# ---- Fig 2.2 age gradient ---------------------------------------------------
data = rows("ch02/fig_2_2.csv")
labels = [r["age_band"] for r in data]
vals = [float(r["gap_pp"]) for r in data]
fig, ax = new_fig(h=3.2)
colors = [ACCENT if l == "22-25" else LGREY for l in labels]
bars = ax.bar(labels, vals, color=colors, width=0.62, zorder=3)
ax.axhline(0, color=GREY, lw=0.9)
for b, v in zip(bars, vals):
    off = 0.9 if v >= 0 else -0.9
    ax.text(b.get_x() + b.get_width()/2, v + off, f"{v:+.1f}",
            ha="center", va="bottom" if v >= 0 else "top", fontsize=8.5,
            color=INK if v == min(vals) else GREY,
            fontweight="bold" if v == min(vals) else "normal")
ax.set_ylim(-23, 8); ax.set_yticks([])
ax.grid(False)
ax.spines["left"].set_visible(False)
finish(fig, ax, "The gap is an age gradient",
       "Most- vs least-exposed occupations, Nov 2022–Jun 2026, percentage points",
       "Source: Brynjolfsson, Chandar & Chen (2026), Table 1 Panel A.  /data/ch02/fig_2_2.py",
       "fig_2_2.png")

# ---- Fig 1.1 exposure bars --------------------------------------------------
data = rows("ch01/fig_1_1.csv")
fig, ax = new_fig(h=2.7)
labels = ["≥10% of tasks\nexposed", "≥50% exposed, incl.\nLLM software", "≥50% exposed,\ncurrent models only"]
vals = [float(r["share_pct"]) for r in data]
cols = [ACCENT, GREY, LGREY]
b = ax.barh(labels[::-1], vals[::-1], color=cols[::-1], height=0.58, zorder=3)
for bar, v in zip(b, vals[::-1]):
    ax.text(v + 1.5, bar.get_y() + bar.get_height()/2, f"{v:.0f}%",
            va="center", fontsize=9, color=INK, fontweight="bold")
ax.set_xlim(0, 95); ax.set_xticks([]); ax.grid(False)
ax.spines["bottom"].set_visible(False)
finish(fig, ax, "Exposure is broad; deep exposure is rarer",
       "Share of US workers by how much of their job's tasks LLMs could affect",
       "Source: Eloundou, Manning, Mishkin & Rock, “GPTs are GPTs” (2023/2024).  /data/ch01/fig_1_1.py",
       "fig_1_1.png", title_x=0.012, left=0.26)

# ---- Fig 4.1 augment/automate split ----------------------------------------
fig, ax = plt.subplots(figsize=(4.6, 2.3))
ax.barh([0], [57], color=GREY, height=0.5, zorder=3)
ax.barh([0], [43], left=[57.4], color=ACCENT, height=0.5, zorder=3)
ax.text(28.5, 0, "Augmentation  57%", ha="center", va="center", fontsize=10, color="white", fontweight="bold")
ax.text(79, 0, "Automation  43%", ha="center", va="center", fontsize=10, color="white", fontweight="bold")
ax.set_xlim(0, 100.5); ax.set_ylim(-0.6, 0.6)
ax.axis("off")
finish(fig, ax, "Most AI use helps a human; a large minority replaces one",
       "Classification of real AI conversations mapped to occupational tasks, first report",
       "Source: Anthropic Economic Index (Feb 2025).  /data/ch04/fig_4_1.py",
       "fig_4_1.png", top=0.70)

# ---- Fig 5.1 women vs men ---------------------------------------------------
data = rows("ch05/fig_5_1.csv")
fig, ax = new_fig(h=3.0)
import numpy as np
x = np.array([0, 1])
women = [7.8, 9.6]; men = [2.9, 3.5]
w = 0.32
b1 = ax.bar(x - w/2, women, width=w, color=ACCENT, zorder=3, label="Women")
b2 = ax.bar(x + w/2, men, width=w, color=LGREY, zorder=3, label="Men")
for bars, vals_, col in ((b1, women, INK), (b2, men, GREY)):
    for bar, v in zip(bars, vals_):
        ax.text(bar.get_x() + bar.get_width()/2, v + 0.25, f"{v}%", ha="center",
                fontsize=9, color=col, fontweight="bold" if col == INK else "normal")
ax.set_xticks(x); ax.set_xticklabels(["2023 index", "2025 index"])
ax.set_ylim(0, 12); ax.set_yticks([])
ax.grid(False); ax.spines["left"].set_visible(False)
ax.legend(frameon=False, fontsize=8.5, loc="upper left", handlelength=1.1)
finish(fig, ax, "The highest-risk desks are mostly women's",
       "Share of employment in jobs at highest automation risk, high-income countries",
       "Source: ILO–NASK refined global index (2025); 2023 vintage for comparison.  /data/ch05/fig_5_1.py",
       "fig_5_1.png")

# ---- Fig 8.1 novices gain most ---------------------------------------------
fig, ax = new_fig(h=3.1)
labels = ["Novice\nagents", "Average", "Bottom\nhalf", "Top\nhalf"]
vals = [34, 14, 43, 17]
xpos = [0, 1, 2.5, 3.5]
cols = [ACCENT, LGREY, ACCENT, LGREY]
bars = ax.bar(xpos, vals, color=cols, width=0.7, zorder=3)
for bx, v in zip(xpos, vals):
    ax.text(bx, v + 1.2, f"+{v}%", ha="center", fontsize=9, color=INK,
            fontweight="bold" if v in (34, 43) else "normal")
ax.set_xticks(xpos); ax.set_xticklabels(labels, fontsize=8.5)
ax.text(0.5, 50.5, "Call-center agents", ha="center", fontsize=8.3, color=GREY)
ax.text(3.0, 50.5, "BCG consultants", ha="center", fontsize=8.3, color=GREY)
ax.set_ylim(0, 55); ax.set_yticks([]); ax.grid(False)
ax.spines["left"].set_visible(False)
finish(fig, ax, "The newest workers gain the most",
       "Measured productivity / performance gain with an AI assistant",
       "Sources: QJE 140(2) 2025; HBS WP 24-013 (2023).  /data/ch08/fig_8_1.py",
       "fig_8_1.png")

# ---- Fig 9.1 exposure by income group --------------------------------------
data = rows("ch09/fig_9_1.csv")
fig, ax = new_fig(h=2.8)
labels = [r["group"] for r in data][::-1]
vals = [float(r["exposure_pct"]) for r in data][::-1]
cols = [LGREY, GREY, GREY, ACCENT]
bars = ax.barh(labels, vals, color=cols, height=0.58, zorder=3)
for bar, v in zip(bars, vals):
    ax.text(v + 1.3, bar.get_y() + bar.get_height()/2, f"{v:.0f}%", va="center",
            fontsize=9, color=INK, fontweight="bold")
ax.set_xlim(0, 70); ax.set_xticks([]); ax.grid(False)
ax.spines["bottom"].set_visible(False)
finish(fig, ax, "Exposure follows income",
       "Share of employment exposed to AI, by country income group",
       "Source: IMF Staff Discussion Note SDN/2024/001 (Cazzaniga et al., Jan 2024).  /data/ch09/fig_9_1.py",
       "fig_9_1.png", title_x=0.012, left=0.30)

# ---- Fig 10.1 tellers -------------------------------------------------------
data = rows("ch10/fig_10_1.csv")
yrs = [int(r["year"]) for r in data]
tel = [float(r["tellers_thousands"]) for r in data]
fig, ax = new_fig(h=3.0)
ax.plot(yrs, tel, color=ACCENT, lw=2.4, marker="o", ms=5, zorder=4)
ax.axvline(1969, color=GREY, lw=1, ls=(0, (3, 3)))
ax.text(1969.8, 470, "First ATM,\nSept 1969", fontsize=8, color=GREY, va="top")
for x_, y_, lab in zip(yrs, tel, ["~250k", "~400k", "~500k"]):
    ax.text(x_, y_ + 22, lab, ha="center", fontsize=8.5, color=INK, fontweight="bold")
ax.set_xlim(1966, 2014); ax.set_ylim(180, 560)
ax.set_yticks([]); ax.grid(False)
ax.spines["left"].set_visible(False)
ax.set_xticks([1970, 1980, 1990, 2000, 2010])
finish(fig, ax, "The ATM arrived — and teller jobs grew for decades",
       "US bank teller employment (approximate), 1970–2010",
       "Sources: Bessen, Learning by Doing (2015); Autor, JEP 29(3) 2015.  /data/ch10/fig_10_1.py",
       "fig_10_1.png")

print("all figures done")
