import requests
import json

url = "http://127.0.0.1:5000/predict"

# Create dummy image (28x28 zeros)
pixels = [[0]*28 for _ in range(28)]

data = {"pixels": pixels}

response = requests.post(url, json=data)

print("Prediction:", response.json())
