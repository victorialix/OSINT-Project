import requests

def get_city_info(city_name):
    """
    Uses GeoDB Cities API to get latitude, longitude, and country code.
    """

    url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"
    params = {"namePrefix": city_name}
    headers = {
        "X-RapidAPI-Key": "e158d9e616mshee4beb4ee098b4bp109869jsn90213cafe6f6",
        "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        data = response.json()

        if "data" not in data or len(data["data"]) == 0:
            return {"error": "City not found"}

        city = data["data"][0]

        return {
            "city": city["city"],
            "lat": city["latitude"],
            "lon": city["longitude"],
            "country_code": city["countryCode"]
        }

    except Exception as e:
        return {"error": str(e)}
