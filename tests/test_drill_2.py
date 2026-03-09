"""
Module 2 — Drill 2 CI Autograder Tests

DO NOT MODIFY THIS FILE. It is used by the GitHub Actions autograder.
"""

import pandas as pd
import numpy as np
import subprocess
import sys
from pathlib import Path


def test_drill_functions_file_exists():
    """drill_functions.py must exist at the repo root."""
    assert Path("drill_functions.py").exists(), "drill_functions.py not found"


def test_clean_column_exists_and_works():
    """clean_column fills NaN values with the series median."""
    from drill_functions import clean_column
    s = pd.Series([1.0, 2.0, np.nan, 4.0, 5.0])
    result = clean_column(s)
    assert result.isna().sum() == 0, "NaN values remain after clean_column"
    # Median of [1, 2, 4, 5] is 3.0
    assert result.iloc[2] == 3.0, f"Expected median fill 3.0, got {result.iloc[2]}"


def test_compute_revenue_exists_and_works():
    """compute_revenue multiplies quantity * price element-wise."""
    from drill_functions import compute_revenue
    q = pd.Series([10, 20, 5])
    p = pd.Series([2.5, 3.0, 10.0])
    result = compute_revenue(q, p)
    expected = pd.Series([25.0, 60.0, 50.0])
    pd.testing.assert_series_equal(result, expected, check_names=False)


def test_learner_tests_exist():
    """test_drill.py must exist at the repo root."""
    assert Path("test_drill.py").exists(), "test_drill.py not found"


def test_learner_tests_pass():
    """Learner's own tests in test_drill.py must pass."""
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "test_drill.py", "-v"],
        capture_output=True, text=True
    )
    assert result.returncode == 0, \
        f"Learner tests failed:\n{result.stdout}\n{result.stderr}"
