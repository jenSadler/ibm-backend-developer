"""Flask sample app"""
from flask import Flask, jsonify
from flask_cors import CORS # Enable CORS for cross-origin requests

app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=["GET"])
def get_data():
    """Default get data method"""
    data = {"message":"Hello from Flask"}
    return jsonify(data)

@app.route('/api/greeting', methods=["GET"])
def greet():
    """Greeting method"""
    greeting = {"hello":"Hello World!"}
    return jsonify(greeting)

if __name__ == '__main__':
    app.run(debug=True)
