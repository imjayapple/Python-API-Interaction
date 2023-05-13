import requests

def get_weather(city_name):
    api_key = "your_openweathermap_api_key"
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Use the 'params' parameter to add the API key and city name to the request

    response = requests.get(base_url, params={
        'q': city_name,
        'appid': api_key
    })

    data = response.json()