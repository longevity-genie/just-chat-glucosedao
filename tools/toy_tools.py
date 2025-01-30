import numpy as np
import pandas as pd

def generate_random_matrix(rows: int, cols: int) -> np.ndarray:
    """
    Generate a random matrix of given dimensions.

    Args:
        rows (int): Number of rows.
        cols (int): Number of columns.

    Returns:
        np.ndarray: A matrix filled with random values.
    """
    return np.random.rand(rows, cols)

def summarize_dataframe(data: dict) -> pd.DataFrame:
    """
    Convert a dictionary into a DataFrame and return basic statistics.

    Args:
        data (dict): A dictionary where keys are column names and values are lists.

    Returns:
        pd.DataFrame: A DataFrame summary with mean and standard deviation.
    """
    df = pd.DataFrame(data)
    return df.describe()
