import requests

#Example for report activity
#Requires Bearer token created from Management

def ReportActivity(token):

    URL = "https://reports.api.umbrella.com/v2/organizations/5326538/activity/dns"

    headers = {"Accept":"application/json",
                "Authorization": 'Bearer {token}'}

    params = {"from":"-1days",
                "to":"now",
                "limit":10}

    response = requests.request("GET", URL, headers=headers,params=params)

    print(response.text)
