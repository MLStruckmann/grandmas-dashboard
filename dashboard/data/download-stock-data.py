import pandas as pd
import yfinance as yf

filename = "usa.csv"

df = pd.read_csv("/home/magnus/Projekte/grandmas-dashboard/dashboard/data/config_stocks/" + filename)
data = df["ticker"].to_list()
print(type(data))
print(data)

for stock in data:
    print(f"Download {stock}")
    stock_data = yf.download(stock, start="2020-06-15")
    stock_data = stock_data[["Close"]]
    print(stock_data)
    print(type(stock_data))
    print(stock_data.shape)
    stock_data.to_csv(f"/home/magnus/Projekte/grandmas-dashboard/dashboard/data/downloads/{stock}.csv")



