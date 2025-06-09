import pandas as pd
def main():
    read_file = "ENQ2023Z_1min.csv"
    df = format_df(read_file)
    df = calculate_sma_window(df)
    visualisation(df)
    


def format_df(file):
    df = pd.read_csv(file, names=["Contract", "Date", "Time", "Open", 
                                                "High", "Low", "Close", "No_need", 
                                                "Volume"])
    df = df.drop(columns="No_need")
    return df


def calculate_sma_window(data):
    ...


def get_signal():
    ...

def take_position():
    ...


def account_equity():
    ...


def visualisation(df):
    print(df.head())


if __name__ == "__main__":
    main()


