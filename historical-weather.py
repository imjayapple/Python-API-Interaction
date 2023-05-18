import requests
import datetime

# Convert the Unix timestamp to a more accessible format

timestamp = 1621228800
date = datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")

print(f"The weather data for New York City on {date}:")


# Set up the API endpoint and parameters
api_key = "your_openweathermap_api_key"
endpoint = "https://api.openweathermap.org/data/2.5/onecall/timemachine"
params = {
    "lat": 40.712776,
    "lon": -74.005974,
    "dt": 1621228800, # Unix timestamp for May 17, 2021
    "appid": api_key,
    "units": "metric"
}

# Make the API request
response = requests.get(endpoint, params=params)

# Parse the response data as JSON
data = response.json()

# Extract the temperature and weather description from the data
temperature = data["current"]["temp"]
weather_desc = data["current"]["weather"][0]["description"]

print(f"The temperature in New York City on May 17, 2021 was {temperature} degrees Celsius, and the weather was {weather_desc}.")