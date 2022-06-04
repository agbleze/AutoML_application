#%%
from dash import html, Input, Output, State, dcc
import dash
import dash_bootstrap_components as dbc
import pandas as pd
from sklearn.preprocessing import LabelEncoder

#%%
df = pd.read_csv(r'data/all_conversions_variables.csv')

le = LabelEncoder()

#%%
app = dash.Dash(__name__)

app.layout = html.Div([
    dbc.Label("Select characteristics of online visitor to predict the number of booking days"),
    dbc.Row([dbc.Col([dcc.Dropdown(placeholder='Number of sessions by site visitor',
                                   options=[
                                       {'label': num_session, 'value': num_session}
                                       for num_session in range(1,11)
                                       ]
                                   
        
                                   )
                      ]
                     ),
            dbc.Col([dcc.Dropdown(
                                    placeholder='city of vistor',
                                   options={'label': df['city'].unique(),
                                             'value': le.fit_transform(df['city'])
                                            }      
                                   )
                      ]
                     ),
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

app.run_server(port='4041', host='0.0.0.0', debug=False)

# %%
