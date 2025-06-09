import pytest
import pandas as pd
from project import calculate_sma_window

def test_calculate_sma_window():
    data = {"close" : [1,2,3,4,5]}
    df = pd.DataFrame(data)
    df = calculate_sma_window(df, short_period=2, long_period=3)

    assert df["short_sma"].iloc[1] == 1.5
    assert df["long_sma"].iloc[2] == 2.0


