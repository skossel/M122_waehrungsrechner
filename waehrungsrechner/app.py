import threading
import time
from flask import Flask, render_template

from waehrungsrechner.request import getDataOfApiRequest

app = Flask(__name__)

def api_request_thread():
    while True:
        data = getDataOfApiRequest()
        print(data)
        time.sleep(2)

@app.route('/')
def index():
    data = getDataOfApiRequest()
    return render_template('index.html', data=data)


if __name__ == '__main__':
    thread = threading.Thread(target=api_request_thread)
    thread.start()
    app.run()
