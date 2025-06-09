import pandas as pd


def main():
    position = 0
    read_file = "ENQ2023Z_1min.csv"
    df = format_df(read_file)
    short_period, long_period = ajustable_variables()
    df = calculate_sma_window(df, short_period, long_period)
    df = get_signal(df)
    df, position = take_position(df, position)
    visualisation(df)
    export(df)
    


def format_df(file):
    df = pd.read_csv(file, names=["Contract", "date", "time", "open", 
                                                "high", "low", "close", "no_need", 
                                                "volume"])
    df = df.drop(columns="no_need")

    return df


def ajustable_variables():
    short_period = 2
    long_period = 10
    return short_period, long_period


def calculate_sma_window(df, short_period, long_period):
    df["short_sma"] = df["close"].rolling(window=short_period).mean()
    short_sma = df["short_sma"]
    # print(short_sma)

    df["long_sma"] = df["close"].rolling(window=long_period).mean()
    long_sma = df["long_sma"]
    # print(long_sma)
    return df


def get_signal(df):
    df["long_bias"] = df["short_sma"] > df["long_sma"]
    df["short_bias"] = df["short_sma"] < df["long_sma"]
    return df

def take_position(df, position):
    for i in range(1, len(df)):
        # Enter long
        if position == 0 and df.at[i, "long_bias"]:
            position = 1
            entry_price = df.at[i, "close"]
            df.at[i, "entry_price"] = entry_price
            df.at[i, "direction"] = "long"

        # Enter snort
        elif position == 0 and df.at[i, "short_bias"]:
            position = -1
            entry_price = df.at[i, "close"]
            df.at[i, "entry_price"] = entry_price
            df.at[i, "direction"] = "short"

        # Exit long
        elif position == 1 and not df.at[i, "long_bias"]:
            position = 0
            exit_price = df.at[i, "open"] # Using open price for exit price
            df.at[i, "exit_price"] = exit_price
            df.at[i, "direction"] = "exit long"

        # Exit short
        elif position == -1 and not df.at[i, "short_bias"]:
            position = 0
            exit_price = df.at[i, "open"] # Same here
            df.at[i, "exit_price"] = exit_price
            df.at[i, "direction"] = "exit short"
    return df, position


def account_equity():
    ...


def visualisation(df):
    print(df.tail(10))


def export(df):
    df.to_excel("export.xlsx", index=False)


if __name__ == "__main__":
    main()


