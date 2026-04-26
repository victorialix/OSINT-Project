import os
import matplotlib.pyplot as plt

def generate_temperature_chart(max_temps, min_temps, city_name):
    """
    Generates a temperature chart and saves it to static/charts/.
    Returns the relative file path so Flask can serve it.
    """

    # Ensure the charts directory exists
    charts_dir = os.path.join("static", "charts")
    os.makedirs(charts_dir, exist_ok=True)

    # Create the chart
    days = list(range(1, len(max_temps) + 1))

    plt.figure(figsize=(8, 4))
    plt.plot(days, max_temps, label="Max Temp (°C)", color="red")
    plt.plot(days, min_temps, label="Min Temp (°C)", color="blue")
    plt.title(f"Temperature Forecast for {city_name}")
    plt.xlabel("Day")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.grid(True)

    # Save chart
    filename = f"{city_name.lower().replace(' ', '_')}_chart.png"
    filepath = os.path.join(charts_dir, filename)
    plt.savefig(filepath)
    plt.close()

    # Return path for the frontend
    return f"/static/charts/{filename}"
