from flask import Blueprint, request, jsonify
from api.city_api import get_city_info
from api.advisory_api import get_travel_advisory
from api.currency_api import get_exchange_rate
from services.intelligence import compute_travel_score, classify_risk, generate_packing_list
from api.weather_api import get_weather
from services.charts import generate_temperature_chart

travel_bp = Blueprint("travel", __name__)

@travel_bp.route("/travel-info", methods=["GET"])
def travel_info():
    city = request.args.get("city")

    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    # 1️⃣ CITY LOOKUP
    city_data = get_city_info(city)
    if "error" in city_data:
        return jsonify(city_data), 400

    city_name = city_data["city"]
    country_name = city_data["country"]
    lat = city_data["lat"]
    lon = city_data["lon"]

    # 2️⃣ TRAVEL ADVISORY (uses COUNTRY NAME)
    advisory = get_travel_advisory(country_name)

    # Extract numeric advisory score safely
    advisory_score = advisory.get("score", 5)

    # 3️⃣ CURRENCY EXCHANGE RATE (uses COUNTRY NAME)
    currency = get_exchange_rate(country_name)

    # 4️⃣ WEATHER (uses LAT/LON)
    weather = get_weather(lat, lon)

    # 5️⃣ TRAVEL INTELLIGENCE
    score = compute_travel_score(advisory_score, weather, currency)
    risk = classify_risk(score)
    packing_list = generate_packing_list(weather, risk)

    # 6️⃣ CHART GENERATION
    chart_path = generate_temperature_chart(
        weather["max_temps"],
        weather["min_temps"],
        city_name
    )

    return jsonify({
        "city": city_name,
        "country": country_name,
        "advisory": advisory,
        "currency": currency,
        "weather": weather,
        "score": score,
        "risk": risk,
        "packing_list": packing_list,
        "chart": chart_path
    })
