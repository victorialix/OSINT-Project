import requests

def get_travel_advisory(country_code):
    url = f"https://www.travel-advisory.info/api?countrycode={country_code}"

    try:
        response = requests.get(url, verify=False)
        data = response.json()

        if "data" not in data or country_code not in data["data"]:
            return {"error": "Advisory data unavailable"}

        advisory = data["data"][country_code]["advisory"]

        return {
            "score": advisory.get("score", 0),
            "message": advisory.get("message", "No advisory message available")
        }

    except Exception as e:
        return {"error": str(e)}
