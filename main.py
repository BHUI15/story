from flask import Flask, request, jsonify
import numpy as np 

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the prediction API!"

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status":"APP is running!"})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    x = data.get("x")
    y = 2*x + 1 # Dummy model for prediction
    return jsonify({"prediction": y})

# Add a GET/greet?name=YourName endpoint
@app.get('/greet')
def greet():
    name = request.args.get("name", default="Guest")
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)