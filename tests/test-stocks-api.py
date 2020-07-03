#######
# Objective: Test whether stocks api is working properly
######

# Perform imports here:
from datetime import datetime, timedelta

import yfinance as yf

# msft = yf.Ticker("MSFT")
# print(msft.info)

# get historical market data, here max is 5 years.
data = yf.download(["V"], start="2020-06-01")
print(data)
#data = data[['Close']]
#data.to_csv("export_dataframe.csv")