# ReDI Python Workshop: The festival fund fiasco

Investigate a fictional festival fund using three small CSV files.
Start with [the case brief](docs/student-brief.md), then open
[the scaffold notebook](notebooks/festival-investigation.ipynb).
[Hints](docs/hints.md) are available when you need them.

## Setup

Use Python 3.10 or newer. Extract the entire ZIP before opening the notebook.
Keep its folders together.

**No-install route:** write a Python script using `csv`, `decimal`, and
`pathlib` from the standard library. Run it from the extracted project root
with `python your_script.py` (or `python3` if that is your Python command).
The case brief lists all tasks; the notebook is not required.

**Notebook route:** from the extracted project root:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m jupyterlab
```

On Windows, use `py -m venv .venv` and activate with
`.venv\Scripts\Activate.ps1` in PowerShell instead of `source`.
If activation is restricted, use `.venv\Scripts\python.exe` directly for
the pip and Jupyter commands.

Open `notebooks/festival-investigation.ipynb` in JupyterLab. In VS Code,
install the Python and Jupyter extensions, open the notebook, and select
the `.venv` interpreter as its kernel. The notebook needs only the standard
library for core tasks; Pandas and Matplotlib are optional stretch tools.

## Submit

Your runnable code, a cleaning log, labelled numerical results, and a short
evidence-based verdict. An optional chart can support your explanation.
Do not edit the source CSVs to make your code work.
