from argparse import Namespace



args = Namespace(categorical_features = ['device_class', 'city', 'country', 
                                         'instant_booking', 'user_verified'
                                        ],
                numeric_features = ['num_sessions']
                )
