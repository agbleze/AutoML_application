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
app = dash.Dash(__name__, external_stylesheets=[
                                                dbc.themes.SOLAR,
                                                dbc.icons.BOOTSTRAP,
                                                dbc.icons.FONT_AWESOME,
                                            ]
                )

app.layout = html.Div([
    dbc.Label("Select characteristics of online visitor to predict the number of booking days"),
    dbc.Row([dbc.Col(md=4,
                     children=[dcc.Dropdown(id='session',
                                                 placeholder='Number of sessions by site visitor',
                                                options=[
                                                    {'label': num_session, 'value': num_session}
                                                    for num_session in range(1,11)
                                                ]                       
                                            )
                      ]
                     ),
            dbc.Col(lg=4,
                    children=[dcc.Dropdown(id='city',
                                    placeholder='city from which client visited the platform',
                                   options=[{'label': city,
                                             'value': city
                                            }
                                            for city in df['city'].unique()
                                            ]      
                                   )
                      ]
                     ),
            dbc.Col(lg=4,     
                    children=[dcc.Dropdown(id='user_verified',
                                           placeholder='Is the visitor verified on platform',
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
                                            placeholder='type of device used to access platform',
                                            options=[{'label': device_class, 'value': device_class}
                                                     for device_class in df['device_class'].unique()
                                                     ]
                                            )
                               ]
                     ), 
             dbc.Col(lg=4,
                    children=[
                                dcc.Dropdown(id='instant_book',
                                                placeholder='Whether visitor used instant booking feature',
                                                options=[
                                                            {'label': instant_booking, 'value': instant_booking}
                                                            for instant_booking in df['instant_booking'].unique()
                                                        ]
                                            )
                                ]
                     ),
             dbc.Col([dbc.Button(id='submit_parameters', 
                                 children='Predict booking days'
                                 )
                      ]
                     )
             ]
            ),
    dbc.Row([
             ]
            )
])

##################### backend ##############################

def make_prediction_request():
    """_summary_
    
        TODO:
        1. Determine if button has been clicked
        2. If clicked, determine if values have been selected for all dropdown
            a. if all values are not selected provide pop-up indicating all values are to be provided
            b. If all values are provided, move to step 3
        3. Assign selected values to variables
        4. if selected value is string, filter data by selected values and take its equivalent encoded value ->
        5. Create list of all selected values and A
        6. create request with selected values as argments 
        7. send get request to API
        8. Receive response and retrieve the prediction returned
        9. Return prediction to dash output.
    """

app.run_server(port='4041', host='0.0.0.0', debug=False)

# %%
df['instant_booking'].unique()
# %%
