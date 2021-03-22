import json
from json import JSONEncoder

class connectionSettings():
    """This class stores all the required settings to create a connection to the Umbrella API"""
    def __init__(self, orgid, key, secret, token='', name='',path=''):
        self.orgid = orgid
        self.key = key
        self.secret = secret
        self.token = token
        self.name = name
        self.path = path
        

   
    def __str__(self):
        return f"Orgid: {self.orgid}\nKey: {self.key}\nSecret: {self.secret}\nToken: {self.token}\nName: {self.name},\nPath: {self.path}"
class connectionSettingsEncoder(JSONEncoder):
    def default(self, APISettings):
        return APISettings.__dict__




    
