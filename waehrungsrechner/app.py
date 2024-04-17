from flask import Flask, render_template
import json

app = Flask(__name__)

# Lade die JSON-Daten aus einer Datei

with open('currency_conversion.json', 'r') as file:
    data = json.loads(file.read())

@app.route('/')
def index():
    print(data)
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run()
