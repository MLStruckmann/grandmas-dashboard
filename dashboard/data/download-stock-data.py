import pandas as pd
import yfinance as yf
import json
import datetime

config_directories = ["test"] #["asia", "europe", "germany", "indices", "usa"]

for stock_config in config_directories:

    df = pd.read_csv(f"/home/magnus/Projekte/grandmas-dashboard/dashboard/data/config_stocks/{stock_config}.csv")
    #data = df["ticker"].to_list()
    data = df.to_dict("index")

    # Define keys for stock reference data
    keys = ["longName","symbol","sector","industry","country","sharesOutstanding","longBusinessSummary","currency"]

    # Define start date for stock price data
    start_date = "2000-01-01"

    for stock in data.values():

        stock_dict = {}
        stock_name = stock["name"]
        stock_ticker = stock["ticker"]

        # Add custom name from CSV
        stock_dict["customName"] = stock_name

        # Download reference datasss
        print(f"Download {stock_name} reference data")
        stock_reference = {}
        stock_info = yf.Ticker(stock_ticker)
        stock_reference = stock_info.info
        for key in keys:
            stock_dict[key] = stock_reference.get(key)

        # Add regional group
        stock_dict["region"] = stock_config.title()

        # Add download timestamp
        stock_dict["downloadTimestamp"] = str(datetime.datetime.now())

        # Download stock data
        print(f"Download {stock_name} stock data")
        stock_price = []
        stock_price = yf.download(stock_ticker, start=start_date)
        stock_price = stock_price[["Close"]]
        stock_price.index = stock_price.index.map(str)
        stock_price.index = stock_price.index.map(lambda x: x[:10]) # Take only yyyy-mm-dd from datetime
        stock_dict["closingPrice"] = stock_price["Close"].to_dict()

        # Save data in json format
        stock_name = stock_name.replace(".", "_") # Replace dots in stock symbols with underscore
        stock_name = stock_name.replace("^", "") # Replace unwanted character in stock symbols
        file_name = f"/home/magnus/Projekte/grandmas-dashboard/dashboard/data/downloads/{stock_config}/{stock_ticker}.json"
        with open(file_name, "w", encoding="utf8") as fp:
            json.dump(stock_dict, fp, ensure_ascii=False)