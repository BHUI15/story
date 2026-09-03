import requests

print("Sending a request to the Flask app...")
response = requests.post('http://127.0.0.1:80/predict', json={'x': 10})
print(response.json())
# print("The prediction from the app is: ", response.json().get("prediction"))

response = requests.get('http://127.0.0.1:80/status')
print("Status check: ", response.status_code, response.json())