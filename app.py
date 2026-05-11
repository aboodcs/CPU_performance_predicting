from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from src.datascience.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')


import sys

@app.route('/train', methods=['GET'])  
def training():
    os.system(f"{sys.executable} main.py")
    return "Training Successful"


@app.route('/predict', methods=['POST', 'GET'])  
def index():
    if request.method == 'POST':
        try:
            MYCT  = float(request.form['MYCT'])
            MMIN  = float(request.form['MMIN'])
            MMAX  = float(request.form['MMAX'])
            CACH  = float(request.form['CACH'])
            CHMIN = float(request.form['CHMIN'])
            CHMAX = float(request.form['CHMAX'])

            data = [MYCT, MMIN, MMAX, CACH, CHMIN, CHMAX]

            data = np.array(data).reshape(1, -1)

            obj = PredictionPipeline()
            prediction = obj.predict(data)

            return render_template(
                'results.html',
                prediction=round(float(prediction[0]), 1),
                MYCT=MYCT,
                MMIN=MMIN,
                MMAX=MMAX,
                CACH=CACH,
                CHMIN=CHMIN,
                CHMAX=CHMAX
            )

        except Exception as e:
            print(f"[ERROR] Prediction failed: {e}")
            return render_template('index.html', error=str(e))

    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)