#%%
import requests
import json
from typing import List
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pandas as pd

def request_prediction(URL: str, data: dict) -> int:
    req = requests.post(url=URL, json=data)
    response = req.content
    prediction = json.loads(response)['predicted_value'][0]
    return prediction


# %%
def create_encoded_data(data: pd.DataFrame, columns: List = None) -> pd.DataFrame:
    le = LabelEncoder()
    if columns == None:
        columns = data.columns
        for column in columns:
            data[f'{column}_encoded'] = le.fit_transform(data[column])
        return data
    else:
        if isinstance(columns, str):
            columns = [columns]
            for column in columns:
                data[f'{column}_encoded'] = le.fit_transform(data[column])
            return data
        else:
            for column in columns:
                data[f'{column}_encoded'] = le.fit_transform(data[column])
            return data






