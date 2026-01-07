import os
import glob
import nbformat
import pytest

# Path to your notebooks folder
NOTEBOOKS_DIR = os.path.join(os.path.dirname(__file__), "..", "notebooks")

@pytest.mark.parametrize("nb_file", glob.glob(os.path.join(NOTEBOOKS_DIR, "*.ipynb")))
def test_notebook_syntax(nb_file):
    """
    Ensure all notebooks can be parsed without syntax/indentation errors.
    """
    try:
        with open(nb_file, "r", encoding="utf-8") as f:
            nbformat.read(f, as_version=4)
    except Exception as e:
        pytest.fail(f"Notebook {nb_file} has a syntax/format error: {e}")
