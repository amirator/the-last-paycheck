# The Last Paycheck — companion repository

**Book:** *The Last Paycheck: Which Jobs AI Is Really Taking — and Which Are Safe*  
**Author:** Amir Khan (Independent Researcher)  
**Amazon listing:** TBD — APPLICATIONS AND FORMS will supply the URL when the listing goes live.

This is the public home for the **data and scripts behind every chart** in the book (promised on the copyright / About the Author pages).

- ORCID: [0009-0008-5996-2841](https://orcid.org/0009-0008-5996-2841)
- GitHub: [amirator](https://github.com/amirator)
- LinkedIn: [amirator1](https://www.linkedin.com/in/amirator1)

---

## Honesty rules

Same rules as the book’s “A note on the numbers”:

1. **Every number is citable** from a public source (peer-reviewed paper, government statistical agency, or named research institution). Chapter endnotes name the source; the CSVs in `/data` hold the summary values used to draw the figures.
2. **Exposure ≠ displacement.** Exposure = what AI *could* do to tasks on paper. Displacement = what employment records show *is* happening. Chart titles and captions must keep those distinct.
3. **No invented interviews or quotes.** Data vintages are named in the text (generally mid-to-late 2026). A yearly edition is planned.
4. **Underlying microdata stays where it lives.** Where a paper uses non-public panels (e.g. ADP payroll in the Stanford Digital Economy Lab “Canaries” work), this repo stores the **published summary series** used in the figure, not a fabricated microdata dump. Read the paper for methods.

Acceptable source families include: BLS, O\*NET, ILO, OECD, IMF, WEF, Indeed Hiring Lab, Lightcast public research reports, ADP Research / papers that publish ADP-based findings, Anthropic Economic Index, and peer-reviewed / NBER / SSRN / arXiv work.

---

## What’s in this repo

| Path | Contents |
|------|----------|
| `manuscript/` | Chapter markdown used to build the book |
| `data/` | CSVs + `make_figures.py` / `bookstyle.py` to rebuild charts |
| `figures/` | Colour figures (accent `#FF5A1F`) |
| `figures_bw/` | Greyscale print set (`BOOK_BW=1`) |
| `build_book.py` / `build_epub.py` / `make_cover.py` | Build helpers |
| `CITATION.cff` | Citation stub (ISBN / Amazon URL TBD) |
| `LICENSE` | MIT for **code and chart-rebuild scripts** in this repository |

The book text and cover art remain the author’s copyright; they are not licensed under MIT. Datasets you download yourself remain under their agency/publisher licenses.

---

## Rebuild the charts

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cd data && python make_figures.py
# greyscale print set:
BOOK_BW=1 python make_figures.py
```

Or run a single figure: `python data/ch02/fig_2_1.py`.

---

## Figures

| Figure | File | Source named in the book |
|------|------|---------------------------|
| 1.1 Exposure to LLMs (US) | `data/ch01/` | Eloundou et al. (2023/2024) |
| 2.1 Junior hiring by exposure | `data/ch02/` | Brynjolfsson, Chandar & Chen (2026) |
| 2.2 Change by age band | `data/ch02/` | ibid. |
| 4.1 Augmentation vs automation | `data/ch04/` | Anthropic Economic Index (Feb 2025) |
| 5.1 Highest automation risk (women/men) | `data/ch05/` | ILO–NASK (2025) |
| 8.1 Productivity gains by experience | `data/ch08/` | QJE 2025; Dell’Acqua et al. (2023) |
| 9.1 Exposure by income group | `data/ch09/` | IMF SDN/2024/001 |
| 10.1 US bank tellers after the ATM | `data/ch10/` | Bessen (2015); Autor (2015) / BLS series |

---

## Citation

Until ISBN and Amazon URL are filled in `CITATION.cff`:

```
Khan, Amir. The Last Paycheck: Which Jobs AI Is Really Taking — and Which Are Safe.
2026. Companion data: https://github.com/amirator/the-last-paycheck
ORCID: https://orcid.org/0009-0008-5996-2841
```
