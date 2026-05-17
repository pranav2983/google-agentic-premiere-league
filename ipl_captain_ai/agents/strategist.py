"""
Strategist Agent — Proposes tactical decisions like a Dhoni-level captain.
Reads stats + conditions analysis and formulates the game plan.
Uses win probability tool for data-backed decisions.
"""
from google.adk.agents import Agent

from ..prompts.system_prompts import STRATEGIST_PROMPT
from ..tools.win_probability import calculate_win_probability
from ..tools.cricket_stats import get_matchup_data

strategist_agent = Agent(
    name="strategist",
    model="gemini-2.5-flash",
    description=(
        "IPL Strategist — proposes specific tactical decisions: bowling changes, "
        "batting order, field placements, strategic timeouts, and impact player usage. "
        "Delegate to this agent after stats and conditions analysis is complete."
    ),
    instruction=STRATEGIST_PROMPT,
    tools=[calculate_win_probability, get_matchup_data],
    output_key="strategy_proposal",
)
