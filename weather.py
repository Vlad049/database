import os

import requests
from dotenv import load_dotenv


load_dotenv()


API_KEY = os.getenv("WEATHER_API")


def get_weather(city: str = "Kyiv"):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    responce = requests.get(url).json()

    current_weather = {
    "city": city,
    "temp": responce.get("current", {}).get("temp_c"),
    "text": responce.get("current", {}).get("condition", {}).get("text"),
    "icon": responce.get("current", {}).get("condition", {}).get("icon")
    }

    return current_weather
