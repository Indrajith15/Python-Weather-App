import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
city = input("Enter city name: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url)
# print(response)
data = response.json()
if response.status_code != 200:
    print(f"Error: {data['message']}")
    exit()
temperature = data["main"]["temp"]
humidity =data["main"]["humidity"]
weather = data["weather"][0]["main"]
wind_speed = data["wind"]["speed"]
feels_like = data["main"]["feels_like"]
description = data["weather"][0]["description"]
country=data["sys"]["country"]

print("\n========== Weather Report ==========")
print(f"City        : {city}, {country}")
print(f"Feels Like  : {feels_like} °C")
print(f"Humidity    : {humidity} %")
print(f"Weather     : {weather}")
print(f"Wind Speed  : {wind_speed} m/s")
print(f"Description: {description}")
print("======================================")
