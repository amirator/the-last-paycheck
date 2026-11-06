"""Build the Kindle EPUB from the manuscript."""
import re, subprocess
from pathlib import Path

ROOT = Path(__file__).parent
MS = ROOT / "manuscript"

ORDER = ["01-introduction.md","02-ch01-tasks-not-jobs.md","03-ch02-the-canaries.md",
 "04-ch03-what-postings-say.md","05-ch04-what-people-use-ai-for.md",
 "06-ch05-middle-of-the-office.md","07-ch06-the-ladder-problem.md",
 "08-ch07-safe-zones.md","09-ch08-the-superworkers.md","10-ch09-countries.md",
 "11-ch10-historys-receipts.md","12-ch11-your-exposure-score.md",
 "13-ch12-for-parents.md","14-conclusion.md","15-toolkit.md","16-backmatter.md"]

FIG_ANCHORS = {
 "02-ch01-tasks-not-jobs.md": [("## What the exposure maps actually show",
   "![Figure 1.1. Exposure to LLMs across the US workforce. Source: Eloundou et al. (2023/2024).](figures/fig_1_1.png)\n\n")],
 "05-ch04-what-people-use-ai-for.md": [("## What this instrument can and cannot see",
   "![Figure 4.1. Augmentation vs automation in real AI conversations. Source: Anthropic Economic Index (Feb 2025).](figures/fig_4_1.png)\n\n")],
 "06-ch05-middle-of-the-office.md": [("## Who holds these jobs",
   "![Figure 5.1. Employment at highest automation risk, high-income countries. Source: ILO–NASK (2025).](figures/fig_5_1.png)\n\n")],
 "09-ch08-the-superworkers.md": [("## The jagged edge",
   "![Figure 8.1. Productivity gains with AI by experience. Sources: QJE 2025; Dell'Acqua et al. (2023).](figures/fig_8_1.png)\n\n")],
 "10-ch09-countries.md": [("## Forecasts, labeled as forecasts",
   "![Figure 9.1. Exposure by country income group. Source: IMF SDN/2024/001.](figures/fig_9_1.png)\n\n")],
 "11-ch10-historys-receipts.md": [("## Three waves, three verdicts",
   "![Figure 10.1. US bank teller employment after the ATM. Sources: Bessen (2015); Autor (2015).](figures/fig_10_1.png)\n\n")],
}

parts_before = {
 "02-ch01-tasks-not-jobs.md": "# PART I: WHAT IS REALLY HAPPENING {.part .unnumbered}\n\n",
 "06-ch05-middle-of-the-office.md": "# PART II: WHO WINS, WHO LOSES {.part .unnumbered}\n\n",
 "11-ch10-historys-receipts.md": "# PART III: WHAT TO DO {.part .unnumbered}\n\n",
}

front = (MS / "00-frontmatter.md").read_text()
_, rest = front.split("---COPYRIGHT---")
copyright_md, note_md = rest.split("---NOTE---")

chunks = []
chunks.append("# A Note on the Numbers {.unnumbered}\n" + note_md.split("## A note on the numbers")[1])

for f in ORDER:
    t = (MS / f).read_text()
    t = t.replace('**[FIGURE 2.1 — "Junior hiring fell first"]**',
      '![Figure 2.1. Employment of 22–25-year-olds by exposure, indexed to Nov 2022. Source: Brynjolfsson, Chandar & Chen (2026).](figures/fig_2_1.png)')
    t = t.replace('**[FIGURE 2.2 — "The gap is an age gradient"]**',
      '![Figure 2.2. Change by age band, Nov 2022–Jun 2026. Source: ibid.](figures/fig_2_2.png)')
    for anchor, fig in FIG_ANCHORS.get(f, []):
        t = t.replace(anchor, fig + anchor)
    chunks.append(parts_before.get(f, "") + t)

epub_md = "\n\n".join(chunks)
(ROOT / "epub_body.md").write_text(epub_md)

meta = """---
title: "The Last Paycheck"
subtitle: "Which Jobs AI Is Really Taking — and Which Are Safe"
author: "Amir M. Khan"
lang: en
date: 2026
rights: "Copyright © 2026 Amir Khan. All rights reserved."
...
"""
(ROOT / "epub_meta.md").write_text(meta)

css = """
body { font-family: serif; line-height: 1.5; }
h1 { font-family: sans-serif; font-weight: 800; font-size: 1.5em; margin-top: 1.4em; }
h2 { font-family: sans-serif; font-weight: 700; font-size: 1.1em; }
h1.part { color: #FF5A1F; text-align: center; margin-top: 35%; letter-spacing: 0.1em; }
img { max-width: 100%; }
figure { margin: 1em 0; } figcaption { font-size: 0.8em; color: #555; font-family: sans-serif; }
table { font-size: 0.78em; border-collapse: collapse; }
th { border-bottom: 2px solid #111; text-align: left; padding: 3px 5px; }
td { border-bottom: 1px solid #ccc; padding: 3px 5px; }
blockquote { border-left: 4px solid #FF5A1F; margin: 1em 0; padding-left: 0.8em;
  font-family: sans-serif; font-weight: bold; }
"""
(ROOT / "epub.css").write_text(css)

subprocess.run([
  "pandoc", "epub_meta.md", "epub_body.md",
  "-o", "The_Last_Paycheck.epub",
  "--epub-cover-image=cover_ebook_1600x2560.jpg",
  "--css=epub.css", "--toc", "--toc-depth=1",
  "--split-level=1", "-f", "markdown+smart",
], cwd=ROOT, check=True)
print("epub built")
