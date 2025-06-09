import pytest
import pandas as pd
from project import calculate_sma_window, get_signal, take_position

def test_calculate_sma_window():
    data = {"close" : [1,2,3,4,5]}
    df = pd.DataFrame(data)
    df = calculate_sma_window(df, short_period=2, long_period=3)

    assert df["short_sma"].iloc[1] == 1.5
    assert df["long_sma"].iloc[2] == 2.0

def test_get_signal():
    df = pd.DataFrame({"short_sma":[3,3,3], "long_sma":[2,2,4]})
    df = get_signal(df)

    # Long when short SMA is higher and inverse
    expected_long = [True, True, False]
    expected_short = [False, False, True]

    assert df["long_bias"].tolist() == expected_long
    assert df["short_bias"].tolist() == expected_short

def test_take_postition():
    df = pd.DataFrame({
        "close": [10, 11, 12, 13],
        "open": [9,10,11,12],
        "long_bias": [True, True, False, False],
        "short_bias": [False, False, False, True]
    })

    df["entry_price"] = None
    df["exit_price"] = None
    df["direction"] = None

    df, position = take_position(df, position=0)

    assert df.loc[1, "direction"] == "long"
    assert df.loc[2, "direction"] == "exit_long"
    assert df.loc[3, "direction"] == "short"





