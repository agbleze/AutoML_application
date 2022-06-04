#%%
from dash import html, Input, Output, State, dcc
import dash
import dash_bootstrap_components as dbc
import pandas as pd
from sklearn.preprocessing import LabelEncoder

#%%
df = pd.read_csv(r'data/all_conversions_variables.csv')

df = df[['num_sessions', 'city', 'country', 
        'device_class', 'instant_booking', 
        'user_verified', 'days'
        ]]

le = LabelEncoder()
# %%
df['city_encoded'] = le.fit_transform(df.city)
df['country_encoded'] = le.fit_transform(df.country)
df['device_class_encoded'] = le.fit_transform(df.device_class)
df['instant_booking_encoded'] = le.fit_transform(df.instant_booking)
df['user_verified_encoded'] = le.fit_transform(df.user_verified)

#%% 
#aindex = df[df['city']=='Kaiserslautern']['city_encoded']#.reset_index()#.reindex([0])
avale = df[df['city']=='Kaiserslautern']['city_encoded'].item()#.unique().item(#[aindex]

bvale = df[df['city']=='Kaiserslautern']['country_encoded'].item()#.unique()
print([avale,bvale])
#%%
df[df['city']=='Kaiserslautern']['city_encoded'][11]


#[avale, bvale]
#%%
app = dash.Dash(__name__)

app.layout = html.Div([
    dbc.Label("Select characteristics of online visitor to predict the number of booking days"),
    dbc.Row([dbc.Col(lg=4,children=[dcc.Dropdown(placeholder='Number of sessions by site visitor',
                                   options=[
                                       {'label': num_session, 'value': num_session}
                                       for num_session in range(1,11)
                                       ]
                                   
        
                                   )
                      ]
                     ),
            dbc.Col(lg=4,children=[dcc.Dropdown(
                                    placeholder='city of vistor',
                                   options=[{'label': city,
                                             'value': city
                                            }
                                            for city in df['city'].unique()
                                            ]      
                                   )
                      ]
                     ),
            dbc.Col(lg=4,
                    placeholder='Is the visitor verified on platform',
                    children=[dcc.Dropdown(id='user_verified',
                                                options=[{'label': user_verified, 'value': user_verified}
                                                         for user_verified in df['user_verified'].unique()
                                                         ]
                                                )
                                   ]
                    )
            ]
            ),
    html.Br(), html.Br(),
    
    dbc.Row([dbc.Col(lg=4,
                     children=[dcc.Dropdown(id='device',
                                            placeholder='type of device used on platform',
                                            options=[{'label': device_class, 'value': device_class}
                                                     for device_class in df['device_class'].unique()
                                                     ]
                                            )
                               ]
                     ), 
             dbc.Col(lg=4,
                     children=[dcc.Dropdown(
                                            children=[dcc.Dropdown(id='instant_book',
                                                                   options=[{'label': instant_booking, 'value': instant_booking}
                                                                            for instant_booking in df['instant_booking'].unique()
                                                                            ]
                                                                   )
                                                      ]
                                            )
                               ]
                     ), dbc.Col()
             ]
            ),
    dbc.Row([dbc.Button(),
             ])
])

app.run_server(port='4041', host='0.0.0.0', debug=False)

# %%