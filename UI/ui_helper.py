#%%
import requests
import json

def request_prediction(URL: str, data: dict) -> int:
    req = requests.post(url=URL, json=data)
    response = req.content
    prediction = json.loads(response)['predicted_value'][0]
    return prediction
# %%
