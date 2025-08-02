# Weather App

A dual-version weather app that displays real-time weather data using the OpenWeatherMap API.

---

# Project Versions

# 1.  CLI Version (Python)

A terminal-based weather app built using Python and the `requests` library.

-  Real-time weather data
-  Simple CLI interaction
-  Uses OpenWeatherMap API

### 2.  Web Version (HTML, CSS, JS)

A fully responsive and interactive web-based weather app.

-  City-based weather search
-  Displays temperature, humidity, wind, and condition
-  Modern UI with clean styling
-  Fetches live data using Fetch API

---



# Tech Stack

| Version | Stack |
|--------|-------|
| CLI    | Python, requests, terminal |
| Web    | HTML, CSS, JavaScript (Fetch API) |

---

## 🔑 API Key Setup

Both versions use [OpenWeatherMap API](https://openweathermap.org/api).  
You’ll need to **get a free API key** and add it as shown below:

### In Python CLI (`weather_cli.py`)
```python
API_KEY = "YOUR_API_KEY_HERE"
