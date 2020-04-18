#######
# Objective: Get stocks data
######

# Perform imports here:
import pandas as pd
import pandas_datareader.data as web

def getdata(requireddata, start_date, end_date):
    start = datetime.strptime(start_date[:10], '%Y-%m-%d')
    end = datetime.strptime(end_date[:10], '%Y-%m-%d')
    filepath = 'config_stocks/' + requireddata + '.csv'
    data = pd.read_csv(filepath)
    data.set_index('ticker', inplace=True)
    traces = []
    for idx in data.index:
        tic = data['ticker'].loc[idx]
        df = web.DataReader(tic, 'iex', start, end)
        traces.append({'x':df.index, 'y': df.close, 'name':tic}) 
    return traces