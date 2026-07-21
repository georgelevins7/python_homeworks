import requests

city = input("Enter city: ")

coords_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"

weather_url = "https://api.open-meteo.com/v1/forecast"

coords_data = requests.get(coords_url).json()
try:
    latitude = coords_data["results"][0]["latitude"]
    longitude = coords_data["results"][0]["longitude"]


    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m",
        "timezone": "auto"
    }

    weather_data = requests.get(weather_url, params=params).json()

    time = weather_data["current"]["time"]
    temperature = weather_data["current"]["temperature_2m"]
    wind = weather_data["current"]["wind_speed_10m"]

    print(f"City: {city}\nTemperature: {temperature}\nWind Speed: {wind}\nTime: {time}")

except KeyError:
    print("City not found")