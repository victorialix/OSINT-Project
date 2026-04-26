import requests
def get_exchange_rate(country_name):

    # Fetch all matching countries
    lookup_url = f"https://restcountries.com/v3.1/name/{country_name}"
    lookup_res = requests.get(lookup_url).json()

    if not isinstance(lookup_res, list):
        return {"error": "Country not found"}

    # Try to find the best match
    selected = None
    for c in lookup_res:
        official = c.get("name", {}).get("official", "").lower()
        common = c.get("name", {}).get("common", "").lower()

        if country_name.lower() == official or country_name.lower() == common:
            selected = c
            break

    # If no exact match, default to the first result
    if selected is None:
        selected = lookup_res[0]

    # Extract currency
    currencies = selected.get("currencies")
    if not currencies:
        return {"error": "Currency data unavailable"}

    currency_code = list(currencies.keys())[0]

    # Get exchange rate
    rate_url = "https://open.er-api.com/v6/latest/USD"
    rate_res = requests.get(rate_url).json()

    if "rates" not in rate_res or currency_code not in rate_res["rates"]:
        return {"error": "Exchange rate unavailable"}

    return {
        "country": selected["name"]["common"],
        "currency_code": currency_code,
        "rate": round(rate_res["rates"][currency_code], 3)
    }
