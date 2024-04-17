import requests
import json

import schedule

api_url = 'https://api.api-ninjas.com/v1/convertcurrency?want=EUR&have=USD&amount=5000'
api_key = 'qTRfOwwc/jXet0zOlGIGvg==f47WreTpyZOG1nM4'

response = requests.get(api_url, headers={'X-Api-Key': api_key})

if response.status_code == requests.codes.ok:
    data = response.json()

    # Speichere die JSON-Antwort in einer Datei
    with open('currency_conversion.json', 'w') as file:
        json.dump(data, file, indent=4)

    print("Die Währungsumrechnung wurde erfolgreich in der Datei 'currency_conversion.json' gespeichert.")
else:
    print("Fehler:", response.status_code, response.text)

