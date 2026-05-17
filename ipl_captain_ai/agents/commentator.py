"""
Match Commentator Agent — Translates analysis into engaging cricket commentary.
No ML jargon — pure cricket talk that any fan would understand.
"""
from google.adk.agents import Agent

from ..prompts.system_prompts import COMMENTATOR_PROMPT

commentator_agent = Agent(
    name="commentator",
    model="gemini-2.5-flash",
    description=(
        "Match Commentator — takes the complete analysis (stats, conditions, strategy "
        "proposal, devil's advocate challenge) and presents the final decision as "
        "engaging, accessible cricket commentary. Think Ravi Shastri meets Harsha Bhogle."
    ),
    instruction=COMMENTATOR_PROMPT,
    output_key="final_commentary",
)
