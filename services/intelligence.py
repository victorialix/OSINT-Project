def compute_travel_score(advisory_score, weather, currency):
    """
    advisory_score = number
    weather = { avg_temp, max_temps, min_temps }
    currency = { currency_code, rate } OR { error }
    """

    # Handle currency API failure safely
    if "rate" not in currency:
        exchange_rate = 1.0  # neutral fallback
    else:
        exchange_rate = currency["rate"]

    # Convert Celsius → Fahrenheit using avg_temp from weather_api
    temp_f = (weather["avg_temp"] * 9/5) + 32

    # Ideal travel temp ~72°F
    temp_factor = max(0, 30 - abs(temp_f - 72))

    # Exchange factor (cheaper currency = better)
    exchange_factor = 1 / exchange_rate if exchange_rate > 0 else 0

    score = (advisory_score * 0.5) + (temp_factor * 0.3) + (exchange_factor * 0.2)
    return round(score, 2)


def classify_risk(score):
    """
    Converts the travel score into a risk category.
    """
    if score >= 7:
        return "Low Risk"
    elif score >= 4:
        return "Moderate Risk"
    else:
        return "High Risk"


def generate_packing_list(weather, risk_level):
    """
    weather = { avg_temp, max_temps, min_temps }
    """

    # Convert Celsius → Fahrenheit
    temp_f = (weather["avg_temp"] * 9/5) + 32

    items = ["Passport", "Phone Charger", "Travel Documents"]

    # Clothing logic in Fahrenheit
    if temp_f < 50:
        items.append("Warm Jacket")
    elif temp_f < 68:
        items.append("Light Jacket")
    else:
        items.append("T-Shirts")

    if risk_level == "High Risk":
        items.append("Emergency Kit")
        items.append("Extra Medication")

    return items
