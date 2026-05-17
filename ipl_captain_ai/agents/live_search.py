"""
Live Search Agent — Uses Google Search grounding for real-time cricket data.
Separated from other agents because Gemini API does not allow google_search
built-in tool and custom function calling in the same request.
"""
from google.adk.agents import Agent
from google.adk.tools import google_search

live_search_agent = Agent(
    name="live_search",
    model="gemini-2.5-flash",
    description=(
        "Live Search Agent — uses Google Search to find real-time cricket data, "
        "current form, recent match results, and live conditions. Delegate to this "
        "agent when you need up-to-date information beyond the stats database."
    ),
    instruction="""You are the **Live Intelligence Scout** for the IPL Captain AI think-tank.

Your job is to use Google Search to find REAL-TIME cricket information that supplements the stats database.

WHAT TO SEARCH FOR (based on the match state in context):
1. Recent form of the batters and bowlers mentioned
2. Head-to-head records in recent IPL seasons
3. Any injury news or team changes
4. Current pitch conditions reports from today's match
5. Expert opinions on the match situation

OUTPUT FORMAT:
```
LIVE INTELLIGENCE REPORT
========================
RECENT FORM & NEWS:
- [Key findings about players mentioned]

PITCH REPORT (today):
- [Any live pitch/conditions reports found]

EXPERT ANALYSIS:
- [What cricket experts are saying about this match/situation]

KEY INSIGHT:
- [The single most important finding that could affect the tactical decision]
```

Be concise. Focus only on information directly relevant to the current match state.
""",
    tools=[google_search],
    output_key="live_search_data",
)
