#%%
from dash import html, Input, Output, State, dcc
import dash
import dash_bootstrap_components as dbc
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import requests
import json

#%%
HOST ='http://ec2-18-220-113-224.us-east-2.compute.amazonaws.com'
PORT = '8000'
ENDPOINT = '/predict'

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
    dbc.Row([dbc.Col(id='prediction',
                     children=[
                         html.Div(id="prediction_output")
                     ]
                     ),
             dbc.Col([
                 dbc.Modal(id='missing_para_popup', is_open=False,
                     children=[
                     dbc.ModalBody(id='desc_popup')
                 ])
             ]
                     )
             ]
            )
])

##################### backend ##############################
@app.callback(Output(component_id='desc_popup', component_property='children'),
              Output(component_id='missing_para_popup', component_property='is_open'),
              Output(component_id='prediction_output', component_property='children'),
              Input(component_id='session', component_property='value'),
              Input(component_id='city', component_property='value'),
              Input(component_id='user_verified', component_property='value'),
              Input(component_id='device', component_property='value'),
              Input(component_id='instant_booking', component_property='value'))

def make_prediction_request(session, city_selected, user_verified_selected, 
                            device_selected, instant_booking_selected):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if button_id == 'submit_parameters':
        if ((not session) and (not city_selected) and (not user_verified_selected) 
            and (not device_selected) and (not instant_booking)):
            message = 'All parameters must be provided. Please select the right values for all parameters from the dropdown'
            return message, True, dash.no_update
    else:
        city_encoded = df[df['city']==city_selected]['city_encoded'].item()
        country_encoded = df[df['city']==city_selected]['country_encoded'].item()
        user_verified_encoded = df[df['user_verified']==user_verified_selected]['user_verified_encoded'].item()
        device_class_encoded = df[df['device_class']==device_selected]['device_class_encoded'].item()
        instant_booking_encoded = df[df['instant_booking']==instant_booking_selected]['instant_booking_encoded'].item()
        
        in_data = {'num_sessions': session, 
                   'city_encoded': city_encoded,
                   'country_encoded': country_encoded, 
                   'device_class_encode': device_class_encoded,
                   'instant_booking_encoded': instant_booking_encoded,
                   'user_verified_encoded': user_verified_encoded
                   }
        URL = f'{HOST}:{PORT}{ENDPOINT}'
        reqs = requests.post(url=URL, json=in_data)
        response = reqs.content
        response_json = json.loads(response)
        prediction = response_json['predicted_value']
        
        return dash.no_update, False, prediction
 
            
            # create pop-up indicating that all parameters needs to provided
            
        
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
        7. send post request to API
        8. Receive response and retrieve the prediction returned
        9. Return prediction to dash output.
    """

app.run_server(port='4041', host='0.0.0.0', debug=False)

# %%
df['user_verified']
# %%
df.columns
# %%
