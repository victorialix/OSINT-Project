def compute_travel_score(advisory_score, weather, exchange_rate):
    """
    Combines advisory score, temperature, and exchange rate
    into a single travel score.
    Higher = better.
    """

    # Extract temperature in Celsius from weather API
    temp_c = weather["current"]["temperature"]

    # Convert to Fahrenheit
    temp_f = (temp_c * 9/5) + 32

    # Ideal travel temp ~72°F
    temp_factor = max(0, 30 - abs(temp_f - 72))

    # Exchange rate factor
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
    Creates a simple packing list based on Fahrenheit temperature and risk.
    """

    # Extract temp in Celsius, convert to Fahrenheit
    temp_c = weather["current"]["temperature"]
    temp_f = (temp_c * 9/5) + 32

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
