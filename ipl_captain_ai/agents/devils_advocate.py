"""
Devil's Advocate Agent — Challenges every strategic proposal with counter-arguments.
Ensures the final decision is battle-tested, not a rubber stamp.
Uses win probability tool to back up counter-proposals.
"""
from google.adk.agents import Agent

from ..prompts.system_prompts import DEVILS_ADVOCATE_PROMPT
from ..tools.win_probability import calculate_win_probability
from ..tools.cricket_stats import get_matchup_data

devils_advocate_agent = Agent(
    name="devils_advocate",
    model="gemini-2.5-flash",
    description=(
        "Devil's Advocate — challenges and stress-tests the Strategist's tactical proposal. "
        "Finds flaws, proposes alternatives, and ensures the final decision is robust. "
        "Delegate to this agent AFTER the Strategist has made a proposal."
    ),
    instruction=DEVILS_ADVOCATE_PROMPT,
    tools=[calculate_win_probability, get_matchup_data],
    output_key="devils_dissent",
)
