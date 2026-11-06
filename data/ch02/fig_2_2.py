"""Rebuilds fig_2_2.png (and all book figures) from the CSVs in /data."""
import runpy, pathlib
runpy.run_path(str(pathlib.Path(__file__).resolve().parents[1] / "make_figures.py"))
