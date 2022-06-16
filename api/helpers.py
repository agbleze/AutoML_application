#%%
import joblib

#%%
model = joblib.load('new_model.model')
#%%

def predict_booking(model, X):
    if type(X) is not list:
        raise Exception('X must be a list')
    if len(X) != 6:
        raise Exception('X must contain 6 values for \
                        num_sessions, city, country, device, \
                        instant booking, user verified'
                        )
    prediction = model.predict([X])
    return prediction.tolist()
# %%
# predict_booking(model=model,
#                 X=[[2, 4, 2, 9, 3, 7]]
#                 )


# # %%
# import requests
# # %%
# URL = "http://127.0.0.1:8000/predict"

# #in_data = {}

# in_data = {
#  'num_sessions': 2,
#  'city_encoded': 3,
#  'country_encoded': 3,
#  'device_class_encoded': 2,
#  'instant_booking_encoded': 1,
#  'user_verified_encoded': 1 
# }
# req = requests.post(url=URL, json=in_data)

# #%%
# req
# num_sessions = user_input['num_sessions']
#         city = user_input['city_encoded']
#         country = user_input['country_encoded']
#         device = user_input['device_class_encoded']
#         instant_booking = user_input['instant_booking_encoded']
#         user_verified = user_input['user_verified_encoded']


# %%
