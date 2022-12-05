from dash import dcc, html
import dash_bootstrap_components as dbc
from style import cardbody_style, card_icon, cardimg_style, card_style
import os


def output_card(id: str = None, card_label: str =None,
                style={"backgroundColor": 'yellow'},
                icon: str ='bi bi-cash-coin', card_size: int = 4):
    return dbc.Col(lg=card_size,
                    children=dbc.CardGroup(
                        children=[
                            dbc.Card(
                                    children=[
                                        html.H3(id=id),
                                        html.P(card_label)
                                    ]
                                ),
                            dbc.Card(
                                    children=[
                                        html.Div(
                                            className=icon,
                                            style=card_icon
                                        )
                                    ],
                                    style=style
                            )
                        ]
                    )
                )


def create_offcanvans(id: str, title: str, is_open=False):
    return html.Div(
        [
            dbc.Offcanvas(
                id=id,
                title=title,
                is_open=is_open,
                children=[
                    dcc.Markdown('''
                                    #### Project description

                                    The aim of this project is to predict the number of days that
                                    customers are likely to book an accommodation for based on user bahaviour.
                                    The client is an accommodation provider who sought to obtain
                                    an intelligent tool that can enable the prediction of booking days
                                    based on a number of features.

                                    #### Features / variables used

                                    The dataset had a number of variables used as predictors for
                                    predicting number of accommodations booked as the target variable.
                                    These includes the following;

                                    ##### Predictor variables
                                    __Number of sessions__ : This describes the number of sessions a customer made
                                    on the booking site.

                                    __City__ : This is the city from which a customer is accessing the booking site from

                                    __Country__ : This is the country from which the user is accessing the booking site.
                                    During the selection of various variables, you do not have the burden to decide this
                                    as reference is automatically made from the city selected.

                                    __Device Class__ : This is the type of device used to access the booking site. It has
                                    the values desktop, phone or tablet

                                    __Instant Booking__ : The is a feature on a booking site. Whether or not this
                                    feature was used by a customer is included in predicting the number of day to
                                    be booked

                                    __User Verification Status__ : Whether or not a customer who visited the site
                                    has been verified is included in predicting number of days to be booked.

                                    ##### Target variable
                                    __ Number of accommodation days to be booked__


                                    #### Tools and method used
                                    Automated machine learning (AutoML) was employed to deliver a high
                                    accuracy optimized prediction model. The model is used to create
                                    an API that receives request, makes and send prediction as response
                                    to this web application.

                                    With the user interface provided here, various features describing customers
                                    behaviours and attributes can be selected to make a prediction.

                                    Among others, the tools used included the following

                                    * TPOT as an AutoML package to develop the machine learning model
                                    * Dash to build this web application as the User Interface
                                    * Flask to develop the API for the machine learning model


                                    #### Project output

                                    The main output of this project were the following

                                    * Machine learning API deployed
                                    * Machine learning web application



                                '''
                                )
                    ]
            ),
        ]
    )



def get_data_path(folder_name, file_name):
    cwd = os.getcwd()
    return f"{cwd}/{folder_name}/{file_name}"

