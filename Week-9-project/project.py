import pandas as pd
import matplotlib as plt


def main():
    position = 0
    read_file = "ENQ2023Z_1min.csv"
    df = format_df(read_file)
    short_period, long_period, starting_cash, dollar_per_point, num_of_contracts = ajustable_variables()
    df = calculate_sma_window(df, short_period, long_period)
    df = get_signal(df)
    df, position = take_position(df, position)
    df, long_pnl, short_pnl, long_total, short_total, grand_total, equity = account_equity(df, starting_cash, dollar_per_point, num_of_contracts)
    visualisation(df, long_pnl, short_pnl, long_total, short_total, grand_total, equity)
    export(df)
    


def format_df(file):
    df = pd.read_csv(file, names=["contract", "date", "time", "open", 
                                                "high", "low", "close", "no_need", 
                                                "volume", "equity"])
    df = df.drop(columns="no_need")

    return df


def ajustable_variables():
    short_period = 2
    long_period = 14
    starting_account = 10_000
    dollar_per_point = 20
    num_of_contracts = 1
    return short_period, long_period, starting_account, dollar_per_point, num_of_contracts


def calculate_sma_window(df, short_period, long_period):
    df["short_sma"] = df["close"].rolling(window=short_period).mean()
    # short_sma = df["short_sma"]
    # print(short_sma)

    df["long_sma"] = df["close"].rolling(window=long_period).mean()
    # long_sma = df["long_sma"]
    # print(long_sma)
    return df


def get_signal(df):
    # There is no wait time here. This means the 
    # signal can change on the next candle. 
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
            df.at[i, "direction"] = "exit_long"

        # Exit short
        elif position == -1 and not df.at[i, "short_bias"]:
            position = 0
            exit_price = df.at[i, "open"] # Same here
            df.at[i, "exit_price"] = exit_price
            df.at[i, "direction"] = "exit_short"
    return df, position


def account_equity(df, starting_account, dollar_per_point, num_of_contracts):
    long_entry = None
    long_exit = None
    short_entry = None
    short_exit = None
    equity = starting_account
    long_pnl = []
    short_pnl = []

    df["equity"] = equity # Filling equity with starting balance

    for i in range(1, len(df)):

        if df.at[i, "direction"] == "long":
            long_entry = df.at[i, "entry_price"]

        elif df.at[i, "direction"] == "short":
            short_entry = df.at[i, "entry_price"]
        
        elif df.at[i, "direction"] == "exit_long":
            long_exit = df.at[i, "exit_price"]

        elif df.at[i, "direction"] == "exit_short":
            short_exit = df.at[i, "exit_price"]
        
        if long_entry is not None and long_exit is not None:
            pnl_1 = (long_exit - long_entry) * dollar_per_point * num_of_contracts
            long_pnl.append(pnl_1)
            long_entry = None
            long_exit = None
        elif short_entry is not None and short_exit is not None:    
            pnl_2 = (short_entry - short_exit) * dollar_per_point * num_of_contracts
            short_pnl.append(pnl_2)
            short_entry = None
            short_exit = None
        
        running_equity = sum(long_pnl) + sum(short_pnl) + starting_account
        df.at[i, "equity"] = running_equity

    long_total = sum(long_pnl)
    short_total = sum(short_pnl)
    grand_total = long_total + short_total
    equity = starting_account + grand_total

    return df, long_pnl, short_pnl, long_total, short_total, grand_total, equity


def visualisation(df, long_pnl, short_pnl, long_total, short_total, grand_total, equity):
    # print(df.tail(10))
    # print(df.dtypes)
    # print(f"{long_pnl=}")
    # print(f"{short_pnl=}")
    print(f"{long_total=}")
    print(f"{short_total=}")
    print(f"{grand_total=}")
    print(f"{equity=}")

    # plt.plot(df["date"], grand_total)


def export(df):
    df.to_excel("export.xlsx", index=False)


if __name__ == "__main__":
    main()


