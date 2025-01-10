from flask import Flask
import pandas as pd
import numpy as np
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World! nice to meet you. good bye"

@app.route("/num")
def play():
    return "Let's Go"

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
