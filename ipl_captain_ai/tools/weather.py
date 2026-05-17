"""
Weather API Tool — Fetches real-time weather conditions for IPL match venues.
Uses OpenWeatherMap free API with fallback to simulated data.
"""
import os
import httpx

# Venue city mapping for weather API
VENUE_CITIES = {
    "wankhede": ("Mumbai", "IN"), "mumbai": ("Mumbai", "IN"),
    "chidambaram": ("Chennai", "IN"), "chepauk": ("Chennai", "IN"), "chennai": ("Chennai", "IN"),
    "chinnaswamy": ("Bengaluru", "IN"), "bengaluru": ("Bengaluru", "IN"), "bangalore": ("Bengaluru", "IN"),
    "eden": ("Kolkata", "IN"), "kolkata": ("Kolkata", "IN"),
    "narendra modi": ("Ahmedabad", "IN"), "motera": ("Ahmedabad", "IN"), "ahmedabad": ("Ahmedabad", "IN"),
    "arun jaitley": ("Delhi", "IN"), "kotla": ("Delhi", "IN"), "delhi": ("Delhi", "IN"),
    "rajiv gandhi": ("Hyderabad", "IN"), "uppal": ("Hyderabad", "IN"), "hyderabad": ("Hyderabad", "IN"),
    "sawai mansingh": ("Jaipur", "IN"), "jaipur": ("Jaipur", "IN"),
    "mohali": ("Mohali", "IN"), "bindra": ("Mohali", "IN"), "chandigarh": ("Mohali", "IN"),
    "dy patil": ("Navi Mumbai", "IN"),
    "lucknow": ("Lucknow", "IN"), "ekana": ("Lucknow", "IN"),
    "dharamsala": ("Dharamsala", "IN"),
    "guwahati": ("Guwahati", "IN"),
}

SIMULATED_WEATHER = {
    "Mumbai": {"temp_c": 32, "humidity": 78, "wind_kph": 14, "condition": "Partly Cloudy", "dew_likelihood": "High — heavy dew expected after 8pm, significant impact on bowling grip"},
    "Chennai": {"temp_c": 35, "humidity": 72, "wind_kph": 10, "condition": "Hot and Humid", "dew_likelihood": "Moderate — some dew possible, manageable for bowlers"},
    "Bengaluru": {"temp_c": 28, "humidity": 55, "wind_kph": 12, "condition": "Pleasant", "dew_likelihood": "Low — altitude keeps dew minimal, good for bowling throughout"},
    "Kolkata": {"temp_c": 33, "humidity": 82, "wind_kph": 8, "condition": "Humid", "dew_likelihood": "Very High — heavy dew from 7:30pm, second innings bowling severely affected"},
    "Ahmedabad": {"temp_c": 38, "humidity": 35, "wind_kph": 18, "condition": "Hot and Dry", "dew_likelihood": "Low — dry conditions, no significant dew impact"},
    "Delhi": {"temp_c": 36, "humidity": 45, "wind_kph": 15, "condition": "Hot", "dew_likelihood": "Moderate — dew sets in after 9pm, late matches affected"},
    "Hyderabad": {"temp_c": 34, "humidity": 60, "wind_kph": 11, "condition": "Warm", "dew_likelihood": "Moderate — some dew in second innings, manageable"},
    "Jaipur": {"temp_c": 37, "humidity": 30, "wind_kph": 20, "condition": "Hot and Windy", "dew_likelihood": "Low — desert climate keeps dew away"},
    "Mohali": {"temp_c": 30, "humidity": 65, "wind_kph": 13, "condition": "Pleasant Evening", "dew_likelihood": "High — evening games see significant dew, impacts bowling"},
}


def get_weather_conditions(venue_or_city: str) -> dict:
    """Get current weather conditions at a cricket match venue for tactical analysis.

    Args:
        venue_or_city: Name of the venue or city (e.g., "Wankhede", "Mumbai", "Chennai", "Eden Gardens")

    Returns:
        Dictionary with temperature, humidity, wind, conditions, and cricket-specific
        dew likelihood assessment for tactical decision-making.
    """
    # Resolve venue to city
    city = None
    venue_lower = venue_or_city.lower()
    for key, (city_name, _) in VENUE_CITIES.items():
        if key in venue_lower:
            city = city_name
            break

    if not city:
        city = venue_or_city.title()

    # Try real API first
    api_key = os.environ.get("OPENWEATHERMAP_API_KEY", "")
    if api_key and api_key != "optional_weather_api_key":
        try:
            resp = httpx.get(
                "https://api.openweathermap.org/data/2.5/weather",
                params={"q": f"{city},IN", "appid": api_key, "units": "metric"},
                timeout=5.0,
            )
            if resp.status_code == 200:
                data = resp.json()
                temp = data["main"]["temp"]
                humidity = data["main"]["humidity"]
                wind = data["wind"]["speed"] * 3.6  # m/s to kph

                # Cricket-specific dew assessment
                if humidity > 75:
                    dew = "High — heavy dew expected, bowling grip significantly affected"
                elif humidity > 55:
                    dew = "Moderate — some dew likely, slight impact on bowling"
                else:
                    dew = "Low — dry conditions, minimal dew impact"

                return {
                    "source": "live_api",
                    "city": city,
                    "temperature_c": round(temp, 1),
                    "humidity_pct": humidity,
                    "wind_kph": round(wind, 1),
                    "condition": data["weather"][0]["description"].title(),
                    "dew_likelihood": dew,
                    "cricket_impact": _assess_cricket_impact(temp, humidity, wind),
                }
        except Exception:
            pass  # Fall through to simulated data

    # Simulated fallback
    sim = SIMULATED_WEATHER.get(city, SIMULATED_WEATHER.get("Mumbai"))
    return {
        "source": "simulated",
        "city": city,
        "temperature_c": sim["temp_c"],
        "humidity_pct": sim["humidity"],
        "wind_kph": sim["wind_kph"],
        "condition": sim["condition"],
        "dew_likelihood": sim["dew_likelihood"],
        "cricket_impact": _assess_cricket_impact(sim["temp_c"], sim["humidity"], sim["wind_kph"]),
    }


def _assess_cricket_impact(temp: float, humidity: int, wind: float) -> str:
    """Assess how weather conditions affect cricket tactics."""
    impacts = []
    if temp > 35:
        impacts.append("Extreme heat — fatigue factor for fast bowlers, consider shorter spells")
    elif temp > 30:
        impacts.append("Hot conditions — rotation of pace bowlers important")

    if humidity > 75:
        impacts.append("High humidity — swing bowling favored, dew will be a major factor in 2nd innings")
    elif humidity > 55:
        impacts.append("Moderate humidity — some swing available, dew possible later")

    if wind > 15:
        impacts.append(f"Strong wind ({wind:.0f} kph) — affects flight of spinners, batters may target downwind boundary")
    elif wind > 10:
        impacts.append(f"Moderate breeze ({wind:.0f} kph) — slight advantage bowling into the wind")

    return " | ".join(impacts) if impacts else "Neutral conditions — no significant weather impact on tactics"
