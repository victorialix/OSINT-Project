from flask import Blueprint, request, jsonify
from api.city_api import get_city_info
from api.weather_api import get_weather
from services.charts import generate_temperature_chart

chart_bp = Blueprint("charts", __name__)

@chart_bp.get("/weather-chart")
def weather_chart():
    city = request.args.get("city")

    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    # Get city info
    city_data = get_city_info(city)
    if "error" in city_data:
        return jsonify(city_data), 400

    # Get weather data
    weather = get_weather(city_data["lat"], city_data["lon"])
    if "error" in weather:
        return jsonify(weather), 500

    # Generate chart
    chart_path = generate_temperature_chart(
        weather["max_temps"],
        weather["min_temps"],
        city_data["city"]
    )

    return jsonify({"chart_url": chart_path})
