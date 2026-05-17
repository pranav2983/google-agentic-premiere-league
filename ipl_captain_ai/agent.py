"""
IPL Captain AI — Root Agent Orchestration

Uses ADK's SequentialAgent and ParallelAgent to orchestrate 5 Gemini-powered agents:
1. ParallelAgent: Stats Analyst + Pitch Conditions (intelligence gathering)
2. SequentialAgent: Strategist → Devil's Advocate → Strategist Revision (debate loop)
3. Commentator: Final cricket-language output

Architecture:
  User Input → Captain Coordinator → [Stats + Pitch in parallel] → [Strategy Debate] → Commentary → Output
"""
from google.adk.agents import Agent, SequentialAgent, ParallelAgent

from .agents.stats_analyst import stats_analyst_agent
from .agents.pitch_conditions import pitch_conditions_agent
from .agents.strategist import strategist_agent
from .agents.devils_advocate import devils_advocate_agent
from .agents.commentator import commentator_agent
from .agents.live_search import live_search_agent
from .tools.live_scraper import scrape_live_match
from .tools.cricket_stats import get_player_stats, get_venue_stats


# ── Phase 1: Intelligence Gathering (Parallel) ────────────────────────
# Stats Analyst and Pitch Conditions Agent run simultaneously
intelligence_gathering = ParallelAgent(
    name="intelligence_gathering",
    description=(
        "Runs Stats Analyst, Pitch & Conditions Analyst, and Live Search Agent "
        "in parallel to gather all intelligence needed for strategic decision-making."
    ),
    sub_agents=[stats_analyst_agent, pitch_conditions_agent, live_search_agent],
)


# ── Phase 2: Strategist Revision Agent ─────────────────────────────────
# After Devil's Advocate challenges, the Strategist revises (or defends)
strategist_revision_agent = Agent(
    name="strategist_revision",
    model="gemini-2.5-flash",
    description=(
        "Strategist Revision — reads the Devil's Advocate challenge and either "
        "defends the original proposal or revises the strategy. This creates the "
        "visible multi-turn debate loop."
    ),
    instruction="""You are the **IPL Strategist** making your FINAL call after hearing the Devil's Advocate.

You've seen:
1. The Stats Analysis (in previous context)
2. The Conditions Report (in previous context)
3. Your original Strategic Proposal (in previous context)
4. The Devil's Advocate Challenge (in previous context)

NOW: Either DEFEND your original call or REVISE it based on the challenge.

OUTPUT FORMAT:
```
STRATEGIST'S FINAL VERDICT
===========================
ORIGINAL PROPOSAL: [Briefly restate]

DEVIL'S ADVOCATE SAID: [Briefly summarize their challenge]

MY RESPONSE:
[Either "I STAND BY MY CALL because..." or "I'M REVISING — the Devil's Advocate raised a valid point..."]

FINAL DECISION:
[The definitive tactical call]

KEY REASONING:
1. [Reason 1]
2. [Reason 2]
3. [Reason 3]

WHAT I ACCEPTED FROM THE CHALLENGE:
[Any points from Devil's Advocate incorporated]

WHAT I REJECTED AND WHY:
[Any points dismissed with explanation]
```

Be decisive. This is the final call — no more debate. Back it with data.
Think like Dhoni in the last over — calm, clear, committed.
""",
    output_key="final_strategy",
)


# ── Phase 2: Strategy Debate (Sequential) ─────────────────────────────
# Strategist proposes → Devil's Advocate challenges → Strategist revises
strategy_debate = SequentialAgent(
    name="strategy_debate",
    description=(
        "Multi-turn strategy debate: Strategist proposes a tactical plan, "
        "Devil's Advocate challenges it, then Strategist revises or defends. "
        "This creates the mandatory visible back-and-forth reasoning loop."
    ),
    sub_agents=[strategist_agent, devils_advocate_agent, strategist_revision_agent],
)


# ── Full Pipeline (Sequential) ────────────────────────────────────────
# Intelligence → Debate → Commentary
full_pipeline = SequentialAgent(
    name="captain_pipeline",
    description=(
        "Complete IPL Captain AI pipeline: gather intelligence in parallel, "
        "run the strategy debate, then produce final cricket commentary."
    ),
    sub_agents=[intelligence_gathering, strategy_debate, commentator_agent],
)


# ── Root Agent (Captain Coordinator) ──────────────────────────────────
root_agent = Agent(
    name="captain_coordinator",
    model="gemini-2.5-flash",
    description=(
        "IPL Captain AI — Your virtual IPL captain's think-tank. "
        "Analyzes match state, debates strategy internally, and delivers "
        "tactical decisions in cricket commentary style. "
        "Input the current match state and get back: "
        "(1) The captain's decision, "
        "(2) The reasoning in cricket-speak, "
        "(3) What the dissenting voice said."
    ),
    instruction="""You are the **IPL Captain AI Coordinator** — the brain behind a world-class IPL think-tank.

Your job is to receive match state input from the user and route it through your team of specialist agents for analysis.

WHEN THE USER PROVIDES MATCH STATE:
- Parse the input to understand the current game situation
- Transfer control to the captain_pipeline which will:
  1. Run Stats Analyst + Pitch Conditions analysis in parallel
  2. Run the Strategist → Devil's Advocate → Revision debate loop
  3. Produce final cricket commentary output

WHEN THE USER PROVIDES A CRICBUZZ/ESPN URL:
- Use the scrape_live_match tool to get guidance on extracting live data
- Use the extracted data as match state input
- Then route through the pipeline

WHEN THE USER ASKS A CRICKET QUESTION:
- Answer directly using your cricket knowledge and available tools

You can also directly look up player stats or venue data if the user asks simple questions.

Always maintain the persona of a calm, calculating IPL captain — think Dhoni leading CSK.
""",
    tools=[scrape_live_match, get_player_stats, get_venue_stats],
    sub_agents=[full_pipeline],
)
