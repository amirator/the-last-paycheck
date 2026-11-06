"""Typeset The Last Paycheck: 6x9 KDP interior PDF from manuscript markdown."""
import re, markdown
from pathlib import Path

ROOT = Path(__file__).parent
MS = ROOT / "manuscript"
import os
BW = os.environ.get("BOOK_BW") == "1"
FIG = ROOT / ("figures_bw" if BW else "figures")
ACC = "#111111" if BW else "{ACC}"

SUP = {"⁰":"0","¹":"1","²":"2","³":"3","⁴":"4","⁵":"5","⁶":"6","⁷":"7","⁸":"8","⁹":"9"}

def md(text):
    return markdown.markdown(text, extensions=["tables", "smarty"])

def supify(html):
    # turn runs of unicode superscript digits into <sup> tags (font-safe)
    return re.sub("([" + "".join(SUP) + "]+)",
                  lambda m: "<sup>" + "".join(SUP[c] for c in m.group(1)) + "</sup>", html)

def load(name):
    return (MS / name).read_text()

def split_notes(text):
    """Return (body_md, notes_md or None), splitting at '## Notes'."""
    parts = re.split(r"\n## Notes\n", text, maxsplit=1)
    return (parts[0], parts[1] if len(parts) > 1 else None)

def fig_html(fname, num, caption):
    return (f'<div class="figure"><img src="{FIG.as_posix()}/{fname}"/>'
            f'<p class="figcap"><b>Figure {num}.</b> {caption}</p></div>')

PULL = {
 "01": "47% of jobs were “at risk” in 2013. Here’s what happened.",
 "02": "1 in 4 jobs worldwide is exposed to generative AI.",
 "03": "Young workers in AI-exposed jobs: 19% below trend. Their older colleagues: no gap at all.",
 "04": "Entry-level postings: down 7.5%. Senior postings: up 14.7%.",
 "05": "57% of real AI use helps a human. 43% replaces one, so far.",
 "06": "The most exposed job category is also the biggest source of women’s office work.",
 "07": "Same job. Same firm. Only the 22-year-olds vanished.",
 "08": "A plumber’s exposure score, in full: approximately zero.",
 "09": "The newest call-center agents gained 34%. Veterans gained almost nothing.",
 "10": "60% of jobs in rich countries are exposed. 26% in poor ones.",
 "11": "The ATM arrived in 1969. Teller employment peaked decades later.",
 "12": "Score your own job in 30 minutes.",
 "13": "“Learn to code” was the advice. Coding is now on the exposed list.",
}

FIGS = {  # file -> (anchor heading in html, figure file, number, caption)
 "02": [("<h2>What the exposure maps actually show</h2>", "fig_1_1.png", "1.1",
         "Exposure to large language models across the US workforce. Source: Eloundou et al. (2023/2024).")],
 "05": [("<h2>What this instrument can and cannot see</h2>", "fig_4_1.png", "4.1",
         "Augmentation vs automation in real AI conversations. Source: Anthropic Economic Index (Feb 2025).")],
 "06": [("<h2>Who holds these jobs</h2>", "fig_5_1.png", "5.1",
         "Share of employment in jobs at highest automation risk, high-income countries. Source: ILO–NASK (2025).")],
 "09": [("<h2>The jagged edge</h2>", "fig_8_1.png", "8.1",
         "Productivity gains with an AI assistant, by worker experience/skill. Sources: Brynjolfsson, Li & Raymond (2025); Dell’Acqua et al. (2023).")],
 "10": [("<h2>Forecasts, labeled as forecasts</h2>", "fig_9_1.png", "9.1",
         "Share of employment exposed to AI by country income group. Source: IMF SDN/2024/001.")],
 "11": [("<h2>Three waves, three verdicts</h2>", "fig_10_1.png", "10.1",
         "US bank teller employment after the ATM. Sources: Bessen (2015); Autor (2015).")],
}

ORDER = [
 ("01-introduction.md", "intro", None),
 ("02-ch01-tasks-not-jobs.md", "chapter", "PART I: WHAT IS REALLY HAPPENING"),
 ("03-ch02-the-canaries.md", "chapter", None),
 ("04-ch03-what-postings-say.md", "chapter", None),
 ("05-ch04-what-people-use-ai-for.md", "chapter", None),
 ("06-ch05-middle-of-the-office.md", "chapter", "PART II: WHO WINS, WHO LOSES"),
 ("07-ch06-the-ladder-problem.md", "chapter", None),
 ("08-ch07-safe-zones.md", "chapter", None),
 ("09-ch08-the-superworkers.md", "chapter", None),
 ("10-ch09-countries.md", "chapter", None),
 ("11-ch10-historys-receipts.md", "chapter", "PART III: WHAT TO DO"),
 ("12-ch11-your-exposure-score.md", "chapter", None),
 ("13-ch12-for-parents.md", "chapter", None),
 ("14-conclusion.md", "chapter", None),
 ("15-toolkit.md", "chapter", None),
]

def chapter_html(fname, kind, part):
    key = fname[:2]
    body_md, notes_md = split_notes(load(fname))
    # pull title out
    m = re.match(r"# (.+)\n", body_md)
    title = m.group(1)
    body_md = body_md[m.end():]
    html = md(body_md)
    html = supify(html)

    # figure markers in ch02 text
    html = html.replace('<p><strong>[FIGURE 2.1 — &ldquo;Junior hiring fell first&rdquo;]</strong></p>',
        fig_html("fig_2_1.png", "2.1", "Employment of 22–25-year-olds by occupation exposure, indexed to Nov 2022. Source: Brynjolfsson, Chandar & Chen (2026)."))
    html = html.replace('<p><strong>[FIGURE 2.2 — &ldquo;The gap is an age gradient&rdquo;]</strong></p>',
        fig_html("fig_2_2.png", "2.2", "Most- vs least-exposed employment change by age band, Nov 2022–Jun 2026. Source: ibid., Table 1 Panel A."))

    # anchored figures
    for anchor, f, num, cap in FIGS.get(key, []):
        html = html.replace(anchor, fig_html(f, num, cap) + anchor)

    html = html.replace("<h2>The blank worksheet</h2>", '<h2 class="fresh">The blank worksheet</h2>')

    # pull-stat card after 3rd paragraph
    if key in PULL:
        paras = html.split("</p>")
        if len(paras) > 3:
            paras[2] = paras[2] + f'</p><div class="pullstat">{PULL[key]}</div>'
            html = "</p>".join(paras)

    part_html = f'<section class="part"><h1>{part}</h1></section>' if part else ""
    ttl = title.replace(": ", ':</span><span class="subt">') \
          if ": " in title else title
    if "</span>" in ttl:
        ttl = f'<span class="chnum">{ttl}</span>'
    notes = ""
    if notes_md:
        notes = f'<div class="notes-src" data-title="{title}">{supify(md(notes_md))}</div>'
    return (part_html +
            f'<section class="{kind}" id="{key}">'
            f'<h1 class="chtitle" data-rh="{title}">{ttl}</h1>{html}</section>'), title, notes

# ---- assemble ----------------------------------------------------------------
front = load("00-frontmatter.md").split("---COPYRIGHT---")
half_title = front[0]
copyright_md, note_md = front[1].split("---NOTE---")
back_md = load("16-backmatter.md")

chapters, toc_entries, all_notes = [], [], []
for fname, kind, part in ORDER:
    h, title, notes = chapter_html(fname, kind, part)
    chapters.append(h)
    toc_entries.append((fname[:2], title))
    if notes:
        all_notes.append((title, notes))

toc_html = "".join(
    f'<p class="tocline"><a href="#{k}">{t}</a>'
    f'<span class="tocpg"><a href="#{k}"></a></span></p>'
    for k, t in toc_entries)

notes_html = "".join(
    f'<h2 class="notes-ch">{t}</h2>{re.sub(chr(34)+r"notes-src"+chr(34), chr(34)+"notes-body"+chr(34), n)}'
    for t, n in all_notes)

back_html = supify(md(back_md))

html_doc = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@page {{ size: 6in 9in; margin: 0.72in 0.56in 0.78in 0.56in; }}
@page :left {{ margin-left: 0.56in; margin-right: 0.78in;
  @bottom-center {{ content: counter(page); font-family: Inter; font-size: 8pt; color:#555; }}
  @top-left {{ content: "THE LAST PAYCHECK"; font-family: Inter; font-size: 7pt;
               letter-spacing: 0.12em; color:#888; }} }}
@page :right {{ margin-left: 0.78in; margin-right: 0.56in;
  @bottom-center {{ content: counter(page); font-family: Inter; font-size: 8pt; color:#555; }}
  @top-right {{ content: string(chtitle); font-family: Inter; font-size: 7pt;
                letter-spacing: 0.08em; color:#888; }} }}
@page bare {{ @bottom-center {{ content: ""; }} @top-left {{ content: ""; }} @top-right {{ content: ""; }} }}
@page bare:left {{ @bottom-center {{ content: ""; }} @top-left {{ content: ""; }} }}
@page bare:right {{ @bottom-center {{ content: ""; }} @top-right {{ content: ""; }} }}
@page :blank {{ @bottom-center {{ content: ""; }} @top-left {{ content: ""; }} @top-right {{ content: ""; }} }}

body {{ font-family: "Charter", "Bitstream Charter", serif; font-size: 10.6pt;
       line-height: 1.52; color: #111; }}
p {{ margin: 0 0 0 0; text-indent: 1.3em; text-align: justify; hyphens: auto; }}
h2 + p, .chtitle + p, .pullstat + p, .figure + p, blockquote + p, ul + p, ol + p, table + p
  {{ text-indent: 0; }}
section.front, section.part, #half, #titlepg, #copyright, #toc {{ page: bare; }}

#half {{ page-break-after: always; text-align: center; padding-top: 2.6in; }}
#half h1 {{ font-family: Inter; font-size: 15pt; letter-spacing: 0.22em; font-weight: 600; }}
#titlepg {{ page-break-after: always; text-align: center; padding-top: 2.0in; }}
#titlepg .t1 {{ font-family: Inter; font-weight: 800; font-size: 27pt; letter-spacing: 0.02em; line-height:1.12; }}
#titlepg .t2 {{ font-family: Inter; font-weight: 400; font-size: 11.5pt; color:#333; margin-top: 0.35in; }}
#titlepg .rule {{ width: 1.1in; border-top: 3px solid {ACC}; margin: 0.3in auto; }}
#titlepg .auth {{ font-family: Inter; font-weight: 600; font-size: 13pt; margin-top: 0.9in; letter-spacing:0.08em; }}
#copyright {{ page-break-after: always; font-size: 8.3pt; color:#333; padding-top: 4.3in; line-height: 1.5; }}
#copyright p {{ text-indent: 0; margin-bottom: 5pt; text-align: left; }}
#toc {{ page-break-after: always; }}
#toc h1, .notes h1, #back h1 {{ font-family: Inter; font-weight: 800; font-size: 17pt; margin: 0.4in 0 0.3in 0; }}
#back h1 {{ page-break-before: right; }}
.tocline {{ text-indent: 0 !important; margin: 0 0 6pt 0 !important; font-size: 10pt; text-align: left !important; }}
.tocline a {{ text-decoration: none; color: #111; }}
.tocpg a::after {{ content: target-counter(attr(href), page); }}
.tocline {{ display: flex; }} .tocline > a {{ flex: 1; }}
.tocpg {{ font-family: Inter; font-size: 9pt; color:#555; }}

section.part {{ page-break-before: right; text-align: center; padding-top: 3.1in; }}
section.part h1 {{ font-family: Inter; font-size: 13pt; font-weight: 700; letter-spacing: 0.18em; color:{ACC}; }}

section.chapter, section.intro, section.front {{ page-break-before: right; }}
.chtitle {{ font-family: Inter; font-weight: 800; font-size: 19pt; line-height: 1.2;
            margin: 0.55in 0 0.32in 0; string-set: chtitle attr(data-rh); }}
.chtitle .chnum {{ display: block; }}
.chtitle .subt {{ display: block; font-size: 19pt; }}
h2.fresh {{ page-break-before: always; }}
h2.fresh + p + table {{ page-break-inside: avoid; }}
h2 {{ font-family: Inter; font-weight: 700; font-size: 12pt; margin: 14pt 0 5pt 0;
      page-break-after: avoid; }}
strong {{ font-weight: bold; }}
ul, ol {{ margin: 5pt 0 7pt 1.1em; padding-left: 0.9em; }}
li {{ margin-bottom: 3pt; text-align: justify; }}
sup {{ font-size: 7pt; line-height: 0; font-family: Inter; }}

.pullstat {{ border-top: 2.5px solid {ACC}; border-bottom: 0.7px solid #ddd;
  font-family: Inter; font-weight: 700; font-size: 12.5pt; line-height: 1.35;
  padding: 9pt 2pt 10pt 2pt; margin: 12pt 0.15in; page-break-inside: avoid; }}
.figure {{ margin: 11pt 0; page-break-inside: avoid; text-align: center; }}
.figure img {{ width: 4.35in; }}
.figcap {{ font-family: Inter; font-size: 8pt; color:#444; text-indent: 0 !important;
           text-align: left; margin-top: 3pt; }}

table {{ border-collapse: collapse; font-family: Inter; font-size: 7.6pt; margin: 9pt 0;
         width: 100%; page-break-inside: auto; }}
th {{ border-bottom: 1.4px solid #111; text-align: left; padding: 3pt 4pt; font-weight: 700; }}
td {{ border-bottom: 0.5px solid #ccc; padding: 3pt 4pt; vertical-align: top; }}
.notes {{ page-break-before: right; }}
.notes-ch {{ font-family: Inter; font-weight: 700; font-size: 10.5pt; margin: 12pt 0 4pt 0; }}
.notes-body ol {{ font-size: 8.4pt; line-height: 1.4; color:#222; }}
.notes-body li {{ text-align: left; }}
.notes-body p {{ text-indent: 0; text-align: left; font-size: 8.4pt; }}
hr {{ border: none; border-top: 0.7px solid #ccc; margin: 10pt 0; }}
a {{ color: #111; text-decoration: none; }}
</style></head><body>

<section id="half"><h1>THE LAST PAYCHECK</h1></section>

<section id="titlepg">
  <div class="t1">THE LAST<br/>PAYCHECK</div>
  <div class="rule"></div>
  <div class="t2">Which Jobs AI Is Really Taking —<br/>and Which Are Safe</div>
  <div class="auth">AMIR M. KHAN</div>
</section>

<section id="copyright">{md(copyright_md)}</section>

<section id="toc"><h1>Contents</h1>{toc_html}
<p class="tocline"><a href="#notesec">Notes</a><span class="tocpg"><a href="#notesec"></a></span></p>
</section>

<section class="front">{supify(md(note_md))}</section>

{''.join(chapters)}

<section class="chapter notes" id="notesec"><h1 class="chtitle">Notes</h1>
<p style="text-indent:0; font-size:9pt; color:#444;">Every number in this book, by chapter, with its source. URLs were live at the time of writing; access dated November 2026.</p>
{notes_html}</section>

<section class="chapter" id="back">{back_html}</section>

</body></html>"""

out_html = ROOT / "book.html"
out_html.write_text(html_doc)
print("html written", len(html_doc))

from weasyprint import HTML
HTML(str(out_html)).write_pdf(str(ROOT / ("The_Last_Paycheck_interior_6x9_PRINT_greyscale.pdf" if BW else "The_Last_Paycheck_interior_6x9.pdf")))
print("pdf written")
