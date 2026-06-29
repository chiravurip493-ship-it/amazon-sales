"""
Data loading utilities for Amazon sales analysis.
"""

import pandas as pd
from pathlib import Path


def load_csv(file_path):
    """
    Load a CSV file into a pandas DataFrame.
    
    Args:
        file_path: Path to the CSV file
        
    Returns:
        pandas.DataFrame: Loaded data
    """
    return pd.read_csv(file_path)


def load_all_csvs(directory):
    """
    Load all CSV files from a directory.
    
    Args:
        directory: Path to directory containing CSV files
        
    Returns:
        pandas.DataFrame: Combined data from all CSV files
    """
    dfs = []
    for csv_file in Path(directory).glob("*.csv"):
        dfs.append(pd.read_csv(csv_file))
    
    return pd.concat(dfs, ignore_index=True) if dfs else None


def save_data(df, file_path):
    """
    Save a DataFrame to CSV.
    
    Args:
        df: DataFrame to save
        file_path: Path where to save the file
    """
    df.to_csv(file_path, index=False)
