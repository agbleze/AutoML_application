#%%
from dash import html, Input, Output, State, dcc
import dash
import dash_bootstrap_components as dbc
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import requests
import json
from dash.exceptions import PreventUpdate
from helper_components import output_card, create_offcanvans

#%%
from ui_helper import request_prediction, create_encoded_data

#%%
from constant import HOST, PORT, ENDPOINT

URL = f'{HOST}:{PORT}{ENDPOINT}'

#%%
df = pd.read_csv(r'/Users/lin/Documents/python_venvs/tpot_homelike_env/machine_learning_api/data/all_conversions_variables.csv')


df = df[['num_sessions', 'city', 'country',
        'device_class', 'instant_booking',
        'user_verified', 'days'
        ]]


#%%
df = create_encoded_data(data=df, columns=['city',
                                            'country',
                                            'device_class',
                                            'instant_booking',
                                            'user_verified'
                                            ]
                          )



#%%
app = dash.Dash(__name__, external_stylesheets=[
                                                dbc.themes.SOLAR,
                                                dbc.icons.BOOTSTRAP,
                                                dbc.icons.FONT_AWESOME,
                                            ]
                )

app.layout = html.Div([

    dbc.Row([
        html.Br(), html.Br(),
        dbc.Col(dbc.Button('Project description',
                           id='proj_desc',
                           n_clicks=0
                           )
            ),
        dbc.Col(children=[
                            html.Div(
                                    children=[create_offcanvans(id='project_canvans',
                                                      title='BookingGauger',
                                                      is_open=False
                                                      )
                                              ]
                                ),
                          ]
                )
    ]),
    dbc.Label("Select characteristics of online visitor to predict the number of accommodation days to be booked"),
    html.Br(), html.Br(),
    dbc.Row([dbc.Col(md=4,
                     children=[dbc.Label('Number of session'),
                         dcc.Dropdown(id='session',
                                                 placeholder='Number of sessions by site visitor',
                                                options=[
                                                    {'label': num_session, 'value': num_session}
                                                    for num_session in range(1,11)
                                                ]
                                            )
                      ]
                     ),
            dbc.Col(lg=4,
                    children=[dbc.Label('City'),
                        dcc.Dropdown(id='city',
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
                    children=[
                        dbc.Label('User verification status'),
                        dcc.Dropdown(id='user_verified',
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
                     children=[
                         dbc.Label('Device type'),
                         dcc.Dropdown(id='device',
                                            placeholder='type of device used to access platform',
                                            options=[{'label': device_class, 'value': device_class}
                                                     for device_class in df['device_class'].unique()
                                                     ]
                                            )
                               ]
                     ),
             dbc.Col(lg=4,
                    children=[
                        dbc.Label('Instant booking feature used?'),
                                dcc.Dropdown(id='instant_book',
                                                placeholder='Whether visitor used instant booking feature',
                                                options=[
                                                            {'label': instant_booking, 'value': instant_booking}
                                                            for instant_booking in df['instant_booking'].unique()
                                                        ]
                                            )
                                ]
                     ),
             dbc.Col([
                 #html.Br(),
                 dbc.Label(''),
                 dbc.Button(id='submit_parameters',
                                 children='Predict booking days'
                                 )
                      ]
                     )
             ]
            ),
    html.Br(), html.Br(),
    dbc.Row([dbc.Col(id='prediction',
                     children=[
                         html.Div(id="prediction_div",
                                  children=[output_card(id="prediction_output",
                                                        card_label="Prediction"
                                                        )
                                            ]
                                  )
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

@app.callback(Output(component_id='project_canvans', component_property='is_open'),
              Input(component_id='proj_desc', component_property='n_clicks'),
              State(component_id='project_canvans', component_property='is_open')
              )
def toggle_project_description(proj_desc_button_clicked, is_open):
    if proj_desc_button_clicked:
        return not is_open
    else:
        return is_open



@app.callback(Output(component_id='desc_popup', component_property='children'),
              Output(component_id='missing_para_popup', component_property='is_open'),
              Output(component_id='prediction_output', component_property='children'),
              Input(component_id='submit_parameters', component_property='n_clicks'),
              Input(component_id='session', component_property='value'),
              Input(component_id='city', component_property='value'),
              Input(component_id='user_verified', component_property='value'),
              Input(component_id='device', component_property='value'),
              Input(component_id='instant_book', component_property='value'))

def make_prediction_request(submit_button, session, city_selected, user_verified_selected,
                            device_selected, instant_booking_selected):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'submit_parameters':
        if ((not session) or (not city_selected) or (not user_verified_selected)
            or (not device_selected) or (not instant_booking_selected)):
            message = ('All parameters must be provided. Please select the \
                       right values for all parameters from the dropdown. \
                        Then, click on predict booking days button to know \
                        the number of accommodation days a customer will book'
                       )
            return message, True, dash.no_update
        else:
            city_encoded = df[df['city']==city_selected]['city_encoded'].unique().tolist()[0]
            country_encoded = df[df['city']==city_selected]['country_encoded'].unique().tolist()[0]
            user_verified_encoded = df[df['user_verified']==user_verified_selected]['user_verified_encoded'].unique().tolist()[0]
            device_class_encoded = df[df['device_class']==device_selected]['device_class_encoded'].unique().tolist()[0]
            instant_booking_encoded = df[df['instant_booking']==instant_booking_selected]['instant_booking_encoded'].unique().tolist()[0]

            in_data = {'num_sessions': session,
                    'city_encoded': city_encoded,
                    'country_encoded': country_encoded,
                    'device_class_encoded': device_class_encoded,
                    'instant_booking_encoded': instant_booking_encoded,
                    'user_verified_encoded': user_verified_encoded
                    }

            prediction = request_prediction(URL=URL,
                                            data=in_data
                                        )

            if prediction > 1:
                return dash.no_update, False,  f'{round(prediction)} day(s)'
            else:
                return dash.no_update, False, f'{round(prediction)} day'


app.run_server(port='4048', host='0.0.0.0', debug=True, use_reloader=False)
