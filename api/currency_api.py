import requests

def get_exchange_rate(country_code):
    """
    Retrieves the exchange rate for the country's currency relative to USD.
    Uses ExchangeRate API (no key required).
    """

    # First, get the currency code for the country
    currency_lookup_url = f"https://restcountries.com/v3.1/alpha/{country_code}"

    try:
        lookup_res = requests.get(currency_lookup_url)
        lookup_data = lookup_res.json()

        if not isinstance(lookup_data, list) or "currencies" not in lookup_data[0]:
            return {"error": "Currency data unavailable"}

        # Extract currency code (e.g., EUR, JPY, GBP)
        currency_code = list(lookup_data[0]["currencies"].keys())[0]

    except Exception as e:
        return {"error": f"Currency lookup failed: {str(e)}"}

    # Now get the exchange rate relative to USD
    rate_url = f"https://open.er-api.com/v6/latest/USD"

    try:
        rate_res = requests.get(rate_url)
        rate_data = rate_res.json()

        if "rates" not in rate_data or currency_code not in rate_data["rates"]:
            return {"error": "Exchange rate unavailable"}

        rate = rate_data["rates"][currency_code]

        return {
            "currency_code": currency_code,
            "rate": round(rate, 3)
        }

    except Exception as e:
        return {"error": f"Exchange rate fetch failed: {str(e)}"}
