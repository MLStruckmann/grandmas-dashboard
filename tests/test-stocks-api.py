#######
# Objective: Test whether stocks api is working properly
######

# Perform imports here:
import pandas as pd
import pandas_datareader.data as web
from datetime import datetime, timedelta
import os

teststock = 'AAPL'

start_date = datetime.today() - timedelta(days=10)
end_date = datetime.today()
start = start_date.date()
end = end_date.date()

IEX_key = os.environ.get('IEX_TOKEN')

print('This IEX API key was fetched:', IEX_key)

df = web.DataReader(teststock, 'iex', start, end, api_key = IEX_key)

print(df.index, df.close)