import requests

def get_weather(lat, lon):
    """
    Retrieves 7-day weather forecast (max/min temps) from Open-Meteo.
    """

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": "temperature_2m_max,temperature_2m_min",
        "timezone": "auto"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if "daily" not in data:
            return {"error": "Weather data unavailable"}

        max_temps = data["daily"]["temperature_2m_max"]
        min_temps = data["daily"]["temperature_2m_min"]

        # Compute average temperature for intelligence scoring
        avg_temp = sum(max_temps) / len(max_temps)

        return {
            "max_temps": max_temps,
            "min_temps": min_temps,
            "avg_temp": round(avg_temp, 2)
        }

    except Exception as e:
        return {"error": str(e)}
