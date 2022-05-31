import joblib
#%%

def predict_booking(model, X):
    if type(X) is not list:
        raise Exception('X must be a list')
    if len(X) != 7:
        raise Exception('X must contain 7 values for \
                        num_sessions, city, country, device, test_status \
                        instant booking, user verified'
                        )
    prediction = model.predict([X])
    return prediction
# %%
predict_booking(model=joblib.load('/Users/lin/Documents/python_venvs/tpot_homelike_env/api/model/booking_model.model'),
                X=[2, 4, 2, 9, 3, 7, 8]
                )






# %%
