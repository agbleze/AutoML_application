#%%
import joblib
import json

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
