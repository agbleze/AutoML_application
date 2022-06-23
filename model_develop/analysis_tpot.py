#%%
from tpot import TPOTRegressor
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score,mean_squared_error
import numpy as np
import joblib

#%% import data set
df = pd.read_csv(r'data/all_conversions_variables.csv')
# %% create instance of label encoder
le = LabelEncoder()

#%%
df['city_encoded'] = le.fit_transform(df.city)
df['country_encoded'] = le.fit_transform(df.country)
df['device_class_encoded'] = le.fit_transform(df.device_class)
df['instant_booking_encoded'] = le.fit_transform(df.instant_booking)
df['user_verified_encoded'] = le.fit_transform(df.user_verified)

# %% CREATE TARGET AND PREDICTOR variables 
########### Predicting the number of days an online visitor will book accommodation for.
# target variable
y = df['days']

# predictor variables
X = df[['num_sessions', 'city_encoded', 'country_encoded', 
        'device_class_encoded', 
        'instant_booking_encoded', 'user_verified_encoded'
        ]]
# %% split data into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# %% create optimizer_pipeline
optimizer_pipeline = TPOTRegressor(max_time_mins=10, 
                                   verbosity=2, random_state=0
)

# %%
optimizer_pipeline.fit(features=X_train, target=y_train)

# %%
optimizer_pipeline.score(X_test, y_test)

# %%
fitted_pipeline = optimizer_pipeline.fitted_pipeline_

# %%
evaluated_models = optimizer_pipeline.evaluated_individuals_
# %%
optimizer_pipeline.predict(X_test)

# %% check score on training dataset -- No overfitting because test error is lower
optimizer_pipeline.score(X_train, y_train)

# %%
rmse = lambda y, y_hat: np.sqrt(mean_squared_error(y, y_hat))

# %%
y_pred = optimizer_pipeline.predict(X_test)

# %% only 27% of the data is explained by the predictors
r2_score(y_test, y_pred)

# %%
mean_squared_error(y_test, y_pred)
# %% the model makes a prediction with an average error of 68 days
rmse(y_test, y_pred)

# %% export model pipeline fitted
joblib.dump(value=fitted_pipeline, filename='new_model.model')
# %% load the model pipeline fitted and make prediction
loaded_model = joblib.load(filename='new_model.model')

loaded_model.predict([[2, 4, 2, 9, 3, 7]])

