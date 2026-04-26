import requests
import xml.etree.ElementTree as ET

def normalize_country_name(name):
    """Convert country codes or variants into proper country names."""
    name = name.strip().lower()

    # Common fixes
    replacements = {
        "usa": "united states",
        "us": "united states",
        "u.s.": "united states",
        "u.s.a": "united states",
        "uk": "united kingdom",
        "uae": "united arab emirates",
        "bahamas": "the bahamas",
        "gambia": "the gambia"
    }

    if name in replacements:
        return replacements[name]

    return name


def get_travel_advisory(country_name):
    """
    Retrieves travel advisory information from the U.S. State Department RSS feed.
    Returns advisory level and summary message.
    """

    url = "https://travel.state.gov/_res/rss/TAs.xml"

    try:
        response = requests.get(url)
        if response.status_code != 200:
            return {"error": "Failed to fetch advisory feed"}

        # Parse XML
        root = ET.fromstring(response.text)
        items = root.find("channel").findall("item")

        # Normalize input
        country_name = normalize_country_name(country_name)

        for item in items:
            title = item.find("title").text.lower()

            # Normalize title too
            title_clean = normalize_country_name(title)

            if country_name in title_clean:
                description = item.find("description").text

                # Extract advisory level
                if "level 4" in title:
                    level = 4
                elif "level 3" in title:
                    level = 3
                elif "level 2" in title:
                    level = 2
                else:
                    level = 1

                return {
                    "score": level,
                    "message": description
                }

        return {"error": "No advisory found for this country"}

    except Exception as e:
        return {"error": str(e)}
