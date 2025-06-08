import pandas as pd

df = pd.read_csv("ENQ2023Z_1min.csv", names=["Contract", "Date", "Time", "Open", 
                                             "High", "Low", "Close", "Volume", 
                                             "Something"])
print(df.head(3))