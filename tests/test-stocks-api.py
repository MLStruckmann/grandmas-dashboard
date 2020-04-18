#######
# Objective: Test whether stocks api is working properly
######

# Perform imports here:
import pandas as pd
import pandas_datareader.data as web
from datetime import datetime, timedelta
import os

teststock = 'APPL'
start_date = datetime.today() - timedelta(days=10)
end_date = datetime.today()

start = start_date.date()
end = end_date.date()

print(os.environ.get('IEX_TOKEN'))

#df = web.DataReader(teststock, 'iex', start, end)

#print(df.index, df.close)