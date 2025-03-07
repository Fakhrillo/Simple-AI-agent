from environs import Env
env = Env()
env.read_env()

OPENWEATHER_TOKEN = env("TOKEN")

import requests

def get_weather(location: str)-> str:
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = { "q": location, "appid": OPENWEATHER_TOKEN, "units": "metric" }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        
        data = response.json()
        return f"Weather in {data['name']} Temperature: {data['main']['temp']}°C (Feels like {data['main']['feels_like']}°C)\n Humidity: {data['main']['humidity']}%\n Wind Speed: {data['wind']['speed']} m/s\n Condition: {data['weather'][0]['description'].capitalize()}"

    except requests.exceptions.RequestException as e:
        return f"error: {e}"
    