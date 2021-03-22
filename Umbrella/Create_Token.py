import requests
import json


def request_Token(APISettings):
    """Starts a connection to the Umbrella API to create a new token, this token will be used to establish a
a connection to any of the other Umbrella APIs
Return: Session token"""
    URL = "https://management.api.umbrella.com/auth/v2/oauth2/token"
    headers = {"Accept":"application/json"}
    Key = APISettings.key
    Secret = APISettings.secret
    params = {"grant_type":"client_credentials"}
    response = requests.request("POST", URL, headers=headers, auth=(Key,Secret),params=params)
    token_json = response.json()
    token_value = token_json['access_token']
    return token_value


    

