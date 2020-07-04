#######
# Objective: Test whether stocks api is working properly
######

import yfinance as yf
import json

stock_reference = yf.Ticker("MSFT")
stock_reference_dict = stock_reference.info
keys = ["sector","country","industry","currency","sharesOutstanding","longBusinessSummary","symbol"]
reference_data = {}
for key in keys:
    reference_data[key] = stock_reference_dict.get(key)
file_name = reference_data["symbol"] + ".json"
with open(file_name, "w", encoding="utf8") as fp:
    json.dump(reference_data, fp, ensure_ascii=False)

# get historical market data, here max is 5 years.
#data = yf.download(["DAX"], start="2020-06-01")
#print(data)
#data = data[['Close']]
#data.to_csv("export_dataframe.csv")