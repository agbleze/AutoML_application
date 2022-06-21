#%%
import requests
import json
from typing import List
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def request_prediction(URL: str, data: dict) -> int:
    """
    This function accepts

    Parameters
    ----------
    URL : str
        The API link.
    data : dict
        input data to be used for prediction.

    Returns
    -------
    int
        prediction.

    """
    req = requests.post(url=URL, json=data)
    response = req.content
    prediction = json.loads(response)['predicted_value'][0]
    return prediction


# %%
def create_encoded_data(data: pd.DataFrame, columns: List = None) -> pd.DataFrame:
    """
    This function accepts data in the dataframe format and optional columns parameter
    and returns a dataframe with variables encoded. When no columns are specified,
    all columns are encoded and when columns are provided all those columns are
    encoded.

    Parameters
    ----------
    data : pd.DataFrame
        Input data.
    columns : List, optional
        List of column names which are essential categorical variables in the data to encode. The default is None.

    Returns
    -------
    data : DataFrame
        A dataframe that included the encoded columns.

    """
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






