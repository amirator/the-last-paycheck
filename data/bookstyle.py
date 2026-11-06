"""Shared chart style for The Last Paycheck. Greyscale-safe, one accent."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

import os
_BW = os.environ.get("BOOK_BW") == "1"
ACCENT = "#111111" if _BW else "#FF5A1F"      # the book's single accent
INK    = "#1A1A1A"      # titles, direct labels
GREY   = "#767676"      # context series / secondary text
LGREY  = "#B0B0B0"      # tertiary marks
GRID   = "#E3E3E0"

FIGDIR = Path(__file__).resolve().parent.parent / ("figures_bw" if _BW else "figures")
FIGDIR.mkdir(exist_ok=True)

plt.rcParams.update({
    "font.family": "Inter",
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "axes.edgecolor": GRID,
    "axes.linewidth": 0.8,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "xtick.color": GREY, "ytick.color": GREY,
    "xtick.labelsize": 8.5, "ytick.labelsize": 8.5,
    "text.color": INK,
    "axes.labelcolor": GREY,
    "axes.titlesize": 11,
})

def new_fig(h=3.0, w=4.6):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0)
    ax.set_axisbelow(True)
    return fig, ax

def finish(fig, ax, title, subtitle, source, fname, title_x=0.01, left=0.11, top=0.80):
    fig.text(title_x, 0.985, title, fontsize=11.5, fontweight="bold",
             color=INK, va="top", ha="left")
    fig.text(title_x, 0.908, subtitle, fontsize=8.5, color=GREY, va="top", ha="left")
    fig.text(title_x, 0.012, source, fontsize=6.4, color=GREY, va="bottom", ha="left")
    fig.subplots_adjust(top=top, bottom=0.17, left=left, right=0.97)
    out = FIGDIR / fname
    fig.savefig(out)
    plt.close(fig)
    print("wrote", out)
