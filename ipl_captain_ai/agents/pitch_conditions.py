"""
Pitch & Conditions Agent — Analyzes weather, dew, pitch behavior, and venue factors.
Uses Weather API tool and Venue Stats for conditions analysis.
"""
from google.adk.agents import Agent

from ..prompts.system_prompts import PITCH_CONDITIONS_PROMPT
from ..tools.weather import get_weather_conditions
from ..tools.cricket_stats import get_venue_stats

pitch_conditions_agent = Agent(
    name="pitch_conditions",
    model="gemini-2.5-flash",
    description=(
        "Pitch & Conditions Analyst — assesses weather, dew factor, pitch type, "
        "and venue characteristics. Delegate to this agent when you need to understand "
        "how conditions will affect bowling, batting, and field placement decisions."
    ),
    instruction=PITCH_CONDITIONS_PROMPT,
    tools=[get_weather_conditions, get_venue_stats],
    output_key="pitch_analysis",
)
