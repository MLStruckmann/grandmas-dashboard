#######
# Objective: build a dashboard that displays investment data
# in line charts and maps
######

# Perform imports here:
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import subpages

# Launch the application:
app = dash.Dash()

# Create a Dash layout that contains a Graph component:
app.layout = html.Div([
    html.H1('Investment Dashboard',
        style={'display':'inline-block', 'verticalAlign':'top', 'width':'30%'}),
    html.H1('Created by Magnus Struckmann',
        style={'display':'inline-block', 'verticalAlign':'top','float': 'right'}),
    html.Div([
        dcc.Tabs(id='invest-tabs', value='stocks', children=[
            dcc.Tab(label='Stocks', value='stocks'),
            dcc.Tab(label='Real Estate', value='realestate'),
            dcc.Tab(label='Commodities', value='commodities'),
            dcc.Tab(label='Bonds', value='bonds'),
            dcc.Tab(label='Cryptocurrencies', value='cryptocurrencies'),
            dcc.Tab(label='Compare', value='compare')
        ]),
        html.Div(id='tabs-content'),
    ])
])

# Create callback for tabs
@app.callback(Output('tabs-content', 'children'),
              [Input('invest-tabs', 'value')])
def render_content(tab):
    if tab == 'stocks':
        return subpages.stocks()
    elif tab == 'realestate':
        return subpages.realestate()
    elif tab == 'commodities':
        return subpages.commodities()
    elif tab == 'bonds':
        return subpages.bonds()
    elif tab == 'cryptocurrencies':
        return subpages.cryptocurrencies()        
    elif tab == 'compare':
        return subpages.compare()

# Add the server clause:
if __name__ == '__main__':
    app.run_server()