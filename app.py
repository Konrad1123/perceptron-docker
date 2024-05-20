from flask import Flask

# Create a Flask app
app = Flask(__name__)

# Create an API end point
@app.route('/')
def say_hello():
    return "Hello World"

if __name__ == '__main__':
    app.run()  # Defaults to localhost and port 5000
    # app.run(host='0.0.0.0', port=8000)

