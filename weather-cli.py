import requests
from datetime import datetime

API_KEY = "21d9f5f83c8341f45c6fe94750b10a7d"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        main = data['main']
        weather = data['weather'][0]
        wind = data['wind']
        sys = data['sys']
        coord = data['coord']

        sunrise = datetime.fromtimestamp(sys['sunrise']).strftime('%I:%M %p')
        sunset = datetime.fromtimestamp(sys['sunset']).strftime('%I:%M %p')

        print(f"\n🌍 Weather in {city.title()}, {sys['country']}:")
        print("──────────────────────────────")
        print(f"🌡️ Temperature     : {main['temp']}°C (Feels like {main['feels_like']}°C)")
        print(f"🌤️ Condition       : {weather['main']} - {weather['description'].capitalize()}")
        print(f"💧 Humidity        : {main['humidity']}%")
        print(f"🔽 Pressure        : {main['pressure']} hPa")
        print(f"💨 Wind Speed      : {wind['speed']} m/s")
        print(f"🌅 Sunrise         : {sunrise}")
        print(f"🌇 Sunset          : {sunset}")
        print(f"📍 Coordinates     : Latitude {coord['lat']}, Longitude {coord['lon']}")
        print("──────────────────────────────\n")

    else:
        if data.get("message"):
            print(f"\n❌ Error: {data['message'].capitalize()}\n")
        else:
            print("\n❌ Something went wrong.\n")

# Run the weather app
while True:
    city = input("Enter city name (or type 'exit' to quit): ")
    if city.lower() == 'exit':
        print("Goodbye! 👋")
        break
    get_weather(city)
