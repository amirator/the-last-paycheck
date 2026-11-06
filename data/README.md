# The Last Paycheck — `/data`

Every chart in the book rebuilds from these CSVs. The values are the published summary figures named in the chapter endnotes (Eloundou et al., Brynjolfsson/Chandar/Chen, Anthropic Economic Index, ILO–NASK, IMF SDN/2024/001, Bessen/Autor via BLS occupational series, etc.). They are **not** a substitute for the underlying papers or agency tables — go to the cited source for methods and full series.

## Honesty

- **Citable sources only.** Every CSV cell maps to a number the book endnotes attribute to a public paper, agency, or named research institution.
- **Exposure ≠ displacement.** Do not relabel an exposure share as job loss (or the reverse) in a chart title or caption.
- **No invented rows.** If you extend a series, pull from the same public source family and date-stamp the pull. Do not fabricate ADP microdata or other non-public panels; cite the published paper figure instead.
- A yearly edition of the book is planned; re-run `make_figures.py` against updated CSVs when vintages change.

## Layout

- `make_figures.py` — builds all figures into `/figures` (set `BOOK_BW=1` for the greyscale print set in `/figures_bw`)
- `bookstyle.py` — shared style (Inter, accent `#FF5A1F`, greyscale-safe)
- `chXX/fig_X_Y.csv` — data behind each figure
- `chXX/fig_X_Y.py` — convenience runner for that figure

Requires: Python 3, matplotlib, Inter font (falls back if missing — see `bookstyle.py`).
