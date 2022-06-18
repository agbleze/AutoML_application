from dash import dcc, html
import dash_bootstrap_components as dbc
from style import cardbody_style, card_icon, cardimg_style, card_style



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

                                    ### BookingGauger

                                    #### Project description

                                    The aim of this project is to predict the number of days that
                                    a website visitor is likely to book based on a number of features.
                                    The client is an accommodation provider who sought to obtain
                                    an intelligent tool that can enable the prediction of booking days
                                    based on a number of features.

                                    #### Tools and method used
                                    Automated machine learning (AutoML) was employed to deliver a high
                                    accuracy optimized prediction model. The model is used to create
                                    an API that receives requests, makes and send prediction as response
                                    to this platform.

                                    With the user interface provided here, various features can be selected as
                                    input for the prediction

                                    Among others the tools used included the following
                                    * TPOT as the AutoML package to develop the machine learning model
                                    * Dash to build this web application as the User Interface
                                    * Flask to develop the API for the machine learning model


                                    #### Project output

                                    The main output of this project were the following

                                    * Machine learning API deployed
                                    * Machine learning web application

                                    Features
                                    The features used for the analysis are as follows;


                                    with the following
                                    pain point

                                '''
                                )
                    ]
            ),
        ]
    )
