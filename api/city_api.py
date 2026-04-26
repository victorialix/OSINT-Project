import requests

def get_city_info(city_name):
    """
    Uses Open-Meteo Geocoding API to get city, country, latitude, and longitude.
    No API key required.
    """

    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city_name, "count": 1}

    try:
        response = requests.get(url)
        data = response.json()

        # If no results found
        if "results" not in data or len(data["results"]) == 0:
            return {"error": "City not found"}

        city = data["results"][0]

        return {
            "city": city.get("name"),
            "country": city.get("country"),
            "lat": city.get("latitude"),
            "lon": city.get("longitude")
        }

    except Exception as e:
        return {"error": str(e)}
