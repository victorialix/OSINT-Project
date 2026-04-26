import os

GEODB_API_KEY = os.getenv("GEODB_API_KEY", "your_key_here")
EXCHANGE_API_KEY = os.getenv("EXCHANGE_API_KEY", "your_key_here")

GEODB_URL = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"
EXCHANGE_URL = "https://v6.exchangerate-api.com/v6"
ADVISORY_URL = "https://www.travel-advisory.info/api"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"
