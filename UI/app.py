#%%
from dash import html, Input, Output, State, dcc
import dash_bootstrap_components as dbc


app = dash.Dash(__name__)

app.layout = html.Div([
    dbc.Label("Select characteristics of online visitor to predict the number of booking days"),
    dbc.Row([dbc.Col([dcc.Dropdown(placeholder='Number of sessions by site visitor',
                                   options={'label': x, 'value': [x for x in range(1,10)]}
                                   )
                      ]
                     ),
            dbc.Col(),
            dbc.Col()
            ]
            ),
    html.Br(), html.Br(),
    
    dbc.Row([dbc.Col(), dbc.Col(), dbc.Col()
             ]
            ),
    dbc.Row([dbc.Button(),
             ])
])
