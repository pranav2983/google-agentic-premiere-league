"""
Live Match Scraper Tool — Uses Gemini Google Search grounding to fetch live match state.
Stretch goal: paste a Cricbuzz/ESPNcricinfo URL and auto-extract match state.
"""


def scrape_live_match(url: str) -> dict:
    """Fetch live cricket match data from a Cricbuzz or ESPNcricinfo URL.

    This tool uses the URL to search for the latest match state via Google Search.
    The agent should use the Google Search grounding tool in conjunction to get
    real-time information from the provided URL.

    Args:
        url: The full URL from Cricbuzz or ESPNcricinfo match page
             (e.g., "https://www.cricbuzz.com/live-cricket-scores/12345/match-name")

    Returns:
        Dictionary with instructions for the agent to use Google Search
        to fetch and parse the live match data from the given URL.
    """
    source = "unknown"
    if "cricbuzz" in url.lower():
        source = "Cricbuzz"
    elif "espn" in url.lower() or "cricinfo" in url.lower():
        source = "ESPNcricinfo"

    return {
        "url": url,
        "source": source,
        "instruction": (
            f"Use Google Search to find the latest live score and match state from this {source} match. "
            f"URL: {url}. "
            "Extract: current score, overs, batting team, bowling team, "
            "current batters (on strike and non-strike), recent bowler figures, "
            "required run rate (if 2nd innings), and any recent wickets or milestones. "
            "Return this as structured match state data."
        ),
        "parse_guidance": {
            "look_for": [
                "Current score (runs/wickets)",
                "Overs completed",
                "Batting team name",
                "Bowling team name", 
                "Batter on strike (name and score)",
                "Batter at non-strike (name and score)",
                "Current bowler (name and figures)",
                "Required run rate (2nd innings)",
                "Target (2nd innings)",
                "Recent events (wickets, boundaries)",
            ]
        },
    }
