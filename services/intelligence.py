def compute_travel_score(advisory_score, avg_temp, exchange_rate):
    """
    Combines advisory score, temperature, and exchange rate
    into a single travel score.
    Higher = better.
    """
    temp_factor = max(0, 30 - abs(avg_temp - 22))  # ideal temp ~22°C
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


def generate_packing_list(avg_temp, risk_level):
    """
    Creates a simple packing list based on weather and risk.
    """
    items = ["Passport", "Phone Charger", "Travel Documents"]

    if avg_temp < 10:
        items.append("Warm Jacket")
    elif avg_temp < 20:
        items.append("Light Jacket")
    else:
        items.append("T-Shirts")

    if risk_level == "High Risk":
        items.append("Emergency Kit")
        items.append("Extra Medication")

    return items
