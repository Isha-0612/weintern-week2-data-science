"""Execute Tasks 1–3 from the repository root with standard Jupyter tooling."""
from pathlib import Path
import nbformat
from nbclient import NotebookClient
ROOT = Path(__file__).resolve().parents[1]
for path in sorted((ROOT / 'notebooks').glob('*.ipynb')):
    notebook = nbformat.read(path, as_version=4)
    NotebookClient(notebook, timeout=1200, kernel_name='python3', resources={'metadata': {'path': str(ROOT)}}).execute()
    nbformat.write(notebook, path)
    print('Executed', path.name)
print('Results updated. PDF exports are snapshots of the submitted run; re-export if you change the data or code.')
