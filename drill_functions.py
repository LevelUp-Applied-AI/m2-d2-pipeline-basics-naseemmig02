"""
Module 2 — Drill 2: Pipeline Basics

Write the two functions below from memory.
Remove the TODO: comments and pass statements as you implement each function.
Do not change the function signatures.
"""

import pandas as pd


def clean_column(series):
    """Fill NaN values with the series median. Returns the cleaned Series."""
    
    median_value = series.median()
    cleaned_series = series.fillna(median_value)
    
    return cleaned_series
    # TODO: Fill NaN values with series.median()
    # TODO: Return the cleaned Series
    pass


def compute_revenue(quantity, price):
    """Multiply quantity and price element-wise. Returns a revenue Series."""
    
    revenue = quantity * price
    
    return revenue
    # TODO: Multiply quantity and price element-wise
    # TODO: Return the result
    pass
