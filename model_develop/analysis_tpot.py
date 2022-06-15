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
# %%
df['city'].nunique()
pd.get_dummies(df.city)

le = LabelEncoder()
df['city_encoded'] = le.fit_transform(df.city)
# %%
df['country_encoded'] = le.fit_transform(df.country)
df['device_class_encoded'] = le.fit_transform(df.device_class)
#df['test_status_encoded'] = le.fit_transform(df.test_status)
df['instant_booking_encoded'] = le.fit_transform(df.instant_booking)
df['user_verified_encoded'] = le.fit_transform(df.user_verified)


#%%
for x in df.city:
        print(x)
le.fit_transform(df.city.unique())
# %%
df
# %% CREATE TARGET AND PREDICTORS 
########### Predicting the number of days an individual is will book accommodation for.
y = df['days']
X = df[['num_sessions', 'city_encoded', 'country_encoded', 
        'device_class_encoded', #'test_status_encoded', 
        'instant_booking_encoded', 'user_verified_encoded'
        ]]
# %%
df.columns
# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

y_train.shape
y_test.shape

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
fitted_pipeline
# %%
type(fitted_pipeline)

# %%
evaluated_models = optimizer_pipeline.evaluated_individuals_
# %%
optimizer_pipeline.predict(X_test)
# %%
y_test
# %% check score on training dataset -- No overfitting because it test error is lower
optimizer_pipeline.score(X_train, y_train)

# %%
optimizer_pipeline.export('/Users/lin/Documents/python_venvs/tpot_homelike_env/machine_learning_api/model_develop/optimized_model.py')

#%%
#optimizer_pipeline.export('/Users/lin/Documents/python_venvs/tpot_homelike_env/model_develop/gene100_model.py')
# %%
rmse = lambda y, y_hat: np.sqrt(mean_squared_error(y, y_hat))

# %%
y_pred = optimizer_pipeline.predict(X_test)

# %%
y_pred

# %% only 27% of the data is explained by the predictors
r2_score(y_test, y_pred)

# %%
mean_squared_error(y_test, y_pred)
# %% the model makes a prediction with an average error of 88 days
rmse(y_test, y_pred)

# %%
df.user_verified_encoded.value_counts()
df.instant_booking_encoded.value_counts()

#%%
X_train.shape

# %%
joblib.dump(value=fitted_pipeline, filename='new_model.model')
# %%
loaded_model = joblib.load(filename='new_model.model')

#%%

# %%
len(X_train.columns)
X_train.columns
# %% make prediction with model
loaded_model.predict([[2, 4, 2, 9, 3, 7]])





# %%
