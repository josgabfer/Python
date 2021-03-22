from Connection_Settings import connectionSettings
from Connection_Settings import connectionSettingsEncoder
from os import path
import os.path
import json

def writeDBPath(path):
    settings = {}
    settings['Global'] = []
    settings['Global'].append({
        'DBPath': path
    })
    filename = 'settings.json'
    try: 
        with open(filename,'w') as outfile:
            json.dump(settings, outfile)
            print('Settings succesfully updated')
    except FileNotFoundError:
        print(f'Sorry, {outfile} can\'t be created')

def readDBPathSettingsJason():
    with open('settings.json', 'r') as readfile:
        jsonData = json.load(readfile.read())
        for setting in jsonData['Global']:
            if setting['DBPath'] == '':
                print('Default settings')
            else:
                print(f'DB path is:' + setting['DBPath'])



