from argparse import Namespace



args = Namespace(categorical_features = ['device_class', 'city', 'country', 
                                         'instant_booking', 'user_verified'
                                        ],
                numeric_features = ['num_sessions'],
                features = ['num_sessions', 'device_class', 'city', 'country', 
                                         'instant_booking', 'user_verified'
                                        ],
                target_variable = 'days',
                data_foldername = 'booking_gauger_tpoter/data',
                data_filename = 'all_conversions_variables.csv'
                )
