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

# Humidty gathering + windspeed & pressure
humidity = data["current"]["humidity"]
wind_speed = data["current"]["wind_speed"]
pressure = data["current"]["pressure"]

print(f"Humidity: {humidity}%")
print(f"Wind Speed: {wind_speed} m/s")
print(f"Atmospheric Pressure: {pressure} hPa")

# Error handling

# Make the API request
response = requests.get(endpoint, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    # Extract and display weather data
else:
    print("An error occurred. Please try again later.")
