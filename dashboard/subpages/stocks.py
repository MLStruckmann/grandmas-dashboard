#######
# Objective: visualize stocks data
######

# Perform imports here:
import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime

def stocks():
    return html.Div([

        html.Div([
            html.H3('Select start and end dates:'),
            dcc.DatePickerRange(
                id='my_date_picker',
                min_date_allowed=datetime(2006, 1, 1),
                max_date_allowed=datetime.today(),
                end_date=datetime.today(),
                display_format='DD.MM.YYYY',
                start_date_placeholder_text='DD.MM.YYYY'
            )
        ]),

        html.Div([
            html.Div(dcc.Graph(
                id='my_graph',
                figure={
                    'data': [
                        {'x': [1,2], 'y': [3,1]}
                    ]
                }
            ), style={'display':'inline-block','float':'left'}),
            html.Div([
                html.H3('Select stock symbols:', style={'paddingRight':'30px'}),
                html.Div([
                        dcc.RadioItems(
                            options=[
                                {'label': 'Indices', 'value': 'indices'},
                                {'label': 'Watchlist', 'value': 'watchlist'}
                            ],
                            value='indices',
                            id='ticker_collection'),                         
                        # dcc.Dropdown(
                        #     id='ticker_collection',
                        #     options=options,
                        #     value=['XOM'],
                        #     multi=True),      
                ])
            ], style={'display':'inline-block','float':'right'})
        ], style={'display':'inline-block'})
    ])

    # @app.callback(
    #     Output('my_graph', 'figure'),
    #     [State('ticker_collection', 'value'),
    #     State('my_date_picker', 'start_date'),
    #     State('my_date_picker', 'end_date')])
    # def update_graph(stock_ticker, start_date, end_date):
    #     traces, start, end = data.getstocks(stock_ticker, start_date, end_date)
    #     fig = {
    #         'data': traces,
    #         'layout': {'title':', '.join(stock_ticker)+' Closing Prices'}
    #     }
    #     return fig