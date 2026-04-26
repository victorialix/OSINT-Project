# OSINT Travel Planner

A Flask web application that lets users enter a city and get travel information. The app uses multiple APIs to gather weather, travel advisories, currency exchange rates, and generates a simple risk score and packing list. It also creates a weather chart and displays everything through a web-based GUI.

## Features
- City search
- 7-day weather forecast and average temperature
- Travel advisory information
- Currency exchange rate
- Risk score based on advisory, weather, and currency
- Auto-generated packing list
- Weather chart (PNG)
- Web GUI using HTML/CSS/JS

## How to Run
1. Install dependencies:
   pip install flask requests matplotlib

2. Run the app:
   python app.py

3. Open in browser:
   http://127.0.0.1:5000

## How It Works
- User enters a city
- App looks up coordinates
- Fetches weather, advisory, and currency data
- Calculates a travel score and risk level
- Generates a packing list
- Creates a weather chart
- Displays everything in the GUI

## Notes
- The GUI requirement is fulfilled through the web interface.
- Charts are generated server-side and saved as PNG files.
- Multiple APIs are used for real-time data.
