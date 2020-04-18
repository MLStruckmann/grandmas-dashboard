#######
# Objective: build a dashboard that displays investment data
# in line charts and maps
######

# Perform imports here:
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

# Launch the application:
app = dash.Dash()

# Create a Dash layout that contains a Graph component:
app.layout = html.Div([
    html.H1('Stock Dashboard',style={'display':'inline-block', 'verticalAlign':'top', 'width':'30%'})
])

# Add the server clause:
if __name__ == '__main__':
    app.run_server()