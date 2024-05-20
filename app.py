from flask import Flask, request, jsonify
import numpy as np
from sklearn.linear_model import Perceptron

app = Flask(__name__)
model = Perceptron()

@app.route('/train', methods=['POST'])
def train():
    data = request.json
    X = np.array(data['X'])
    y = np.array(data['y'])
    model.fit(X, y)
    return jsonify({"message": "Model trained!"})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    X = np.array(data['X'])
    predictions = model.predict(X)
    return jsonify({"predictions": predictions.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
