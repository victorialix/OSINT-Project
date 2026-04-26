from flask import Blueprint, request, jsonify

# These imports will work once Person A & B add their files.
# For now, they won't break anything if the files don't exist yet.
from api.city_api import get_city_info
from api.weather_api import get_weather
from api.advisory_api import get_travel_advisory
from api.currency_api import get_exchange_rate

from services.intelligence import (
    compute_travel_score,
    classify_risk,
    generate_packing_list
)

travel_bp = Blueprint("travel", __name__)

@travel_bp.get("/travel-info")
def travel_info():
    city = request.args.get("city")

    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    # Get city info (lat, lon, country)
    city_data = get_city_info(city)
    if "error" in city_data:
        return jsonify(city_data), 400

    # Get weather data
    weather = get_weather(city_data["lat"], city_data["lon"])
    if "error" in weather:
        return jsonify(weather), 500

    # Get travel advisory
    advisory = get_travel_advisory(city_data["country_code"])
    if "error" in advisory:
        return jsonify(advisory), 500

    # Get currency exchange rate
    currency = get_exchange_rate(city_data["country_code"])
    if "error" in currency:
        return jsonify(currency), 500

    # Intelligence logic
    score = compute_travel_score(advisory["score"], weather["avg_temp"], currency["rate"])
    risk = classify_risk(score)
    packing = generate_packing_list(weather["avg_temp"], risk)

    return jsonify({
        "city": city_data["city"],
        "country": city_data["country_code"],
        "avg_temp": weather["avg_temp"],
        "risk_level": risk,
        "advisory_message": advisory["message"],
        "exchange_rate": currency["rate"],
        "packing_list": packing
    })
