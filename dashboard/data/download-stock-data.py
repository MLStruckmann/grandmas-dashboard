import pandas as pd
import yfinance as yf
import json

stock_config = "usa"

df = pd.read_csv(f"/home/magnus/Projekte/grandmas-dashboard/dashboard/data/config_stocks/{stock_config}.csv")
data = df["ticker"].to_list()

# Define keys for stock reference data
keys = ["longName","symbol","sector","industry","country","sharesOutstanding","longBusinessSummary","currency"]

# Define start date for stock price data
start_date = "2000-01-01"

for stock in data:

    stock_dict = {}

    # Download reference data
    print(f"Download {stock} reference data")
    stock_reference = {}
    stock_info = yf.Ticker(stock)
    stock_reference = stock_info.info
    for key in keys:
        stock_dict[key] = stock_reference.get(key)

    # Download stock data
    print(f"Download {stock} stock data")
    stock_price = []
    stock_price = yf.download(stock, start=start_date)
    stock_price = stock_price[["Close"]]
    stock_price.index = stock_price.index.map(str)
    stock_price.index = stock_price.index.map(lambda x: x[:10])
    stock_dict["closingPrice"] = stock_price["Close"].to_dict()

    # Save data in json format
    file_name = f"/home/magnus/Projekte/grandmas-dashboard/dashboard/data/downloads/{stock_config}/{stock}.json"
    with open(file_name, "w", encoding="utf8") as fp:
        json.dump(stock_dict, fp, ensure_ascii=False)