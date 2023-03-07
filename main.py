
#%%
from booking_gauger_tpoter.model.tpoter_pipeline import TpotModeler
from booking_gauger_tpoter.model.utils import get_path
from arguments import args
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import joblib

# %%
data_path = get_path(folder_name=args.data_foldername, 
                    file_name=args.data_filename
                    )

data = pd.read_csv(data_path)

cat_features = args.categorical_features
num_features = args.numeric_features


X = data[args.features]

y = data[args.target_variable]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3, random_state=2023)

tpot_mod = TpotModeler(training_features=X_train, training_target_variable=y_train,
                       testing_features=X_test, testing_target_variable=y_test
                    )


tpot_fitted_mod = tpot_mod.fit_models(max_time_mins=60, warm_start=True)

test_error = tpot_mod.evaluate_testset()

print(f'Test error is {test_error}')

#%%

days_predict = tpot_mod.predict_booked_days(device_class='desktop', city='Berlin', 
                                            country='DE', instant_booking='Not_instant', 
                                            user_verified='Verified', num_sessions=2
                                        )


print(days_predict)

#%%
rmse = lambda y, y_hat: np.sqrt(mean_squared_error(y, y_hat))


y_pred = tpot_fitted_mod.predict(X_test)


rmse(y=y_test, y_hat=y_pred)

#%% save the best model

tpot_mod.save_best_model()

#%%# load the saved model and use it for prediction
model_path = get_path(folder_name='model_store', file_name='best_model.model')

loaded_model = joblib.load(filename=model_path)


#%%

in_data = {'num_sessions': 2, 'city': 'Berlin', 'country': 'DE',
            'device_class': 'desktop', 'instant_booking': 'Not_instant',
            'user_verified': 'Verified'
            }
        
prediction_input_data = pd.DataFrame(data=in_data, index=[0])

loaded_model.predict(prediction_input_data)
