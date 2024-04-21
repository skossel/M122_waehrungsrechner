import requests
import json


api_url = 'https://api.api-ninjas.com/v1/convertcurrency?want=CHF&have=GBP&amount=1000'
api_key = 'qTRfOwwc/jXet0zOlGIGvg==f47WreTpyZOG1nM4'

def getDataOfApiRequest():
    response = requests.get(api_url, headers={'X-Api-Key': api_key})

    if response.status_code == requests.codes.ok:
        data = response.json()
        print("JSON mit akutellen Daten wurde erfolgreich ausgelesen")
        return data

    else:
        print("Fehler:", response.status_code, response.text)

