"""
Stats Analyst Agent — Crunches IPL player data, matchups, and venue statistics.
Uses Player Stats Database tools for comprehensive cricket analytics.
"""
from google.adk.agents import Agent

from ..prompts.system_prompts import STATS_ANALYST_PROMPT
from ..tools.cricket_stats import get_player_stats, get_matchup_data, get_venue_stats

stats_analyst_agent = Agent(
    name="stats_analyst",
    model="gemini-2.5-flash",
    description=(
        "IPL Stats Analyst — looks up player statistics, head-to-head matchup data, "
        "and venue performance numbers. Delegate to this agent when you need hard "
        "numbers on batting strike rates, bowling economy, venue averages, or player form."
    ),
    instruction=STATS_ANALYST_PROMPT,
    tools=[get_player_stats, get_matchup_data, get_venue_stats],
    output_key="stats_analysis",
)
