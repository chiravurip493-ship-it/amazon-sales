"""
Unit tests for data loader module.
"""

import pytest
import pandas as pd
from src.data_loader import load_csv, save_data


def test_save_and_load():
    """Test saving and loading a DataFrame."""
    df = pd.DataFrame({
        'product': ['A', 'B', 'C'],
        'sales': [100, 200, 300]
    })
    
    # Save
    save_data(df, 'test_data.csv')
    
    # Load
    loaded_df = load_csv('test_data.csv')
    
    assert loaded_df.shape == df.shape
    assert list(loaded_df.columns) == list(df.columns)
