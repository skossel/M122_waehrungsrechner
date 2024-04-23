import requests
from config import API_URL, API_KEY

def getDataOfApiRequest():
    response = requests.get(API_URL, headers={'X-Api-Key': API_KEY})

    if response.status_code == requests.codes.ok:
        data = response.json()
        print("JSON mit akutellen Daten wurde erfolgreich ausgelesen")
        return data

    else:
        print("Fehler:", response.status_code, response.text)

