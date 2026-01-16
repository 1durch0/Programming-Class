import requests
import time
import json


url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 52.52,
    "longitude": 13.405,
    "hourly": "temperature_2m",
    "start": int(time.time()),
    "end": int(time.time()) + 3600,
    "timezone": "Europe/Berlin"
}

response = requests.get(url, params=params, timeout=10)


if response.status_code == 200:
    print("Success!")
    data = response.json()
elif response.status_code == 404:
    print("Resource not found")
elif response.status_code == 401:
    print("Authentication required")
else:
    print(f"Error: {response.status_code}")