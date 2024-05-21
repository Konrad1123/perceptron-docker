import numpy as np
from sklearn.linear_model import Perceptron
import joblib
from flask import Flask, request, jsonify

app = Flask(__name__)

# Trening modelu
def train_model():
    X = np.array([[0, 0], [1, 1], [1, 0], [0, 1]])
    y = np.array([0, 1, 1, 0])
    clf = Perceptron(tol=1e-3, random_state=0)
    clf.fit(X, y)
    joblib.dump(clf, 'model.pkl')
    print("Model trained and saved as model.pkl")

# Endpoint do przewidywań
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    X_new = np.array(data['data'])
    clf = joblib.load('model.pkl')
    predictions = clf.predict(X_new)
    return jsonify(predictions.tolist())

if __name__ == '__main__':
    train_model()
    app.run(host='0.0.0.0', port=5000)

