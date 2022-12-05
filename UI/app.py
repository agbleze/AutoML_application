#%%
from dash import html, Input, Output, State, dcc
import dash
import dash_bootstrap_components as dbc
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import requests
import json
from dash.exceptions import PreventUpdate
from helper_components import output_card, create_offcanvans, get_data_path

#%%
from ui_helper import request_prediction, create_encoded_data

#%%
from constant import HOST, PORT, ENDPOINT

URL = f'{HOST}:{PORT}{ENDPOINT}'

#%%
data_path = get_data_path(folder_name='UI', file_name='data_used.csv')
data_used = pd.read_csv(data_path)

data_encoded = create_encoded_data(data=data_used, columns=['city',
                                                            'country',
                                                            'device_class',
                                                            'instant_booking',
                                                            'user_verified'
                                                            ]
                                   )

data_encoded
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
                                            for city in data_encoded['city'].unique()
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
                                                         for user_verified in data_encoded['user_verified'].unique()
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
                                                     for device_class in data_encoded['device_class'].unique()
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
                                                            for instant_booking in data_encoded['instant_booking'].unique()
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
def toggle_project_description(proj_desc_button_clicked: str, is_open: bool) -> bool:
    """
    This function accepts click event input and the state of canvas component,
    and change the state of the canvans component when a click occurs

    Parameters
    ----------
    proj_desc_button_clicked : str
        This parameter is a count of each click made on a button.
    is_open : bool
        Has the values True or False that specifies whether the canvas component is opened or not.

    Returns
    -------
    bool
        Has values True or False that determines whether the canvans component should be open.

    """
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

def make_prediction_request(submit_button: int, session: int, city_selected: str, user_verified_selected: str,
                            device_selected: str, instant_booking_selected: str):
    """
    This function accepts various input data selected, makes a request to a machine learning API
    and returns prediction

    Parameters
    ----------
    submit_button : int
        Number of times the submit button has been clicked.
    session : int
        This describes the number of sessions a customer made on the booking site..
    city_selected : str
        This is the city from which a customer is accessing the booking site from
    user_verified_selected : str
        Whether or not a customer who visited the site has been verified.
    device_selected : str
        This is the type of device used to access the booking site.
    instant_booking_selected : str
        The is a feature on a booking site and value is whether or not this feature was used by a customer.

    Returns
    -------
    desc_popup: str
        This is a message in a popup component that indicates corrections to be made before submitting API request.
    missing_para_popup: bool
        This is an output component that opens when selection is not made
        for all parameters before clicking submit buttion.
    prediction_output
        This is an output component where prediction is displayed.

    """
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
            city_encoded = data_encoded[data_encoded['city']==city_selected]['city_encoded'].unique().tolist()[0]
            country_encoded = data_encoded[data_encoded['city']==city_selected]['country_encoded'].unique().tolist()[0]
            user_verified_encoded = data_encoded[data_encoded['user_verified']==user_verified_selected]['user_verified_encoded'].unique().tolist()[0]
            device_class_encoded = data_encoded[data_encoded['device_class']==device_selected]['device_class_encoded'].unique().tolist()[0]
            instant_booking_encoded = data_encoded[data_encoded['instant_booking']==instant_booking_selected]['instant_booking_encoded'].unique().tolist()[0]

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


app.run_server(port='4048', host='0.0.0.0', debug=False, use_reloader=False)
