"""Sample data helpers."""
import pandas as pd
import numpy as np

def sample_timeseries(n=100, seed=42):
    rng = np.random.RandomState(seed)
    dates = pd.date_range('2024-01-01', periods=n, freq='D')
    df = pd.DataFrame({
        'date': dates,
        'value': rng.randn(n).cumsum() + 100,
        'category': rng.choice(['A','B','C'], size=n)
    })
    return df

def sample_categorical(n=50, seed=1):
    rng = np.random.RandomState(seed)
    df = pd.DataFrame({
        'category': rng.choice(['X','Y','Z'], size=n),
        'count': rng.randint(1, 100, size=n)
    })
    return df
