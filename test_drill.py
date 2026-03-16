"""
Module 2 — Drill 2: Learner Test File

Write your two pytest test functions below.
The autograder will run these as part of the CI check.
"""

import pandas as pd
import numpy as np
from drill_functions import clean_column, compute_revenue


import pandas as pd
import numpy as np
from drill_functions import clean_column, compute_revenue


def test_clean_column():
    # Create a Series with a NaN value
    data = pd.Series([10, 20, np.nan, 40])
    
    # Clean the column
    result = clean_column(data)
    
    # Check that there are no NaN values
    assert result.isna().sum() == 0
    
    # Check that NaN was filled with the correct median
    expected_median = data.median()
    assert result.iloc[2] == expected_median


def test_compute_revenue():
    # Create quantity and price Series
    quantity = pd.Series([2, 3, 4])
    price = pd.Series([10, 20, 30])
    
    # Compute revenue
    result = compute_revenue(quantity, price)
    
    # Expected result
    expected = pd.Series([20, 60, 120])
    
    # Check equality
    assert result.equals(expected)
