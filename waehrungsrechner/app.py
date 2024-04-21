from flask import Flask, render_template
import request
import os
import sys
import time


import requests
import json

app = Flask(__name__)


def restartprogram():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def main():
    # Hauptteil Ihres Programms hier einfügen
    print("Das Programm wird in einer Stunde neu gestartet.")

    # Verzögerung von einer Stunde
    time.sleep(10)

    # Nach einer Stunde das Programm neu starten
    restartprogram()

@app.route('/')
def index():
    data = request.getDataOfApiRequest()
    print(data)
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run()
    main()




from flask_apscheduler import APScheduler
app = Flask(__name__)
scheduler = APScheduler()

# Konfiguriere den Scheduler
scheduler.api_enabled = True
scheduler.init_app(app)

# Starte den Scheduler
scheduler.start()


def hourly_job():
    with app.app_context():
        index()


# Füge den Job zum Scheduler hinzu
scheduler.add_job(id='hourly_job', func=hourly_job, trigger='interval', seconds=5)

if __name__ == '__main__':
    app.run()









