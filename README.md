# Perceptron Docker

This project provides a Dockerized implementation of a Perceptron model using Flask for serving predictions.

## Prerequisites

- Docker installed on your machine.

## Building the Docker Image

To build the Docker image, run the following command:

```bash
docker build -t perceptron-docker .

Running the Docker Container

To run the Docker container, use the following command:

docker run -p 5001:5000 perceptron-docker

File Structure

Dockerfile: Dockerfile containing instructions to build the image.
requirements.txt: File listing the Python dependencies.
app.py: Main application script containing the model training and prediction logic.

Model Training

The model is trained automatically when the container starts. The trained model is saved as model.pkl.

Endpoint

/predict: POST endpoint that accepts a JSON payload with data for predictions and returns the model's predictions.
Author

Konrad Wira

License

This project is licensed under the MIT License - see the LICENSE file for details.

```bash
git add README.md
git commit -m "Add README.md with instructions"
git push origin main
