import requests

def get_weather(city_name):
    # Use your own key here
    api_key = "your_openweathermap_api_key"
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Use the 'params' parameter to add the API key and city name to the request

    response = requests.get(base_url, params={
        'q': city_name,
        'appid': api_key
    })

    data = response.json()

    # Extract the temperature, weather description from the data
    if data.get("main") is not None:
        main = data["main"]
        temperature = main["temp"]
        humidity = main["humidity"]

        weather_desc = data["weather"][0]["description"]

        return temperature, humidity, weather_desc
    else:
        return None

# Capture user input, city name, and weather variable to capture get_weather(city_name)

city_name = input("Enter city name : ")
temp_unit = input("Enter temperature unit (C/F) : ")

if temp_unit.lower() == 'f':
    temp_unit = 'imperial'
else:
    temp_unit = 'metric'

weather = get_weather(city_name, temp_unit)

if weather:
    print(f"Temperature : {weather[0]} {'' if temp_unit == 'metric' else '°F'}")
    print(f"Humidity : {weather[1]}%")
    print(f"Weather description : {weather[2]}")
else:
    print("City Not Found!")
