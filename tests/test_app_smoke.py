"""Catch app startup failures that unit tests of the simulator cannot see."""

import ast
from pathlib import Path

from streamlit.testing.v1 import AppTest


def test_home_opens_without_exception():
    root = Path(__file__).resolve().parents[1]
    app = AppTest.from_file(str(root / "app/main.py")).run(timeout=20)
    assert not app.exception
    assert app.title[0].value == "FinLearnX"


def test_page_links_reference_pages_relative_to_main_script():
    root = Path(__file__).resolve().parents[1]
    for path in ("app/main.py", "app/pages/simulations.py", "app/pages/portfolio_review.py"):
        source = ast.parse((root / path).read_text())
        for node in ast.walk(source):
            if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Attribute):
                continue
            if node.func.attr == "page_link" and node.args and isinstance(node.args[0], ast.Constant):
                target = node.args[0].value
                assert (root / "app" / target).is_file(), f"Broken page link in {path}: {target}"
