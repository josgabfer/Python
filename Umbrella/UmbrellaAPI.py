import argparse
from Connection_Settings import connectionSettings
from IO import writeDBPath, readDBPathSettingsJason
from Create_Token import request_Token
from Model import saveConnectionSettings, openConnectionSettings, saveConnectionSettingsPath
from datetime import datetime




parser = argparse.ArgumentParser(description='Umbrella API logging interface')
group = parser.add_argument_group('setup')
parser.add_argument('-o','--oid', dest='orgid', metavar='',type=str, help='oid is the organization ID, this value can be found in your umbrella dashboard URL')
parser.add_argument('-k','--key', dest='key',metavar='', type=str, help='This value is the key created from your Umbrella Dashboard')
parser.add_argument('-s','--secret', dest='secret', metavar='',type=str, help='This value stores the secret created from your Umbrella Dashboard')
parser.add_argument('-n','--name', dest='name', metavar='',type=str, help='This value represents the new credentials for the connection')
parser.add_argument('-p','--path', dest='path', metavar='',type=str, help='This value instructs the program where to save the Database in your OS, for example Windows: C:\\\\path\\\\to\\\\ ---- Unix/Mac: sqlite:////absolute/path/to/foo.db')
group = parser.add_mutually_exclusive_group()
group.add_argument('-S', '--setup', action='store_true', help='Setup the connection settings, it requires an orgainzation ID (-o), a key (-k) and a secret (-s)')
group.add_argument('-q', '--query', action='store_true', help='Query the Umbrella\'s API')
group.add_argument('-ct', '--createToken', action='store_true', help='Refresh API\'s Token')

args = parser.parse_args()

def setupConnectionSettings():
    """Calls the API reporting interface to create a token for further use.
        APISettings: Object, stores all the required arguments for a connection to the Umbrella API
        saveConnectionSettings: function in Model.py, this will save the settings in a DB (ConnectionSettings.db) to reuse the settings
    """
    if args.path:
        APISettings = connectionSettings(args.orgid, args.key, args.secret)
        APISettings.token = request_Token(APISettings)
        saveConnectionSettingsPath(APISettings, args.path)
        writeDBPath(args.path)
    else:
        APISettings = connectionSettings(args.orgid, args.key, args.secret)
        APISettings.token = request_Token(APISettings)
        saveConnectionSettings(APISettings)

    print(f'Connection settings succesfully created')

def printConnectionSettings():
    readDBPathSettingsJason()

def refreshToken():
    currentTime = datetime.now()
    print(currentTime.second)
   


def main():
    if args.setup:
        setupConnectionSettings()
    elif args.query:
        printConnectionSettings()
    elif args.createToken:
        refreshToken()       
    else:
        print('Either setup (-s) or query (-q) is required')

if __name__ =='__main__':
    main()
